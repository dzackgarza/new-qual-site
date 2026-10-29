---
schema: qual/card@1
id: P-LOHM5
kind: problem
title: Groups of order $p^3$ have a normal subgroup of order $p^2$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $p$ be a prime and $\abs{G} = p^3$.

(a) Prove that $G$ has a normal subgroup $N$ of order $p^2$.

(b) Suppose $N = \generators{h}$ is cyclic and classify all possibilities for $G$ if:

(i) $\abs h = p^3$

(ii) $\abs h = p$.
:::

::: {.hint}
Sylow and semidirect products.
:::

::: {.solution}

::: pf

::: pf-step
(a) $G$ has a normal subgroup of order $p^2$.

::: pf-proof
Since $G$ is a nontrivial finite $p$-group, $Z(G)\ne1$ by the class equation.

::: pf-step
If $\abs{Z(G)}\ge p^2$, the claim holds.

::: pf-proof
The $p$-group $Z(G)$ has a subgroup of order $p^2$, and every subgroup of the center is normal.
:::

:::

::: pf-step
If $\abs{Z(G)}=p$, the claim holds.

::: pf-proof
Then $G/Z(G)$ has order $p^2$, so it is abelian. Choose a subgroup $L/Z(G)$ of order $p$; it is normal in the abelian group $G/Z(G)$, so its preimage $L$ is normal in $G$, and $\abs{L}=p\cdot p=p^2$.
:::

:::

:::

:::

::: pf-step
(b) Neither case occurs for the subgroup $N$ of part (a); if instead $G$ has an element $h$ of order $p^3$, then $G=\generators{h}\cong C_{p^3}$, and the existence of an element of order $p$ imposes no condition on $G$.

::: pf-proof
If $N=\generators{h}$ has order $p^2$, then $\abs h=p^2$, which is neither $p^3$ nor $p$. An element of order $p^3=\abs G$ generates $G$. Every group of order $p^3$ has an element of order $p$ by Cauchy's theorem.
:::

:::

:::

:::
