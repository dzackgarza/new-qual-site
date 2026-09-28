---
schema: qual/card@1
id: P-APAS24A
kind: problem
title: Invariant orthogonal complement implies an eigenvector of $A^H$
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Inner Product Spaces
relations: []
review: draft
---

::: {.problem}
Let $A\in M_n(\mathbb{C})=\mathbb{C}^{n\times n}$ and let $x\in\mathbb{C}^n$, $x\neq 0$.
Prove that if
\[
S=(\operatorname{span}\{x\})^\perp\subseteq\mathbb{C}^n
\]
is an invariant subspace of $A$, meaning $AS\subseteq S$, then $x$ is an eigenvector of $A^H$.

Note: $A^H=\overline{A^T}$.
:::

::: {.solution}
Let $S=(\operatorname{span}\{x\})^\perp$. For every $s\in S$, the invariance hypothesis gives $As\in S$. Hence
\[
\langle As,x\rangle=0.
\]
Using the adjoint,
\[
\langle s,A^Hx\rangle=\langle As,x\rangle=0
\]
for every $s\in S$. Therefore $A^Hx$ is orthogonal to $S$, i.e.
\[
A^Hx\in S^\perp.
\]
Since
\[
S^\perp=\operatorname{span}\{x\},
\]
there is a scalar $\lambda\in\mathbb C$ such that
\[
A^Hx=\lambda x.
\]
Because $x\ne0$, this shows that $x$ is an eigenvector of $A^H$.
:::
