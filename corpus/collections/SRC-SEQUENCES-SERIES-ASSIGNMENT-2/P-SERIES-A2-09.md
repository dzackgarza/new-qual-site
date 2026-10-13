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

::: {.solution}
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

<1>1. Suppose first that
\[
q>R.
\]
Then there exists \(N\) such that
\[
\boxed{r_n<q}
\]
for every \(n\ge N\).

::: {.proof}
This is the defining eventual upper-bound property of the limsup.
:::

<1>2. For every \(n>N\),
\[
a_n
=
a_N
\prod_{k=N}^{n-1}r_k.
\]

::: {.proof}
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

<1>3. Hence
\[
\boxed{
a_n
\le
a_N q^{\,n-N}}
\]
for every \(n>N\).

::: {.proof}
Apply the bound \(r_k<q\) from step <1>1 to every factor in step <1>2.
:::

<1>4. Taking \(n\)th roots,
\[
\rho_n
\le
a_N^{1/n}
q^{1-N/n}.
\]

::: {.proof}
All quantities are positive, so taking \(n\)th roots preserves the
inequality.
:::

<1>5. Therefore
\[
\limsup_{n\to\infty}\rho_n
\le
q.
\]

::: {.proof}
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

<1>6. Letting \(q\downarrow R\),
\[
\boxed{
\limsup_{n\to\infty}\rho_n
\le
R}.
\]

::: {.proof}
Step <1>5 holds for every \(q>R\).
:::

<1>7. Suppose now that
\[
0<q<L.
\]
Then there exists \(N\) such that
\[
\boxed{r_n>q}
\]
for every \(n\ge N\).

::: {.proof}
This is the defining eventual lower-bound property of the liminf.
:::

<1>8. For every \(n>N\),
\[
\boxed{
a_n
\ge
a_N q^{\,n-N}}.
\]

::: {.proof}
Use the product identity from step <1>2 and bound every factor below by \(q\)
using step <1>7.
:::

<1>9. Taking \(n\)th roots,
\[
\rho_n
\ge
a_N^{1/n}
q^{1-N/n}.
\]

::: {.proof}
All quantities are positive.
:::

<1>10. Therefore
\[
\liminf_{n\to\infty}\rho_n
\ge
q.
\]

::: {.proof}
Take \(n\to\infty\) in step <1>9.
:::

<1>11. If \(L>0\), letting \(q\uparrow L\) gives
\[
\liminf\rho_n\ge L.
\]

::: {.proof}
Step <1>10 holds for every \(q\in(0,L)\).
:::

<1>12. If \(L=0\), one still has
\[
\liminf\rho_n\ge0=L.
\]

::: {.proof}
Every \(\rho_n\) is positive.
:::

<1>13. Thus
\[
\boxed{
L
\le
\liminf_{n\to\infty}\rho_n}.
\]

::: {.proof}
Combine steps <1>11--<1>12.
:::

<1>14. Trivially,
\[
\boxed{
\liminf\rho_n
\le
\limsup\rho_n}.
\]

::: {.proof}
For every real sequence, the liminf is at most the limsup.
:::

<1>15. Combining steps <1>6, <1>13, and <1>14,
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

::: {.proof}
This is exactly the chain of inequalities established above.
:::

## Part (b): ratio test implies root test

<1>16. Suppose \(\sum a_n\) converges by the ratio test. Then
\[
\boxed{
\limsup_{n\to\infty}
\left|
\frac{a_{n+1}}{a_n}
\right|
<1}.
\]

::: {.proof}
This is the convergence hypothesis in the generalized ratio test; in the
usual version where the ratio limit exists, the same strict inequality holds
for that limit.
:::

<1>17. Applying part (a) to the positive sequence \((|a_n|)\),
\[
\limsup_{n\to\infty}\sqrt[n]{|a_n|}
\le
\limsup_{n\to\infty}
\left|
\frac{a_{n+1}}{a_n}
\right|.
\]

