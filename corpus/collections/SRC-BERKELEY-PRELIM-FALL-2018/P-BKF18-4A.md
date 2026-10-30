---
schema: qual/card@1
id: P-BKF18-4A
kind: problem
title: A cosine power series
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $a\in\RR$ with $\abs{a}<1$.
Prove that
$$
\sum_{k=1}^{\infty}a^k\cos(k\theta)
=\frac{-a^2+a\cos\theta}{1+a^2-2a\cos\theta}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

With $z=e^{i\theta}$,
$$
\sum_{k=1}^\infty a^k\cos(k\theta)=\operatorname{Re}\frac{az}{1-az}.
$$

::: pf-proof

Since $\abs{az}=\abs{a}<1$, the geometric series gives $\sum_{k\ge1}a^kz^k=az/(1-az)$, and $\operatorname{Re}(a^kz^k)=a^k\cos(k\theta)$ because $a$ is real.

:::

:::

::: {.pf-step #s2}

$$
\operatorname{Re}\frac{az}{1-az}=\frac{a\cos\theta-a^2}{1+a^2-2a\cos\theta}.
$$

::: pf-proof

Multiply numerator and denominator by $1-a\bar z$. Since $z\bar z=1$, the numerator becomes $az-a^2$, and the denominator becomes
$$
\abs{1-az}^2=(1-a\cos\theta)^2+a^2\sin^2\theta=1+a^2-2a\cos\theta,
$$
which is real. The real part of $az-a^2$ is $a\cos\theta-a^2$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give the identity.

:::

:::

:::
