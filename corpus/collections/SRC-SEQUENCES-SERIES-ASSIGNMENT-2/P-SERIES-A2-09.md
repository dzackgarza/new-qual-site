---
schema: qual/card@1
id: P-SERIES-A2-09
kind: problem
title: Ratio test versus root test
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
(a) Let $\{a_n\}$ be a sequence of positive real numbers. Show that
\[
\liminf_{n\to\infty}\frac{a_{n+1}}{a_n}
\le \liminf_{n\to\infty}\sqrt[n]{a_n}
\le \limsup_{n\to\infty}\sqrt[n]{a_n}
\le \limsup_{n\to\infty}\frac{a_{n+1}}{a_n}.
\]
You may assume all four quantities are finite.

(b) Show that if $\sum a_n$ converges by the ratio test, then it also converges by the root test.

(c) Let
\[
a_n=\frac1{2^{n+(-1)^n}}.
\]
Compute $\limsup\sqrt[n]{|a_n|}$ and $\limsup|a_{n+1}/a_n|$. Show that the series converges by the root test. Does the ratio test decide convergence?

(d) Let $b_n=n^n/n!$. Show that
\[
\lim_{n\to\infty}\sqrt[n]{b_n}=e.
\]
:::

For part (a), define
\[
r_n=\frac{a_{n+1}}{a_n},
\qquad
\rho_n=\sqrt[n]{a_n}.
\]

## Part (a): comparison of ratio and root limits

Let
\[
L=\liminf_{n\to\infty}r_n,
\qquad
R=\limsup_{n\to\infty}r_n.
\]

::: pf

::: pf-step

Suppose first that
\[
q>R.
\]
Then there exists \(N\) such that
\[
\boxed{r_n<q}
\]
for every \(n\ge N\).


::: pf-proof

This is the defining eventual upper-bound property of the limsup.

:::

:::

::: pf-step

For every \(n>N\),
\[
a_n
=
a_N
\prod_{k=N}^{n-1}r_k.
\]


::: pf-proof

The product telescopes:
\[
a_N
\frac{a_{N+1}}{a_N}
\frac{a_{N+2}}{a_{N+1}}
\cdots
\frac{a_n}{a_{n-1}}
=
a_n.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
a_n
\le
a_N q^{\,n-N}}
\]
for every \(n>N\).


::: pf-proof

Apply the bound \(r_k<q\) from step <1>1 to every factor in step <1>2.

:::

:::

::: pf-step

Taking \(n\)th roots,
\[
\rho_n
\le
a_N^{1/n}
q^{1-N/n}.
\]


::: pf-proof

All quantities are positive, so taking \(n\)th roots preserves the
inequality.

:::

:::

::: pf-step

Therefore
\[
\limsup_{n\to\infty}\rho_n
\le
q.
\]


::: pf-proof

As \(n\to\infty\),
\[
a_N^{1/n}\to1
\]
and
\[
q^{1-N/n}\to q.
\]
Apply step <1>4.

:::

:::

::: pf-step

Letting \(q\downarrow R\),
\[
\boxed{
\limsup_{n\to\infty}\rho_n
\le
R}.
\]


::: pf-proof

Step <1>5 holds for every \(q>R\).

:::

:::

::: pf-step

Suppose now that
\[
0<q<L.
\]
Then there exists \(N\) such that
\[
\boxed{r_n>q}
\]
for every \(n\ge N\).


::: pf-proof

This is the defining eventual lower-bound property of the liminf.

:::

:::

::: pf-step

For every \(n>N\),
\[
\boxed{
a_n
\ge
a_N q^{\,n-N}}.
\]


::: pf-proof

Use the product identity from step <1>2 and bound every factor below by \(q\)
using step <1>7.

:::

:::

::: pf-step

Taking \(n\)th roots,
\[
\rho_n
\ge
a_N^{1/n}
q^{1-N/n}.
\]


::: pf-proof

All quantities are positive.

:::

:::

::: pf-step

Therefore
\[
\liminf_{n\to\infty}\rho_n
\ge
q.
\]


::: pf-proof

Take \(n\to\infty\) in step <1>9.

:::

:::

::: pf-step

If \(L>0\), letting \(q\uparrow L\) gives
\[
\liminf\rho_n\ge L.
\]


::: pf-proof

Step <1>10 holds for every \(q\in(0,L)\).

:::

:::

::: pf-step

If \(L=0\), one still has
\[
\liminf\rho_n\ge0=L.
\]


::: pf-proof

Every \(\rho_n\) is positive.

:::

:::

::: pf-step

Thus
\[
\boxed{
L
\le
\liminf_{n\to\infty}\rho_n}.
\]


::: pf-proof

Combine steps <1>11--<1>12.

:::

:::

::: pf-step

Trivially,
\[
\boxed{
\liminf\rho_n
\le
\limsup\rho_n}.
\]


::: pf-proof

For every real sequence, the liminf is at most the limsup.

:::

:::

::: pf-step

Combining steps <1>6, <1>13, and <1>14,
\[
\boxed{
\liminf\frac{a_{n+1}}{a_n}
\le
\liminf\sqrt[n]{a_n}
\le
\limsup\sqrt[n]{a_n}
\le
\limsup\frac{a_{n+1}}{a_n}}.
\]


::: pf-proof

This is exactly the chain of inequalities established above.

:::

:::

::: pf-step

