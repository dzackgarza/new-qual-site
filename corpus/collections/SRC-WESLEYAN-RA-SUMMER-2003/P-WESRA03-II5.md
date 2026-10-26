---
schema: qual/card@1
id: P-WESRA03-II5
kind: problem
title: Failure of equality of iterated integrals with counting measure
classification:
  areas: [real-analysis]
  topics: [Tonelli-Fubini Theorem, Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, Problem 5 in the deterministic MinerU Flash extraction of analysis_2003-2007.pdf.
---

::: {.problem}
Let $X=\mathbb R$, let $\mathcal B(\mathbb R)$ be the Borel sigma-algebra, let $m$ be Lebesgue measure, and let $\sigma$ be counting measure on $\mathbb R$.
Define $f:\mathbb R^2\to\mathbb R$ by
\[
f(x,y)=
\begin{cases}
1,&x=y,\\
0,&x\ne y.
\end{cases}
\]
Show that
\[
\int_X\!\int_X f(x,y)\,dm(x)\,d\sigma(y)
\ne
\int_X\!\int_X f(x,y)\,d\sigma(y)\,dm(x).
\]
:::

Let
\[
D=\{(x,y)\in\mathbb R^2:x=y\}
\]
be the diagonal. Then
\[
f=\mathbf 1_D.
\]

::: pf

::: pf-step

The function \(f\) is Borel measurable.


::: pf-proof

The diagonal is closed:
\[
D
=
\{(x,y):x-y=0\}
\]
is the inverse image of the closed set \(\{0\}\) under the continuous map
\[
(x,y)\longmapsto x-y.
\]
Hence \(D\) is Borel, so its indicator is Borel measurable.

:::

:::

::: pf-step

Fix \(y\in\mathbb R\). Then
\[
\boxed{
f(x,y)=\mathbf 1_{\{y\}}(x)}.
\]


::: pf-proof

By definition,
\[
f(x,y)=1
\iff
x=y.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\int_{\mathbb R}f(x,y)\,dm(x)=0}.
\]


::: pf-proof

The singleton \(\{y\}\) has Lebesgue measure zero. Hence
\[
\int_{\mathbb R}\mathbf 1_{\{y\}}\,dm
=
m(\{y\})
=
0.
\]

:::

:::

::: pf-step

Consequently,
\[
\boxed{
\int_{\mathbb R}
\left(
\int_{\mathbb R}
f(x,y)\,dm(x)
\right)
d\sigma(y)
=
0}.
\]


::: pf-proof

By step <1>3, the inner integral is the zero function of \(y\). The integral
of the zero function with respect to any measure is zero.

:::

:::

::: pf-step

Fix \(x\in\mathbb R\). Then
\[
\boxed{
f(x,y)=\mathbf 1_{\{x\}}(y)}.
\]


::: pf-proof

Again,
\[
f(x,y)=1
\iff
y=x.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\int_{\mathbb R}f(x,y)\,d\sigma(y)=1}.
\]


::: pf-proof

Counting measure assigns to a singleton the value
\[
\sigma(\{x\})=1.
\]
Hence
\[
\int_{\mathbb R}\mathbf 1_{\{x\}}\,d\sigma
=
1.
\]

:::

:::

::: pf-step

Consequently,
\[
\int_{\mathbb R}
\left(
\int_{\mathbb R}
f(x,y)\,d\sigma(y)
\right)
dm(x)
=
\int_{\mathbb R}1\,dm(x).
\]


::: pf-proof

Substitute the constant value from step <1>6.

:::

:::

::: pf-step

The last integral equals
\[
\boxed{+\infty}.
\]


::: pf-proof

Lebesgue measure of \(\mathbb R\) is infinite:
\[
\int_{\mathbb R}1\,dm
=
m(\mathbb R)
=
\infty.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
\int_X\!\int_X
f(x,y)\,dm(x)\,d\sigma(y)
=
0}
\]
while
\[
\boxed{
\int_X\!\int_X
f(x,y)\,d\sigma(y)\,dm(x)
=
\infty}.
\]


::: pf-proof

The first equality is step <1>4 and the second is steps <1>7--<1>8.

:::

:::

::: pf-step

Therefore the two iterated integrals are unequal.


::: pf-proof

One is \(0\) and the other is \(+\infty\).

:::

:::

::: pf-step

This does not contradict Tonelli--Fubini because counting measure on
the uncountable set \(\mathbb R\) is not \(\sigma\)-finite.


::: pf-proof

Every set of finite counting measure is finite. A countable union of finite
sets is countable, so \(\mathbb R\) cannot be written as a countable union of
sets of finite counting measure. Thus \(\sigma\) is not \(\sigma\)-finite,
and the usual Tonelli--Fubini hypotheses fail.

:::

:::

::: pf-qed

Step <1>10 is the required inequality.

:::

:::
