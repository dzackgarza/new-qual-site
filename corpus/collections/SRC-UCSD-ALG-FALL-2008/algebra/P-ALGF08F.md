---
schema: qual/card@1
id: P-ALGF08F
kind: problem
title: "Prime ideal disjoint from the set of non-zero-divisors"
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
  note: Checked against Question 6 of the official UCSD Algebra Qualifying Examination, Fall 2008; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified multiplicative closure of the non-zero-divisors, the Zorn maximality argument for ideals disjoint from S, and the standard product expansion proving the maximal disjoint ideal is prime.
---

::: {.problem}
Let $R$ be a commutative ring with identity and $S$ the set of non-zero-divisors of $R$.
Using Zorn's Lemma, show that there is a prime ideal of $R$ that intersects $S$ trivially.
:::

::: {.solution}
Assume the standard convention that a ring with identity has \(1\neq0\). Let
\[
S:=\{s\in R: sx=0\Longrightarrow x=0\}.
\]

<1>1. The set \(S\) is multiplicatively closed and contains \(1\), but not \(0\).
::: {.proof}
Clearly \(1\in S\), and \(0\notin S\) because \(0\cdot1=0\) with \(1\neq0\). If \(s,t\in S\) and
\[
stx=0,
\]
then, since \(s\) is a non-zero-divisor,
\[
tx=0.
\]
Since \(t\) is also a non-zero-divisor, \(x=0\). Thus \(st\in S\).
:::

<1>2. There is an ideal \(P\subseteq R\) maximal among the ideals disjoint from \(S\).
::: {.proof}
Let
\[
\mathcal C:=\{I\triangleleft R:I\cap S=\varnothing\},
\]
ordered by inclusion.
Since \(0\notin S\), the zero ideal belongs to \(\mathcal C\), so the family is nonempty.

Let \(\{I_\lambda\}\) be a chain in \(\mathcal C\), and set
\[
I:=\bigcup_\lambda I_\lambda.
\]
Because the \(I_\lambda\) form a chain, \(I\) is an ideal.
If \(I\cap S\neq\varnothing\), choose
\[
s\in I\cap S.
\]
Then \(s\in I_\lambda\) for some \(\lambda\), contradicting
\[
I_\lambda\cap S=\varnothing.
\]
Thus \(I\in\mathcal C\), so every chain has an upper bound in \(\mathcal C\). By Zorn's lemma, \(\mathcal C\) has a maximal element \(P\).
:::

<1>3. The ideal \(P\) is prime.
::: {.proof}
Because \(1\in S\) and \(P\cap S=\varnothing\), one has \(1\notin P\), so \(P\neq R\).

Suppose
\[
ab\in P
\]
and, toward a contradiction,
\[
a\notin P,
\qquad
b\notin P.
\]
Then the ideals
\[
P+(a)
\qquad\text{and}\qquad
P+(b)
\]
properly contain \(P\). By maximality of \(P\) in \(\mathcal C\), neither larger ideal can be disjoint from \(S\). Hence there exist
\[
s\in (P+(a))\cap S,
\qquad
t\in (P+(b))\cap S.
\]
Write
\[
s=p_1+ra,
\qquad
t=p_2+ub
\]
with \(p_1,p_2\in P\) and \(r,u\in R\). Since \(S\) is multiplicatively closed,
\[
st\in S.
\]
But
\[
st
=p_1p_2+p_1ub+p_2ra+ruab.
\]
Every term on the right lies in \(P\): the first three because \(p_1,p_2\in P\), and the last because \(ab\in P\). Thus
\[
st\in P\cap S,
\]
contradicting \(P\cap S=\varnothing\). Therefore \(a\in P\) or \(b\in P\), and \(P\) is prime.
:::

<1>4. Hence \(R\) has a prime ideal disjoint from all non-zero-divisors.
::: {.proof}
The ideal \(P\) from <1>2 is prime by <1>3 and satisfies
\[
P\cap S=\varnothing
\]
by construction.
:::
:::
