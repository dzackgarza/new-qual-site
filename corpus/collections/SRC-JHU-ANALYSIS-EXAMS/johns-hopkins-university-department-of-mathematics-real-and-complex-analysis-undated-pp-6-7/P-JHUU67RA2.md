---
schema: qual/card@1
id: P-JHUU67RA2
kind: problem
title: 'Weak convergence plus norm convergence implies strong convergence in $L^2$'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against entry 2 of the undated JHU Real and Complex Analysis exam on pp. 6–7 of the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $L^2=L^2(\mathbb R^d)$ be the real Hilbert space with inner product
\[
(f,g)=\int_{\mathbb R^d}f g\,dm.
\]

(a) Prove that if $f_n\rightharpoonup f$ weakly in $L^2$ and
\[
\|f_n\|_2\to\|f\|_2,
\]
then $f_n\to f$ strongly in $L^2$.

(b) Give a sequence of bounded functions in $L^2$ which converges weakly along a subsequence but not strongly. What does this imply about the unit ball of $L^2$ in the norm topology?
:::

::: {.solution}
<1>1. Weak convergence plus convergence of norms implies strong convergence.
::: {.proof}
Weak convergence gives, taking the test function $g=f$,
\[
(f_n,f)\longrightarrow(f,f)=\|f\|_2^2.
\]
Therefore
\[
\begin{aligned}
\|f_n-f\|_2^2
&=\|f_n\|_2^2+\|f\|_2^2-2(f_n,f)\\
&\longrightarrow
\|f\|_2^2+\|f\|_2^2-2\|f\|_2^2=0.
\end{aligned}
\]
Hence $f_n\to f$ strongly in $L^2$.
:::

<1>2. A bounded weakly convergent sequence need not converge strongly.
::: {.proof}
For $n\ge1$, let
\[
Q_n=[n,n+1]\times[0,1]^{d-1}
\]
and define
\[
e_n=\chi_{Q_n}.
\]
Then each $e_n$ is bounded by $1$ and
\[
\|e_n\|_2=1.
\]
The sets $Q_n$ are pairwise disjoint, so $(e_n)$ is an orthonormal sequence. Hence for every $g\in L^2$,
\[
(e_n,g)\to0
\]
by Bessel's inequality. Thus
\[
e_n\rightharpoonup0.
\]
But
\[
\|e_n-0\|_2=1
\]
for every $n$, so the sequence does not converge strongly. In fact, for $m\ne n$,
\[
\|e_n-e_m\|_2=\sqrt2,
\]
so no subsequence is strongly Cauchy.

Therefore the closed unit ball of $L^2(\mathbb R^d)$ is not compact in the norm topology.
:::
:::
