---
schema: qual/card@1
id: P-KXSW3
kind: problem
title: A subgroup of a finite $p$-group generating $H/[H,H]$ equals $H$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Commutators
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $H$ be a finite $p$-group and let $G\le H$. Suppose the composite
$$
G\hookrightarrow H\twoheadrightarrow H/[H,H]
$$
is surjective. Prove that $G=H$.
:::

::: {.solution}
Surjectivity of the composite is equivalent to $H=G[H,H]$. Suppose, for contradiction, that $G<H$. Since $H$ is finite, $G$ is contained in a maximal subgroup $M<H$.

::: pf

::: {.pf-step #index-p}
$M$ is normal in $H$ of index $p$.

::: pf-proof
In a finite $p$-group every proper subgroup is properly contained in its normalizer. Maximality gives $N_H(M)=H$, so $M\trianglelefteq H$. The quotient $H/M$ is a nontrivial $p$-group with no nontrivial proper subgroup, since such a subgroup would correspond to a subgroup strictly between $M$ and $H$; a $p$-group of order $p^k$ has subgroups of every order $p^j$, $j\le k$, so $\abs{H/M}=p$.
:::

:::

::: {.pf-step #derived}
$[H,H]\subseteq M$.

::: pf-proof
By step [](#index-p){.pf-ref}, $H/M$ has order $p$, so it is cyclic and hence abelian. The derived subgroup lies in the kernel of every homomorphism to an abelian group, in particular of $H\to H/M$.
:::

:::

::: pf-step
$G=H$.

::: pf-proof
$G\subseteq M$ and, by step [](#derived){.pf-ref}, $[H,H]\subseteq M$, so $G[H,H]\subseteq M<H$, contradicting $G[H,H]=H$.
:::

:::

:::

:::
