---
schema: qual/card@1
id: P-ALGF14C
kind: problem
title: Product of primes equals zero in a Noetherian ring
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
  note: Checked against Problem 3 of the official UCSD Algebra Qualifying Exam, Fall 2014; the statement and hint agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the maximal-counterexample argument showing every ideal contains a finite product of prime ideals, then applied it to the zero ideal.
---

::: {.problem}
Let $A$ be a Noetherian unital commutative ring.
Prove that there is a finite collection of prime ideals $\mathfrak{p}_1, \ldots, \mathfrak{p}_n$ such that
\[
\mathfrak{p}_1 \cdots \mathfrak{p}_n = (0).
\]
(Hint: consider the set of all ideals of $A$ which do not contain a finite product of prime ideals.)
:::


::: {.solution}
Call an ideal \(I\subseteq A\) **good** if there exist prime ideals
\[
\mathfrak p_1,\ldots,\mathfrak p_r
\]
such that
\[
\mathfrak p_1\cdots\mathfrak p_r\subseteq I.
\]
We show that every ideal is good.

<1>1. If some ideal is not good, then there is a maximal non-good ideal.
::: {.proof}
Because \(A\) is Noetherian, every ascending chain of ideals stabilizes.
Therefore every nonempty collection of ideals has a maximal element under inclusion.
If non-good ideals exist, choose one maximal among them and call it \(I\).
:::

<1>2. The maximal non-good ideal \(I\) is not prime.
::: {.proof}
If \(I\) were prime, then the one-factor product
\[
I
\]
would itself be a product of prime ideals contained in \(I\).
Thus \(I\) would be good, contrary to its choice.
Hence \(I\) is not prime.
:::

<1>3. The existence of a maximal non-good ideal gives a contradiction.
::: {.proof}
By <1>2, choose
\[
a,b\notin I
\qquad\text{with}\qquad
ab\in I.
\]
Then both
\[
I+(a)
\]
and the colon ideal
\[
(I:a):=\{r\in A:ra\in I\}
\]
strictly contain \(I\): the first contains \(a\notin I\), while the second contains \(b\notin I\).
By maximality of \(I\), both larger ideals are good.
Thus there are prime ideals
\[
\mathfrak p_1,\ldots,\mathfrak p_r,
\qquad
\mathfrak q_1,\ldots,\mathfrak q_s
\]
such that
\[
P:=\mathfrak p_1\cdots\mathfrak p_r\subseteq I+(a)
\]
and
\[
Q:=\mathfrak q_1\cdots\mathfrak q_s\subseteq(I:a).
\]

We claim that
\[
PQ\subseteq I.
\]
Indeed, let \(p\in P\) and \(q\in Q\).
Because \(p\in I+(a)\), write
\[
p=i+ac
\qquad(i\in I,\ c\in A).
\]
Because \(q\in(I:a)\), one has \(aq\in I\).
Hence
\[
pq=iq+c(aq)\in I.
\]
Therefore
\[
\mathfrak p_1\cdots\mathfrak p_r
\mathfrak q_1\cdots\mathfrak q_s
\subseteq I,
\]
so \(I\) is good, a contradiction.
Thus no non-good ideal exists.
:::

<1>4. There are prime ideals \(\mathfrak p_1,\ldots,\mathfrak p_n\) whose product is the zero ideal.
::: {.proof}
By <1>3, every ideal of \(A\) is good.
Apply this to the zero ideal.
There exist prime ideals \(\mathfrak p_1,\ldots,\mathfrak p_n\) such that
\[
\mathfrak p_1\cdots\mathfrak p_n\subseteq(0).
\]
An ideal contained in the zero ideal is the zero ideal itself, so
\[
\mathfrak p_1\cdots\mathfrak p_n=(0).
\]
:::
:::
