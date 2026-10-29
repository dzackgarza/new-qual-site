---
schema: qual/card@1
id: P-HAGJY
kind: problem
title: $\Endo_R(A)$ is a ring
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Rings
  - Homomorphisms
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

Let $A$ be an $R$-module. Prove that
$$
\Endo_R(A)=\Hom_R(A,A)
$$
is a ring under pointwise addition and composition.

:::

::: {.solution}

::: pf

::: pf-step

Under pointwise addition, $\Endo_R(A)$ is an abelian group.

::: pf-proof

For $f,g\in\Endo_R(A)$ define
$$
(f+g)(a)=f(a)+g(a).
$$
The map $f+g$ is $R$-linear because $f$ and $g$ are. The zero map is the additive identity and $(-f)(a)=-f(a)$ is the additive inverse. Associativity and commutativity follow pointwise from the abelian-group structure on $A$.

:::

:::

::: pf-step

Composition is closed and associative, with identity $\id_A$.

::: pf-proof

If $f,g$ are $R$-linear, then for $r\in R$ and $x,y\in A$,
$$
(f\circ g)(rx+y)
=f(rg(x)+g(y))
=r f(g(x))+f(g(y)),
$$
so $f\circ g$ is $R$-linear. Associativity is associativity of function composition, and $\id_A$ is a two-sided identity.

:::

:::

::: pf-step

Composition distributes over addition on both sides.

::: pf-proof

For $f,g,h\in\Endo_R(A)$ and $x\in A$,
$$
(f\circ(g+h))(x)
=f(g(x)+h(x))
=(f\circ g)(x)+(f\circ h)(x),
$$
using linearity of $f$. Also
$$
((f+g)\circ h)(x)
=f(h(x))+g(h(x))
=(f\circ h)(x)+(g\circ h)(x).
$$

:::

:::

:::

:::

::: {.remark}

The ring $\Endo_R(A)$ is in general noncommutative.

:::
