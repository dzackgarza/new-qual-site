---
schema: qual/card@1
id: P-5YZPH
kind: problem
title: A $p$-subgroup acting on the cosets of a Sylow $p$-subgroup has a length-one
  orbit iff it lies in a conjugate
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Group Actions
  - Cosets and Lagrange
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group, $H$ a $p\dash$subgroup, and $P$ a sylow $p\dash$subgroup for $p$ a prime.
Let $H$ act on the left cosets of $P$ in $G$ by left translation.

Prove that this is an orbit under this action of length 1.

Prove that $xP$ is an orbit of length 1 $\iff H$ is contained in $xPx\inv$.
:::

::: {.solution}
Write $X=G/P$ for the finite set of left cosets, with the action $h\cdot xP=hxP$.

<1>1. The action of $H$ on $X$ has an orbit of cardinality one.

::: {.proof}
Since $P$ is a Sylow $p$-subgroup, the index $|X|=[G:P]$ is not divisible by $p$. For any coset $xP$, orbit–stabilizer gives $|H\cdot xP|=[H:H_{xP}]$, which is a power of $p$. If every orbit had cardinality greater than one, all orbit cardinalities would be divisible by $p$, as would their sum $|X|$. This is impossible. Therefore some coset is fixed by $H$.
:::

<1>2. A coset $xP$ is an orbit of cardinality one precisely when
\[
\boxed{H\subseteq xPx^{-1}}.
\]

::: {.proof}
The orbit of $xP$ consists of one element if and only if $hxP=xP$ for all $h\in H$. For each $h$, equality of these left cosets is equivalent to $x^{-1}hx\in P$. Thus the condition is $x^{-1}Hx\subseteq P$, equivalently $H\subseteq xPx^{-1}$.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 prove existence of a length-one orbit and characterize precisely which cosets have this property.
:::
:::
