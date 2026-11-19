---
schema: qual/card@1
id: E-2V2VL
kind: problem
title: Compact subspaces of metric spaces are closed and bounded
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 4, printed p. 171, with Theorem
    26.3; the stored statement is the printed one, including the request for a
    counterexample.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.4, PDF p. 12. Finitely many balls about a point
    of Y cover Y; an infinite discrete metric space is closed and bounded and not compact.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2 and re-checked against both the retained set and
    the book: the text of Exercise 26.4 is line 224 of
    `tmp/sources/munkres-solutions-positron-ch3.md`, and `pdftotext -f 12 -l 12` of the PDF prints
    it, so the cited page 12 is right. Its steps: metric spaces are Hausdorff, so $Y$ is closed by
    Theorem 26.3; the balls $B_d(y,n)$ for $n\in\ZZ_+$ are an open cover of $Y$ whose finite
    subcover has a largest radius $N$, giving $Y\subseteq B_d(y,N)$; and the infinite discrete
    metric space is closed, bounded, and not compact, its singleton cover having no finite
    subcover. Added: the increase of the balls, which the set's "the greatest positive number such
    that $B_N$ belongs" assumes, and the open-ness of the singletons in the discrete metric. No
    defect found in the statement, which is Munkres's Exercise 4 of §26 on printed p. 171. Not
    claimed: a printed publication, the source being a posted solution set.
---

::: {.exercise}

Show that every compact subspace of a metric space is bounded in that metric and is closed.
Find a metric space in which not every closed bounded subspace is compact.
:::

::: {.solution}
The retained published solution is **positron0802, *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.4, PDF p. 12** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument and the counterexample below are its, with the citations to Munkres's §26 theorems checked against the book.

::: pf

::: {.pf-step #closed}
A compact subspace $Y$ of a metric space $(X,d)$ is closed in $X$.

::: pf-proof
Metric spaces are Hausdorff: distinct points have disjoint balls of radius a third of their distance. A compact subspace of a Hausdorff space is closed, which is Theorem 26.3 of Munkres, so $Y$ is closed.
:::

:::

::: {.pf-step #bounded}
$Y$ is bounded in $d$: there is $y\in Y$ and $N$ with $Y\subseteq B_d(y,N)$.

::: pf-proof
Fix $y\in Y$ and let $B_n=B_d(y,n)$ for $n\in\ZZ_{+}$; these balls are open and increase with $n$, and every point of $Y$ lies in some $B_n$ because distances are finite, so $\{B_n\}_{n\in\ZZ_+}$ is an open cover of $Y$. Compactness gives a finite subcover $B_{n_1},\ldots,B_{n_k}$, and with $N=\max\{n_1,\ldots,n_k\}$ the increase gives $Y\subseteq B_N$.
:::

:::

::: {.pf-step #counterexample}
There is a metric space in which a closed bounded subspace is not compact.

::: pf-proof
Let $X$ be an infinite set with the discrete metric, $d(x,y)=1$ for $x\ne y$ and $d(x,x)=0$. Then $X$ is closed in itself, and it is bounded because $X=B_d(x,2)$ for any $x\in X$. The one-point sets $\{x\}$ are open, since each is the ball of radius $1/2$ about $x$, so they form an open cover of $X$; a finite subcover would cover $X$ by finitely many points, and $X$ is infinite. Hence this closed bounded subspace $X$ is not compact.
:::

:::

::: {.pf-step}
Every compact subspace of a metric space is bounded and closed, and not every closed bounded subspace of a metric space is compact.

::: pf-proof
The first clause is steps [](#closed){.pf-ref} and [](#bounded){.pf-ref}; the second is the example of step [](#counterexample){.pf-ref}.
:::

:::

:::
:::
