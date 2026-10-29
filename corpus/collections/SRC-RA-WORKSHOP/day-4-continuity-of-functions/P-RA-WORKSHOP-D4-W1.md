---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-W1
kind: problem
title: Uniform continuity and a continuous non-uniformly-continuous example
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
State the definition of uniform continuity.
Give an example of a function $f:(0,1)\to\RR$ which is continuous but not uniformly continuous.
:::

::: {.solution}
A function $f:D\to\RR$ on a set $D\subseteq\RR$ is uniformly continuous if for every $\varepsilon>0$ there exists $\delta>0$ such that, for every $x,y\in D$,
$$
\abs{x-y}<\delta\quad\Longrightarrow\quad \abs{f(x)-f(y)}<\varepsilon.
$$
The same $\delta$ depends only on $\varepsilon$, not on the points $x,y$.

::: pf

::: pf-step

The function $f:(0,1)\to\RR$ defined by $f(x)=1/x$ is continuous.

::: pf-proof

The reciprocal function is continuous at every nonzero real number, so its restriction to $(0,1)$ is continuous.

:::

:::

::: pf-step

The continuous function $\boxed{f(x)=1/x}$ on $(0,1)$ is not uniformly continuous.

::: pf-proof

Suppose it were uniformly continuous. Apply the definition with $\varepsilon=1$ to obtain $\delta>0$. Choose an integer $n\geq2$ with $1/(2n)<\delta$, and put $x=1/n$ and $y=1/(2n)$. Then $x,y\in(0,1)$ and $\abs{x-y}=1/(2n)<\delta$, while
$$
\abs{f(x)-f(y)}=\abs{n-2n}=n\geq2,
$$
contradicting the required inequality $\abs{f(x)-f(y)}<1$.

:::

:::

:::

:::
