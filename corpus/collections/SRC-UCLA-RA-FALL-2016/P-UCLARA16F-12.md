---
schema: qual/card@1
id: P-UCLARA16F-12
kind: problem
title: Runge approximation by rational functions
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
Let $U\subset\mathbb C$ be open and $K\subset U$ compact.

(a) Prove that there exists a bounded open set $V$ with
\[
K\subset V\subset\overline V\subset U
\]
such that $\partial V$ consists of finitely many closed line segments.
Hint: consider a fine square grid.

(b) Let $f$ be holomorphic on $U$.
Show that there exists a sequence $\{R_n\}$ of rational functions such that (i) $R_n\to f$ uniformly on $K$ and (ii) none of the functions $R_n$ has a pole in $K$.
Hint: first represent $f(z)$ for $z\in K$ as a suitable integral over $\partial V$ and then notice that the integrand is equicontinuous in $z$.
:::

## Part (a)

Since \(K\subset U\), with \(K\) compact and \(U\) open, define
\[
\delta
=
\operatorname{dist}
\bigl(
K,\mathbb C\setminus U
\bigr).
\]

::: pf

::: pf-step

One has
\[
\boxed{\delta>0}.
\]


::: pf-proof

The sets \(K\) and \(\mathbb C\setminus U\) are disjoint, \(K\) is compact, and \(\mathbb C\setminus U\) is closed. The distance from a compact set to a disjoint closed set is positive.

:::

:::

::: pf-step

The collection \(\mathcal Q\) is finite.


::: pf-proof

The compact set \(K\) is bounded. Only finitely many squares of a fixed square grid can meet a bounded set.

:::

:::

::: pf-step

The set \(V\) is open and bounded.


::: pf-proof

It is open by definition. The set \(W\) is a finite union of bounded squares, hence bounded, and \(V\subseteq W\).

:::

:::

::: pf-step

One has
\[
\boxed{K\subset V}.
\]


::: pf-proof

Fix \(x\in K\).

If \(x\) lies in the interior of one grid square, that square belongs to \(\mathcal Q\), so a neighborhood of \(x\) lies in \(W\).

If \(x\) lies on a grid edge, both adjacent closed squares meet \(K\), hence both lie in \(\mathcal Q\); their union contains a neighborhood of \(x\).

If \(x\) lies at a grid vertex, all four adjacent closed squares meet \(K\), hence all four lie in \(\mathcal Q\); their union contains a neighborhood of \(x\).

Thus every point of \(K\) is an interior point of \(W\), so \(K\subset V\).

:::

:::

::: pf-step

Every point of \(W\) has distance \(<\delta\) from \(K\).


::: pf-proof

Let \(z\in W\). Then \(z\in Q\) for some selected square \(Q\in\mathcal Q\). By definition of \(\mathcal Q\), choose
\[
x\in Q\cap K.
\]
The diameter of \(Q\) is
\[
\sqrt2\,h<\delta.
\]
Hence
\[
|z-x|<\delta.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{W\subset U}.
\]


::: pf-proof

If some \(z\in W\) lay in \(\mathbb C\setminus U\), then by definition of \(\delta\),
\[
\operatorname{dist}(z,K)\ge\delta,
\]
contradicting step <1>5.

:::

:::

::: pf-step

Since \(W\) is closed,
\[
\boxed{
\overline V\subseteq W\subset U}.
\]


::: pf-proof

The set \(W\) is a finite union of closed squares, hence closed. Since
\[
V=\operatorname{int}W\subseteq W,
\]
its closure is contained in \(W\).

:::

:::

::: pf-step

The boundary \(\partial V\) consists of finitely many closed line segments.


::: pf-proof

The set \(W\) is a finite union of grid squares. Every boundary point of \(V\) lies on an edge of one of these squares. Internal edges cancel from the boundary, leaving only finitely many subsegments of grid edges. After merging collinear adjacent pieces, \(\partial V\) is a finite union of closed line segments.

:::

:::

::: pf-step

Thus
\[
\boxed{
K\subset V\subset\overline V\subset U}
\]
with \(V\) bounded and \(\partial V\) polygonal.


::: pf-proof

Combine steps <1>3--<1>8.

:::

:::

::: pf-step

