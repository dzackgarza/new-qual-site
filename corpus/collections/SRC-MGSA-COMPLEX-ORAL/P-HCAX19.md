---
schema: qual/card@1
id: P-HCAX19
kind: problem
title: Conformal equivalence of a half-disk and the disk
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the card's own argument into Lamport steps. The three maps are kept
    (T(z) = (1+z)/(1-z) from the disc to the right half-plane, squaring from the first
    quadrant to the upper half-plane, C(z) = (z-i)/(z+i) from there to the disc), and the
    three claims the prose asserted are now proved: T maps the disc onto the right half-plane
    and the half-disc onto the first quadrant, with the images of the diameter and of the
    upper semicircle computed from Re T and Im T; squaring is a bijection of the quadrant
    with the half-plane; and C is a bijection of the half-plane with the disc. The composition
    is checked to be a conformal isomorphism, and its explicit formula is stated with the
    substitution of T made once. No statement repair; the problem says "the upper half of the
    unit disk", which the card names H. No retained solution set covers this problem: the
    collection's provenance, assets/attachments/MGSA_Complex_Analysis_Oral_Questions.pdf, is
    the question sheet.
---

::: {.problem}
Show that the upper half of the unit disk is conformally equivalent to the unit disk, and give an explicit conformal isomorphism.
:::

::: {.solution}
No retained solution set covers this problem — the collection's provenance, `assets/attachments/MGSA_Complex_Analysis_Oral_Questions.pdf`, is the question sheet — so the argument is the card's own.

Throughout, $H=\{z : \abs z<1,\ \operatorname{Im}z>0\}$ is the upper half of the unit disc, $D=\{z : \abs z<1\}$, $Q=\{w : \operatorname{Re}w>0,\ \operatorname{Im}w>0\}$ is the first quadrant, $\HH=\{w:\operatorname{Im}w>0\}$ is the upper half-plane, and a conformal isomorphism of domains is a bijective holomorphic map with holomorphic inverse.

::: pf

::: {.pf-step #moebius}
$T(z)=\frac{1+z}{1-z}$ is a conformal isomorphism of $D$ onto $\{w:\operatorname{Re}w>0\}$, and $T(H)=Q$.

::: pf-proof
$T$ is a Möbius transformation, hence holomorphic on $\CC\setminus\{1\}$ and injective, with inverse $T^{-1}(w)=\frac{w-1}{w+1}$, which is holomorphic off $w=-1$; so $T$ is a conformal isomorphism onto its image.

For $\abs z<1$,
$\operatorname{Re}T(z)=\operatorname{Re}\frac{(1+z)\overline{(1-z)}}{\abs{1-z}^2}=\frac{1-\abs z^2}{\abs{1-z}^2}>0$,
since $\abs z<1$ and $z\neq1$. Conversely, if $\operatorname{Re}w>0$ then $z=T^{-1}(w)=\frac{w-1}{w+1}$ satisfies $\abs z<1$: indeed $\abs{w-1}<\abs{w+1}$ because $\operatorname{Re}w>0$, and $\abs z^2=\frac{\abs{w-1}^2}{\abs{w+1}^2}<1$. So $T(D)=\{\operatorname{Re}w>0\}$.

For the image of $H$: if $z\in H$ then $\operatorname{Re}T(z)>0$ as above, while
$\operatorname{Im}T(z)=\operatorname{Im}\frac{(1+z)\overline{(1-z)}}{\abs{1-z}^2}=\frac{2\operatorname{Im}z}{\abs{1-z}^2}>0$,
so $T(z)\in Q$. Conversely, if $w\in Q$ and $z=T^{-1}(w)$, then $\abs z<1$ and $\operatorname{Im}z=\operatorname{Im}\frac{w-1}{w+1}=\frac{2\operatorname{Im}w}{\abs{w+1}^2}>0$, so $z\in H$. Hence $T(H)=Q$.
:::

:::

::: {.pf-step #square}
$S(w)=w^2$ is a conformal isomorphism of $Q$ onto $\HH$.

::: pf-proof
Write $w=\rho e^{i\theta}$ with $\rho>0$ and $\theta\in(0,\pi/2)$, which is possible and unique for $w\in Q$. Then $S(w)=\rho^2e^{2i\theta}$ with $2\theta\in(0,\pi)$, so $S(w)\in\HH$. Conversely, if $\zeta=Re^{i\varphi}$ with $R>0$ and $\varphi\in(0,\pi)$, the two square roots are $\sqrt{R}e^{i\varphi/2}$ and its negative; exactly one of them, $\sqrt R e^{i\varphi/2}$, has argument in $(0,\pi/2)$ and hence lies in $Q$. So $S$ is a bijection $Q\to\HH$; it is holomorphic with holomorphic inverse $w=\sqrt\zeta$ on $\HH$, the branch of the square root with positive real part being holomorphic on $\CC\setminus(-\infty,0]$. Hence it is a conformal isomorphism.
:::

:::

::: {.pf-step #cayley}
$C(\zeta)=\frac{\zeta-i}{\zeta+i}$ is a conformal isomorphism of $\HH$ onto $D$.

::: pf-proof
$C$ is Möbius, so holomorphic off $\zeta=-i$ and injective on $\HH$; its inverse $C^{-1}(\xi)=i\frac{1+\xi}{1-\xi}$ is holomorphic off $\xi=1$.

For $\zeta\in\HH$: $\abs{\zeta-i}<\abs{\zeta+i}$, since the point $\zeta$ is closer to $i$ than to $-i$ exactly when $\operatorname{Im}\zeta>0$; hence $\abs{C(\zeta)}=\frac{\abs{\zeta-i}}{\abs{\zeta+i}}<1$ and $C(\HH)\subseteq D$. Conversely, if $\abs\xi<1$ and $\zeta=C^{-1}(\xi)=i\frac{1+\xi}{1-\xi}$, then $\operatorname{Im}\zeta$ has the sign of $\operatorname{Re}\frac{1+\xi}{1-\xi}=\frac{1-\abs\xi^2}{\abs{1-\xi}^2}>0$, so $\zeta\in\HH$. Hence $C$ maps $\HH$ bijectively onto $D$, conformally.
:::

:::

::: {.pf-step #composite}
$F=C\circ S\circ T$ is a conformal isomorphism of $H$ onto $D$, given explicitly by
$F(z)=\frac{\big(\frac{1+z}{1-z}\big)^2-i}{\big(\frac{1+z}{1-z}\big)^2+i}$.

::: pf-proof
$T$ carries $H$ bijectively onto $Q$ and is conformal (step [](#moebius){.pf-ref}), $S$ carries $Q$ bijectively onto $\HH$ conformally (step [](#square){.pf-ref}), and $C$ carries $\HH$ bijectively onto $D$ conformally (step [](#cayley){.pf-ref}). A composition of conformal isomorphisms is a conformal isomorphism, with inverse $T^{-1}\circ S^{-1}\circ C^{-1}$. Composing the three formulas gives $F(z)=\frac{\big(\frac{1+z}{1-z}\big)^2-i}{\big(\frac{1+z}{1-z}\big)^2+i}$, which is the explicit map required.
:::

:::

:::
:::
