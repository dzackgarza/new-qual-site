---
schema: qual/card@1
id: E-PER08-6.4
kind: problem
title: Perutz Algebraic Topology I Exercise 6.4
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
---

::: {.problem}
(a) The universal cover of the torus T 2 is R2. Identify all the deck transformations and hence determine (once again) the fundamental group.
Which surfaces can cover T 2? (b) Show that the Klein bottle is also covered by R2; identify the deck transformations and hence the fundamental group.
:::

::: {.solution}
<1>1. The torus.
::: {.proof}
Write $T^2=\mathbb R^2/\mathbb Z^2$.
The universal covering map is the quotient, and its deck transformations are exactly
\[
(x,y)\longmapsto(x+m,y+n),\qquad (m,n)\in\mathbb Z^2.
\]
Hence $\pi_1(T^2)\cong\mathbb Z^2$.

Connected covering surfaces correspond to subgroups $H\le\mathbb Z^2$.
Such a subgroup has rank $0,1$, or $2$.
The quotient $\mathbb R^2/H$ is respectively homeomorphic to $\mathbb R^2$, $S^1\times\mathbb R$, or $T^2$ (in the rank-$2$ case possibly with more than one sheet).
Thus these are precisely the connected surface types covering $T^2$.
:::

<1>2. The Klein bottle.
::: {.proof}
Let
\[
a(x,y)=(x+1,y),\qquad b(x,y)=(-x,y+1).
\]
The group $\Gamma=\langle a,b\rangle$ acts freely and properly discontinuously on $\mathbb R^2$, and a fundamental domain is a unit square with one pair of opposite edges identified in the same direction and the other pair in opposite directions.
Hence $\mathbb R^2/\Gamma$ is the Klein bottle and $\mathbb R^2$ is its universal cover.

A direct calculation gives
\[
bab^{-1}=a^{-1}.
\]
Therefore
\[
\pi_1(K)\cong\Gamma\cong\langle a,b\mid bab^{-1}=a^{-1}\rangle.
\]
:::
:::
