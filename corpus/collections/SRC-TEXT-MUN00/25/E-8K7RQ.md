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

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.1, PDF p. 7** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs. Its reason for the closedness of $[a,\infty)$ is replaced below: that set is closed because its complement is a union of basis elements, not because $\RR_{\ell}$ is Hausdorff.

$\RR_{\ell}$ is $\RR$ with the topology of basis elements $[x,y)$, $x<y$ (Example 3, printed p. 82).

::: pf

::: {.pf-step #half-line}
For $a\in\RR$ the set $[a,\infty)$ is both open and closed in $\RR_{\ell}$.

::: pf-proof
$[a,\infty)=\bigcup_{n\ge0}[a+n,a+n+1)$ and $(-\infty,a)=\bigcup_{n\ge0}[a-n-1,a-n)$ are unions of basis elements, hence open. So $[a,\infty)$ is open and its complement $(-\infty,a)$ is open, that is $[a,\infty)$ is also closed.
:::

:::

::: {.pf-step #connected-singleton}
Every nonempty connected subspace $A$ of $\RR_{\ell}$ is a singleton.

::: pf-proof
Let $a,b\in A$ and put $B=[a,\infty)\cap A$. By step [](#half-line){.pf-ref} the set $[a,\infty)$ is open and closed in $\RR_{\ell}$, so $B$ is open and closed in the subspace $A$; and $B\ne\varnothing$ since $a\in B$. As $A$ is connected, the only nonempty subset of $A$ that is both open and closed in $A$ is $A$ itself, so $B=A$: every $b\in A$ satisfies $b\ge a$. Interchanging $a$ and $b$ gives $a\ge b$, hence $a=b$. So $A$ has at most one point, and being nonempty it is $\{a\}$.
:::

:::

::: {.pf-step #components}
The components of $\RR_{\ell}$ are its one-point subsets, and so are its path components.

::: pf-proof
A component is a maximal connected subspace; by step [](#connected-singleton){.pf-ref} every connected subspace is a singleton, so the component containing $x$ is $\{x\}$. A path component is path connected, hence connected, hence a singleton by step [](#connected-singleton){.pf-ref}; and every singleton $\{x\}$ is path connected (the constant path), so it is the path component of $x$.
:::

:::

::: {.pf-step #maps}
The continuous maps $f:\RR\to\RR_{\ell}$ are exactly the constant maps.

::: pf-proof
If $f$ is continuous then $f(\RR)$ is connected in $\RR_{\ell}$, being the continuous image of the connected space $\RR$ (Theorem 23.5 on the page range that this scan leaves image-only: the image of a connected space under a continuous map is connected), so $f(\RR)$ is a singleton by step [](#connected-singleton){.pf-ref}: $f$ is constant. Conversely a constant map is continuous.
:::

:::

::: {.pf-qed}
Both the components and the path components of $\RR_{\ell}$ are the one-point sets (step [](#components){.pf-ref}), and the continuous maps $\RR\to\RR_{\ell}$ are the constant ones (step [](#maps){.pf-ref}).
:::

:::

:::
