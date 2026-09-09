---
schema: qual/card@1
id: P-NNJHK
kind: problem
title: $\hom_R(A, B)$ under pointwise addition is an abelian group
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

::: problem
Let $A,B$ be $R$-modules. Show that
\[
\Hom_R(A,B)
\]
is an abelian group under pointwise addition
\[
(f+g)(a)=f(a)+g(a).
\]
:::

::: {.solution}
If $f,g\in\Hom_R(A,B)$, then $f+g$ is $R$-linear because
\[
(f+g)(a+a')=f(a)+f(a')+g(a)+g(a')
=(f+g)(a)+(f+g)(a')
\]
and
\[
(f+g)(ra)=rf(a)+rg(a)=r(f+g)(a).
\]
Thus pointwise addition is closed.

Associativity and commutativity follow pointwise from the abelian-group law on $B$:
\[
(f+(g+h))(a)=f(a)+g(a)+h(a)=((f+g)+h)(a),
\]
\[
(f+g)(a)=f(a)+g(a)=g(a)+f(a)=(g+f)(a).
\]

The zero map is the identity element, and the inverse of $f$ is the map
\[
(-f)(a)=-f(a),
\]
which is again $R$-linear.

Therefore
\[
(\Hom_R(A,B),+)
\]
is an abelian group.
:::
