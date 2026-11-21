---
schema: qual/card@1
id: P-CAFA17C
kind: problem
title: "Bijective analytic map from a half-disk to the upper half-plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The
      source is a course examination, so there is no retained solution set behind the card and the
      problem statement is the source. Each step re-read and the trigonometry redone: T(iy) =
      (y-1)/(y+1) is real and negative on the diameter, and T(e^{i theta}) = i tan((theta - pi/2)/2)
      is purely imaginary and negative on the semicircle; an interior point decides which side of
      the two rays the image lies on; squaring doubles arguments from (-pi, -pi/2) to (0, pi) and
      is injective there. The remark on the inverse direction was kept when the solution was
      replaced. Not claimed: any statement about maps from the half-disc with other normalisations.
---

::: {.problem}
Find a bijective analytic function $f$ from $\{z : \abs{z} < 1, \operatorname{Re} z > 0\}$ to $\{z : \operatorname{Im} z > 0\}$.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #mobius}
$T(z)=\dfrac{z-i}{z+i}$ is a Möbius transformation, with $T(i)=0$, $T(-i)=\infty$ and $T(\infty)=1$; it is holomorphic and injective on the right half-disc, where $z\ne-i$ because $\operatorname{Re}z>0$.

::: pf-proof
$T$ is a fractional linear map with nonzero determinant $i\cdot1-1\cdot(-i)=2i$, hence a bijection of the Riemann sphere carrying generalized circles to generalized circles and conformal off its pole $-i$, which is not in the closed right half-disc.
:::

:::

::: {.pf-step #diameter}
The diameter segment $\{iy:-1<y<1\}$ maps onto the negative real axis.

::: pf-proof
$T(iy)=\dfrac{iy-i}{iy+i}=\dfrac{y-1}{y+1}$, which is real and negative for $-1<y<1$, and it runs from $-\infty$ (as $y\to-1^{+}$) to $0$ (as $y\to1^{-}$) monotonically.
:::

:::

::: {.pf-step #semicircle}
The right semicircle $\{e^{i\theta}:-\pi/2<\theta<\pi/2\}$ maps onto the negative imaginary axis.

::: pf-proof
$T(e^{i\theta})=\dfrac{e^{i\theta}-i}{e^{i\theta}+i}$. Writing $A=\theta/2$ and $B=\pi/2-\theta/2$, the numerator is $e^{iA}-e^{iB}=2i\sin\frac{A-B}{2}e^{i(A+B)/2}$ and the denominator is $2\cos\frac{A-B}{2}e^{i(A+B)/2}$, so $T=i\tan\frac{\theta-\pi/2}{2}$. As $\theta$ runs over $(-\pi/2,\pi/2)$, $\frac{\theta-\pi/2}{2}$ runs over $(-\pi/2,0)$, where the tangent is negative, so the values are purely imaginary and negative and fill that half-axis.
:::

:::

::: {.pf-step #quadrant}
$T$ maps the right half-disc onto the quadrant $Q=\{w:\operatorname{Re}w<0,\operatorname{Im}w<0\}$.

::: pf-proof
The boundary of the half-disc is the union of the two arcs of steps [](#diameter){.pf-ref} and [](#semicircle){.pf-ref}, which map onto the two boundary rays of $Q$ meeting at $0=T(i)$; $T$ is injective, so it maps the half-disc onto one of the two components of the complement of those rays. The interior point $z=1/2$ has $T(1/2)=\frac{1/2-i}{1/2+i}=\frac{-3-4i}{5}$, which lies in $Q$, so the image is $Q$.
:::

:::

::: {.pf-step #square}
$w\mapsto w^{2}$ is a bijection $Q\to\halfplane$.

::: pf-proof
On $Q$ the argument lies in $(-\pi,-\pi/2)$, an interval of length $\pi/2<\pi$ on which $w\mapsto w^{2}$ is injective; squaring doubles arguments, so the image arguments fill $(-2\pi,-\pi)$, which modulo $2\pi$ is $(0,\pi)$, the upper half-plane, and every point of the upper half-plane has exactly one preimage square root in $Q$.
:::

:::

::: {.pf-step}
$f(z)=\left(\dfrac{z-i}{z+i}\right)^{2}$ is a bijective analytic map from the right half-disc onto the upper half-plane.

::: pf-proof
$f=T^{2}$ is analytic on the half-disc by step [](#mobius){.pf-ref} and maps it bijectively onto $\halfplane$ by steps [](#quadrant){.pf-ref} and [](#square){.pf-ref}:
$$
\boxed{f(z)=\left(\frac{z-i}{z+i}\right)^{2},\qquad \{\abs{z}<1,\ \operatorname{Re}z>0\}\longrightarrow\halfplane\text{ bijectively}.}
$$
:::

:::

:::
:::

::: {.remark title="Inverse direction"}
A conformal map is a holomorphic map with nonzero
derivative; a conformal equivalence is such a map
with a holomorphic inverse. Let $\sqrt z$ be the
branch with argument in $(0,\pi/2)$ for
$\operatorname{Im}z>0$. The inverse of the
displayed map, from the upper half-plane
to the right half of the unit disk, is
$$
F(z)=i\,\frac{1-\sqrt z}{1+\sqrt z}.
$$
Indeed $-\sqrt z$ lies in the third quadrant,
where it is the inverse branch of squaring
used above, and
$F=T^{-1}(-\sqrt z)$. Both factors have
nonzero derivative on their domains, so
$F$ is conformal.
:::
