---
schema: qual/card@1
id: P-BKF08-3B
kind: problem
title: Abelian groups of order $p^n$ and similarity classes of nilpotent $n\times n$ matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 3B of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked that the finite-abelian-p-group classification and nilpotent
    Jordan form are both parametrized uniquely by partitions of n, over
    an arbitrary field F.
---

::: {.problem}
Let $F$ be a field and $p$ a prime.
For $n\ge1$, show that the number, up to isomorphism, of abelian groups of order $p^n$ equals the number, up to similarity, of $n\times n$ matrices $A$ over $F$ satisfying $A^n=0$.
:::

::: {.solution}
Let a partition of $n$ mean a tuple
$$
\lambda=(\lambda_1,\ldots,\lambda_r),
\qquad
\lambda_1\ge\cdots\ge\lambda_r\ge1,
\qquad
\sum_{j=1}^r\lambda_j=n.
$$

::: pf

::: {.pf-step #s1}

Isomorphism classes of abelian groups of order $p^n$ are in
bijection with partitions of $n$.

::: pf-proof

By the classification theorem for finite abelian groups, every abelian
group $G$ of order $p^n$ has a decomposition
$$
G\cong
\ZZ/p^{\lambda_1}\ZZ
\oplus\cdots\oplus
\ZZ/p^{\lambda_r}\ZZ
$$
with
$$
\lambda_1\ge\cdots\ge\lambda_r\ge1.
$$
Taking orders gives
$$
p^n=\abs{G}=p^{\lambda_1+\cdots+\lambda_r},
$$
so the $\lambda_j$ form a partition of $n$. The same classification
theorem says that these exponents are uniquely determined by the
isomorphism class of $G$. Conversely, every partition of $n$ gives such
an abelian group of order $p^n$.

:::

:::

::: {.pf-step #s2}

Every $n\times n$ matrix $A$ over $F$ satisfying $A^n=0$ is
similar over $F$ to a direct sum
$$
J_{\lambda_1}(0)\oplus\cdots\oplus J_{\lambda_r}(0),
$$
where $(\lambda_1,\ldots,\lambda_r)$ is a partition of $n$.

::: pf-proof

The relation $A^n=0$ says that $A$ is nilpotent. Its minimal polynomial
therefore divides $x^n$, which splits over every field $F$. Hence the
Jordan normal form theorem applies over $F$, and every Jordan block has
the form $J_d(0)$ for some $d\ge1$.

If the block sizes are $\lambda_1,\ldots,\lambda_r$, then their dimensions
sum to the dimension of the whole space:
$$
\lambda_1+\cdots+\lambda_r=n.
$$
Reordering the blocks so that the sizes are weakly decreasing produces a
partition of $n$.

:::

:::

::: {.pf-step #s3}

Two matrices satisfying $A^n=0$ are similar if and only if their
partitions in step [](#s2){.pf-ref} are equal.

::: pf-proof

Jordan normal form is unique up to permutation of its Jordan blocks.
Thus a nilpotent similarity class is determined exactly by the multiset
of its block sizes. Writing those sizes in weakly decreasing order gives
exactly one partition of $n$. Conversely, equal partitions give the same
Jordan normal form and hence similar matrices.

:::

:::

::: {.pf-step #s4}

Similarity classes of $n\times n$ matrices $A$ satisfying $A^n=0$
are therefore in bijection with partitions of $n$.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} assign to each similarity class a unique partition.
Conversely, for every partition
$\lambda=(\lambda_1,\ldots,\lambda_r)$ of $n$, the matrix
$$
J_{\lambda_1}(0)\oplus\cdots\oplus J_{\lambda_r}(0)
$$
has size $n$ and satisfies $A^n=0$, since each block has size at most
$n$ and is nilpotent.

:::

:::

::: {.pf-step #s5}

The two numbers in the problem are equal; both are the number of
partitions of $n$.

::: pf-proof

Step [](#s1){.pf-ref} identifies the abelian-group isomorphism classes with
partitions of $n$, while step [](#s4){.pf-ref} identifies the required matrix
similarity classes with the same set of partitions.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves the asserted equality.

:::

:::

:::
