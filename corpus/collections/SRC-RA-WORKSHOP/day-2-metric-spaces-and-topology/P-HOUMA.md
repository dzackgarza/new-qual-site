---
schema: qual/card@1
id: P-HOUMA
kind: problem
title: $\{x:d(x,x_0)=r\}$ is nonempty in an unbounded connected metric space
classification:
  areas:
  - real-analysis
  topics:
  - Metric Spaces
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $(X,d)$ be an unbounded and connected metric space.
Prove that for each $x_0 \in X$ and each $r \geq 0$, the set $\{x \in X \, \colon \,  d(x,x_0) = r\}$ is nonempty.
:::
::: {.solution}

::: pf

::: pf-step

For $x_0 \in X$, the map $d_{x_0} : X \to [0, \infty)$, $x \mapsto d(x, x_0)$, is continuous.

::: pf-proof

The triangle inequality gives $\abs{d(x, x_0) - d(y, x_0)} \le d(x, y)$.

:::

:::

::: {.pf-step #s2}

$d_{x_0}$ is unbounded: for every $M$ there is $x \in X$ with $d(x, x_0) > M$.

::: pf-proof

$X$ is unbounded, so no ball $B(x_0, M)$ contains all of $X$.

:::

:::

::: {.pf-step #s3}

$d_{x_0}(X)$ is an interval containing $0$: if $u, v \in d_{x_0}(X)$ with $u \le w \le v$, then $w \in d_{x_0}(X)$.

::: pf-proof

$d_{x_0}(X)$ is the continuous image of the connected space $X$, hence connected; the connected subsets of $\RR$ are exactly the intervals; $0 = d(x_0, x_0) \in d_{x_0}(X)$.

:::

:::

::: {.pf-step #s4}

$r \in d_{x_0}(X)$ for every $r \ge 0$.

::: pf-proof

$0 \in d_{x_0}(X)$ (step [](#s3){.pf-ref}) and $d_{x_0}$ is unbounded (step [](#s2){.pf-ref}), so the interval $d_{x_0}(X) \supseteq [0, \infty)$; in particular $r$ lies in the image.

:::

:::

::: pf-qed

By step [](#s4){.pf-ref}, every $r\geq 0$ has a preimage under $d_{x_0}$, so $\{x \in X : d(x, x_0) = r\} = \inverseof{d_{x_0}}(r) \neq \varnothing$.

:::

:::

:::
