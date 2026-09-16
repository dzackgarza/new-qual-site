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

::: {.proof}
1. $\bigcup_i D(f_i) = \Spec R \setminus V((f_i)_{i \in I})$, since a prime avoids some $f_i$ exactly when it does not contain the ideal they generate.
2. $V(J) = \emptyset$ exactly when $J = R$, because every proper ideal lies in a maximal ideal, which is a prime.
3. If $1 = \sum_{i \in F} r_i f_i$, the sum is finite, so the finitely many $D(f_i)$ with $i \in F$ cover $\Spec R$.
:::
