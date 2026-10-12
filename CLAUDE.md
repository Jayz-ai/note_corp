# CLAUDE.md

note販売の1人会社の運営リポジトリ。コードより文章・運営ドキュメントが中心。

## 規約
- 文章は日本語。ファイル名・フォルダ名は半角英数字とハイフン（スクリプトで扱うため）。
- 記事は `content/drafts/YYYY-MM-DD-<slug>/article.md` に1記事1フォルダ。画像は同フォルダの `images/`。
- 記事の frontmatter（title / status / price / magazine / tags / url / published_at）は必ず維持する。
  - status: `idea` → `draft` → `review` → `published`
- 新規記事は `scripts/new-article.sh` で作成する（手作りしない）。
- 販売記事の執筆・添削時は note-storyteller-sales スキルの構成に従う。
- 個人情報・口座・取引先情報・領収書は `private/`（gitignore済み）以外に書かない。
- 売上数値は `analytics/sales-log.csv` に集計値のみ記録（購入者の個人情報は書かない）。
