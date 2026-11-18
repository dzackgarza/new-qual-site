---
schema: qual/card@1
id: E-SS8.EX-12
kind: problem
title: Fixed points of holomorphic self-maps of the disc
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Fixed Points
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
A complex number $w \in \DD$ is a fixed point for the map $f \colon \DD \to \DD$ if $f(w) = w$.

(a) Prove that if $f \colon \DD \to \DD$ is analytic and has two distinct fixed points, then $f$ is the identity, that is, $f(z) = z$ for all $z \in \DD$.

(b) Must every holomorphic function $f \colon \DD \to \DD$ have a fixed point? [Hint: Consider the upper half-plane.]
:::

::: {.solution}

The argument is the card's own: conjugate by a disc automorphism sending a fixed point to $0$ and apply Schwarz's lemma; for (b) transport a fixed-point-free automorphism of the upper half-plane.

::: pf

::: {.pf-step #transport}

For $a\in\DD$ there is an automorphism $\phi$ of $\DD$ with $\phi(a)=0$; then $g=\phi\circ f\circ\phi^{-1}$ is a holomorphic self-map of $\DD$ with $g(0)=0$, and fixed points of $f$ correspond to fixed points of $g$.

::: pf-proof

Take $\phi(z)=\frac{z-a}{1-\bar a z}$, which is holomorphic on a neighbourhood of $\DD$, maps $\DD$ bijectively onto $\DD$ (for $\abs{z}<1$ one computes $\abs{\phi(z)}<1$ with equality only when $\abs{z}=1$), and satisfies $\phi(a)=0$; its inverse $\phi^{-1}(w)=\frac{w+a}{1+\bar a w}$ is of the same form. Then $g=\phi\circ f\circ\phi^{-1}$ is a composite of holomorphic maps $\DD\to\DD$, so it is holomorphic and maps $\DD$ into $\DD$, with $g(0)=\phi(f(a))=\phi(a)=0$. Finally $f(w)=w\iff g(\phi(w))=\phi(w)$, so the fixed points of $f$ correspond bijectively, via $\phi$, to those of $g$.

:::

:::

::: {.pf-step #schwarz}

If $g:\DD\to\DD$ is holomorphic with $g(0)=0$ and $\abs{g(c)}=\abs{c}$ for some $c\ne0$, then $g(z)=e^{i\theta}z$.

::: pf-proof

This is the equality case of Schwarz's lemma: $g(0)=0$ and $\abs{g}\le1$ give $\abs{g(z)}\le\abs{z}$ on $\DD$, and when equality holds at one point $c\ne0$ the lemma's rigidity clause says $g$ is a rotation $z\mapsto e^{i\theta}z$ with $\theta\in\RR$.

:::

:::

::: {.pf-step #parta}

(a) If $f:\DD\to\DD$ is analytic with two distinct fixed points then $f=\mathrm{id}$.

::: pf-proof

Let $a\ne b$ in $\DD$ be fixed points and let $\phi$, $g$ be as in step [](#transport){.pf-ref} with $\phi(a)=0$. Then $c=\phi(b)\ne0$ because $\phi$ is injective and $b\ne a$, and $g(c)=\phi(f(b))=\phi(b)=c$, so $\abs{g(c)}=\abs{c}$. By step [](#schwarz){.pf-ref} $g(z)=e^{i\theta}z$, and $g(c)=c$ with $c\ne0$ forces $e^{i\theta}=1$. Hence $g=\mathrm{id}$ and therefore $f=\phi^{-1}\circ g\circ\phi=\mathrm{id}$:
$$
\boxed{f \text{ analytic, } \DD\to\DD,\ \text{two distinct fixed points}\implies f(z)=z.}
$$

:::

:::

::: {.pf-step #upper}

$\phi(z)=\dfrac{z-i}{z+i}$ maps the upper half-plane biholomorphically onto $\DD$, and $T(z)=z+1$ is a fixed-point-free automorphism of the upper half-plane.

::: pf-proof

For $\operatorname{Im}z>0$, $\abs{z-i}<\abs{z+i}$ because the first distance is to a point above and the second to a point below, so $\abs{\phi(z)}<1$; $\phi$ is a biholomorphism onto $\DD$ with inverse $w\mapsto i\frac{1+w}{1-w}$, which maps $\DD$ into the upper half-plane. $T(z)=z+1$ is holomorphic with holomorphic inverse $z\mapsto z-1$ and preserves the upper half-plane since $\operatorname{Im}(z+1)=\operatorname{Im}z>0$. It has no fixed point: $z=z+1$ has no solution.

:::

:::

::: {.pf-step #partb}

(b) Not every holomorphic $f:\DD\to\DD$ has a fixed point.

::: pf-proof

With $\phi$ and $T$ as in step [](#upper){.pf-ref}, put $F=\phi\circ T\circ\phi^{-1}:\DD\to\DD$, a holomorphic self-map of the disc. If $F(w)=w$ then applying $\phi^{-1}$ gives $T(\phi^{-1}(w))=\phi^{-1}(w)$, a fixed point of $T$, which does not exist. So
$$
\boxed{F \text{ has no fixed point in } \DD.}
$$

:::

:::

:::

:::
