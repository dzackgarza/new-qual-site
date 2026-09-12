---
schema: qual/card@1
id: P-MMAQ-BFNULVNWCY
kind: problem
title: Irreducibility, degree, and Galois group of $x^{10}+x^5+1$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Consider the polynomial $f(x)=x^{10}+x^5+1\in\mathbb Q[x]$ with splitting field $K$ over $\mathbb Q$.

- Determine whether $f(x)$ is irreducible over $\mathbb Q$ and find $[K:\mathbb Q]$.

- Determine the structure of the Galois group $\Gal(K/\mathbb Q)$.
:::

::: solution
<1>1. The polynomial $f$ is reducible over $\mathbb Q$.
::: {.proof}
We have
\[
x^{15}-1=(x^5-1)(x^{10}+x^5+1),
\]
so
\[
f(x)=\frac{x^{15}-1}{x^5-1}.
\]
Using the cyclotomic factorization
\[
x^{15}-1=\prod_{d\mid15}\Phi_d(x)
=\Phi_1(x)\Phi_3(x)\Phi_5(x)\Phi_{15}(x)
\]
and
\[
x^5-1=\Phi_1(x)\Phi_5(x),
\]
we obtain
\[
f(x)=\Phi_3(x)\Phi_{15}(x).
\]
Both factors have positive degree, namely $2$ and $8$, so $f$ is reducible over $\mathbb Q$.
:::

<1>2. The roots of $f$ are exactly the $15$th roots of unity whose orders are $3$ or $15$.
::: {.proof}
From
\[
f(x)=\frac{x^{15}-1}{x^5-1},
\]
a complex number $\alpha$ is a root of $f$ precisely when $\alpha^{15}=1$ but $\alpha^5\ne1$. The possible orders of a $15$th root of unity are $1,3,5,15$; excluding those whose order divides $5$ leaves orders $3$ and $15$. Equivalently, this is the union of the roots of $\Phi_3$ and $\Phi_{15}$ from <1>1.
:::

<1>3. If $\zeta_{15}$ is a primitive $15$th root of unity, then
\[
K=\mathbb Q(\zeta_{15}).
\]
::: {.proof}
The polynomial $f$ has primitive $15$th roots among its roots, so its splitting field contains $\zeta_{15}$. Conversely, $\mathbb Q(\zeta_{15})$ contains every $15$th root of unity, hence contains all roots of $f$ described in <1>2. Therefore it is exactly the splitting field.
:::

<1>4. The degree of the splitting field is
\[
[K:\mathbb Q]=\varphi(15)=8.
\]
::: {.proof}
By <1>3, $K=\mathbb Q(\zeta_{15})$. The degree of the $15$th cyclotomic extension is the degree of $\Phi_{15}$, namely Euler's totient
\[
\varphi(15)=15\left(1-\frac13\right)\left(1-\frac15\right)=8.
\]
:::

<1>5. The Galois group is
\[
\operatorname{Gal}(K/\mathbb Q)
\cong (\mathbb Z/15\mathbb Z)^\times
\cong C_2\times C_4.
\]
::: {.proof}
Every automorphism of the cyclotomic field $\mathbb Q(\zeta_{15})$ is determined by
\[
\zeta_{15}\longmapsto \zeta_{15}^a
\]
for a unique $a\in(\mathbb Z/15\mathbb Z)^\times$, and every such $a$ defines an automorphism. Hence
\[
\operatorname{Gal}(K/\mathbb Q)\cong(\mathbb Z/15\mathbb Z)^\times.
\]
By the Chinese remainder theorem,
\[
(\mathbb Z/15\mathbb Z)^\times
\cong
(\mathbb Z/3\mathbb Z)^\times\times(\mathbb Z/5\mathbb Z)^\times.
\]
The first factor is cyclic of order $2$, and the second is cyclic of order $4$. Thus the group is $C_2\times C_4$.
:::
:::
