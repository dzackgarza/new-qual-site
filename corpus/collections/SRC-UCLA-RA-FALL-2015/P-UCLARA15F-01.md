---
schema: qual/card@1
id: P-UCLARA15F-01
kind: problem
title: Locally uniform convergence of $f*g_n$ for bounded $g_n\to0$ almost everywhere
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
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 1 on page 1 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $g_n$ be a sequence of measurable functions on $\mathbb{R}^d$, such that $|g_n(x)| \leq 1$ for all $x$, and assume that $g_n \to 0$ almost everywhere. Let $f \in L^1(\mathbb{R}^d)$. Show that the sequence
\[
f * g_n(x) = \int f(x-y) g_n(y)\,dy \to 0
\]
uniformly on each compact subset of $\mathbb{R}^d$, as $n \to \infty$.
:::

Let
\[
K\subset\mathbb R^d
\]
be compact. We prove
\[
\sup_{x\in K}|(f*g_n)(x)|\to0.
\]

## Approximate \(f\) by a compactly supported continuous function

::: pf

::: pf-step

Fix
\[
\varepsilon>0.
\]
Choose
\[
\varphi\in C_c(\mathbb R^d)
\]
such that
\[
\boxed{
\|f-\varphi\|_{L^1}<\frac{\varepsilon}{3}}.
\]


::: pf-proof

The space \(C_c(\mathbb R^d)\) is dense in \(L^1(\mathbb R^d)\).

:::

:::

::: pf-step

For every \(x\in\mathbb R^d\) and every \(n\),
\[
\boxed{
|((f-\varphi)*g_n)(x)|
\le
\|f-\varphi\|_{L^1}}.
\]


::: pf-proof

Since
\[
|g_n|\le1,
\]
\[
\begin{aligned}
|((f-\varphi)*g_n)(x)|
&\le
\int_{\mathbb R^d}
|f(x-y)-\varphi(x-y)|\,|g_n(y)|\,dy\\
&\le
\int_{\mathbb R^d}
|f(x-y)-\varphi(x-y)|\,dy\\
&=
\|f-\varphi\|_1.
\end{aligned}
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
\sup_{x\in\mathbb R^d}
|((f-\varphi)*g_n)(x)|
<
\frac{\varepsilon}{3}}
\]
for every \(n\).


::: pf-proof

Combine steps <1>1--<1>2.

:::

:::

::: pf-step

Fix \(x\in\mathbb R^d\). Then
\[
\varphi(x-y)g_n(y)\to0
\]
for almost every \(y\).


::: pf-proof

By hypothesis,
\[
g_n(y)\to0
\]
for almost every \(y\), while \(\varphi(x-y)\) is fixed.

:::

:::

::: pf-step

The integrands satisfy
\[
\boxed{
|\varphi(x-y)g_n(y)|
\le
|\varphi(x-y)|}.
\]


::: pf-proof

Use \(|g_n(y)|\le1\).

:::

:::

::: pf-step

The dominating function
\[
y\mapsto|\varphi(x-y)|
\]
is integrable.


::: pf-proof

Translation preserves the \(L^1\)-norm:
\[
\int |\varphi(x-y)|\,dy
=
\|\varphi\|_1<\infty.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
(\varphi*g_n)(x)\to0}
\]
for every fixed \(x\in\mathbb R^d\).


::: pf-proof

Apply the dominated convergence theorem using steps <1>4--<1>6.

:::

:::

::: pf-step

