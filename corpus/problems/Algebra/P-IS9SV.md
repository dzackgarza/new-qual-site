---
schema: qual/card@1
id: P-IS9SV
kind: problem
title: Evaluation makes $A$ a module over $\mathrm{End}_R(A)$
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
Let $A$ be an $R$-module. Show that evaluation
\[
\End_R(A)\times A\longrightarrow A,\qquad (f,a)\longmapsto f(a),
\]
makes $A$ into a left module over the endomorphism ring $\End_R(A)$.
:::

::: {.solution}
Write $f\cdot a=f(a)$.

<1>1. The action is additive in the $A$-variable.
::: {.proof}
For $a,b\in A$,
\[
f\cdot(a+b)=f(a+b)=f(a)+f(b)=f\cdot a+f\cdot b,
\]
because $f$ is $R$-linear.
:::

<1>2. The action is additive in the scalar variable.
::: {.proof}
For $f,g\in\End_R(A)$,
\[
(f+g)\cdot a=(f+g)(a)=f(a)+g(a)=f\cdot a+g\cdot a.
\]
:::

<1>3. Multiplication in $\End_R(A)$ is compatible with the action.
::: {.proof}
The ring multiplication is composition, so
\[
(fg)\cdot a=(f\circ g)(a)=f(g(a))=f\cdot(g\cdot a).
\]
:::

<1>4. The identity endomorphism acts as the identity.
::: {.proof}
The multiplicative identity of $\End_R(A)$ is $\id_A$, and
\[
\id_A\cdot a=\id_A(a)=a.
\]
:::

Therefore $A$ is a left $\End_R(A)$-module under evaluation.
:::
