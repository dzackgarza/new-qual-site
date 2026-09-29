---
schema: qual/card@1
id: P-ZS4IH
kind: problem
title: A bound on the difference quotient of a holomorphic function on a half-radius
  disc
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $\bar{B}(a, r)$ denote the closed disk of radius $r > 0$ centered at $a \in \mathbb{C}$. Let $f$ be holomorphic on an open neighborhood containing $\bar{B}(a, r)$, and define
$$
M = \sup_{z \in \bar{B}(a, r)} |f(z)|.
$$
Prove that for all $z \in \bar{B}(a, r/2)$ with $z \ne a$:
$$
\frac{|f(z) - f(a)|}{|z - a|} \le \frac{2M}{r}.
$$
:::

::: {.solution}
**Goal:** Let $\bar B(a, r)$ be the closed disk of radius $r$ about $a$, and let $f$ be holomorphic on an open set containing it, with $M := \sup_{z \in \bar B(a,r)} \abs{f(z)}$. Prove that for $z \in \bar B\qty{a, \frac{r}{2}}$, $z \neq a$:
$$\frac{\abs{f(z) - f(a)}}{\abs{z - a}} \leq \frac{2M}{r}.$$

::: pf

::: {.pf-step #s1}
Reduce to the unit disk by scaling: define $g(w) := f(a + rw)$ for $\abs w \leq 1$.

::: pf-proof
$g$ is holomorphic on a neighborhood of the closed unit disk, and $\abs{g(w)} \leq M$ there.
:::

:::

::: {.pf-step #s2}
Define $h(w) := g(w) - g(0)$; then $h(0) = 0$ and $\abs{h(w)} \leq 2M$ on $\abs w \leq 1$.

::: pf-proof
$\abs{h(w)} = \abs{g(w) - g(0)} \leq \abs{g(w)} + \abs{g(0)} \leq 2M$.
:::

:::

::: pf-step
Apply Schwarz's lemma to $\frac{h}{2M}$.

::: pf-proof

::: pf-step
$\frac{h}{2M}$ is holomorphic on $\DD$ and maps $\DD$ into $\overline{\DD}$, with value $0$ at $w = 0$.

::: pf-proof
Step [](#s2){.pf-ref}; if $M = 0$ then $f \equiv 0$ and $\abs{h(w)} \leq 0$ holds, so assume $M > 0$.
:::

:::

::: {.pf-step #s3-2}
$\abs{h(w)} \leq 2M \abs w$ for $\abs w < 1$.

::: pf-proof
Schwarz's lemma applied to $h/2M$.
:::

:::

:::

:::

::: pf-step
Translate back to $z$.

::: pf-proof

::: pf-step
For $z \in \bar B(a, r/2)$, set $w := (z - a)/r$; then $\abs w \leq 1/2 < 1$.

::: pf-proof
$\abs{z - a} \leq r/2$.
:::

:::

::: {.pf-step #s4-2}
$\abs{f(z) - f(a)} = \abs{h(w)} \leq 2M\abs w = \frac{2M}{r}\abs{z - a}$.

::: pf-proof
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3-2){.pf-ref}, with $f(z) - f(a) = g(w) - g(0) = h(w)$.
:::

:::

:::

:::

::: pf-qed
Step [](#s4-2){.pf-ref} is exactly the claimed inequality (both sides well-defined since $z \neq a$).
:::

:::
:::
