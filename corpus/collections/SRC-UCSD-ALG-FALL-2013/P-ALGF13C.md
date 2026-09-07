---
schema: qual/card@1
id: P-ALGF13C
kind: problem
title: Ideals contain a product of primes; finitely many minimal primes
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 3 of the official UCSD Algebra Qualifying Exam, Fall 2013; both parts and the hint agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the maximal-counterexample proof for products of prime ideals and the deduction that every minimal prime is one of finitely many prime factors lying over the zero ideal.
---

::: {.problem}
Let $A$ be a commutative noetherian ring.

(a) Show that every ideal $I$ of $A$ contains a finite product $P_1 P_2 \cdots P_k$ for some $k$, where the $P_i$ are (not necessarily distinct) prime ideals.
(Hint: Consider the set of ideals which do not satisfy this property.)

(b) Show that $A$ has only finitely many minimal prime ideals.
:::

::: {.solution}
<1>1. Every ideal of \(A\) contains a finite product of prime ideals.
::: {.proof}
Call an ideal \(I\subseteq A\) good if there exist prime ideals \(P_1,\ldots,P_k\) such that
\[
P_1P_2\cdots P_k\subseteq I.
\]
Suppose, toward a contradiction, that some ideal is not good.
Because \(A\) is Noetherian, the set of non-good ideals has a maximal element \(I\) under inclusion.

The ideal \(I\) is not prime.
Indeed, if it were prime, then the one-factor product \(I\) itself would be contained in \(I\), making \(I\) good.
Hence there exist \(a,b\notin I\) such that
\[
ab\in I.
\]

Both ideals
\[
I+(a)
\qquad\text{and}\qquad
(I:a):=\{r\in A:ra\in I\}
\]
strictly contain \(I\): the first contains \(a\notin I\), while the second contains \(b\notin I\) because \(ba\in I\).
By maximality of \(I\), both larger ideals are good.
Thus there are prime ideals \(P_1,\ldots,P_r\) and \(Q_1,\ldots,Q_s\) such that
\[
P_1\cdots P_r\subseteq I+(a)
\]
and
\[
Q_1\cdots Q_s\subseteq (I:a).
\]
Set
\[
P:=P_1\cdots P_r,
\qquad
Q:=Q_1\cdots Q_s.
\]
For any \(p\in P\) and \(q\in Q\), write
\[
p=i+ac
\qquad(i\in I,\ c\in A).
\]
Since \(q\in(I:a)\), one has \(aq\in I\), and therefore
\[
pq=iq+c(aq)\in I.
\]
Hence
\[
PQ=P_1\cdots P_rQ_1\cdots Q_s\subseteq I,
\]
so \(I\) is good, a contradiction.
Therefore every ideal is good.
:::

<1>2. The zero ideal contains a finite product of prime ideals.
::: {.proof}
Apply <1>1 to \(I=(0)\).
There exist prime ideals \(P_1,\ldots,P_k\) such that
\[
P_1P_2\cdots P_k=(0).
\]
:::

<1>3. Every minimal prime of \(A\) is equal to one of the primes \(P_i\) from <1>2.
::: {.proof}
Let \(\mathfrak p\) be a minimal prime ideal of \(A\).
By <1>2,
\[
P_1P_2\cdots P_k\subseteq\mathfrak p.
\]
Since \(\mathfrak p\) is prime, repeated application of primality shows that
\[
P_i\subseteq\mathfrak p
\]
for some \(i\).
But \(P_i\) is itself a prime ideal containing \((0)\).
Minimality of \(\mathfrak p\) among prime ideals containing \((0)\) therefore forces
\[
P_i=\mathfrak p.
\]
:::

<1>4. Hence \(A\) has only finitely many minimal prime ideals.
::: {.proof}
By <1>3, every minimal prime belongs to the finite set
\[
\{P_1,\ldots,P_k\}.
\]
Thus there are only finitely many minimal primes.
:::
:::
