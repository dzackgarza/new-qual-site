---
schema: qual/card@1
id: P-UGAP08S-06
kind: problem
title: Zeros of every derivative from zeros at all integers
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction drops x after “integer” and mangles the reference to the nth derivative; the surrounding Rolle-theorem statement uniquely determines the restored notation.
---

::: {.problem}
Let $f:\RR\to\RR$ have derivatives of all orders, and suppose
\[
f(x)=0
\]
for every integer $x$. Prove that for each $n\in\NN$, the $n$th derivative $f^{(n)}$ has at least one root.
:::

::: {.solution}

We prove the stronger statement that every derivative
\[
f^{(n)}
\]
has infinitely many zeros.

::: pf

::: {.pf-step #s1-1}

The function
\[
f
\]
has the strictly increasing sequence of zeros
\[
x_k^{(0)}
\coloneqq
k,
\qquad
k\in\ZZ.
\]


::: pf-proof

This is exactly the hypothesis
\[
f(k)=0
\]
for every integer $k$.

:::

:::

::: pf-step

Suppose for some
\[
m\ge0
\]
that
\[
f^{(m)}
\]
has a strictly increasing bi-infinite sequence of zeros
\[
\cdots
<
x_{-1}^{(m)}
<
x_0^{(m)}
<
x_1^{(m)}
<
\cdots.
\]


::: pf-proof

This is the induction hypothesis.
The case
\[
m=0
\]
is step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

For every
\[
k\in\ZZ,
\]
there exists
\[
x_k^{(m+1)}
\in
\left(
x_k^{(m)},
x_{k+1}^{(m)}
\right)
\]
such that
\[
f^{(m+1)}
\left(
x_k^{(m+1)}
\right)
=
0.
\]


::: pf-proof

The function
\[
f^{(m)}
\]
is differentiable on
\[
\RR
\]
because $f$ has derivatives of all orders.
Hence it is continuous on the closed interval
\[
[x_k^{(m)},x_{k+1}^{(m)}]
\]
and differentiable on its interior.

The two endpoint values are equal:
\[
f^{(m)}(x_k^{(m)})
=
0
=
f^{(m)}(x_{k+1}^{(m)}).
\]
By Rolle's theorem, there exists a point
\[
x_k^{(m+1)}
\]
strictly between the endpoints where
\[
(f^{(m)})'
=
f^{(m+1)}
\]
vanishes.

:::

:::

::: {.pf-step #s1-4}

The sequence
\[
\{x_k^{(m+1)}\}_{k\in\ZZ}
\]
is strictly increasing.


::: pf-proof

For every $k$,
\[
x_k^{(m+1)}
\in
(x_k^{(m)},x_{k+1}^{(m)})
\]
and
\[
x_{k+1}^{(m+1)}
\in
(x_{k+1}^{(m)},x_{k+2}^{(m)}).
\]
Therefore
\[
x_k^{(m+1)}
<
x_{k+1}^{(m)}
<
x_{k+1}^{(m+1)}.
\]

:::

:::

::: {.pf-step #s1-5}

Thus if
\[
f^{(m)}
\]
has infinitely many zeros, then so does
\[
f^{(m+1)}.
\]


::: pf-proof

Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} construct a strictly increasing bi-infinite sequence of
zeros of
\[
f^{(m+1)}.
\]

:::

:::

::: {.pf-step #s1-6}

By induction, for every
\[
n\in\NN,
\]
the derivative
\[
f^{(n)}
\]
has infinitely many roots.


::: pf-proof

Step [](#s1-1){.pf-ref} gives the base case.
Step [](#s1-5){.pf-ref} gives the induction step.

:::

:::

::: {.pf-step #s1-7}

In particular, for every
\[
n\in\NN,
\]
the derivative
\[
f^{(n)}
\]
has at least one root.


::: pf-proof

This is immediate from the stronger conclusion in step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
