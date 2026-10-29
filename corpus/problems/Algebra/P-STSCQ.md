---
schema: qual/card@1
id: P-STSCQ
kind: problem
title: Orders of elements of $\SL_2(\ZZ)$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Cyclic Groups
relations: []
review: draft
---

::: {.problem}
What are all possible orders of elements of $\SL_2(\ZZ)$?
:::

::: {.solution}

::: pf

::: {.pf-step #trace}

If $A\in\SL_2(\ZZ)$ has finite order, then $A$ is diagonalizable over $\CC$, $\chi_A(x)=x^2-(\tr A)x+1$, and $\tr A\in\{-2,-1,0,1,2\}$.

::: pf-proof

If $A^m=I$, the minimal polynomial of $A$ divides the separable polynomial $x^m-1$, so $A$ is diagonalizable with eigenvalues roots of unity. Since $\det A=1$, $\chi_A(x)=x^2-(\tr A)x+1$. The trace is an integer and a sum of two numbers of absolute value $1$, so $\abs{\tr A}\le2$.

:::

:::

::: {.pf-step #cases}

The order of a finite-order $A$ is $1,2,3,4$, or $6$ according as $\tr A=2,-2,-1,0,1$.

::: pf-proof

If $\tr A=\pm2$, then $\chi_A=(x\mp1)^2$, so both eigenvalues are $\pm1$ and, by step [](#trace){.pf-ref}, $A=\pm I$, of order $1$ or $2$. If $\tr A=-1$, Cayley--Hamilton gives $A^2+A+I=0$, so $A^3=I$ with $A\neq I$, and $A$ has order $3$. If $\tr A=0$, then $A^2=-I$, so $A$ has order $4$. If $\tr A=1$, then $A^2=A-I$ and $A^3=A^2-A=-I$, so $A^6=I$ while $A^2\neq I$ (else $A=2I$) and $A^3\neq I$; hence $A$ has order $6$.

:::

:::

::: pf-qed

All these orders occur: $I$, $-I$, $\begin{pmatrix}0&-1\\1&-1\end{pmatrix}$, $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, $\begin{pmatrix}0&-1\\1&1\end{pmatrix}$ have traces $2,-2,-1,0,1$, and $\begin{pmatrix}1&1\\0&1\end{pmatrix}^k=\begin{pmatrix}1&k\\0&1\end{pmatrix}\neq I$ for $k\ge1$ has infinite order. By step [](#cases){.pf-ref}, the possible orders are $\boxed{1,2,3,4,6,\infty}$.

:::

:::

:::
