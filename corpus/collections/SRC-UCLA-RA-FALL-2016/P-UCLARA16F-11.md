---
schema: qual/card@1
id: P-UCLARA16F-11
kind: problem
title: Entire functions with $f(z)f(1/z)$ bounded are monomials
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Suppose $f:\mathbb C\to\mathbb C$ is holomorphic and the function
\[
z\longmapsto g(z)=f(z)f(1/z)
\]
is bounded on $\mathbb C\setminus\{0\}$.

(a) Show that if $f(0)\ne0$, then $f$ is constant.

(b) Show that if $f(0)=0$, then there exist $n\in\mathbb N$ and $a\in\mathbb C$ such that $f(z)=az^n$ for all $z\in\mathbb C$.
:::

Assume
\[
|f(z)f(1/z)|\le M
\]
for every \(z\ne0\).

## Part (a)

Assume
\[
f(0)\ne0.
\]

::: pf

::: pf-step

Since \(f\) is continuous at \(0\),
\[
\boxed{
f(1/z)\to f(0)}
\]
as \(|z|\to\infty\).


::: pf-proof

As \(|z|\to\infty\),
\[
1/z\to0.
\]
Apply continuity of the entire function \(f\).

:::

:::

::: pf-step

There exists \(R>0\) such that for \(|z|\ge R\),
\[
\boxed{
|f(1/z)|\ge\frac{|f(0)|}{2}>0}.
\]


::: pf-proof

By step <1>1, choose \(R\) so large that
\[
|f(1/z)-f(0)|
<
\frac{|f(0)|}{2}
\]
whenever \(|z|\ge R\). The reverse triangle inequality gives
\[
|f(1/z)|
\ge
|f(0)|
-
|f(1/z)-f(0)|
>
\frac{|f(0)|}{2}.
\]

:::

:::

::: pf-step

Hence for \(|z|\ge R\),
\[
\boxed{
|f(z)|
\le
\frac{2M}{|f(0)|}}.
\]


::: pf-proof

By hypothesis,
\[
|f(z)|\,|f(1/z)|
\le
M.
\]
Use the lower bound from step <1>2 and divide.

:::

:::

::: pf-step

The function \(f\) is bounded on the closed disk
\[
\{|z|\le R\}.
\]


::: pf-proof

The entire function \(f\) is continuous, and the closed disk is compact.

:::

:::

::: pf-step

Therefore \(f\) is bounded on all of \(\mathbb C\).


::: pf-proof

Use step <1>3 outside the disk and step <1>4 inside.

:::

:::

::: pf-step

By Liouville's theorem,
\[
\boxed{
f\text{ is constant}.}
\]


::: pf-proof

An entire bounded function is constant.

:::

:::

::: pf-step

If
\[
f\equiv0,
\]
then the desired conclusion holds.


::: pf-proof

Choose any \(n\in\mathbb N\) and set
\[
a=0.
\]
Then
\[
f(z)=az^n=0.
\]

:::

:::

::: pf-step

There exists a unique integer
\[
n\ge1
\]
and an entire function \(h\) such that
\[
\boxed{
f(z)=z^n h(z)}
\]
and
\[
\boxed{
h(0)\ne0}.
\]


::: pf-proof

Since \(f\) is nonzero entire and vanishes at \(0\), the zero at \(0\) has finite positive order \(n\). Dividing the Taylor series by \(z^n\) gives an entire function \(h\) with nonzero constant term.

:::

:::

::: pf-step

For \(z\ne0\),
\[
f(1/z)
=
z^{-n}h(1/z).
\]


::: pf-proof

Apply the factorization from step <1>8 at the point \(1/z\).

:::

:::

::: pf-step

Therefore
\[
\boxed{
f(z)f(1/z)
=
h(z)h(1/z)}
\]
for every \(z\ne0\).


::: pf-proof

Multiply
\[
z^nh(z)
\]
by
\[
z^{-n}h(1/z).
\]
The powers of \(z\) cancel.

:::

:::

::: pf-step

The function
\[
z\longmapsto h(z)h(1/z)
\]
is bounded on \(\mathbb C\setminus\{0\}\).


::: pf-proof

By step <1>10, it is exactly the originally bounded function
\[
f(z)f(1/z).
\]

:::

:::

::: pf-step

Since
\[
h(0)\ne0,
\]
part (a) applies to \(h\).


::: pf-proof

The function \(h\) is entire by step <1>8, its value at \(0\) is nonzero, and its product
\[
h(z)h(1/z)
\]
is bounded by step <1>11.

:::

:::

::: pf-step

Hence
\[
\boxed{
h(z)\equiv a}
\]
for some \(a\in\mathbb C\).


::: pf-proof

Apply step <1>6 to \(h\).

:::

:::

::: pf-step

Therefore
\[
\boxed{
f(z)=az^n}
\]
for all \(z\in\mathbb C\).


::: pf-proof

Substitute the constant \(h\equiv a\) from step <1>13 into
\[
f(z)=z^nh(z).
\]

:::

:::

::: pf-qed

Step <1>6 proves part (a), and step <1>14 proves part (b).

:::

:::
