---
schema: qual/card@1
id: P-UMC34
kind: problem
title: Entire functions satisfying $\abs{f(z)}\geq\abs{z}$ are the maps $cz$ with $\abs{c}\geq
  1$
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Removable Singularities
  - Zeros
relations: []
review: draft
---

::: {.problem}
Find all entire functions that satisfy
$$
\abs{f(z)} \geq \abs{z} \quad \forall z\in \CC.
$$
Prove this list is complete.

:::

::: {.concept}
If $f$ is bounded in a punctured neighborhood of an isolated singularity $z_0$, then $z_0$ is removable.
:::

::: {.solution}

::: pf

::: {.pf-step #zeros}

The only possible zero of $f$ is $z = 0$.

::: pf-proof

If $f(z) = 0$, then $\abs{z} \leq \abs{f(z)} = 0$.

:::

:::

::: {.pf-step #g}

The function $g(z) \coloneqq z/f(z)$ on $\CC\setminus\{0\}$ extends to an entire function $\tilde g$ with $\abs{\tilde g} \leq 1$.

::: pf-proof

By step [](#zeros){.pf-ref}, $g$ is holomorphic on $\CC\setminus\{0\}$, and the inequality gives $\abs{g} \leq 1$ there. By Riemann's removable singularity theorem $g$ extends to an entire function $\tilde g$, and $\abs{\tilde g(0)} \leq 1$ by continuity.

:::

:::

::: pf-step

$f(z) = cz$ for a constant $c$ with $\abs{c} \geq 1$.

::: pf-proof

By step [](#g){.pf-ref} and Liouville's theorem, $\tilde g$ is a constant $c_0$ with $\abs{c_0} \leq 1$. Since $g(z) = z/f(z) \neq 0$ for $z \neq 0$, $c_0 \neq 0$. Hence $f(z) = c_0^{-1} z$ for $z \neq 0$, and also at $z = 0$ by continuity, with $c = c_0^{-1}$ satisfying $\abs{c} \geq 1$.

:::

:::

::: pf-step

The entire functions with $\abs{f(z)} \geq \abs{z}$ are exactly $\boxed{f(z) = cz \text{ with } c \in \CC,\ \abs{c} \geq 1}$.

::: pf-proof

Each such $f$ is entire and satisfies $\abs{f(z)} = \abs{c}\abs{z} \geq \abs{z}$; the preceding step shows there are no others.

:::

:::

:::

:::
