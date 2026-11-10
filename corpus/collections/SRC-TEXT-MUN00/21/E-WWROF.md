---
schema: qual/card@1
id: E-WWROF
kind: problem
title: Closed sets via the closed-set formulation of continuity
classification:
  areas:
  - topology
  topics:
  - Closed Sets
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 10, printed p. 134, with the closed
    set formulation of continuity and Theorem 21.5; the three sets are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.10, PDF p. 26. Each set is the preimage of a
    closed subset of R under a continuous polynomial map of R^2: xy = 1, x^2 + y^2 = 1, and
    x^2 + y^2 in [0,1]. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Using the closed set formulation of continuity (Theorem 18.1), show that the following are closed subsets of $\RR^2$:

$$
A = \theset{x \times y \mid xy = 1},
$$

$$
S^1 = \theset{x \times y \mid x^2 + y^2 = 1},
$$

$$
B^2 = \theset{x \times y \mid x^2 + y^2 \leq 1}.
$$

The set $B^2$ is called the (closed) unit ball in $\RR^2$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.10, PDF p. 26** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the argument is theirs.

By the closed set formulation of continuity (Theorem 18.1(3), printed p. 107), the preimage of a closed set under a continuous map is closed, and by Theorem 21.5 (printed p. 129) sums and products of continuous real-valued functions are continuous; in particular the polynomial maps below are continuous on $\RR^{2}$.

$A=\{(x,y)\mid xy=1\}$ is the preimage of the closed set $\{1\}\subset\RR$ under the continuous map $f(x,y)=xy$, hence closed.

$S^{1}=\{(x,y)\mid x^{2}+y^{2}=1\}$ is the preimage of the closed set $\{1\}$ under the continuous map $g(x,y)=x^{2}+y^{2}$, hence closed.

$B^{2}=\{(x,y)\mid x^{2}+y^{2}\le1\}$ is the preimage of the closed set $[0,1]$ under the same $g$, hence closed.
:::
