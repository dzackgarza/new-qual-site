---
schema: qual/card@1
id: P-CASP19B
kind: problem
title: "Continuous function whose square is analytic is analytic"
classification:
  areas:
  - complex-analysis
  topics:
  - Analytic Functions
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $U \subset \CC$ be an open set and $f$ a continuous function on $U$.
Assume $f^2$ is analytic on $U$.
Prove $f$ is analytic on $U$.
:::

::: {.solution}
Let $g \coloneqq f^2$, which is analytic on $U$, and let $Z \coloneqq \{z \in U : f(z) = 0\}$, which is also the zero set of $g$.
It suffices to show that $f$ is complex differentiable at every point of $U$.

::: pf

::: {.pf-step #off-zeros}
$f$ is complex differentiable at every $z_0 \in U \setminus Z$, with $f'(z_0) = g'(z_0)/(2f(z_0))$.

::: pf-proof
For $z \in U$ with $z \neq z_0$ and $f(z) + f(z_0) \neq 0$, the difference of squares gives
$$\frac{f(z) - f(z_0)}{z - z_0} = \frac{g(z) - g(z_0)}{z - z_0} \cdot \frac{1}{f(z) + f(z_0)}.$$
Since $f$ is continuous, $f(z) + f(z_0) \to 2f(z_0) \neq 0$ as $z \to z_0$, so the condition holds near $z_0$ and the right side tends to $g'(z_0)/(2f(z_0))$.
:::

:::

::: pf-step
$f$ is complex differentiable at every $z_0 \in Z$.

::: pf-proof
Choose an open disc $D \subset U$ centred at $z_0$.
If $g \equiv 0$ on $D$, then $f \equiv 0$ on $D$, so $f$ is complex differentiable at $z_0$.
Otherwise $g$ is analytic and not identically zero on the connected set $D$, so its zero $z_0$ is isolated: some punctured disc $D^\ast$ about $z_0$ misses $Z$.
By step [](#off-zeros){.pf-ref}, $f$ is analytic on $D^\ast$, and $f$ is bounded near $z_0$ because it is continuous.
By the Riemann removable singularity theorem, $f|_{D^\ast}$ extends to an analytic function $F$ on $D^\ast \cup \{z_0\}$, and $F(z_0) = \lim_{z \to z_0} f(z) = f(z_0)$ by continuity of $f$.
Hence $f = F$ near $z_0$, and $f$ is complex differentiable at $z_0$.
:::

:::

:::

:::
