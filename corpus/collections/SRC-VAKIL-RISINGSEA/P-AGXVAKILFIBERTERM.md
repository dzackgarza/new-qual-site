---
schema: qual/card@1
id: P-AGXVAKILFIBERTERM
kind: problem
title: The fiber product over a terminal object is the cartesian product
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fiber Products
  - Universal Properties
  - Terminal Objects
relations: []
review: draft
---

::: {.problem}
Show that the fiber product over the terminal object is the cartesian product.
:::

::: {.solution}
Let $T$ be a terminal object of a category $\mathcal C$, and let $X,Y$ be objects with their unique morphisms $t_X:X\to T$ and $t_Y:Y\to T$.
A fiber product $\fiberprod{X}{T}{Y}$ is an object $P$ with morphisms ${\operatorname{pr}}_X:P\to X$ and ${\operatorname{pr}}_Y:P\to Y$ such that $t_X\circ{\operatorname{pr}}_X=t_Y\circ{\operatorname{pr}}_Y$, and such that for every object $W$ with morphisms $p:W\to X$ and $q:W\to Y$ satisfying $t_X\circ p=t_Y\circ q$ there is a unique $h:W\to P$ with ${\operatorname{pr}}_X\circ h=p$ and ${\operatorname{pr}}_Y\circ h=q$.
A product $X\cross Y$ has the same definition with both conditions on $t_X,t_Y$ removed.

::: pf

::: {.pf-step #condition-automatic}
Every pair of morphisms $p:W\to X$ and $q:W\to Y$ satisfies $t_X\circ p=t_Y\circ q$.

::: pf-proof
Both $t_X\circ p$ and $t_Y\circ q$ are morphisms $W\to T$.
Since $T$ is terminal, there is exactly one morphism $W\to T$, so the two are equal.
:::

:::

::: pf-step
An object $P$ with morphisms ${\operatorname{pr}}_X:P\to X$ and ${\operatorname{pr}}_Y:P\to Y$ is a fiber product $\fiberprod{X}{T}{Y}$ if and only if it is a product $X\cross Y$.

::: pf-proof
By step [](#condition-automatic){.pf-ref}, the condition $t_X\circ{\operatorname{pr}}_X=t_Y\circ{\operatorname{pr}}_Y$ holds for every $P$, and the condition $t_X\circ p=t_Y\circ q$ holds for every test pair $(p,q)$.
With both conditions removed, the definition of the fiber product is word for word the definition of the product.
Hence the fiber product over $T$ exists exactly when the product exists, and then the two are isomorphic by a unique isomorphism compatible with the projections, since an object with a universal property is unique up to such an isomorphism.
:::

:::

:::
:::
