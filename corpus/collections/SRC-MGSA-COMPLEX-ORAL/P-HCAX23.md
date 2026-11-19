---
schema: qual/card@1
id: P-HCAX23
kind: problem
title: Conformal automorphisms of the upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Mobius Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the classification already on the card, whose answer and
    whose two directions are correct. Repaired one gap: the card asserted that because F maps
    the boundary circle to itself 'its coefficients may be scaled to be real', which needs the
    reflection argument — now given explicitly, with conjugate coefficients S(z) = conj(T(conj
    z)) agreeing with T on the extended real line and hence identically. Added: the computation
    of the imaginary part, the explicit inverse of the Cayley transform and the inequality that
    shows it maps the half-plane to the disc, the Schwarz-lemma derivation of the disc
    classification, and the kernel argument giving PSL_2(R) rather than SL_2(R). The card's own
    notation PSL_2 is now written with the preamble's \PSL macro. Not claimed: a retained
    solution set; the collection's provenance is the oral examination compilation.
---

::: {.problem}
Determine all conformal automorphisms of the upper half-plane.
:::

::: {.solution}
Throughout $\halfplane \coloneqq \theset{z \in \CC \mid \operatorname{Im}z > 0}$, $\DD$ is the open unit disc, $\hat{\CC} = \CC \cup \theset{\infty}$ is the Riemann sphere, $\hat{\RR} = \RR \cup \theset{\infty}$, and a Möbius transformation is a map $z \mapsto \frac{az+b}{cz+d}$ with $ad - bc \ne 0$. The collection's `provenance` is the oral-examination compilation, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #imaginary}
For real $a,b,c,d$ with $ad - bc \ne 0$ and $z$ not a pole, $\operatorname{Im}\frac{az+b}{cz+d} = \frac{(ad-bc)\operatorname{Im}z}{\abs{cz+d}^{2}}$, and the map carries $\hat{\RR}$ onto $\hat{\RR}$.

::: pf-proof
Multiply numerator and denominator by $\overline{cz+d}$: $\frac{az+b}{cz+d} = \frac{(az+b)(c\bar z + d)}{\abs{cz+d}^{2}}$, whose numerator is $ac\abs{z}^{2} + adz + bc\bar z + bd$. Twice its imaginary part is $(ad - bc)z - (ad-bc)\bar z = (ad-bc)(z - \bar z) = 2i(ad-bc)\operatorname{Im}z$, using that $ac\abs{z}^{2}$ and $bd$ are real; dividing by $2i\abs{cz+d}^{2}$ gives the formula. For $z$ real, $z = \bar z$, so the numerator is real and the image is real or $\infty$; and the pole $-d/c$ is real when $c \ne 0$, while $c = 0$ gives $\infty \mapsto \infty$.

:::

:::

