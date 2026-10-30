---
schema: qual/card@1
id: P-BKF18-2B
kind: problem
title: A real polynomial forced to have a nonreal zero
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Suppose $p$ is a nonconstant real polynomial such that for some real $a$, $p(a)\ne0$ and $p'(a)=p''(a)=0$.
Prove that $p$ has at least one nonreal zero.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Suppose $p$ has only real zeros $r_1,\dots,r_n$ (with multiplicity), $n=\deg p\ge1$. Then for real $x$ with $p(x)\ne0$,
$$
\left(\frac{p'}{p}\right)'(x)=-\sum_{i=1}^n\frac{1}{(x-r_i)^2}<0.
$$

::: pf-proof

Write $p(x)=c\prod_i(x-r_i)$ with $c\in\RR\setminus\{0\}$. Logarithmic differentiation gives $p'/p=\sum_i 1/(x-r_i)$. Differentiate once more. The sum is strictly negative because $n\ge1$ and each term is positive.

:::

:::

::: {.pf-step #s2}

$\left(p'/p\right)'(a)=0$.

::: pf-proof

$\left(p'/p\right)'=(p''p-p'^2)/p^2$, and $p'(a)=p''(a)=0$, $p(a)\ne0$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} contradict each other at $x=a$. So $p$ has a nonreal zero.

:::

:::

:::
