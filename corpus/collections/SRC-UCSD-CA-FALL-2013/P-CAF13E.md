---
schema: qual/card@1
id: P-CAF13E
kind: problem
title: "Conformal bijections involving half-planes, slits, and Möbius transformations"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
(a) Prove that the function $f(z) = \left(\frac{1 + \sqrt{z}}{1 - \sqrt{z}}\right)^2$ is a conformal bijection mapping $\CC_-$ onto $\DD \setminus [0, 1)$.

(b) Let $f(z) = \frac{az + b}{cz + d}$ with $a, b, c, d \in \RR$ and $ad - bc < 0$.
Show that $f$ is a conformal bijection from $\CC_+$ onto $\CC_-$.
:::

::: {.remark}
The official Fall 2013 UCSD exam has $\CC_-$ in part (a). An earlier
transcription of this card incorrectly had $\CC_+$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own chain of conformal maps for (a) and the imaginary-part formula for (b) are set out step by step.

Let $\CC_{-}=\theset{\operatorname{Im}z<0}$ and $\CC_{+}=\theset{\operatorname{Im}z>0}$.

::: pf

::: {.pf-step #branch}
On $\CC_{-}$ the branch $\sqrt z=\abs z^{1/2}e^{i\arg z/2}$ with $\pi<\arg z<2\pi$ maps $\CC_{-}$ conformally onto the second quadrant $Q=\theset{\operatorname{Re}w<0,\operatorname{Im}w>0}$.

::: pf-proof
On $\CC_{-}$ minus the negative real axis the argument $\arg z\in(\pi,2\pi)$ is a holomorphic branch of the argument, so $\sqrt z$ is holomorphic there; it is injective with inverse $w\mapsto w^{2}$ on $Q$. Since $\pi/2<\arg z/2<\pi$, the image lies in the second quadrant, and every $w$ in the second quadrant has $w^{2}\in\CC_{-}$.
:::

:::

::: {.pf-step #mobius}
$M(w)=\dfrac{1+w}{1-w}$ maps $Q$ conformally onto the upper half of the unit disc.

::: pf-proof
$M$ is a Möbius map, so conformal; $w=-1$ and $w=1$ are the pole and the zero. For $w=it$ on the positive imaginary axis, $\abs{M(it)}=\abs{1+it}/\abs{1-it}=1$, so the imaginary axis maps into the unit circle; for $w=0$, $M=1$, and $M$ maps the right half-plane onto the disc (this is the Cayley transform), so the second quadrant, which lies to the left of the imaginary axis and above the real axis, maps into the disc and above the real axis, giving the upper half disc.
:::

:::

::: {.pf-step #square}
$w\mapsto w^{2}$ maps the upper half disc conformally onto $\DD\setminus[0,1)$.

::: pf-proof
Squaring is holomorphic with nonzero derivative off $0$ and is injective on the upper half disc (polar coordinates: $re^{i\theta}\mapsto r^{2}e^{2i\theta}$ with $0<r<1$, $0<\theta<\pi$, and $2\theta\in(0,2\pi)$ determines $\theta$). The image is $\theset{0<\abs{\zeta}<1,\ 0<\arg\zeta<2\pi}=\DD\setminus[0,1)$.
:::

:::

::: {.pf-step #part-a}
$f(z)=\Big(\dfrac{1+\sqrt z}{1-\sqrt z}\Big)^{2}$ is a conformal bijection of $\CC_{-}$ onto $\DD\setminus[0,1)$.

::: pf-proof
$f$ is the composite of the branch of step [](#branch){.pf-ref}, the Möbius map $M$ of step [](#mobius){.pf-ref} (applied to $\sqrt z$) and the square of step [](#square){.pf-ref}; a composite of conformal bijections between the intermediate domains is a conformal bijection onto the final one.
:::

:::

::: {.pf-step #part-b}
For $f(z)=\dfrac{az+b}{cz+d}$ with real $a,b,c,d$ and $ad-bc<0$, $\operatorname{Im}f(z)=\dfrac{(ad-bc)\operatorname{Im}z}{\abs{cz+d}^{2}}$, so $f$ maps $\CC_{+}$ conformally onto $\CC_{-}$.

::: pf-proof
Writing $f(z)=\dfrac{(az+b)(c\bar z+d)}{\abs{cz+d}^{2}}$ and taking imaginary parts with real coefficients, $\operatorname{Im}\big((az+b)(c\bar z+d)\big)=(ad-bc)\operatorname{Im}z$; the denominator $\abs{cz+d}^{2}$ is positive real wherever $cz+d\ne0$. Since $ad-bc<0$, $\operatorname{Im}z>0$ gives $\operatorname{Im}f(z)<0$. A Möbius map with nonvanishing derivative is conformal and injective on the Riemann sphere, so on $\CC_{+}$ (which omits the pole $-d/c$ when $c\ne0$) it is a conformal bijection onto its image, and every $w\in\CC_{-}$ has preimage $z=\dfrac{dw-b}{a-cw}\in\CC_{+}$ by the same computation with the inverse matrix, whose determinant is also $ad-bc<0$.
:::

:::

::: {.pf-qed}
Part (a) is step [](#part-a){.pf-ref} and part (b) is step [](#part-b){.pf-ref}.
:::

:::

:::
