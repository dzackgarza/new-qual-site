---
schema: qual/card@1
id: P-7J6RO
kind: problem
title: Simple modules are cyclic, and Schur's lemma
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Semisimplicity
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.problem}
If $R$ has an identity, then a nonzero unitary $R\dash$module is **simple** if its only submodules are $0$ and $A$.

1. Show that every simple $R-$module is cyclic.

2. If $A$ is simple, every $R-$module endomorphism is either the zero map or an isomorphism.
:::

::: {.solution}
<1>1. Every simple $R$-module $A$ is cyclic; indeed $A=Ra$ for every nonzero $a\in A$.

::: {.proof}
Since $A\ne0$, there is $a\in A$ with $a\ne0$. The cyclic submodule $Ra=\{ra : r\in R\}$ contains $a=1_R\cdot a$ because $A$ is unitary, so $Ra\ne0$. As $A$ is simple, its only submodules are $0$ and $A$, hence $Ra=A$.
:::

<1>2. (Schur's lemma) If $A$ is simple, every $f\in\operatorname{End}_R(A)$ is either $0$ or an isomorphism.

<2>1. Either $f=0$ or $f$ is injective.

::: {.proof}
The kernel $\ker f$ is a submodule of $A$, so $\ker f=A$ or $\ker f=0$. In the first case $f=0$; in the second $f$ is injective.
:::

<2>2. If $f$ is injective, then $f$ is surjective.

::: {.proof}
The image $\operatorname{im} f$ is a submodule of $A$. Since $A\ne0$ and $f$ is injective, $\operatorname{im} f\ne0$, so simplicity gives $\operatorname{im} f=A$.
:::

<2>3. Q.E.D.

::: {.proof}
By steps <2>1 and <2>2, a nonzero $f$ is a bijective $R$-module homomorphism, hence an isomorphism.
:::
:::
