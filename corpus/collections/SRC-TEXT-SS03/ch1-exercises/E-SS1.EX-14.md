---
schema: qual/card@1
id: E-SS1.EX-14
kind: problem
title: Summation by parts
classification:
  areas:
  - complex-analysis
  topics:
  - Series
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: exercise
Suppose $\{a_n\}_{n=1}^N$ and $\{b_n\}_{n=1}^N$ are two finite sequences of complex numbers. Let
\[
B_k=\sum_{n=1}^k b_n,
\qquad B_0=0.
\]
Prove the summation-by-parts formula
\[
\sum_{n=M}^N a_n b_n
=
a_NB_N-a_MB_{M-1}-\sum_{n=M}^{N-1}(a_{n+1}-a_n)B_n.
\]
:::

::: {.solution}
<1>1. For every $n$, one has $b_n=B_n-B_{n-1}$.
::: {.proof}
By definition,
\[
B_n=\sum_{k=1}^n b_k
\quad\text{and}\quad
B_{n-1}=\sum_{k=1}^{n-1}b_k,
\]
so subtraction gives $B_n-B_{n-1}=b_n$.
:::

<1>2. Therefore
\[
\sum_{n=M}^N a_nb_n
=
\sum_{n=M}^N a_nB_n-
\sum_{n=M}^N a_nB_{n-1}.
\]
::: {.proof}
Substitute the identity from <1>1 into each term of the finite sum and distribute.
:::

<1>3. The second sum may be separated and reindexed as
\[
\sum_{n=M}^N a_nB_{n-1}
=
a_MB_{M-1}+\sum_{n=M}^{N-1}a_{n+1}B_n.
\]
::: {.proof}
Separate the term with $n=M$, and in the remaining sum replace the index $n$ by $n+1$.
:::

<1>4. Likewise,
\[
\sum_{n=M}^N a_nB_n
=
a_NB_N+\sum_{n=M}^{N-1}a_nB_n.
\]
::: {.proof}
Separate the terminal term $n=N$.
:::

<1>5. Hence
\[
\sum_{n=M}^N a_nb_n
=
a_NB_N-a_MB_{M-1}
-\sum_{n=M}^{N-1}(a_{n+1}-a_n)B_n.
\]
::: {.proof}
Insert <1>3 and <1>4 into <1>2. The remaining interior contribution is
\[
\sum_{n=M}^{N-1}(a_n-a_{n+1})B_n
=-\sum_{n=M}^{N-1}(a_{n+1}-a_n)B_n,
\]
which gives the claimed identity.
:::
:::
