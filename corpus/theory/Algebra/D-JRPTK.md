---
schema: qual/card@1
id: D-JRPTK
kind: definition
title: Equivalent matrices
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Canonical Forms
  - Linear Algebra
relations: []
review: draft
---

::: {.definition}
Let $R$ be a [[D-HTIL5|principal ideal domain]] and $m,n\geq 1$.
Matrices $A, B\in\Mat_{m\times n}(R)$ are \dfn{equivalent} if there exist $P\in\GL_m(R)$ and $Q\in\GL_n(R)$ such that $A = PBQ$.
:::

::: {.proposition}
Let $R$ be a principal ideal domain and $A,B\in\Mat_{m\times n}(R)$.
Then $A$ and $B$ are equivalent if and only if they have the same invariant factors, that is, the same Smith normal form.
In particular, equivalent matrices have the same rank, namely the number of nonzero invariant factors.
:::

::: {.proof}
Every matrix over $R$ is equivalent to its Smith normal form $\diag(d_1,\ldots,d_s,0,\ldots,0)$ with $d_1\divides d_2\divides\cdots\divides d_s$ nonzero, so matrices with the same Smith normal form are equivalent.
Conversely, for each $i$ let $\Delta_i(A)$ be a greatest common divisor of the $i\times i$ minors of $A$.
By the Cauchy--Binet formula, every $i\times i$ minor of $PBQ$ is an $R$-linear combination of $i\times i$ minors of $B$, so $\Delta_i(B)\divides\Delta_i(PBQ)$; applying this also to $B=P^{-1}AQ^{-1}$ shows that $\Delta_i(A)$ and $\Delta_i(B)$ are associates.
For the Smith normal form, $\Delta_i=d_1\cdots d_i$ for $i\leq s$ and $\Delta_i=0$ for $i>s$, so $s$ and the invariant factors $d_i=\Delta_i/\Delta_{i-1}$ are determined up to units by the equivalence class.
:::

::: {.example}
Over a field $k$, the invariant factors of a matrix of rank $s$ are $1,\ldots,1$ ($s$ times), so $A,B\in\Mat_{m\times n}(k)$ are equivalent if and only if they have the same rank.
Equivalence is coarser than [[D-JIGMN|similarity]]: if $A=PBP^{-1}$ then $A$ and $B$ are equivalent, but over $\QQ$ the matrices $I_2$ and $\diag(2,1)$ both have rank $2$, so they are equivalent, while they are not similar, since their eigenvalues differ.
:::
