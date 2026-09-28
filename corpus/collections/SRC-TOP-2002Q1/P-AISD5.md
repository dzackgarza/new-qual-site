---
schema: qual/card@1
id: P-AISD5
kind: problem
title: Nested nonempty closed subsets of a compact space have nonempty intersection
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $X$ be a compact space, and let $$A_1 \supseteq A_2 \supseteq \cdots \supseteq A_n \supseteq \cdots$$ be a descending chain of non-empty closed subsets of $X$.
Show that their intersection $$\bigcap_{n=1}^{\infty} A_n$$ is non-empty.
:::

::: {.solution}
<1>1. If $\bigcap_{n=1}^{\infty} A_n = \varnothing$, then $\{X \setminus A_n\}_{n\ge1}$ is an open cover of $X$.

::: {.proof}
Each $X\setminus A_n$ is open because $A_n$ is closed.
By De Morgan's law, $\bigcup_n (X \setminus A_n) = X \setminus \bigcap_n A_n = X$.
:::

<1>2. If $\bigcap_{n=1}^{\infty} A_n = \varnothing$, then $A_N=\varnothing$ for some $N$.

::: {.proof}
By step <1>1 and compactness of $X$, there are indices $n_1,\ldots,n_k$ with $X = \bigcup_{i=1}^k (X \setminus A_{n_i})$.
By De Morgan's law, $\bigcap_{i=1}^k A_{n_i} = \varnothing$.
Put $N = \max(n_1, \ldots, n_k)$.
Since the chain is descending, $A_N\subseteq A_{n_i}$ for each $i$, so $A_N=\bigcap_{i=1}^k A_{n_i}=\varnothing$.
:::

<1>3. Q.E.D.

::: {.proof}
Each $A_n$ is nonempty by hypothesis, so the conclusion of step <1>2 is false.
Hence $\bigcap_{n=1}^{\infty} A_n \neq \varnothing$.
:::
:::
