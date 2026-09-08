---
schema: qual/card@1
id: P-ALGS08F
kind: problem
title: "Polynomial ring with constant coefficients in a subfield is Noetherian iff the extension is finite"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 6 of the official UCSD Spring 2008 algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: "Verified both directions: finite [L:K] gives a finite-type K-algebra, while finite generation of xL[x] forces finitely many x-coefficients to span L over K."
---

::: problem
If $K$ is a subfield of $L$, show that the ring $S$ of all polynomials over $L$ with constant coefficient in $K$ is Noetherian if and only if $L$ is finite-dimensional over $K$.
:::

::: {.solution}
Write
\[
S=K+xL[x]
=\{a_0+a_1x+\cdots+a_nx^n: a_0\in K,\ a_i\in L\text{ for }i\ge1\}.
\]

<1>1. If $[L:K]<\infty$, then $S$ is Noetherian.
::: {.proof}
Choose a $K$-basis
\[
1=b_1,b_2,\ldots,b_r
\]
of $L$.
Then
\[
S=K[x,b_2x,\ldots,b_rx].
\]
Indeed, every positive-degree coefficient $a_d\in L$ can be written as
\[
a_d=\sum_{i=1}^r c_{id}b_i,
\qquad c_{id}\in K,
\]
so
\[
a_dx^d
=c_{1d}x^d+\sum_{i=2}^r c_{id}(b_ix)x^{d-1}.
\]
Thus $S$ is a finitely generated $K$-algebra.
Since $K$ is Noetherian, Hilbert's basis theorem implies that $S$ is Noetherian.
:::

<1>2. If $S$ is Noetherian, then $[L:K]<\infty$.
::: {.proof}
Consider the ideal
\[
I=xL[x]\subseteq S.
\]
Since $S$ is Noetherian, there exist $f_1,\ldots,f_r\in I$ such that
\[
I=(f_1,\ldots,f_r)_S.
\]
Write
\[
f_j=c_jx+\text{terms of degree at least }2,
\qquad c_j\in L.
\]
Let $a\in L$.
Since $ax\in I$, there exist $s_j\in S$ with
\[
ax=\sum_{j=1}^r s_jf_j.
\]
Every $s_j$ has constant term in $K$.
Comparing coefficients of $x$ on both sides gives
\[
a\in Kc_1+\cdots+Kc_r.
\]
Since $a\in L$ was arbitrary,
\[
L=Kc_1+\cdots+Kc_r.
\]
Therefore $L$ is finite-dimensional over $K$.
:::

<1>3. Hence $S$ is Noetherian if and only if $L/K$ is finite.
::: {.proof}
Combine <1>1 and <1>2.
:::
:::
