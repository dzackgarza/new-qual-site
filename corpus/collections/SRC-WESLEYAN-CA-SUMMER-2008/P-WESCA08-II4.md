---
schema: qual/card@1
id: P-WESCA08-II4
kind: problem
title: 'Analytic l’Hôpital rule from a derivative-ratio limit'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $D\subset\mathbb C$ be a domain and let $f,g:D\to\mathbb C$ be analytic.
Suppose $z_0\in D$, $f(z_0)=g(z_0)=0$, and
\[
\lim_{z\to z_0}\frac{f'(z)}{g'(z)}\in\mathbb C
\]
exists.
Show that
\[
\lim_{z\to z_0}\frac{f(z)}{g(z)}
\]
exists and calculate it.
:::

::: {.solution}
Let
\[
L
=
\lim_{z\to z_0}
\frac{f'(z)}{g'(z)}
\in\mathbb C.
\]

<1>1. The function \(g\) is not identically zero in a neighborhood of
\(z_0\).

::: {.proof}
The quotient
\[
\frac{f'(z)}{g'(z)}
\]
has an ordinary complex limit as \(z\to z_0\). In particular, it is defined
on some punctured neighborhood of \(z_0\), so \(g'\) cannot vanish
identically there. Hence \(g\) is not locally constant, and since
\[
g(z_0)=0,
\]
it is not identically zero near \(z_0\).
:::

<1>2. Suppose first that \(f\) is not identically zero near \(z_0\). Then
there are integers
\[
m,n\ge1
\]
and analytic functions \(F,G\), nonzero at \(z_0\), such that
\[
\boxed{
f(z)
=
(z-z_0)^mF(z)}
\]
and
\[
\boxed{
g(z)
=
(z-z_0)^nG(z)}.
\]

::: {.proof}
A nonzero analytic function has an isolated zero of finite order. Since
\[
f(z_0)=g(z_0)=0,
\]
their orders of vanishing are positive integers \(m,n\).
:::

<1>3. Differentiating the factorizations in step <1>2 gives
\[
f'(z)
=
(z-z_0)^{m-1}
\left(
mF(z)+(z-z_0)F'(z)
\right)
\]
and
\[
g'(z)
=
(z-z_0)^{n-1}
\left(
nG(z)+(z-z_0)G'(z)
\right).
\]

::: {.proof}
Apply the product rule.
:::

<1>4. Define
\[
F_1(z)
=
mF(z)+(z-z_0)F'(z)
\]
and
\[
G_1(z)
=
nG(z)+(z-z_0)G'(z).
\]
Then
\[
\boxed{
F_1(z_0)=mF(z_0)\ne0}
\]
and
\[
\boxed{
G_1(z_0)=nG(z_0)\ne0}.
\]

::: {.proof}
Substitute \(z=z_0\). The nonvanishing follows from
\[
m,n\ge1
\]
and
\[
F(z_0),G(z_0)\ne0.
\]
:::

<1>5. For \(z\ne z_0\) sufficiently close to \(z_0\),
\[
\boxed{
\frac{f'(z)}{g'(z)}
=
(z-z_0)^{m-n}
\frac{F_1(z)}{G_1(z)}}.
\]

::: {.proof}
Divide the two derivative formulas in step <1>3. By step <1>4,
\(G_1\) is nonzero in some neighborhood of \(z_0\).
:::

<1>6. The existence of the finite limit \(L\) forces
\[
\boxed{m\ge n}.
\]

::: {.proof}
If \(m<n\), then step <1>5 gives
\[
\left|
\frac{f'(z)}{g'(z)}
\right|
=
|z-z_0|^{m-n}
\left|
\frac{F_1(z)}{G_1(z)}
\right|.
\]
The second factor tends to the nonzero finite number
\[
\left|
\frac{mF(z_0)}{nG(z_0)}
\right|,
\]
while \(m-n<0\), so the first factor tends to \(+\infty\). This contradicts
the assumed finite limit.
:::

<1>7. If
\[
m>n,
\]
then
\[
\boxed{L=0}.
\]

::: {.proof}
In step <1>5, the analytic quotient
\[
F_1/G_1
\]
tends to a finite nonzero value, while
\[
(z-z_0)^{m-n}\to0.
\]
Thus the derivative ratio tends to \(0\).
:::

<1>8. If
\[
m=n,
\]
then
\[
\boxed{
L
=
\frac{F(z_0)}{G(z_0)}}.
\]

::: {.proof}
Step <1>5 gives
\[
L
=
\frac{F_1(z_0)}{G_1(z_0)}
=
\frac{mF(z_0)}{mG(z_0)}
=
\frac{F(z_0)}{G(z_0)}.
\]
:::

<1>9. For \(z\ne z_0\) sufficiently close to \(z_0\),
\[
\boxed{
\frac{f(z)}{g(z)}
=
(z-z_0)^{m-n}
\frac{F(z)}{G(z)}}.
\]

::: {.proof}
Divide the factorizations from step <1>2.
:::

<1>10. If \(m>n\), then
\[
\boxed{
\lim_{z\to z_0}
\frac{f(z)}{g(z)}
=
0
=
L}.
\]

::: {.proof}
In step <1>9,
\[
F(z)/G(z)
\to
F(z_0)/G(z_0),
\]
a finite nonzero number, while
\[
(z-z_0)^{m-n}\to0.
\]
Use step <1>7 for the value of \(L\).
:::

<1>11. If \(m=n\), then
\[
\boxed{
\lim_{z\to z_0}
\frac{f(z)}{g(z)}
=
\frac{F(z_0)}{G(z_0)}
=
L}.
\]

::: {.proof}
Set \(m-n=0\) in step <1>9 and use continuity of \(F/G\), then apply
step <1>8.
:::

<1>12. If \(f\) is identically zero in a neighborhood of \(z_0\), then
\[
\boxed{L=0}
\]
and
\[
\boxed{
\lim_{z\to z_0}
\frac{f(z)}{g(z)}
=
0}.
\]

::: {.proof}
Then
\[
f'(z)=0
\]
near \(z_0\), so wherever the derivative ratio is defined it equals \(0\).
Thus \(L=0\).

Since \(g\) is not identically zero by step <1>1, its zeros are isolated.
For all \(z\ne z_0\) sufficiently close to \(z_0\) with \(g(z)\ne0\),
\[
\frac{f(z)}{g(z)}=0.
\]
Hence the quotient limit is \(0\).
:::

<1>13. Therefore in all cases,
\[
\boxed{
\lim_{z\to z_0}
\frac{f(z)}{g(z)}
=
\lim_{z\to z_0}
\frac{f'(z)}{g'(z)}
=
L}.
\]

::: {.proof}
If \(f\) is locally nonzero, steps <1>6, <1>10, and <1>11 exhaust the
possibilities. If \(f\) is locally identically zero, use step <1>12.
:::

<1>14. Q.E.D.

::: {.proof}
Step <1>13 proves existence of the requested limit and calculates it.
:::
:::
