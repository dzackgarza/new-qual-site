---
schema: qual/card@1
id: P-Y3TRT
kind: problem
title: A continuous solution of $f(x)=\int_0^x g(t,f(t))\,dt$
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Functions
  - Arzelà-Ascoli
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let g : $[0, 1] \times [0, 1] \to [0, 1]$ be a continuous function and let $\{f_n\}$ be a sequence of functions such that

$$f_n(x)=\begin{cases}{0,   0\leq x\leq 1/n},\\{\int_0^{x-\frac1n} g(t,f_n(t))dt, 1/n\leq x \leq 1.}\end{cases}$$

With the help of the Arzela-Ascoli theorem or otherwise, show that there exists a continuous function $f : [0, 1] \to \mathbb{R}$ such that

$f(x) = \int_0^x g(t, f(t))dt$

for all $x \in [0, 1]$.

> Hint: first show that $|f_n(x_1) - f_n(x_2)| \leq |x_1 - x_2|$.
:::

::: {.solution}
::: pf

::: {.pf-step #fn-well-defined-bounded}
The sequence $\{f_n\}$ is well defined, and $0 \leq f_n(x) \leq 1$ for all $n$ and all $x \in [0,1]$.

::: pf-proof

::: {.pf-step #fn-well-defined-continuous}
Each $f_n$ is well defined and continuous.

::: pf-proof
On $[0, 1/n]$, $f_n \equiv 0$.
On $[j/n, (j+1)/n]$ the integrand $g(t, f_n(t))$ is evaluated only at $t \leq x - 1/n \leq j/n$, that is, at values of $f_n$ already defined on $[0, j/n]$. So the recursion defines $f_n$ piece by piece; each piece is continuous as an integral of a continuous function, and consecutive pieces agree at the common endpoint.
:::

:::

::: {.pf-step #fn-bounded-by-x-minus-1n}
$0 \leq f_n(x) \leq x - \frac1n \leq 1$ for $x \geq \frac1n$; hence $0 \leq f_n \leq 1$ everywhere.

::: pf-proof
$g \geq 0$ gives $f_n \geq 0$; $g \leq 1$ gives $f_n(x) = \int_0^{x - 1/n} g \leq \int_0^{x - 1/n} 1 = x - \frac1n \leq 1$.
:::

:::


::: pf-qed
Steps [](#fn-well-defined-continuous){.pf-ref} and [](#fn-bounded-by-x-minus-1n){.pf-ref}.
:::

:::

:::

::: {.pf-step #fn-lipschitz}
Each $f_n$ is $1$-Lipschitz: $|f_n(x_1) - f_n(x_2)| \leq |x_1 - x_2|$.

::: pf-proof

::: {.pf-step #lipschitz-case-both-above}
For $1/n \leq x_1 \leq x_2$: $|f_n(x_2) - f_n(x_1)| = \left|\int_{x_1 - 1/n}^{x_2 - 1/n} g(t, f_n(t)) \, dt\right| \leq x_2 - x_1$.

::: pf-proof
$|g| \leq 1$, and the interval of integration has length $x_2 - x_1$.
:::

:::

::: {.pf-step #lipschitz-case-straddle}
For $x_1 < 1/n \leq x_2$: $|f_n(x_2) - f_n(x_1)| = |f_n(x_2)| \leq x_2 - \frac1n \leq x_2 - x_1$.

::: pf-proof
$f_n(x_1) = 0$ by definition on $[0, 1/n]$, and $|f_n(x_2)| \leq x_2 - 1/n$ by step [](#fn-well-defined-bounded){.pf-ref}.
:::

:::

::: {.pf-step #lipschitz-case-both-below}
For $x_1 \leq x_2 < 1/n$, both values are $0$.
:::


::: pf-qed
Taking $x_1 \leq x_2$, steps [](#lipschitz-case-both-above){.pf-ref}, [](#lipschitz-case-straddle){.pf-ref}, and [](#lipschitz-case-both-below){.pf-ref} cover the three possible positions of $x_1, x_2$ relative to $1/n$.
:::

:::

:::

::: {.pf-step #ascoli-subsequence}
Arzelà–Ascoli gives a subsequence $f_{n_k} \to f$ uniformly on $[0,1]$, with $f$ continuous.

::: pf-proof
$\{f_n\}$ is uniformly bounded by $1$ (step [](#fn-well-defined-bounded){.pf-ref}) and equicontinuous (step [](#fn-lipschitz){.pf-ref}: a common Lipschitz constant), so Arzelà–Ascoli applies on the compact interval $[0,1]$.
:::

:::

::: {.pf-step #limit-satisfies-equation}
The limit $f$ satisfies $f(x) = \int_0^x g(t, f(t)) \, dt$ for every $x$.

::: pf-proof

::: {.pf-step #g-converges-uniformly}
$g(t, f_{n_k}(t)) \to g(t, f(t))$ uniformly in $t$.

::: pf-proof
$g$ is uniformly continuous on the compact square $[0,1]^2$, and $f_{n_k} \to f$ uniformly (step [](#ascoli-subsequence){.pf-ref}).
:::

:::

::: {.pf-step #integral-converges}
For each fixed $x \in (0,1]$: $\int_0^{x - 1/n_k} g(t, f_{n_k}(t)) \, dt \to \int_0^x g(t, f(t)) \, dt$.

::: pf-proof
For $k$ large, $1/n_k \leq x$, and then $\left|\int_0^{x - 1/n_k} g(t, f_{n_k}(t))\,dt - \int_0^x g(t, f(t))\,dt\right| \leq \int_0^{x - 1/n_k} |g(t, f_{n_k}(t)) - g(t, f(t))|\,dt + \int_{x - 1/n_k}^x |g(t, f(t))|\,dt \leq \sup_t |g(t, f_{n_k}(t)) - g(t, f(t))| + \frac1{n_k}$, which tends to $0$ by step [](#g-converges-uniformly){.pf-ref} and the width $\frac1{n_k} \to 0$.
:::

:::

::: {.pf-step #base-case-x-zero}
For $x = 0$: $f(0) = 0 = \int_0^0 g(t, f(t))\,dt$.

::: pf-proof
$f_{n_k}(0) = 0$ by definition, and $f(0) = \lim_k f_{n_k}(0)$ by step [](#ascoli-subsequence){.pf-ref}.
:::

:::

::: pf-qed
For $x > 0$ and $k$ large, $f_{n_k}(x) = \int_0^{x - 1/n_k} g(t, f_{n_k}(t))\,dt$ converges to $f(x)$ by uniform convergence and to $\int_0^x g(t, f(t))\,dt$ by step [](#integral-converges){.pf-ref}, so the two limits agree. Step [](#base-case-x-zero){.pf-ref} covers $x = 0$.
:::

:::

:::

::: pf-qed
Step [](#ascoli-subsequence){.pf-ref} gives continuity of $f$, and step [](#limit-satisfies-equation){.pf-ref} gives the integral equation.
:::

:::
:::
