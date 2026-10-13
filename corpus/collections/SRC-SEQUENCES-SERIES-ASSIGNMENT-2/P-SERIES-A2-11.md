---
schema: qual/card@1
id: P-SERIES-A2-11
kind: problem
title: 'Convergent series: $\sum a_nb_n$, $\sum n^2a_n$ and $na_n\to0$'
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
For each proposition, give a short proof if it is true and a counterexample if it is false.

(a) If $\sum a_n$ converges and the sequence $\{b_n\}$ also converges, then $\sum a_n b_n$ converges.

(b) If $\sum a_n$ converges conditionally, then $\sum n^2a_n$ diverges.

(c) If $\{a_n\}$ is decreasing and $\sum a_n$ converges, then
\[
\lim_{n\to\infty} n a_n=0.
\]
:::

::: {.solution}
## Part (a)

The proposition is false.

<1>1. Define
\[
\boxed{
a_n=\frac{(-1)^n}{\sqrt n},
\qquad
b_n=\frac{(-1)^n}{\sqrt n}}.
\]

::: {.proof}
These sequences will give a counterexample.
:::

<1>2. The series
\[
\sum_{n=1}^{\infty}a_n
\]
converges.

::: {.proof}
The positive sequence
\[
n^{-1/2}
\]
decreases to \(0\), so the alternating-series test applies.
:::

<1>3. The sequence \((b_n)\) converges to \(0\).

::: {.proof}
\[
|b_n|=\frac1{\sqrt n}\to0.
\]
:::

<1>4. But
\[
\boxed{
a_nb_n=\frac1n}.
\]

::: {.proof}
\[
\frac{(-1)^n}{\sqrt n}
\frac{(-1)^n}{\sqrt n}
=
\frac{(-1)^{2n}}{n}
=
\frac1n.
\]
:::

<1>5. Therefore
\[
\sum_{n=1}^{\infty}a_nb_n
\]
diverges.

::: {.proof}
By step <1>4, this is the harmonic series.
:::

<1>6. Hence proposition (a) is
\[
\boxed{\text{false}}.
\]

::: {.proof}
Steps <1>2--<1>5 satisfy the hypotheses but not the conclusion.
:::

## Part (b)

The proposition is true.

Assume
\[
\sum a_n
\]
converges conditionally.

<1>7. Suppose, toward a contradiction, that
\[
\sum n^2a_n
\]
converges.

::: {.proof}
We will show this forces absolute convergence of \(\sum a_n\).
:::

<1>8. Then
\[
\boxed{
n^2a_n\to0}.
\]

::: {.proof}
The terms of every convergent series tend to zero.
:::

<1>9. Hence there exists \(N\) such that for every \(n\ge N\),
\[
\boxed{
|n^2a_n|<1}.
\]

::: {.proof}
Apply step <1>8 with \(\varepsilon=1\).
:::

<1>10. Therefore, for \(n\ge N\),
\[
\boxed{
|a_n|<\frac1{n^2}}.
\]

::: {.proof}
Divide step <1>9 by the positive number \(n^2\).
:::

<1>11. Hence
\[
\sum_{n=N}^{\infty}|a_n|
\]
converges.

::: {.proof}
By step <1>10, compare with the convergent \(p\)-series
\[
\sum_{n=N}^{\infty}\frac1{n^2}.
\]
:::

<1>12. Thus
\[
\sum a_n
\]
would converge absolutely.

::: {.proof}
Adding finitely many initial absolute values does not affect convergence.
Apply step <1>11.
:::

<1>13. This contradicts conditional convergence.

::: {.proof}
Conditional convergence means convergence without absolute convergence.
:::

<1>14. Therefore
\[
\boxed{
\sum n^2a_n
\text{ diverges}}.
\]

::: {.proof}
The assumption in step <1>7 led to a contradiction.
:::

## Part (c)

The proposition is true.

Assume \((a_n)\) is decreasing and
\[
\sum a_n
\]
converges.

<1>15. One has
\[
\boxed{a_n\to0}.
\]

::: {.proof}
The terms of a convergent series tend to zero.
:::

<1>16. Since \((a_n)\) is decreasing and tends to \(0\),
\[
\boxed{a_n\ge0}
\]
for every \(n\).

::: {.proof}
If some \(a_N<0\), then decreasingness would give
\[
a_n\le a_N<0
\]
for all \(n\ge N\), contradicting \(a_n\to0\).
:::

<1>17. Let
\[
\varepsilon>0.
\]
By the Cauchy criterion for the convergent series \(\sum a_n\), there exists
\(N\) such that whenever \(q>p\ge N\),
\[
\boxed{
\sum_{k=p}^{q}a_k<\frac{\varepsilon}{2}}.
\]

::: {.proof}
All terms are nonnegative by step <1>16, so the absolute value in the Cauchy
criterion may be omitted.
:::

<1>18. Let \(n>2N\) and set
\[
m=\left\lfloor\frac n2\right\rfloor.
\]
Then
\[
m\ge N.
\]

::: {.proof}
Since \(n>2N\),
\[
\frac n2>N.
\]
Taking the floor gives \(m\ge N\).
:::

<1>19. Since the sequence is decreasing,
\[
a_k\ge a_n
\]
for every
\[
m\le k\le n.
\]

::: {.proof}
For \(k\le n\), decreasingness gives \(a_k\ge a_n\).
:::

<1>20. Hence
\[
\sum_{k=m}^{n}a_k
\ge
(n-m+1)a_n.
\]

::: {.proof}
There are \(n-m+1\) terms, each at least \(a_n\) by step <1>19.
:::

<1>21. One has
\[
n-m+1\ge\frac n2.
\]

::: {.proof}
Since
\[
m=\left\lfloor\frac n2\right\rfloor\le\frac n2,
\]
\[
n-m+1
\ge
n-\frac n2
=
\frac n2.
\]
:::

<1>22. Therefore
\[
\boxed{
\sum_{k=m}^{n}a_k
\ge
\frac n2\,a_n}.
\]

::: {.proof}
Combine steps <1>20--<1>21 and use \(a_n\ge0\).
:::

<1>23. By step <1>17,
\[
\sum_{k=m}^{n}a_k<\frac{\varepsilon}{2}.
\]

::: {.proof}
Step <1>18 gives \(m\ge N\), so the Cauchy tail estimate applies.
:::

<1>24. Combining steps <1>22--<1>23,
\[
\frac n2\,a_n<\frac{\varepsilon}{2}.
\]

::: {.proof}
The same tail sum is bounded below and above by those two quantities.
:::

<1>25. Hence
\[
\boxed{
na_n<\varepsilon}
\]
for every \(n>2N\).

::: {.proof}
Multiply step <1>24 by \(2\).
:::

<1>26. Therefore
\[
\boxed{
na_n\to0}.
\]

::: {.proof}
Step <1>25 is the \(\varepsilon\)-definition of convergence to \(0\).
:::

<1>27. Thus the answers are:
\[
\boxed{
\text{(a) false,\qquad (b) true,\qquad (c) true}.}
\]

::: {.proof}
Use steps <1>6, <1>14, and <1>26.
:::

<1>28. Q.E.D.

::: {.proof}
Step <1>27 gives the required dispositions.
:::
:::
