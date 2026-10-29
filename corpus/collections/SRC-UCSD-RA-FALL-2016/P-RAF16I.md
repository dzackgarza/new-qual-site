---
schema: qual/card@1
id: P-RAF16I
kind: problem
title: 'Ratios of $L^k$ norms converge to the $L^\infty$ norm'
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 9 of the official UCSD Fall 2016 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) < \infty$.
Let $f \in L^\infty(\mu)$ with $\|f\|_\infty > 0$.
Define
$$
\alpha_k = \int_X |f|^k\,d\mu \qquad \text{for } k = 1, 2, \ldots.
$$
Prove that
$$
\lim_{k \to \infty} \frac{\alpha_{k+1}}{\alpha_k} = \|f\|_\infty.
$$
:::

::: {.solution}

Let $M \coloneqq \norm{f}_\infty > 0$ and $r_k \coloneqq \alpha_{k+1}/\alpha_k$. Since $M > 0$, the set $\theset{\abs{f} > 0}$ has positive measure, so $\alpha_k > 0$ for every $k$.

::: pf

::: {.pf-step #monotone}

$(r_k)$ is increasing and bounded above by $M$, so $r_k \to L$ for some $L$ with $0 < r_1 \le L \le M$.

::: pf-proof

By the Cauchy--Schwarz inequality, $\alpha_{k+1}^2 = \left(\int \abs{f}^{k/2}\abs{f}^{(k+2)/2}\,d\mu\right)^2 \le \alpha_k\alpha_{k+2}$, which is $r_k \le r_{k+1}$. Since $\abs{f} \le M$ almost everywhere, $\alpha_{k+1} \le M\alpha_k$, which is $r_k \le M$.

:::

:::

::: {.pf-step #root}

$\alpha_k^{1/k} \to M$.

::: pf-proof

First, $\alpha_k^{1/k} \le M\mu(X)^{1/k}$, so $\limsup_k \alpha_k^{1/k} \le M$. For $0 < a < M$, the set $E_a \coloneqq \theset{\abs{f} > a}$ has positive measure by the definition of the essential supremum, so $\alpha_k \ge a^k\mu(E_a)$ and $\liminf_k \alpha_k^{1/k} \ge a$. Let $a \uparrow M$.

:::

:::

::: pf-step

$\displaystyle\lim_{k \to \infty} \frac{\alpha_{k+1}}{\alpha_k} = L = \boxed{\norm{f}_\infty}$.

::: pf-proof

Write $\alpha_k^{1/k} = \alpha_1^{1/k}\left(\prod_{j=1}^{k-1}r_j\right)^{1/k}$. By step [](#monotone){.pf-ref}, $\log r_j \to \log L$, so the Cesàro means of $(\log r_j)$ tend to $\log L$, and with $\alpha_1^{1/k} \to 1$ this gives $\alpha_k^{1/k} \to L$. By step [](#root){.pf-ref}, $L = M$.

:::

:::

:::

:::
