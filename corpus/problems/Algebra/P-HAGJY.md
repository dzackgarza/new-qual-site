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

::: problem
Let $A$ be an $R$-module. Prove that
\[
\operatorname{End}_R(A)=\operatorname{Hom}_R(A,A)
\]
is a ring under pointwise addition and composition.
:::


::: {.solution}
<1>1. Under pointwise addition, $\operatorname{End}_R(A)$ is an abelian group.
::: {.proof}
For $f,g\in\operatorname{End}_R(A)$ define
\[
(f+g)(a)=f(a)+g(a).
\]
The zero map is the additive identity and $(-f)(a)=-f(a)$ is the additive inverse. Associativity and commutativity follow pointwise from the abelian-group structure on $A$.
:::

<1>2. Composition is closed and associative, with identity $\operatorname{id}_A$.
::: {.proof}
If $f,g$ are $R$-linear, then for $r\in R$ and $x,y\in A$,
\[
(f\circ g)(rx+y)
=f(rg(x)+g(y))
=r f(g(x))+f(g(y)),
\]
so $f\circ g$ is $R$-linear. Associativity is associativity of function composition, and $\operatorname{id}_A$ is a two-sided identity.
:::

<1>3. Composition distributes over addition on both sides.
::: {.proof}
For $f,g,h\in\operatorname{End}_R(A)$ and $x\in A$,
\[
(f\circ(g+h))(x)
=f(g(x)+h(x))
=(f\circ g)(x)+(f\circ h)(x),
\]
using linearity of $f$. Also
\[
((f+g)\circ h)(x)
=f(h(x))+g(h(x))
=(f\circ h)(x)+(g\circ h)(x).
\]
:::

Thus $\operatorname{End}_R(A)$ is a ring, generally noncommutative, with multiplicative identity $\operatorname{id}_A$.
:::
