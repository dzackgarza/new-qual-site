---
schema: qual/card@1
id: P-APAS24C
kind: problem
title: Hermitian matrices are those with real quadratic forms $x^HAx$
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The converse is the standard basis-vector computation and every entry is now distinguished: e_i gives the vanishing of the diagonal entries, e_i + e_j gives b_ij + b_ji = 0, and e_i + i e_j gives i(b_ij - b_ji) = 0, with the two coefficient signs written out (conj(i) = -i) since that is where such an argument usually goes wrong. The one-directional implication now shows conj(x^H A x) = x^H A^H x by taking the conjugate transpose of a 1 x 1 matrix. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair.
---

::: {.problem}
Let $A\in M_n(\CC)=\CC^{n\times n}$.
Prove that $A$ is Hermitian if and only if $x^HAx\in\RR$ for all $x\in\CC^n$.

Note: $x^H=\overline{x^T}$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Write $x^H=\overline{x^T}$ and $A^H=\overline{A^T}$, so that $(Ax)^Hy=x^HA^Hy$ for all $x,y\in\CC^n$; also $\overline{\lambda}$ denotes the complex conjugate of a scalar and $e_1,\dots,e_n$ the standard basis of $\CC^n$.

::: pf

::: {.pf-step #hermitianreal}
If $A$ is Hermitian, then $x^HAx\in\RR$ for every $x\in\CC^n$.

::: pf-proof
For a scalar $\lambda=x^HAx$, $\lambda\in\RR$ exactly when $\lambda=\overline\lambda$, and $\overline\lambda=\overline{x^HAx}=(x^HAx)^H=x^HA^Hx$, since conjugating and transposing a $1\times1$ matrix leaves it unchanged. If $A$ is Hermitian then $A^H=A$, so $\overline\lambda=x^HAx=\lambda$ and $\lambda\in\RR$.
:::

:::

::: {.pf-step #antisymmetric}
Conversely, if $x^HAx\in\RR$ for every $x$, then $B=A-A^H$ satisfies $x^HBx=0$ for every $x\in\CC^n$.

::: pf-proof
For $x\in\CC^n$ the number $x^HAx$ is a $1\times1$ matrix and $\overline{x^HAx}=(x^HAx)^H=x^HA^Hx$. If $x^HAx\in\RR$ then $x^HAx=\overline{x^HAx}=x^HA^Hx$, so
$$
x^HBx=x^H(A-A^H)x=x^HAx-x^HA^Hx=0.
$$
:::

:::

::: {.pf-step #diagonal}
$b_{ii}=0$ for every $i$.

::: pf-proof
$e_i^HBe_i=b_{ii}$ is the $(i,i)$ entry of $B$, and step [](#antisymmetric){.pf-ref} gives $e_i^HBe_i=0$.
:::

:::

::: {.pf-step #offdiagonal}
For $i\ne j$: $b_{ij}+b_{ji}=0$ and $b_{ij}-b_{ji}=0$, hence $b_{ij}=b_{ji}=0$.

::: pf-proof
Write $B=(b_{pq})$. For $u=e_i+e_j$, the $(p,q)$ summands of $u^HBu=\sum_{p,q}\overline{u_p}\,b_{pq}u_q$ that survive are $b_{ii},b_{ij},b_{ji},b_{jj}$, so by step [](#diagonal){.pf-ref}
$$
0=(e_i+e_j)^HB(e_i+e_j)=b_{ii}+b_{ij}+b_{ji}+b_{jj}=b_{ij}+b_{ji}.
$$
For $u=e_i+ie_j$ the coefficients are $\overline{u_i}=1$, $u_j=i$, $\overline{u_j}=-i$, $u_i=1$, so
$$
0=(e_i+ie_j)^HB(e_i+ie_j)=b_{ii}+i\,b_{ij}-i\,b_{ji}+\abs{i}^2b_{jj}=i\,(b_{ij}-b_{ji})
$$
again by step [](#diagonal){.pf-ref}. Dividing by $i\ne0$ gives $b_{ij}-b_{ji}=0$; with $b_{ij}+b_{ji}=0$ this forces $2b_{ij}=0$ and $2b_{ji}=0$.
:::

:::

::: {.pf-step #conclusion}
$A=A^H$.

::: pf-proof
$B=A-A^H$ has all entries zero by steps [](#diagonal){.pf-ref} and [](#offdiagonal){.pf-ref}, so $B=0$. Together with step [](#hermitianreal){.pf-ref} this proves both implications.
:::

:::

:::
:::
