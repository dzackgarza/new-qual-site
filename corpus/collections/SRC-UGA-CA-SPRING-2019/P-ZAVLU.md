---
schema: qual/card@1
id: P-ZAVLU
kind: problem
title: Schwarz–Pick lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Factors
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Let $f$ be a holomorphic map of the open unit disc $\DD$ to itself.
Show that for any $z, w\in \DD$,
$$
\abs{\frac{f(w)-f(z)}{1-\overline{f(w)} f(z)}} \leq\abs{\frac{w-z}{1-\bar{w} z}}
.$$
Show that this inequality is strict for $z\neq w$ except when $f$ is a linear fractional transformation from $\DD$ to itself.
:::

::: {.concept}

The Schwarz conjugation trick:

![](../../assets/Complex_Analysis/999_Quals/figures/2021-11-27_01-09-06.png)

Write the RHS as $a$, we then want something in the form $\abs{F(a)}\leq \abs{a}$.
The choice $a=\psi_w(z)$ is forced, so $z= \inverseof{\psi_w}(a)$.
This forces the choice for the LHS
$$
{ f(w) - (f\circ \inverseof{\psi_w})(a) \over 1 - \bar{f(w)} (f\circ \inverseof{\psi_w})(a) }
= (\psi_{f(w)} \circ f \circ \inverseof{\psi_w})(a) \coloneqq F(a)
.$$

:::

::: {.solution}
For $a\in\DD$ let $\varphi_a(z)=\dfrac{z-a}{1-\bar az}$. It is an automorphism of $\DD$ with $\varphi_a(a)=0$ and inverse $\varphi_{-a}$. The asserted inequality reads $\abs{\varphi_{f(w)}(f(z))}\le\abs{\varphi_w(z)}$.

::: pf

::: {.pf-step #F}
Fix $w\in\DD$ and put $F=\varphi_{f(w)}\circ f\circ\varphi_{-w}$. Then $F$ is a holomorphic self-map of $\DD$ with $F(0)=0$, and $\abs{F(\zeta)}\le\abs{\zeta}$ on $\DD$.

::: pf-proof
$F(0)=\varphi_{f(w)}(f(w))=0$, and $F$ is a composition of holomorphic self-maps of $\DD$. The bound is the Schwarz lemma.
:::

:::

::: {.pf-step #ineq}
For all $z,w\in\DD$, $\abs{\varphi_{f(w)}(f(z))}\le\abs{\varphi_w(z)}$.

::: pf-proof
Apply step [](#F){.pf-ref} at $\zeta=\varphi_w(z)$, for which $\varphi_{-w}(\zeta)=z$.
:::

:::

::: {.pf-step #eq}
If equality holds for one pair $z\neq w$, then $f$ is a linear fractional transformation of $\DD$ onto itself. Conversely, for such $f$ equality holds for all $z,w$.

::: pf-proof
If equality holds at $z\neq w$, then $\zeta=\varphi_w(z)\neq0$ satisfies $\abs{F(\zeta)}=\abs{\zeta}$, so the equality case of the Schwarz lemma gives $F(\zeta)=\lambda\zeta$ with $\abs{\lambda}=1$. Then $f=\varphi_{-f(w)}\circ(\lambda\,\cdot)\circ\varphi_w$ is a composition of linear fractional automorphisms of $\DD$.

Conversely, if $f$ is a linear fractional automorphism of $\DD$, then for each $w$ the map $F$ of step [](#F){.pf-ref} is an automorphism of $\DD$ fixing $0$, hence a rotation $\zeta\mapsto\lambda\zeta$ by the Schwarz lemma applied to $F$ and $F^{-1}$. So $\abs{F(\zeta)}=\abs{\zeta}$ for all $\zeta$, which is equality in step [](#ineq){.pf-ref}.
:::

:::

::: pf-qed
Step [](#ineq){.pf-ref} is the inequality, and step [](#eq){.pf-ref} identifies the equality case: the inequality is strict for all $z\neq w$ unless $f$ is a linear fractional map of $\DD$ onto itself.
:::

:::

:::
