---
schema: qual/card@1
id: P-FHW1-01
kind: problem
title: Algebraic elements via invariant finite-dimensional subspaces
classification:
  areas: [algebra]
  topics: [Field Extensions, Minimal and Characteristic Polynomials]
relations: []
review: draft
audit:
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Transcribed from the MinerU Flash extraction of assets/attachments/fields-homework-1.pdf and checked against the page image.
- event: source-corrected
  by: claude
  date: 2026-10-31
  note: >-
    The sheet's problem 1(a) asks for a finite-dimensional K-subspace L with
    alpha L inside L and states no nonvanishing condition. With L = {0} the
    condition holds for every alpha in F, so the converse direction fails as
    the sheet writes it (for F = K(t) and alpha = t no nonzero such L exists).
    The statement now requires L to be nonzero. Both directions of the corrected
    statement, and the fact that the printed hypothesis holds for L = 0, are
    certified in Lean in proofs/cards/FieldHomework1.lean; COMPLAINTS.md records
    the source defect and the certificate.
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Fix a field extension $K\subset F$.

(a) Show that $\alpha\in F$ is algebraic over $K$ if and only if $F$ contains a nonzero finite-dimensional $K$-vector subspace $L$ such that $\alpha\cdot L\subset L$.

(b) If the conditions of (a) are satisfied, let $A\colon L\to L$ be the $K$-linear operator of multiplication by $\alpha$. Show that its minimal polynomial in the sense of linear algebra is equal to the minimal polynomial of $\alpha$ in the field-theoretic sense.
:::

::: {.solution}
Fix $\alpha\in F$ and a $K$-subspace $L\subseteq F$ with $\alpha L\subseteq L$, and write $A_L\colon L\to L$ for the $K$-linear map $v\mapsto\alpha v$.
Two monic polynomials over $K$ are equal exactly when each divides the other.

::: pf

::: {.pf-step #part-a}
(a) $\alpha$ is algebraic over $K$ if and only if $F$ contains a nonzero finite-dimensional $K$-subspace $L$ with $\alpha L\subseteq L$.

::: pf-proof
Suppose first that $\alpha$ is algebraic, let $m_\alpha\in K[x]$ be its minimal polynomial and $n=\deg m_\alpha\ge1$, and let $L$ be the $K$-span of $1,\alpha,\ldots,\alpha^{n-1}$.
The set $L$ contains $1$, so $L\ne0$, and it is spanned by $n$ elements, so $\dim_K L\le n<\infty$.
For $p\in K[x]$ of degree less than $n$ the product $\alpha p$ has degree less than $n+1$, and reducing it modulo $m_\alpha$ gives $q\in K[x]$ of degree less than $n$ with $\alpha p(\alpha)=q(\alpha)$; hence $\alpha L\subseteq L$.

Conversely, let $L\ne0$ be finite-dimensional with $\alpha L\subseteq L$ and put $n=\dim_KL$.
For $v\in L$ the $n+1$ elements $v,\alpha v,\ldots,\alpha^nv$ lie in $L$, so they are $K$-linearly dependent: there are $c_0,\ldots,c_n\in K$, not all zero, with $\sum_{i=0}^n c_i\alpha^iv=0$.
Since $L\ne0$ we may choose $v\ne0$, and multiplying by $v^{-1}$ in the field $F$ gives $\sum_{i=0}^n c_i\alpha^i=0$.
The polynomial $\sum_{i=0}^n c_ix^i\in K[x]$ is then nonzero, so $\alpha$ is algebraic over $K$.
:::

:::

::: {.pf-step #part-b}
(b) If $L$ is a nonzero finite-dimensional subspace as in (a), then the minimal polynomial of $A_L$ equals $m_\alpha$.

::: pf-proof
The polynomial $m_\alpha$ annihilates $A_L$, because $m_\alpha(A_L)$ is multiplication by $m_\alpha(\alpha)=0$; hence the minimal polynomial of $A_L$ divides $m_\alpha$.
Conversely the minimal polynomial $m_{A_L}$ of $A_L$ satisfies $m_{A_L}(A_L)=0$, so $m_{A_L}(\alpha)v=0$ for every $v\in L$; taking $v\ne0$ and cancelling it in the field $F$ gives $m_{A_L}(\alpha)=0$, hence $m_\alpha$ divides $m_{A_L}$.
Both are monic, so they are equal.
:::

:::

:::

:::

::: {.remark}
The sheet prints problem 1(a) with no nonvanishing condition on $L$, and with $L=\{0\}$ the printed hypothesis holds for every $\alpha\in F$, so the printed statement is false.
The statement above adds $L\ne0$.
The refutation of the printed form and both directions of the corrected form are checked in Lean in `proofs/cards/FieldHomework1.lean`.
:::
