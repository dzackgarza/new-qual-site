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
Let $A\in M_n(\CC)=\CC^{n\times n}$ and let $x\in\CC^n$, $x\neq 0$.
Prove that if
$$
S=(\operatorname{span}\{x\})^\perp\subseteq\CC^n
$$
is an invariant subspace of $A$, meaning $AS\subseteq S$, then $x$ is an eigenvector of $A^H$.

Note: $A^H=\overline{A^T}$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the orthogonality from invariance and the identification of $S^{\perp}$ as separate steps.

Let $A\in M_{n}(\CC)$, $x\ne0$, and $S=(\operatorname{span}\theset{x})^{\perp}$ with $AS\subseteq S$; the inner product is the standard one, linear in the first slot.

::: pf

::: {.pf-step #orthogonal}
$\langle s,A^{H}x\rangle=0$ for every $s\in S$.

::: pf-proof
For $s\in S$ the invariance hypothesis gives $As\in S$, and $S$ is the orthogonal complement of $\operatorname{span}\theset{x}$, so $\langle As,x\rangle=0$. By the defining property of the adjoint, $\langle s,A^{H}x\rangle=\langle As,x\rangle$, which is $0$.
:::

:::

::: {.pf-step #perp}
$S^{\perp}=\operatorname{span}\theset{x}$.

::: pf-proof
In finite dimensions $(\operatorname{span}\theset{x})^{\perp\perp}=\operatorname{span}\theset{x}$, since $\operatorname{span}\theset{x}$ is a finite-dimensional, hence closed, subspace.
:::

:::

::: {.pf-qed}
Step [](#orthogonal){.pf-ref} says $A^{H}x\in S^{\perp}$, so $A^{H}x\in\operatorname{span}\theset{x}$ by step [](#perp){.pf-ref}: there is $\lambda\in\CC$ with $A^{H}x=\lambda x$. Since $x\ne0$, this says $x$ is an eigenvector of $A^{H}$.
:::

:::

:::
