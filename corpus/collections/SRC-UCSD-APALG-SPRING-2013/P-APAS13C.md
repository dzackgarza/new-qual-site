---
schema: qual/card@1
id: P-APAS13C
kind: problem
title: Matrix $p$- and Frobenius norms; diagonal $p$-norm; two explicit $\norm{B}_2$ computations
classification:
  areas:
  - applied-algebra
  topics:
  - Norms
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the definitions of the induced p-norm and the
    Frobenius norm with tr(A^H A) = sum |a_ij|^2, the two-sided estimate for a diagonal
    matrix at every p including p = infinity (upper bound entrywise, attainment at a
    standard basis vector), and both 2-norm computations: for [[0,b^H],[b,0]] the action
    B(x_0,w) = (b^H w, x_0 b) with the eigenvectors (1, u) and (1, -u) at eigenvalues plus
    and minus ||b||, and the kernel on the orthogonal complement of b; and for bb^H the
    eigenvector b at ||b||^2 and the kernel on the complement. The argument is the card's
    own; no retained set is cited. No repair needed to the answers.
---

::: {.problem}
(a) Define the $p$-norm $\norm{A}_p$ and Frobenius norm $\norm{A}_F$ of a matrix $A\in M_{m,n}$.

(b) Suppose that $D\in M_n$ with $D=\operatorname{diag}(d_1,d_2,\ldots,d_n)$.
Prove that for all $1\le p\le\infty$ the $p$-norm of $D$ is given by $\norm{D}_p=\max_{1\le i\le n}\abs{d_i}$.

(c) Given $b\in\CC^{n-1}$, find $\norm{B}_2$ for the matrices
$$
B=\begin{pmatrix} 0 & b^H \\ b & 0 \end{pmatrix}
\quad\text{and}\quad
B=bb^H.
$$
(Show your work.
Simply writing down the answer will not be sufficient.)
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it.

For $x=(x_{1},\dots,x_{n})^{\mathsf T}\in\CC^{n}$ write $\norm{x}_{p}=\big(\sum_{i}\abs{x_{i}}^{p}\big)^{1/p}$ for $1\le p<\infty$ and $\norm{x}_{\infty}=\max_{i}\abs{x_{i}}$.

::: pf

::: {.pf-step #definitions}
(a) $\norm{A}_{p}=\sup_{x\ne0}\norm{Ax}_{p}/\norm{x}_{p}$ for $A\in M_{m,n}$, and $\norm{A}_{F}=\big(\sum_{i,j}\abs{a_{ij}}^{2}\big)^{1/2}=\sqrt{\operatorname{tr}(A^{H}A)}$.

::: pf-proof
The induced $p$-norm is the supremum of the ratio over nonzero vectors, which is finite because $x\mapsto\norm{Ax}_{p}$ is continuous and the unit sphere of $\norm{\cdot}_{p}$ is compact. For the Frobenius norm, the $(j,j)$ entry of $A^{H}A$ is $\sum_{i}\overline{a_{ij}}a_{ij}=\sum_{i}\abs{a_{ij}}^{2}$, so its trace is $\sum_{i,j}\abs{a_{ij}}^{2}$, whose square root is the displayed sum.
:::

:::

::: {.pf-step #upper}
(b) For $D=\operatorname{diag}(d_{1},\dots,d_{n})$ with $M=\max_{i}\abs{d_{i}}$ one has $\norm{Dx}_{p}\le M\norm{x}_{p}$ for every $x$ and every $1\le p\le\infty$, hence $\norm{D}_{p}\le M$.

::: pf-proof
For $1\le p<\infty$, $\norm{Dx}_{p}^{p}=\sum_{i}\abs{d_{i}x_{i}}^{p}=\sum_{i}\abs{d_{i}}^{p}\abs{x_{i}}^{p}\le M^{p}\sum_{i}\abs{x_{i}}^{p}=M^{p}\norm{x}_{p}^{p}$. For $p=\infty$, $\norm{Dx}_{\infty}=\max_{i}\abs{d_{i}}\abs{x_{i}}\le M\max_{i}\abs{x_{i}}=M\norm{x}_{\infty}$. Dividing by $\norm{x}_{p}\ne0$ and taking the supremum gives the bound on the induced norm.
:::

:::

::: {.pf-step #attained}
(b) $\norm{D}_{p}\ge M$, so $\norm{D}_{p}=\max_{i}\abs{d_{i}}$.

::: pf-proof
Choose $j$ with $\abs{d_{j}}=M$ and take $x=e_{j}$, the $j$-th standard basis vector. Then $De_{j}=d_{j}e_{j}$, so $\norm{De_{j}}_{p}/\norm{e_{j}}_{p}=\abs{d_{j}}=M$ for every $p$, and the supremum defining $\norm{D}_{p}$ is at least $M$. With step [](#upper){.pf-ref} this gives equality.
:::

:::

::: {.pf-step #first-matrix}
(c) For $b\in\CC^{n-1}$ and $B=\begin{pmatrix}0&b^{H}\\ b&0\end{pmatrix}$ one has $\norm{B}_{2}=\norm{b}_{2}$.

::: pf-proof
$B$ is Hermitian, so its $2$-norm is the largest modulus of an eigenvalue. If $b=0$ then $B=0$ and the norm is $0=\norm{b}_{2}$. Otherwise put $u=b/\norm{b}_{2}$; writing a vector of $\CC^{n}$ as $(x_{0},w)$ with $x_{0}\in\CC$ and $w\in\CC^{n-1}$, one has $B(x_{0},w)=(b^{H}w,\ x_{0}b)$. Hence
$$
B(1,u)=(\norm{b}_{2},\,b)=\norm{b}_{2}(1,u),\qquad B(1,-u)=(-\norm{b}_{2},\,b)=-\norm{b}_{2}(1,-u),
$$
using $b^{H}u=\norm{b}_{2}$ and $u=b/\norm{b}_{2}$. And $B(0,v)=(b^{H}v,0)=0$ whenever $v\perp b$, a subspace of dimension $n-2$. So the eigenvalues are $\norm{b}_{2}$, $-\norm{b}_{2}$ and $0$ with multiplicity $n-2$, and the largest modulus is $\norm{b}_{2}$.
:::

:::

::: {.pf-step #second-matrix}
(c) For $B=bb^{H}$ one has $\norm{B}_{2}=\norm{b}_{2}^{2}$.

::: pf-proof
$bb^{H}$ is Hermitian and positive semidefinite, since $x^{H}bb^{H}x=\abs{b^{H}x}^{2}\ge0$; its $2$-norm is again the largest eigenvalue. Now $Bb=b(b^{H}b)=\norm{b}_{2}^{2}b$, so $\norm{b}_{2}^{2}$ is an eigenvalue with eigenvector $b$, and for $v\perp b$ one has $Bv=b(b^{H}v)=0$, so $0$ is an eigenvalue on a subspace of dimension $n-2$. These account for all $n-1$ eigenvalues, and the largest is $\norm{b}_{2}^{2}$.
:::

:::

::: {.pf-step}
Parts (a), (b) and (c) hold.

::: pf-proof
Step [](#definitions){.pf-ref} is (a), steps [](#upper){.pf-ref} and [](#attained){.pf-ref} are (b), and steps [](#first-matrix){.pf-ref} and [](#second-matrix){.pf-ref} are the two computations of (c).
:::

:::

:::
:::
