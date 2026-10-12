---
description: 月次経営会議。前月の数値をまとめて損益と来月の方針をCEOに諮る
argument-hint: [YYYY-MM]
---

COO として月次経営会議を進めてください。対象月: $ARGUMENTS（指定がなければ前月）

1. 対象月の数値（note の売上・ビュー・フォロワー・経費）がそろっているか確認する。足りなければ CEO に依頼して止める
2. analyst エージェントに `analytics/monthly/<YYYY-MM>.md` を作らせる
3. planner エージェントに、レポートをもとにした来月の企画方針案を出させる
4. 来月の KPI と重点施策の案を CEO に提示する。決まったことは `org/decision-log.md` に記録する
