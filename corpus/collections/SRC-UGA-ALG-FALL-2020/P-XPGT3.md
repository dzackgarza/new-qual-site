---
schema: qual/card@1
id: P-XPGT3
kind: problem
title: $IM$ is a submodule, and $f$ is surjective if $I$ is nilpotent and $\overline{f}:M/IM\to
  N/IN$ is surjective
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Ideals
  - Nakayama's Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $R$ be a ring with $1$ and let $M$ be a left \(R\dash\)module.
If $I$ is a left ideal of $R$, define 
\[
IM \da \ts{ \sum_{i=1}^{N < \infty} a_i m_i \st a_i \in I, m_i \in M, n\in \NN}
,\]
i.e. the set of finite sums of of elements of the form $am$ where \( a\in I, m\in M \).

a. Prove that $IM \leq M$ is a submodule.

b. Let $M, N$ be left \(R\dash\)modules, $I$ a nilpotent left ideal of $R$, and $f: M\to N$ an \(R\dash\)module morphism.
Prove that if the induced morphism \( \bar{f}: M/IM \to N/IN \) is surjective, then $f$ is surjective.
:::

::: solution
For (a), $IM$ contains $0$ and is closed under addition by concatenating finite sums. If
\[
x=\sum_i a_i m_i\in IM
\]
and $r\in R$, then, because $I$ is a left ideal,
\[
rx=\sum_i (ra_i)m_i\in IM.
\]
Thus $IM$ is a left $R$-submodule of $M$.

For (b), surjectivity of $\bar f$ means that for every $n\in N$ there exist $m\in M$ and $u\in IN$ such that
\[
n=f(m)+u.
\]
Hence
\[
N=f(M)+IN.
\]
Let $Q=N/f(M)$. Since $f(M)$ is a submodule, $Q$ is a left $R$-module. The displayed equality says
\[
Q=IQ.
\]
Iterating,
\[
Q=I^kQ
\]
for every $k\ge1$. If $I$ is nilpotent, choose $k$ with $I^k=0$. Then
\[
Q=I^kQ=0.
\]
Therefore $N=f(M)$, so $f$ is surjective.
:::
