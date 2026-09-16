---
schema: qual/card@1
id: P-TOPS24E
kind: problem
title: $\operatorname{Tor}(M,\mathbb Z_2)$ for a presented abelian group
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.problem}
Let $M$ be the abelian group given by the following presentation with three generators and three relators: $\langle a, b, c : 2a + 3b + 5c,\ 3a + 5b + 2c,\ 5a + 2b + 3c \rangle$.
Compute $\operatorname{Tor}(M, \mathbb{Z}_2)$.
:::

::: {.solution}
<1>1. Let $A$ be the relation matrix
$$A=\begin{pmatrix}2&3&5\\3&5&2\\5&2&3\end{pmatrix}.$$
Its determinant is $-70$.
::: {.proof}
Expanding along the first row gives
$$2(15-4)-3(9-10)+5(6-25)=22+3-95=-70.$$
:::

<1>2. The Smith normal form of $A$ has invariant factors $1,1,70$.
::: {.proof}
The gcd of all entries is $1$, so the first invariant factor is $1$. The $2\times2$ minor from the first two rows and columns is $2\cdot5-3\cdot3=1$, so the product of the first two invariant factors is $1$. Their total product has absolute value $|\det A|=70$.
:::

<1>3. Therefore
$$M\cong\mathbb Z/70.$$
::: {.proof}
The presented abelian group is the cokernel of $A$, and its decomposition is read from the Smith normal form in <1>2.
:::

<1>4. For cyclic groups,
$$\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\cong\mathbb Z/\gcd(n,m).$$
Hence
$$\boxed{\operatorname{Tor}(M,\mathbb Z_2)\cong\mathbb Z/2.}$$
::: {.proof}
Apply the standard free resolution of $\mathbb Z/n$ and take $n=70,m=2$.
:::
:::
