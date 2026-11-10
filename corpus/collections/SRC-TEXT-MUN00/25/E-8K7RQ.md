---
schema: qual/card@1
id: E-8K7RQ
kind: problem
title: Components and continuous maps out of the lower limit line
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §25 Exercise 1, printed p. 162, with the lower
    limit topology of §13 and Exercise 18.7(b); the stored statement is the printed
    question.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.1, PDF p. 7. The ray above a point of a
    connected subspace of R_l is open and closed in it, so the subspace is a single point;
    the continuous maps into R_l are then the constant maps. (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
---

::: {.exercise}

What are the components and path components of $\RR_\ell$?
What are the continuous maps $f: \RR \to \RR_\ell$?
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.1, PDF p. 7** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

Let $A$ be a nonempty connected subspace of $\RR_{\ell}$ and $a\in A$. The set $[a,\infty)\cap A$ is open in $A$ (trace of the open set $[a,\infty)=\bigcup_{n}[a+n,a+n+1)$) and closed in $A$ (trace of the closed set $(-\infty,a)$, closed since $\RR_{\ell}$ is Hausdorff), and it is nonempty; since $A$ is connected it equals $A$. So every $b\in A$ satisfies $b\ge a$, whence $A=\{a\}$. Thus the components of $\RR_{\ell}$ are the singletons.

Every path component lies in a component, so the path components are the singletons too.

If $f:\RR\to\RR_{\ell}$ is continuous then $f(\RR)$ is connected in $\RR_{\ell}$, hence a single point: the continuous maps $\RR\to\RR_{\ell}$ are exactly the constant maps (compare Exercise 18.7(b)).
:::
