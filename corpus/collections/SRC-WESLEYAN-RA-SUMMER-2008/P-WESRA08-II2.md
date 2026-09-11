---
schema: qual/card@1
id: P-WESRA08-II2
kind: problem
title: Almost-everywhere and L1 convergence need not imply each other
classification:
  areas: [real-analysis]
  topics: [L1 Convergence, Almost Everywhere Convergence, Counterexamples]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 2 of the Wesleyan Real Analysis Preliminary Examination, July 8, 2008, in analysis_2008-2013.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Give examples showing that neither of the following implications holds in general on $[0,1]$:

1. convergence almost everywhere to $0$ implies convergence to $0$ in $L^1$;
2. convergence to $0$ in $L^1$ implies convergence almost everywhere to $0$.
:::

::: solution
<1>1. Almost-everywhere convergence need not imply $L^1$ convergence.
::: proof
Let
\[
f_n(x):=n\mathbf1_{(0,1/n)}(x).
\]
For every $x>0$, eventually $x\notin(0,1/n)$, so $f_n(x)\to0$; also $f_n(0)=0$. Thus $f_n\to0$ everywhere.

However,
\[
\|f_n\|_1
=n\,m((0,1/n))
=1
\]
for every $n$. Hence $f_n$ does not converge to $0$ in $L^1$.
:::

<1>2. $L^1$ convergence need not imply almost-everywhere convergence.
::: proof
Use the typewriter sequence. For $m\ge0$ and $0\le k<2^m$, define
\[
h_{2^m+k}(x)
:=\mathbf1_{[k2^{-m},(k+1)2^{-m})}(x),
\qquad x\in[0,1),
\]
and set $h_n(1)=0$.

If $2^m\le n<2^{m+1}$, then
\[
\|h_n\|_1=2^{-m}\longrightarrow0.
\]
Thus $h_n\to0$ in $L^1([0,1])$.

On the other hand, for every $x\in[0,1)$ and every level $m$, exactly one of the $2^m$ functions in that level equals $1$ at $x$. Hence $h_n(x)=1$ infinitely often. It also equals $0$ infinitely often, so $h_n(x)$ does not converge at any $x\in[0,1)$. In particular it does not converge almost everywhere to $0$.
:::
:::
