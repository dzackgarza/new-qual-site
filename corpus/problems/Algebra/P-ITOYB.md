---
schema: qual/card@1
id: P-ITOYB
kind: problem
title: The $p$-torsion $A[p]$ is an $R/(p)$-module
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Torsion
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $R$ be a commutative ring, let $A$ be an $R$-module, and let $p\in R$.
Define
\[
A[p]=\{a\in A:pa=0\}.
\]
Show that $A[p]$ is naturally an $R/(p)$-module.
:::

::: {.solution}
Define
\[
(r+(p))\cdot a:=ra,
\qquad r\in R,\ a\in A[p].
\]

<1>1. The action is well defined with respect to the residue class of $r$.
::: {.proof}
If $r-r'\in(p)$, write $r-r'=sp$. Then for $a\in A[p]$,
\[
ra-r'a=(r-r')a=spa=s(pa)=0.
\]
Hence $ra=r'a$.
:::

<1>2. The action preserves $A[p]$.
::: {.proof}
If $a\in A[p]$, then
\[
p(ra)=r(pa)=0
\]
by commutativity of $R$. Thus $ra\in A[p]$.
:::

<1>3. The module axioms descend from the $R$-module structure on $A$.
::: {.proof}
For $r,s\in R$ and $a,b\in A[p]$,
\[
(r+(p))\cdot(a+b)=ra+rb,
\]
\[
((r+s)+(p))\cdot a=ra+sa,
\]
\[
((rs)+(p))\cdot a=(r+(p))\cdot((s+(p))\cdot a),
\]
and
\[
(1+(p))\cdot a=a.
\]
:::

Therefore $A[p]$ is naturally an $R/(p)$-module. If $(p)$ is maximal, then $R/(p)$ is a field and $A[p]$ is consequently a vector space over that field.
:::
