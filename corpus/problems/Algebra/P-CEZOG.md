---
schema: qual/card@1
id: P-CEZOG
kind: problem
title: Order of a cyclic module over a commutative ring
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Cyclic Groups
  - Torsion
relations: []
review: draft
---

::: problem
Let $A=Ra$ be a cyclic module over a commutative ring $R$.
Define the order ideal of $a$ by
\[
\mathcal O_a=\{r\in R:ra=0\}.
\]
Show that
\[
A\cong R/\mathcal O_a.
\]
In particular, if $\mathcal O_a=(r)$ is principal, show that $ra=0$ and $A\cong R/(r)$.
:::

::: {.solution}
Consider the surjective $R$-module homomorphism
\[
\phi:R\longrightarrow A,\qquad s\longmapsto sa.
\]
Its kernel is exactly
\[
\ker\phi=\{s\in R:sa=0\}=\mathcal O_a.
\]
The first isomorphism theorem therefore gives
\[
A\cong R/\mathcal O_a.
\]

If $\mathcal O_a=(r)$, then $r\in\mathcal O_a$, hence $ra=0$, and the preceding isomorphism becomes
\[
A\cong R/(r).
\]
Thus the principal generator of the order ideal records the annihilator of the cyclic generator and therefore the cyclic module itself, up to associates.
:::
