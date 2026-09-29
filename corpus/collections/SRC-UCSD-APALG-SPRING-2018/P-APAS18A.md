---
schema: qual/card@1
id: P-APAS18A
kind: problem
title: Similarity of $8\times 8$ matrices with prescribed ranks of powers
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $A,B\in\mathbb{C}^{8\times 8}$ be two matrices such that
\[
\operatorname{rank} A=\operatorname{rank} B=6,\quad
\operatorname{rank} A^2=\operatorname{rank} B^2=4,\quad
\operatorname{rank} A^3=\operatorname{rank} B^3=2,\quad
\operatorname{rank} A^4=\operatorname{rank} B^4=0.
\]
Determine whether $A$ and $B$ are similar to each other or not.
If yes, explain why; if no, give a counterexample.
:::

::: {.solution}

::: pf

::: pf-step

$A^4 = 0$ and $B^4 = 0$, so both $A$ and $B$ are nilpotent.

::: pf-proof

$\operatorname{rank} A^4 = 0$ means $A^4 = 0$.

:::

:::

::: {.pf-step #s2}

The ranks of the powers of a nilpotent matrix determine its Jordan form.

::: pf-proof

::: {.pf-step #s2-1}

For a nilpotent matrix $N$, the number of Jordan blocks of size $\ge k$ is $\operatorname{rank} N^{k-1} - \operatorname{rank} N^k$.

::: pf-proof

standard fact about nilpotent Jordan forms.

:::

:::

::: {.pf-step #s2-2}

For $A$: number of blocks of size $\ge 1$ is $8 - 6 = 2$; size $\ge 2$ is $6 - 4 = 2$; size $\ge 3$ is $4 - 2 = 2$; size $\ge 4$ is $2 - 0 = 2$.

::: pf-proof

Step [](#s2-1){.pf-ref} applied to the given ranks.

:::

:::

::: pf-step

Hence $A$ has $2$ Jordan blocks, each of size $4$.

::: pf-proof

Step [](#s2-2){.pf-ref} (two blocks of size $\ge 4$, and total size $8$, so two blocks of size exactly $4$).

:::

:::

:::

:::

::: {.pf-step #s3}

The same computation applies to $B$, so $B$ also has $2$ Jordan blocks of size $4$.

::: pf-proof

$B$ has the same ranks of powers.

:::

:::

::: {.pf-step #s4}

Hence $A$ and $B$ have the same Jordan form (two nilpotent blocks of size $4$), so they are similar.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref}.

:::

:::

:::