Suppose \(\sum a_n\) converges by the ratio test. Then
\[
\boxed{
\limsup_{n\to\infty}
\left|
\frac{a_{n+1}}{a_n}
\right|
<1}.
\]


::: pf-proof

This is the convergence hypothesis in the generalized ratio test; in the
usual version where the ratio limit exists, the same strict inequality holds
for that limit.

:::

:::

::: pf-step

Applying part (a) to the positive sequence \((|a_n|)\),
\[
\limsup_{n\to\infty}\sqrt[n]{|a_n|}
\le
\limsup_{n\to\infty}
\left|
\frac{a_{n+1}}{a_n}
\right|.
\]


::: pf-proof

Use step <1>15 with \(a_n\) replaced by \(|a_n|\).

:::

:::

::: pf-step

Hence
\[
\boxed{
\limsup_{n\to\infty}\sqrt[n]{|a_n|}<1}.
\]


::: pf-proof

Combine steps <1>16--<1>17.

:::

:::

::: pf-step

Therefore the root test also proves that
\[
\boxed{\sum a_n\text{ converges absolutely}.}
\]


::: pf-proof

The root-test convergence criterion is exactly the strict inequality in
step <1>18.

:::

:::

::: pf-step

The \(n\)th root is
\[
\boxed{
|a_n|^{1/n}
=
2^{-1-(-1)^n/n}}.
\]


::: pf-proof

\[
\left(
2^{-n-(-1)^n}
\right)^{1/n}
=
2^{-1-(-1)^n/n}.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\lim_{n\to\infty}|a_n|^{1/n}
=
\frac12}.
\]


::: pf-proof

Since
\[
\frac{(-1)^n}{n}\to0,
\]
the exponent in step <1>20 tends to \(-1\).

:::

:::

::: pf-step

In particular,
\[
\boxed{
\limsup_{n\to\infty}|a_n|^{1/n}
=
\frac12}.
\]


::: pf-proof

The full sequence has a limit by step <1>21.

:::

:::

::: pf-step

The ratio is
\[
\frac{a_{n+1}}{a_n}
=
2^{-1+2(-1)^n}.
\]


::: pf-proof

\[
\begin{aligned}
\frac{a_{n+1}}{a_n}
&=
2^{-[n+1+(-1)^{n+1}]+[n+(-1)^n]}\\
&=
2^{-1-(-1)^{n+1}+(-1)^n}\\
&=
2^{-1+2(-1)^n}.
\end{aligned}
\]

:::

:::

::: pf-step

If \(n\) is even,
\[
\boxed{
\frac{a_{n+1}}{a_n}=2}.
\]


::: pf-proof

Then
\[
(-1)^n=1,
\]
so the exponent in step <1>23 is \(1\).

:::

:::

::: pf-step

If \(n\) is odd,
\[
\boxed{
\frac{a_{n+1}}{a_n}=\frac18}.
\]


::: pf-proof

Then
\[
(-1)^n=-1,
\]
so the exponent is \(-3\).

:::

:::

::: pf-step

Hence
\[
\boxed{
\limsup_{n\to\infty}
\left|
\frac{a_{n+1}}{a_n}
\right|
=
2}
\]
and
\[
\boxed{
\liminf_{n\to\infty}
\left|
\frac{a_{n+1}}{a_n}
\right|
=
\frac18}.
\]


::: pf-proof

The ratio alternates between the two values in steps <1>24--<1>25.

:::

:::

::: pf-step

The series
\[
\sum a_n
\]
converges absolutely by the root test.


::: pf-proof

By step <1>22, the root-test limsup is
\[
1/2<1.
\]

:::

:::

::: pf-step

The ratio test does not decide convergence.


::: pf-proof

The sufficient convergence condition
\[
\limsup |a_{n+1}/a_n|<1
\]
fails because the limsup is \(2\), while the sufficient divergence condition
\[
\liminf |a_{n+1}/a_n|>1
\]
also fails because the liminf is \(1/8\). Thus the generalized ratio test is
inconclusive.

:::

:::

::: pf-step

The consecutive ratio is
\[
\boxed{
\frac{b_{n+1}}{b_n}
=
\left(
1+\frac1n
\right)^n}.
\]


::: pf-proof

\[
\begin{aligned}
\frac{b_{n+1}}{b_n}
&=
\frac{(n+1)^{n+1}}{(n+1)!}
\frac{n!}{n^n}\\
&=
\frac{(n+1)^n}{n^n}\\
&=
\left(
1+\frac1n
\right)^n.
\end{aligned}
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\frac{b_{n+1}}{b_n}\to e}.
\]


::: pf-proof

Use the standard limit
\[
\left(
1+\frac1n
\right)^n\to e.
\]

:::

:::

::: pf-step

Hence both the liminf and limsup of the ratios equal \(e\).


::: pf-proof

The ratio sequence converges by step <1>30.

:::

:::

::: pf-step

Applying the inequality from part (a),
\[
e
\le
\liminf\sqrt[n]{b_n}
\le
\limsup\sqrt[n]{b_n}
\le
e.
\]


::: pf-proof

Use step <1>15 together with step <1>31.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\lim_{n\to\infty}\sqrt[n]{b_n}=e}.
\]


::: pf-proof

The liminf and limsup are both \(e\) by step <1>32, so the sequence
converges to \(e\).

:::

:::

::: pf-qed

Step <1>15 proves part (a), step <1>19 proves part (b), steps <1>22--<1>28
prove part (c), and step <1>33 proves part (d).

:::

:::
