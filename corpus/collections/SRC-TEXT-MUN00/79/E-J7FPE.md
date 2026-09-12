---
schema: qual/card@1
id: E-J7FPE
kind: problem
title: Coverings of the torus are classified by rank
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
---

::: {.exercise}

Let $T = S^1 \times S^1$ be the torus; let $x_0 = b_0 \times b_0$.

(a) Prove the following.

Theorem.
Every isomorphism of $\pi_1(T, x_0)$ with itself is induced by a homeomorphism of $T$ with itself that maps $x_0$ to $x_0$.

[Hint: Let $p: \mathbb{R}^2 \to T$ be the usual covering map. If $A$ is a $2 \times 2$ matrix with integer entries, the linear map $T_A: \mathbb{R}^2 \to \mathbb{R}^2$ with matrix $A$ induces a continuous map $f: T \to T$. Furthermore, $f$ is a homeomorphism if $A$ is invertible over the integers.]

(b) Prove the following.

Theorem.
If $E$ is a covering space of $T$, then $E$ is homeomorphic either to $\mathbb{R}^2$, or to $S^1 \times \mathbb{R}$, or to $T$.

[Hint: You may use the following result from algebra: if $F$ is a free abelian group of rank 2 and $N$ is a nontrivial subgroup, then there is a basis $a_1, a_2$ for $F$ such that either (1) $ma_1$ is a basis for $N$, for some positive integer $m$, or (2) $ma_1, na_2$ is a basis for $N$, where $m$ and $n$ are positive integers.]
:::

::: {.solution}
(a) Identify
\[
\pi_1(T,x_0)\cong\mathbb Z^2.
\]
Every automorphism is therefore represented by a matrix
\[
A\in GL_2(\mathbb Z).
\]
Let \(L_A:\mathbb R^2	o\mathbb R^2\) be the linear map with matrix \(A\). Since \(A(\mathbb Z^2)=\mathbb Z^2\), the map descends through the quotient \(\mathbb R^2/\mathbb Z^2=T\) to
\[
f_A:T\to T,\qquad [v]\mapsto[Av].
\]
It fixes the basepoint \([0]\). Since \(A^{-1}\in GL_2(\mathbb Z)\), \(f_{A^{-1}}\) is its inverse, so \(f_A\) is a homeomorphism. On fundamental groups, \((f_A)_*=A\). Hence every automorphism of \(\pi_1(T)\) is induced by a basepoint-preserving homeomorphism.

(b) Assume the covering \(p:E	o T\) is connected, and put
\[
H=p_*\pi_1(E,e_0)\le\mathbb Z^2.
\]
By the subgroup classification quoted in the hint, after changing the basis of \(\mathbb Z^2\) by an automorphism, exactly one of the following occurs:

1. \(H=0\).
2. \(H=\langle(m,0)\rangle\) for some \(m>0\).
3. \(H=\langle(m,0),(0,n)\rangle\) for some \(m,n>0\).

By part (a), the basis change is induced by a homeomorphism of the base torus, so it does not change the homeomorphism type of the total covering space. The standard coverings realizing these three subgroups are exactly those in [[E-XFMJA]]:
\[
\mathbb R^2\to T,\qquad
S^1\times\mathbb R\to T,\qquad
T\to T.
\]
The classification theorem for connected covering spaces says two connected coverings corresponding to the same subgroup (up to the chosen basepoint equivalence) are equivalent. Therefore
\[
\boxed{E\cong\mathbb R^2,\quad S^1\times\mathbb R,\quad\text{or}\quad T.}
\]
:::
