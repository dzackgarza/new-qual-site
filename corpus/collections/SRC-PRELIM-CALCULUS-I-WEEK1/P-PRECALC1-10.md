---
schema: qual/card@1
id: P-PRECALC1-10
kind: problem
title: The product $e^{g}h$ when $h'=-g'h$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f ( x ) = e ^ { g ( x ) } h ( x )$ where $h ^ { \prime } ( x ) = - g ^ { \prime } ( x ) h ( x )$ for all $x \in \mathbb { R }$ . Which of the following is necessarily true? (a) f is constant $( \mathrm { b } ) \ f$ is linear and non-constant (c) g is constant (d) g is linear and non-constant (e) none of the above
:::

::: pf

::: pf-step

Differentiate
\[
f(x)=e^{g(x)}h(x).
\]


::: pf-proof

Use the product rule and the chain rule.

:::

:::

::: pf-step

One obtains
\[
\boxed{
f'(x)
=
e^{g(x)}g'(x)h(x)
+
e^{g(x)}h'(x)}.
\]


::: pf-proof

The derivative of
\[
e^{g(x)}
\]
is
\[
e^{g(x)}g'(x).
\]

:::

:::

::: pf-step

Factor out \(e^{g(x)}\):
\[
\boxed{
f'(x)
=
e^{g(x)}
\left(
g'(x)h(x)+h'(x)
\right)}.
\]


::: pf-proof

This is an algebraic factorization of step <1>2.

:::

:::

::: pf-step

The given relation
\[
h'(x)=-g'(x)h(x)
\]
implies
\[
g'(x)h(x)+h'(x)=0.
\]


::: pf-proof

Substitute the stated formula for \(h'(x)\).

:::

:::

::: pf-step

Hence
\[
\boxed{
f'(x)=0}
\]
for every \(x\in\mathbb R\).


::: pf-proof

Combine steps <1>3--<1>4.

:::

:::

::: pf-step

Therefore \(f\) is constant on \(\mathbb R\).


::: pf-proof

A differentiable function whose derivative is identically zero on an interval
is constant there. The real line is an interval.

:::

:::

::: pf-step

Thus the necessarily true statement is
\[
\boxed{\text{(a) }f\text{ is constant}.}
\]


::: pf-proof

This is step <1>6.

:::

:::

::: pf-qed

Step <1>7 gives the required choice.

:::

:::
