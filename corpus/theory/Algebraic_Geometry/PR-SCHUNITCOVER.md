---
schema: qual/card@1
id: PR-SCHUNITCOVER
kind: proposition
title: Distinguished opens cover exactly when the functions generate the unit ideal
slogan: 'Distinguished opens cover $\Spec R$ exactly when their defining functions generate $1$; a finite subcover is already hidden in that equation.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Zariski Topology
  - Open Covers
relations:
- kind: uses
  target: D-VKR54
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
Let $J=(f_i\mid i\in I)$.
If $J=R$, then
$$
1=a_1f_{i_1}+\cdots+a_rf_{i_r}
$$
for finitely many indices $i_1,\ldots,i_r$. No prime ideal can contain all of those $f_{i_j}$, so
$$
\Spec R=D(f_{i_1})\cup\cdots\cup D(f_{i_r}).
$$

Conversely, if the $D(f_i)$ cover $\Spec R$ and $J$ were proper, then $J$ would lie in a maximal ideal $\mfm$. This point $\mfm\in\Spec R$ would contain every $f_i$, hence belong to none of the $D(f_i)$, a contradiction. Thus $J=R$.

Distinguished opens form a basis for the Zariski topology on $\Spec R$. Refining an arbitrary open cover by distinguished opens and applying the preceding finite-subcover argument proves that $\Spec R$ is quasicompact.
:::
