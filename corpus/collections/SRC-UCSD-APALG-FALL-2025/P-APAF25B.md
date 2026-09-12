---
schema: qual/card@1
id: P-APAF25B
kind: problem
title: Vanishing Hermitian quadratic form forces $A=0$
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
relations: []
review: draft
---

::: problem
Given $n\geq 1$, let $A\in M_n(\mathbb{C})=\mathbb{C}^{n\times n}$.
Prove if $x^H Ax=0$, for all $x\in\mathbb{C}^n$, then $A=0$.

(Notationally: for all $m,n\geq 1$, $z^H=\overline{z}^T$ for all $z\in M_{m,n}(\mathbb{C})=\mathbb{C}^{m\times n}$.)
:::

::: {.solution}
Write \(A=(a_{ij})\).

<1>1. Every diagonal entry of \(A\) is zero.
::: {.proof}
For the standard basis vector \(e_i\), the hypothesis gives
\[
0=e_i^HAe_i=a_{ii}.
\]
Thus \(a_{ii}=0\) for every \(i\).
:::

<1>2. For \(i\ne j\), one has
\[
a_{ij}+a_{ji}=0.
\]
::: {.proof}
Apply the hypothesis to \(x=e_i+e_j\). Using <1>1,
\[
0=(e_i+e_j)^HA(e_i+e_j)
=a_{ii}+a_{ij}+a_{ji}+a_{jj}
=a_{ij}+a_{ji}.
\]
:::

<1>3. For \(i\ne j\), one also has
\[
a_{ij}-a_{ji}=0.
\]
::: {.proof}
Apply the hypothesis to \(x=e_i+i e_j\). Since
\[
x^H=e_i^H-i e_j^H,
\]
we obtain, again using <1>1,
\[
\begin{aligned}
0
&=(e_i^H-i e_j^H)A(e_i+i e_j)\\
&=a_{ii}+i a_{ij}-i a_{ji}+a_{jj}\\
&=i(a_{ij}-a_{ji}).
\end{aligned}
\]
Hence \(a_{ij}=a_{ji}\).
:::

<1>4. Therefore \(A=0\).
::: {.proof}
For \(i\ne j\), <1>2 gives \(a_{ji}=-a_{ij}\), while <1>3 gives \(a_{ji}=a_{ij}\). Hence \(2a_{ij}=0\). Over \(\mathbb C\), this implies \(a_{ij}=0\). Together with <1>1, every entry of \(A\) is zero.
:::
:::
