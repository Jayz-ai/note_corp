#!/usr/bin/env python3
"""記事の機械チェック（禁止語・有料ライン・字数）。

usage: scripts/check-article.py <article.md> [<article.md> ...]

- 禁止語（保証表現・時期依存の表現）を全件出す。HTML コメントは対象外、frontmatter の title は対象
- 有料記事（type: paid）は `<!-- ここから有料 -->` が1つだけあることを確認する
- 500円ライン（line: 500yen）は字数も確認する（全体 3,800〜4,200字、無料部分 600〜1,000字）
エラーが1件でもあれば終了コード1を返す。
"""
import re
import sys

PAYWALL = "<!-- ここから有料 -->"

# (パターン, 種別)
BANNED = [
    (r"絶対", "保証"),
    (r"必ず", "保証"),
    (r"100\s*[%％]", "保証"),
    (r"確実に", "保証"),
    (r"間違いなく", "保証"),
    (r"誰でも", "保証"),
    (r"一生", "保証"),
    (r"保証", "保証"),
    (r"稼げる", "保証"),
    (r"(?:19|20)\d\d\s*年", "時期依存"),
    (r"令和\s*\d", "時期依存"),
    (r"最新", "時期依存"),
    (r"今年|去年|昨年|来年", "時期依存"),
    (r"今話題|話題の", "時期依存"),
    (r"最近", "時期依存"),
    (r"(?:今|これから)の時代", "時期依存"),
]

LINE_500 = {"total": (3800, 4200), "free": (600, 1000)}


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text, 0
    meta = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^(\w+):\s*(.*?)\s*(?:#.*)?$", line)
        if kv:
            meta[kv.group(1)] = kv.group(2).strip('"')
    offset = m.group(0).count("\n")
    return meta, text[m.end():], offset


def strip_comments(s):
    # 行番号を保つため、コメントは同じ数の改行に置き換える
    return re.sub(r"<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"), s, flags=re.S)


def count_chars(s):
    s = strip_comments(s)
    s = re.sub(r"^#+\s*", "", s, flags=re.M)  # 見出し記号
    return len(re.sub(r"\s", "", s))


def check(path):
    text = open(path, encoding="utf-8").read()
    meta, body, offset = split_frontmatter(text)
    errors = []

    # 禁止語: title と本文
    targets = [("title", meta.get("title", ""))]
    for i, line in enumerate(strip_comments(body).splitlines(), start=offset + 1):
        targets.append((f"L{i}", line))
    hits = []
    for where, line in targets:
        for pat, kind in BANNED:
            for m in re.finditer(pat, line):
                hits.append(f"  [{kind}] {where}: 「{m.group(0)}」 … {line.strip()[:60]}")
    if hits:
        errors.append(f"禁止語 {len(hits)}件")

    # 有料ライン
    n_pw = body.count(PAYWALL)
    if meta.get("type") == "paid" and n_pw != 1:
        errors.append(f"有料ライン `{PAYWALL}` が {n_pw} 個（1個であること）")

    free, _, _ = body.partition(PAYWALL)
    total_n, free_n = count_chars(body), count_chars(free)
    lines = [f"== {path}", f"字数: 全体 {total_n} / 無料部分 {free_n}"]
    if meta.get("line") == "500yen":
        lo, hi = LINE_500["total"]
        if not lo <= total_n <= hi:
            errors.append(f"全体の字数 {total_n} が {lo}〜{hi} の範囲外")
        lo, hi = LINE_500["free"]
        if not lo <= free_n <= hi:
            errors.append(f"無料部分の字数 {free_n} が {lo}〜{hi} の範囲外")

    lines.append(f"禁止語: {len(hits)}件")
    lines += hits
    lines.append("判定: " + ("OK" if not errors else "NG（" + " / ".join(errors) + "）"))
    print("\n".join(lines))
    return not errors


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    ok = all([check(p) for p in argv[1:]])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
