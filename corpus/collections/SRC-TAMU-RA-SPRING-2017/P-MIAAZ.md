---
schema: qual/card@1
id: P-MIAAZ
kind: problem
title: A continuous convex function on the unit ball of a reflexive Banach space attains
  its minimum
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
relations: []
review: draft
---

::: {.problem}
Show that every convex continuous function defined on the closed unit ball of a reflexive Banach space achieves a minimum.
(A convex function on a convex subset $A$ of a normed space is a real valued function $f$ on $A$ such that for every $x,y\in A$ and every $0<\lambda<1$ we have $f(\lambda x+(1-\lambda)y)\le\lambda f(x)+(1-\lambda)f(y)$.)
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/j17.pdf` and no solutions sheet accompanies it, so the argument below is the card's own. It is written out because the earlier version of the card leaned on two results it named only in passing — that a norm-continuous convex function is weakly lower semicontinuous, and that a weakly compact set has the finite intersection property for its closed subsets — and hedged about the first.

Throughout, $X$ is a reflexive Banach space, $B\coloneqq\theset{x\in X\mid\norm{x}\leq1}$ is its closed unit ball, and $f\colon B\to\RR$ is convex and continuous with respect to the norm topology. Write $B^{**}$ for the closed unit ball of $X^{**}$.

::: pf

::: {.pf-step #ball-compact}
$B$ is weakly compact.

::: pf-proof
By Alaoglu's theorem $B^{**}$ is compact in the weak$^{*}$ topology of $X^{**}$. Reflexivity says the canonical embedding $J\colon X\to X^{**}$, $J(x)(\varphi)=\varphi(x)$, is a surjective isometry, and $J$ is a homeomorphism of $X$ with the weak topology onto $X^{**}$ with the weak$^{*}$ topology, because the two topologies are defined by the same families of functionals. Hence $J(B)=B^{**}$, and a homeomorphic image of the compact space $B^{**}$ is compact, so $B$ is weakly compact.
:::

:::

::: {.pf-step #weakly-lsc}
$f$ is lower semicontinuous for the weak topology on $B$.

:::: pf-proof

::: {.pf-step #sublevel}
For every real $t$ the sublevel set $F_{t}\coloneqq\theset{x\in B\mid f(x)\leq t}$ is convex and closed in the norm topology of $B$.

::: pf-proof
$f$ is convex, so for $x,y\in F_{t}$ and $0<\lambda<1$ one has $f(\lambda x+(1-\lambda)y)\leq\lambda f(x)+(1-\lambda)f(y)\leq t$, which puts the segment inside $F_{t}$; and $f$ is continuous, so $F_{t}=f^{-1}\big((-\infty,t]\big)$ is the preimage of a closed set and is closed in $B$.
:::

:::

::: {.pf-step #convex-weakly-closed}
A convex subset of a normed space that is closed in the norm topology is closed in the weak topology.

::: pf-proof
The weak topology is coarser than the norm topology, so a weakly closed set is norm closed; conversely, if $C$ is convex and norm closed and $x\notin C$, the separation theorem for a point and a closed convex set gives a bounded linear functional $\varphi$ and a real $\alpha$ with $\varphi(x)>\alpha\geq\varphi(c)$ for all $c\in C$. The set $\theset{y\mid\varphi(y)>\alpha}$ is a weak neighbourhood of $x$ disjoint from $C$, so the complement of $C$ is weakly open.
:::

:::

::: {.pf-step}
$f$ is weakly lower semicontinuous.

::: pf-proof
By steps [](#sublevel){.pf-ref} and [](#convex-weakly-closed){.pf-ref} each $F_{t}$ is weakly closed, and a function is lower semicontinuous exactly when its sublevel sets $\theset{f\leq t}$ are closed.
:::

:::

::::

:::

::: pf-step
Therefore $f$ attains its minimum on $B$.

::: pf-proof
Let $m\coloneqq\inf_{B}f\in[-\infty,\infty)$, the infimum being taken in the extended reals; it is not asserted to be finite. For each real $t>m$ the set $F_{t}$ is nonempty, because otherwise $t$ would be a lower bound strictly larger than the greatest lower bound, and it is weakly closed by step [](#weakly-lsc){.pf-ref}; the family $\theset{F_{t}}_{t>m}$ is nested, so any finite subfamily has nonempty intersection, and $B$ is weakly compact by step [](#ball-compact){.pf-ref}, so the whole intersection contains a point $x_{0}$. Then $f(x_{0})\leq t$ for every real $t>m$, so $f(x_{0})\leq m$; and $f(x_{0})\geq m$ because $m$ is a lower bound for $f$ on $B$. Hence $f(x_{0})=m$. This has two consequences: the infimum is finite after all, $m=f(x_{0})\in\RR$, so it was not $-\infty$, and it is attained at $x_{0}$, which is what the exercise asks. Reflexivity enters through the weak compactness of $B$ and continuity through the closedness of the sublevel sets.
:::

:::

:::

:::
