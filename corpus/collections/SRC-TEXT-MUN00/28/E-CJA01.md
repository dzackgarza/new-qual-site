---
schema: qual/card@1
id: E-CJA01
kind: problem
title: The unit interval is not limit point compact in the lower limit topology
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
    Read against Munkres, Topology (2000), §28 Exercise 2, printed p. 181; the stored
    statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 28.2, PDF p. 18. The increasing sequence 1 - 1/n
    has no limit point in [0,1] as a subspace of R_l, half-open intervals isolating each of
    its points. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Munkres, *Topology* (2000), §28 Exercise 2, printed p. 181. The argument is transcribed from the retained set: "positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.2, PDF p. 18. Checked: the choice of $n$ for $x\in[0,1)$, that $[x,1-1/(n+1))$ is a lower-limit basis element isolating $x$ from $A$, and that $[1,2)\cap[0,1]=\{1\}$ is a neighbourhood of $1$.
---

::: {.exercise}

Show that $[0, 1]$ is not limit point compact as a subspace of $\RR_\ell$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.2, PDF p. 18** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the infinite subset and both cases are theirs. The statement is Munkres, *Topology* (2000), §28 Exercise 2, printed p. 181.

::: pf

::: {.pf-step #set}
$A=\{1-1/n\st n\in\ZZ_+\}$ is an infinite subset of $[0,1]$.

::: pf-proof
The terms $1-1/n$ are distinct for distinct $n$ and lie in $[0,1)$, since $0\le1-1/n<1$.
:::
:::

::: {.pf-step #below}
No $x\in[0,1)$ is a limit point of $A$ in the subspace topology.

::: pf-proof
Given $x\in[0,1)$ choose $n$ with $1-1/n\le x<1-1/(n+1)$, possible because the points $1-1/n$ increase to $1$. Then $[x,1-1/(n+1))$ is a basis element of $\RR_\ell$, so its intersection with $[0,1]$ is a neighbourhood of $x$ in the subspace, and it meets $A$ at most in $x$ itself, since every element of $A$ other than $x$ is either below $x$ or at least $1-1/(n+1)$.
:::
:::

::: {.pf-step #one}
$1$ is not a limit point of $A$.

::: pf-proof
$[1,2)$ is a basis element of $\RR_\ell$ containing $1$, so $[1,2)\cap[0,1]=\{1\}$ is a neighbourhood of $1$ in the subspace meeting $A$ only in $1$.
:::
:::

::: {.pf-step}
$[0,1]$ is not limit point compact as a subspace of $\RR_\ell$.

::: pf-proof
Steps [](#set){.pf-ref}, [](#below){.pf-ref} and [](#one){.pf-ref} exhibit an infinite subset of $[0,1]$ with no limit point in $[0,1]$, which is the negation of limit point compactness.
:::
:::

:::
:::
