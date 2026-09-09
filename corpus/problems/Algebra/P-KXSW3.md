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

::: problem
Let $H$ be a finite $p$-group and let $G\le H$. Suppose the composite
\[
G\hookrightarrow H\twoheadrightarrow H/[H,H]
\]
is surjective. Prove that $G=H$.
:::

::: {.solution}
Surjectivity is equivalent to
\[
H=G[H,H].
\]
Suppose for contradiction that $G<H$. Since $H$ is finite, $G$ is contained in a maximal subgroup $M<H$.

<1>1. Every maximal subgroup of a finite $p$-group has index $p$ and is normal.
::: {.proof}
The quotient action of $H$ on the left cosets $H/M$ shows that the index is a power of $p$. Maximality forces the quotient to have no nontrivial proper subgroup, hence
\[
[H:M]=p.
\]
A subgroup of index $p$ in a finite $p$-group is normal.
:::

<1>2. We have $[H,H]\subseteq M$.
::: {.proof}
Because $H/M$ has order $p$, it is cyclic and therefore abelian. The derived subgroup is contained in the kernel of every homomorphism to an abelian group, so
\[
[H,H]\subseteq M.
\]
:::

Now $G\subseteq M$ and $[H,H]\subseteq M$, so
\[
G[H,H]\subseteq M<H,
\]
contradicting the surjectivity identity $G[H,H]=H$. Therefore $G=H$.
:::
