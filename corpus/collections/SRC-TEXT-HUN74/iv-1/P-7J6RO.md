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
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section IV.1,
    exercise 5, book page 179: "If R has an identity, then a nonzero unitary
    R-module A is simple if its only submodules are 0 and A. (a) Every simple
    R-module is cyclic. (b) If A is simple every R-module endomorphism is
    either the zero map or an isomorphism." The card states exactly this,
    including the definition. The proof was checked: for nonzero a, the cyclic
    submodule Ra contains 1_R a = a by unitarity, so Ra ≠ 0 and simplicity gives
    Ra = A; and for an endomorphism f of a simple A the kernel is 0 or A and the
    image is 0 or A, so f is zero or bijective. Complete; no defect. The result
    is not called Schur's lemma in the book, but the card's title uses the
    standard name for the same statement and adds no hypothesis.
---

::: {.problem}
If $R$ has an identity, then a nonzero unitary $R$-module $A$ is \dfn{simple} if its only submodules are $0$ and $A$.

(a) Show that every simple $R$-module is cyclic.

(b) If $A$ is simple, every $R$-module endomorphism of $A$ is either the zero map or an isomorphism.
:::

::: {.solution}

::: pf

::: pf-step

Every simple $R$-module $A$ is cyclic; indeed $A=Ra$ for every nonzero $a\in A$.

::: pf-proof

Since $A\ne0$, there is $a\in A$ with $a\ne0$. The cyclic submodule $Ra=\{ra \st r\in R\}$ contains $a=1_R\cdot a$ because $A$ is unitary, so $Ra\ne0$. As $A$ is simple, its only submodules are $0$ and $A$, hence $Ra=A$.

:::

:::

::: pf-step

(Schur's lemma) If $A$ is simple, every $f\in\operatorname{End}_R(A)$ is either $0$ or an isomorphism.

::: pf-proof

::: {.pf-step #s2-1}

Either $f=0$ or $f$ is injective.

::: pf-proof

The kernel $\ker f$ is a submodule of $A$, so $\ker f=A$ or $\ker f=0$. In the first case $f=0$; in the second $f$ is injective.

:::

:::

::: {.pf-step #s2-2}

If $f$ is injective, then $f$ is surjective.

::: pf-proof

The image $\operatorname{im} f$ is a submodule of $A$. Since $A\ne0$ and $f$ is injective, $\operatorname{im} f\ne0$, so simplicity gives $\operatorname{im} f=A$.

:::

:::

::: pf-qed

By steps [](#s2-1){.pf-ref} and [](#s2-2){.pf-ref}, a nonzero $f$ is a bijective $R$-module homomorphism, hence an isomorphism.

:::

:::

:::

:::

:::
