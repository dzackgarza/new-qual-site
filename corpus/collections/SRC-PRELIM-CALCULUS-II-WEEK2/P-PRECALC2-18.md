---
schema: qual/card@1
id: P-PRECALC2-18
kind: problem
title: Convergence and divergence of infinite products
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked Problem 18 on page 6 of Week2_solns.pdf and added an erratum remark that the first two factors of product (c) are undefined or negative.
---

::: {.problem}
Let $(a_n)$ be a sequence of positive numbers.
The infinite product
\[
\prod_{n=1}^{\infty}a_n=a_1a_2a_3\cdots
\]
is said to converge if there is $L\in(0,\infty)$ such that
\[
\lim_{N\to\infty}\prod_{n=1}^{N}a_n=L.
\]
Otherwise the product is said to diverge to zero or diverge to $+\infty$ if the limit is zero or $+\infty$, respectively.
Consider the infinite products
\[
\text{(a) }\prod_{n=1}^{\infty}\left(1+\frac1{n^2}\right),\qquad
\text{(b) }\prod_{n=1}^{\infty}\left(1+\frac1n\right),\qquad
\text{(c) }\prod_{n=1}^{\infty}\left(1-\frac1{\log n}\right).
\]
Show that (a) converges, (b) diverges to $+\infty$, and (c) diverges to $0$.
:::

::: {.remark}
Erratum: product (c) does not satisfy the source's standing hypothesis that the factors are positive. At $n = 1$ the factor $1 - \frac{1}{\log 1}$ is undefined, and at $n = 2$ it is $1 - \frac{1}{\log 2} \approx -0.44 < 0$. For $n \ge 3$ we have $\log n > 1$, so every factor lies in $(0,1)$; the intended claim is that $\prod_{n=3}^{\infty}\left(1 - \frac{1}{\log n}\right)$ diverges to $0$.
:::

::: {.solution}
## Product (a)

Let
\[
P_N
=
\prod_{n=1}^{N}
\left(1+\frac1{n^2}\right).
\]

<1>1. For every \(x\ge0\),
\[
\boxed{\log(1+x)\le x}.
\]

::: {.proof}
Define
\[
h(x)=x-\log(1+x).
\]
Then
\[
h(0)=0
\]
and
\[
h'(x)
=
1-\frac1{1+x}
=
\frac{x}{1+x}
\ge0.
\]
Hence \(h(x)\ge0\).
:::

<1>2. Therefore
\[
0<
\log\left(1+\frac1{n^2}\right)
\le
\frac1{n^2}.
\]

::: {.proof}
Positivity follows because
\[
1+\frac1{n^2}>1.
\]
Apply step <1>1 with \(x=1/n^2\).
:::

<1>3. The series
\[
\sum_{n=1}^{\infty}
\log\left(1+\frac1{n^2}\right)
\]
converges.

::: {.proof}
By step <1>2 it is a nonnegative series dominated termwise by the convergent
\(p\)-series
\[
\sum_{n=1}^{\infty}\frac1{n^2}.
\]
:::

<1>4. Hence there is a finite real number \(S\) such that
\[
\log P_N
=
\sum_{n=1}^{N}
\log\left(1+\frac1{n^2}\right)
\longrightarrow
S.
\]

::: {.proof}
The logarithm of a finite product of positive factors is the sum of the
logarithms. Apply step <1>3.
:::

<1>5. Therefore
\[
\boxed{
P_N\longrightarrow e^S\in(0,\infty)}.
\]

::: {.proof}
Exponentiation is continuous and
\[
P_N=e^{\log P_N}.
\]
Since \(S\in\mathbb R\), one has
\[
e^S>0.
\]
:::

<1>6. Thus
\[
\boxed{
\prod_{n=1}^{\infty}
\left(1+\frac1{n^2}\right)
\text{ converges}}.
\]

::: {.proof}
Step <1>5 gives a positive finite limit of the partial products.
:::

## Product (b)