For every \(z\in K\),
\[
\boxed{
f(z)
=
\frac1{2\pi i}
\int_{\partial V}
\frac{f(\zeta)}{\zeta-z}\,d\zeta}.
\]


::: pf-proof

The compact set \(K\) lies in \(V\), and
\[
\overline V\subset U.
\]
Thus \(f\) is holomorphic on a neighborhood of \(\overline V\). The Cauchy integral formula for a bounded polygonal domain, with all boundary components given their induced orientations, yields the formula on each component of \(V\) containing \(z\). Equivalently, the full oriented boundary chain has winding number \(1\) about points of \(V\) and \(0\) about points outside.

:::

:::

::: pf-step

The compact sets \(K\) and \(\partial V\) are disjoint.


::: pf-proof

By step <1>4,
\[
K\subset V,
\]
while
\[
\partial V\cap V=\varnothing.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
d
=
\operatorname{dist}(K,\partial V)
>
0}.
\]


::: pf-proof

Both sets are compact and disjoint.

:::

:::

::: pf-step

The function
\[
G(z,\zeta)
=
\frac{f(\zeta)}{\zeta-z}
\]
is continuous on
\[
K\times\partial V.
\]


::: pf-proof

The numerator is continuous because \(f\) is holomorphic on a neighborhood of \(\overline V\). By step <1>12,
\[
|\zeta-z|\ge d>0
\]
on the product, so the denominator never vanishes.

:::

:::

::: pf-step

Therefore \(G\) is uniformly continuous on
\[
K\times\partial V.
\]


::: pf-proof

The product \(K\times\partial V\) is compact, and every continuous function on a compact metric space is uniformly continuous.

:::

:::

::: pf-step

For each \(\ell\), the family of functions
\[
t\longmapsto
\frac{
f(\gamma_\ell(t))
}{
\gamma_\ell(t)-z
}
\gamma_\ell'(t),
\qquad z\in K,
\]
is uniformly equicontinuous in \(t\).


::: pf-proof

This follows from uniform continuity of \(G\) on \(K\times\partial V\) from step <1>14. The derivative \(\gamma_\ell'\) is constant on each segment.

:::

:::

::: pf-step

Each \(R_N\) is a rational function of \(z\).


::: pf-proof

It is a finite sum of terms of the form
\[
\frac{c}{a-z},
\]
with constants \(a,c\in\mathbb C\).

:::

:::

::: pf-step

Every pole of \(R_N\) lies on \(\partial V\).


::: pf-proof

The only possible poles occur at the sample points
\[
a=\gamma_\ell(t_{\ell,j}^{(N)})\in\partial V.
\]

:::

:::

::: pf-step

Hence no \(R_N\) has a pole in \(K\).


::: pf-proof

By step <1>11,
\[
K\cap\partial V=\varnothing.
\]
Combine with step <1>17.

:::

:::

::: pf-step

The Riemann sums defining \(R_N(z)\) converge uniformly in \(z\in K\) to the boundary integrals.


::: pf-proof

Fix \(\varepsilon>0\). By uniform equicontinuity from step <1>15, choose \(N\) so large that on each subinterval the oscillation of every integrand, uniformly over \(z\in K\), is less than
\[
\frac{2\pi\varepsilon}{\sum_{\ell=1}^{L}|\gamma_\ell'|+1}.
\]
The standard Riemann-sum estimate on each segment then bounds the difference between its integral and its Riemann sum uniformly in \(z\). Summing over the finitely many segments gives a total error \(<\varepsilon\).

:::

:::

::: pf-step

Therefore
\[
\boxed{
R_N\to f
\quad\text{uniformly on }K}.
\]


::: pf-proof

Use the Cauchy representation in step <1>10 and the uniform Riemann-sum convergence in step <1>19.

:::

:::

::: pf-step

Thus there exists a sequence of rational functions \((R_N)\) such that
\[
\boxed{
R_N\to f\text{ uniformly on }K}
\]
and
\[
\boxed{
R_N\text{ has no pole in }K}.
\]


::: pf-proof

Uniform approximation is step <1>20, and the pole statement is step <1>18.

:::

:::

::: pf-qed

Step <1>9 proves part (a), and step <1>21 proves part (b).

:::

:::
