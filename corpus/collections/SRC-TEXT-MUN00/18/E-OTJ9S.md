---
schema: qual/card@1
id: E-OTJ9S
kind: problem
title: Coordinate slices are imbeddings
classification:
  areas:
  - topology
  topics:
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 4, printed p. 111, with Theorem
    18.2, Theorem 18.4 and the definition of imbedding on printed pp. 105-110; the stored
    statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 18.4, printed p. 180.
    His proof for f, which is the same for g: injective, continuous because both components
    are (identity and constant), and an imbedding because on its image it is inverse to the
    projection pi_1, which is continuous by Theorem 18.4. (tmp/sources/munkres-solutions-
    whitman.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and checked each claim against Munkres §18 Exercise 4,
    printed p. 111: injectivity, continuity from the two components by Theorem 18.4, and the
    inverse on the image as the restriction of pi_1 (also Theorem 18.4), with Theorem
    18.2(e) for the restriction of the range. Whitman, Exercise 18.4, printed p. 180;
    positron0802, Exercise 18.4, PDF p. 11. The printed statement needed no repair.
---

::: {.exercise}

Given $x_0 \in X$ and $y_0 \in Y$, show that the maps $f: X \to X \times Y$ and $g: Y \to X \times Y$ defined by

$$
f(x) = x \times y_0 \quad \text{and} \quad g(y) = x_0 \times y
$$

are imbeddings.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 18.4, printed p. 180** (`tmp/sources/munkres-solutions-whitman.pdf`); the proof for $f$ is his and $g$ is the same argument. "positron0802", *Solutions to Topology, Chapter 2*, Exercise 18.4, PDF p. 11, states the same in one line.

::: pf

::: {.pf-step #injective}
$f:X\to X\times Y$, $f(x)=x\times y_{0}$, is injective.

::: pf-proof
If $f(x)=f(x')$ then the first coordinates of the two ordered pairs agree, that is $x=x'$.
:::

:::

::: {.pf-step #continuous}
$f$ is continuous.

::: pf-proof
The components of $f$ are $\pi_{1}\circ f$, which is the identity map $x\mapsto x$ of $X$, and $\pi_{2}\circ f$, which is the constant map $x\mapsto y_{0}$. Both are continuous (Theorem 18.2). A map into a product is continuous when each of its components is (Theorem 18.4, printed p. 110), so $f$ is continuous.
:::

:::

::: {.pf-step #onto-image}
$f':X\to f(X)$, $f'(x)=f(x)$, is a homeomorphism onto the subspace $f(X)$ of $X\times Y$.

::: pf-proof
$f'$ is a bijection by step [](#injective){.pf-ref}. It is continuous because $f$ is (Theorem 18.2(e): the restriction of a continuous map to a smaller range is continuous). Let $p:f(X)\to X$ be the restriction of $\pi_{1}$ to $f(X)$; it is continuous as a restriction of the continuous map $\pi_{1}$ (Theorem 18.4). For $x\in X$ one has $p\big(f'(x)\big)=x$, and for $(x,y_{0})\in f(X)$ one has $f'\big(p(x,y_{0})\big)=f'(x)=x\times y_{0}$; so $p$ is the inverse of $f'$. A bijection whose inverse is continuous is a homeomorphism.
:::

:::

::: {.pf-step #f-imbedding}
$f$ is an imbedding.

::: pf-proof
An imbedding is an injective continuous map that is a homeomorphism onto its image in the subspace topology. Steps [](#injective){.pf-ref}, [](#continuous){.pf-ref} and [](#onto-image){.pf-ref} establish exactly this for $f$.
:::

:::

::: {.pf-step #g-imbedding}
$g:Y\to X\times Y$, $g(y)=x_{0}\times y$, is an imbedding.

::: pf-proof
The argument of steps [](#injective){.pf-ref}, [](#continuous){.pf-ref} and [](#onto-image){.pf-ref} repeats with the two factors exchanged: $g$ is injective because its second coordinate determines $y$; its components are the constant map $y\mapsto x_{0}$ and the identity of $Y$, both continuous, so it is continuous by Theorem 18.4; and on its image it is inverse to the restriction of $\pi_{2}$, which is continuous. Hence $g$ is an imbedding.
:::

:::

:::
:::
