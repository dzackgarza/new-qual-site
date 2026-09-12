---
schema: qual/card@1
id: E-SS10.EX-4
kind: problem
title: "SS 10.4: Euler's recurrence for the partition function"
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
4. Using the generating formula for $p ( n )$ , prove the recurrence formula

$$
\begin{array}{r c l} p (n) & = & p (n - 1) + p (n - 2) - p (n - 5) - p (n - 7) - \dots \\ & = & \sum_ {k \neq 0} (- 1) ^ {k + 1} p \left(n - \frac {k (3 k + 1)}{2}\right), \end{array}
$$

where the right-hand side is the finite sum taken over those $k \in \mathbb { Z } , k \neq 0$ , with $k ( 3 k + 1 ) / 2 \leq n$ . Use this formula to calculate $p ( 5 ) , p ( 6 ) , p ( 7 ) , p ( 8 ) , p ( 9 )$ , and $p ( 1 0 )$ ; check that $p ( 1 0 ) = 4 2$

The next two exercises give elementary results related to the asymptotics of the partition function.
More refined statements can be found in Appendix A.
:::

::: solution
Let
\[
P(q)=\sum_{n=0}^\infty p(n)q^n
=\prod_{m=1}^\infty(1-q^m)^{-1},
\qquad p(0)=1,
\]
and set \(p(j)=0\) for \(j<0\). Euler's pentagonal-number identity is
\[
\prod_{m=1}^\infty(1-q^m)
=\sum_{k\in\mathbb Z}(-1)^k q^{k(3k+1)/2};
\]
this is the usual form with \(k(3k-1)/2\) after replacing \(k\) by \(-k\).
Multiplying by \(P(q)\) gives \(1\). Therefore, for every \(n\ge1\), the coefficient of \(q^n\) is zero:
\[
p(n)+\sum_{k\ne0}(-1)^k
p\!\left(n-\frac{k(3k+1)}2\right)=0.
\]
Hence
\[
\boxed{
p(n)=\sum_{k\ne0}(-1)^{k+1}
 p\!\left(n-\frac{k(3k+1)}2\right)}.
\]
Only finitely many terms occur because \(p(j)=0\) for \(j<0\). Ordering the generalized pentagonal numbers as
\[
1,2,5,7,12,15,\ldots
\]
gives
\[
p(n)=p(n-1)+p(n-2)-p(n-5)-p(n-7)+\cdots.
\]
Starting with \(p(0)=1\), \(p(1)=1\), \(p(2)=2\), \(p(3)=3\), \(p(4)=5\), we obtain
\[
\begin{array}{c|rrrrrr}
n&5&6&7&8&9&10\\ \hline
p(n)&7&11&15&22&30&42.
\end{array}
\]
In particular \(p(10)=42\).
:::
