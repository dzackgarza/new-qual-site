---
schema: qual/card@1
id: P-JHUMAY11ANE
kind: problem
title: "The running maximum of a bounded C1 sequence converges uniformly"
classification:
  areas:
  - real-analysis
  topics:
  - Convergence Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the JHU Analysis Qualifying Exam, May 2011, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f_n\in C^1([0,1])$ satisfy
$$
f_n(t)\le5,
\qquad
\abs{f_n'(t)}\le1
$$
for all $n,t$. Define
$$
g_n(t)=\max\{f_1(t),\ldots,f_n(t)\}.
$$
Prove that $(g_n)$ converges uniformly on $[0,1]$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the Lipschitz stability of the maximum, the limit function and Dini's theorem as separate steps.

Suppose $f_{n}\in C^{1}([0,1])$ with $f_{n}\le5$ and $\abs{f_{n}'}\le1$, and $g_{n}=\max\theset{f_{1},\dots,f_{n}}$.

::: pf

::: {.pf-step #lipschitz}
Each $f_{n}$ and each $g_{n}$ is $1$-Lipschitz, and $g_{n}$ is continuous.

::: pf-proof
By the mean value theorem $\abs{f_{n}(s)-f_{n}(t)}\le\sup\abs{f_{n}'}\abs{s-t}\le\abs{s-t}$. If $u,v$ are $1$-Lipschitz and $s,t\in[0,1]$, then $\max(u,v)(s)\le\max(u(t)+\abs{s-t},v(t)+\abs{s-t})=\max(u,v)(t)+\abs{s-t}$, and symmetrically, so the maximum is $1$-Lipschitz; induction gives it for $g_{n}$, and a Lipschitz function is continuous.
:::

:::

::: {.pf-step #monotone}
$(g_{n}(t))$ is nondecreasing and bounded above by $5$ for each $t$, so $g(t)=\lim_{n}g_{n}(t)=\sup_{n}f_{n}(t)$ exists and is finite; also $\abs{g(s)-g(t)}\le\abs{s-t}$.

::: pf-proof
$g_{n}\le g_{n+1}$ pointwise by definition of the maximum, and $g_{n}(t)\le5$ for all $n$; a nondecreasing sequence bounded above converges. Moreover $g(t)\ge g_{1}(t)>-\infty$, so $g$ is real valued. Letting $n\to\infty$ in $\abs{g_{n}(s)-g_{n}(t)}\le\abs{s-t}$ of step [](#lipschitz){.pf-ref} gives the same inequality for $g$, which is therefore continuous.
:::

:::

::: {.pf-step #dini}
$(g_{n})$ converges to $g$ uniformly on $[0,1]$.

::: pf-proof
$(g_{n})$ is a sequence of continuous functions on the compact space $[0,1]$, nondecreasing pointwise, with continuous limit $g$; Dini's theorem then gives uniform convergence.
:::

:::

::: {.pf-qed}
The limit $g$ exists and $(g_{n})$ converges to it uniformly on $[0,1]$ by steps [](#monotone){.pf-ref} and [](#dini){.pf-ref}.
:::

:::

:::
