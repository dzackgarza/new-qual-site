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
---

::: {.exercise}

Show that $[0, 1]$ is not limit point compact as a subspace of $\RR_\ell$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.2, PDF p. 18** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the infinite subset and both cases are theirs.

Let $A=\{1-1/n\mid n\in\ZZ_{+}\}\subset[0,1]$, an infinite set. In the subspace $[0,1]$ of $\RR_{\ell}$ no point is a limit point of $A$:

- if $x\in[0,1)$ and $1-1/n\le x<1-1/(n+1)$, then $[x,1-1/(n+1))$ is a basis element of $\RR_{\ell}$ intersected with $[0,1]$ that contains $x$ and meets $A$ at most in $x$ itself;
- $x=1$ has the neighbourhood $[1,2)\cap[0,1]=\{1\}$, which meets $A$ only in $1$ when $1\in A$.

So $A$ is an infinite subset of $[0,1]$ with no limit point in $[0,1]$, and $[0,1]$ is not limit point compact as a subspace of $\RR_{\ell}$.
:::
