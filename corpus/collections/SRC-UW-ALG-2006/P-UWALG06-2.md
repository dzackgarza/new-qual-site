---
schema: qual/card@1
id: P-UWALG06-2
kind: problem
title: Eigenvalues of a matrix with $A(A^c)^T=I_n$ satisfy $\lambda c(\lambda)=1$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Eigenvalues
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $c$ be an automorphism of order 1 or 2 of a field $F$.
Suppose that $c$ has the property that for any finite set $\{a_j\}_{j\in J}$ of nonzero elements of $F$, $\sum_{j\in J}a_jc(a_j)$ is nonzero.
For any $n\times n$-matrix $A=(a_{ij})$ with entries in $F$, let $A^c=(c(a_{ij}))$.
The $n\times n$ identity matrix is denoted by $I_n$.

Show that if $A$ has the property that $A(A^c)^T=I_n$, then every eigenvalue $\lambda\in F$ for $A$ satisfies the equation $\lambda c(\lambda)=1$.

(Remark: This result implies the familiar facts that the eigenvalues of an orthogonal matrix over the field of real numbers are in the set $\{\pm1\}$ and that the eigenvalues of a unitary matrix over the complex numbers have absolute value 1. One takes $c$ to be the identity map in the first case, complex conjugation in the second.)
:::

::: {.solution}
For column vectors $x,y$ over $F$ put $B(x,y)=\sum_ix_ic(y_i)$, and for a matrix $M$ write $M^c$ for the entrywise image under $c$; then $c(My)=M^cc(y)$ because $c$ is a field homomorphism, and the hypothesis says $B(x,x)\ne0$ for every $x\ne0$.

::: pf

::: {.pf-step #inverse}
$A^TA^c=I_n$.

::: pf-proof
Transposing $A(A^c)^T=I_n$ gives $A^cA^T=I_n$.
Two square matrices that multiply to the identity in one order multiply to it in the other, so $A^TA^c=I_n$ as well.
:::

:::

::: {.pf-step #isometry}
$B(Ax,Ay)=B(x,y)$ for all $x,y$.

::: pf-proof
Using $c(Ay)=A^cc(y)$ and step [](#inverse){.pf-ref},
$$
B(Ax,Ay)=(Ax)^Tc(Ay)=x^TA^TA^cc(y)=x^Tc(y)=B(x,y).
$$
:::

:::

::: {.pf-step #eigenvalue}
Every eigenvalue $\lambda\in F$ of $A$ satisfies $\lambda c(\lambda)=1$.

::: pf-proof
Let $v\ne0$ with $Av=\lambda v$. By step [](#isometry){.pf-ref} with $x=y=v$,
$$
B(v,v)=B(Av,Av)=B(\lambda v,\lambda v)=\lambda c(\lambda)B(v,v).
$$
The hypothesis gives $B(v,v)\ne0$, since the nonzero entries of $v$ form a finite set of nonzero elements of $F$ and the zero entries contribute nothing to the sum.
Hence $\lambda c(\lambda)=1$.
:::

:::

:::
:::
