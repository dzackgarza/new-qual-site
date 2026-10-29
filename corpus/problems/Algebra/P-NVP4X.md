---
schema: qual/card@1
id: P-NVP4X
kind: problem
title: Groups of order 55
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Discuss groups of order 55." and poses no definite question; the statement asks for the classification up to isomorphism, which the solution gives.'
---

::: {.problem}
Classify the groups of order 55 up to isomorphism.
:::

::: {.solution}
Let $G$ be a group of order $55=5\cdot11$.

::: pf

::: {.pf-step #normal-11}

The Sylow $11$-subgroup $P\cong C_{11}$ of $G$ is normal.

::: pf-proof

By the Sylow theorems,
$$
n_{11}\equiv1\pmod{11},\qquad n_{11}\mid5,
$$
so $n_{11}=1$.

:::

:::

::: {.pf-step #semidirect}

$G\cong C_{11}\rtimes_\varphi C_5$ for a homomorphism $\varphi\colon C_5\to\Aut(C_{11})\cong C_{10}$.

::: pf-proof

Let $Q\cong C_5$ be a Sylow $5$-subgroup. Then $P\cap Q=1$ by Lagrange's theorem, so $\abs{PQ}=55$ and $PQ=G$. Since $P$ is normal by step [](#normal-11){.pf-ref}, $G$ is the internal semidirect product of $P$ by $Q$.

:::

:::

::: pf-step

There are exactly $\boxed{2}$ groups of order $55$ up to isomorphism: $C_{55}$ and one nonabelian group $C_{11}\rtimes C_5$.

::: pf-proof

The image of $\varphi$ in step [](#semidirect){.pf-ref} has order dividing $5$, so it is trivial or the unique subgroup of order $5$ of the cyclic group $C_{10}$. A trivial $\varphi$ gives $C_{11}\times C_5\cong C_{55}$. Any two injective $\varphi$ have the same image, so they differ by an automorphism of $C_5$ and give isomorphic semidirect products; this group is nonabelian because $C_5$ acts nontrivially on $C_{11}$.

:::

:::

:::

:::
