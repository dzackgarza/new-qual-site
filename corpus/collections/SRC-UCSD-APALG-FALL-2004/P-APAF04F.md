---
schema: qual/card@1
id: P-APAF04F
kind: problem
title: Character values on conjugate partitions of $S_n$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
If $\lambda=(\lambda_1\ge\lambda_2\ge\dots\ge\lambda_k)$ is a partition of $n$, let $A^\lambda$ denote the irreducible representation of the symmetric group $S_n$ such that the Frobenius image of $\chi^{A^\lambda}=\chi^\lambda$ is the Schur function $S_\lambda(x_1,\ldots,x_N)$ where $N>n$.

Given a partition $\lambda$ of $n$, let $l(\lambda)$ denote the number of parts of $\lambda$ and $\lambda'$ denote its conjugate partition.
Let $\chi^\lambda_\mu$ denote the value of the character of the irreducible representation $A^\lambda$ of $S_n$ at the conjugacy class indexed by the partition $\mu$.
Show that
\[
\chi^{\lambda'}_\mu=(-1)^{n-l(\mu)}\chi^\lambda_\mu.
\]
:::

::: {.solution}
<1>1. For a class function $\chi$ of $S_n$, its Frobenius characteristic is
\[
\operatorname{ch}(\chi)
=\sum_{\mu\vdash n}\frac{\chi_\mu}{z_\mu}p_\mu,
\]
where
\[
p_\mu=p_{\mu_1}\cdots p_{\mu_{l(\mu)}}
\]
and $z_\mu$ is the usual centralizer factor.
In particular,
\[
s_\lambda
=\sum_{\mu\vdash n}\frac{\chi^\lambda_\mu}{z_\mu}p_\mu.
\]
::: {.proof}
This is the defining power-sum expansion of the Frobenius characteristic map. By the convention in the problem, the irreducible character $\chi^\lambda$ has Frobenius image $s_\lambda$.
:::

<1>2. Let $\omega$ be the standard involution of the ring of symmetric functions determined by
\[
\omega(h_r)=e_r.
\]
Then
\[
\omega(s_\lambda)=s_{\lambda'}.
\]
::: {.proof}
The Jacobi--Trudi identity gives
\[
s_\lambda=\det(h_{\lambda_i-i+j}),
\]
while the dual Jacobi--Trudi identity gives
\[
s_{\lambda'}=\det(e_{\lambda_i-i+j}).
\]
Applying $\omega$ entrywise to the first determinant therefore gives the second. Hence $\omega(s_\lambda)=s_{\lambda'}$.
:::

<1>3. For every $r\ge1$,
\[
\omega(p_r)=(-1)^{r-1}p_r.
\]
::: {.proof}
Let
\[
H(t)=\sum_{m\ge0}h_mt^m,
\qquad
E(t)=\sum_{m\ge0}e_mt^m.
\]
The standard generating-function identities are
\[
H(t)=\exp\left(\sum_{r\ge1}\frac{p_r}{r}t^r\right),
\]
and
\[
E(t)=\exp\left(\sum_{r\ge1}(-1)^{r-1}\frac{p_r}{r}t^r\right).
\]
Since $\omega(H(t))=E(t)$, comparison of the logarithms gives
\[
\sum_{r\ge1}\frac{\omega(p_r)}r t^r
=
\sum_{r\ge1}(-1)^{r-1}\frac{p_r}r t^r.
\]
Comparing coefficients of $t^r$ yields the formula.
:::

<1>4. If $\mu=(\mu_1,\ldots,\mu_{l(\mu)})\vdash n$, then
\[
\omega(p_\mu)=(-1)^{n-l(\mu)}p_\mu.
\]
::: {.proof}
Using multiplicativity of $\omega$ and <1>3,
\[
\omega(p_\mu)
=\prod_{j=1}^{l(\mu)}(-1)^{\mu_j-1}p_{\mu_j}
=(-1)^{\sum_j(\mu_j-1)}p_\mu.
\]
Because $\sum_j\mu_j=n$,
\[
\sum_j(\mu_j-1)=n-l(\mu).
\]
:::

<1>5. Applying $\omega$ to the Frobenius expansion of $s_\lambda$ gives
\[
s_{\lambda'}
=\sum_{\mu\vdash n}
\frac{(-1)^{n-l(\mu)}\chi^\lambda_\mu}{z_\mu}p_\mu.
\]
::: {.proof}
By <1>1,
\[
s_\lambda
=\sum_{\mu\vdash n}\frac{\chi^\lambda_\mu}{z_\mu}p_\mu.
\]
Apply $\omega$ to both sides. By <1>2 the left side becomes $s_{\lambda'}$, and by <1>4 each $p_\mu$ is multiplied by $(-1)^{n-l(\mu)}$.
:::

<1>6. Therefore, for every partition $\mu\vdash n$,
\[
\boxed{\chi^{\lambda'}_\mu=(-1)^{n-l(\mu)}\chi^\lambda_\mu}.
\]
::: {.proof}
Applying <1>1 to the conjugate partition $\lambda'$ also gives
\[
s_{\lambda'}
=\sum_{\mu\vdash n}\frac{\chi^{\lambda'}_\mu}{z_\mu}p_\mu.
\]
The power sums $p_\mu$ for $\mu\vdash n$ form a basis of the degree-$n$ symmetric functions over $\mathbb Q$. Comparing the coefficient of $p_\mu$ with <1>5 yields
\[
\frac{\chi^{\lambda'}_\mu}{z_\mu}
=
\frac{(-1)^{n-l(\mu)}\chi^\lambda_\mu}{z_\mu}.
\]
Since $z_\mu\ne0$, the desired identity follows.
:::
:::
