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

::: {.solution}
<1>1. Differentiate
\[
f(x)=e^{g(x)}h(x).
\]

::: {.proof}
Use the product rule and the chain rule.
:::

<1>2. One obtains
\[
\boxed{
f'(x)
=
e^{g(x)}g'(x)h(x)
+
e^{g(x)}h'(x)}.
\]

::: {.proof}
The derivative of
\[
e^{g(x)}
\]
is
\[
e^{g(x)}g'(x).
\]
:::

<1>3. Factor out \(e^{g(x)}\):
\[
\boxed{
f'(x)
=
e^{g(x)}
\left(
g'(x)h(x)+h'(x)
\right)}.
\]

::: {.proof}
This is an algebraic factorization of step <1>2.
:::

<1>4. The given relation
\[
h'(x)=-g'(x)h(x)
\]
implies
\[
g'(x)h(x)+h'(x)=0.
\]

::: {.proof}
Substitute the stated formula for \(h'(x)\).
:::

<1>5. Hence
\[
\boxed{
f'(x)=0}
\]
for every \(x\in\mathbb R\).

::: {.proof}
Combine steps <1>3--<1>4.
:::

<1>6. Therefore \(f\) is constant on \(\mathbb R\).

::: {.proof}
A differentiable function whose derivative is identically zero on an interval
is constant there. The real line is an interval.
:::

<1>7. Thus the necessarily true statement is
\[
\boxed{\text{(a) }f\text{ is constant}.}
\]

::: {.proof}
This is step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 gives the required choice.
:::
:::
