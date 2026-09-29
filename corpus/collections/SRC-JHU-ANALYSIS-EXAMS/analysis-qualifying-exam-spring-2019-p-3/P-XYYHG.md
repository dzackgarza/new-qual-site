---
schema: qual/card@1
id: P-XYYHG
kind: problem
title: Automorphisms of the upper half plane
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Question 2.1. Determine all holomorphic automorphisms of the upper half plane $u =$ $\lbrace z : I m z > 0 \rbrace$
:::

::: {.solution}
Let $\HH=\{z:\Im z>0\}$ and let $\phi(z)=\frac{z-i}{z+i}$, the Cayley transform, a biholomorphism $\HH\to\DD$.

::: pf

::: {.pf-step #s1}

Every map $T(z)=\frac{az+b}{cz+d}$ with $a,b,c,d\in\RR$ and $ad-bc=1$ is an automorphism of $\HH$.

::: pf-proof

For real coefficients, $\Im T(z)=\frac{(ad-bc)\Im z}{\abs{cz+d}^2}=\frac{\Im z}{\abs{cz+d}^2}$, so $T$ maps $\HH$ into $\HH$. Its inverse $\frac{dz-b}{-cz+a}$ has the same form.

:::

:::

::: {.pf-step #s2}

Every automorphism $T$ of $\HH$ has this form.

::: pf-proof

$\phi\circ T\circ\phi^{-1}$ is an automorphism of $\DD$, hence a Möbius map $w\mapsto e^{i\theta}\frac{w-a}{1-\bar aw}$ by the Schwarz lemma, so $T$ is a Möbius map. It extends to a homeomorphism of $\overline\HH\cup\{\infty\}$, so it maps $\RR\cup\{\infty\}$ onto itself. A Möbius map is determined by the images of $0$, $1$ and $\infty$, and when these are real, the linear conditions on $(a,b,c,d)$ have real coefficients and a one-dimensional solution space; so $T$ has a real representative, which can be scaled to $ad-bc=\pm1$. Since $\Im T(i)=\frac{ad-bc}{c^2+d^2}>0$, the sign is $+1$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $\operatorname{Aut}(\HH)=\boxed{\Bigl\{z\mapsto\frac{az+b}{cz+d}:a,b,c,d\in\RR,\ ad-bc=1\Bigr\}}\cong\operatorname{PSL}_2(\RR)$.

:::

:::

:::
