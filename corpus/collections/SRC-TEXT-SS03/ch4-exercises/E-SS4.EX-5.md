---
schema: qual/card@1
id: E-SS4.EX-5
kind: problem
title: "SS 4.5: Fourier transforms of rational functions by partial fractions"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 4 notation and exercise statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
5. More generally, let $R ( x ) = P ( x ) / Q ( x )$ be a rational function with (degree $Q ) \geq$ (degreeP )+2 and $Q ( x ) \neq 0$ on the real axis.

(a) Prove that if $\alpha _ { 1 } , \ldots , \alpha _ { k }$ are the roots of R in the upper half-plane, then there exists polynomials $P _ { j } ( \boldsymbol { \xi } )$ of degree less than the multiplicity of $\alpha _ { j }$ so that

$$
\int_ {- \infty} ^ {\infty} R (x) e ^ {- 2 \pi i x \xi} d x = \sum_ {j = 1} ^ {k} P _ {j} (\xi) e ^ {- 2 \pi i \alpha_ {j} \xi}, \quad \text {when} \xi <   0.
$$

(b) In particular, if $Q ( z )$ has no zeros in the upper half-plane, then $\begin{array} { r } { \int _ { - \infty } ^ { \infty } R ( x ) e ^ { - 2 \pi i x \xi } \dot { d x } = 0 } \end{array}$ for $\xi < 0 .$

(c) Show that similar results hold in the case $\xi > 0$

(d) Show that

$$
\int_ {- \infty} ^ {\infty} R (x) e ^ {- 2 \pi i x \xi} d x = O (e ^ {- a | \xi |}), \quad \xi \in \mathbb {R}
$$

as $| \xi | \to \infty$ for some $a > 0$ . Determine the best possible $a \mathrm { { s } }$ in terms of the roots of R.

[Hint: For part $\mathrm { ( a ) }$ , use residues. The powers of $\xi$ appear when one diferentiates the function $f ( z ) = R ( z ) e ^ { - 2 \pi i z \xi }$ (as in the formula of Theorem 1.4 in the previous chapter). For part (c) argue in the lower half-plane.]
:::

::: solution
Write the poles of $R=P/Q$ in the upper half-plane as $\alpha_j$, with multiplicities $m_j$. For $\xi<0$, close the contour in the upper half-plane. The assumption
\[
\deg Q\ge \deg P+2
\]
ensures that the large semicircle contributes $0$. Hence
\[
\int_{\mathbb R}R(x)e^{-2\pi i x\xi}\,dx
=2\pi i\sum_j\operatorname{Res}_{z=\alpha_j}
\left(R(z)e^{-2\pi i z\xi}\right).
\tag{1}
\]
At a pole $\alpha_j$ of order $m_j$, the higher-order residue formula differentiates at most $m_j-1$ times. Differentiating the exponential produces powers of $\xi$, so the corresponding residue has the form
\[
P_j(\xi)e^{-2\pi i\alpha_j\xi},
\qquad \deg P_j<m_j.
\]
This proves (a). If there are no poles in the upper half-plane, the sum in (1) is empty, proving (b).

For $\xi>0$, close instead in the lower half-plane. Since the contour is clockwise,
\[
\int_{\mathbb R}R(x)e^{-2\pi i x\xi}\,dx
=-2\pi i\sum_{\Im\beta_j<0}
Q_j(\xi)e^{-2\pi i\beta_j\xi},
\tag{2}
\]
where $\deg Q_j$ is less than the multiplicity of the pole $\beta_j$. This proves (c).

For (d), let
\[
\delta_+=\min_{\Im\alpha_j>0}\Im\alpha_j,
\qquad
\delta_- =\min_{\Im\beta_j<0}|\Im\beta_j|,
\]
omitting a quantity when the corresponding half-plane contains no pole. From (1), as $\xi\to-\infty$, each term has magnitude bounded by a polynomial times
\[
e^{-2\pi(\Im\alpha_j)|\xi|},
\]
so for every $a<2\pi\delta_+$ the transform is $O(e^{-a|\xi|})$ on that side. Similarly, for every $a<2\pi\delta_-$ it is $O(e^{-a|\xi|})$ as $\xi\to+\infty$. If one half-plane contains no poles, the transform is identically zero on the corresponding side.

Consequently a two-sided estimate
\[
\int_{\mathbb R}R(x)e^{-2\pi i x\xi}\,dx=O(e^{-a|\xi|})
\]
holds for every
\[
a<2\pi\,\operatorname{dist}(\{\text{poles of }R\},\mathbb R).
\]
The supremal possible exponential rate is therefore
\[
2\pi\,\operatorname{dist}(\{\text{poles of }R\},\mathbb R).
\]
At the endpoint itself the estimate holds when every pole at minimal distance is simple; higher multiplicity may introduce a nonconstant polynomial factor, so in general the endpoint rate is only a supremum.
:::
