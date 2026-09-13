---
schema: qual/card@1
id: P-ALGCOMP03-03
kind: problem
title: Fall 2003 algebra comprehensive practice problem 3
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified all three implications in the local-ring characterization and the power-series example.
---

::: {.problem}
Let A be a commutative ring with identity which is not a field.
Prove that the following conditions are equivalent.

(a) The sum of two non-invertible elements is non-invertible.

(b) The non-invertible elements form a proper ideal.

(c) The ring A possesses a unique maximal ideal.

Give an example of a ring satisfying the above conditions and describe its unique maximal ideal.
:::


::: {.solution}
Let
\[
N:=\{a\in A:a\text{ is not a unit}\}.
\]
We prove
\[
(a)\Longrightarrow(b)\Longrightarrow(c)\Longrightarrow(a).
\]

<1>1. \((a)\Rightarrow(b)\): the nonunits form a proper ideal.
::: {.proof}
Certainly \(0\in N\). If \(a\in N\), then \(-a\in N\), because if \(-a\) were invertible then so would \(a=-(-a)\). By hypothesis (a), if \(a,b\in N\), then
\[
a+b\in N.
\]
Thus \(N\) is an additive subgroup of \(A\).

Now let \(r\in A\) and \(a\in N\). If \(ra\) were a unit, say
\[
(ra)c=1,
\]
then, using commutativity,
\[
a(rc)=1,
\]
so \(a\) would be a unit, contradiction. Hence \(ra\in N\). Therefore \(N\) is an ideal.

Finally, \(1\notin N\), so \(N\ne A\). Hence \(N\) is a proper ideal.
:::

<1>2. \((b)\Rightarrow(c)\): \(A\) has a unique maximal ideal.
::: {.proof}
Assume \(N\) is a proper ideal. We first show that \(N\) is maximal. If \(I\) is an ideal properly containing \(N\), choose
\[
a\in I\setminus N.
\]
Then \(a\) is a unit. Since an ideal containing a unit is all of \(A\), we obtain
\[
I=A.
\]
Thus \(N\) is maximal.

Let \(M\) be any maximal ideal of \(A\). No element of \(M\) can be a unit, because a unit in \(M\) would imply \(1\in M\). Hence
\[
M\subseteq N.
\]
Since both \(M\) and \(N\) are maximal ideals, it follows that
\[
M=N.
\]
Therefore \(N\) is the unique maximal ideal of \(A\).
:::

<1>3. \((c)\Rightarrow(a)\): sums of nonunits are nonunits.
::: {.proof}
Let \(M\) be the unique maximal ideal, and let \(x,y\in A\) be nonunits.

Because \(x\) is not a unit, the principal ideal \((x)\) is proper. Every proper ideal of a commutative ring with identity is contained in a maximal ideal, so
\[
x\in M.
\]
Likewise,
\[
y\in M.
\]
Hence
\[
x+y\in M.
\]
Every element of a proper ideal is a nonunit, so \(x+y\) is noninvertible. This proves (a).
:::

<1>4. Example: the formal power-series ring \(k[[t]]\).
::: {.proof}
In \(k[[t]]\), a series
\[
f(t)=a_0+a_1t+a_2t^2+\cdots
\]
is a unit if and only if \(a_0\ne0\). Therefore the nonunits are exactly the series with zero constant term, namely
\[
(t)=\{tf(t):f(t)\in k[[t]]\}.
\]
Thus \(k[[t]]\) has the unique maximal ideal
\[
\boxed{(t)}.
\]
Since \((t)\ne0\), the ring is not a field, and it satisfies the three equivalent conditions.
:::
:::
