---
schema: qual/card@1
id: E-HAT-2.2-11
kind: problem
title: Homology of cube with opposite faces identified via one-quarter twist (quaternion group)
classification:
  areas:
  - topology
  topics:
  - Homology
  - CW Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
In an exercise for §1.2 we described a 3 dimensional CW complex obtained from the cube $I^3$ by identifying opposite faces via a one-quarter twist.
Compute the homology groups of this complex.
:::

::: {.solution}
Use the CW structure and face words computed for this cube in Hatcher Exercise 1.2.14. It has two vertices, four edges, three faces, and one $3$-cell. Choose one edge as a maximal tree. The other three edges give a basis $i,j,k$ for the cycle group $\ker(d_1:C_1\to C_0)$.

::: pf

::: {.pf-step #s1}

In this cycle basis, the cellular boundary $d_2:C_2\to\ker d_1$ has matrix
$$
M=
\begin{pmatrix}
1&-1&-1\\
-1&1&-1\\
-1&-1&1
\end{pmatrix}.
$$

::: pf-proof

The three attaching words in Exercise 1.2.14 give the relations $i=jk$, $j=ki$, and $k=ij$ in the fundamental group. Their exponent sums are respectively
$$
i-j-k,\qquad -i+j-k,\qquad -i-j+k.
$$
These are the three columns of $M$. The edge chosen as a tree contributes no cycle generator.

:::

:::

::: {.pf-step #s2}

The map $d_2$ is injective, and
$$
\operatorname{coker}(d_2:C_2\to\ker d_1)
\cong\ZZ/2\oplus\ZZ/2.
$$

::: pf-proof

The matrix is $2I-J$, where $J$ is the $3$ by $3$ all-ones matrix. Its eigenvalues over $\QQ$ are $-1,2,2$, so $\det M=-4$ and $d_2$ is injective. The gcd of its entries is $1$, and the gcd of its $2$ by $2$ minors is $2$. Hence its Smith invariant factors are $1,2,2$, giving the stated cokernel.

:::

:::

::: {.pf-step #s3}

The cellular boundary $d_3:C_3\to C_2$ is zero.

::: pf-proof

The chain identity gives $d_2d_3=0$. Since $d_2$ is injective by step [](#s2){.pf-ref}, its kernel is zero, so $d_3=0$.

:::

:::

::: pf-step

The homology groups of the cube quotient are
$$
\boxed{
H_0(X)\cong\ZZ,\quad
H_1(X)\cong\ZZ/2\oplus\ZZ/2,\quad
H_2(X)=0,\quad
H_3(X)\cong\ZZ,
}
$$
and $H_q(X)=0$ for $q>3$.

::: pf-proof

The $1$-skeleton is connected, so $H_0(X)=\ZZ$. The cycle group of the $1$-skeleton is free on $i,j,k$, and step [](#s2){.pf-ref} computes its quotient by the $2$-cell boundaries. Injectivity of $d_2$ and step [](#s3){.pf-ref} give $H_2=0$ and $H_3=C_3\cong\ZZ$. There are no higher cells.

:::

:::

:::
:::
