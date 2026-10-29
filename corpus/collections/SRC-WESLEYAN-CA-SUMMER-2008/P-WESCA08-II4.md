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
Let $D\subset\CC$ be a domain and let $f,g:D\to\CC$ be analytic.
Suppose $z_0\in D$, $f(z_0)=g(z_0)=0$, and
\[
\lim_{z\to z_0}\frac{f'(z)}{g'(z)}\in\CC
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
\in\CC.
\]

::: pf

::: {.pf-step #s1-1}

The function \(g\) is not identically zero in a neighborhood of
\(z_0\).


::: pf-proof

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

:::

::: {.pf-step #s1-2}

Suppose first that \(f\) is not identically zero near \(z_0\). Then
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


::: pf-proof

A nonzero analytic function has an isolated zero of finite order. Since
\[
f(z_0)=g(z_0)=0,
\]
their orders of vanishing are positive integers \(m,n\).

:::

:::

::: {.pf-step #s1-3}

Differentiating the factorizations in step [](#s1-2){.pf-ref} gives
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


::: pf-proof

Apply the product rule.

:::

:::

::: {.pf-step #s1-4}

Define
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


::: pf-proof

Substitute \(z=z_0\). The nonvanishing follows from
\[
m,n\ge1
\]
and
\[
F(z_0),G(z_0)\ne0.
\]

:::

:::

::: {.pf-step #s1-5}

For \(z\ne z_0\) sufficiently close to \(z_0\),
\[
\boxed{
\frac{f'(z)}{g'(z)}
=
(z-z_0)^{m-n}
\frac{F_1(z)}{G_1(z)}}.
\]


::: pf-proof

Divide the two derivative formulas in step [](#s1-3){.pf-ref}. By step [](#s1-4){.pf-ref},
\(G_1\) is nonzero in some neighborhood of \(z_0\).

:::

:::

::: {.pf-step #s1-6}

The existence of the finite limit \(L\) forces
\[
\boxed{m\ge n}.
\]


::: pf-proof

If \(m<n\), then step [](#s1-5){.pf-ref} gives
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

:::

::: {.pf-step #s1-7}

If
\[
m>n,
\]
then
\[
\boxed{L=0}.
\]


::: pf-proof

In step [](#s1-5){.pf-ref}, the analytic quotient
\[
F_1/G_1
\]
tends to a finite nonzero value, while
\[
(z-z_0)^{m-n}\to0.
\]
Thus the derivative ratio tends to \(0\).

:::

:::

::: {.pf-step #s1-8}

If
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


::: pf-proof

Step [](#s1-5){.pf-ref} gives
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

:::

::: {.pf-step #s1-9}

For \(z\ne z_0\) sufficiently close to \(z_0\),
\[
\boxed{
\frac{f(z)}{g(z)}
=
(z-z_0)^{m-n}
\frac{F(z)}{G(z)}}.
\]


::: pf-proof

Divide the factorizations from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

If \(m>n\), then
\[
\boxed{
\lim_{z\to z_0}
\frac{f(z)}{g(z)}
=
0
=
L}.
\]


::: pf-proof

In step [](#s1-9){.pf-ref},
\[
F(z)/G(z)
\to
F(z_0)/G(z_0),
\]
a finite nonzero number, while
\[
(z-z_0)^{m-n}\to0.
\]
Use step [](#s1-7){.pf-ref} for the value of \(L\).

:::

:::

::: {.pf-step #s1-11}

If \(m=n\), then
\[
\boxed{
\lim_{z\to z_0}
\frac{f(z)}{g(z)}
=
\frac{F(z_0)}{G(z_0)}
=
L}.
\]


::: pf-proof

Set \(m-n=0\) in step [](#s1-9){.pf-ref} and use continuity of \(F/G\), then apply
step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

If \(f\) is identically zero in a neighborhood of \(z_0\), then
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


::: pf-proof

Then
\[
f'(z)=0
\]
near \(z_0\), so wherever the derivative ratio is defined it equals \(0\).
Thus \(L=0\).

Since \(g\) is not identically zero by step [](#s1-1){.pf-ref}, its zeros are isolated.
For all \(z\ne z_0\) sufficiently close to \(z_0\) with \(g(z)\ne0\),
\[
\frac{f(z)}{g(z)}=0.
\]
Hence the quotient limit is \(0\).

:::

:::

::: {.pf-step #s1-13}

Therefore in all cases,
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


::: pf-proof

If \(f\) is locally nonzero, steps [](#s1-6){.pf-ref} and [](#s1-10){.pf-ref}, and [](#s1-11){.pf-ref} exhaust the
possibilities. If \(f\) is locally identically zero, use step [](#s1-12){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} proves existence of the requested limit and calculates it.

:::

:::

:::
