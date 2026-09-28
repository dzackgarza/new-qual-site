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
Let $(\pi, V)$ be a faithful finite-dimensional representation of a finite group $G$ over $\mathbb{C}$.
Show that, given any irreducible representation $W$ of $G$, the $n$-th tensor power $V^{\otimes n}$ (or tensor algebra $T(V \oplus V^*)$) contains an isomorphic copy of $W$ for some integer $n \ge 0$.
:::

::: {.solution}
Let $\chi$ be the character of the faithful representation $V$, and let
\[
a_1=\chi(1),a_2,\dots,a_r
\]
be the distinct values taken by $\chi$ on $G$. Because $G$ is finite, we may choose a $G$-invariant Hermitian inner product on $V$, so every $\pi(g)$ is unitary. Thus
\[
|\chi(g)|\le \chi(1),
\]
and equality $\chi(g)=\chi(1)$ implies $\pi(g)=I$. Faithfulness then gives
\[
\chi(g)=\chi(1)\iff g=1.
\]
Hence the level set corresponding to $a_1=\chi(1)$ is exactly $\{1\}$.

Let $\psi$ be the irreducible character of $W$. Suppose, toward a contradiction, that $W$ occurs in none of
\[
V^{\otimes0},V^{\otimes1},\dots,V^{\otimes(r-1)}.
\]
Then
\[
0=|G|\langle \chi^n,\psi\rangle
=\sum_{g\in G}\chi(g)^n\overline{\psi(g)}
=\sum_{j=1}^r a_j^n c_j
\]
for $0\le n<r$, where
\[
c_j=\sum_{\chi(g)=a_j}\overline{\psi(g)}.
\]
The Vandermonde matrix $(a_j^n)_{0\le n<r,1\le j\le r}$ is invertible because the $a_j$ are distinct. Hence all $c_j=0$. But
\[
c_1=\overline{\psi(1)}=\dim W>0,
\]
a contradiction.

Therefore some $n\ge0$ satisfies
\[
\langle\chi^n,\psi\rangle>0,
\]
so $W$ occurs in $V^{\otimes n}$. In particular it also occurs in the tensor algebra $T(V\oplus V^*)$.
:::
