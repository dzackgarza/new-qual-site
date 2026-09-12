---
schema: qual/card@1
id: E-HK-EZDH
kind: problem
title: The Hilbert matrix is invertible with integer inverse
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hoffman--Kunze Exercise 1.6.12; the closed inverse formula was independently checked against the classical Hilbert-matrix formula.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
The result of Example 16 suggests that perhaps the matrix

$$
A = \left[ \begin{array}{c c c c} 1 & \frac {1}{2} & \dots & \frac {1}{n} \\ \frac {1}{2} & \frac {1}{3} & \dots & \frac {1}{n + 1} \\ \vdots & \vdots & & \vdots \\ \frac {1}{n} & \frac {1}{n + 1} & \dots & \frac {1}{2 n - 1} \end{array} \right]
$$

is invertible and $A^{-1}$ has integer entries.
Can you prove that?

# 2. Vector Spaces
:::


::: solution
Write $H_n=(h_{ij})_{1\le i,j\le n}$ with
\[
h_{ij}=\frac1{i+j-1}.
\]
We first prove the inverse formula for a general Cauchy matrix and then specialize it.

<1>1. Let $x_1,\ldots,x_n$ and $y_1,\ldots,y_n$ be scalars such that the $x_i$ are distinct, the $y_i$ are distinct, and $x_i+y_j\ne0$ for all $i,j$. For
\[
C_{ij}=\frac1{x_i+y_j},
\]
one has
\[
(C^{-1})_{ij}
=
\frac{
\displaystyle\prod_{k=1}^n(x_j+y_k)
\displaystyle\prod_{k=1}^n(x_k+y_i)
}{
(x_j+y_i)
\displaystyle\prod_{k\ne j}(x_j-x_k)
\displaystyle\prod_{k\ne i}(y_i-y_k)
}.
\]
::: proof
Fix $j$. Define
\[
R_j(z)=
\frac{\displaystyle\prod_{\ell\ne j}(z-x_\ell)}
{\displaystyle\prod_{\ell=1}^n(z+y_\ell)}
\cdot
\frac{\displaystyle\prod_{\ell=1}^n(x_j+y_\ell)}
{\displaystyle\prod_{\ell\ne j}(x_j-x_\ell)}.
\]
Then $R_j(x_m)=\delta_{mj}$. Since $R_j$ is a proper rational function with simple poles at $-y_i$, it has a partial-fraction expansion
\[
R_j(z)=\sum_{i=1}^n\frac{b_{ij}}{z+y_i}.
\]
The coefficient at the pole $-y_i$ is
\[
b_{ij}
=
\lim_{z\to-y_i}(z+y_i)R_j(z).
\]
Substituting the definition of $R_j$ gives
\[
b_{ij}
=
\frac{
\displaystyle\prod_{k=1}^n(x_j+y_k)
\displaystyle\prod_{k=1}^n(x_k+y_i)
}{
(x_j+y_i)
\displaystyle\prod_{k\ne j}(x_j-x_k)
\displaystyle\prod_{k\ne i}(y_i-y_k)
}.
\]
Evaluating the partial-fraction expansion at $z=x_m$ yields
\[
\sum_{i=1}^n C_{mi}b_{ij}=R_j(x_m)=\delta_{mj}.
\]
Thus the matrix $B=(b_{ij})$ satisfies $CB=I$, hence $B=C^{-1}$.
:::

<1>2. For the Hilbert matrix take
\[
x_j=j-1,\qquad y_i=i.
\]
Then
\[
(H_n^{-1})_{ij}
=(-1)^{i+j}
\frac{(n+i-1)!(n+j-1)!}
{(i+j-1)(i-1)!^2(j-1)!^2(n-i)!(n-j)!}.
\]
::: proof
In the formula of <1>1,
\[
\prod_{k=1}^n(x_j+y_k)=\frac{(n+j-1)!}{(j-1)!},
\qquad
\prod_{k=1}^n(x_k+y_i)=\frac{(n+i-1)!}{(i-1)!}.
\]
Also
\[
\prod_{k\ne j}(x_j-x_k)
=(-1)^{n-j}(j-1)!(n-j)!,
\]
and
\[
\prod_{k\ne i}(y_i-y_k)
=(-1)^{n-i}(i-1)!(n-i)!.
\]
Since $(-1)^{2n-i-j}=(-1)^{i+j}$, substitution gives the displayed expression.
:::

<1>3. Equivalently,
\[
(H_n^{-1})_{ij}=(-1)^{i+j}(i+j-1)
\binom{n+i-1}{n-j}
\binom{n+j-1}{n-i}
\binom{i+j-2}{i-1}^{\!2}.
\]
::: proof
Expanding the three binomial coefficients into factorials and cancelling gives exactly the expression in <1>2.
:::

<1>4. Hence $H_n$ is invertible and every entry of $H_n^{-1}$ is an integer.
::: proof
The matrix in <1>3 is an inverse by <1>1--<1>3. Every factor in the formula of <1>3 is an integer, so every inverse entry is an integer.
:::
:::
