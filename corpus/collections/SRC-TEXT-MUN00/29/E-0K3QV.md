---
schema: qual/card@1
id: E-0K3QV
kind: problem
title: The one-point compactification of the minimal uncountable well-ordered set
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 7, printed p. 186, with Theorem 27.1
    and Theorem 29.1 for uniqueness; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.7, PDF p. 23. S_Omega with its largest point
    added is compact Hausdorff: an open set containing the largest point contains a final
    interval, and the initial closed interval is compact by Theorem 27.1.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that the one-point compactification of $S_\Omega$ is homeomorphic with $\overline{S}_\Omega$.
:::

::: {.solution}

The argument is **"positron0802"**, *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.7, PDF p. 23 (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the cover at the largest element and the appeal to uniqueness are that solution's, and the two points it leaves implicit — that $S_{\Omega}$ inherits the order topology as a subspace, and that $S_{\Omega}$ is not compact, so that it has a one-point compactification in the book's sense — are supplied below. The statement was checked against Munkres, *Topology* (2000), §29 Exercise 7, printed p. 186.

Throughout, $S_{\Omega}$ is the minimal uncountable well-ordered set and $\overline{S}_{\Omega}=S_{\Omega}\cup\theset{\Omega}$, where $\Omega$ is an element larger than every element of $S_{\Omega}$; both carry the order topology, and $a_{0}$ denotes the least element of $S_{\Omega}$.

::: pf

::: {.pf-step #subspace}
$S_{\Omega}$ is a subspace of $\overline{S}_{\Omega}$.

::: pf-proof
$S_{\Omega}$ is convex in $\overline{S}_{\Omega}$: if $x<y$ lie in $S_{\Omega}$ and $z\in\overline{S}_{\Omega}$ satisfies $x<z<y$, then $z<y$ forces $z\in S_{\Omega}$, since $\Omega$ is larger than every element of $S_{\Omega}$. By Theorem 16.4 (printed p. 91) the order topology on a convex subset is the subspace topology, so $S_{\Omega}$ carries the topology it inherits from $\overline{S}_{\Omega}$.
:::

:::

::: {.pf-step #one-point}
$\overline{S}_{\Omega}-S_{\Omega}=\theset{\Omega}$.

::: pf-proof
$\overline{S}_{\Omega}$ is by definition $S_{\Omega}$ together with the single element $\Omega$, which is not in $S_{\Omega}$.
:::

:::

::: {.pf-step #hausdorff}
$\overline{S}_{\Omega}$ is Hausdorff.

::: pf-proof
Every order topology is Hausdorff (§17 Exercise 10, printed p. 101). Explicitly, given $x<y$ in $\overline{S}_{\Omega}$: if some $z$ satisfies $x<z<y$, then the rays $(-\infty,z)$ and $(z,\infty)$ are disjoint open neighbourhoods; otherwise $(-\infty,y)$ and $(x,\infty)$ are disjoint open sets containing $x$ and $y$ respectively, since no element lies strictly between them.
:::

:::

::: {.pf-step #intervals-compact}
Every closed interval $[c,d]$ of $\overline{S}_{\Omega}$ is compact.

::: pf-proof
A well-ordered set has the least upper bound property: a nonempty subset bounded above has an upper bound, and the least element of the set of its upper bounds, which exists by well-ordering, is its least upper bound. Hence $\overline{S}_{\Omega}$ is a simply ordered set with the least upper bound property, and Theorem 27.1 (printed p. 172) makes each closed interval in it compact in the order topology.
:::

:::

::: {.pf-step #compact}
$\overline{S}_{\Omega}$ is compact.

:::: pf-proof

::: {.pf-step #containing-omega}
If $\mathcal{A}$ is an open cover of $\overline{S}_{\Omega}$ and $A\in\mathcal{A}$ contains $\Omega$, then $(a,\Omega]\subset A$ for some $a\in S_{\Omega}$.

::: pf-proof
$A$ is open and contains the largest element $\Omega$ of the ordered set, so it contains a basis element about $\Omega$; a basis element of the order topology containing the largest element is a ray $(a,\Omega]$ for some $a<\Omega$. Such an $a$ lies in $S_{\Omega}$ because only $\Omega$ lies outside it.
:::

:::

::: {.pf-step #finite-subcover}
There are $A_{1},\dots,A_{n}\in\mathcal{A}$ covering $[a_{0},a]$.

::: pf-proof
$[a_{0},a]$ is a closed interval of $\overline{S}_{\Omega}$ and is convex there, so by Theorem 16.4 its order topology is the subspace topology; hence $\theset{A\cap[a_{0},a]\mid A\in\mathcal{A}}$ is an open cover of the compact space $[a_{0},a]$ given by step [](#intervals-compact){.pf-ref}, and it has a finite subcover.
:::

:::

::: {.pf-step}
$A,A_{1},\dots,A_{n}$ cover $\overline{S}_{\Omega}$, so $\overline{S}_{\Omega}$ is compact.

::: pf-proof
Every element of $\overline{S}_{\Omega}$ satisfies $x\leq a$ or $x>a$. In the first case $x\in[a_{0},a]$ and $x$ lies in some $A_{i}$; in the second $x\in(a,\Omega]\subset A$ by step [](#containing-omega){.pf-ref}. Hence the finite subcollection $A,A_{1},\dots,A_{n}$ covers $\overline{S}_{\Omega}$, and $\mathcal{A}$ was arbitrary.
:::

:::

::::

:::

::: {.pf-step #not-compact}
$S_{\Omega}$ is not compact.

::: pf-proof
Suppose $S_{\Omega}$ were compact. It is a subspace of the Hausdorff space $\overline{S}_{\Omega}$ by steps [](#subspace){.pf-ref} and [](#hausdorff){.pf-ref}, so it would be closed in $\overline{S}_{\Omega}$ and $\theset{\Omega}=\overline{S}_{\Omega}-S_{\Omega}$ would be open. A basis element of the order topology containing $\Omega$ is a ray $(a,\Omega]$ with $a\in S_{\Omega}$, and $(a,\Omega]$ contains the successor of $a$, which lies in $S_{\Omega}$ because $S_{\Omega}$ is well ordered; so no basis element about $\Omega$ is contained in $\theset{\Omega}$, and $\theset{\Omega}$ is not open. This contradiction shows $S_{\Omega}$ is not compact.
:::

:::

::: pf-step
Therefore the one-point compactification of $S_{\Omega}$ is homeomorphic with $\overline{S}_{\Omega}$.

::: pf-proof
Steps [](#subspace){.pf-ref}, [](#one-point){.pf-ref}, [](#hausdorff){.pf-ref} and [](#compact){.pf-ref} say that $\overline{S}_{\Omega}$ is a space $Y$ satisfying the three conditions of Theorem 29.1 (printed p. 183) for $X=S_{\Omega}$: $S_{\Omega}$ is a subspace, $Y-X$ is a single point, and $Y$ is compact Hausdorff. By the backward direction of that theorem $S_{\Omega}$ is locally compact Hausdorff, and by step [](#not-compact){.pf-ref} it is not compact, so it has a one-point compactification in the sense of the definition on the same page; and by Step 1 of the same theorem, any two spaces satisfying the three conditions for the same $X$ are homeomorphic by a homeomorphism that is the identity on $X$. Hence $\overline{S}_{\Omega}$ is homeomorphic with the one-point compactification of $S_{\Omega}$.
:::

:::

:::

:::
