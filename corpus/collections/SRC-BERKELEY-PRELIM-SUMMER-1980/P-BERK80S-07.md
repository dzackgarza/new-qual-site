---
schema: qual/card@1
id: P-BERK80S-07
kind: problem
title: Conformal map from a half-disk to the disk
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 7 of the vendored Berkeley Preliminary Exam, Summer 1980.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the Möbius image of both boundary arcs, injectivity of squaring on the resulting quadrant, and the final Cayley map.
---

::: {.problem}
Exhibit a conformal map from $\{ z \in \mathbb { C } \mid | z | < 1 , \Re z > 0 \}$ onto $\mathbb { D } = \left\{ z \in \mathbb { C } \ | \ | z | < 1 \right\}$
:::


::: {.solution}
Let
\[
H=\{z\in\mathbb C:|z|<1,\ \Re z>0\}.
\]
Define
\[
M(z)=\frac{z-i}{z+i},
\qquad
S(w)=w^2,
\qquad
C(\zeta)=\frac{\zeta-i}{\zeta+i}.
\]
Then a conformal bijection from $H$ onto $\mathbb D$ is
\[
\boxed{
F(z)=C(S(M(z)))
=\frac{\left(\frac{z-i}{z+i}\right)^2-i}
{\left(\frac{z-i}{z+i}\right)^2+i}.}
\]

<1>1. $M$ maps $H$ conformally onto the open third quadrant.
::: {.proof}
The boundary of $H$ consists of the diameter
\[
\{iy:-1<y<1\}
\]
and the right semicircle $\{|z|=1,\Re z>0\}$.
For $z=iy$ on the diameter,
\[
M(iy)=\frac{y-1}{y+1}<0,
\]
so this boundary arc maps to the negative real ray.

A Möbius transformation maps generalized circles to generalized circles. Since the unit circle passes through $i$ and $-i$, and
\[
M(i)=0,\qquad M(-i)=\infty,
\]
its image is a line through $0$ and $\infty$. At the interior point $z=1$ of the right semicircle,
\[
M(1)=-i,
\]
so the right semicircle maps to the negative imaginary ray.
Finally,
\[
M\left(\frac12\right)=-\frac35-\frac45 i,
\]
which lies between those rays in the third quadrant. Therefore $M$ maps $H$ bijectively and conformally onto
\[
Q=\{w:\Re w<0,\ \Im w<0\}.
\]
:::

<1>2. Squaring maps $Q$ conformally onto the upper half-plane.
::: {.proof}
Every $w\in Q$ has a unique argument
\[
\pi<\arg w<\frac{3\pi}{2}.
\]
Thus
\[
2\pi<\arg(w^2)<3\pi,
\]
which modulo $2\pi$ is exactly the range $(0,\pi)$. Hence $w^2$ lies in the upper half-plane.
Conversely, every nonzero point of the upper half-plane has exactly one square root whose argument lies in $(\pi,3\pi/2)$, so $S$ is bijective from $Q$ onto the upper half-plane. Its derivative $2w$ never vanishes on $Q$, hence it is conformal there.
:::

<1>3. $C$ maps the upper half-plane conformally onto $\mathbb D$.
::: {.proof}
For $\Im\zeta>0$,
\[
|\zeta-i|<|\zeta+i|,
\]
so
\[
\left|\frac{\zeta-i}{\zeta+i}\right|<1.
\]
The standard inverse Möbius transformation shows that $C$ is a bijection from the upper half-plane onto $\mathbb D$.
Therefore the composite $F=C\circ S\circ M$ is the required conformal bijection.
:::
:::
