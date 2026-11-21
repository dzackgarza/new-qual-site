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

The argument is **"positron0802"**, *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.10, PDF p. 26 (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the three preimages are that solution's, and the statement and each cited theorem were checked against Munkres, *Topology* (2000), §21 Exercise 10, printed pp. 134--135, Theorem 18.1(3), printed p. 107, Lemma 21.4 and Theorem 21.5, printed p. 131, and Theorem 18.4, printed p. 110. The card's earlier reference to Theorem 21.5 on p. 129 is corrected here: that theorem is on printed p. 131.

::: pf

::: {.pf-step #maps-continuous}
The maps $f\colon\RR^{2}\to\RR$, $f(x,y)\coloneqq xy$ and $g\colon\RR^{2}\to\RR$, $g(x,y)\coloneqq x^{2}+y^{2}$ are continuous.

::: pf-proof
Identify $\RR^{2}$ with $\RR\times\RR$. By Lemma 21.4 (printed p. 131) multiplication is a continuous map $\RR\times\RR\to\RR$, and $f$ is that map. By Theorem 18.4 (printed p. 110) applied to the identity map of $\RR^{2}$, whose coordinate functions are the projections $\pi_{1},\pi_{2}$, both projections are continuous; by Theorem 21.5 (printed p. 131) the products $\pi_{1}\cdot\pi_{1}$ and $\pi_{2}\cdot\pi_{2}$, that is $(x,y)\mapsto x^{2}$ and $(x,y)\mapsto y^{2}$, are continuous, and so is their sum $g$.
:::

:::

::: {.pf-step #closed-in-line}
$\theset{1}$ and $[0,1]$ are closed subsets of $\RR$.

::: pf-proof
$\RR-\theset{1}=(-\infty,1)\cup(1,\infty)$ is a union of open rays and hence open, so its complement $\theset{1}$ is closed; $\RR-[0,1]=(-\infty,0)\cup(1,\infty)$ is likewise open, so $[0,1]$ is closed.
:::

:::

::: {.pf-step #hyperbola}
$A=\theset{x\times y\mid xy=1}$ is closed in $\RR^{2}$.

::: pf-proof
$A=f^{-1}(\theset{1})$, the preimage of a closed set under the continuous map of step [](#maps-continuous){.pf-ref}; by the closed set formulation of continuity, Theorem 18.1(3) (printed p. 107), a preimage of a closed set under a continuous map is closed.
:::

:::

::: {.pf-step #circle}
$S^{1}=\theset{x\times y\mid x^{2}+y^{2}=1}$ is closed in $\RR^{2}$.

::: pf-proof
$S^{1}=g^{-1}(\theset{1})$, and $\theset{1}$ is closed by step [](#closed-in-line){.pf-ref}, so Theorem 18.1(3) applies to the continuous map $g$ of step [](#maps-continuous){.pf-ref}.
:::

:::

::: {.pf-step #ball}
$B^{2}=\theset{x\times y\mid x^{2}+y^{2}\leq 1}$ is closed in $\RR^{2}$.

::: pf-proof
Since $x^{2}+y^{2}\geq 0$ for all real $x,y$, the inequality $x^{2}+y^{2}\leq 1$ is equivalent to $g(x,y)\in[0,1]$; hence $B^{2}=g^{-1}([0,1])$, and $[0,1]$ is closed by step [](#closed-in-line){.pf-ref}, so Theorem 18.1(3) makes $B^{2}$ closed.
:::

:::

::: pf-step
Therefore $A$, $S^{1}$ and $B^{2}$ are closed subsets of $\RR^{2}$.

::: pf-proof
These are steps [](#hyperbola){.pf-ref}, [](#circle){.pf-ref} and [](#ball){.pf-ref}, each of them the preimage of a closed subset of $\RR$ under one of the two continuous real-valued maps of step [](#maps-continuous){.pf-ref}.
:::

:::

:::

:::
