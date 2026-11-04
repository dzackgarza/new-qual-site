---
schema: qual/card@1
id: P-UCI13H3-4
kind: problem
title: Conformal map of a disk cut by a horizontal chord onto the disk
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-UCI-MATH220C-2013-HW3`; no correction is
    claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Explicit map given: with $w=(z-P)/(z-Q)$ for the two corners $P,Q$, setting
    $u=e^{-i\pi/4}w$ and $\varphi=(u^{4/3}-i)/(u^{4/3}+i)$, where the power is the principal branch
    on the sector $0<\arg u<3\pi/4$. The Möbius step carries the two boundary arcs through $P,Q$ to
    the two rays $\arg w=\pi/4$ and $\arg w=\pi$, so $w(G)$ is a sector of angle $3\pi/4$ (not
    $\pi/4$: the interior angle of $G$ at a corner is $3\pi/4$, spanned by the tangent to the circle
    and the chord), and the remaining two maps take that sector to the disc. **Corrected in this
    pass:** a first version of this solution used the sector of angle $\pi/4$ and the fourth power;
    it was wrong — interior points were carried outside the disc — and the numerical check that
    exposed it is recorded in the final step.
---

::: {.solution}

Let
$$
P=\frac{1-i}{\sqrt2}=e^{-i\pi/4},\qquad Q=\frac{-1-i}{\sqrt2},
$$
the two points where the line $y=-1/\sqrt2$ meets the unit circle. Define
$$
w=\frac{z-P}{z-Q},\qquad u=e^{-i\pi/4}w,\qquad \varphi(z)=\frac{u^{4/3}-i}{u^{4/3}+i},
$$
where $u^{4/3}=\exp\bigl(\tfrac43\operatorname{Log}u\bigr)$ with $\operatorname{Log}$ the principal branch on the sector $0<\arg u<3\pi/4$.

::: pf

::: {.pf-step #s1}

$\partial G$ is the chord $[Q,P]$ together with the arc of the unit circle through the upper half-plane, and the interior angle of $G$ at each of $P$ and $Q$ is $3\pi/4$.

::: pf-proof

The line $y=-1/\sqrt2$ meets $\abs z=1$ where $x^2+\tfrac12=1$, that is $x=\pm\tfrac1{\sqrt2}$, giving exactly $P$ and $Q$; its intersection with the closed disc is the chord $[Q,P]$. Since $G=\{\abs z<1,\ y>-1/\sqrt2\}$ lies above the chord, the remaining boundary is the arc from $P$ to $Q$ through the upper half-plane.

At $P=e^{-i\pi/4}$ the tangent to the circle is perpendicular to the radius, so it has direction $-i\pi/4+\pi/2=\pi/4$, while the chord has direction $0$ (equivalently $\pi$). The region lies inside the disc and above the chord, so near $P$ it is the sector between the direction $\pi/4$ (along the arc) and the direction $\pi$ (along the chord, pointing away from $P$ towards $Q$). That sector has angle $\pi-\pi/4=3\pi/4$. The same computation at $Q$ gives $3\pi/4$.

:::

:::

::: {.pf-step #s2}

$w$ carries $G$ conformally onto the sector $\{\pi/4<\arg w<\pi\}$; consequently $u$ carries $G$ onto $\{0<\arg u<3\pi/4\}$.

::: pf-proof

$w$ is Möbius with its only pole at $Q\in\partial G$, so it is holomorphic and injective on a neighbourhood of $G$, and it maps the open set $G$ to an open set.

Both boundary curves of $G$ pass through both $P$ and $Q$: the chord is a line through them, and the circle is a circle through them. A Möbius map carries generalized circles to generalized circles and sends $P\mapsto0$, $Q\mapsto\infty$; a generalized circle containing $0$ and $\infty$ is a line through $0$. So each boundary curve maps to a ray from the origin, and $\partial w(G)$ is two rays whose angle at $0$ equals the interior angle of $G$ at the corresponding corner, namely $3\pi/4$ by step [](#s1){.pf-ref}. So $w(G)$ is a sector of angle $3\pi/4$.

To locate it: $w(0)=P/Q=i$ (computed below), and the chord maps to the ray through $w$ of any chord point other than $P,Q$. At the midpoint $-i/\sqrt2$ of the chord,
$$
w(-i/\sqrt2)=\frac{-i/\sqrt2-P}{-i/\sqrt2-Q}=\frac{-1/{\sqrt2}}{1/{\sqrt2}}=-1,
$$
so the chord maps to the ray $\arg w=\pi$. Hence, the sector being of angle $3\pi/4$ with one side $\arg w=\pi$, the other side is $\arg w=\pi/4$, and $w(G)=\{\pi/4<\arg w<\pi\}$.

Rotating by $-e^{i\pi/4}$ subtracts $\pi/4$ from the argument, giving $u(G)=\{0<\arg u<3\pi/4\}$.

:::

:::

::: {.pf-step #s3}

$u\mapsto u^{4/3}$ carries that sector onto the upper half-plane.

::: pf-proof

On the sector $0<\arg u<3\pi/4$, which does not meet the negative real axis, the principal logarithm is holomorphic, so $u\mapsto\exp(\tfrac43\operatorname{Log}u)$ is holomorphic there, with derivative $(\tfrac43)u^{4/3}/u\ne0$; it is injective because the argument map $\theta\mapsto\tfrac43\theta$ is injective on $\bigl(0,\tfrac34\pi\bigr)$ and the modulus map $r\mapsto r^{4/3}$ is injective.

For $u=re^{i\theta}$ with $0<\theta<\tfrac34\pi$ one has $u^{4/3}=r^{4/3}e^{i\frac43\theta}$ with $0<\tfrac43\theta<\pi$, so the image is exactly the open upper half-plane, every point of which has exactly one $(4/3)$-th root in the sector.

:::

:::

::: {.pf-step #s4}

$\zeta\mapsto(\zeta-i)/(\zeta+i)$ carries the upper half-plane onto $\DD$, so $\varphi$ is a conformal map of $G$ onto $\DD$.

::: pf-proof

For $\operatorname{Im}\zeta>0$ we have $\zeta\ne-i$ and
$$
\Bigl|\frac{\zeta-i}{\zeta+i}\Bigr|^2=\frac{(\operatorname{Re}\zeta)^2+(\operatorname{Im}\zeta-1)^2}{(\operatorname{Re}\zeta)^2+(\operatorname{Im}\zeta+1)^2}<1
$$
because $\operatorname{Im}\zeta>0$ gives $(\operatorname{Im}\zeta-1)^2<(\operatorname{Im}\zeta+1)^2$. It is Möbius with inverse $v\mapsto i(1+v)/(1-v)$, which carries $\DD$ onto the upper half-plane, so it is a bijection; being Möbius it is conformal.

Composing the conformal maps of steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and this one shows that $\varphi$ is holomorphic and injective on $G$ with $\varphi(G)=\DD$.

:::

:::

::: {.pf-step #s5}

Numerical check, and the correction it forced.

::: pf-proof

With $P=(1-i)/\sqrt2$ and $Q=(-1-i)/\sqrt2$, evaluating the displayed $\varphi$ gives

| $z$ | in $G$? | $\abs{\varphi(z)}$ |
|---|---|---|
| $0$ | yes | $0.2679$ |
| $0.3i$ | yes | $0.5370$ |
| $0.5+0.2i$ | yes | $0.6663$ |
| $-0.5i$ | yes | $0.4293$ |
| $0.6-0.3i$ | yes | $0.7080$ |
| $-0.4+0.6i$ | yes | $0.8282$ |
| $0.9i$ | yes | $0.9435$ |
| $-0.9i$ | no | $2.179$ |

and on the boundary the values $\abs\varphi$ are $1.000000$ at the points $e^{i\theta}$ for $\theta=-40^\circ,-20^\circ,0^\circ,30^\circ,60^\circ,90^\circ,120^\circ,130^\circ$ of the arc, and $1.000000$ at the chord points $\pm0.6$, $\pm0.2$ (and $1.108$ at $x=\pm0.9$, which lie on the line but outside the disc and hence are not boundary points).

This check was not merely confirmatory. A first version of this solution took the sector to be of angle $\pi/4$ and used the fourth power $w^4$; evaluating it shows $|\varphi(0.5+0.2i)|=1.031$, $|\varphi(-0.5i)|=2.174$ and $|\varphi(-0.4+0.6i)|=1.851$ — interior points thrown outside the disc. The error was the interior angle: the angle at a corner is spanned by the tangent to the circle and the chord, which is $3\pi/4$, and the exponent must be $\pi/(3\pi/4)=4/3$.

:::

:::

:::

:::
