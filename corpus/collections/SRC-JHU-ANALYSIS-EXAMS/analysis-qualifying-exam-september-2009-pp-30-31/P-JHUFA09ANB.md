---
schema: qual/card@1
id: P-JHUFA09ANB
kind: problem
title: 'Bilinear forms with polynomially weighted coefficients on $\ell^2$'
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the JHU Analysis Qualifying Exam, September 2009, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
For which $\sigma\in\RR$ does there exist $C_\sigma<\infty$ such that
$$
\abs{\sum_{j,k=1}^\infty (1+\abs{j-k})^\sigma a_jb_k}
\le C_\sigma\norm{a}_{\ell^2}\norm{b}_{\ell^2}
$$
for all $a,b\in\ell^2$?
:::

::: {.solution}
The estimate holds exactly when
$$
\boxed{\sigma<-1}.
$$

::: pf

::: pf-step

Sufficiency for $\sigma<-1$.

::: pf-proof

Set
$$
K_{jk}=(1+\abs{j-k})^\sigma.
$$
If $\sigma<-1$, then
$$
M:=1+2\sum_{m=1}^\infty(1+m)^\sigma<\infty.
$$
For every $j$,
$$
\sum_{k=1}^\infty K_{jk}\le M,
$$
and similarly every column sum is at most $M$. By Schur's test, the operator
$$
(Tb)_j=\sum_{k=1}^\infty K_{jk}b_k
$$
is bounded on $\ell^2$ with $\norm{T}\le M$. Therefore
$$
\abs{\sum_{j,k}K_{jk}a_jb_k}
=\abs{\langle a,Tb\rangle}
\le M\norm{a}_2\norm{b}_2.
$$

:::

:::

::: pf-step

Necessity.

::: pf-proof

For $N\ge1$, let
$$
a_j=b_j=\begin{cases}N^{-1/2},&1\le j\le N,\\0,&j>N.\end{cases}
$$
Then $\norm{a}_2=\norm{b}_2=1$, while the bilinear form equals
$$
S_N=\frac1N\sum_{j,k=1}^N(1+\abs{j-k})^\sigma
=1+\frac2N\sum_{m=1}^{N-1}(N-m)(1+m)^\sigma.
$$
For $1\le m\le N/2$, one has $N-m\ge N/2$, hence
$$
S_N\ge \sum_{m=1}^{\lfloor N/2\rfloor}(1+m)^\sigma.
$$
If $\sigma=-1$, the right-hand side grows like $\log N$. If $\sigma>-1$, it grows on the order of $N^{\sigma+1}$. Thus $S_N\to\infty$ whenever $\sigma\ge-1$. No uniform constant $C_\sigma$ can then exist.

Hence the estimate holds exactly for $\sigma<-1$.

:::

:::

:::

:::
