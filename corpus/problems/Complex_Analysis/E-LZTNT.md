---
schema: qual/card@1
id: E-LZTNT
kind: problem
title: Every value in $\CC\cup\{\infty\}$ is a limit of $e^{1/z^2}$ at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Essential Singularities
  - Casorati-Weierstrass
  - Singularities
relations: []
review: draft
---

::: {.exercise}
Fix $a\in \CC\union\theset{\infty}$ and let $f(z) \coloneqq e^{1\over z^2}$.
Find a sequence $z_k\to 0$ such that $f(z_k) \convergesto{k\to\infty} a$.
:::

::: {.solution}
::: pf

::: pf-step
If $a\in\CC^\times$, let $L$ satisfy $e^L=a$ and let $z_k$ be either square root of $(L+2\pi ik)^{-1}$ for $k\ge1$ with $L+2\pi ik\neq0$. Then $z_k\to0$ and $f(z_k)=a$.

::: pf-proof
$\abs{L+2\pi ik}\to\infty$, so $z_k\to0$, and $1/z_k^2=L+2\pi ik$ gives $f(z_k)=e^{L+2\pi ik}=a$.
:::

:::

::: pf-step
If $a=0$, take $z_k=i/\sqrt k$.

::: pf-proof
$1/z_k^2=-k$, so $f(z_k)=e^{-k}\to0$.
:::

:::

::: pf-step
If $a=\infty$, take $z_k=1/\sqrt k$.

::: pf-proof
$1/z_k^2=k$, so $f(z_k)=e^k\to\infty$ in $\CP^1$.
:::

:::

:::

:::
