---
schema: qual/card@1
id: P-XNN6S
kind: problem
title: 'Schur''s lemma: endomorphisms of a simple module are zero or isomorphisms'
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Semisimplicity
  - Homomorphisms
relations: []
review: draft
---

::: {.problem}
Let $A$ be a simple module and let $\phi:A\to A$ be a module endomorphism. Prove that either $\phi=0$ or $\phi$ is an isomorphism.
:::

::: {.solution}

::: pf

::: {.pf-step #submodules}
Each of $\ker\phi$ and $\im\phi$ is $0$ or $A$.

::: pf-proof
Both are submodules of $A$, and the only submodules of the simple module $A$ are $0$ and $A$.
:::

:::

::: pf-step
Either $\phi=0$ or $\phi$ is an isomorphism.

::: pf-proof
If $\im\phi=0$, then $\phi=0$.
Otherwise $\im\phi=A$ by step [](#submodules){.pf-ref}, so $\phi$ is surjective and nonzero.
Then $\ker\phi\ne A$, so $\ker\phi=0$ by step [](#submodules){.pf-ref}, and $\phi$ is injective.
Hence $\phi$ is bijective, and a bijective module homomorphism is an isomorphism.
:::

:::

:::

:::
