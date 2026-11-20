---
schema: qual/card@1
id: E-UX2C4
kind: problem
title: Behavior of limit point compactness under images, closed subsets, and Hausdorff ambient spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §28 Exercise 3, printed p. 181, with Examples 1
    and 2 of §28; the three questions are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 28.3, PDF pp. 18-19. Continuous images need not be
    limit point compact (Example 1), closed subspaces are, and limit point compact subspaces
    need not be closed (S_Omega in its compactification). (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked (a) the continuous image of Example 1 of §28
    onto the discrete Z_+, (b) that a limit point of a subset of a closed set lies in it,
    and (c) that S_Omega is limit point compact and not closed in its one-point
    compactification. positron0802, Chapter 3 Exercise 28.3, PDF pp. 18-19. The printed
    statement needed no repair.
---

::: {.exercise}

Let $X$ be limit point compact.

(a) If $f: X \to Y$ is continuous, does it follow that $f(X)$ is limit point compact?

(b) If $A$ is a closed subset of $X$, does it follow that $A$ is limit point compact?

(c) If $X$ is a subspace of the Hausdorff space $Z$, does it follow that $X$ is closed in $Z$?

We comment that it is not in general true that the product of two limit point compact spaces is limit point compact, even if the Hausdorff condition is assumed.
But the examples are fairly sophisticated.
See [S-S], Example 112.
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.3** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all three answers are theirs.

::: pf

::: {.pf-step #part-a}
(a) A continuous image of a limit point compact space need not be limit point compact.

::: pf-proof
Let $X=\ZZ_{+}\cup\{a,b\}$ be the space of Example 1 of §28, in which $a$ and $b$ are the only points not isolated, each neighbourhood of either meeting $\ZZ_{+}$ in all but finitely many points; the subspace $\ZZ_{+}$ carries the discrete topology and $X$ is limit point compact. The projection $\pi_{1}:X\to\ZZ_{+}$, $\pi_{1}(n)=n$ for $n\in\ZZ_{+}$ and $\pi_{1}(a)=\pi_{1}(b)=1$, is continuous, since preimages of points are points or the finite set $\{1,a,b\}$ or the whole space. But $\pi_{1}(X)=\ZZ_{+}$ is not limit point compact: it is infinite and discrete, so its infinite subsets have no limit point.
:::

:::

::: {.pf-step #part-b}
(b) A closed subset of a limit point compact space is limit point compact.

::: pf-proof
Let $A$ be closed in $X$ and $B\subset A$ infinite. Since $X$ is limit point compact, $B$ has a limit point $x\in X$, and $x$ is a limit point of $A\supset B$. As $A$ is closed it contains all its limit points, so $x\in A$. Hence every infinite subset of $A$ has a limit point in $A$.
:::

:::

::: {.pf-step #part-c}
(c) A limit point compact subspace of a Hausdorff space need not be closed.

::: pf-proof
In the order topology $S_{\Omega}$ is limit point compact (Example 2 of §28) and Hausdorff (§17 Exercise 10), but as a subspace of the compact space $\overline{S}_{\Omega}$ it is not closed: $\Omega$ is a limit point of $S_{\Omega}$ in $\overline{S}_{\Omega}$ and does not lie in $S_{\Omega}$.
:::

:::

::: {.pf-step}
All three answers hold.

::: pf-proof
Steps [](#part-a){.pf-ref}, [](#part-b){.pf-ref} and [](#part-c){.pf-ref} answer (a), (b) and (c).
:::

:::

:::
:::
