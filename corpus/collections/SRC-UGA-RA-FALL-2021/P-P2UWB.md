---
schema: qual/card@1
id: P-P2UWB
kind: problem
title: Approximation of measurable sets by elementary sets, and $\lim_{n\to\infty}\int_E\sin(nt)\,dt=0$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Convergence of Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 3 of the official UGA Fall 2021 exam. Part (a) is false for arbitrary infinite-measure E because an elementary finite union of bounded rectangles has finite measure; the card is corrected to m(E)<infinity, which is also the regime used in part (b).
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Recall that a set $E \subset \mathbb{R}^{d}$ is measurable if for every $c>0$ there is an open set $U \subseteq \RR^d$ such that $m^{*}(U \sm E)<\epsilon$.

a.
Prove that if $E$ is measurable and $m(E)<\infty$, then for all $\epsilon>0$ there exists an elementary set $F$ such that $m(E \Delta F)<\epsilon$. 

  Here $m(E)$ denotes the Lebesgue measure of $E$, a set $F$ is called elementary if it is a finite union of rectangles and $E \Delta F$ denotes the symmetric difference of the sets $E$ and $F$.

b.
Let $E \subset \mathbb{R}$ be a measurable set, such that $0<m(E)<\infty$. Use part (a) to show that
\[
\lim _{n \rightarrow \infty} \int_{E} \sin (n t) d t=0
\]
:::
::: {.solution}
<1>1. Approximate a finite-measure measurable set by an elementary set.
::: {.proof}
Let $E\subset\mathbb R^d$ be measurable with $m(E)<\infty$, and fix $\varepsilon>0$. By outer regularity choose an open set $U\supset E$ such that
\[
m(U\setminus E)<\varepsilon/2.
\]
Then $m(U)<\infty$.

Every open subset of $\mathbb R^d$ is a countable union of pairwise disjoint half-open rectangles (for example dyadic cubes), say
\[
U=\bigcup_{j=1}^\infty Q_j,
\qquad
m(U)=\sum_{j=1}^\infty m(Q_j).
\]
Choose $N$ so that
\[
m\!\left(U\setminus\bigcup_{j=1}^NQ_j\right)<\varepsilon/2.
\]
Let
\[
F=\bigcup_{j=1}^NQ_j.
\]
Then $F$ is elementary and
\[
E\triangle F\subset (U\setminus E)\cup(U\setminus F),
\]
so
\[
m(E\triangle F)<\varepsilon.
\]
:::

<1>2. Prove the oscillatory integral limit.
::: {.proof}
Let $E\subset\mathbb R$ be measurable with $0<m(E)<\infty$. Fix $\varepsilon>0$ and choose an elementary set $F$, a finite union of intervals, with
\[
m(E\triangle F)<\varepsilon/2.
\]
Then
\[
\left|\int_E\sin(nt)\,dt-\int_F\sin(nt)\,dt\right|
\le m(E\triangle F)<\varepsilon/2.
\]
If $F$ is the disjoint union of $N$ bounded intervals $[a_j,b_j]$, then
\[
\left|\int_F\sin(nt)\,dt\right|
\le\sum_{j=1}^N\frac{|\cos(na_j)-\cos(nb_j)|}{n}
\le\frac{2N}{n}\longrightarrow0.
\]
Hence for all sufficiently large $n$,
\[
\left|\int_E\sin(nt)\,dt\right|<\varepsilon.
\]
Therefore
\[
\boxed{\lim_{n\to\infty}\int_E\sin(nt)\,dt=0.}
\]
:::
:::
