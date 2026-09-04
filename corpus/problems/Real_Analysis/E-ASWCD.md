---
schema: qual/card@1
id: E-ASWCD
kind: problem
title: Continuity of outer measure on Carathéodory-measurable sets
classification:
  areas:
  - real-analysis
  topics:
  - Continuity of Measure
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: exercise
- Let $\mu^*$ be an outer measure on $X$ and let $\mathcal M(\mu^*)$ be its Carathéodory $\sigma$-algebra.
  Show that the restriction of $\mu^*$ to $\mathcal M(\mu^*)$ is continuous from below, and continuous from above when the first set has finite outer measure.

- Give an outer measure for which these continuity statements fail on arbitrary subsets of $X$.
:::

::: {.solution}
By Carathéodory's theorem, $\mu\da\mu^*|_{\mathcal M(\mu^*)}$ is a measure.
Thus the usual continuity theorems for measures apply.
Explicitly, if $E_1\subseteq E_2\subseteq\cdots$ are Carathéodory measurable, set $F_1=E_1$ and $F_n=E_n\setminus E_{n-1}$ for $n\ge2$.
Then the $F_n$ are pairwise disjoint and measurable, and
\[
\mu^*\qty{\bigcup_{n\ge1}E_n}
=\sum_{n\ge1}\mu^*(F_n)
=\lim_{N\to\infty}\sum_{n=1}^N\mu^*(F_n)
=\lim_{N\to\infty}\mu^*(E_N).
\]

If $E_1\supseteq E_2\supseteq\cdots$ are measurable and $\mu^*(E_1)<\infty$, put $F_n=E_1\setminus E_n$.
Then $F_n\uparrow E_1\setminus\bigcap_nE_n$, so continuity from below and finite additivity give
\[
\mu^*(E_1)-\mu^*\qty{\bigcap_nE_n}
=\lim_{n\to\infty}\mu^*(F_n)
=\mu^*(E_1)-\lim_{n\to\infty}\mu^*(E_n).
\]
Cancellation is legitimate because $\mu^*(E_1)<\infty$, yielding continuity from above.

Neither statement is true for an arbitrary outer measure on arbitrary sets.
On $X=\NN$, define
\[
\mu^*(A)=
\begin{cases}
0,&A=\emptyset,\\
1,&0<|A|<\infty,\\
2,&|A|=\infty.
\end{cases}
\]
This is an outer measure: monotonicity is immediate, and countable subadditivity follows because an infinite union either contains an infinite member or has infinitely many nonempty finite members.
For $E_n=\{1,\ldots,n\}$,
\[
\mu^*(E_n)=1\quad\text{for all }n,
\qquad
\mu^*\qty{\bigcup_nE_n}=\mu^*(\NN)=2,
\]
so continuity from below fails.
For $G_n=\{n,n+1,\ldots\}$,
\[
\mu^*(G_n)=2\quad\text{for all }n,
\qquad
\mu^*\qty{\bigcap_nG_n}=0,
\]
so continuity from above fails even though $\mu^*(G_1)=2<\infty$.
:::
