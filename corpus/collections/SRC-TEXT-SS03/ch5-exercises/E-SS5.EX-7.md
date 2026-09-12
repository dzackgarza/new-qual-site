---
schema: qual/card@1
id: E-SS5.EX-7
kind: problem
title: "SS 5.7: Convergence criteria and counterexamples for infinite products"
classification:
  areas:
  - complex-analysis
  topics: ['Entire Functions', 'Hadamard Factorization', "Jensen's Formula"]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Split this exercise from source bleed in E-SS5.EX-6 and added the necessary exclusion of zero factors in part (a).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
7. Establish the following properties of infinite products.

(a) Suppose $a_n\neq -1$ for every $n$. Show that if $\sum |a_n|^2$ converges, then the product $\prod (1+a_n)$ converges to a non-zero limit if and only if $\sum a_n$ converges.

(b) Find an example of a sequence of complex numbers $\{a_n\}$ such that $\sum a_n$ converges but $\prod(1+a_n)$ diverges.

(c) Also find an example such that $\prod(1+a_n)$ converges to a non-zero limit and $\sum a_n$ diverges.
:::

::: solution
For part (a), because $\sum |a_n|^2<\infty$, we have $a_n\to0$. Hence for all sufficiently large $n$, say $|a_n|\le1/2$, we may use the principal logarithm and the expansion
\[
\log(1+a_n)=a_n+O(|a_n|^2),
\tag{1}
\]
with an absolute implied constant. Since $a_n\ne-1$, no factor vanishes.

The tail product $\prod(1+a_n)$ converges to a nonzero limit if and only if the series
\[
\sum \log(1+a_n)
\]
converges. By (1), the difference between this logarithmic series and $\sum a_n$ is absolutely convergent because $\sum|a_n|^2<\infty$. Therefore
\[
\prod(1+a_n)\text{ converges to a nonzero limit}
\iff \sum a_n\text{ converges}.
\]

For part (b), take
\[
a_n=\frac{(-1)^n}{\sqrt n}.
\]
The series $\sum a_n$ converges by the alternating-series test. On the other hand,
\[
\log(1+a_n)=a_n-\frac{a_n^2}{2}+O(|a_n|^3).
\]
The series $\sum a_n$ converges and $\sum |a_n|^3$ converges, but
\[
\sum a_n^2=\sum\frac1n=\infty.
\]
Hence
\[
\sum_{n=1}^N\log(1+a_n)\longrightarrow-\infty,
\]
so the partial products tend to $0$. Thus the infinite product does not converge to a nonzero limit.

For part (c), let
\[
b_n=\frac{(-1)^n}{\sqrt n},
\qquad
a_n=e^{b_n}-1.
\]
Then
\[
1+a_n=e^{b_n},
\]
so
\[
\prod_{n=1}^N(1+a_n)
=\exp\!\left(\sum_{n=1}^N b_n\right)
\]
converges to a nonzero limit because $\sum b_n$ converges. But
\[
a_n=b_n+\frac{b_n^2}{2}+O(|b_n|^3).
\]
Again $\sum b_n$ and $\sum|b_n|^3$ converge, while
\[
\frac12\sum b_n^2=\frac12\sum\frac1n
\]
diverges to $+\infty$. Therefore $\sum a_n$ diverges.
:::
