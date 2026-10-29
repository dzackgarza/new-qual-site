---
schema: qual/card@1
id: P-UECFO
kind: problem
title: Every irreducible representation of $G$ appears in a tensor power of a faithful
  finite-dimensional representation
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Tensor Products
  - Semisimplicity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $(\pi, V)$ be a faithful finite-dimensional representation of a finite group $G$ over $\CC$.
Show that, given any irreducible representation $W$ of $G$, the $n$-th tensor power $V^{\otimes n}$ (or tensor algebra $T(V \oplus V^*)$) contains an isomorphic copy of $W$ for some integer $n \ge 0$.
:::

::: {.solution}
Let $\chi$ be the character of $V$, let $a_1=\chi(1),a_2,\ldots,a_r$ be the distinct values of $\chi$ on $G$, and let $\psi$ be the character of $W$.

::: pf

::: {.pf-step #level-set}
$\chi(g)=\chi(1)$ if and only if $g=1$.

::: pf-proof
Averaging a Hermitian inner product over $G$ gives a $G$-invariant one, so each $\pi(g)$ is unitary and diagonalizable with eigenvalues of absolute value $1$.
Thus $\chi(g)$ is a sum of $\chi(1)$ such eigenvalues, and $\chi(g)=\chi(1)$ forces every eigenvalue to be $1$, so $\pi(g)=I$.
Since $\pi$ is faithful, $g=1$.
:::

:::

::: pf-step
$W$ occurs in $V^{\otimes n}$ for some $0\le n<r$.

::: pf-proof
Suppose not. Then for $0\le n<r$, with $c_j\coloneqq\sum_{\chi(g)=a_j}\overline{\psi(g)}$,
$$
0=\abs{G}\inner{\chi^n}{\psi}=\sum_{g\in G}\chi(g)^n\overline{\psi(g)}=\sum_{j=1}^r a_j^nc_j.
$$
The Vandermonde matrix $(a_j^n)_{0\le n<r,\,1\le j\le r}$ is invertible because the $a_j$ are distinct, so every $c_j=0$.
But by step [](#level-set){.pf-ref} the level set of $a_1$ is $\{1\}$, so $c_1=\overline{\psi(1)}=\dim W>0$, a contradiction.
:::

:::

::: pf-step
$W$ occurs in the tensor algebra $T(V\oplus V^*)$.

::: pf-proof
$V^{\otimes n}$ is a direct summand of $(V\oplus V^*)^{\otimes n}$, which is a summand of $T(V\oplus V^*)$.
:::

:::

:::

:::
