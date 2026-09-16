---
schema: qual/card@1
id: PR-XB3O7
kind: proposition
title: Irreducible polynomials over perfect fields are separable
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Fields
  - Irreducibility Criteria
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a [[D-KQFIV|perfect]] field.
Then every [[D-BVMTZ|irreducible]] polynomial $f\in k[x]$ is [[D-ZT46D|separable]].
:::

::: {.proof}
An irreducible $f$ has a repeated root if and only if $f'=0$ ([[PR-OMKPN]]).
If $\ch k=0$, then $f'\neq0$ for nonconstant $f$.
If $\ch k=p>0$ and $f'=0$, then $f=\sum_i a_ix^{pi}$; since $k^p=k$, write $a_i=b_i^p$ with $b_i\in k$, so $f=\qty{\sum_i b_ix^i}^p$ is not irreducible.
:::
