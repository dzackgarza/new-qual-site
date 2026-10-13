---
schema: qual/card@1
id: P-PRECALC2-17
kind: problem
title: Counterexamples for the alternating series test and for $\sum b_n$ versus $\sum b_n^2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Find a sequence $\left( a _ { n } \right)$ such that $a _ { n } > 0$ for all $n \in \mathbb { N }$ and $a _ { n } \to 0$ but

$$
\sum _ { n = 1 } ^ { \infty } ( - 1 ) ^ { n } a _ { n } \mathrm { d i v e r g e s } .
$$

[Note: this shows that the assumption that $a _ { n }$ is decreasing is necessary in the Alternating Series Test.] Find a sequence $\left( b _ { n } \right)$ such that

$$
\sum _ { n = 1 } ^ { \infty } b _ { n } \mathrm { c o n v e r g e s ~ w h i l e } \sum _ { n = 1 } ^ { \infty } b _ { n } ^ { 2 } \mathrm { d i v e r g e s } .
$$

Is it possible to choose $\left( b _ { n } \right)$ so that $\sum _ { n = 1 } ^ { \infty } b _ { n }$ converges absolutely while $\textstyle \sum _ { n = 1 } ^ { \infty } b _ { n } ^ { 2 }$ diverges?
:::

::: {.solution}
## A nonmonotone alternating-series counterexample

For \(k\ge1\), define
\[
\boxed{
a_{2k}=\frac1k,
\qquad
a_{2k-1}=\frac1{2k}}.
\]

<1>1. Every \(a_n\) is positive.

::: {.proof}
Both formulas defining \(a_{2k}\) and \(a_{2k-1}\) are positive for
\(k\ge1\).
:::

<1>2. One has
\[
\boxed{a_n\to0}.
\]

::: {.proof}
Along the even subsequence,
\[
a_{2k}=\frac1k\to0.
\]
Along the odd subsequence,
\[
a_{2k-1}=\frac1{2k}\to0.
\]
Since both subsequences tend to \(0\), the whole sequence does.
:::

<1>3. The contribution of the \(k\)th odd-even pair to the alternating
series is
\[
\boxed{
(-1)^{2k-1}a_{2k-1}
+
(-1)^{2k}a_{2k}
=
\frac1{2k}}.
\]

::: {.proof}
Since
\[
(-1)^{2k-1}=-1
\qquad\text{and}\qquad
(-1)^{2k}=1,
\]
one has
\[
-\frac1{2k}+\frac1k
=
\frac1{2k}.
\]
:::

<1>4. The even partial sums satisfy
\[
S_{2N}
=
\sum_{k=1}^{N}\frac1{2k}.
\]

::: {.proof}
Group the first \(2N\) terms into the \(N\) consecutive pairs computed in
step <1>3.
:::

<1>5. Therefore
\[
S_{2N}\to+\infty.
\]

::: {.proof}
\[
S_{2N}
=
\frac12
\sum_{k=1}^{N}\frac1k,
\]
and the harmonic partial sums diverge to \(+\infty\).
:::

<1>6. Hence
\[
\boxed{
\sum_{n=1}^{\infty}
(-1)^na_n
\text{ diverges}}.
\]

::: {.proof}
A convergent series must have all subsequences of its partial sums converge
to the same finite limit. Step <1>5 shows the even partial sums diverge.
:::

## A convergent series whose square series diverges

Define
\[
\boxed{
b_n=\frac{(-1)^n}{\sqrt n}}.
\]

<1>7. The sequence
\[
\frac1{\sqrt n}
\]
is positive, decreasing, and tends to \(0\).

::: {.proof}
The function
\[
x\mapsto x^{-1/2}
\]
is positive and decreasing on \((0,\infty)\), and
\[
n^{-1/2}\to0.
\]
:::

<1>8. Therefore
\[
\boxed{
\sum_{n=1}^{\infty}b_n
=
\sum_{n=1}^{\infty}
\frac{(-1)^n}{\sqrt n}
\text{ converges}}.
\]

::: {.proof}
Apply the alternating series test using step <1>7.
:::

<1>9. But
\[
\boxed{
b_n^2=\frac1n}.
\]

::: {.proof}
\[
\left(
\frac{(-1)^n}{\sqrt n}
\right)^2
=
\frac1n.
\]
:::

<1>10. Hence
\[
\boxed{
\sum_{n=1}^{\infty}b_n^2
=
\sum_{n=1}^{\infty}\frac1n
\text{ diverges}}.
\]

::: {.proof}
Use step <1>9 and divergence of the harmonic series.
:::

## The absolute-convergence question

<1>11. Suppose
\[
\sum_{n=1}^{\infty}|b_n|
\]
converges. Then
\[
\boxed{b_n\to0}.
\]

::: {.proof}
A necessary condition for convergence of any series is that its terms tend
to zero. Apply this to the nonnegative series \(\sum|b_n|\).
:::

<1>12. Hence there exists \(N\) such that
\[
\boxed{|b_n|\le1}
\qquad(n\ge N).
\]

::: {.proof}
Since \(b_n\to0\), eventually
\[
|b_n|<1.
\]
:::

<1>13. For \(n\ge N\),
\[
\boxed{
b_n^2
=
|b_n|^2
\le
|b_n|}.
\]

::: {.proof}
If \(0\le x\le1\), then
\[
x^2\le x.
\]
Apply this with \(x=|b_n|\).
:::

<1>14. Therefore
\[
\sum_{n=N}^{\infty}b_n^2
\]
converges.

::: {.proof}
By step <1>13, the nonnegative series is termwise bounded by the convergent
tail
\[
\sum_{n=N}^{\infty}|b_n|.
\]
Apply the comparison test.
:::

<1>15. Thus
\[
\boxed{
\sum |b_n|<\infty
\quad\Longrightarrow\quad
\sum b_n^2<\infty}.
\]

::: {.proof}
Step <1>14 gives convergence of the tail, and finitely many initial terms do
not affect convergence.
:::

<1>16. Consequently, it is impossible to choose \((b_n)\) so that
\[
\sum b_n
\]
converges absolutely while
\[
\sum b_n^2
\]
diverges.

::: {.proof}
Such a sequence would contradict step <1>15.
:::

<1>17. Q.E.D.

::: {.proof}
Step <1>6 gives the first requested sequence, steps <1>8--<1>10 give the
second, and step <1>16 answers the final question.
:::
:::
