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
Let $X=\RR$, let $\mathcal B(\RR)$ be the Borel sigma-algebra, let $m$ be Lebesgue measure, and let $\sigma$ be counting measure on $\RR$.
Define $f:\RR^2\to\RR$ by
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

::: {.solution}

Let
\[
D=\{(x,y)\in\RR^2:x=y\}
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

Fix \(y\in\RR\). Then
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

::: {.pf-step #s1-3}

Therefore
\[
\boxed{
\int_{\RR}f(x,y)\,dm(x)=0}.
\]


::: pf-proof

The singleton \(\{y\}\) has Lebesgue measure zero. Hence
\[
\int_{\RR}\mathbf 1_{\{y\}}\,dm
=
m(\{y\})
=
0.
\]

:::

:::

::: {.pf-step #s1-4}

Consequently,
\[
\boxed{
\int_{\RR}
\left(
\int_{\RR}
f(x,y)\,dm(x)
\right)
d\sigma(y)
=
0}.
\]


::: pf-proof

By step [](#s1-3){.pf-ref}, the inner integral is the zero function of \(y\). The integral
of the zero function with respect to any measure is zero.

:::

:::

::: pf-step

Fix \(x\in\RR\). Then
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

::: {.pf-step #s1-6}

Therefore
\[
\boxed{
\int_{\RR}f(x,y)\,d\sigma(y)=1}.
\]


::: pf-proof

Counting measure assigns to a singleton the value
\[
\sigma(\{x\})=1.
\]
Hence
\[
\int_{\RR}\mathbf 1_{\{x\}}\,d\sigma
=
1.
\]

:::

:::

::: {.pf-step #s1-7}

Consequently,
\[
\int_{\RR}
\left(
\int_{\RR}
f(x,y)\,d\sigma(y)
\right)
dm(x)
=
\int_{\RR}1\,dm(x).
\]


::: pf-proof

Substitute the constant value from step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

The last integral equals
\[
\boxed{+\infty}.
\]


::: pf-proof

Lebesgue measure of \(\RR\) is infinite:
\[
\int_{\RR}1\,dm
=
m(\RR)
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

The first equality is step [](#s1-4){.pf-ref} and the second is steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Therefore the two iterated integrals are unequal.


::: pf-proof

One is \(0\) and the other is \(+\infty\).

:::

:::

::: pf-step

This does not contradict Tonelli--Fubini because counting measure on
the uncountable set \(\RR\) is not \(\sigma\)-finite.


::: pf-proof

Every set of finite counting measure is finite. A countable union of finite
sets is countable, so \(\RR\) cannot be written as a countable union of
sets of finite counting measure. Thus \(\sigma\) is not \(\sigma\)-finite,
and the usual Tonelli--Fubini hypotheses fail.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required inequality.

:::

:::

:::
