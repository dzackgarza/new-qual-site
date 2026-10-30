---
schema: qual/card@1
id: P-BKS07-5A
kind: problem
title: Solutions of an order-$r$ linear ODE with $C^m$ coefficients are $C^{m+r}$
classification:
  areas: [prelim]
  topics:
  - Calculus
relations: []
review: draft
---

::: {.problem}
Let $a_{0}(x), a_{1}(x), \ldots, a_{r-1}(x)$ and $b(x)$ be $C^{m}$ functions on $\RR$. Prove that if $y(x)$ is a solution of the differential equation
$$
y^{(r)} + a_{r-1}(x) y^{(r-1)} + \cdots + a_{1}(x) y' + a_{0}(x) y = b(x)
$$
(in particular, assuming that the derivatives $y', y'', \ldots, y^{(r)}$ exist), then $y(x)$ is $C^{m+r}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$y$ is $C^r$.

::: pf-proof

Write the equation as
$$
y^{(r)}=b-\bigl(a_{r-1}y^{(r-1)}+\cdots+a_1y'+a_0y\bigr).
$$
The derivatives $y,\ldots,y^{(r-1)}$ are differentiable, hence continuous, and the $a_i$ and $b$ are continuous. So $y^{(r)}$ is continuous.

:::

:::

::: {.pf-step #s2}

If $y$ is $C^{j+r}$ for some $j<m$, then $y$ is $C^{j+1+r}$.

::: pf-proof

Then $y,\ldots,y^{(r-1)}$ are $C^{j+1}$, and the $a_i$ and $b$ are $C^m$, hence $C^{j+1}$. By the displayed equation of step [](#s1){.pf-ref}, $y^{(r)}$ is $C^{j+1}$.

:::

:::

::: pf-qed

By step [](#s1){.pf-ref} and $m$ applications of step [](#s2){.pf-ref}, $y$ is $C^{m+r}$.

:::

:::

:::
