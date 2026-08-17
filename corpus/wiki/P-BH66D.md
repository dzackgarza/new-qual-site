---
schema: qual/card@1
id: P-BH66D
kind: problem
title: Equivalence of $\varepsilon$-$\delta$ and sequential continuity at a point
classification:
  areas:
  - real-analysis
  topics:
  - continuity
  - metric-spaces
relations: []
review: draft
solved: true
---

Let $(X, d)$ and $(Y, \rho)$ be metric spaces, $f: X\to Y$, and $x_0 \in X$.

Prove that the following statements are equivalent:

1. For every $\varepsilon > 0 \quad \exists \delta > 0$ such that $\rho( f(x), f(x_0)  ) < \varepsilon$ whenever $d(x, x_0) < \delta$.

2. The sequence $\theset{f(x_n)}_{n=1}^\infty \to f(x_0)$ for every sequence $\theset{x_n} \to x_0$ in $X$.

::: {.concept}
\envlist

- What it means for a sequence to converge.

- Trading $N$s for $\delta$s.
:::

::: {.solution}
\envlist

::: {.proof title="1 $\implies$ 2"}
\envlist

- Let $\theset{x_n} \converges{n\to\infty}\to x_0$ be arbitrary; we want to show $\theset{f(x_n)}\converges{n\to\infty}\to f(x_0)$.

  - We thus want to show that for every $\eps>0$, there exists an $N(\eps)$ such that \[n\geq N(\eps) \implies \rho(f(x_n),  f(x_0)) < \eps.\]

- Let $\eps>0$ be arbitrary, then by (1) choose $\delta$ such that $\rho(f(x), f(x_0)) < \eps$ when $d(x, x_0) < \delta$.

- Since $x_n\to x$, there is some $N$ such that $n\geq N \implies d(x_n, x_0) < \delta$

- Then for $n\geq N$, $d(x_n, x_0) < \delta$ and thus $\rho(f(x_n), f(x_0)) < \eps$, so $f(x_n)\to f(x_0)$ by definition.
:::

::: {.proof title="$2\implies 1$"}

> The direct implication is not a good idea here, since you need a handle on *all* $x$ in a neighborhood of $x_0$, not just a specific sequence.

- By contrapositive, show that $\not 1\implies \not 2$.

- Need to show: if $f$ is not $\eps\dash\delta$ continuous at $x_0$, then there exists a sequence $x_n\to x_0$ where $f(x_n)\not\to f(x_0)$.

- Negating $1$, we have that there exists an $\eps>0$ such that for all $\delta$, there exists an $x$ with $d(x, x_0) < \delta$ but $\rho(f(x), f(x_0))>\eps$

- So take a sequence of deltas $\delta_n = {1\over n}$, apply this to produce a sequence $x_n$ with $d(x_n, x_0) < \delta_n \da {1\over n} \too 0$ and $\rho(f(x_n), f(x_0)) > \eps$ for all $n$.

- This yields a sequence $x_n \to x_0$ where $f(x_n) \not\to f(x_0)$.
:::
:::
