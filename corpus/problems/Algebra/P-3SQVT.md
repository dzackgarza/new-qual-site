---
schema: qual/card@1
id: P-3SQVT
kind: problem
title: A group of order $p^2q$ has a nontrivial normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Classification
relations: []
review: draft
---

::: {.problem}
Let $G$ be a group of order $p^2q$ for $p, q$ prime. Show that $G$ has a nontrivial normal subgroup.
:::

::: {.solution}
Let $|G|=p^2q$, and let $n_p,n_q$ be the numbers of Sylow $p$- and $q$-subgroups.
A proper nontrivial normal subgroup is produced in each of three cases.

<1>1. If $p=q$, then $G$ has a proper nontrivial normal subgroup.

::: {.proof}
$|G|=p^3$, so $Z(G)\neq1$ by the class equation.
If $Z(G)\neq G$, it is the required subgroup; if $G$ is abelian, every subgroup of order $p$ (which exists by Cauchy's theorem) is normal.
:::

<1>2. If $p>q$, then the Sylow $p$-subgroup is normal.

::: {.proof}
$n_p\mid q$ and $n_p\equiv1\pmod p$; since $1<q<p$, $q\not\equiv1\pmod p$, so $n_p=1$.
:::

<1>3. If $p<q$, then a Sylow $p$- or Sylow $q$-subgroup is normal.

::: {.proof}
$n_q\mid p^2$ and $n_q\equiv1\pmod q$, and $p\not\equiv1\pmod q$ since $1<p<q$, so $n_q\in\{1,p^2\}$.
If $n_q=1$, the Sylow $q$-subgroup is normal.
If $n_q=p^2$, distinct Sylow $q$-subgroups (of prime order $q$) meet trivially, so they contain $p^2(q-1)$ elements of order $q$.
The remaining $p^2q-p^2(q-1)=p^2$ elements contain every Sylow $p$-subgroup, each of order $p^2$, so there is exactly one Sylow $p$-subgroup, and it is normal.
:::
:::
