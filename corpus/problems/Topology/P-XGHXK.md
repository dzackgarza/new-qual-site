---
schema: qual/card@1
id: P-XGHXK
kind: problem
title: A non-surjective map into $S^n$ is nullhomotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $f: X \to S^n$ be a continuous map that is not surjective.
Prove that $f$ is nullhomotopic.
:::

::: {.solution}
Since $f$ is not surjective, choose $p \in S^n \setminus f(X)$, and let $s_0 = -p$.

::: pf

::: {.pf-step #nonzero}
For all $x \in X$ and $t \in [0, 1]$, $(1 - t)f(x) + t s_0 \neq 0$ in $\RR^{n+1}$.

::: pf-proof
Suppose $(1 - t)f(x) + t s_0 = 0$.
Taking norms, with $\norm{f(x)} = \norm{s_0} = 1$, gives $1 - t = t$, so $t = 1/2$ and $f(x) = -s_0 = p$, contradicting $p \notin f(X)$.
:::

:::

::: pf-step
The map
$$
H(x, t) = \frac{(1 - t)f(x) + t s_0}{\norm{(1 - t)f(x) + t s_0}}
$$
is a homotopy $X \times [0,1] \to S^n$ from $f$ to the constant map with value $s_0$, so $f$ is nullhomotopic.

::: pf-proof
By step [](#nonzero){.pf-ref} the denominator never vanishes, so $H$ is a continuous map into $S^n$.
Since $\norm{f(x)} = \norm{s_0} = 1$, we have $H(x,0) = f(x)$ and $H(x,1) = s_0$.
:::

:::

:::

:::
