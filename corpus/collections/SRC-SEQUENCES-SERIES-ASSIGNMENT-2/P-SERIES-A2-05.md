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

::: pf

::: {.pf-step #s1-1}

The hypothesis is
\[
\boxed{
d_{n+1}\le\frac12d_n}
\]
for every \(n\ge1\).


::: pf-proof

This is exactly the given inequality written in terms of \(d_n\).

:::

:::

::: {.pf-step #s1-2}

For every \(n\ge1\),
\[
\boxed{
d_n\le
\left(\frac12\right)^{n-1}d_1}.
\]


::: pf-proof

Use induction.

For \(n=1\), the statement is equality.

If it holds for \(n\), then by step [](#s1-1){.pf-ref},
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

:::

::: {.pf-step #s1-3}

Let \(m>n\). Then
\[
a_m-a_n
=
\sum_{k=n+1}^{m}
(a_k-a_{k-1}).
\]


::: pf-proof

The sum telescopes:
\[
(a_{n+1}-a_n)+\cdots+(a_m-a_{m-1})
=
a_m-a_n.
\]

:::

:::

::: {.pf-step #s1-4}

Hence
\[
|a_m-a_n|
\le
\sum_{k=n+1}^{m}d_k.
\]


::: pf-proof

Apply the triangle inequality to step [](#s1-3){.pf-ref}.

:::

:::

::: pf-step

Using step [](#s1-2){.pf-ref},
\[
|a_m-a_n|
\le
d_1
\sum_{k=n+1}^{m}
\left(\frac12\right)^{k-1}.
\]


::: pf-proof

Bound each \(d_k\) in step [](#s1-4){.pf-ref} by the geometric estimate from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Extending the finite sum to an infinite geometric tail,
\[
|a_m-a_n|
\le
d_1
\sum_{k=n+1}^{\infty}
\left(\frac12\right)^{k-1}.
\]


::: pf-proof

All terms are nonnegative.

:::

:::

::: {.pf-step #s1-7}

The geometric tail is
\[
\boxed{
\sum_{k=n+1}^{\infty}
\left(\frac12\right)^{k-1}
=
2^{1-n}}.
\]


::: pf-proof

Set \(j=k-1\):
\[
\sum_{j=n}^{\infty}2^{-j}
=
\frac{2^{-n}}{1-1/2}
=
2^{1-n}.
\]

:::

:::

::: {.pf-step #s1-8}

Therefore, for every \(m>n\),
\[
\boxed{
|a_m-a_n|
\le
d_1\,2^{1-n}}.
\]


::: pf-proof

Combine steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: pf-step

Let
\[
\varepsilon>0.
\]
Choose \(N\) so large that
\[
d_1\,2^{1-N}<\varepsilon.
\]


::: pf-proof

Since
\[
2^{1-N}\to0,
\]
such \(N\) exists. If \(d_1=0\), any \(N\) works.

:::

:::

::: {.pf-step #s1-10}

Then for all
\[
m>n\ge N,
\]
one has
\[
\boxed{
|a_m-a_n|<\varepsilon}.
\]


::: pf-proof

By step [](#s1-8){.pf-ref},
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

:::

::: pf-step

Thus \((a_n)\) is a Cauchy sequence.


::: pf-proof

Step [](#s1-10){.pf-ref} is exactly the Cauchy criterion.

:::

:::

::: {.pf-step #s1-12}

Since \(\RR\) is complete,
\[
\boxed{
(a_n)\text{ converges in }\RR}.
\]


::: pf-proof

Every Cauchy sequence of real numbers converges.

:::

:::

::: pf-qed

Step [](#s1-12){.pf-ref} is the required conclusion.

:::

:::

:::
