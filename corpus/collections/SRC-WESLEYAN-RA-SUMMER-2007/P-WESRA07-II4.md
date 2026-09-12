---
schema: qual/card@1
id: P-WESRA07-II4
kind: problem
title: A finite measure invariant under a nonzero translation is zero
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Part II, item 4 of the Real Analysis section of the Wesleyan University Analysis Qualifier, Summer 2007, in analysis_2003-2007.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $\mu$ be a finite Borel measure on $\mathbb R$. Suppose there is $t>0$ such that
\[
\mu(A+t)=\mu(A)
\]
for every Borel set $A\subset\mathbb R$. Prove that $\mu$ is the zero measure.
:::

::: solution
Let
\[
I=[0,t).
\]
For distinct integers $k$, the translates
\[
I+kt=[kt,(k+1)t)
\]
are pairwise disjoint. By the assumed translation invariance,
\[
\mu(I+kt)=\mu(I)
\]
for every $k\in\mathbb Z$.

If $\mu(I)>0$, then for every $N\ge1$,
\[
\mu(\mathbb R)
\ge
\mu\!\left(\bigcup_{k=0}^{N-1}(I+kt)\right)
=N\mu(I),
\]
which contradicts finiteness of $\mu(\mathbb R)$ as $N\to\infty$. Hence
\[
\mu(I)=0.
\]

Now
\[
\mathbb R=\bigcup_{k\in\mathbb Z}(I+kt),
\]
so countable subadditivity gives
\[
\mu(\mathbb R)
\le\sum_{k\in\mathbb Z}\mu(I+kt)=0.
\]
Thus $\mu(\mathbb R)=0$, and consequently every Borel set has measure zero. Therefore
\[
\boxed{\mu=0}.
\]
:::
