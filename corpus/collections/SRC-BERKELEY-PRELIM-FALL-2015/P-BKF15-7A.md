---
schema: qual/card@1
id: P-BKF15-7A
kind: problem
title: Similarity of nilpotent Jordan matrices is determined by block sizes
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2015 solution packet: successive
    differences dim ker(N^r)-dim ker(N^(r-1)) are the column lengths of the
    Young diagram, equivalently the numbers of blocks of size at least r.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the kernel dimension of powers of one nilpotent Jordan block,
    invariance of kernel dimensions under similarity, and recovery of the
    exact block-size multiplicities from successive differences.
---

::: {.problem}
It is a corollary to the Jordan canonical form theorem that $n\times n$ matrices in Jordan canonical form, all of whose eigenvalues are zeroes, are similar if and only if the sizes of their Jordan blocks coincide (up to permutations).
Prove this directly, without using the Jordan canonical form theorem.
:::

::: {.solution}
For $m\ge1$, let $J_m$ denote the nilpotent $m\times m$ Jordan block.

::: pf

::: {.pf-step #s1}

For every $m,r\ge1$,
$$
\dim\ker(J_m^r)=\min\{r,m\}.
$$

::: pf-proof

In the standard basis $e_1,\ldots,e_m$, choose the convention
$$
J_m e_1=0,
\qquad
J_m e_j=e_{j-1}
\quad
(2\le j\le m).
$$
Then
$$
J_m^r e_j=0
$$
exactly when $j\le r$, except that all basis vectors are killed when
$r\ge m$. Thus
$$
\ker(J_m^r)
=
\operatorname{span}
\{e_1,\ldots,e_{\min\{r,m\}}\},
$$
which has the stated dimension.

:::

:::

::: {.pf-step #s2}

Let
$$
N
=
J_{n_1}\oplus\cdots\oplus J_{n_k},
\qquad
n_1\ge\cdots\ge n_k.
$$
Then for every $r\ge1$,
$$
\dim\ker(N^r)
=
\sum_{j=1}^k\min\{r,n_j\}.
$$

::: pf-proof

The power $N^r$ is the direct sum
$$
J_{n_1}^r\oplus\cdots\oplus J_{n_k}^r.
$$
Its kernel is therefore the direct sum of the kernels of the block
powers. Apply step [](#s1){.pf-ref} and add their dimensions.

:::

:::

::: {.pf-step #s3}

Define
$$
d_r
\coloneqq
\dim\ker(N^r)-\dim\ker(N^{r-1}),
\qquad
r\ge1,
$$
where $\ker(N^0)=\{0\}$. Then
$$
d_r
=
\#\{j:n_j\ge r\}.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
\begin{aligned}
d_r
&=
\sum_{j=1}^k
\left(
\min\{r,n_j\}-\min\{r-1,n_j\}
\right).
\end{aligned}
$$
For a fixed block size $n_j$, the summand is $1$ exactly when
$n_j\ge r$, and is $0$ otherwise. Thus $d_r$ counts precisely the
blocks whose sizes are at least $r$.

:::

:::

::: {.pf-step #s4}

The sequence
$$
d_1,d_2,\ldots
$$
determines the multiset of Jordan block sizes of $N$.

::: pf-proof

By step [](#s3){.pf-ref}, the number of blocks of size exactly $r$ is
$$
d_r-d_{r+1},
$$
because $d_r$ counts blocks of size at least $r$ and $d_{r+1}$ counts
those of size at least $r+1$.

Thus, for every positive integer $r$, the multiplicity of the block
$J_r$ is determined by the sequence $(d_r)$.

:::

:::

::: {.pf-step #s5}

If two matrices $N$ and $M$ are similar, then
$$
\dim\ker(N^r)=\dim\ker(M^r)
$$
for every $r\ge1$.

::: pf-proof

If
$$
M=SNS^{-1},
$$
then
$$
M^r=SN^rS^{-1}.
$$
Moreover,
$$
v\in\ker(M^r)
\iff
N^rS^{-1}v=0
\iff
S^{-1}v\in\ker(N^r).
$$
Hence $S$ restricts to an isomorphism
$$
\ker(N^r)\xrightarrow{\sim}\ker(M^r),
$$
so the dimensions agree.

:::

:::

::: {.pf-step #s6}

If two nilpotent Jordan matrices are similar, then their Jordan
block sizes coincide up to permutation.

::: pf-proof

By step [](#s5){.pf-ref}, the two matrices have the same dimensions
$\dim\ker(N^r)$ for every $r$. Therefore they have the same sequence
of differences $d_r$. Step [](#s4){.pf-ref} then shows that they have the same
number of Jordan blocks of every size.

:::

:::

::: {.pf-step #s7}

If two nilpotent Jordan matrices have the same block sizes up to
permutation, then they are similar.

::: pf-proof

Reordering direct-sum blocks is accomplished by reordering the
corresponding coordinate basis vectors. The resulting change-of-basis
matrix is a permutation matrix. Hence two block-diagonal Jordan
matrices with the same blocks in a different order are conjugate by a
permutation matrix.

:::

:::

::: {.pf-step #s8}

Therefore two nilpotent matrices already in Jordan form are
similar if and only if their Jordan block sizes coincide up to
permutation.

::: pf-proof

The forward implication is step [](#s6){.pf-ref} and the reverse implication is
step [](#s7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s8){.pf-ref} is exactly the required direct classification.

:::

:::

:::
