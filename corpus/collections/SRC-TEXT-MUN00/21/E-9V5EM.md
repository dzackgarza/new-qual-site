---
schema: qual/card@1
id: E-9V5EM
kind: problem
title: Powers converge pointwise but not uniformly on $[0,1]$
classification:
  areas:
  - topology
  topics:
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Define $f_n: [0,1] \to \mathbb{R}$ by the equation $f_n(x) = x^n$.
Show that the sequence $(f_n(x))$ converges for each $x \in [0,1]$, but that the sequence $(f_n)$ does not converge uniformly.
:::

::: {.solution}
<1>1. $f_n\to f$ pointwise, where $f(x)=0$ for $0\le x<1$ and $f(1)=1$.

::: {.proof}
For $0\le x<1$, $x^n\to0$; and $f_n(1)=1$ for every $n$.
:::

<1>2. $(f_n)$ does not converge uniformly.

::: {.proof}
Uniform convergence would be to the pointwise limit $f$.
For each $n$, the point $x_n=2^{-1/n}\in[0,1)$ has $\abs{f_n(x_n)-f(x_n)}=\frac12$, so $\sup_{[0,1]}\abs{f_n-f}\ge\frac12$ for every $n$.
Equivalently, each $f_n$ is continuous and $f$ is not continuous at $1$, while a uniform limit of continuous functions is continuous.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2.
:::
:::
