---
schema: qual/card@1
id: P-ALGS04B
kind: problem
title: "Sylow 17-subgroups and elements of order 17 in GL(2, Z_17)"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $G$ be the group of $2 \times 2$ invertible matrices with entries in the finite field $\mathbb{Z}_p$.
Then $|G| = (p-1)^2 p(p+1)$.
Assume that $p = 17$, so $|G| = 2^9 \cdot 3^2 \cdot 17$.

(a) Let $x$ be an element of $G$ of order 17. Prove that $x$ is conjugate to an element of the form $\begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}$.

(b) Prove that $G$ contains 18 Sylow 17-subgroups.

Hint: Use the fact that the upper triangular matrices contain a Sylow 17-subgroup as a normal subgroup.

(c) How many elements in $G$ have order 17?
:::

::: {.solution}
<1>1. Let $B$ be upper triangular Sylow $17$-subgroup.
::: {.proof}
order $17$.
:::

<1>2. (a) Any $x$ of order $17$ is unipotent, conjugate to $\begin{pmatrix}1&b\\0&1\end{pmatrix}$.
::: {.proof}
$x$ has eigenvalue $1$ (order $17$ in $\F_{17}^\times$ is $16$, so eigenvalues $1$).
:::

<1>3. (b) $N_G(B)=B$, and $n_{17}=[G:N_G(B)]=|G|/17=18$.
::: {.proof}
Sylow count.
:::

<1>4. (c) Each Sylow has $16$ non-identity elements of order $17$, distinct Sylows intersect trivially, so $18\cdot16=288$ elements of order $17$.
::: {.proof}
<1>3.
:::

<1>5. Q.E.D.
::: {.proof}
<1>2 and <1>4.
:::
:::
