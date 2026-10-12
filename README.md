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
| `/run-500yen-line [本数] [ジャンル]` | 500円ライン。リサーチ → テーマ → タイトル → 執筆 → 検品まで複数本まとめて作る |
| `/monthly-review [YYYY-MM]` | 月次経営会議。損益と来月の方針をまとめる |

部署（エージェント）: `planner`（企画部）/ `writer`（制作部）/ `editor`（編集・品質部）/ `marketer`（マーケティング部）/ `analyst`（分析部・財務）

## 記事の流れ

```
企画書(proposed) ─CEO採用→ adopted ─→ 記事 draft ─→ review ─合格→ ready ─CEOが公開→ published
  企画部                          制作部      編集・品質部        マーケティング部が告知文を作成
                                     ↑___不合格（差し戻しは最大2回）___|
```

### 500円ライン
朝8時の X 巡回ルーティン（PC 上、`ops/routines/x-scan-daily.md`）の結果や、CEO が見つけた読者の悩みを `content/runs/inbox/` に置いて `/run-500yen-line` を実行すると、リサーチ → テーマ → タイトル → 執筆 → 検品まで進み、`ready` の記事がそろう。詳細は `org/playbooks/500yen-line.md`。

## ディレクトリ構成

| パス | 内容 | 担当部署 |
|---|---|---|
| `org/` | 組織図・憲章・役割・意思決定ログ・議事録 | COO |
| `.claude/agents/` | 部署ごとのエージェント定義 | — |
| `.claude/commands/` | 会議・制作ラインのコマンド | — |
| `strategy/` | 事業計画・ペルソナ・KPI | 企画部 / 分析部 |
| `content/ideas/` | ネタ帳（`backlog.md`）と企画書（`proposals/`） | 企画部 |
| `content/runs/` | 500円ラインの実行記録（テーマ・タイトル・レポート）と、リサーチ素材の受け取り口 `inbox/` | 企画部 / COO |
| `content/drafts/` | 制作中の記事（1記事 = 1フォルダ。`article.md` と `review.md`） | 制作部 / 編集・品質部 |
| `content/published/` | 公開済みの記事 | COO |
| `content/magazines/` | マガジンの定義 | 企画部 |
| `products/` | 商品ラインナップと価格 | 企画部 |
| `marketing/` | 告知文・発信カレンダー | マーケティング部 |
| `analytics/` | 売上・経費・月次レポート | 分析部 |
| `templates/` | 企画書・記事・審査・月次レポートなどの雛形 | — |
| `ops/` | 運営カレンダー・利用ツール・PC 上のルーティンの説明（`routines/`） | COO |
| `scripts/` | `new-article.sh`（記事フォルダの作成）、`check-article.py`（禁止語・有料ライン・字数のチェック） | — |
| `private/` | 機密情報（Git の管理対象外） | CEO |
