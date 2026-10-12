# 朝8時の X 巡回ルーティン

X の巡回は CEO の PC 上で動く予定タスク（Claude デスクトップアプリの「Scheduled」）が担当する。
X を読むにはログイン済みの Chrome が必要なため、クラウドのセッションやエージェントでは代わりに行えない。

| 項目 | 内容 |
|---|---|
| タスク ID | `note-factory-daily` |
| 実行 | 毎朝8時ごろ（PC 上でアプリが起動しているときだけ） |
| 定義ファイル | `C:\Users\<ユーザー>\.claude\scheduled-tasks\note-factory-daily\SKILL.md`（PC 上） |
| 作業フォルダ | `C:\Users\<ユーザー>\Documents\New project\note_factory` |
| 担当 | X の巡回（ネタ拾い）だけ。定義は `note_factory/agents/01_neta_hiroi.md` |
| 出力 | `note_factory/runs/YYYY-MM-DD/01_themes.md` |

## 500円ラインとのつなぎ方
ルーティンの `01_themes.md`（X の悩み投稿50本から選んだ10テーマ）を、500円ラインの **最優先のリサーチ素材** として使う。

1. ルーティンの `runs/YYYY-MM-DD/01_themes.md` を、このリポジトリの `content/runs/inbox/x-scan-YYYY-MM-DD.md` にコピーする
2. `/run-500yen-line` を実行する。企画部は `x-scan-*.md` を最初に読み、そのテーマから選ぶ（足りないときだけ WebSearch で補う）

ルーティンの形式（`## テーマ01:` / 読者像 / 悩みの核心 / 答えの骨子 / 根拠 / 鮮度リスク）は、500円ラインの `01_themes.md` と同じ項目なので、そのまま読める。

## 運用上の注意（元スレッドでの実績）
- 初回の実行（2026-09-20 8:05）は、最初の Bash 実行で権限の承認待ちになって止まり、成果物は0件だった
- 止まったセッションが「実行中」のまま残ると、翌日の実行も「already running」で始まらない
- 対処: サイドバーで止まっているセッションを **Stop** → **Run now** を押して、出てくる承認（Bash・Chrome 操作・ファイル書き込み）を一度許可する。許可はタスクに保存され、翌日以降も使われる

## 役割分担（2026-10-12 CEO 決定: A案）
ルーティンは X の巡回（①）だけを行う。②タイトル・③執筆・④検品は、このリポジトリの部署が 500円ラインとして行う。
`note_factory/agents/` の `02_title.md` / `03_shippitsu.md` / `04_kenpin.md` は使わない（中身は `org/playbooks/500yen-line.md` に取り込み済み）。

### 切り替え手順（CEO が PC 上で行う）
1. `C:\Users\<ユーザー>\.claude\scheduled-tasks\note-factory-daily\SKILL.md` を開き、先頭の `---` で囲まれた部分（name / description）は残して、本文を下の「SKILL.md 本文」に差し替える
2. description を「X の悩み投稿を50本読み、500円note向けのテーマを10個選ぶ」に変える
3. サイドバーで止まっているセッションがあれば **Stop** → **Run now** を押し、承認を一度許可する
4. `runs/<日付>/01_themes.md` ができたことを確認する

### SKILL.md 本文

```
500円noteのネタ拾い（X巡回）だけを行う。作業フォルダは `C:\Users\<ユーザー>\Documents\New project\note_factory`。

1. 今日の日付で `runs/YYYY-MM-DD/` を作る（既にあれば `runs/YYYY-MM-DD_2/`）
2. `agents/01_neta_hiroi.md` を全文読み、その手順・基準・禁止・出力形式どおりに `runs/YYYY-MM-DD/01_themes.md` を作る
3. 各テーマに `- slug:`（半角英小文字・数字・ハイフン）の行を足す
4. タイトル・執筆・検品は行わない

X の読み方: Claude in Chrome（ユーザーのログイン済み X）を使う。使えなければ内蔵ブラウザ、それも不可なら WebSearch で代わりに行い、そのことを書く。
X では閲覧と検索だけを行い、投稿・いいね・フォロー・DM・設定変更はしない。ログインを求められたら自分で入力せず、その旨を書いて代わりの手段に切り替える。

読んでいない投稿を件数に入れない。50本に届かなければ実数を書く。前日以前の `runs/` を見て、直近7日と同じテーマは避ける。
最後に、読んだ件数・取得手段・10テーマを結論から短く日本語で報告する。
```
