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
Exhibit a conformal map from $\{z\in\CC\mid\abs{z}<1,\ \Re z>0\}$ onto $\DD=\{z\in\CC\mid\abs{z}<1\}$.
:::

::: {.solution}
Let
$$
H=\{z\in\CC:\abs{z}<1,\ \Re z>0\},
\qquad
Q=\{w:\Re w<0,\ \Im w<0\},
$$
and define
$$
M(z)=\frac{z-i}{z+i},
\qquad
S(w)=w^2,
\qquad
C(\zeta)=\frac{\zeta-i}{\zeta+i}.
$$

::: pf

::: {.pf-step #s1}

$M$ maps $H$ conformally onto the open third quadrant $Q$.

::: pf-proof

The boundary of $H$ consists of the diameter
$$
\{iy:-1<y<1\}
$$
and the right semicircle $\{\abs{z}=1,\ \Re z>0\}$. For $z=iy$ on the
diameter,
$$
M(iy)=\frac{y-1}{y+1}<0,
$$
so this boundary arc maps to the negative real ray.

A Möbius transformation maps generalized circles to generalized circles.
Since the unit circle passes through $i$ and $-i$, and
$$
M(i)=0,\qquad M(-i)=\infty,
$$
its image is a line through $0$. At the point $z=1$ of the right
semicircle,
$$
M(1)=-i,
$$
so the right semicircle maps to the negative imaginary ray. Finally,
$$
M\left(\frac12\right)=-\frac35-\frac45 i,
$$
which lies in $Q$. The Möbius transformation $M$ is a homeomorphism of the
Riemann sphere carrying $\partial H$ onto $\partial Q$, and it carries the
point $\tfrac12\in H$ into $Q$, so it maps $H$ bijectively and
conformally onto $Q$.

:::

:::

::: {.pf-step #s2}

$S$ maps $Q$ conformally onto the upper half-plane.

::: pf-proof

Every $w\in Q$ has a unique argument
$$
\pi<\arg w<\frac{3\pi}{2}.
$$
Thus
$$
2\pi<\arg(w^2)<3\pi,
$$
which modulo $2\pi$ is exactly the range $(0,\pi)$. Hence $w^2$ lies in the
upper half-plane. Conversely, every point of the upper half-plane has
exactly one square root whose argument lies in $(\pi,3\pi/2)$, so $S$ is
bijective from $Q$ onto the upper half-plane. Its derivative $2w$ never
vanishes on $Q$, so it is conformal there.

:::

:::

::: {.pf-step #s3}

$C$ maps the upper half-plane conformally onto $\DD$.

::: pf-proof

For $\Im\zeta>0$,
$$
\abs{\zeta-i}<\abs{\zeta+i},
$$
so $\abs{C(\zeta)}<1$. The inverse Möbius transformation
$$
C^{-1}(u)=i\,\frac{1+u}{1-u}
$$
satisfies
$$
\Im C^{-1}(u)=\frac{1-\abs{u}^2}{\abs{1-u}^2}>0
$$
for $\abs{u}<1$, so $C$ is a bijection from the upper half-plane onto
$\DD$. Möbius transformations are conformal off their pole.

:::

:::

::: {.pf-step #s4}

The map
$$
\boxed{
F(z)=C(S(M(z)))
=\frac{\left(\frac{z-i}{z+i}\right)^2-i}
{\left(\frac{z-i}{z+i}\right)^2+i}}
$$
is a conformal bijection from $H$ onto $\DD$.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} show that $M$, $S$, and $C$ are conformal bijections
$H\to Q$, $Q\to\{\Im\zeta>0\}$, and $\{\Im\zeta>0\}\to\DD$. Their
composite $F$ is therefore a conformal bijection $H\to\DD$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} exhibits the required conformal map.

:::

:::

:::
