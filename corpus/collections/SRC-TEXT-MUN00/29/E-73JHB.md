---
schema: qual/card@1
id: E-73JHB
kind: problem
title: The one-point compactification of the positive integers
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
    Read against Munkres, Topology (2000), §29 Exercise 8, printed p. 186, with Theorem 27.3
    and Exercise 29.5; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.8, PDF p. 23. n -> 1/n is a homeomorphism of
    Z_+ onto {1/n}, and {1/n} with 0 adjoined is compact, so it is the one-point
    compactification and the homeomorphism extends to it. (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof. The reading found one gap: the earlier prose concluded
    that Y is the one-point compactification of X from compactness, Hausdorffness and Y - X a single
    point, without the density of X in Y that the definition on printed p. 183 also requires. The
    card now proves the density, and proves separately that Z_+ is locally compact Hausdorff and not
    compact, which is what makes its one-point compactification exist at all. The map and the use of
    Exercise 29.5 are unchanged; the statement was checked against Munkres, Topology (2000), Section
    29 Exercise 8, printed p. 186.
---

::: {.exercise}

Show that the one-point compactification of $\ZZ_+$ is homeomorphic with the subspace $\theset{0} \cup \theset{1/n \mid n \in \ZZ_+}$ of $\RR$.
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.8, PDF p. 23** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the map $n\mapsto 1/n$ and the appeal to Exercise 29.5 are that solution's. Two points it leaves implicit are supplied below: that $\ZZ_{+}$ is locally compact Hausdorff and not compact, which is what makes its one-point compactification exist, and that $\theset{1/n}$ is *dense* in $\theset{0}\cup\theset{1/n}$, which the definition of a compactification on printed p. 183 requires. The statement was checked against Munkres, *Topology* (2000), §29 Exercise 8, with that definition, Theorem 27.3 on printed p. 173 and Exercise 29.5 on printed p. 186.

Throughout, $\ZZ_{+}$ is the subspace of $\RR$ consisting of the positive integers, $X\coloneqq\theset{1/n\mid n\in\ZZ_{+}}$, and $Y\coloneqq X\cup\theset{0}$, both with the subspace topology of $\RR$.

::: pf

::: {.pf-step #homeo}

$f\colon\ZZ_{+}\to X$, $f(n)\coloneqq 1/n$, is a homeomorphism.

::: pf-proof

$f$ is a bijection by the definition of $X$. It is continuous because $\ZZ_{+}$ is discrete: for each $n$ the set $\theset{n}$ is open, so every subset of $\ZZ_{+}$ is open. Its inverse $g\colon X\to\ZZ_{+}$, $g(1/n)\coloneqq n$, is continuous as well, since $\theset{1/n}=X\cap\big(1/(n+1),1/(n-1)\big)$ for $n\geq2$ and $\theset{1}=X\cap(1/2,2)$ are open in $X$; so each point of $X$ is isolated there and every subset of $X$ is open. A continuous bijection with continuous inverse is a homeomorphism.

:::

:::

::: {.pf-step #locally-compact}

$\ZZ_{+}$ is locally compact Hausdorff and is not compact.

::: pf-proof

Every subset of $\ZZ_{+}$ is open, since each $\theset{n}$ is open there, so $\ZZ_{+}$ is discrete; and it is a subspace of the Hausdorff space $\RR$, hence Hausdorff. At a point $n$ the set $\theset{n}$ is an open neighbourhood that is finite, hence compact, so $\ZZ_{+}$ is locally compact. The cover by the sets $\theset{n}$, $n\in\ZZ_{+}$, is an open cover with no finite subcover, since $\ZZ_{+}$ is infinite and each member contains exactly one point; so $\ZZ_{+}$ is not compact.

:::

:::

::: {.pf-step #compact}

$Y$ is compact and Hausdorff.

::: pf-proof

$Y$ is closed in $\RR$: its complement is
$$
(\RR-Y)=(-\infty,0)\cup(1,+\infty)\cup\bigcup_{n\geq1}\big(1/(n+1),1/n\big),
$$
a union of open intervals, hence open. It is bounded, being contained in $[0,1]$. A closed and bounded subset of $\RR$ is compact (Theorem 27.3), so $Y$ is compact; and $Y$ is Hausdorff as a subspace of the Hausdorff space $\RR$.

:::

:::

::: {.pf-step #dense}

$X$ is a proper subspace of $Y$, its closure in $Y$ is $Y$, and $Y-X=\theset{0}$.

::: pf-proof

$0\in Y-X$ and $0\notin X$, while $X\subset Y$, so $X$ is a proper subspace and $Y-X=\theset{0}$. For density, let $V$ be a subset of $Y$ that is open in $Y$ and contains $0$; then $V=Y\cap U$ with $U$ open in $\RR$, and $(-\varepsilon,\varepsilon)\subset U$ for some $\varepsilon>0$, so $V$ contains $1/n$ for every $n>1/\varepsilon$, and $V\cap X\neq\varnothing$. Hence every neighbourhood in $Y$ of the one point of $Y-X$ meets $X$, and since $X\subset Y$ and $Y=X\cup\theset{0}$ the closure of $X$ in $Y$ is $Y$.

:::

:::

::: {.pf-step #one-point}

$Y$ is the one-point compactification of $X$.

::: pf-proof

By steps [](#compact){.pf-ref} and [](#dense){.pf-ref} the space $Y$ is compact Hausdorff, contains $X$ as a proper subspace whose closure is $Y$, and $Y-X$ is a single point: so $Y$ is a compactification of $X$ which is a one-point compactification, in the sense of the definition on printed p. 183.

:::

:::

::: pf-step

Therefore the one-point compactification of $\ZZ_{+}$ is homeomorphic with $Y$.

::: pf-proof

By step [](#locally-compact){.pf-ref} the space $\ZZ_{+}$ is a locally compact Hausdorff space that is not compact, so it has a one-point compactification $\ZZ_{+}^{+}$, and $X$ is a locally compact Hausdorff space, being homeomorphic to $\ZZ_{+}$ by step [](#homeo){.pf-ref}; its one-point compactification is $Y$ by step [](#one-point){.pf-ref}. Exercise 29.5 says a homeomorphism of locally compact Hausdorff spaces extends to a homeomorphism of their one-point compactifications, so the homeomorphism $f$ of step [](#homeo){.pf-ref} extends to one, and $\ZZ_{+}^{+}$ is homeomorphic with $Y$.

:::

:::

:::

:::
