---
schema: qual/card@1
id: E-SS10.EX-9
kind: problem
title: "SS 10.9: The two-squares theorem via the representation count r2(n)"
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
---

::: exercise
9. Use the formula for $r _ { 2 } ( n )$ to prove the following:

(a) If $n = p ,$ where p is a prime of the form $4 k + 1$ , then $r _ { 2 } ( n ) = 8$ . This implies that n can be written in a unique way as $n = n _ { 1 } ^ { 2 } + n _ { 2 } ^ { 2 }$ , except for the signs and reordering of $n _ { 1 }$ and $n _ { 2 }$ .

(b) If $n = q ^ { a }$ , where q is prime of the form $4 k + 3$ and a is a positive integer, then $r _ { 2 } ( n ) > 0$ if and only if a is even.

(c) In general, n can be represented as the sum of two squares if and only if all the primes of the form $4 k + 3$ that arise in the prime decomposition of n occur with even exponents.
:::

::: solution
Use the formula
\[
r_2(n)=4\bigl(d_1(n)-d_3(n)\bigr),
\tag{1}
\]
where \(d_j(n)\) is the number of positive divisors of \(n\) congruent to \(j\pmod4\).

If \(p\equiv1\pmod4\) is prime, its divisors are \(1,p\), both congruent to \(1\pmod4\). Thus
\[
r_2(p)=4(2-0)=8.
\]
For such an odd prime no representation can have a zero coordinate or two coordinates of equal absolute value. Therefore the eight sign-and-order variants come from one unordered pair of positive absolute values, proving uniqueness up to signs and reordering.

If \(q\equiv3\pmod4\) is prime, the divisors of \(q^a\) are \(1,q,\ldots,q^a\), and \(q^j\equiv(-1)^j\pmod4\). Hence
\[
d_1(q^a)-d_3(q^a)=
\begin{cases}
1,&a\text{ even},\\
0,&a\text{ odd}.
\end{cases}
\]
Thus \(r_2(q^a)>0\) exactly when \(a\) is even.

For the general case, let \(\chi\) be the nontrivial character modulo \(4\), extended by \(\chi(d)=0\) for even \(d\). Then
\[
d_1(n)-d_3(n)=\sum_{d\mid n}\chi(d).
\]
The divisor sum of a multiplicative function is multiplicative. Write
\[
n=2^e\prod_i p_i^{\alpha_i}\prod_j q_j^{\beta_j},
\]
where \(p_i\equiv1\pmod4\) and \(q_j\equiv3\pmod4\). Then
\[
\sum_{d\mid n}\chi(d)
=\prod_i(\alpha_i+1)
\prod_j\left(1-1+1-\cdots+(-1)^{\beta_j}\right).
\]
The second factor is \(1\) when \(\beta_j\) is even and \(0\) when \(\beta_j\) is odd. By (1), \(r_2(n)>0\) exactly when every prime \(q\equiv3\pmod4\) occurs with even exponent. This is precisely the two-squares criterion.
:::
