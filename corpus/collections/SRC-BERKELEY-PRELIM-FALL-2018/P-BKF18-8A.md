---
schema: qual/card@1
id: P-BKF18-8A
kind: problem
title: GCD distributes over LCM
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
For nonzero integers $a,b,c$, show that
$$
\gcd(a,\operatorname{lcm}(b,c))
=\operatorname{lcm}(\gcd(a,b),\gcd(a,c)).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

It suffices to show, for each prime $p$ with exponents $\alpha,\beta,\gamma$ in $a,b,c$, that
$$
\min\{\alpha,\max\{\beta,\gamma\}\}=\max\{\min\{\alpha,\beta\},\min\{\alpha,\gamma\}\}.
$$

::: pf-proof

Both sides of the claimed identity are positive integers. A positive integer is determined by the exponent of each prime in it. The exponent of $p$ in $\gcd(x,y)$ is the minimum, and in $\operatorname{lcm}(x,y)$ the maximum, of the exponents in $x$ and $y$.

:::

:::

::: {.pf-step #s2}

The identity of step [](#s1){.pf-ref} holds.

::: pf-proof

By symmetry in $\beta,\gamma$, assume $\beta\le\gamma$. Then $\max\{\beta,\gamma\}=\gamma$ and $\min\{\alpha,\beta\}\le\min\{\alpha,\gamma\}$, so both sides equal $\min\{\alpha,\gamma\}$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove the identity.

:::

:::

:::
