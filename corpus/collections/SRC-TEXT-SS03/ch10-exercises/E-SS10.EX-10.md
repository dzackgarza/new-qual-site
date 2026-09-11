---
schema: qual/card@1
id: E-SS10.EX-10
kind: problem
title: "Observe the following irregularities of the functions  and  as n becomes large:
"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Repaired a statement or hint transcription defect before solving.
---

::: exercise
10. Observe the following irregularities of the functions $r _ { 2 } ( n )$ and $r _ { 4 } ( n )$ as n becomes large:

(a) $r _ { 2 } ( n ) = 0$ for infinitely many n, while lim $\begin{array} { r } { \operatorname* { s u p } _ { n  \infty } r _ { 2 } ( n ) = \infty , } \end{array}$

(b) $r _ { 4 } ( n ) = 2 4$ for infinitely many n while lim $\begin{array} { r } { \operatorname* { s u p } _ { n \to \infty } r _ { 4 } ( n ) / n = \infty . } \end{array}$

[Hint: For (a) consider $n = 5 ^ { k }$ ; for (b) consider alternatively $n = 2 ^ { k }$ , and $n = q ^ { k }$ using products of many distinct odd primes.]
:::

::: solution
We use the formulas established in the chapter
\[
r_2(n)=4\bigl(d_1(n)-d_3(n)\bigr),
\qquad
r_4(n)=8\sum_{\substack{d\mid n\\4\nmid d}}d,
\tag{1}
\]
where \(d_j(n)\) counts divisors congruent to \(j\pmod4\).

For part (a), if \(n=3^{2k+1}\), the divisors are \(1,3,3^2,\ldots,3^{2k+1}\); exactly \(k+1\) are \(1\pmod4\) and \(k+1\) are \(3\pmod4\). Hence \(r_2(3^{2k+1})=0\), giving infinitely many zeros.

On the other hand, for \(n=5^k\), every divisor is \(1\pmod4\), so
\[
r_2(5^k)=4(k+1)\longrightarrow\infty.
\]
Thus \(\limsup r_2(n)=\infty\).

For part (b), if \(n=2^k\) with \(k\ge1\), the only divisors not divisible by \(4\) are \(1\) and \(2\). Therefore
\[
r_4(2^k)=8(1+2)=24,
\]
so the value \(24\) occurs infinitely often.

To make \(r_4(n)/n\) arbitrarily large, let
\[
n_k=p_1p_2\cdots p_k
\]
be the product of the first \(k\) odd primes. Since \(n_k\) is odd and squarefree, (1) gives
\[
\frac{r_4(n_k)}{n_k}
=8\frac{\prod_{j=1}^k(1+p_j)}{\prod_{j=1}^kp_j}
=8\prod_{j=1}^k\left(1+\frac1{p_j}\right).
\]
The product diverges: indeed \(\log(1+1/p)\ge 1/(2p)\) for \(p\ge2\), and Euler's theorem \(\sum_p1/p=\infty\) implies
\[
\sum_j\log\left(1+\frac1{p_j}\right)=\infty.
\]
Hence
\[
\limsup_{n\to\infty}\frac{r_4(n)}n=\infty.
\]
:::
