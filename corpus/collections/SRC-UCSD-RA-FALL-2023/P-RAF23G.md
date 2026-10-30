---
schema: qual/card@1
id: P-RAF23G
kind: problem
title: "Ratios of successive moments $\\int_X \\abs{f}^n$ converge to the $L^\\infty$ norm"
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
  note: Checked against Problem 7 of the official UCSD Fall 2023 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(X, \mu)$ be a nonempty measure space with $\mu(X) < \infty$, $f \in L^\infty(\mu)$ and $\norm{f}_\infty > 0$.
Define $\alpha_n := \int_X \abs{f}^n$ for $n = 1, 2, 3, \ldots$.
Prove that
$$
\lim_{n \to \infty} \frac{\alpha_{n+1}}{\alpha_n} = \norm{f}_\infty.
$$
:::

::: {.solution}

Write $M\coloneqq\norm{f}_\infty>0$.

::: pf

::: {.pf-step #upper}

$\alpha_n>0$ and $\alpha_{n+1}/\alpha_n\le M$ for every $n$.

::: pf-proof

Since $M>0$, the set $\{\abs{f}>0\}$ has positive measure, so $\alpha_n>0$.
Since $\abs{f}\le M$ almost everywhere, $\alpha_{n+1}=\int\abs{f}^{n+1}\,d\mu\le M\int\abs{f}^n\,d\mu=M\alpha_n$.

:::

:::

::: {.pf-step #average}

The measure $d\nu_n\coloneqq\abs{f}^n\alpha_n^{-1}\,d\mu$ is a probability measure and $\alpha_{n+1}/\alpha_n=\int\abs{f}\,d\nu_n$.

::: pf-proof

Both statements follow from the definitions of $\nu_n$ and $\alpha_n$, since $0<\alpha_n<\infty$ by step [](#upper){.pf-ref} and $\mu(X)<\infty$.

:::

:::

::: {.pf-step #concentrate}

For $0<2\varepsilon<M$ and $B_\varepsilon\coloneqq\{\abs{f}\le M-2\varepsilon\}$, $\nu_n(B_\varepsilon)\to0$ as $n\to\infty$.

::: pf-proof

By the definition of the essential supremum, $A_\varepsilon\coloneqq\{\abs{f}>M-\varepsilon\}$ has positive measure, so $\alpha_n\ge\int_{A_\varepsilon}\abs{f}^n\,d\mu\ge(M-\varepsilon)^n\mu(A_\varepsilon)$.
Hence
$$
\nu_n(B_\varepsilon)=\frac{1}{\alpha_n}\int_{B_\varepsilon}\abs{f}^n\,d\mu\le\frac{\mu(X)}{\mu(A_\varepsilon)}\left(\frac{M-2\varepsilon}{M-\varepsilon}\right)^n\convergesto{n\to\infty}0.
$$

:::

:::

::: pf-step

$\boxed{\lim_{n\to\infty}\alpha_{n+1}/\alpha_n=\norm{f}_\infty}$.

::: pf-proof

Fix $\varepsilon$ with $0<2\varepsilon<M$.
Since $\abs{f}>M-2\varepsilon$ off $B_\varepsilon$, step [](#average){.pf-ref} gives $\alpha_{n+1}/\alpha_n\ge(M-2\varepsilon)\,\nu_n(X\setminus B_\varepsilon)$, and by step [](#concentrate){.pf-ref} the right side tends to $M-2\varepsilon$.
So $\liminf_n\alpha_{n+1}/\alpha_n\ge M-2\varepsilon$ for every such $\varepsilon$, and step [](#upper){.pf-ref} gives $\limsup_n\alpha_{n+1}/\alpha_n\le M$.

:::

:::

:::

:::
