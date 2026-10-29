---
schema: qual/card@1
id: P-M9SRT
kind: problem
title: The series $\sum_{n=1}^\infty f(z/n)$ for $f$ vanishing to order $2$ at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f$ be analytic on $\DD$, with $f(0)=f'(0)=0$. Show that
$$
g(z)=\sum_{n=1}^\infty f(z/n)
$$
defines an analytic function on $\DD$. Moreover, prove that
$$
g(z)=f(z)\sum_{n=1}^\infty\frac1{n^2}
$$
for all $z\in\DD$ if and only if $f(z)=cz^2$ for some constant $c$.
:::

::: {.solution}
Write $f(z)=\sum_{m\ge2}a_mz^m$ on $\DD$ and $\zeta(m)=\sum_{n\ge1}n^{-m}$ for $m\ge2$.

::: pf

::: pf-step
$g$ is analytic on $\DD$.

::: pf-proof
Since $f(0)=f'(0)=0$, $F(z)=f(z)/z^2$ extends holomorphically to $\DD$. For $0<r<1$ let $M_r=\max_{\abs{w}\le r}\abs{F(w)}$. For $\abs{z}\le r$ and $n\ge1$, $\abs{z/n}\le r$, so $\abs{f(z/n)}\le M_r\abs{z}^2/n^2\le M_r/n^2$. By the Weierstrass $M$-test the series converges uniformly on $\abs{z}\le r$, and a locally uniform limit of holomorphic functions is holomorphic.
:::

:::

::: {.pf-step #coefficients}
$g(z)=\sum_{m\ge2}a_m\zeta(m)z^m$ on $\DD$.

::: pf-proof
For $z\in\DD$, $\sum_n\sum_m\abs{a_m}\abs{z}^mn^{-m}\le\zeta(2)\sum_m\abs{a_m}\abs{z}^m<\infty$, so the double series converges absolutely and may be summed over $n$ first.
:::

:::

::: pf-step
$g=\zeta(2)f$ on $\DD$ if and only if $f(z)=cz^2$ for a constant $c$.

::: pf-proof
By step [](#coefficients){.pf-ref} and uniqueness of power series coefficients, $g=\zeta(2)f$ if and only if $a_m(\zeta(m)-\zeta(2))=0$ for all $m\ge2$. For $m>2$, $n^{-m}<n^{-2}$ for $n\ge2$, so $\zeta(m)<\zeta(2)$. Hence the condition holds if and only if $a_m=0$ for all $m>2$, that is, $f(z)=a_2z^2$.
:::

:::

:::
:::
