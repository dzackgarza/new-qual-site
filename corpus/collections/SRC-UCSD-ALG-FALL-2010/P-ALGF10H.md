---
schema: qual/card@1
id: P-ALGF10H
kind: problem
title: "The nilpotent elements of a ring with trivial automorphism group form an ideal"
classification:
  areas:
  - algebra
  topics:
  - Ring Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 8 of the official UCSD Algebra Qualifying Examination, Fall 2010; the statement and unit hint agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified that triviality of all inner automorphisms makes every unit central; applying this to 1+n makes every nilpotent central, from which additive and two-sided ideal closure follows.
---

::: {.problem}
Let $R$ be a ring with identity such that the identity map is the only ring automorphism of $R$.
Prove that the set $N$ of all nilpotent elements of $R$ is an ideal of $R$.

Hint: $1 + n$, with $n$ a nilpotent element, is invertible.
:::


::: {.solution}
Let \(N\) denote the set of nilpotent elements of \(R\).

<1>1. Every unit of \(R\) is central.
::: {.proof}
Let \(u\in R^\times\).
Conjugation by \(u\),
\[
\iota_u:R\longrightarrow R,
\qquad
r\longmapsto uru^{-1},
\]
is a ring automorphism.
By hypothesis the identity map is the only ring automorphism of \(R\).
Hence
\[
uru^{-1}=r
\]
for every \(r\in R\), and therefore \(ur=ru\).
Thus \(u\in Z(R)\).
:::

<1>2. Every nilpotent element of \(R\) is central.
::: {.proof}
Let \(n\in N\), say \(n^m=0\).
Then
\[
(1+n)^{-1}=1-n+n^2-\cdots+(-1)^{m-1}n^{m-1},
\]
so \(1+n\) is a unit.
By <1>1, \(1+n\) is central.
Since \(1\) is central,
\[
n=(1+n)-1
\]
is central as well.
Thus
\[
N\subseteq Z(R).
\]
:::

<1>3. The set \(N\) is an additive subgroup of \(R\).
::: {.proof}
Clearly \(0\in N\), and if \(n^r=0\), then
\[
(-n)^r=(-1)^r n^r=0,
\]
so \(-n\in N\).

Let \(n,m\in N\), with
\[
n^r=0,
\qquad
m^s=0.
\]
By <1>2, \(n\) and \(m\) are central and hence commute.
Therefore the binomial theorem applies:
\[
(n+m)^{r+s-1}
=\sum_{j=0}^{r+s-1}\binom{r+s-1}{j}n^j m^{r+s-1-j}.
\]
For each term, either \(j\ge r\) or \(r+s-1-j\ge s\), so that term is zero.
Hence
\[
(n+m)^{r+s-1}=0,
\]
and \(n+m\in N\).
Thus \(N\) is an additive subgroup.
:::

<1>4. The set \(N\) absorbs multiplication from both sides by arbitrary elements of \(R\).
::: {.proof}
Let \(n\in N\), say \(n^k=0\), and let \(r\in R\).
By <1>2, \(n\) is central, so
\[
(rn)^k=r^k n^k=0.
\]
Thus \(rn\in N\).
Also \(nr=rn\), so \(nr\in N\).
:::

<1>5. Therefore \(N\) is a two-sided ideal of \(R\).
::: {.proof}
By <1>3, \(N\) is an additive subgroup, and by <1>4 it absorbs multiplication from either side by elements of \(R\).
Hence \(N\triangleleft R\).
:::
:::
