---
schema: qual/card@1
id: P-TOPSU15D
kind: problem
title: "Homology of a product of spaces with H_k = Z/kZ"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Künneth Formula
relations: []
review: draft
---

::: {.problem}
Let $X_n$ be a space whose homology groups are given by $H_k(X_n; \mathbb{Z}) \cong \mathbb{Z}/k\mathbb{Z}$ for $0 \leq k \leq n$ and which vanish for $k > n$.
Compute the homology $H_*(X_3 \times X_5; \mathbb{Z})$.
:::

::: {.solution}
<1>1. Interpreting $\mathbb Z/0\mathbb Z$ as $\mathbb Z$ and $\mathbb Z/1\mathbb Z$ as $0$, the nonzero homology groups are
$$
H_0(X_3)=\mathbb Z,\quad H_2(X_3)=\mathbb Z/2,\quad H_3(X_3)=\mathbb Z/3,
$$
and
$$
H_0(X_5)=\mathbb Z,\ H_2=\mathbb Z/2,\ H_3=\mathbb Z/3,\ H_4=\mathbb Z/4,\ H_5=\mathbb Z/5.
$$
::: {.proof}
This is the given formula $H_k(X_n)=\mathbb Z/k\mathbb Z$ in the indicated range.
:::

<1>2. The tensor terms in the integral Künneth theorem give
$$
\begin{array}{c|c}
q&\displaystyle\bigoplus_{i+j=q}H_i(X_3)\otimes H_j(X_5)\\ \hline
0&\mathbb Z\\
2&(\mathbb Z/2)^2\\
3&(\mathbb Z/3)^2\\
4&\mathbb Z/4\oplus\mathbb Z/2\\
5&\mathbb Z/5\\
6&\mathbb Z/2\oplus\mathbb Z/3\\
\end{array}
$$
with zero tensor terms in the other degrees.
::: {.proof}
Use $\mathbb Z/a\otimes\mathbb Z/b\cong\mathbb Z/\gcd(a,b)$ for $a,b>1$ and tensoring with $\mathbb Z$ unchanged.
:::

<1>3. The only nonzero Tor terms are
$$
\operatorname{Tor}(\mathbb Z/2,\mathbb Z/2)\cong\mathbb Z/2
$$
in total degree $5$, and
$$
\operatorname{Tor}(\mathbb Z/2,\mathbb Z/4)\oplus
\operatorname{Tor}(\mathbb Z/3,\mathbb Z/3)
\cong\mathbb Z/2\oplus\mathbb Z/3
$$
in total degree $7$.
::: {.proof}
A Tor term from bidegree $(i,j)$ contributes to $H_{i+j+1}$, and $\operatorname{Tor}(\mathbb Z/a,\mathbb Z/b)\cong\mathbb Z/\gcd(a,b)$.
:::

<1>4. Therefore, using the noncanonical splitting in the Künneth theorem,
$$
\boxed{H_q(X_3\times X_5;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&q=0,\\
(\mathbb Z/2)^2,&q=2,\\
(\mathbb Z/3)^2,&q=3,\\
\mathbb Z/4\oplus\mathbb Z/2,&q=4,\\
\mathbb Z/10,&q=5,\\
\mathbb Z/6,&q=6,7,\\
0,&\text{otherwise}.
\end{cases}}
$$
::: {.proof}
In degree $5$, $\mathbb Z/5\oplus\mathbb Z/2\cong\mathbb Z/10$; in degrees $6$ and $7$, $\mathbb Z/2\oplus\mathbb Z/3\cong\mathbb Z/6$.
:::
:::
