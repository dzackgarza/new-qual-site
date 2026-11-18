---
schema: qual/card@1
id: E-DWC4M
kind: problem
title: The equalizer of two maps into a Hausdorff space is closed
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: Ana Emilia de Orellana, "Solutions -
    Topology Munkres", Section 31 Exercise 5, printed p. 32
    (tmp/sources/munkres-solutions-anadeore.pdf), and "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017), Problem 31.5, printed p. 5
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against Munkres, Topology (2000),
    Section 31 Exercise 5, printed p. 199, Exercise 17.13 (X is Hausdorff iff the diagonal is
    closed, printed p. 101) and Theorem 18.4 (continuity of a map into a product). What was
    corrected: Doug's World proves that the diagonal of the SUBSPACE h(D) is closed, which is
    automatic and does not give the conclusion; the card uses that the diagonal of Y x Y is closed
    in Y x Y and that E is the preimage of it under the continuous map x -> (f(x), g(x)), which is
    Orellana's argument and the standard one.
---

::: {.exercise}

Let $f, g: X \to Y$ be continuous; assume that $Y$ is Hausdorff.
Show that $\theset{x \mid f(x) = g(x)}$ is closed in $X$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, using only the definition of the product topology and the Hausdorff condition.

Let $f,g:X\to Y$ be continuous with $Y$ Hausdorff, and put $E=\theset{x\in X\mid f(x)=g(x)}$.

::: pf

::: {.pf-step #map}
$F:X\to Y\times Y$, $F(x)=\big(f(x),g(x)\big)$, is continuous.

::: pf-proof
Its coordinate functions $\pi_{1}\circ F=f$ and $\pi_{2}\circ F=g$ are continuous, so $F$ is continuous (Theorem 18.4, printed p. 110).
:::

:::

::: {.pf-step #diagonal}
$\Delta_{Y}=\theset{(y,y)\mid y\in Y}$ is closed in $Y\times Y$.

::: pf-proof
A space is Hausdorff exactly when its diagonal is closed in its square (Exercise 17.13, printed p. 101), and $Y$ is Hausdorff.
:::

:::

::: {.pf-step #preimage}
$E=F^{-1}(\Delta_{Y})$.

::: pf-proof
$x\in F^{-1}(\Delta_{Y})$ means $F(x)\in\Delta_{Y}$, that is $f(x)=g(x)$, that is $x\in E$.
:::

:::

::: {.pf-qed}
$E$ is the preimage under the continuous map $F$ of the closed set $\Delta_{Y}$, hence closed in $X$ (Theorem 18.1(3), printed p. 104).
:::

:::

:::
