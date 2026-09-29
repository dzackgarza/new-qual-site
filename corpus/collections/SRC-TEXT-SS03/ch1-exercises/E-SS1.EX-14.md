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

::: {.exercise}
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

::: pf

::: {.pf-step #s1}

For every $n$, one has $b_n=B_n-B_{n-1}$.

::: pf-proof

By definition,
\[
B_n=\sum_{k=1}^n b_k
\quad\text{and}\quad
B_{n-1}=\sum_{k=1}^{n-1}b_k,
\]
so subtraction gives $B_n-B_{n-1}=b_n$.

:::

:::

::: {.pf-step #s2}

Therefore
\[
\sum_{n=M}^N a_nb_n
=
\sum_{n=M}^N a_nB_n-
\sum_{n=M}^N a_nB_{n-1}.
\]

::: pf-proof

Substitute the identity from step [](#s1){.pf-ref} into each term of the finite sum and distribute.

:::

:::

::: {.pf-step #s3}

The second sum may be separated and reindexed as
\[
\sum_{n=M}^N a_nB_{n-1}
=
a_MB_{M-1}+\sum_{n=M}^{N-1}a_{n+1}B_n.
\]

::: pf-proof

Separate the term with $n=M$, and in the remaining sum replace the index $n$ by $n+1$.

:::

:::

::: {.pf-step #s4}

Likewise,
\[
\sum_{n=M}^N a_nB_n
=
a_NB_N+\sum_{n=M}^{N-1}a_nB_n.
\]

::: pf-proof

Separate the terminal term $n=N$.

:::

:::

::: pf-step

Hence
\[
\sum_{n=M}^N a_nb_n
=
a_NB_N-a_MB_{M-1}
-\sum_{n=M}^{N-1}(a_{n+1}-a_n)B_n.
\]

::: pf-proof

Insert steps [](#s3){.pf-ref} and [](#s4){.pf-ref} into step [](#s2){.pf-ref}. The remaining interior contribution is
\[
\sum_{n=M}^{N-1}(a_n-a_{n+1})B_n
=-\sum_{n=M}^{N-1}(a_{n+1}-a_n)B_n,
\]
which gives the claimed identity.

:::

:::

:::

:::
