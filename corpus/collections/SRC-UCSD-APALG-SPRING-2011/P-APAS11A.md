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

The argument is the card's own, from Maschke's theorem, the diagonalizability criterion and Schur's lemma; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $G$ be a finite group and $A:G\to\mathrm{GL}(n,\CC)$ a representation, with $A(g)$ acting on $V=\CC^{n}$.

::: pf

::: {.pf-step #a}
(a) If the only matrices commuting with every $A(g)$ are the scalar matrices, then $A$ is irreducible.

::: pf-proof

::: {.pf-step #invariant}
A reducible $A$ leaves a proper nonzero subspace $W$ invariant, and $W$ has an $A(G)$-stable complement.

::: pf-proof
Reducibility means exactly that there is a subspace $W$ with $0\ne W\subsetneq V$ and $A(g)W\subseteq W$ for every $g$. Because $G$ is finite and $\CC$ has characteristic $0$, Maschke's theorem applies: averaging any projection onto $W$ over $G$, the map $\frac{1}{\abs{G}}\sum_{g}A(g)\pi A(g)^{-1}$ is a $G$-equivariant projection onto $W$, whose kernel $W'$ is a $G$-stable complement with $V=W\oplus W'$.
:::

:::

::: {.pf-step #projection}
The projection $P$ of $V$ onto $W$ along $W'$ satisfies $P A(g)=A(g)P$ for every $g$, and $P$ is neither $0$ nor $I$.

::: pf-proof
Write $v=w+w'$ with $w\in W$, $w'\in W'$. Both summands are $G$-stable, so $A(g)w\in W$ and $A(g)w'\in W'$; hence $A(g)v=A(g)w+A(g)w'\in W$ is the decomposition of $A(g)v$ along $V=W\oplus W'$. Therefore $P A(g)v=A(g)w=A(g)Pv$. And $P$ is the identity on the nonzero space $W$ and zero on $W'$, which is nonzero because $W\ne V$; so $P\ne I$ and $P\ne0$.
:::

:::

::: {.pf-qed}
By step [](#projection){.pf-ref} $P$ commutes with every $A(g)$ but is not a scalar matrix: a scalar matrix $\lambda I$ that is a projection satisfies $(\lambda I)^{2}=\lambda I$, so $\lambda\in\{0,1\}$ and $P$ would be $0$ or $I$. This contradicts the hypothesis on the commutant, so $A$ is irreducible.
:::

:::

:::

::: {.pf-step #diagonalizable}
(b) Every $A(g)$ is diagonalizable.

::: pf-proof
$G$ is finite, so $g^{m}=1$ for some $m\ge1$, and then $A(g)^{m}=A(g^{m})=A(1)=I$. So the minimal polynomial of $A(g)$ divides $x^{m}-1$, which has $m$ distinct roots in $\CC$ because its derivative $mx^{m-1}$ vanishes only at $0$ and $0$ is not a root. A matrix whose minimal polynomial has distinct roots is diagonalizable over $\CC$.
:::

:::

::: {.pf-step #simultaneous}
(b) A commuting family of diagonalizable complex matrices is simultaneously diagonalizable.

::: pf-proof
Induction on the dimension $n$; for $n=0$ there is nothing to prove. If every member of the family is a scalar matrix, the claim holds in any basis. Otherwise choose a non-scalar member $M$ of the family. Let $V=\bigoplus_{\lambda}V_{\lambda}$ be the decomposition of $V$ into the eigenspaces of $M$, which is direct because $M$ is diagonalizable. Each $N$ in the family commutes with $M$, so for $v\in V_{\lambda}$, $M N v=NMv=\lambda Nv$ and $Nv\in V_{\lambda}$: the eigenspaces are stable under the whole family. The restrictions of the family to $V_{\lambda}$ are diagonalizable (the minimal polynomial of a restriction divides that of the operator) and commute, so by induction, applied in each nonzero eigenspace, each admits a basis of common eigenvectors; their union over $\lambda$ is a basis of $V$ of common eigenvectors.
:::

:::

::: {.pf-step #abelian}
(b) If $G$ is abelian there is $T\in\mathrm{GL}(n,\CC)$ with $TA(g)T^{-1}$ diagonal for every $g$.

::: pf-proof
For an abelian $G$ one has $A(g)A(h)=A(gh)=A(hg)=A(h)A(g)$ for all $g,h$, so the family $\{A(g)\}$ commutes pairwise. Each member is diagonalizable by step [](#diagonalizable){.pf-ref}, so by step [](#simultaneous){.pf-ref} there is a basis of $V$ consisting of common eigenvectors; the matrix $T$ of change from the standard basis to that basis conjugates every $A(g)$ to a diagonal matrix.
:::

:::

::: {.pf-step #central}
(c) If $A$ is irreducible and $g$ lies in the centre of $G$, then $A(g)=cI_{n}$ with $c\ne0$.

::: pf-proof
For $h\in G$, centrality gives $A(g)A(h)=A(gh)=A(hg)=A(h)A(g)$, so $A(g)$ commutes with every element of $A(G)$. An operator commuting with an irreducible representation is a scalar (Schur's lemma), so $A(g)=cI_{n}$. Since $A(g)\in\mathrm{GL}_{n}(\CC)$ is invertible and $n\ge1$, $c\ne0$.
:::

:::

:::
:::
