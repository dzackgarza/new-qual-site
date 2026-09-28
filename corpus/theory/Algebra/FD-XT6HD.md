---
schema: qual/card@1
id: FD-XT6HD
kind: definition
title: Rational canonical form
prompts:
- 'Which decomposition of $V$ as a $k[x]\dash$module gives the rational canonical form of $\phi: V \to V$?'
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Structure Theorem
  - Modules
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
