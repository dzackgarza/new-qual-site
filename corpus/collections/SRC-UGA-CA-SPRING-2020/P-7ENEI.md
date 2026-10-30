---
schema: qual/card@1
id: P-7ENEI
kind: problem
title: $\lim_{n\to\infty}c_n=-\lim_{z\to 1}(z-1)f(z)$ for a simple pole at $z=1$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Poles
  - Laurent Series
relations: []
review: draft
---

::: {.problem}
Suppose that $f$ is holomorphic in an open set containing the closed unit disc, except for a simple pole at $z=1$. Let $f(z)=\sum_{n=1}^{\infty} c_{n} z^{n}$ denote the power series in the open unit disc. Show that 
$$
\lim _{n \rightarrow \infty} c_{n}=-\lim _{z \rightarrow 1}(z-1) f(z)
.$$
:::

::: {.solution}
Let $A=\lim_{z\to1}(z-1)f(z)$, the residue of $f$ at its simple pole $1$.

::: pf

::: {.pf-step #split}
$g(z)=f(z)-\dfrac{A}{z-1}$ is holomorphic on a disk $\abs{z}<\rho$ with $\rho>1$.

::: pf-proof
$f$ is holomorphic on an open set containing $\overline\DD\setminus\{1\}$, and subtracting the principal part removes the simple pole at $1$. So $g$ is holomorphic on an open set containing $\overline\DD$. This open set contains a disk $\abs{z}<\rho$ with $\rho>1$, because $\overline\DD$ is compact.
:::

:::

::: {.pf-step #coeff}
Write $g(z)=\sum_{n\ge0}b_nz^n$ on $\abs{z}<\rho$. Then $c_n=b_n-A$ for $n\ge1$, and $b_n\to0$.

::: pf-proof
For $\abs{z}<1$, $\dfrac{A}{z-1}=-A\sum_{n\ge0}z^n$, so $f(z)=\sum_{n\ge0}(b_n-A)z^n$ there, and uniqueness of power series coefficients gives $c_n=b_n-A$. The series of $g$ converges at $z=r$ for any $1<r<\rho$, so $b_nr^n\to0$ and hence $b_n\to0$.
:::

:::

::: pf-qed
By step [](#coeff){.pf-ref}, $\lim_{n\to\infty}c_n=-A=-\lim_{z\to1}(z-1)f(z)$.
:::

:::

:::
