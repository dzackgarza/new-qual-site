---
schema: qual/card@1
id: P-PXZN2
kind: problem
title: Finite groups as Galois groups
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Classification
relations: []
review: draft
---

::: {.problem}
Which finite groups occur as Galois groups of some field extension?
:::

::: {.solution}
Let $G$ be a finite group, let $k$ be a field, and let $L=k(x_g:g\in G)$ be the rational function field in algebraically independent variables indexed by $G$.

::: pf

::: {.pf-step #action}
$G$ acts faithfully on $L$ by $k$-automorphisms with $h(x_g)=x_{hg}$.

::: pf-proof
For each $h\in G$, the permutation $x_g\mapsto x_{hg}$ of the variables extends uniquely to a $k$-automorphism of the polynomial ring and hence of its fraction field $L$. These automorphisms compose as $G$ does, and $h\ne e$ moves $x_e$ to $x_h\ne x_e$.
:::

:::

::: pf-step
$\boxed{\text{Every finite group}}$ occurs: with $K=L^G$, the extension $L/K$ is Galois with $\Gal(L/K)\cong G$.

::: pf-proof
By step [](#action){.pf-ref}, $G$ is a finite group of automorphisms of $L$. Artin's theorem gives that $L/L^G$ is Galois with $[L:L^G]=\abs{G}$ and $\Gal(L/L^G)=G$.
:::

:::

:::

:::

::: {.remark}
Over the fixed base field $\QQ$, whether every finite group occurs is the inverse Galois problem, which is open.
:::
