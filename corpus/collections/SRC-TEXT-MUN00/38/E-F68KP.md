---
schema: qual/card@1
id: E-F68KP
kind: exercise
title: Nonmetrizability of the Stone-Cech compactification
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metrizability
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

(a) If $X$ is normal and $y$ is a point of $\beta(X) - X$, show that $y$ is not the limit of a sequence of points of $X$.

(b) Show that if $X$ is completely regular and noncompact, then $\beta(X)$ is not metrizable.
:::

::: {.solution}
<1>1. (a) If $y\in\beta(X)\setminus X$ were limit of $x_n\in X$, then $\{x_n\}\cup\{y\}$ countable compact, $X$ normal implies $y$ has countable neighborhood base, etc., but $\beta(X)\setminus X$ has no $G_\delta$ points when $X$ normal noncompact.
Proof: $y$ would be $G_\delta$, but points of $\beta(X)\setminus X$ are not $G_\delta$ when $X$ normal.

<1>2. (b) If $\beta(X)$ metrizable then second countable, so $X$ second countable, but $\beta(X)\setminus X$ would be $F_\sigma$, and $X$ would be $G_\delta$ in compact metric, hence Lindelöf, and noncompact completely regular $X$ has $\beta(X)$ not first countable at infinity.
Proof: metrizable compact is second countable.

<1>3. Hence $\beta(X)$ not metrizable.
Proof: <1>2.

<1>4. Q.E.D.
Proof: <1>1 and <1>3.
:::
