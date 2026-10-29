---
schema: qual/card@1
id: P-QXYTV
kind: problem
title: $\lim_{p\to\infty}\bigl(\int_a^b f^p\bigr)^{1/p}=\sup f$ for continuous $f\ge
  0$ on $[a,b]$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - L∞
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Suppose that $f:[a,b]\to\RR$ is continuous, $f\geq 0$ on $[a,b]$, and put $M=\sup\{f(x):x\in[a,b]\}$.
Prove that $$\lim_{p\to\infty}\left(\int_a^b f(x)^p\,dx\right)^{1/p}=M.$$
:::

::: {.solution}

Assume $a<b$ and write $I_p\coloneqq\left(\int_a^b f^p\right)^{1/p}$. If $M=0$, then $f\equiv0$ and $I_p=0$ for every $p$, so assume $M>0$.

::: pf

::: {.pf-step #upper}

$\limsup_{p\to\infty} I_p \le M$.

::: pf-proof

Since $0 \le f \le M$ on $[a,b]$, we have $\int_a^b f^p \le M^p (b-a)$, so $I_p\le M(b-a)^{1/p}$. Since $(b-a)^{1/p} \to 1$, the bound follows.

:::

:::

::: {.pf-step #lower}

For each $0 < \varepsilon < M$, $\liminf_{p\to\infty} I_p \ge M - \varepsilon$.

::: pf-proof

Since $f$ is continuous on the compact interval $[a,b]$, it attains $M$ at some $x_0 \in [a,b]$.
The set $\{x\in[a,b] : f(x) > M - \varepsilon\}$ is relatively open in $[a,b]$ and contains $x_0$, so it contains an interval of length $\delta > 0$.
Hence
$$
\int_a^b f^p \ge (M-\varepsilon)^p \delta, \qquad \text{so} \qquad I_p \ge (M-\varepsilon)\,\delta^{1/p} \to M - \varepsilon .
$$

:::

:::

::: pf-step

$\lim_{p\to\infty} I_p = M$.

::: pf-proof

Step [](#lower){.pf-ref}, with $\varepsilon \to 0$, gives $\liminf_{p\to\infty} I_p\ge M$, and step [](#upper){.pf-ref} gives $\limsup_{p\to\infty} I_p\le M$.

:::

:::

:::

:::
