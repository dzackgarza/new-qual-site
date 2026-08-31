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
<1>1. Suppose for contradiction that $\bigcap_{n=1}^{\infty} A_n = \varnothing$.
::: {.proof}
assume the intersection is empty.
:::

<1>2. Then $\{X \setminus A_n\}_{n=1}^{\infty}$ is an open cover of $X$.
::: {.proof}
$\bigcup_n (X \setminus A_n) = X \setminus \bigcap_n A_n = X \setminus \varnothing = X$ by De Morgan's law.
:::

<1>3. Since $X$ is compact, there is a finite subcover $X = \bigcup_{i=1}^k (X \setminus A_{n_i})$.
::: {.proof}
compactness.
:::

<1>4. Hence $\bigcap_{i=1}^k A_{n_i} = \varnothing$.
::: {.proof}
De Morgan's law applied to <1>3.
:::

<1>5. But $\bigcap_{i=1}^k A_{n_i} = A_N$ where $N = \max(n_1, \ldots, n_k)$.
::: {.proof}
the chain is descending, so the intersection of finitely many of them is the one with the largest index.
:::

<1>6. $A_N \neq \varnothing$, a contradiction.
::: {.proof}
each $A_n$ is nonempty by hypothesis.
:::

<1>7. Hence $\bigcap_{n=1}^{\infty} A_n \neq \varnothing$.
::: {.proof}
<1>1–<1>6.
:::

<1>8. Q.E.D.
::: {.proof}
<1>7.
:::
:::
