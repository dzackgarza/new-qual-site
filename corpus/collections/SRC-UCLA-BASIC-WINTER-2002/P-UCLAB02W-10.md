---
schema: qual/card@1
id: P-UCLAB02W-10
kind: problem
title: Finite-dimensional Riesz representation for a complex linear functional
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 10 of the official UCLA Basic Examination, Winter 2002 PDF.
---

::: {.problem}
Let $V$ be a finite-dimensional complex inner-product space and let $f:V\to\CC$ be linear.
Show that there exists $w\in V$ such that
\[
f(v)=\langle v,w\rangle
\]
for every $v\in V$.
:::

::: {.solution}

Use the convention that the complex inner product is linear in its first argument and conjugate-linear in its second, as required by the formula $f(v)=\langle v,w\rangle$ for a linear functional $f$.

::: pf

::: {.pf-step #s1-1}

Choose an orthonormal basis
$$
e_1,\ldots,e_n
$$
of $V$ and define
$$
w=\sum_{j=1}^n \overline{f(e_j)}\,e_j.
$$


::: pf-proof

A finite-dimensional complex inner-product space admits an orthonormal basis by Gram--Schmidt. The displayed finite sum therefore defines a vector $w\in V$.

:::

:::

::: {.pf-step #s1-2}

If
$$
v=\sum_{j=1}^n v_j e_j,
$$
then
$$
f(v)=\sum_{j=1}^n v_j f(e_j).
$$


::: pf-proof

This follows immediately from linearity of $f$.

:::

:::

::: {.pf-step #s1-3}

For the vector $w$ from step [](#s1-1){.pf-ref},
$$
\langle v,w\rangle
=\sum_{j=1}^n v_j f(e_j).
$$


::: pf-proof

Using linearity in the first argument, conjugate-linearity in the second, and orthonormality,
$$
\begin{aligned}
\langle v,w\rangle
&=
\left\langle
\sum_{i=1}^n v_i e_i,
\sum_{j=1}^n \overline{f(e_j)}e_j
\right\rangle\\
&=
\sum_{i,j=1}^n
v_i f(e_j)\langle e_i,e_j\rangle\\
&=
\sum_{j=1}^n v_j f(e_j).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{f(v)=\langle v,w\rangle}
$$
for every $v\in V$.


::: pf-proof

The right-hand sides obtained in steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} are identical.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} constructs the required vector $w$, and step [](#s1-4){.pf-ref} verifies that it represents $f$ on every vector in $V$.

:::

:::

:::
