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

::: {.problem}
Let $A=Ra$ be a cyclic module over a commutative ring $R$.
Define the order ideal of $a$ by
$$
\mathcal O_a=\{r\in R:ra=0\}.
$$
Show that
$$
A\cong R/\mathcal O_a.
$$
In particular, if $\mathcal O_a=(r)$ is principal, show that $ra=0$ and $A\cong R/(r)$.
:::

::: {.solution}

::: pf

::: {.pf-step #quotient}

$A\cong R/\mathcal O_a$.

::: pf-proof

The map $\phi:R\to A$, $s\mapsto sa$, is an $R$-module homomorphism. It is surjective because $A=Ra$, and $\ker\phi=\{s\in R:sa=0\}=\mathcal O_a$. The first isomorphism theorem gives $A\cong R/\mathcal O_a$.

:::

:::

::: pf-step

If $\mathcal O_a=(r)$, then $ra=0$ and $A\cong R/(r)$.

::: pf-proof

$r\in(r)=\mathcal O_a$, so $ra=0$, and step [](#quotient){.pf-ref} gives $A\cong R/(r)$.

:::

:::

:::

:::
