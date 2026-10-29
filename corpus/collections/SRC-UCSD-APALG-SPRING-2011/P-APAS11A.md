---
schema: qual/card@1
id: P-APAS11A
kind: problem
title: Schur's lemma converse, abelian simultaneous diagonalization, and central elements
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Part (c) of the source omitted the hypothesis that A is irreducible, and A(s)=diag(1,-1) for C_2 is a counterexample; part (c) now assumes A irreducible.
---

::: {.problem}
Let $G$ be a finite group and $A\colon G\to\mathrm{GL}(n,\CC)$ be a representation of $G$.

(a) Show that if the only matrices $S$ which commute with $A(g)$ for all $g\in G$ are of the form $\lambda I$, then $A$ is irreducible.

(b) Show that if $G$ is abelian, then there is an invertible matrix $T$ such that for all $g\in G$, $TA(g)T^{-1}$ is a diagonal matrix.

(c) Show that if $A$ is irreducible and $g\in G$ is in the center of $G$, then $A(g)=cI_n$ for some nonzero constant $c\in\CC$.
:::

::: {.solution}
For (a), suppose $A$ were reducible. Then there would be a nonzero proper $G$-stable subspace
\[
0\ne W\subsetneq \CC^n.
\]
Because $G$ is finite and the ground field has characteristic $0$, Maschke's theorem gives a $G$-stable complement $W'$ with
\[
\CC^n=W\oplus W'.
\]
Let $P$ be the projection onto $W$ along $W'$. Since both summands are $G$-stable,
\[
PA(g)=A(g)P
\qquad(g\in G).
\]
But $P$ is neither $0$ nor $I$, so it is not a scalar matrix. This contradicts the hypothesis on the commutant. Hence $A$ is irreducible.

For (b), because $G$ is finite, every $g\in G$ has finite order. If $g^m=1$, then
\[
A(g)^m=I,
\]
so the minimal polynomial of $A(g)$ divides $x^m-1$. Over $\CC$, the polynomial $x^m-1$ has distinct roots, hence every $A(g)$ is diagonalizable.

Since $G$ is abelian, the matrices $A(g)$ commute pairwise. A commuting family of diagonalizable complex matrices is simultaneously diagonalizable. Indeed, diagonalize one member $A(g_0)$. Every other $A(g)$ preserves each eigenspace of $A(g_0)$ because it commutes with $A(g_0)$. Restrict the remaining commuting diagonalizable operators to each eigenspace and proceed by induction on the dimension. Thus there is a basis of common eigenvectors, i.e. an invertible matrix $T$ such that
\[
TA(g)T^{-1}
\]
is diagonal for every $g\in G$.

For (c), let $A$ be irreducible and $g\in Z(G)$. Centrality gives
\[
A(g)A(h)=A(gh)=A(hg)=A(h)A(g)
\qquad(h\in G).
\]
Thus $A(g)$ lies in the commutant of the irreducible representation. By Schur's lemma,
\[
A(g)=cI_n.
\]
Since $A(g)\in\operatorname{GL}_n(\CC)$, necessarily $c\ne0$.
:::
