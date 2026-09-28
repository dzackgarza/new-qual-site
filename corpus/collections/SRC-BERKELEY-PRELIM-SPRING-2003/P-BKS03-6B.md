---
schema: qual/card@1
id: P-BKS03-6B
kind: problem
title: Elements of equal finite order in $\operatorname{PGL}_2(\CC)$ are conjugate up to a power
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $a,b\in\operatorname{PGL}_2(\mathbb C)$ have the same finite order $n$.
Prove that there exists $c\in\operatorname{PGL}_2(\mathbb C)$ such that $cac^{-1}$ is a power of $b$.
:::

::: {.solution}
Choose $A\in\operatorname{GL}_2(\CC)$ representing $a$. Then $A^n=\lambda I$ for some $\lambda\in\CC^*$. By dividing $A$ by an $n$-th root of $\lambda$, we may assume without loss of generality that $A^n=I$. Since the polynomial $x^n-1$ has distinct roots, $A$ is diagonalizable, and the eigenvalues must be $n$-th roots of unity.
Without loss of generality, we may conjugate, and divide $A$ by the first root of unity, to assume that $A=\begin{pmatrix}1&0\\0&\zeta\end{pmatrix}$. If for some $m\geq1$, $A^m=sI$ for some $s\in\CC^*$, then comparing upper left hand corners shows that $s=1$. Since the order of $a$ is exactly $n$, the previous sentence implies that $A$ has order exactly $n$, so that $\zeta$ is a primitive $n$-th root of unity.

Similarly, $b$ is represented by a matrix that is conjugate to $B=\begin{pmatrix}1&0\\0&\zeta'\end{pmatrix}$ for some primitive $n$-th root of unity $\zeta'$. Then $\zeta'$ is a power of $\zeta$, so $B$ is a power of $A$, and $b$ is conjugate to a power of $a$.
:::
