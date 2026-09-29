---
schema: qual/card@1
id: P-TOPF22E
kind: problem
title: "Long exact sequence for homology with Z, R, and R/Z coefficients; homology of RP^infinity with T coefficients"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Coefficients
  - Exact Sequences
  - Projective Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Consider the circle in the form of the abelian group $T = \mathbb{R}/\mathbb{Z}$.
Show that there is a long exact sequence relating homology with coefficients in $\mathbb{Z}$, $\mathbb{R}$ and $T$ and use it to compute $H_*(\mathbb{RP}^\infty; T)$.
:::

::: {.solution}
**Goal.** Derive the long exact sequence relating $H_*(\cdot;\ZZ)$, $H_*(\cdot;\RR)$, $H_*(\cdot;T)$, and compute $H_*(\RP^\infty; T)$.

::: pf

::: pf-step

The short exact sequence $0 \to \ZZ \to \RR \to T \to 0$ of coefficient groups.

::: pf-proof

$\ZZ \hookrightarrow \RR$ and $T = \RR/\ZZ$.

:::

:::

::: pf-step

This induces a long exact sequence in homology:
$$
\cdots \to H_n(X;\ZZ) \to H_n(X;\RR) \to H_n(X;T) \to H_{n-1}(X;\ZZ) \to \cdots
$$

::: pf-proof

the short exact sequence of coefficients induces a long exact sequence in homology (via the universal coefficient theorem / the long exact sequence of the tensor product).

:::

:::

::: pf-step

Compute $H_*(\RP^\infty;\ZZ)$ and $H_*(\RP^\infty;\RR)$.

::: pf-proof

::: pf-step

$H_n(\RP^\infty;\ZZ) = \ZZ$ for $n = 0$, $\ZZ/2$ for $n$ odd, $0$ otherwise.

::: pf-proof

standard homology of $\RP^\infty$.

:::

:::

::: pf-step

$H_n(\RP^\infty;\RR) = \RR$ for $n = 0$, $0$ for $n > 0$.

::: pf-proof

$\RP^\infty$ has no free part in positive degrees (all positive homology is $\ZZ/2$ torsion), so tensoring with $\RR$ kills it.

:::

:::

:::

:::

::: pf-step

Compute $H_*(\RP^\infty; T)$ from the long exact sequence.

::: pf-proof

::: pf-step

For $n \ge 1$ even: $H_n(\RP^\infty;\ZZ) = 0$ and $H_n(\RP^\infty;\RR) = 0$, so $H_n(\RP^\infty;T) \cong H_{n-1}(\RP^\infty;\ZZ) = \ZZ/2$ (for $n$ even, $n-1$ odd).

::: pf-proof

the LES gives $0 \to H_n(\cdot;T) \to H_{n-1}(\cdot;\ZZ) \to H_{n-1}(\cdot;\RR) = 0$, so $H_n(\cdot;T) \cong H_{n-1}(\cdot;\ZZ) = \ZZ/2$.

:::

:::

::: pf-step

For $n \ge 1$ odd: $H_n(\RP^\infty;\ZZ) = \ZZ/2$ and $H_n(\RP^\infty;\RR) = 0$, so the LES gives $0 \to H_n(\cdot;T) \to H_{n-1}(\cdot;\ZZ) = 0$, hence $H_n(\cdot;T) = 0$.

::: pf-proof

$H_{n-1}(\cdot;\ZZ) = 0$ for $n-1$ even, so $H_n(\cdot;T) = 0$.

:::

:::

::: pf-step

$H_0(\RP^\infty;T) = T$.

::: pf-proof

$H_0(X;G) = G$ for path-connected $X$.

:::

:::

:::

:::

::: pf-qed

$H_0(\RP^\infty;T) = T$, $H_n(\RP^\infty;T) = \ZZ/2$ for $n$ even $\ge 2$, and $H_n(\RP^\infty;T) = 0$ for $n$ odd.

:::

:::

:::
