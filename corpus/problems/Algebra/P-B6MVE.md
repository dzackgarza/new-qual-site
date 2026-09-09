---
schema: qual/card@1
id: P-B6MVE
kind: problem
title: $\mathrm{Hom}_R(R,R)\cong R^{\mathrm{op}}$
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
Let $R$ be a unital ring, viewed as a left $R$-module over itself. Prove that
\[
\operatorname{End}_R({}_RR)\cong R^{\mathrm{op}}
\]
as rings.
:::

::: {.solution}
Define
\[
\Phi:\operatorname{End}_R({}_RR)\longrightarrow R^{\mathrm{op}},
\qquad
\Phi(f)=f(1).
\]

<1>1. Every left $R$-linear endomorphism is right multiplication by $f(1)$.
::: {.proof}
For $r\in R$,
\[
f(r)=f(r\cdot1)=r f(1)
\]
by left $R$-linearity. Thus $f$ is uniquely determined by $f(1)$ and has the form
\[
r\longmapsto r x
\]
for $x=f(1)$.
:::

<1>2. The map $\Phi$ is bijective.
::: {.proof}
Injectivity follows from <1>1. For surjectivity, given $x\in R$, the map
\[
\rho_x:R\to R,\qquad r\mapsto rx
\]
is left $R$-linear and satisfies $\Phi(\rho_x)=x$.
:::

<1>3. The map $\Phi$ respects addition and multiplication into the opposite ring.
::: {.proof}
Addition is immediate. For composition,
\[
(g\circ f)(1)=g(f(1))=g(x_f)=x_f x_g.
\]
Thus
\[
\Phi(g\circ f)=x_f x_g.
\]
But multiplication in $R^{\mathrm{op}}$ is reversed, so
\[
\Phi(g)\cdot_{R^{\mathrm{op}}}\Phi(f)=x_g\cdot_{R^{\mathrm{op}}}x_f=x_f x_g.
\]
Hence $\Phi(g\circ f)=\Phi(g)\cdot_{R^{\mathrm{op}}}\Phi(f)$, as required.
:::

Therefore
\[
\operatorname{End}_R({}_RR)\cong R^{\mathrm{op}}.
\]
:::
