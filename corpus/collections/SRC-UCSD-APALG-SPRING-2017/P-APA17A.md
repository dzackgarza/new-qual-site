---
schema: qual/card@1
id: P-APA17A
kind: problem
title: Jordan form from the rank sequence of a $10\times 10$ nilpotent matrix
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 1 of the Qualifying Exam in Applied Algebra of May 30, 2017, printed p.
    1 of the nine-page paper retained at assets/attachments/APPLIED-ALGEBRA-EXAM.pdf, is the statement
    the card answers, and the paragraph at the head of the solution records that the paper prints no
    solutions, so the argument is the card's own. Checked: the statement against the paper's text layer
    at the page named; the ranks of the powers read against the Jordan block count; `qualc.authoring
    check` on the card, and `tmp/lam.sh` for the numbering and the QED. Not checked: no retained
    solution set exists for this paper to compare the argument with, and no other card of the collection
    in this pass.
---

::: {.problem}
Let $A \in \CC^{10 \times 10}$ be a matrix such that
$$
\operatorname{rank} A = 7,\quad
\operatorname{rank} A^2 = 4,\quad
\operatorname{rank} A^3 = 1,\quad
\operatorname{rank} A^4 = 0.
$$
Determine all possibilities of Jordan's canonical form for $A$.
:::

::: {.solution}

The computation is the card's own, from the ranks and the Jordan block count; no retained set solves this exercise — the retained paper `assets/attachments/APPLIED-ALGEBRA-EXAM.pdf`, the Qualifying Exam in Applied Algebra of May 30, 2017, prints this as Problem 1 on its p. 1 and contains no solutions — and the sets searched are recorded in the audit trail.

Let $A\in\CC^{10\times10}$ with $\operatorname{rank}A=7$, $\operatorname{rank}A^{2}=4$, $\operatorname{rank}A^{3}=1$ and $\operatorname{rank}A^{4}=0$.

::: pf

::: {.pf-step #nilpotent}
$A$ is nilpotent, so every Jordan block of $A$ is a nilpotent block $J_{m}(0)$.

::: pf-proof
$A^{4}=0$ by the vanishing of its rank, so $A$ is nilpotent. The Jordan form of a nilpotent matrix has all diagonal entries $0$, since the only eigenvalue of a nilpotent matrix is $0$; so every Jordan block is $J_{m}(0)$ for some $m\ge1$.
:::

:::

::: {.pf-step #kernels}
$\dim\ker A^{k}=3,6,9,10$ for $k=1,2,3,4$.

::: pf-proof
By the rank–nullity theorem applied to $A^{k}$, $\dim\ker A^{k}=10-\operatorname{rank}A^{k}$, which gives $10-7=3$, $10-4=6$, $10-1=9$ and $10-0=10$ for $k=1,2,3,4$.
:::

:::

::: {.pf-step #increments}
$\dim\ker A^{k}-\dim\ker A^{k-1}$ equals the number of Jordan blocks of $A$ of size at least $k$.

::: pf-proof
A nilpotent Jordan block $J_{m}(0)$ of size $m$ satisfies $\dim\ker J_{m}(0)^{k}=\min(k,m)$, so the increment $\dim\ker J_{m}(0)^{k}-\dim\ker J_{m}(0)^{k-1}$ is $1$ if $m\ge k$ and $0$ otherwise. Both $\ker A^{k}$ and the count are read off block by block in the Jordan basis, so the increments add.
:::

:::

::: {.pf-step #sizes}
The Jordan blocks of $A$ have sizes $4,3,3$.

::: pf-proof
The increments of step [](#kernels){.pf-ref} are
$$
\dim\ker A-\dim\ker A^{0}=3,\quad 6-3=3,\quad 9-6=3,\quad 10-9=1,
$$
using $\ker A^{0}=0$. By step [](#increments){.pf-ref}: the number of blocks is $3$; all three have size at least $2$ and at least $3$; exactly one has size at least $4$; and no block has size at least $5$, the increment at $k=5$ being $\dim\ker A^{5}-\dim\ker A^{4}=0$ since $A^{5}=A\cdot A^{4}=0$. So there are three blocks, all of size at least $3$, exactly one of size at least $4$ and none of size $5$ or more: that one is a block of size $4$ and the other two have size exactly $3$.
:::

:::

::: {.pf-step #answer}
The only possible Jordan form is
$$
\boxed{J_{4}(0)\oplus J_{3}(0)\oplus J_{3}(0).}
$$

::: pf-proof
By step [](#sizes){.pf-ref} the block sizes are $4,3,3$, and their sum is $4+3+3=10$, the whole dimension; the Jordan form is determined by the multiset of block sizes and the eigenvalue $0$. So this is the only possibility, and it does satisfy the given ranks: $\rank J_{4}\oplus J_{3}\oplus J_{3}$ is $3+2+2=7$, its square has rank $2+1+1=4$, its cube has rank $1+0+0=1$, and its fourth power is $0$.
:::

:::

:::
:::
