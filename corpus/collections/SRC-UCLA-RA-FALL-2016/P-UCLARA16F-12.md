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

::: {.solution}
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

<1>1. One has
\[
\boxed{\delta>0}.
\]

::: {.proof}
The sets \(K\) and \(\mathbb C\setminus U\) are disjoint, \(K\) is compact, and \(\mathbb C\setminus U\) is closed. The distance from a compact set to a disjoint closed set is positive.
:::

Choose a square grid in \(\mathbb C\cong\mathbb R^2\) with side length \(h>0\) so small that
\[
\boxed{\sqrt2\,h<\delta}.
\]

Let \(\mathcal Q\) be the collection of all closed grid squares that meet \(K\).

<1>2. The collection \(\mathcal Q\) is finite.

::: {.proof}
The compact set \(K\) is bounded. Only finitely many squares of a fixed square grid can meet a bounded set.
:::

Let
\[
W
=
\bigcup_{Q\in\mathcal Q}Q
\]
and define
\[
\boxed{V=\operatorname{int}W}.
\]

<1>3. The set \(V\) is open and bounded.

::: {.proof}
It is open by definition. The set \(W\) is a finite union of bounded squares, hence bounded, and \(V\subseteq W\).
:::

<1>4. One has
\[
\boxed{K\subset V}.
\]

::: {.proof}
Fix \(x\in K\).

If \(x\) lies in the interior of one grid square, that square belongs to \(\mathcal Q\), so a neighborhood of \(x\) lies in \(W\).

If \(x\) lies on a grid edge, both adjacent closed squares meet \(K\), hence both lie in \(\mathcal Q\); their union contains a neighborhood of \(x\).

If \(x\) lies at a grid vertex, all four adjacent closed squares meet \(K\), hence all four lie in \(\mathcal Q\); their union contains a neighborhood of \(x\).

Thus every point of \(K\) is an interior point of \(W\), so \(K\subset V\).
:::

<1>5. Every point of \(W\) has distance \(<\delta\) from \(K\).

::: {.proof}
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

<1>6. Therefore
\[
\boxed{W\subset U}.
\]

::: {.proof}
If some \(z\in W\) lay in \(\mathbb C\setminus U\), then by definition of \(\delta\),
\[
\operatorname{dist}(z,K)\ge\delta,
\]
contradicting step <1>5.
:::

<1>7. Since \(W\) is closed,
\[
\boxed{
\overline V\subseteq W\subset U}.
\]

::: {.proof}
The set \(W\) is a finite union of closed squares, hence closed. Since
\[
V=\operatorname{int}W\subseteq W,
\]
its closure is contained in \(W\).
:::

<1>8. The boundary \(\partial V\) consists of finitely many closed line segments.

::: {.proof}
The set \(W\) is a finite union of grid squares. Every boundary point of \(V\) lies on an edge of one of these squares. Internal edges cancel from the boundary, leaving only finitely many subsegments of grid edges. After merging collinear adjacent pieces, \(\partial V\) is a finite union of closed line segments.
:::

<1>9. Thus
\[
\boxed{
K\subset V\subset\overline V\subset U}
\]
with \(V\) bounded and \(\partial V\) polygonal.

::: {.proof}
Combine steps <1>3--<1>8.
:::

## Part (b)

Let
\[
f\in\mathcal O(U).
\]

Orient each polygonal boundary component of \(V\) positively with respect to \(V\).

<1>10. For every \(z\in K\),
\[
\boxed{
f(z)
=
\frac1{2\pi i}
\int_{\partial V}
\frac{f(\zeta)}{\zeta-z}\,d\zeta}.
\]

::: {.proof}
The compact set \(K\) lies in \(V\), and
\[
\overline V\subset U.
\]
Thus \(f\) is holomorphic on a neighborhood of \(\overline V\). The Cauchy integral formula for a bounded polygonal domain, with all boundary components given their induced orientations, yields the formula on each component of \(V\) containing \(z\). Equivalently, the full oriented boundary chain has winding number \(1\) about points of \(V\) and \(0\) about points outside.
:::

<1>11. The compact sets \(K\) and \(\partial V\) are disjoint.

