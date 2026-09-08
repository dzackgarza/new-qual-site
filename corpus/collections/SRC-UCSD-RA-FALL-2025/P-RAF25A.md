---
schema: qual/card@1
id: P-RAF25A
kind: problem
title: "An infinite sigma-algebra is uncountable"
classification:
  areas:
  - real-analysis
  topics:
  - Sigma-Algebras
  - Cardinality
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Fall 2025 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $\mathcal{M}$ be an infinite $\sigma$-algebra of subsets of a set $X$.
For $A \subset X$, $A \neq \emptyset, X$, consider the collection $\mathcal{M}_A := \{B \cap A : B \in \mathcal{M}\}$.

(1) Prove that $\mathcal{M}_A$ is a $\sigma$-algebra of subsets of $A$.

(2) Prove that at least one of $\mathcal{M}_A$ and $\mathcal{M}_{A^c}$ contains infinitely many elements.

(3) Prove that $\mathcal{M}$ contains infinitely many pairwise disjoint sets.

(4) Prove that $\mathcal{M}$ is uncountable.
:::

::: solution
<1>1. The trace on $A$ is a $\sigma$-algebra.
::: proof
We have $A=X\cap A\in\mathcal M_A$. If $C=B\cap A\in\mathcal M_A$, then its complement relative to $A$ is
\[
A\setminus C=A\cap B^c\in\mathcal M_A.
\]
If $C_j=B_j\cap A\in\mathcal M_A$, then
\[
\bigcup_{j=1}^\infty C_j
=A\cap\bigcup_{j=1}^\infty B_j
\in\mathcal M_A.
\]
Thus $\mathcal M_A$ is a $\sigma$-algebra on $A$.
:::

<1>2. At least one trace $\sigma$-algebra is infinite.
::: proof
Consider
\[
\Phi:\mathcal M\to\mathcal M_A\times\mathcal M_{A^c},
\qquad
\Phi(B)=(B\cap A,B\cap A^c).
\]
The map is injective because
\[
B=(B\cap A)\cup(B\cap A^c).
\]
If both $\mathcal M_A$ and $\mathcal M_{A^c}$ were finite, their product would be finite, forcing $\mathcal M$ to be finite, contrary to hypothesis. Hence at least one of the two trace $\sigma$-algebras is infinite.
:::

<1>3. Construct infinitely many pairwise disjoint measurable sets.
::: proof
Set $R_0=X$. Since $\mathcal M_{R_0}=\mathcal M$ is infinite, choose a measurable subset
\[
\varnothing\ne A_1\subsetneq R_0.
\]
By Step 2 applied inside $R_0$, at least one of the trace $\sigma$-algebras on $A_1$ and $R_0\setminus A_1$ is infinite. Let $R_1$ be an infinite side and let $D_1$ be the other side. Then
\[
D_1\ne\varnothing,
\qquad
D_1\cap R_1=\varnothing,
\qquad
\mathcal M_{R_1}\text{ is infinite}.
\]

Repeat this construction recursively. At stage $n$, split $R_{n-1}$ into two nonempty measurable pieces, retain one piece $R_n$ whose trace $\sigma$-algebra is infinite, and call the other piece $D_n$. Then
\[
D_n\subset R_{n-1},
\qquad
R_n\subset R_{n-1},
\qquad
D_n\cap R_n=\varnothing.
\]
Since $R_{n-1}$ is contained in all earlier retained sets, the sets $D_1,D_2,\dots$ are pairwise disjoint and nonempty. Thus $\mathcal M$ contains infinitely many pairwise disjoint sets.
:::

<1>4. Use arbitrary subunions to prove uncountability.
::: proof
For every subset $I\subseteq\mathbb N$, define
\[
E_I:=\bigcup_{n\in I}D_n.
\]
Because $I$ is countable, $E_I\in\mathcal M$. If $I\ne J$, choose $n\in I\triangle J$. Since the $D_n$ are pairwise disjoint and nonempty,
\[
E_I\ne E_J.
\]
Hence
\[
I\longmapsto E_I
\]
is an injection from $\mathcal P(\mathbb N)$ into $\mathcal M$. Since $\mathcal P(\mathbb N)$ is uncountable,
\[
\boxed{\mathcal M\text{ is uncountable}.}
\]
:::
:::
