---
schema: qual/card@1
id: P-XVXER
kind: problem
title: Unit quaternions and $\SO(3)$
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Geometry
  - Matrix Groups
relations: []
review: draft
---

::: {.problem}
Describe the group of unit quaternions topologically and explain its relationship with $\SO(3)$.
:::

::: {.solution}
Write $\HH=\{a+bi+cj+dk:a,b,c,d\in\RR\}$ with norm $\abs{q}^2=q\bar q=a^2+b^2+c^2+d^2$, and let $\operatorname{Im}\HH\cong\RR^3$ be the purely imaginary quaternions.
For a unit quaternion $q$ define $\rho(q)(v)=qvq^{-1}$ for $v\in\operatorname{Im}\HH$.

::: pf

::: {.pf-step #sphere}
The unit quaternions form the sphere $S^3\subset\RR^4$, a compact connected Lie group under multiplication, isomorphic to $\SU(2)$.

::: pf-proof
The condition $\abs{q}=1$ is $a^2+b^2+c^2+d^2=1$.
The norm is multiplicative, so $S^3$ is closed under products and inverses, and multiplication is polynomial in the coordinates.
The map $a+bi+cj+dk\mapsto\begin{pmatrix}a+bi & c+di\\ -c+di & a-bi\end{pmatrix}$ is an injective algebra homomorphism $\HH\to M_2(\CC)$ carrying $S^3$ onto $\SU(2)$.
:::

:::

::: {.pf-step #hom}
$\rho$ is a continuous homomorphism $S^3\to\SO(3)$.

::: pf-proof
Conjugation fixes the real axis and preserves the norm, and $\operatorname{Im}\HH$ is the orthogonal complement of the real axis, so $\rho(q)$ is an orthogonal map of $\operatorname{Im}\HH$.
The function $q\mapsto\det\rho(q)\in\{\pm1\}$ is continuous on the connected space $S^3$ and equals $1$ at $q=1$, so $\rho(q)\in\SO(3)$.
Clearly $\rho(qq')=\rho(q)\rho(q')$.
:::

:::

::: {.pf-step #onto}
$\rho$ is surjective.

::: pf-proof
For a unit vector $u\in\operatorname{Im}\HH$ and $\theta\in\RR$, the quaternion $q=\cos(\theta/2)+\sin(\theta/2)u$ satisfies $\rho(q)u=u$, and $\rho(q)$ rotates the plane $u^\perp$ by the angle $\theta$, as a direct computation with $u=i$ shows.
Every element of $\SO(3)$ is a rotation about some axis by some angle.
:::

:::

::: {.pf-step #kernel}
$\ker\rho=\{\pm1\}$.

::: pf-proof
$\rho(q)=\id$ means $q$ commutes with $i$, $j$ and $k$, which forces $q\in\RR$; with $\abs{q}=1$ this is $q=\pm1$.
:::

:::

::: pf-step
$S^3\cong\SU(2)\to\SO(3)$ is a two-sheeted covering homomorphism, and $\SO(3)\cong S^3/\{\pm1\}\cong\RR P^3$.

::: pf-proof
By steps [](#hom){.pf-ref}, [](#onto){.pf-ref} and [](#kernel){.pf-ref}, $\rho$ induces a continuous bijective homomorphism $S^3/\{\pm1\}\to\SO(3)$, which is a homeomorphism because $S^3$ is compact and $\SO(3)$ is Hausdorff.
The quotient of $S^3$ by the free action of $\{\pm1\}$ is a two-sheeted covering, and $S^3/\{\pm1\}$ is $\RR P^3$ by definition.
:::

:::

:::

:::
