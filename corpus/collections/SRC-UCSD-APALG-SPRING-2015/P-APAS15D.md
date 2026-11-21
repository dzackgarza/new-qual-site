---
schema: qual/card@1
id: P-APAS15D
kind: problem
title: Finite-group complex matrix representations are diagonalizable; infinite counterquestion
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: an element of a finite group has
    finite order $m$, so $X(g)^m=I$; the minimal polynomial generates the annihilator ideal, so it
    divides $t^m-1$; $t^m-1$ is squarefree in characteristic $0$ because its derivative $mt^{m-1}$
    vanishes only at $0$, where $t^m-1=-1$; a divisor of a squarefree polynomial is squarefree; and
    a complex matrix is diagonalizable exactly when its minimal polynomial is squarefree. The
    counterexample is checked too: $J^n$ is a homomorphism, and $J-I\ne0$ with $(J-I)^2=0$ gives
    minimal polynomial $(t-1)^2$. Presentation repairs: `\mathrm{GL}_n` and `\operatorname{GL}_2`
    are written `\GL`, the vocabulary macro (STYLE-03/04). The statement is Problem D of the Spring
    2015 applied-algebra examination; the collection's provenance is that paper, so no retained
    solution set covers it.
---

::: {.problem}
Let $G$ be a finite group and let $X \colon G \to \GL_n(\CC)$ be a complex matrix representation of $G$.
For any $g \in G$, prove that the matrix $X(g)$ is diagonalizable.
Is this still true if the group $G$ is infinite?
:::

::: {.solution}
The collection's provenance is the examination paper, so no retained solution set covers the problem and the argument is the card's own. Write $X\colon G\to\GL_n(\CC)$ for the representation and $I$ for the identity matrix.

::: pf

::: {.pf-step #finite-order}
For $g\in G$ the matrix $X(g)$ satisfies $X(g)^m=I$ for $m=\abs{g}$, the order of $g$.

::: pf-proof
$G$ is finite, so every element has finite order. Since $X$ is a homomorphism, $X(g)^m=X(g^m)=X(e)=I$ for such $m$.
:::

:::

::: {.pf-step #minimal-divides}
The minimal polynomial $\mu$ of $X(g)$ divides $t^m-1$.

::: pf-proof
A polynomial $p$ satisfies $p(X(g))=0$ exactly when $\mu$ divides $p$: the minimal polynomial generates the ideal of annihilating polynomials in $\CC[t]$. By step [](#finite-order){.pf-ref}, $t^m-1$ annihilates $X(g)$.
:::

:::

::: {.pf-step #squarefree}
$t^m-1$ has $m$ distinct roots in $\CC$, so every divisor of it has distinct roots.

::: pf-proof
The derivative is $mt^{m-1}$, whose only root is $0$, and $0^m-1=-1\ne0$, so $t^m-1$ and its derivative have no common root; hence $t^m-1$ has no repeated root. Over $\CC$ it therefore factors as a product of $m$ distinct linear factors. A divisor of a polynomial with distinct roots has distinct roots, its roots being some of those.
:::

:::

::: {.pf-step #diagonalizable}
Every $X(g)$ is diagonalizable.

::: pf-proof
A matrix over $\CC$ is diagonalizable exactly when its minimal polynomial has no repeated root. By steps [](#minimal-divides){.pf-ref} and [](#squarefree){.pf-ref}, $\mu$ divides $t^m-1$ and so has distinct roots; hence $X(g)$ is diagonalizable for each $g\in G$.
:::

:::

::: {.pf-step}
The conclusion fails for an infinite group.

::: pf-proof
Take $G=\ZZ$ and $X(n)=J^n$ with $J=\begin{pmatrix}1&1\\0&1\end{pmatrix}$; this is a homomorphism because $J$ is invertible and $J^{m+n}=J^mJ^n$. The matrix $X(1)=J$ has characteristic polynomial $(t-1)^2$ and $J-I=\begin{pmatrix}0&1\\0&0\end{pmatrix}\ne0$, so its minimal polynomial is $(t-1)^2$, which has a repeated root; hence $J$ is not diagonalizable, and the finite-group hypothesis is essential.
:::

:::

:::
:::
