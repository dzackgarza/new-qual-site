---
schema: qual/card@1
id: P-WESRA07-II3
kind: problem
title: A measurable set contains subsets of every smaller prescribed measure
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Part II, item 3 of the Real Analysis section of the Wesleyan University Analysis Qualifier, Summer 2007, in analysis_2003-2007.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $A\subset\mathbb R^2$ be Lebesgue measurable with $m(A)>0$. Prove that for every
\[
0<t<m(A)
\]
there is a measurable subset $B\subset A$ with $m(B)=t$.
:::

::: solution
Fix $0<t<m(A)$. Since
\[
A=\bigcup_{N=1}^\infty \bigl(A\cap[-N,N]^2\bigr)
\]
and these sets increase with $N$, continuity from below gives
\[
m(A)=\lim_{N\to\infty}m\bigl(A\cap[-N,N]^2\bigr).
\]
Hence for some $N$ the bounded measurable set
\[
E:=A\cap[-N,N]^2
\]
satisfies $m(E)>t$.

For $s\in\mathbb R$, define
\[
F(s)=m\bigl(E\cap(( -\infty,s]\times\mathbb R)\bigr).
\]
Then $F(s)=0$ for $s<-N$ and $F(s)=m(E)>t$ for $s\ge N$. Moreover $F$ is continuous. Indeed, if $s_j\to s$, then
\[
\mathbf1_{E\cap(( -\infty,s_j]\times\mathbb R)}
\longrightarrow
\mathbf1_{E\cap(( -\infty,s]\times\mathbb R)}
\]
for every point outside the vertical line $\{s\}\times\mathbb R$, which has two-dimensional Lebesgue measure zero. Since the indicators are bounded by the integrable function $\mathbf1_E$, dominated convergence gives $F(s_j)\to F(s)$.

By the intermediate value theorem, there is $s_0\in[-N,N]$ such that
\[
F(s_0)=t.
\]
Therefore
\[
B:=E\cap(( -\infty,s_0]\times\mathbb R)
\]
is measurable, satisfies $B\subset A$, and has
\[
\boxed{m(B)=t}.
\]
:::