::: {.pf-step #halfplane-maps}
For real coefficients with $ad-bc > 0$ the map carries $\halfplane$ onto itself, and with $ad-bc < 0$ onto the lower half-plane.

::: pf-proof
By step [](#imaginary){.pf-ref} the sign of the imaginary part of the image is the sign of $(ad-bc)\operatorname{Im}z$, since $\abs{cz+d}^{2} > 0$; so positive determinant preserves the sign of the imaginary part and negative reverses it. The map is injective on $\hat{\CC}$ with Möbius inverse $z \mapsto \frac{dz-b}{-cz+a}$, of determinant $ad-bc$, so it is a bijection.

:::

:::

::: {.pf-step #cayley}
The Cayley transform $C(z) = \frac{z-i}{z+i}$ is a biholomorphism $\halfplane \to \DD$, with inverse $C^{-1}(w) = i\frac{1+w}{1-w}$.

::: pf-proof
Writing $a = 1$, $b = -i$, $c = 1$, $d = i$ gives $ad - bc = i + i = 2i \ne 0$, so $C$ is a biholomorphism of $\hat{\CC}$; its inverse is $z = \frac{-dw + b}{cw - a} = \frac{-iw - i}{w - 1} = i\frac{1+w}{1-w}$. For $z \ne -i$, $\abs{C(z)}^{2} = \frac{\abs{z-i}^{2}}{\abs{z+i}^{2}} = \frac{x^{2} + (y-1)^{2}}{x^{2} + (y+1)^{2}}$ with $z = x + iy$, and this is $< 1$ exactly when $(y-1)^{2} < (y+1)^{2}$, that is when $y > 0$; so $C$ carries $\halfplane$ into $\DD$, and being a bijection of $\hat{\CC}$ carrying the boundary $\hat{\RR}$ onto the unit circle $\abs{w} = 1$ it carries $\halfplane$ onto $\DD$.

:::

:::

::: {.pf-step #disk}
Every automorphism of $\DD$ is $w \mapsto e^{i\theta}\frac{w - \alpha}{1 - \bar\alpha w}$ for some $\theta \in \RR$ and $\alpha \in \DD$, hence Möbius.

::: pf-proof
This is the classification of the conformal automorphisms of the disc: given $\varphi \in \Aut(\DD)$ put $\alpha \coloneqq \varphi^{-1}(0)$ and $\psi \coloneqq \varphi \circ \frac{w+\alpha}{1+\bar\alpha w}$, so that $\psi(0) = 0$; then $\psi$ is an automorphism of $\DD$ with $\psi(0) = 0$, and the Schwarz lemma applied to $\psi$ and to $\psi^{-1}$ gives $\abs{\psi(w)} \le \abs{w} \le \abs{\psi(w)}$, so $\abs{\psi(w)} = \abs{w}$ and $\psi$ is a rotation $w \mapsto e^{i\theta}w$. Solving for $\varphi$ gives the displayed form.

:::

:::

::: {.pf-step #mobius}
Every $F \in \Aut(\halfplane)$ is a Möbius transformation.

::: pf-proof
By step [](#cayley){.pf-ref} the conjugate $CFC^{-1}$ is an automorphism of $\DD$, which is Möbius by step [](#disk){.pf-ref}; and $C$, $C^{-1}$ are Möbius, so their composition with it is a composition of three Möbius transformations, which is Möbius.

:::

:::

::: {.pf-step #real}
If a Möbius transformation $T$ carries $\halfplane$ onto itself then $T(\hat{\RR}) = \hat{\RR}$, and its coefficients can be chosen real.

::: pf-proof
A Möbius transformation is a homeomorphism of $\hat{\CC}$, so it carries the boundary of $\halfplane$ onto the boundary of $T(\halfplane) = \halfplane$, and that boundary is $\hat{\RR}$. Write $T(z) = \frac{az+b}{cz+d}$ and put $S(z) \coloneqq \overline{T(\bar z)} = \frac{\bar a z + \bar b}{\bar c z + \bar d}$, which is Möbius. For $t \in \RR$ one has $T(t) \in \hat{\RR}$, so $T(t) = \overline{T(t)} = S(t)$; the set $\hat{\RR}$ has accumulation points in $\hat{\CC}$, so the two Möbius transformations $S$ and $T$ agree identically. Hence $(a,b,c,d) = \lambda(\bar a,\bar b,\bar c,\bar d)$ for a single $\lambda \ne 0$, since the coefficient vectors of a Möbius transformation are determined up to one scalar. Writing $\lambda = e^{i\varphi}$, the numbers $ae^{-i\varphi/2}, be^{-i\varphi/2}, ce^{-i\varphi/2}, de^{-i\varphi/2}$ each satisfy $u = e^{i\varphi}\bar u = \overline{u}$ when $u$ denotes it, so after this rescaling all four coefficients are real.

:::

:::

::: {.pf-step #sign}
A Möbius transformation with real coefficients lies in $\Aut(\halfplane)$ exactly when $ad - bc > 0$.

::: pf-proof
By step [](#halfplane-maps){.pf-ref} a positive determinant maps $\halfplane$ onto itself, and a negative one maps it onto the lower half-plane, which is not $\halfplane$; a Möbius transformation with real coefficients and nonzero determinant has one of the two signs.

:::

:::

::: pf-step
The conformal automorphisms of $\halfplane$ are exactly $z \mapsto \frac{az+b}{cz+d}$ with $a,b,c,d \in \RR$ and $ad - bc > 0$, so $\Aut(\halfplane) \cong \boxed{\PSL_{2}(\RR)}$.

::: pf-proof
Steps [](#mobius){.pf-ref}, [](#real){.pf-ref} and [](#sign){.pf-ref} show that every $F \in \Aut(\halfplane)$ has such a form, and step [](#halfplane-maps){.pf-ref} that every such form lies in $\Aut(\halfplane)$. Two matrices in $\SL_{2}(\RR)$ induce the same map exactly when one is minus the other, because $\frac{az+b}{cz+d} = \frac{a'z+b'}{c'z+d'}$ forces $(a',b',c',d') = \mu(a,b,c,d)$ and the determinants agree, so $\mu^{2} = 1$; hence the group of these maps is $\SL_{2}(\RR)/\theset{\pm I} = \PSL_{2}(\RR)$, and a matrix of positive determinant is a positive multiple of one of determinant $1$, which does not change the map.

:::

:::

:::
:::
