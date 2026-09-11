---
schema: qual/card@1
id: P-BKF82-7
kind: problem
title: Evaluate $\int_{-\infty}^{\infty}\cos(\pi x)/(4x^2-1)\,dx$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Evaluated the integral by an upper-half-plane contour for e^{iπz}/(4z²-1), with small upper indentations at the two real poles."
---

::: problem
Evaluate
\[
\int_{-\infty}^{\infty}\frac{\cos(\pi x)}{4x^2-1}\,dx.
\]
:::

::: solution
Consider
$$
F(z)=\frac{e^{i\pi z}}{4z^2-1}.
$$
The poles $z=\pm\frac12$ lie on the real axis, so use a large upper
semicircle and indent the real axis by small upper semicircles around those
two poles.

<1>1. The contribution from the large semicircle tends to zero.
::: proof
On the upper half-plane,
$$
|e^{i\pi z}|=e^{-\pi\operatorname{Im}z}\le1.
$$
On $|z|=R$ with $R$ large,
$$
|4z^2-1|\ge4R^2-1,
$$
so the large-arc integral has absolute value at most
$$
\frac{\pi R}{4R^2-1}\longrightarrow0.
$$
:::

<1>2. Compute the residues at the two real poles.
::: proof
Since $(4z^2-1)'=8z$,
$$
\operatorname{Res}_{z=1/2}F
=\frac{e^{i\pi/2}}{4}
=\frac{i}{4},
$$
and
$$
\operatorname{Res}_{z=-1/2}F
=\frac{e^{-i\pi/2}}{-4}
=\frac{i}{4}.
$$
Thus the sum of the two residues is $i/2$.
:::

<1>3. Evaluate the principal-value integral of $F$.
::: proof
The small upper indentation around a simple real pole is traversed clockwise,
so its limiting contribution is $-i\pi$ times the residue. There are no
poles strictly inside the indented contour. Hence, after letting the large
radius tend to infinity and the indentation radii tend to zero,
$$
\operatorname{PV}\int_{-\infty}^{\infty}F(x)\,dx
=i\pi\left(\frac{i}{4}+\frac{i}{4}\right)
=-\frac\pi2.
$$
:::

<1>4. Take real parts.
::: proof
For real $x$,
$$
\operatorname{Re}F(x)
=\frac{\cos(\pi x)}{4x^2-1}.
$$
Although $F$ itself has poles at $\pm\frac12$, the real part has removable
singularities there because $\cos(\pi x)$ vanishes at both points. It is also
$O(x^{-2})$ at infinity, so its ordinary improper integral converges and equals
the real part of the principal value computed in step <1>3. Therefore
$$
\boxed{
\int_{-\infty}^{\infty}\frac{\cos(\pi x)}{4x^2-1}\,dx
=-\frac\pi2.}
$$
:::
:::
