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
Let $X_n$ be a space whose homology groups are given by $H_k(X_n; \ZZ) \cong \ZZ/k\ZZ$ for $0 \leq k \leq n$ and which vanish for $k > n$.
Compute the homology $H_*(X_3 \times X_5; \ZZ)$.
:::

::: {.solution}

::: pf

::: pf-step
Interpreting $\ZZ/0\ZZ$ as $\ZZ$ and $\ZZ/1\ZZ$ as $0$, the nonzero homology groups are
$$
H_0(X_3)=\ZZ,\quad H_2(X_3)=\ZZ/2,\quad H_3(X_3)=\ZZ/3,
$$
and
$$
H_0(X_5)=\ZZ,\ H_2=\ZZ/2,\ H_3=\ZZ/3,\ H_4=\ZZ/4,\ H_5=\ZZ/5.
$$

::: pf-proof
This is the given formula $H_k(X_n)=\ZZ/k\ZZ$ in the indicated range.
:::

:::

::: pf-step
The tensor terms in the integral Künneth theorem give
$$
\begin{array}{c|c}
q&\displaystyle\bigoplus_{i+j=q}H_i(X_3)\otimes H_j(X_5)\\ \hline
0&\ZZ\\
2&(\ZZ/2)^2\\
3&(\ZZ/3)^2\\
4&\ZZ/4\oplus\ZZ/2\\
5&\ZZ/5\\
6&\ZZ/2\oplus\ZZ/3\\
\end{array}
$$
with zero tensor terms in the other degrees.

::: pf-proof
Use $\ZZ/a\otimes\ZZ/b\cong\ZZ/\gcd(a,b)$ for $a,b>1$ and tensoring with $\ZZ$ unchanged.
:::

:::

::: pf-step
The only nonzero Tor terms are
$$
\operatorname{Tor}(\ZZ/2,\ZZ/2)\cong\ZZ/2
$$
in total degree $5$, and
$$
\operatorname{Tor}(\ZZ/2,\ZZ/4)\oplus
\operatorname{Tor}(\ZZ/3,\ZZ/3)
\cong\ZZ/2\oplus\ZZ/3
$$
in total degree $7$.

::: pf-proof
A Tor term from bidegree $(i,j)$ contributes to $H_{i+j+1}$, and $\operatorname{Tor}(\ZZ/a,\ZZ/b)\cong\ZZ/\gcd(a,b)$.
:::

:::

::: pf-step
Therefore, using the noncanonical splitting in the Künneth theorem,
$$
\boxed{H_q(X_3\times X_5;\ZZ)\cong
\begin{cases}
\ZZ,&q=0,\\
(\ZZ/2)^2,&q=2,\\
(\ZZ/3)^2,&q=3,\\
\ZZ/4\oplus\ZZ/2,&q=4,\\
\ZZ/10,&q=5,\\
\ZZ/6,&q=6,7,\\
0,&\text{otherwise}.
\end{cases}}
$$

::: pf-proof
In degree $5$, $\ZZ/5\oplus\ZZ/2\cong\ZZ/10$; in degrees $6$ and $7$, $\ZZ/2\oplus\ZZ/3\cong\ZZ/6$.
:::

:::

:::

:::
