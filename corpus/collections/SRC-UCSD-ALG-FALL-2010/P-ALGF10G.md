---
schema: qual/card@1
id: P-ALGF10G
kind: problem
title: "A maximal non-finitely generated ideal in a commutative ring is prime"
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
  date: 2026-09-07
  note: Checked against Question 7 of the official UCSD Algebra Qualifying Examination, Fall 2010; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the colon-ideal argument showing that failure of primality would force the maximal non-finitely generated ideal itself to be finitely generated.
---

::: {.problem}
Let $R$ be a commutative ring with identity and let $U$ be maximal among non-finitely generated ideals of $R$.
Prove $U$ is a prime ideal.
:::


::: {.solution}
Let \(U\) be maximal, under inclusion, among the non-finitely generated ideals of \(R\).

<1>1. The ideal \(U\) is proper.
::: {.proof}
The unit ideal \(R=(1)\) is finitely generated.
Since \(U\) is not finitely generated, \(U\neq R\).
:::

<1>2. If \(a\notin U\), then the ideal \(U+(a)\) is finitely generated.
::: {.proof}
The inclusion
\[
U\subsetneq U+(a)
\]
is strict because \(a\notin U\).
By maximality of \(U\) among non-finitely generated ideals, every ideal strictly containing \(U\) is finitely generated.
Hence \(U+(a)\) is finitely generated.
:::

<1>3. If \(a,b\notin U\) and \(ab\in U\), then the colon ideal
\[
(U:a):=\{r\in R:ra\in U\}
\]
is finitely generated.
::: {.proof}
Clearly
\[
U\subseteq (U:a).
\]
Because \(ab\in U\), one has
\[
b\in(U:a).
\]
But \(b\notin U\), so the inclusion is strict:
\[
U\subsetneq(U:a).
\]
By maximality of \(U\), the ideal \((U:a)\) is finitely generated.
:::

<1>4. The situation in <1>3 would force \(U\) to be finitely generated.
::: {.proof}
By <1>2, \(U+(a)\) is finitely generated.
Choose generators \(c_1,\ldots,c_m\).
Write
\[
c_i=u_i+r_i a
\qquad
(u_i\in U,\ r_i\in R).
\]
Then
\[
U+(a)=(u_1,\ldots,u_m,a).
\]
Indeed, each \(c_i\) lies in the ideal on the right, while each \(u_i=c_i-r_i a\) lies in \(U+(a)\).

By <1>3, write
\[
(U:a)=(t_1,\ldots,t_s).
\]
For each \(j\),
\[
t_j a\in U.
\]
We claim that
\[
U=(u_1,\ldots,u_m,t_1a,\ldots,t_sa).
\]
The right-hand side is contained in \(U\).
Conversely, let \(x\in U\).
Since \(x\in U+(a)\), we can write
\[
x=\sum_i q_i u_i+ra.
\]
Then
\[
ra=x-\sum_i q_i u_i\in U,
\]
so \(r\in(U:a)\).
Write \(r=\sum_j v_jt_j\).
Therefore
\[
x=\sum_i q_i u_i+\sum_j v_j(t_ja),
\]
which proves the claim.
Thus \(U\) would be finitely generated, contradicting its definition.
:::

<1>5. Therefore \(U\) is prime.
::: {.proof}
Suppose \(ab\in U\).
If both \(a\notin U\) and \(b\notin U\), then <1>3 and <1>4 give a contradiction.
Hence
\[
a\in U\quad\text{or}\quad b\in U.
\]
Together with <1>1, this is exactly the definition that \(U\) is prime.
:::
:::
