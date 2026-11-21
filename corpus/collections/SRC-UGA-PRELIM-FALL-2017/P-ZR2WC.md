---
schema: qual/card@1
id: P-ZR2WC
kind: problem
title: Uniform convergence to zero implies convergence of the integrals
classification:
  areas:
  - prelim
  topics:
  - Uniform Convergence
  - Riemann Integrability
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for a statement that needed no repair. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise; the card now says the argument is its own. The two facts the prose compressed are separated: that uniform convergence to zero is convergence of the sup norm (the supremum exists, is nonnegative, and is at most epsilon from the definition), and the chain of inequalities with the monotonicity of the integral for a constant integrand. No statement repair.
---

::: {.problem}
Let $\{f_n:[0,1]\to\RR\}_{n=1}^{\infty}$ be continuous functions that converge uniformly to $0$.
Show that
$$
\int_0^1 f_n(x)\,dx\longrightarrow0.
$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #supnorm}
$\norm{f_n}_{\infty}=\sup_{x\in[0,1]}\abs{f_n(x)}\to0$.

::: pf-proof
$f_n\to0$ uniformly means that for every $\varepsilon>0$ there is $N$ with $\abs{f_n(x)-0}<\varepsilon$ for all $x\in[0,1]$ and all $n\ge N$. So for $n\ge N$ the set $\{\abs{f_n(x)}:x\in[0,1]\}$ is nonempty, bounded above by $\varepsilon$, and its supremum is at most $\varepsilon$; as $\abs{f_n(x)}\ge0$ the supremum is a nonnegative real. Hence $\norm{f_n}_\infty\le\varepsilon$ for $n\ge N$, which is convergence of the real sequence $\norm{f_n}_\infty$ to $0$.
:::

:::

::: {.pf-step #estimate}
For every $n$, $\abs{\int_0^1f_n(x)\,dx}\le\norm{f_n}_\infty$.

::: pf-proof
Each $f_n$ is continuous on $[0,1]$, hence Riemann integrable there, and so is $\abs{f_n}$. By the triangle inequality for integrals, $\abs{\int_0^1f_n}\le\int_0^1\abs{f_n}$; and $\abs{f_n(x)}\le\norm{f_n}_\infty$ for every $x$, so $\int_0^1\abs{f_n}\le\int_0^1\norm{f_n}_\infty\,dx=\norm{f_n}_\infty$ because the integral is monotone and $\int_0^1 1\,dx=1$.
:::

:::

::: {.pf-step}
$\int_0^1f_n(x)\,dx\to0$.

::: pf-proof
By step [](#estimate){.pf-ref}, $0\le\abs{\int_0^1f_n}\le\norm{f_n}_\infty$ for every $n$, and $\norm{f_n}_\infty\to0$ by step [](#supnorm){.pf-ref}. So the real sequence $\abs{\int_0^1f_n}$ converges to $0$, hence so does $\int_0^1f_n$.
:::

:::

:::
:::