For \(x,x'\in\mathbb R^d\),
\[
\begin{aligned}
|(\varphi*g_n)(x)-(\varphi*g_n)(x')|
\le
\int
|\varphi(x-y)-\varphi(x'-y)|\,dy.
\end{aligned}
\]


::: pf-proof

Subtract the two convolution integrals and use
\[
|g_n(y)|\le1.
\]

:::

:::

::: pf-step

The right-hand side is
\[
\boxed{
\|\tau_x\varphi-\tau_{x'}\varphi\|_{L^1}},
\]
where
\[
(\tau_x\varphi)(y)=\varphi(x-y).
\]


::: pf-proof

This is exactly the definition of the displayed \(L^1\)-norm.

:::

:::

::: pf-step

As \(x'\to x\),
\[
\boxed{
\|\tau_x\varphi-\tau_{x'}\varphi\|_{L^1}\to0}.
\]


::: pf-proof

Translations are continuous in \(L^1\). Since \(\varphi\in C_c\), this can also be seen directly from uniform continuity of \(\varphi\) and the finite measure of a common compact support neighborhood.

:::

:::

::: pf-step

Thus the family
\[
\{\varphi*g_n:n\ge1\}
\]
is equicontinuous on \(\mathbb R^d\), with a modulus independent of \(n\).


::: pf-proof

Steps <1>8--<1>10 give a bound on the increment depending only on \(x-x'\), not on \(n\).

:::

:::

::: pf-step

By equicontinuity, choose \(\delta>0\) such that
\[
|x-x'|<\delta
\]
implies
\[
\boxed{
|(\varphi*g_n)(x)-(\varphi*g_n)(x')|
<
\frac{\varepsilon}{3}}
\]
for every \(n\).


::: pf-proof

Apply step <1>11 with tolerance \(\varepsilon/3\).

:::

:::

::: pf-step

Since \(K\) is compact, choose points
\[
x_1,\dots,x_m\in K
\]
such that
\[
K\subseteq
\bigcup_{j=1}^{m}B(x_j,\delta).
\]


::: pf-proof

The family of \(\delta\)-balls centered at points of \(K\) is an open cover; compactness gives a finite subcover.

:::

:::

::: pf-step

For each \(j\),
\[
(\varphi*g_n)(x_j)\to0.
\]


::: pf-proof

This is step <1>7.

:::

:::

::: pf-step

Hence there exists \(N\) such that for every \(n\ge N\) and every
\[
1\le j\le m,
\]
\[
\boxed{
|(\varphi*g_n)(x_j)|
<
\frac{\varepsilon}{3}}.
\]


::: pf-proof

There are only finitely many points \(x_j\). Choose \(N\) larger than all individual convergence thresholds.

:::

:::

::: pf-step

Let \(x\in K\) and \(n\ge N\). Choose \(j\) with
\[
|x-x_j|<\delta.
\]
Then
\[
|(\varphi*g_n)(x)|
<
\frac{2\varepsilon}{3}.
\]


::: pf-proof

By the triangle inequality,
\[
\begin{aligned}
|(\varphi*g_n)(x)|
&\le
|(\varphi*g_n)(x)-(\varphi*g_n)(x_j)|
+
|(\varphi*g_n)(x_j)|\\
&<
\frac{\varepsilon}{3}
+
\frac{\varepsilon}{3}
=
\frac{2\varepsilon}{3},
\end{aligned}
\]
using steps <1>12 and <1>15.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\sup_{x\in K}|(\varphi*g_n)(x)|
<
\frac{2\varepsilon}{3}}
\]
for every \(n\ge N\).


::: pf-proof

The bound in step <1>16 holds for every \(x\in K\).

:::

:::

::: pf-step

For \(n\ge N\) and \(x\in K\),
\[
|f*g_n(x)|
\le
|((f-\varphi)*g_n)(x)|
+
|(\varphi*g_n)(x)|.
\]


::: pf-proof

Use
\[
f*g_n
=
(f-\varphi)*g_n+\varphi*g_n.
\]

:::

:::

::: pf-step

Hence, for \(n\ge N\),
\[
\boxed{
\sup_{x\in K}|f*g_n(x)|<\varepsilon}.
\]


::: pf-proof

Use step <1>3 for the first term and step <1>17 for the second:
\[
\frac{\varepsilon}{3}
+
\frac{2\varepsilon}{3}
=
\varepsilon.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
f*g_n\to0
\text{ uniformly on }K}.
\]


::: pf-proof

Step <1>19 is the definition of uniform convergence on the compact set \(K\).

:::

:::

::: pf-step

Since \(K\subset\mathbb R^d\) was arbitrary,
\[
\boxed{
f*g_n\to0
\text{ locally uniformly on }\mathbb R^d}.
\]


::: pf-proof

Local uniform convergence means uniform convergence on every compact subset.

:::

:::

::: pf-qed

Step <1>21 is the required conclusion.

:::

:::
