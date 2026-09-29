---
schema: qual/card@1
id: P-HCAX26
kind: problem
title: The Riemann zeta function and its analytic continuation
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta Function
relations: []
review: draft
---

::: {.problem}
Define the Riemann zeta function, including its analytic continuation.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $\operatorname{Re}s>1$, the Riemann zeta function is
$$
\boxed{
\zeta(s)=\sum_{n=1}^{\infty}\frac1{n^s}.
}
$$

::: pf-proof

This is the defining Dirichlet series on its half-plane of absolute convergence; see [[D-HJYH3|Riemann zeta function]]. In the same half-plane,
$$
\zeta(s)=\prod_{p\text{ prime}}\frac1{1-p^{-s}}.
$$

:::

:::

::: {.pf-step #s2}

The Dirichlet-series function has a unique meromorphic continuation to $\mathbb C$, holomorphic away from a simple pole at $s=1$.

::: pf-proof

The construction and uniqueness are given by [[PR-K4KTF|meromorphic continuation of $\zeta$]]. Thus the symbol $\zeta(s)$ is thereafter used for this meromorphic continuation on all of $\mathbb C$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give the definition and its analytic continuation requested in the problem.

:::

:::

:::
