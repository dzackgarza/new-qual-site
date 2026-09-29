---
schema: qual/card@1
id: E-MLBWS
kind: problem
title: Finite extension with infinitely many intermediate fields
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Counterexamples
  - Separability
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Give an example of a finite extension of fields that has infinitely many intermediate fields.
:::

::: {.solution}
Let $p$ be prime, $k=\FF_p(u,v)$ the rational function field in two indeterminates, and $K=\FF_p(u^p,v^p)\subseteq k$.

::: pf

::: {.pf-step #k-over-k-degree-p2}
$[k:K]=p^2$, with basis $\{u^iv^j:0\le i,j\le p-1\}$.

::: pf-proof
Since $u,v$ are algebraically independent over $\FF_p$, $[K(u):K]=p$ with basis $1,u,\dots,u^{p-1}$ and $[K(u,v):K(u)]=p$ with basis $1,v,\dots,v^{p-1}$; the tower law gives $[k:K]=p^2$.
:::

:::

::: {.pf-step #ec-degree-p}
For $c\in K$, the field $E_c=K(u+cv)$ satisfies $[E_c:K]=p$.

::: pf-proof
In characteristic $p$, $(u+cv)^p=u^p+c^pv^p\in K$, so $[E_c:K]\le p$.
Since $1,u,v$ are linearly independent over $K$ by step [](#k-over-k-degree-p2){.pf-ref}, $u+cv\notin K$, so $[E_c:K]>1$; and $[E_c:K]$ divides $p^2$.
Hence $[E_c:K]=p$.
:::

:::

::: {.pf-step #distinct-ec}
If $c_1\neq c_2$ in $K$, then $E_{c_1}\neq E_{c_2}$.

::: pf-proof
Suppose $E=E_{c_1}=E_{c_2}$.
Then $(u+c_1v)-(u+c_2v)=(c_1-c_2)v\in E$, and $c_1-c_2\in K^\times$, so $v\in E$ and then $u=(u+c_1v)-c_1v\in E$.
So $E=k$, and $[E:K]=p^2$, contradicting step [](#ec-degree-p){.pf-ref}.
:::

:::

::: pf-qed
$K$ is infinite (it contains the distinct elements $u^{pn}$, $n\ge1$), so by step [](#distinct-ec){.pf-ref} the fields $E_c$, $c\in K$, are infinitely many distinct intermediate fields of the extension $k/K$, which is finite of degree $p^2$ by step [](#k-over-k-degree-p2){.pf-ref}.
:::

:::

:::
