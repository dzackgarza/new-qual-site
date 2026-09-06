---
schema: qual/card@1
id: P-AMD-5TCMW6KG
kind: problem
title: Units, domains, and the unique maximal ideal of $R[[x]]$
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Local Rings
  - Maximal Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 6, Exercise 5. Restored
    the three source parts. In part (c), interpreted the handout's final
    occurrence of "R" as "R[[x]]", as required by the preceding sentence and
    by the stated local-ring remark.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    A series with invertible constant coefficient receives an inverse by a
    coefficient-by-coefficient recursion; the converse follows from the
    constant coefficient of a product. For domains, the first nonzero
    coefficient of a product is the product of the first nonzero coefficients.
    Over a field, the zero-constant-term ideal is the kernel of the constant
    coefficient map to R, and every series outside it is a unit, proving
    maximality and uniqueness.
---

::: {.problem}
Let $R$ be a commutative ring and let
\[
R[[x]]
 =\left\{\sum_{n=0}^{\infty}a_nx^n:a_n\in R\right\}
\]
be the ring of formal power series in one variable.

(a) Prove that
\[
\sum_{n=0}^{\infty}a_nx^n\in R[[x]]^\times
\quad\Longleftrightarrow\quad
a_0\in R^\times.
\]

(b) Prove that if $R$ is a domain, then $R[[x]]$ is a domain.

(c) Suppose that $R$ is a field.
Prove that
\[
I=\left\{\sum_{n=0}^{\infty}a_nx^n\in R[[x]]:a_0=0\right\}
\]
is a maximal ideal of $R[[x]]$ and is its unique maximal ideal.

(Thus $R[[x]]$ is a local ring.)
:::

::: {.solution}
<1>1. If a formal power series
\[
f=\sum_{n=0}^{\infty}a_nx^n
\]
is a unit in $R[[x]]$, then $a_0$ is a unit in $R$.
::: {.proof}
Let
\[
g=\sum_{n=0}^{\infty}b_nx^n
\]
be an inverse of $f$.
The constant coefficient of $fg=1$ is
\[
a_0b_0=1.
\]
Hence $a_0\in R^\times$.
:::

<1>2. If $a_0\in R^\times$, then $f$ has an inverse in $R[[x]]$.
::: {.proof}
We construct coefficients $b_n\in R$ recursively so that
\[
g=\sum_{n=0}^{\infty}b_nx^n
\]
satisfies $fg=1$.

Set
\[
b_0=a_0^{-1}.
\]
Suppose $b_0,\ldots,b_{n-1}$ have been defined.
Define
\[
b_n
  =-a_0^{-1}\sum_{i=1}^{n}a_i b_{n-i}.
\]
Then the coefficient of $x^n$ in $fg$ is
\[
\sum_{i=0}^{n}a_i b_{n-i}
  =a_0b_n+\sum_{i=1}^{n}a_i b_{n-i}
  =0.
\]
The constant coefficient is $a_0b_0=1$.
Therefore
\[
fg=1.
\]
Since $R[[x]]$ is commutative, $g$ is the inverse of $f$.
:::

<1>3. A formal power series is a unit exactly when its constant coefficient is a unit.
::: {.proof}
Combine <1>1 and <1>2. This proves part (a).
:::

<1>4. If $R$ is a domain and $f,g\in R[[x]]$ are nonzero, then $fg\ne0$.
::: {.proof}
Write
\[
f=\sum_{i=0}^{\infty}a_ix^i,
\qquad
g=\sum_{j=0}^{\infty}b_jx^j.
\]
Since $f$ and $g$ are nonzero, there are least indices $m,n$ such that
\[
a_m\ne0,
\qquad
b_n\ne0.
\]

The coefficient of $x^{m+n}$ in $fg$ is
\[
\sum_{i=0}^{m+n}a_i b_{m+n-i}.
\]
If $i<m$, then $a_i=0$.
If $i>m$, then
\[
m+n-i<n,
\]
so $b_{m+n-i}=0$.
Thus the only possibly nonzero summand is the one with $i=m$, and the coefficient is
\[
a_mb_n.
\]
Because $R$ is a domain and both factors are nonzero,
\[
a_mb_n\ne0.
\]
Hence $fg\ne0$.
:::

<1>5. If $R$ is a domain, then $R[[x]]$ is a domain.
::: {.proof}
By <1>4, the product of two nonzero elements of $R[[x]]$ is nonzero.
Thus $R[[x]]$ has no zero divisors.
This proves part (b).
:::

<1>6. If $R$ is a field, the set $I$ of series with zero constant coefficient is a maximal ideal of $R[[x]]$.
::: {.proof}
Define the constant-coefficient map
\[
\varepsilon:R[[x]]\longrightarrow R,
\qquad
\varepsilon\left(\sum_{n=0}^{\infty}a_nx^n\right)=a_0.
\]
The constant coefficient of a sum or product is respectively the sum or product of the constant coefficients, so $\varepsilon$ is a ring homomorphism.
It is surjective because every $r\in R$ is the image of the constant series $r$.
Its kernel is exactly $I$.

The first isomorphism theorem gives
\[
R[[x]]/I\cong R.
\]
Since $R$ is a field, $I$ is maximal.
:::

<1>7. Every element of $R[[x]]\setminus I$ is a unit.
::: {.proof}
If
\[
f=\sum_{n=0}^{\infty}a_nx^n\notin I,
\]
then $a_0\ne0$.
Since $R$ is a field,
\[
a_0\in R^\times.
\]
By <1>3, $f$ is a unit in $R[[x]]$.
:::

<1>8. The ideal $I$ is the unique maximal ideal of $R[[x]]$.
::: {.proof}
Let $M$ be any maximal ideal of $R[[x]]$.
A proper ideal cannot contain a unit.
By <1>7, every element outside $I$ is a unit.
Hence every element of $M$ lies in $I$, so
\[
M\le I.
\]
Since $M$ is maximal and $I$ is a proper ideal, it follows that
\[
M=I.
\]
Thus $I$ is the unique maximal ideal, proving part (c).
:::

<1>9. Q.E.D.
::: {.proof}
Parts (a), (b), and (c) are <1>3, <1>5, and <1>8.
:::
:::
