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
<1>1. For $\operatorname{Re}s>1$, the Riemann zeta function is
$$
\boxed{
\zeta(s)=\sum_{n=1}^{\infty}\frac1{n^s}.
}
$$
::: {.proof}
This is the defining Dirichlet series on its half-plane of absolute convergence; see [[D-HJYH3|Riemann zeta function]]. In the same half-plane,
$$
\zeta(s)=\prod_{p\text{ prime}}\frac1{1-p^{-s}}.
$$
:::

<1>2. The Dirichlet-series function has a unique meromorphic continuation to $\mathbb C$, holomorphic away from a simple pole at $s=1$.
::: {.proof}
The construction and uniqueness are given by [[PR-K4KTF|meromorphic continuation of $\zeta$]]. Thus the symbol $\zeta(s)$ is thereafter used for this meromorphic continuation on all of $\mathbb C$.
:::

<1>3. Q.E.D.
::: {.proof}
Steps <1>1--<1>2 give the definition and its analytic continuation requested in the problem.
:::
:::
