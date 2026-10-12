# note_corp

note（note.com）でのコンテンツ販売を事業とする会社の運営リポジトリ。
人間は CEO の1人だけで、そのほかの部署は Claude Code のエージェントが担当する。

- 組織図・決裁権限・会議体: [`org/README.md`](org/README.md)
- ミッション・バリュー: [`org/charter.md`](org/charter.md)

> ⚠️ このリポジトリは **Private** で運用すること。機密情報は `private/` に置く（Git の管理対象外）。

## 使い方（Claude Code）

| コマンド | 内容 |
|---|---|
| `/weekly-meeting` | 週次定例。全部署の状況を集め、議事録と CEO の決裁待ちリストを作る |
| `/plan-ideas [テーマ]` | 企画会議。企画書を3本作り、CEO に採用を諮る |
| `/produce-article <slug>` | 採用済みの企画を、執筆 → 品質審査 → 告知準備まで進める |
| `/monthly-review [YYYY-MM]` | 月次経営会議。損益と来月の方針をまとめる |

部署（エージェント）: `planner`（企画部）/ `writer`（制作部）/ `editor`（編集・品質部）/ `marketer`（マーケティング部）/ `analyst`（分析部・財務）

## 記事の流れ

```
企画書(proposed) ─CEO採用→ adopted ─→ 記事 draft ─→ review ─合格→ ready ─CEOが公開→ published
  企画部                          制作部      編集・品質部        マーケティング部が告知文を作成
                                     ↑___不合格（差し戻しは最大2回）___|
```

## ディレクトリ構成

| パス | 内容 | 担当部署 |
|---|---|---|
| `org/` | 組織図・憲章・役割・意思決定ログ・議事録 | COO |
| `.claude/agents/` | 部署ごとのエージェント定義 | — |
| `.claude/commands/` | 会議・制作ラインのコマンド | — |
| `strategy/` | 事業計画・ペルソナ・KPI | 企画部 / 分析部 |
| `content/ideas/` | ネタ帳（`backlog.md`）と企画書（`proposals/`） | 企画部 |
| `content/drafts/` | 制作中の記事（1記事 = 1フォルダ。`article.md` と `review.md`） | 制作部 / 編集・品質部 |
| `content/published/` | 公開済みの記事 | COO |
| `content/magazines/` | マガジンの定義 | 企画部 |
| `products/` | 商品ラインナップと価格 | 企画部 |
| `marketing/` | 告知文・発信カレンダー | マーケティング部 |
| `analytics/` | 売上・経費・月次レポート | 分析部 |
| `templates/` | 企画書・記事・審査・月次レポートなどの雛形 | — |
| `ops/` | 運営カレンダー・利用ツール | COO |
| `scripts/` | 補助スクリプト（`new-article.sh`） | — |
| `private/` | 機密情報（Git の管理対象外） | CEO |
