---
schema: qual/card@1
id: T-MORSMREG
kind: theorem
title: Smooth over an algebraically closed field equals regular
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smooth Morphisms
  - Regularity
  - Singularities
relations:
- kind: uses
  target: D-MORSM
review: draft
prompts:
- How is smoothness related to regularity?
- Is a regular scheme smooth?
---

::: {.theorem}
Let $k$ be a field and $X$ a scheme locally of finite type over $k$.
If $X \to \Spec k$ is smooth of relative dimension $n$ then $X$ is regular of dimension $n$.
The converse holds when $k$ is perfect, in particular when $k = \kbar$, and fails otherwise.
:::

::: {.remark}
Smooth is a property of a *morphism* and regular is a property of a *ring*, and keeping them apart is most of what this question tests.
Smooth is the stronger, base-change-stable notion: it is "regular after every field extension", which is why the two agree exactly when there are no inseparable extensions to spoil it.

The counterexample to the converse over an imperfect field is the one to have ready: $k = \FF_p(t)$ and $X = \Spec k[x]/(x^p - t)$ is the spectrum of a field, hence regular, while $\fiberprod{X}{k}{\kbar} = \Spec \kbar[x]/(x - t^{1/p})^p$ is non-reduced, so $X$ is not smooth over $k$.

A smooth morphism is regular fibrewise, not absolutely: a smooth morphism over a singular base has singular total space, and the fibres are what the definition controls.
:::
