---
schema: qual/card@1
id: E-SS4.EX-4
kind: problem
title: "The Fourier transform of a reciprocal polynomial via residues"
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
4. Suppose $Q$ is a polynomial of degree $\geq 2$ with distinct roots, none lying on the real axis.
   Calculate

$$
\int_ {- \infty} ^ {\infty} \frac {e ^ {- 2 \pi i x \xi}}{Q (x)} d x, \quad \xi \in \mathbb {R}
$$

in terms of the roots of $Q$ . What happens when several roots coincide?
[Hint: Consider separately the cases $\xi < 0 , \xi = 0$ , and $\xi > 0$ . Use residues.]
:::

::: solution
Let the distinct roots of $Q$ be $\alpha_1,\ldots,\alpha_m$, none real, and set
\[
I(\xi)=\int_{-\infty}^{\infty}\frac{e^{-2\pi i x\xi}}{Q(x)}\,dx.
\]
Because $\deg Q\ge2$, the semicircular arc contribution tends to $0$ in every case below.

If $\xi<0$, close in the upper half-plane, where the exponential decays. The residue theorem gives
\[
I(\xi)=2\pi i\sum_{\Im\alpha_j>0}
\frac{e^{-2\pi i\alpha_j\xi}}{Q'(\alpha_j)}.
\tag{1}
\]
If $\xi>0$, close in the lower half-plane. The contour is clockwise, hence
\[
I(\xi)=-2\pi i\sum_{\Im\alpha_j<0}
\frac{e^{-2\pi i\alpha_j\xi}}{Q'(\alpha_j)}.
\tag{2}
\]
For $\xi=0$ one may close in either half-plane; for example
\[
I(0)=2\pi i\sum_{\Im\alpha_j>0}\frac1{Q'(\alpha_j)}.
\tag{3}
\]

If roots coincide, the same contour argument holds but the poles are of higher order. A root $\alpha$ of multiplicity $r$ contributes its higher-order residue
\[
\operatorname{Res}_{z=\alpha}
\frac{e^{-2\pi i z\xi}}{Q(z)},
\]
which is $e^{-2\pi i\alpha\xi}$ times a polynomial in $\xi$ of degree at most $r-1$. Thus (1)--(2) are replaced by finite sums of terms
\[
P_\alpha(\xi)e^{-2\pi i\alpha\xi},
\qquad \deg P_\alpha<r.
\]
:::