Let
\[
Q_N
=
\prod_{n=1}^{N}
\left(1+\frac1n\right).
\]

<1>7. Each factor satisfies
\[
\boxed{
1+\frac1n
=
\frac{n+1}{n}}.
\]

::: {.proof}
This is direct algebra.
:::

<1>8. Therefore
\[
Q_N
=
\frac21
\frac32
\frac43
\cdots
\frac{N+1}{N}.
\]

::: {.proof}
Substitute step <1>7 into the finite product.
:::

<1>9. The product telescopes:
\[
\boxed{Q_N=N+1}.
\]

::: {.proof}
Every intermediate numerator cancels with the same denominator:
\[
\frac21
\frac32
\cdots
\frac{N+1}{N}
=
N+1.
\]
:::

<1>10. Hence
\[
\boxed{
\prod_{n=1}^{\infty}
\left(1+\frac1n\right)
\text{ diverges to }+\infty}.
\]

::: {.proof}
By step <1>9,
\[
Q_N=N+1\to+\infty.
\]
:::

## Product (c), with the corrected starting index \(n=3\)

Let
\[
R_N
=
\prod_{n=3}^{N}
\left(1-\frac1{\log n}\right).
\]

<1>11. For every \(n\ge3\),
\[
\boxed{
0<
1-\frac1{\log n}
<
1}.
\]

::: {.proof}
Since
\[
\log n>1
\qquad(n\ge3),
\]
one has
\[
0<\frac1{\log n}<1.
\]
Subtract from \(1\).
:::

<1>12. For \(0<x<1\),
\[
\boxed{\log(1-x)\le -x}.
\]

::: {.proof}
Define
\[
k(x)=-x-\log(1-x).
\]
Then
\[
k(0)=0
\]
and
\[
k'(x)
=
-1+\frac1{1-x}
=
\frac{x}{1-x}
>0.
\]
Hence \(k(x)>0\) for \(x>0\).
:::

<1>13. Therefore
\[
\log R_N
\le
-\sum_{n=3}^{N}
\frac1{\log n}.
\]

::: {.proof}
By step <1>11 all factors are positive, so logarithms are defined. Then
\[
\log R_N
=
\sum_{n=3}^{N}
\log\left(1-\frac1{\log n}\right).
\]
Apply step <1>12 termwise with
\[
x=\frac1{\log n}.
\]
:::

<1>14. For every \(n\ge3\),
\[
\boxed{
\frac1{\log n}
>
\frac1n}.
\]

::: {.proof}
For \(n>1\),
\[
\log n<n.
\]
Both quantities are positive, so taking reciprocals reverses the inequality.
:::

<1>15. Hence
\[
\sum_{n=3}^{\infty}
\frac1{\log n}
\]
diverges.

::: {.proof}
By step <1>14 it dominates the divergent harmonic tail
\[
\sum_{n=3}^{\infty}\frac1n.
\]
:::

<1>16. Consequently,
\[
\boxed{\log R_N\to-\infty}.
\]

::: {.proof}
Step <1>13 gives
\[
\log R_N
\le
-\sum_{n=3}^{N}\frac1{\log n},
\]
and the right-hand side tends to \(-\infty\) by step <1>15.
:::

<1>17. Therefore
\[
\boxed{R_N\to0}.
\]

::: {.proof}
Since
\[
R_N=e^{\log R_N}
\]
and the exponential tends to \(0\) as its argument tends to \(-\infty\),
step <1>16 gives the result.
:::

<1>18. Thus the intended positive-tail product satisfies
\[
\boxed{
\prod_{n=3}^{\infty}
\left(1-\frac1{\log n}\right)
=0}
\]
in the sense that its partial products diverge to zero.

::: {.proof}
This is step <1>17.
:::

<1>19. Q.E.D.

::: {.proof}
Step <1>6 proves (a), step <1>10 proves (b), and step <1>18 proves the
corrected form of (c).
:::
:::
