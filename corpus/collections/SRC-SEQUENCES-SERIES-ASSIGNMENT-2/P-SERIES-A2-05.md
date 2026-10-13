---
schema: qual/card@1
id: P-SERIES-A2-05
kind: problem
title: Sequences with $|a_{n+1}-a_n|\le\frac12|a_n-a_{n-1}|$ converge
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\{a_n\}_{n=0}^\infty$ be a sequence of real numbers satisfying
\[
|a_{n+1}-a_n|\le \frac12|a_n-a_{n-1}|.
\]
Show that the sequence converges. Hint: show that the sequence is Cauchy.
:::

::: {.solution}
For \(n\ge1\), define
\[
d_n=|a_n-a_{n-1}|.
\]

<1>1. The hypothesis is
\[
\boxed{
d_{n+1}\le\frac12d_n}
\]
for every \(n\ge1\).

::: {.proof}
This is exactly the given inequality written in terms of \(d_n\).
:::

<1>2. For every \(n\ge1\),
\[
\boxed{
d_n\le
\left(\frac12\right)^{n-1}d_1}.
\]

::: {.proof}
Use induction.

For \(n=1\), the statement is equality.

If it holds for \(n\), then by step <1>1,
\[
d_{n+1}
\le
\frac12d_n
\le
\frac12
\left(\frac12\right)^{n-1}d_1
=
\left(\frac12\right)^n d_1.
\]
:::

<1>3. Let \(m>n\). Then
\[
a_m-a_n
=
\sum_{k=n+1}^{m}
(a_k-a_{k-1}).
\]

::: {.proof}
The sum telescopes:
\[
(a_{n+1}-a_n)+\cdots+(a_m-a_{m-1})
=
a_m-a_n.
\]
:::

<1>4. Hence
\[
|a_m-a_n|
\le
\sum_{k=n+1}^{m}d_k.
\]

::: {.proof}
Apply the triangle inequality to step <1>3.
:::

<1>5. Using step <1>2,
\[
|a_m-a_n|
\le
d_1
\sum_{k=n+1}^{m}
\left(\frac12\right)^{k-1}.
\]

::: {.proof}
Bound each \(d_k\) in step <1>4 by the geometric estimate from step <1>2.
:::

<1>6. Extending the finite sum to an infinite geometric tail,
\[
|a_m-a_n|
\le
d_1
\sum_{k=n+1}^{\infty}
\left(\frac12\right)^{k-1}.
\]

::: {.proof}
All terms are nonnegative.
:::

<1>7. The geometric tail is
\[
\boxed{
\sum_{k=n+1}^{\infty}
\left(\frac12\right)^{k-1}
=
2^{1-n}}.
\]

::: {.proof}
Set \(j=k-1\):
\[
\sum_{j=n}^{\infty}2^{-j}
=
\frac{2^{-n}}{1-1/2}
=
2^{1-n}.
\]
:::

<1>8. Therefore, for every \(m>n\),
\[
\boxed{
|a_m-a_n|
\le
d_1\,2^{1-n}}.
\]

::: {.proof}
Combine steps <1>6--<1>7.
:::

<1>9. Let
\[
\varepsilon>0.
\]
Choose \(N\) so large that
\[
d_1\,2^{1-N}<\varepsilon.
\]

::: {.proof}
Since
\[
2^{1-N}\to0,
\]
such \(N\) exists. If \(d_1=0\), any \(N\) works.
:::

<1>10. Then for all
\[
m>n\ge N,
\]
one has
\[
\boxed{
|a_m-a_n|<\varepsilon}.
\]

::: {.proof}
By step <1>8,
\[
|a_m-a_n|
\le
d_1\,2^{1-n}
\le
d_1\,2^{1-N}
<
\varepsilon.
\]
:::

<1>11. Thus \((a_n)\) is a Cauchy sequence.

::: {.proof}
Step <1>10 is exactly the Cauchy criterion.
:::

<1>12. Since \(\mathbb R\) is complete,
\[
\boxed{
(a_n)\text{ converges in }\mathbb R}.
\]

::: {.proof}
Every Cauchy sequence of real numbers converges.
:::

<1>13. Q.E.D.

::: {.proof}
Step <1>12 is the required conclusion.
:::
:::
