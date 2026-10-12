# note_corp

note（note.com）でのコンテンツ販売を主事業とする1人会社の運営リポジトリ。
記事の企画〜公開、販売分析、会社運営（法務・経理・税務）をすべてここで管理する。

> ⚠️ このリポジトリは **Private** で運用すること。個人情報・口座情報・領収書は `private/` に置き、Git管理しない。

## ディレクトリ構成

| パス | 用途 |
|---|---|
| `company/` | 会社情報・法務（特商法表記・設立）・経理・税務 |
| `strategy/` | 事業計画・ペルソナ・商品ラインナップ・KPI |
| `content/ideas/` | ネタ帳（バックログ） |
| `content/drafts/` | 執筆中の記事（1記事 = 1フォルダ） |
| `content/published/` | 公開済み記事（公開後に drafts から移動） |
| `content/magazines/` | マガジン（記事のまとめ売り・定期購読）定義 |
| `templates/` | 記事・マガジン・公開チェックリスト・月次レビューの雛形 |
| `products/` | 商品ラインナップと価格設計 |
| `marketing/` | 集客（X / Threads / LINE 等）と発信カレンダー |
| `analytics/` | 売上ログ・月次レポート |
| `ops/` | 週次ルーティン・利用ツール一覧 |
| `scripts/` | 補助スクリプト |
| `private/` | Git管理外（機密情報置き場） |

## 記事制作フロー

```
ネタ出し → 下書き作成 → セルフレビュー → 公開 → 告知 → 数値記録
ideas/      drafts/       チェックリスト    published/  marketing/  analytics/
```

1. `content/ideas/backlog.md` にネタを追加（または GitHub Issue「記事企画」で起票）
2. `scripts/new-article.sh <slug> [paid|free]` で下書きフォルダを作成
3. `templates/launch-checklist.md` で公開前チェック
4. 公開したら frontmatter の `status` / `url` / `published_at` を更新し、`content/published/` へ `git mv`
5. 月末に `templates/monthly-review.md` を `analytics/monthly/YYYY-MM.md` にコピーして振り返り

## ブランチ運用

- `main`: 公開済み・確定した内容
- 作業ブランチ: `article/<slug>`、`ops/<topic>` など。PR でセルフレビューしてマージ
