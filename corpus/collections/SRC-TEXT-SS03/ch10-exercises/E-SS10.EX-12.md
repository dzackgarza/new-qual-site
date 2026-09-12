---
schema: qual/card@1
id: E-SS10.EX-12
kind: problem
title: "Here we give another identity involving  , which is equivalent to the foursquare"
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
12. Here we give another identity involving $\theta ^ { 4 }$ , which is equivalent to the foursquares theorem.

(a) Show that for $| q | < 1$

$$
\sum_ {n = 1} ^ {\infty} \frac {n q ^ {n}}{1 - q ^ {n}} = \sum_ {n = 1} ^ {\infty} \frac {q ^ {n}}{(1 - q ^ {n}) ^ {2}}.
$$

[Hint: The left-hand side is $\sum \sigma _ { 1 } ( n ) q ^ { n }$ . Use $\textstyle x / ( 1 - x ) ^ { 2 } = \sum _ { n = 1 } ^ { \infty } n x ^ { n } . ]$

(b) Show as a result that

$$
\sum_ {n = 1} ^ {\infty} \frac {n q ^ {n}}{1 - q ^ {n}} - \sum_ {n = 1} ^ {\infty} \frac {4 n q ^ {4 n}}{1 - q ^ {4 n}} = \sum_ {n = 1} ^ {\infty} \frac {q ^ {n}}{(1 - q ^ {n}) ^ {2}} - 4 \sum_ {n = 1} ^ {\infty} \frac {q ^ {4 n}}{(1 - q ^ {4 n}) ^ {2}} = \sum \sigma_ {1} ^ {*} (n) q ^ {n}
$$

where $\sigma _ { 1 } ^ { * } ( n )$ is the sum of the divisors of n that are not divisible by 4.

(c) Show that the four-squares theorem is equivalent to the identity

$$
\theta (\tau) ^ {4} = 1 + 8 \sum_ {n = 1} ^ {\infty} \frac {q ^ {n}}{(1 + (- 1) ^ {n} q ^ {n}) ^ {2}}, \quad q = e ^ {\pi i \tau}.
$$
:::

::: solution
For \(|q|<1\), all series below converge absolutely. Using
\[
\frac{x}{(1-x)^2}=\sum_{k=1}^\infty kx^k,
\]
we get
\[
\sum_{n=1}^\infty\frac{q^n}{(1-q^n)^2}
=\sum_{n,k\ge1}kq^{nk}.
\]
Interchanging the dummy indices \(n\) and \(k\) gives
\[
\sum_{n,k\ge1}nq^{nk}
=\sum_{n=1}^\infty\frac{nq^n}{1-q^n},
\]
which proves part (a).

Let
\[
A(q)=\sum_{n=1}^\infty\frac{nq^n}{1-q^n}
=\sum_{N=1}^\infty\sigma_1(N)q^N.
\]
Then
\[
A(q)-4A(q^4)
=\sum_{N=1}^\infty
\bigl(\sigma_1(N)-4\sigma_1(N/4)\bigr)q^N,
\]
where \(\sigma_1(N/4)=0\) unless \(4\mid N\). The coefficient equals
\[
\sum_{\substack{d\mid N\\4\nmid d}}d=:\sigma_1^*(N),
\]
because the divisors of \(N\) divisible by \(4\) are exactly \(4e\) with \(e\mid N/4\). This proves the first equality in part (b); part (a), applied at \(q\) and \(q^4\), proves the second.

Now put
\[
B(q)=\sum_{n=1}^\infty
\frac{q^n}{(1+(-1)^nq^n)^2}.
\]
Split into odd and even \(n\). For even \(n=2m\),
\[
\frac{q^{2m}}{(1-q^{2m})^2}
-4\frac{q^{4m}}{(1-q^{4m})^2}
=\frac{q^{2m}}{(1+q^{2m})^2}.
\]
For odd \(n\), the summand is simply \(q^n/(1-q^n)^2\). Hence
\[
B(q)=\sum_{n=1}^\infty\frac{q^n}{(1-q^n)^2}
-4\sum_{n=1}^\infty\frac{q^{4n}}{(1-q^{4n})^2}
=\sum_{N=1}^\infty\sigma_1^*(N)q^N.
\]

Finally
\[
\theta(\tau)^4
=\sum_{N=0}^\infty r_4(N)q^N,
\qquad q=e^{\pi i\tau}.
\]
Thus Jacobi's four-squares theorem
\[
r_4(N)=8\sigma_1^*(N)\quad(N\ge1)
\]
is equivalent, coefficient by coefficient, to
\[
\boxed{\theta(\tau)^4
=1+8\sum_{n=1}^\infty
\frac{q^n}{(1+(-1)^nq^n)^2}}.
\]
:::
