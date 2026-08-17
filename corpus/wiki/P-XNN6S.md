---
schema: qual/card@1
id: P-XNN6S
kind: problem
title: 'Let $\phi: A \to A$ be a module endomorphism on a simple module $A$.'
classification:
  areas:
  - algebra
  topics:
  - modules
  - semisimplicity
  - homomorphisms
relations: []
review: draft
solved: false
---

::: problem
Let $\phi: A \to A$ be a module endomorphism on a simple module $A$.
Then $\im \phi \definedas \phi(A)$ is a submodule of $A$.
Since $A$ is simple, we have either $\im \phi = 0$, in which case $\phi$ is the zero map, or $\im \phi = A$, so $\phi$ is surjective.
In this case, we can also consider $\ker \phi$, which is a submodule of $A$.
Since $A$ is simple, we can again only have $\ker \phi = A$, which can not happen if $\phi$ is not the zero map, or $\ker \phi = 0$, in which case $\phi$ is both a surjective and an injective map and thus an isomorphism of modules.
:::
