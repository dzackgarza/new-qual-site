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
Prove that for each $x_0 \in X$, the set $\{x \in X \, \colon \,  d(x,x_0) = r\}$ is nonempty.
:::
::: {.solution}

::: pf

::: pf-step

Fix $x_0 \in X$ and $r > 0$; the map $d_{x_0} : X \to [0, \infty)$, $x \mapsto d(x, x_0)$, is continuous.

::: pf-proof

the triangle inequality gives $|d(x, x_0) - d(y, x_0)| \le d(x, y)$.

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

: $\{x \in X : d(x, x_0) = r\} = \inverseof{d_{x_0}}(r) \neq \varnothing$ for every $r \ge 0$.

Step [](#s4){.pf-ref} says $r$ has a preimage under $d_{x_0}$, which is exactly a point at distance $r$ from $x_0$.

:::

:::

:::
