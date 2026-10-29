---
schema: qual/card@1
id: P-NNJHK
kind: problem
title: $\Hom_R(A, B)$ under pointwise addition is an abelian group
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homomorphisms
  - Abelian Groups
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

::: {.problem}
Let $A,B$ be $R$-modules. Show that
$$
\Hom_R(A,B)
$$
is an abelian group under pointwise addition
$$
(f+g)(a)=f(a)+g(a).
$$
:::

::: {.solution}
::: pf

::: {.pf-step #closed}
If $f,g\in\Hom_R(A,B)$, then $f+g\in\Hom_R(A,B)$.

::: pf-proof
For $a,a'\in A$ and $r\in R$, $(f+g)(a+a')=f(a)+f(a')+g(a)+g(a')=(f+g)(a)+(f+g)(a')$ and $(f+g)(ra)=rf(a)+rg(a)=r(f+g)(a)$.
:::

:::

::: {.pf-step #axioms}
Pointwise addition on $\Hom_R(A,B)$ is associative and commutative, the zero map is an identity, and $-f\colon a\mapsto-f(a)$ is an $R$-linear inverse of $f$.

::: pf-proof
Each identity holds at every $a\in A$ because it holds in the abelian group $B$: $(f+(g+h))(a)=f(a)+g(a)+h(a)=((f+g)+h)(a)$ and $(f+g)(a)=g(a)+f(a)$.
The map $-f$ is $R$-linear because $-f(a+a')=-f(a)-f(a')$ and $-f(ra)=r(-f(a))$.
:::

:::

::: pf-step
$(\Hom_R(A,B),+)$ is an abelian group.

::: pf-proof
Steps [](#closed){.pf-ref} and [](#axioms){.pf-ref}.
:::

:::

:::

:::
