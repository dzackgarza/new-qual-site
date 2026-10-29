---
schema: qual/card@1
id: FD-XT6HD
kind: definition
title: Rational canonical form
prompts:
- 'Which decomposition of $V$ as a $k[x]\dash$module gives the rational canonical form of $\phi\colon V \to V$?'
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Structure Theorem
  - Modules
  - Matrices
relations: []
review: draft
---

::: {.definition}
Let $k$ be a field, let $V$ be a finite-dimensional $k$-vector space, and let $\phi\colon V\to V$ be a $k$-linear map.
Make $V$ a $k[x]$-module by letting $x$ act as $\phi$.
By the structure theorem for finitely generated modules over the [[D-HTIL5|principal ideal domain]] $k[x]$, there are unique monic nonconstant polynomials $r_1\divides r_2\divides\cdots\divides r_t$ in $k[x]$ and a decomposition $V=V_1\oplus\cdots\oplus V_t$ into $\phi$-invariant subspaces with
$$
V_i\cong k[x]/(r_i)\quad\text{as } k[x]\text{-modules},\qquad 1\le i\le t.
$$
The \dfn{rational canonical form} of $\phi$ is the block diagonal matrix
$$
\diag\qty{C_{r_1},C_{r_2},\ldots,C_{r_t}},
$$
where $C_{r_i}$ is the [[D-HJR7M|companion matrix]] of $r_i$.
:::

::: {.remark}
The polynomial $r_i$ is the [[D-GK5SF|minimal polynomial]] of the restriction $\phi|_{V_i}$.
If $v_i\in V_i$ corresponds to the class of $1$ in $k[x]/(r_i)$ and $d_i=\deg r_i$, then $v_i,\phi(v_i),\ldots,\phi^{d_i-1}(v_i)$ is a basis of $V_i$, and the matrix of $\phi|_{V_i}$ in this basis is $C_{r_i}$.
Concatenating these bases gives a basis of $V$ in which $\phi$ has its rational canonical form.
:::

::: {.proposition}
With $k$, $V$, $\phi$ and $r_1\divides\cdots\divides r_t$ as above:

- If the matrix of $\phi$ in some basis of $V$ is $\diag\qty{C_{s_1},\ldots,C_{s_m}}$ for monic nonconstant $s_1\divides\cdots\divides s_m$, then $m=t$ and $s_i=r_i$ for all $i$. So the rational canonical form is the unique matrix of this shape that represents $\phi$, and two matrices in $\Mat_{n\times n}(k)$ are similar if and only if they have the same rational canonical form.

- The [[D-GK5SF|minimal polynomial]] of $\phi$ is $r_t$, and its characteristic polynomial is $r_1r_2\cdots r_t$.
:::

::: {.proof}
On $k[x]/(s)$ with $s$ monic of degree $d$, multiplication by $x$ has matrix $C_s$ in the basis $1,x,\ldots,x^{d-1}$.
So if $\phi$ has matrix $\diag\qty{C_{s_1},\ldots,C_{s_m}}$, then $V\cong\bigoplus_i k[x]/(s_i)$ as $k[x]$-modules, and uniqueness of the invariant factors gives $s_i=r_i$.
Matrices $A,B$ are similar if and only if $k^n$ with $x$ acting by $A$ and $k^n$ with $x$ acting by $B$ are isomorphic $k[x]$-modules, that is, if and only if they have the same invariant factors.

Since $r_i\divides r_t$ for every $i$, $r_t(\phi)$ vanishes on each $V_i$, so $\min_\phi\divides r_t$.
Since $\min_\phi(\phi)$ vanishes on $V_t\cong k[x]/(r_t)$, whose annihilator is $(r_t)$, $r_t\divides\min_\phi$; both are monic, so $\min_\phi=r_t$.
Expanding $\det(xI-C_r)$ along its last column gives $r$, so the characteristic polynomial of the block diagonal matrix is $r_1\cdots r_t$.
:::
