---
schema: qual/card@1
id: P-UCLARA15F-03
kind: problem
title: Locally integrable functions bounded by the $L^p$ quasinorm with $0<p<1$ vanish
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
  note: Retranscribed the font-garbled statement in LaTeX from Problem 3 on page 1 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $f \in L^1_{\mathrm{loc}}(\mathbb{R}^d)$ be such that for some $0 < p < 1$, we have
\[
\left| \int f(x) g(x)\,dx \right| \leq \left( \int |g(x)|^p\,dx \right)^{\frac{1}{p}},
\]
for all $g \in C_0(\mathbb{R}^d)$. Show that $f(x) = 0$ a.e. Here $C_0(\mathbb{R}^d)$ is the space of continuous functions with compact support on $\mathbb{R}^d$.
:::

Fix
\[
0<p<1.
\]

## A compact-set estimate

Let
\[
K\subset\mathbb R^d
\]
be compact.

::: pf

::: pf-step

Choose a bounded open set \(U\) with
\[
K\subset U
\]
such that both
\[
\boxed{
\int_{U\setminus K}|f(x)|\,dx<\varepsilon}
\]
and
\[
\boxed{
|U\setminus K|<\varepsilon}.
\]


::: pf-proof

Since \(f\in L^1_{\mathrm{loc}}\), it is integrable on some bounded neighborhood of \(K\), and its integral is absolutely continuous with respect to Lebesgue measure there. By outer regularity of Lebesgue measure, choose bounded open \(U\supset K\) with \(|U\setminus K|\) as small as desired; then absolute continuity of the integral makes \(\int_{U\setminus K}|f|\) small as well.

:::

:::

::: pf-step

By Urysohn's lemma on \(\mathbb R^d\), choose
\[
g\in C_c(\mathbb R^d)
\]
such that
\[
0\le g\le1,
\qquad
g=1\text{ on }K,
\qquad
\operatorname{supp}g\subset U.
\]


::: pf-proof

Euclidean space is normal, and \(K\) is closed while \(U\) is open with \(K\subset U\).

:::

:::

::: pf-step

One has
\[
\left|
\int_{\mathbb R^d}f(x)g(x)\,dx
-
\int_K f(x)\,dx
\right|
<
\varepsilon.
\]


::: pf-proof

Since \(g=1\) on \(K\) and \(g=0\) outside \(U\),
\[
\begin{aligned}
\left|
\int fg-\int_K f
\right|
&=
\left|
\int_{U\setminus K}
f(x)g(x)\,dx
\right|\\
&\le
\int_{U\setminus K}|f(x)|\,dx
<
\varepsilon
\end{aligned}
\]
by step <1>1.

:::

:::

::: pf-step

By the hypothesis,
\[
\left|
\int fg
\right|
\le
\left(
\int |g|^p
\right)^{1/p}.
\]


::: pf-proof

This is the assumed inequality applied to the test function \(g\in C_c(\mathbb R^d)\).

:::

:::

::: pf-step

Since
\[
0\le g\le1
\]
and
\[
\operatorname{supp}g\subset U,
\]
\[
\boxed{
\int |g|^p\le |U|}.
\]


::: pf-proof

On \(U\),
\[
|g|^p\le1,
\]
and outside \(U\), \(g=0\).

:::

:::

::: pf-step

Therefore
\[
\left|
\int_K f
\right|
\le
\varepsilon+|U|^{1/p}.
\]


::: pf-proof

Use the triangle inequality with steps <1>3--<1>5.

:::

:::

::: pf-step

Since
\[
|U|
\le
|K|+\varepsilon,
\]
\[
\left|
\int_K f
\right|
\le
\varepsilon+(|K|+\varepsilon)^{1/p}.
\]


::: pf-proof

By step <1>1,
\[
|U|=|K|+|U\setminus K|
<
|K|+\varepsilon.
\]

:::

:::

::: pf-step

Letting \(\varepsilon\downarrow0\),
\[
\boxed{
\left|
\int_K f(x)\,dx
\right|
\le
|K|^{1/p}}.
\]


::: pf-proof

The bound in step <1>7 holds for every positive \(\varepsilon\), and the right-hand side converges to \(|K|^{1/p}\).

:::

:::

::: pf-step

Partition \(Q\) into
\[
N^d
\]
closed subcubes
\[
Q_1,\dots,Q_{N^d}
\]
of side length
\[
s/N.
\]


::: pf-proof

Divide each coordinate interval into \(N\) equal pieces and take Cartesian products.

:::

:::

::: pf-step

Since the overlaps of distinct subcubes lie in boundaries of measure zero,
\[
\int_Q f
=
\sum_{j=1}^{N^d}
\int_{Q_j}f.
\]


::: pf-proof

The interiors are disjoint and cover \(Q\) up to the union of finitely many lower-dimensional faces, which has Lebesgue measure zero.

:::

:::

::: pf-step

Hence
\[
\left|
\int_Q f
\right|
\le
\sum_{j=1}^{N^d}
\left|
\int_{Q_j}f
\right|.
\]


::: pf-proof

Apply the triangle inequality to step <1>10.

:::

:::

::: pf-step

By step <1>8,
\[
\left|
\int_{Q_j}f
\right|
\le
|Q_j|^{1/p}
=
\left(
\frac{s^d}{N^d}
\right)^{1/p}.
\]


::: pf-proof

Each \(Q_j\) is compact, and its volume is
\[
(s/N)^d.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\left|
\int_Q f
\right|
\le
s^{d/p}
N^{d-d/p}}.
\]


::: pf-proof

There are \(N^d\) subcubes, so
\[
N^d
\left(
\frac{s^d}{N^d}
\right)^{1/p}
=
s^{d/p}
N^{d(1-1/p)}.
\]

:::

:::

::: pf-step

Since \(0<p<1\),
\[
\boxed{
d-d/p<0}.
\]


::: pf-proof

Because
\[
1/p>1,
\]
one has
\[
1-1/p<0.
\]
Multiply by \(d>0\).

:::

:::

::: pf-step

Letting \(N\to\infty\) in step <1>13 gives
\[
\boxed{
\int_Q f(x)\,dx=0}
\]
for every closed cube \(Q\).


::: pf-proof

By step <1>14,
\[
N^{d-d/p}\to0.
\]
The left-hand side is independent of \(N\), so its absolute value is bounded by quantities tending to zero.

:::

:::

::: pf-step

Since
\[
f\in L^1_{\mathrm{loc}}(\mathbb R^d),
\]
the Lebesgue differentiation theorem gives, for almost every \(x\),
\[
\boxed{
f(x)
=
\lim_{r\downarrow0}
\frac1{|Q_r(x)|}
\int_{Q_r(x)}f(y)\,dy},
\]
where \(Q_r(x)\) is any family of cubes centered at \(x\) with side length tending to zero.


::: pf-proof

This is the Lebesgue differentiation theorem for locally integrable functions, with cubes as the differentiation basis.

:::

:::

::: pf-step

Every integral in step <1>16 is zero.


::: pf-proof

Each \(Q_r(x)\) is a closed cube, so step <1>15 applies.

:::

:::

::: pf-step

Therefore
\[
\boxed{
f(x)=0}
\]
for almost every \(x\in\mathbb R^d\).


::: pf-proof

At every Lebesgue differentiation point of \(f\), steps <1>16--<1>17 give
\[
f(x)=\lim_{r\downarrow0}0=0.
\]
Such points form a full-measure set.

:::

:::

::: pf-qed

Step <1>18 is the required conclusion.

:::

:::
