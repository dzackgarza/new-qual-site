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
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.3, PDF pp. 18--19** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all three answers are theirs.

(a) **No.** Let $X=\ZZ_{+}\cup Y$ be the space of Example 1 of §28 (two points of $Y$ with the indiscrete topology); $X$ is limit point compact, the projection $\pi_{1}:X\to\ZZ_{+}$ is continuous, and $\pi_{1}(X)=\ZZ_{+}$ is not limit point compact.

(b) **Yes.** If $A\subset X$ is closed and $B\subset A$ is infinite, then $B$ has a limit point $x\in X$; $x$ is a limit point of $A$, so $x\in\overline A=A$. Hence every infinite subset of $A$ has a limit point in $A$.

(c) **No.** $S_{\Omega}$ in the order topology is limit point compact (Example 2 of §28), but as a subspace of $\overline{S}_{\Omega}$ it is not closed: it does not contain its limit point $\Omega$. (It is Hausdorff by Exercise 17.10, so this is not a failure of the separation axioms.)
:::
