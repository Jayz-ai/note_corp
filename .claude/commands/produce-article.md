---
description: 記事制作ライン。採用済みの企画を執筆→品質審査→告知準備まで進める
argument-hint: <slug>
---

COO として、企画 `$ARGUMENTS` の記事を制作ラインに流してください。

1. `content/ideas/proposals/$ARGUMENTS.md` の status が `adopted` であることを確認する。違う場合は止めて、CEO に確認する
2. writer エージェントに執筆させる
3. editor エージェントに審査させる
4. 不合格なら writer に差し戻す（最大2回）。それでも不合格なら止めて CEO に判断を求める
5. 合格（status: `ready`）したら、marketer エージェントに告知文を作らせる
6. CEO に報告する: 記事のパス、点数、残っている `【CEO確認】`、公開手順（`templates/launch-checklist.md`）

途中で `【CEO確認】` が残った場合は、まとめて CEO に質問し、回答を writer に渡す。