::: {.proof}
By step <1>4,
\[
K\subset V,
\]
while
\[
\partial V\cap V=\varnothing.
\]
:::

<1>12. Hence
\[
\boxed{
d
=
\operatorname{dist}(K,\partial V)
>
0}.
\]

::: {.proof}
Both sets are compact and disjoint.
:::

<1>13. The function
\[
G(z,\zeta)
=
\frac{f(\zeta)}{\zeta-z}
\]
is continuous on
\[
K\times\partial V.
\]

::: {.proof}
The numerator is continuous because \(f\) is holomorphic on a neighborhood of \(\overline V\). By step <1>12,
\[
|\zeta-z|\ge d>0
\]
on the product, so the denominator never vanishes.
:::

<1>14. Therefore \(G\) is uniformly continuous on
\[
K\times\partial V.
\]

::: {.proof}
The product \(K\times\partial V\) is compact, and every continuous function on a compact metric space is uniformly continuous.
:::

Write the finitely many oriented line segments making up \(\partial V\) as
\[
\gamma_\ell:[0,1]\to\mathbb C,
\qquad
1\le\ell\le L,
\]
with each \(\gamma_\ell\) affine.

Then
\[
f(z)
=
\frac1{2\pi i}
\sum_{\ell=1}^{L}
\int_0^1
\frac{
f(\gamma_\ell(t))
}{
\gamma_\ell(t)-z
}
\gamma_\ell'(t)\,dt.
\]

<1>15. For each \(\ell\), the family of functions
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

::: {.proof}
This follows from uniform continuity of \(G\) on \(K\times\partial V\) from step <1>14. The derivative \(\gamma_\ell'\) is constant on each segment.
:::

For each integer \(N\ge1\), partition every interval \([0,1]\) into \(N\) equal subintervals, choose sample points
\[
t_{\ell,j}^{(N)}
\]
in those subintervals, and define
\[
\boxed{
R_N(z)
=
\frac1{2\pi i}
\sum_{\ell=1}^{L}
\sum_{j=1}^{N}
\frac{
f(\gamma_\ell(t_{\ell,j}^{(N)}))
}{
\gamma_\ell(t_{\ell,j}^{(N)})-z
}
\gamma_\ell'
\frac1N}.
\]

<1>16. Each \(R_N\) is a rational function of \(z\).

::: {.proof}
It is a finite sum of terms of the form
\[
\frac{c}{a-z},
\]
with constants \(a,c\in\mathbb C\).
:::

<1>17. Every pole of \(R_N\) lies on \(\partial V\).

::: {.proof}
The only possible poles occur at the sample points
\[
a=\gamma_\ell(t_{\ell,j}^{(N)})\in\partial V.
\]
:::

<1>18. Hence no \(R_N\) has a pole in \(K\).

::: {.proof}
By step <1>11,
\[
K\cap\partial V=\varnothing.
\]
Combine with step <1>17.
:::

<1>19. The Riemann sums defining \(R_N(z)\) converge uniformly in \(z\in K\) to the boundary integrals.

::: {.proof}
Fix \(\varepsilon>0\). By uniform equicontinuity from step <1>15, choose \(N\) so large that on each subinterval the oscillation of every integrand, uniformly over \(z\in K\), is less than
\[
\frac{2\pi\varepsilon}{\sum_{\ell=1}^{L}|\gamma_\ell'|+1}.
\]
The standard Riemann-sum estimate on each segment then bounds the difference between its integral and its Riemann sum uniformly in \(z\). Summing over the finitely many segments gives a total error \(<\varepsilon\).
:::

<1>20. Therefore
\[
\boxed{
R_N\to f
\quad\text{uniformly on }K}.
\]

::: {.proof}
Use the Cauchy representation in step <1>10 and the uniform Riemann-sum convergence in step <1>19.
:::

<1>21. Thus there exists a sequence of rational functions \((R_N)\) such that
\[
\boxed{
R_N\to f\text{ uniformly on }K}
\]
and
\[
\boxed{
R_N\text{ has no pole in }K}.
\]

::: {.proof}
Uniform approximation is step <1>20, and the pole statement is step <1>18.
:::

<1>22. Q.E.D.

::: {.proof}
Step <1>9 proves part (a), and step <1>21 proves part (b).
:::
:::