::: {.proof}
Use step <1>15 with \(a_n\) replaced by \(|a_n|\).
:::

<1>18. Hence
\[
\boxed{
\limsup_{n\to\infty}\sqrt[n]{|a_n|}<1}.
\]

::: {.proof}
Combine steps <1>16--<1>17.
:::

<1>19. Therefore the root test also proves that
\[
\boxed{\sum a_n\text{ converges absolutely}.}
\]

::: {.proof}
The root-test convergence criterion is exactly the strict inequality in
step <1>18.
:::

## Part (c)

Let
\[
a_n
=
\frac1{2^{n+(-1)^n}}.
\]

<1>20. The \(n\)th root is
\[
\boxed{
|a_n|^{1/n}
=
2^{-1-(-1)^n/n}}.
\]

::: {.proof}
\[
\left(
2^{-n-(-1)^n}
\right)^{1/n}
=
2^{-1-(-1)^n/n}.
\]
:::

<1>21. Therefore
\[
\boxed{
\lim_{n\to\infty}|a_n|^{1/n}
=
\frac12}.
\]

::: {.proof}
Since
\[
\frac{(-1)^n}{n}\to0,
\]
the exponent in step <1>20 tends to \(-1\).
:::

<1>22. In particular,
\[
\boxed{
\limsup_{n\to\infty}|a_n|^{1/n}
=
\frac12}.
\]

::: {.proof}
The full sequence has a limit by step <1>21.
:::

<1>23. The ratio is
\[
\frac{a_{n+1}}{a_n}
=
2^{-1+2(-1)^n}.
\]

::: {.proof}
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

<1>24. If \(n\) is even,
\[
\boxed{
\frac{a_{n+1}}{a_n}=2}.
\]

::: {.proof}
Then
\[
(-1)^n=1,
\]
so the exponent in step <1>23 is \(1\).
:::

<1>25. If \(n\) is odd,
\[
\boxed{
\frac{a_{n+1}}{a_n}=\frac18}.
\]

::: {.proof}
Then
\[
(-1)^n=-1,
\]
so the exponent is \(-3\).
:::

<1>26. Hence
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

::: {.proof}
The ratio alternates between the two values in steps <1>24--<1>25.
:::

<1>27. The series
\[
\sum a_n
\]
converges absolutely by the root test.

::: {.proof}
By step <1>22, the root-test limsup is
\[
1/2<1.
\]
:::

<1>28. The ratio test does not decide convergence.

::: {.proof}
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

## Part (d)

Let
\[
b_n=\frac{n^n}{n!}.
\]

<1>29. The consecutive ratio is
\[
\boxed{
\frac{b_{n+1}}{b_n}
=
\left(
1+\frac1n
\right)^n}.
\]

::: {.proof}
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

<1>30. Therefore
\[
\boxed{
\frac{b_{n+1}}{b_n}\to e}.
\]

::: {.proof}
Use the standard limit
\[
\left(
1+\frac1n
\right)^n\to e.
\]
:::

<1>31. Hence both the liminf and limsup of the ratios equal \(e\).

::: {.proof}
The ratio sequence converges by step <1>30.
:::

<1>32. Applying the inequality from part (a),
\[
e
\le
\liminf\sqrt[n]{b_n}
\le
\limsup\sqrt[n]{b_n}
\le
e.
\]

::: {.proof}
Use step <1>15 together with step <1>31.
:::

<1>33. Therefore
\[
\boxed{
\lim_{n\to\infty}\sqrt[n]{b_n}=e}.
\]

::: {.proof}
The liminf and limsup are both \(e\) by step <1>32, so the sequence
converges to \(e\).
:::

<1>34. Q.E.D.

::: {.proof}
Step <1>15 proves part (a), step <1>19 proves part (b), steps <1>22--<1>28
prove part (c), and step <1>33 proves part (d).
:::
:::
