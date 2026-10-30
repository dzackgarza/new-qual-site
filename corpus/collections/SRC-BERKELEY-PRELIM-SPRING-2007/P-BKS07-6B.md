---
schema: qual/card@1
id: P-BKS07-6B
kind: problem
title: An integral curve confined to a compact set has a limit at the right endpoint
classification:
  areas: [prelim]
  topics:
  - Calculus
relations: []
review: draft
---

::: {.problem}
Let $U$ be a non-empty open subset of $\RR^{d}$ and let $f \colon U \to \RR^{d}$ be a continuous vector field defined on $U$. Let $K$ be a compact subset of $U$ and let $b > 0$. Suppose $\varphi \colon [0, b) \to K$ is a continuous function satisfying
$$
\varphi(t) = \varphi(0) + \int_{0}^{t} f(\varphi(s))\, ds, \qquad (0 \leq t < b).
$$
Prove that $\lim_{t \to b^{-}} \varphi(t)$ exists, where $t \to b^{-}$ means $t$ approaches $b$ from the left.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $M=\sup_{y\in K}\norm{f(y)}$. Then $M<\infty$ and $\norm{\varphi(t_2)-\varphi(t_1)}\le M\abs{t_2-t_1}$ for $t_1,t_2\in[0,b)$.

::: pf-proof

$f$ is continuous on the compact set $K$, so $M<\infty$. Since $\varphi$ takes values in $K$,
$$
\norm{\varphi(t_2)-\varphi(t_1)}=\Bigl\|\int_{t_1}^{t_2}f(\varphi(s))\,ds\Bigr\|\le M\abs{t_2-t_1}.
$$

:::

:::

::: pf-qed

Let $\varepsilon>0$ and $\delta=\varepsilon/(M+1)$. By step [](#s1){.pf-ref}, $\norm{\varphi(t_2)-\varphi(t_1)}<\varepsilon$ for all $t_1,t_2\in(b-\delta,b)$. This is the Cauchy criterion for the limit as $t\to b^-$, and $\RR^d$ is complete, so $\lim_{t\to b^-}\varphi(t)$ exists.

:::

:::

:::
