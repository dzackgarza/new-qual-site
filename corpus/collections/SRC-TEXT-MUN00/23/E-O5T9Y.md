---
schema: qual/card@1
id: E-O5T9Y
kind: problem
title: The lower limit line is disconnected
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
    Read against Munkres, Topology (2000), §23 Exercise 7, printed p. 152, with the lower
    limit topology of §13; the stored statement is the printed question.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.7, PDF p. 2. The ray (-infinity,0) and the ray
    [0,infinity) are disjoint nonempty open sets of R_l whose union is the space.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Is the space $\RR_\ell$ connected?
Justify your answer.
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.7, PDF p. 2** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the witness pair is theirs.

$\RR_{\ell}$ is the set $\RR$ with the topology having as a basis the sets $[a,b)$ with $a<b$ (Example 3); a subset is open exactly when it is a union of such sets.

::: pf

::: {.pf-step #both-open}
$(-\infty,0)$ and $[0,\infty)$ are open in $\RR_{\ell}$.

::: pf-proof
$(-\infty,0)=\bigcup_{n\ge1}[-n,0)$, a union of basis elements. $[0,\infty)=[0,1)\cup\bigcup_{n\ge1}[n,n+1)$, a union of basis elements: a real $x\ge0$ lies in $[0,1)$ if $x<1$, and otherwise in $[n,n+1)$ for $n=\lfloor x\rfloor\ge1$. A union of basis elements is open.
:::

:::

::: {.pf-step #separation}
These two open sets are disjoint and nonempty, and their union is $\RR$.

::: pf-proof
$(-\infty,0)\cap[0,\infty)=\varnothing$, both are nonempty ($-1$ lies in the first, $0$ in the second), and every real number is either negative or in $[0,\infty)$.
:::

:::

::: {.pf-qed}
By steps [](#both-open){.pf-ref} and [](#separation){.pf-ref} the sets $(-\infty,0)$ and $[0,\infty)$ form a separation of $\RR_{\ell}$, so $\RR_{\ell}$ is not connected.
:::

:::

:::
