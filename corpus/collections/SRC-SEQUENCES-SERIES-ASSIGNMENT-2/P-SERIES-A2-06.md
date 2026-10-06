---
schema: qual/card@1
id: P-SERIES-A2-06
kind: problem
title: Convergence of the Kempner series omitting the digit 0
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $S=\{n_1,n_2,\ldots\}$ be the set of positive integers whose decimal representations contain no digit $0$. Show that
\[
\sum_{k=1}^\infty \frac1{n_k}
\]
converges.
:::

::: {.solution}
For each integer \(m\ge1\), let
\[
S_m
=
\{n\in S:10^{m-1}\le n<10^m\},
\]
the admissible positive integers with exactly \(m\) decimal digits.

<1>1. The number of elements of \(S_m\) is
\[
\boxed{|S_m|=9^m}.
\]

::: {.proof}
Each of the \(m\) decimal digits must belong to
\[
\{1,2,\dots,9\}.
\]
There are \(9\) independent choices for each digit, including the leading
digit. Hence there are \(9^m\) such numbers.
:::

<1>2. Every \(n\in S_m\) satisfies
\[
\boxed{
n\ge10^{m-1}}.
\]

::: {.proof}
This is the defining lower bound for an \(m\)-digit positive integer.
:::

<1>3. Therefore, for every \(n\in S_m\),
\[
\boxed{
\frac1n\le\frac1{10^{m-1}}}.
\]

::: {.proof}
All quantities are positive, so taking reciprocals reverses the inequality
in step <1>2.
:::

<1>4. Hence the total contribution of the \(m\)-digit block satisfies
\[
\sum_{n\in S_m}\frac1n
\le
\frac{|S_m|}{10^{m-1}}.
\]

::: {.proof}
There are \(|S_m|\) terms, each bounded above by the quantity in step <1>3.
:::

<1>5. Using step <1>1,
\[
\boxed{
\sum_{n\in S_m}\frac1n
\le
\frac{9^m}{10^{m-1}}
=
10\left(\frac9{10}\right)^m}.
\]

::: {.proof}
Substitute
\[
|S_m|=9^m
\]
into step <1>4 and factor:
\[
\frac{9^m}{10^{m-1}}
=
10\frac{9^m}{10^m}.
\]
:::

<1>6. The series
\[
\sum_{m=1}^{\infty}
10\left(\frac9{10}\right)^m
\]
converges.

::: {.proof}
It is geometric with ratio
\[
\frac9{10}<1.
\]
:::

<1>7. Since
\[
S=\bigsqcup_{m=1}^{\infty}S_m,
\]
one has
\[
\sum_{n\in S}\frac1n
=
\sum_{m=1}^{\infty}
\sum_{n\in S_m}\frac1n.
\]

::: {.proof}
Every positive integer has a unique number of decimal digits, so the sets
\(S_m\) partition \(S\).
:::

<1>8. By comparison,
\[
\boxed{
\sum_{n\in S}\frac1n
\text{ converges}}.
\]

::: {.proof}
Each block is nonnegative and bounded above by the corresponding term of the
convergent geometric series in step <1>6, by step <1>5. Apply the comparison
test to the block sums in step <1>7.
:::

<1>9. Therefore
\[
\boxed{
\sum_{k=1}^{\infty}\frac1{n_k}
\text{ converges}}.
\]

::: {.proof}
The enumeration
\[
S=\{n_1,n_2,\dots\}
\]
does not change the sum of the nonnegative terms.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the required conclusion.
:::
:::
