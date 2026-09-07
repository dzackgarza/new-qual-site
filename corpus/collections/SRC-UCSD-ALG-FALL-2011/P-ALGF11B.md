---
schema: qual/card@1
id: P-ALGF11B
kind: problem
title: Number of commuting ordered pairs in $S_n$
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 2 of the official UCSD Algebra Qualifying Exam, Fall 2011; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the centralizer sum and the bijection between conjugacy classes of S_n and partitions of n, giving n! p(n) commuting ordered pairs.
---

::: {.problem}
Let $n \geq 3$ be an integer.
Calculate the number of ordered pairs of permutations $(\sigma, \tau)$ in the symmetric group $S_n$ such that $\sigma\tau = \tau\sigma$.
Your answer should be a simple formula involving known functions of $n$.
:::


::: {.solution}
Let
\[
N_n:=\#\{(\sigma,\tau)\in S_n\times S_n:\sigma\tau=\tau\sigma\}.
\]
We will prove
\[
N_n=n!\,p(n),
\]
where \(p(n)\) is the partition function, i.e. the number of partitions of \(n\).

<1>1. For a fixed \(\sigma\in S_n\), the number of \(\tau\in S_n\) commuting with \(\sigma\) is \(|C_{S_n}(\sigma)|\).
::: {.proof}
By definition,
\[
C_{S_n}(\sigma)
=\{\tau\in S_n:\tau\sigma=\sigma\tau\}.
\]
Hence the number of possible second coordinates \(\tau\) for a fixed first coordinate \(\sigma\) is exactly the size of this centralizer.
Therefore
\[
N_n=\sum_{\sigma\in S_n}|C_{S_n}(\sigma)|.
\]
:::

<1>2. Each conjugacy class of \(S_n\) contributes exactly \(n!\) to the sum in <1>1.
::: {.proof}
Let \(\mathcal C\) be the conjugacy class of \(\sigma\).
The orbit-stabilizer theorem for the conjugation action gives
\[
|\mathcal C|=[S_n:C_{S_n}(\sigma)]
=\frac{n!}{|C_{S_n}(\sigma)|}.
\]
Centralizer size is constant on a conjugacy class.
Hence the contribution of all elements of \(\mathcal C\) to the sum is
\[
|\mathcal C|\,|C_{S_n}(\sigma)|
=\frac{n!}{|C_{S_n}(\sigma)|}|C_{S_n}(\sigma)|
=n!.
\]
:::

<1>3. The number of conjugacy classes in \(S_n\) is \(p(n)\).
::: {.proof}
Two permutations in \(S_n\) are conjugate if and only if they have the same cycle type.
A cycle type is specified by positive integers
\[
1^{m_1}2^{m_2}\cdots n^{m_n}
\]
with
\[
\sum_{j=1}^n j m_j=n.
\]
Such data are exactly partitions of \(n\): the part \(j\) occurs \(m_j\) times.
Thus the conjugacy classes of \(S_n\) are in bijection with the partitions of \(n\), and their number is \(p(n)\).
:::

<1>4. Therefore
\[
N_n=n!\,p(n).
\]
::: {.proof}
By <1>2, every conjugacy class contributes \(n!\) commuting ordered pairs to the centralizer sum, and by <1>3 there are \(p(n)\) conjugacy classes.
Hence
\[
N_n=n!\,p(n).
\]
:::
:::
