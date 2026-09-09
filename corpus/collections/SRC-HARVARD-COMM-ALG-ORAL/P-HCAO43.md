---
schema: qual/card@1
id: P-HCAO43
kind: problem
title: Localization of annihilators
classification:
  areas:
  - algebra
  topics:
  - Localization
  - Annihilators
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $M$ be an $A$-module, and let $S\subseteq A$ be a multiplicative set.
Must
\[
S^{-1}\operatorname{Ann}_A(M)
=
\operatorname{Ann}_{S^{-1}A}(S^{-1}M)
\]
hold?
Prove the equality or give a counterexample.
What changes if $M$ is finitely generated?
:::

::: solution
There is always an inclusion
\[
S^{-1}\operatorname{Ann}_A(M)
\subseteq
\operatorname{Ann}_{S^{-1}A}(S^{-1}M),
\]
but equality can fail for infinitely generated $M$. It holds when $M$ is
finitely generated.

<1>1. The inclusion always holds.
::: proof
If $a\in\operatorname{Ann}_A(M)$, then $am=0$ for every $m\in M$. Hence for
every $s,t\in S$,
\[
\frac as\frac mt=\frac{am}{st}=0
\]
in $S^{-1}M$.
:::

<1>2. Equality can fail without finite generation.
::: proof
Take
\[
A=\mathbb Z,
\qquad
S=\{1,2,2^2,\ldots\},
\qquad
M=\bigoplus_{n\ge1}\mathbb Z/2^n\mathbb Z.
\]
Every element of $M$ is killed by some power of $2$, so $S^{-1}M=0$. Thus
\[
\operatorname{Ann}_{S^{-1}A}(S^{-1}M)=S^{-1}A=\mathbb Z[1/2].
\]
On the other hand, no nonzero integer annihilates every summand
$\mathbb Z/2^n\mathbb Z$, so $\operatorname{Ann}_A(M)=0$. Hence its localization
is zero.
:::

<1>3. If $M$ is finitely generated, equality holds.
::: proof
Let $m_1,\ldots,m_r$ generate $M$, and suppose
$a/s\in S^{-1}A$ annihilates $S^{-1}M$. For each $i$,
\[
\frac a1\frac{m_i}1=0,
\]
so there exists $t_i\in S$ with $t_i a m_i=0$ in $M$. Put
$t=t_1\cdots t_r\in S$. Then $ta$ kills every generator and hence all of
$M$, so $ta\in\operatorname{Ann}_A(M)$. But
\[
\frac as=\frac{ta}{ts}
\]
lies in $S^{-1}\operatorname{Ann}_A(M)$.
:::
:::
