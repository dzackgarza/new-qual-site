---
schema: qual/card@1
id: P-POJFX
kind: problem
title: Jordan form of the all-ones matrix over a field
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Characteristic
relations: []
review: draft
---

::: {.problem}
Let $F$ be a field and $n$ a positive integer, and consider
$$
A=\left[\begin{array}{ccc}
1 & \dots & 1 \\
& \ddots & \\
1 & \dots & 1
\end{array}\right] \in M_{n}(F)
.$$

Show that $A$ has a Jordan normal form over $F$ and find it.

> Hint: treat the cases $n\cdot  1 \neq 0$ in $F$ and $n\cdot 1 = 0$ in $F$ separately.

:::

::: {.solution}

Let $u=(1,\ldots,1)^T\in F^n$, so that $A=uu^T$ and $Ax=(\textstyle\sum_ix_i)\,u$.

::: pf

::: {.pf-step #kernel}

$A^2=(n\cdot1)A$, $\operatorname{rk}A=1$, and $\ker A=\{x:\sum_ix_i=0\}$ has dimension $n-1$.

::: pf-proof

$A^2=u(u^Tu)u^T=(n\cdot1)uu^T$. The image of $A$ is $Fu\neq0$, and $Ax=0$ exactly when $\sum_ix_i=0$.

:::

:::

::: {.pf-step #exists}

$A$ has a Jordan normal form over $F$.

::: pf-proof

By Step [](#kernel){.pf-ref}, $A$ is annihilated by $x(x-n\cdot1)$, which splits over $F$. Hence the minimal polynomial splits, and $A$ is similar over $F$ to a Jordan matrix.

:::

:::

::: {.pf-step #nonzero}

If $n\cdot1\neq0$ in $F$, then $A$ is similar to $\operatorname{diag}(n,0,\ldots,0)$.

::: pf-proof

$x(x-n\cdot1)$ has distinct roots, so $A$ is diagonalizable. The eigenvalue $0$ has multiplicity $\dim\ker A=n-1$ by Step [](#kernel){.pf-ref}, and $Au=(n\cdot1)u$ gives the remaining eigenvalue $n\cdot1$.

:::

:::

::: {.pf-step #zero}

If $n\cdot1=0$ in $F$, then $n\ge2$ and $A$ is similar to $J_2(0)\oplus 0_{n-2}$, a single $2\times2$ nilpotent Jordan block and $n-2$ zero blocks of size $1$.

::: pf-proof

$n\cdot1=0$ forces $n\geq\operatorname{char}F\geq2$. By Step [](#kernel){.pf-ref}, $A^2=0$ and $A\neq0$, so $0$ is the only eigenvalue and every Jordan block has size at most $2$, with at least one of size $2$. The number of blocks is $\dim\ker A=n-1$. Blocks of sizes at most $2$, $n-1$ of them, with total size $n$, are exactly one block of size $2$ and $n-2$ of size $1$.

:::

:::

::: pf-qed

Step [](#exists){.pf-ref} gives existence, and Steps [](#nonzero){.pf-ref} and [](#zero){.pf-ref} give the Jordan form in the two cases.

:::

:::

:::
