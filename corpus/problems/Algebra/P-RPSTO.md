---
schema: qual/card@1
id: P-RPSTO
kind: problem
title: Solvable groups have a nontrivial normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Normal Subgroups
  - Commutators
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source reads "Show that if $G$ is solvable, then $G$ contains a nontrivial normal subroup." with the follow-up "What does this mean on the Galois theory side?" and the hint "consider the derived series." Taken literally, $G$ itself is such a subgroup. The statement now asks for a proper nontrivial normal subgroup of a nontrivial solvable group not of prime order, the hint is a hint block, and the parts are labelled (a) and (b).'
---

::: {.problem}
(a) Show that if $G$ is a nontrivial solvable group that is not of prime order, then $G$ contains a proper nontrivial normal subgroup.

(b) What does this mean on the Galois theory side?
:::

::: {.hint}
Consider the derived series.
:::

::: {.solution}
::: pf

::: {.pf-step #nonabelian}
If $G$ is nonabelian and solvable, then $[G,G]$ is a proper nontrivial normal subgroup.

::: pf-proof
$[G,G]\ne1$ because $G$ is nonabelian. If $[G,G]=G$, then every term of the derived series equals $G\ne1$, so the series never reaches $1$, contradicting solvability. $[G,G]$ is characteristic, hence normal.
:::

:::

::: {.pf-step #abelian}
If $G$ is abelian, nontrivial and not of prime order, then $G$ has a proper nontrivial subgroup, which is normal.

::: pf-proof
Pick $x\ne1$. If $\langle x\rangle\ne G$, it is the required subgroup. Otherwise $G$ is cyclic: if $G\cong\ZZ$, take $2\ZZ$; if $G\cong\ZZ/n\ZZ$ with $n$ composite, take the subgroup of order $d$ for a divisor $1<d<n$. Every subgroup of an abelian group is normal.
:::

:::

::: pf-step
(a) A nontrivial solvable group not of prime order has a proper nontrivial normal subgroup; equivalently, the simple solvable groups are the cyclic groups of prime order.

::: pf-proof
Steps [](#nonabelian){.pf-ref} and [](#abelian){.pf-ref} cover the nonabelian and abelian cases.
:::

:::

::: pf-step
(b) Let $L/F$ be a finite Galois extension with solvable group $G=\Gal(L/F)$ whose order is neither $1$ nor prime. Then there is an intermediate field $F\subsetneq E\subsetneq L$ with $E/F$ Galois. Iterating along the derived series gives a tower $F=E_0\subset E_1\subset\cdots\subset E_m=L$ in which each $E_{j+1}/E_j$ is Galois with abelian group.

::: pf-proof
By the Galois correspondence, a normal subgroup $N\trianglelefteq G$ corresponds to $E=L^N$ with $E/F$ Galois and $\Gal(E/F)\cong G/N$; $N$ proper and nontrivial gives $E\ne F,L$. With $G^{(j)}$ the derived series, $E_j\coloneqq L^{G^{(m-j)}}$ for the derived length $m$, and $\Gal(E_{j+1}/E_j)\cong G^{(m-j-1)}/G^{(m-j)}$ is abelian.
:::

:::

:::
:::
