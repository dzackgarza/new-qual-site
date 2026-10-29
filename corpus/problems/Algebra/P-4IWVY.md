---
schema: qual/card@1
id: P-4IWVY
kind: problem
title: Irreducible modules over a PID are $R/(p)$ and indecomposable modules are $R/(p^n)$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Semisimplicity
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $R$ be a Principal Ideal Domain (PID).

(1) If $R$ is not a field, prove that the irreducible (simple) $R$-modules are precisely $R/(p)$ where $p\in R$ is irreducible. If $R$ is a field, show that the only simple $R$-module up to isomorphism is $R$.

(2) Prove that the finitely generated indecomposable $R$-modules are precisely $R$ and $R/(p^n)$ where $p\in R$ is irreducible and $n\ge1$.
:::

::: {.solution}

::: pf

::: pf-step
(1) If $R$ is not a field, the simple $R$-modules are exactly the modules $R/(p)$ with $p$ irreducible. If $R$ is a field, every simple $R$-module is isomorphic to $R$.

::: pf-proof

::: {.pf-step #cyclic}
Every simple $R$-module $M$ satisfies $M\cong R/\Ann(m)$ for each $0\ne m\in M$, and $\Ann(m)$ is a maximal ideal.

::: pf-proof
The submodule $Rm$ is nonzero, so simplicity gives $Rm=M$. The map $R\to M$, $r\mapsto rm$, is therefore surjective with kernel $\Ann(m)$, so $M\cong R/\Ann(m)$. The submodules of $R/\Ann(m)$ correspond to the ideals that contain $\Ann(m)$, and $M$ has exactly two submodules, so $\Ann(m)$ is maximal.
:::

:::

::: pf-step
If $R$ is not a field, the simple modules are the $R/(p)$ with $p$ irreducible.

::: pf-proof
Since $R$ is not a field, the ideal $(0)$ is not maximal, so every maximal ideal of the PID $R$ is nonzero and has the form $(p)$ with $p$ irreducible. By step [](#cyclic){.pf-ref}, every simple module is isomorphic to such an $R/(p)$. Conversely, $(p)$ is maximal for irreducible $p$ in a PID, so $R/(p)$ is simple.
:::

:::

::: pf-step
If $R$ is a field, every simple module is isomorphic to $R$.

::: pf-proof
The only maximal ideal of a field is $(0)$, so step [](#cyclic){.pf-ref} gives $M\cong R$. The module $R$ is simple because its only ideals are $0$ and $R$.
:::

:::

:::

:::

::: pf-step
(2) The finitely generated indecomposable $R$-modules are exactly $R$ and the $R/(p^n)$ with $p$ irreducible and $n\ge1$.

::: pf-proof

::: pf-step
A finitely generated indecomposable $R$-module is isomorphic to $R$ or to some $R/(p^n)$.

::: pf-proof
The structure theorem writes every finitely generated $R$-module as
$$
R^r\oplus\bigoplus_i R/(p_i^{n_i}).
$$
An indecomposable module has exactly one nonzero summand in this decomposition.
:::

:::

::: pf-step
$R$ is indecomposable.

::: pf-proof
A decomposition $R=I\oplus J$ into ideals gives $1=e+f$ with $e\in I$, $f\in J$, and $e^2=e$. A domain has only the idempotents $0$ and $1$, so $I=0$ or $J=0$.
:::

:::

::: pf-step
$R/(p^n)$ is indecomposable.

::: pf-proof
The submodules of $R/(p^n)$ are exactly
$$
(p^j)/(p^n),\qquad 0\le j\le n,
$$
which form a chain. Two nonzero submodules therefore have nonzero intersection, so $R/(p^n)$ is not a direct sum of two nonzero submodules.
:::

:::

:::

:::

:::

:::
