---
schema: qual/card@1
id: P-WESRA05-1
kind: problem
title: Sigma-algebras, limsup and liminf of sets, and finite cardinalities
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked directly against Problem 1 of the scanned Wesleyan Real Analysis Preliminary Examination, 2005, in analysis_2003-2007.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $X$ be nonempty and let $\mathcal A$ be a collection of subsets of $X$.

1. Define what it means for $\mathcal A$ to be a sigma-algebra.
2. If $A_1,A_2,\ldots\in\mathcal A$, prove that the set of points belonging to infinitely many $A_n$ lies in $\mathcal A$.
3. Prove that the set of points belonging to all but finitely many $A_n$ lies in $\mathcal A$.
4. Describe the relationship between these two sets.
5. If $X$ has exactly five points, determine the possible cardinalities of sigma-algebras on $X$.
:::

::: solution
<1>1. Definition.
::: proof
A sigma-algebra $\mathcal A$ on $X$ is a collection of subsets of $X$ such that
\[
X\in\mathcal A,
\]
$A\in\mathcal A$ implies $X\setminus A\in\mathcal A$, and whenever $A_1,A_2,\ldots\in\mathcal A$,
\[
\bigcup_{n=1}^\infty A_n\in\mathcal A.
\]
:::

<1>2. The infinitely-often set is measurable.
::: proof
The set of points belonging to infinitely many $A_n$ is
\[
\limsup_{n\to\infty}A_n
=
\bigcap_{N=1}^\infty\bigcup_{n\ge N}A_n.
\]
Since sigma-algebras are closed under countable unions and intersections, this set belongs to $\mathcal A$.
:::

<1>3. The eventually-always set is measurable.
::: proof
The set of points belonging to all but finitely many $A_n$ is
\[
\liminf_{n\to\infty}A_n
=
\bigcup_{N=1}^\infty\bigcap_{n\ge N}A_n.
\]
Again this belongs to $\mathcal A$.
:::

<1>4. Compare the two sets.
::: proof
If a point belongs to all but finitely many $A_n$, then it certainly belongs to infinitely many of them. Therefore
\[
\boxed{\liminf A_n\subseteq\limsup A_n.}
\]
Equality holds exactly when membership in the sequence $(A_n)$ eventually stabilizes for every point outside no exceptional oscillatory set; equivalently, no point belongs to infinitely many $A_n$ and also to infinitely many complements $A_n^c$.
:::

<1>5. Determine the possible sizes on a five-point set.
::: proof
Every sigma-algebra on a finite set is determined by its atoms, which form a partition of $X$. If there are $k$ atoms, then every measurable set is a union of atoms, so the sigma-algebra has exactly
\[
2^k
\]
elements.

Since $X$ has five points, the number $k$ of nonempty atoms may be any integer from $1$ through $5$. Each value occurs, by choosing a partition of $X$ into $k$ nonempty blocks. Hence the possible cardinalities are
\[
\boxed{2,4,8,16,32.}
\]
:::
:::
