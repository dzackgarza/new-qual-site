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

::: {.solution}
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

<1>1. Since \(f\) is continuous at \(0\),
\[
\boxed{
f(1/z)\to f(0)}
\]
as \(|z|\to\infty\).

::: {.proof}
As \(|z|\to\infty\),
\[
1/z\to0.
\]
Apply continuity of the entire function \(f\).
:::

<1>2. There exists \(R>0\) such that for \(|z|\ge R\),
\[
\boxed{
|f(1/z)|\ge\frac{|f(0)|}{2}>0}.
\]

::: {.proof}
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

<1>3. Hence for \(|z|\ge R\),
\[
\boxed{
|f(z)|
\le
\frac{2M}{|f(0)|}}.
\]

::: {.proof}
By hypothesis,
\[
|f(z)|\,|f(1/z)|
\le
M.
\]
Use the lower bound from step <1>2 and divide.
:::

<1>4. The function \(f\) is bounded on the closed disk
\[
\{|z|\le R\}.
\]

::: {.proof}
The entire function \(f\) is continuous, and the closed disk is compact.
:::

<1>5. Therefore \(f\) is bounded on all of \(\mathbb C\).

::: {.proof}
Use step <1>3 outside the disk and step <1>4 inside.
:::

<1>6. By Liouville's theorem,
\[
\boxed{
f\text{ is constant}.}
\]

::: {.proof}
An entire bounded function is constant.
:::

## Part (b)

Assume now
\[
f(0)=0.
\]

<1>7. If
\[
f\equiv0,
\]
then the desired conclusion holds.

::: {.proof}
Choose any \(n\in\mathbb N\) and set
\[
a=0.
\]
Then
\[
f(z)=az^n=0.
\]
:::

Assume henceforth
\[
f\not\equiv0.
\]

<1>8. There exists a unique integer
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

::: {.proof}
Since \(f\) is nonzero entire and vanishes at \(0\), the zero at \(0\) has finite positive order \(n\). Dividing the Taylor series by \(z^n\) gives an entire function \(h\) with nonzero constant term.
:::

<1>9. For \(z\ne0\),
\[
f(1/z)
=
z^{-n}h(1/z).
\]

::: {.proof}
Apply the factorization from step <1>8 at the point \(1/z\).
:::

<1>10. Therefore
\[
\boxed{
f(z)f(1/z)
=
h(z)h(1/z)}
\]
for every \(z\ne0\).

::: {.proof}
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

<1>11. The function
\[
z\longmapsto h(z)h(1/z)
\]
is bounded on \(\mathbb C\setminus\{0\}\).

::: {.proof}
By step <1>10, it is exactly the originally bounded function
\[
f(z)f(1/z).
\]
:::

<1>12. Since
\[
h(0)\ne0,
\]
part (a) applies to \(h\).

::: {.proof}
The function \(h\) is entire by step <1>8, its value at \(0\) is nonzero, and its product
\[
h(z)h(1/z)
\]
is bounded by step <1>11.
:::

<1>13. Hence
\[
\boxed{
h(z)\equiv a}
\]
for some \(a\in\mathbb C\).

::: {.proof}
Apply step <1>6 to \(h\).
:::

<1>14. Therefore
\[
\boxed{
f(z)=az^n}
\]
for all \(z\in\mathbb C\).

::: {.proof}
Substitute the constant \(h\equiv a\) from step <1>13 into
\[
f(z)=z^nh(z).
\]
:::

<1>15. Q.E.D.

::: {.proof}
Step <1>6 proves part (a), and step <1>14 proves part (b).
:::
:::
