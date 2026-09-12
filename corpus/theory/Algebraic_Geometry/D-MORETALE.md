---
schema: qual/card@1
id: D-MORETALE
kind: definition
title: Étale morphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Étale Morphisms
  - Unramified Morphisms
  - Flatness
relations:
- kind: uses
  target: D-MORUNR
review: draft
prompts:
- What is an étale morphism?
- Give several equivalent definitions of étale.
- Is a bijective étale morphism an isomorphism?
---

::: {.definition title="Étale"}
$f : X \to Y$ is **étale** if it is flat and unramified, equivalently flat, locally of finite presentation, with $\Omega_{X/Y} = 0$, equivalently smooth of relative dimension $0$.
:::

::: {.remark}
An étale morphism is open. Finite étale morphisms form the category of covers used to define the étale fundamental group.

Étale does not imply local isomorphism in the Zariski topology: $\GG_m \to \GG_m$, $t \mapsto t^2$, over a field of characteristic not $2$ is finite étale of degree $2$ and is not an isomorphism over any nonempty Zariski open.
Pulling this cover back along itself gives a disjoint union of two copies of the base.

A finite étale morphism of degree $1$ is an isomorphism. Bijectivity on underlying points does not suffice: $\Spec L\to\Spec k$ is bijective and finite étale for a nontrivial finite separable field extension $L/k$.
:::
