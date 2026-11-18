---
schema: qual/card@1
id: E-SS8.EX-14
kind: problem
title: Conformal maps from the upper half-plane onto the disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so. Each step re-read: the modulus comparison
    |z - beta|^2 - |z - bbar|^2 = -4 (Im z)(Im beta) shows phi_beta lands in the disc; phi_beta is
    Mobius, maps the real axis to the unit circle and beta to 0, so it is a conformal bijection;
    conjugating an arbitrary F by phi_beta gives an automorphism of the disc fixing 0; and Schwarz
    applied to it and its inverse forces a rotation. The converse direction is stated too. Not
    claimed: any statement about conformal maps of the disc other than the automorphisms, or about
    non-injective holomorphic maps.
---

::: {.exercise}
Prove that all conformal mappings from the upper half-plane $\halfplane$ to the unit disc $\DD$ take the form
$$
e^{i\theta} \frac{z - \beta}{z - \overline{\beta}}, \qquad \theta \in \RR \text{ and } \beta \in \halfplane.
$$
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none was located for this exercise among the retained sets. It is checked against Stein and Shakarchi, Complex Analysis (2003), Chapter 8 Exercise 14.

::: pf

::: {.pf-step #inside}
For $\beta\in\halfplane$ the map $\phi_{\beta}(z)=\dfrac{z-\beta}{z-\overline\beta}$ carries $\halfplane$ into $\DD$.

::: pf-proof
$\abs{z-\beta}^{2}-\abs{z-\overline\beta}^{2}=-4\operatorname{Im}z\,\operatorname{Im}\beta<0$ when $\operatorname{Im}z>0$ and $\operatorname{Im}\beta>0$, so $\abs{z-\beta}<\abs{z-\overline\beta}$ and $\abs{\phi_{\beta}(z)}<1$. Also $z\ne\overline\beta$ on the half-plane because $\operatorname{Im}\overline\beta<0$.
:::

:::

::: {.pf-step #bijection}
$\phi_{\beta}$ is a conformal bijection $\halfplane\to\DD$, with $\phi_{\beta}(\beta)=0$.

::: pf-proof
$\phi_{\beta}$ is a Möbius transformation, hence a bijection of the Riemann sphere carrying generalized circles to generalized circles. It maps the boundary $\RR\cup\{\infty\}$ to the unit circle, since $\abs{z-\beta}=\abs{z-\overline\beta}$ for real $z$ and $\phi_{\beta}(\infty)=1$. Since it maps the interior point $\beta$ to $0\in\DD$, it maps the component $\halfplane$ onto $\DD$; it is holomorphic with nonvanishing derivative there, hence conformal.
:::

:::

::: {.pf-step #automorphism}
For a conformal bijection $F:\halfplane\to\DD$ with $\beta=F^{-1}(0)$, the map $G=F\circ\phi_{\beta}^{-1}$ is an automorphism of $\DD$ fixing $0$.

::: pf-proof
Both $F$ and $\phi_{\beta}^{-1}$ are conformal bijections onto $\DD$, so the composite is a conformal bijection of $\DD$ with itself; $G(0)=F(\phi_{\beta}^{-1}(0))=F(\beta)=0$.
:::

:::

::: {.pf-step #rotation}
$G(w)=e^{i\theta}w$ for some $\theta\in\RR$.

::: pf-proof
$G$ and $G^{-1}$ both map $\DD$ into $\DD$ and fix $0$, so Schwarz's lemma gives $\abs{G(w)}\le\abs{w}$ and $\abs{G^{-1}(w)}\le\abs{w}$, hence $\abs{G(w)}=\abs{w}$ for all $w$. Equality in Schwarz's lemma forces $G$ to be a rotation, $G(w)=e^{i\theta}w$.
:::

:::

::: {.pf-step}
Every conformal bijection $\halfplane\to\DD$ has the stated form, and conversely.

::: pf-proof
$F=G\circ\phi_{\beta}=e^{i\theta}\phi_{\beta}$, that is
$$
\boxed{F(z)=e^{i\theta}\frac{z-\beta}{z-\overline\beta},\qquad \theta\in\RR,\ \beta\in\halfplane.}
$$
Conversely, a map of this form is the composite of the conformal bijection $\phi_{\beta}$ with the rotation $w\mapsto e^{i\theta}w$ of $\DD$, hence is a conformal bijection $\halfplane\to\DD$.
:::

:::

:::
:::
