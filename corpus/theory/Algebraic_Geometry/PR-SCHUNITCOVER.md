---
schema: qual/card@1
id: PR-SCHUNITCOVER
kind: proposition
title: Distinguished opens cover exactly when the functions generate the unit ideal
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Zariski Topology
  - Open Covers
relations:
- kind: uses
  target: D-AN662
review: draft
prompts:
- Show that $\{f_i\}$ generate the unit ideal of $R$ if and only if the $D(f_i)$ cover $\Spec R$.
---

::: {.proposition}
Let $R$ be a ring and $\{f_i\}_{i \in I}$ elements of $R$.
Then $\bigcup_i D(f_i) = \Spec R$ if and only if the $f_i$ generate the unit ideal.
In that case finitely many of the $f_i$ already generate it, so $\Spec R$ is quasicompact.
:::

