---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-W3
kind: problem
title: Uniform limits of continuous functions are continuous
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Continuity
  - Convergence of Functions
relations:
- kind: uses
  target: T-ERNLN
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Assume that $\theset{f_n}$ is a sequence of continuous functions $f_n\colon E\subseteq\RR\to\RR$ which converges uniformly to $f$.
Prove directly from the definitions that $f$ is continuous on $E$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $\varepsilon>0$ there exists $N\geq1$ such that
$$
\abs{f_N(x)-f(x)}<\varepsilon/3\qquad(x\in E).
$$

::: pf-proof

This is the definition of uniform convergence applied with tolerance $\varepsilon/3$.

:::

:::

::: {.pf-step #s2}

For $x_0\in E$ and $\varepsilon,N$ as in step [](#s1){.pf-ref}, there exists $\delta>0$ such that
$$
\abs{f_N(x)-f_N(x_0)}<\varepsilon/3
\quad\text{whenever }x\in E,\ \abs{x-x_0}<\delta.
$$

::: pf-proof

The function $f_N$ is continuous at $x_0$ by hypothesis; apply its $\varepsilon$-$\delta$ condition with tolerance $\varepsilon/3$.

:::

:::

::: {.pf-step #s3}

The function $f$ is continuous at every $x_0\in E$.

::: pf-proof

Fix $x_0\in E$ and $\varepsilon>0$, and choose $N$ and $\delta$ by steps [](#s1){.pf-ref} and [](#s2){.pf-ref}. Whenever $x\in E$ and $\abs{x-x_0}<\delta$, the triangle inequality gives
$$
\abs{f(x)-f(x_0)}
\leq \abs{f(x)-f_N(x)}+\abs{f_N(x)-f_N(x_0)}+\abs{f_N(x_0)-f(x_0)}
<\varepsilon.
$$

:::

:::

::: pf-qed

By step [](#s3){.pf-ref}, $f$ is continuous on $E$.

:::

:::

:::
