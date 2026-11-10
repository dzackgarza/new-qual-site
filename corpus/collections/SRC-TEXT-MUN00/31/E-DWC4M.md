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
    closed, printed p. 100) and Theorem 18.4 (continuity of a map into a product). What was
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
Let
$$
E=\{x\in X:f(x)=g(x)\}.
$$
The map
$$
F:X\to Y\times Y,\qquad F(x)=(f(x),g(x))
$$
is continuous. Since $Y$ is Hausdorff, its diagonal
$$
\Delta_Y=\{(y,y):y\in Y\}
$$
is closed in $Y\times Y$. Hence
$$
E=F^{-1}(\Delta_Y)
$$
is closed in $X$.
:::
