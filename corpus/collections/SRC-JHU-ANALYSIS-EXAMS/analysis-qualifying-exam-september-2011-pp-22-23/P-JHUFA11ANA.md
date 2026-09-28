---
schema: qual/card@1
id: P-JHUFA11ANA
kind: problem
title: '$\int_\gamma \frac{dz}{z^3\cos z}$ for $|z-1|=2$'
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked September 2011 problem 1 on PDF page 22. The printed inequality describes a disk despite calling it a counterclockwise circle; restored the boundary equation with the stated center and radius."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Located all possible poles relative to the off-center circle, excluded boundary poles, and checked the third-order and simple-pole residues and orientation sign."
---

::: {.problem}
Determine $\int_\gamma \frac{dz}{z^3\cos z}$, where
$\gamma$ is the circle $\abs{z-1}=2$ traversed counterclockwise.
:::

::: {.remark}
The contour is the boundary circle $\abs{z-1}=2$; the strict
inequality $\abs{z-1}<2$ describes its interior, not the contour.
:::

::: {.solution}
<1>1. The only enclosed poles are $0$ and $\pi/2$, with no pole on the contour.

::: {.proof}
Put $F(z)=1/(z^3\cos z)$. Besides zero, its possible
poles are the zeros of cosine. The equation $\cos z=0$
is equivalent to $e^{2iz}=-1$, hence to
$z=\pi/2+k\pi$ for $k\in\ZZ$: taking moduli
first forces $\operatorname{Im}z=0$, and the real
solutions are the indicated odd multiples of $\pi/2$.

A real point is inside the contour exactly when it
belongs to $(-1,3)$. The bounds $2<\pi<4$ follow from
$\pi=4\int_0^1(1+t^2)^{-1}\,dt$ and
$1/2<(1+t^2)^{-1}<1$ for $0<t<1$.
Thus $\pi/2\in(1,2)$ lies inside, while $-\pi/2<-1$
and $3\pi/2>3$; all other cosine zeros are farther away.
Also $\abs{0-1}=1<2$. These strict inequalities exclude
boundary poles and identify every enclosed pole.
:::

<1>2. The integral is
$$
\boxed{\int_\gamma \frac{dz}{z^3\cos z}=i\pi-\frac{16i}{\pi^2}}.
$$

::: {.proof}
At zero the Taylor expansion gives
$$
\cos z=1-\frac{z^2}{2}+O(z^4),\qquad
F(z)=\frac1{z^3}+\frac1{2z}+O(z).
$$
Therefore $\operatorname{Res}_0F=1/2$.
At $a=\pi/2$, cosine has a simple zero with derivative
$-\sin a=-1$, so
$$
\operatorname{Res}_{a}F
=\frac1{a^3(-\sin a)}=-\frac8{\pi^3}.
$$
The [[T-HRPNO|residue theorem]] applies to the meromorphic function
$F$ on the disk and its counterclockwise boundary.
Using step <1>1, it gives
$$
\int_\gamma F(z)\,dz
=2\pi i\left(\frac12-\frac8{\pi^3}\right)
=i\pi-\frac{16i}{\pi^2}.
$$
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 gives the requested integral.
:::
:::
