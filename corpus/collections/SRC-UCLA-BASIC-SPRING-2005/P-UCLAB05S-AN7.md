---
schema: qual/card@1
id: P-UCLAB05S-AN7
kind: problem
title: Openness of invertibility and continuity of matrix inversion
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Analysis Problem 7 of the official UCLA Basic Exam, May 2005 PDF. The source parenthetically calls the displayed metric the usual metric on $\RR^{n^2}$; for complex matrices it is the Euclidean metric on $\CC^{n^2}\cong\RR^{2n^2}$.
---

::: {.problem}
Equip $M_n(\CC)$ with the metric
$$
\operatorname{dist}(A,B)
=\left(\sum_{i,j}|A_{ij}-B_{ij}|^2\right)^{1/2}.
$$

(a) Suppose $F:\RR\to M_n(\CC)$ is continuous.
Show that
$$
\{x\in\RR:F(x)\text{ is invertible}\}
$$
is open in the usual topology on $\RR$.

(b) Show that on the set above, the map
$$
x\longmapsto F(x)^{-1}
$$
is continuous.
:::

::: {.solution}

Let
$$
U\coloneqq\{x\in\RR:F(x)\text{ is invertible}\}.
$$

::: pf

::: {.pf-step #s1-1}

The function
$$
x\longmapsto\det F(x)
$$
is continuous on $\RR$.


::: pf-proof

Continuity of $F$ for the displayed Euclidean matrix metric is equivalent to continuity of each matrix-entry function $x\mapsto F_{ij}(x)$. The determinant is a polynomial in the matrix entries, so its composition with $F$ is continuous.

:::

:::

::: {.pf-step #s1-2}

The set $U$ is open in $\RR$.


::: pf-proof

A complex matrix is invertible exactly when its determinant is nonzero. Hence
$$
U=(\det\circ F)^{-1}(\CC\setminus\{0\}).
$$
The set $\CC\setminus\{0\}$ is open, and $\det\circ F$ is continuous by step [](#s1-1){.pf-ref}. Therefore $U$ is open.

:::

:::

::: {.pf-step #s1-3}

On $U$,
$$
F(x)^{-1}=\frac{\operatorname{adj}(F(x))}{\det F(x)}.
$$


::: pf-proof

This is the adjugate formula for the inverse of an invertible matrix.

:::

:::

::: {.pf-step #s1-4}

Every entry of the matrix-valued map $x\mapsto F(x)^{-1}$ is continuous on $U$.


::: pf-proof

Each entry of $\operatorname{adj}(F(x))$ is, up to sign, a determinant of an $(n-1)\times(n-1)$ minor of $F(x)$, hence is a polynomial in the entries of $F(x)$ and therefore continuous. By definition of $U$, the denominator $\det F(x)$ never vanishes there. Thus each entry in the quotient formula from step [](#s1-3){.pf-ref} is continuous on $U$.

:::

:::

::: {.pf-step #s1-5}

The map
$$
\boxed{U\longrightarrow M_n(\CC),\qquad x\longmapsto F(x)^{-1}}
$$
is continuous.


::: pf-proof

The metric on $M_n(\CC)$ is the Euclidean metric on its finitely many complex coordinates. A matrix-valued map into this space is continuous exactly when all of its coordinate functions are continuous. Apply step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), and step [](#s1-5){.pf-ref} proves part (b).

:::

:::

:::
