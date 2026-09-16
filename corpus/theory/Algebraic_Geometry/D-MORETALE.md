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
$f : X \to Y$ is \dfn{étale} if it is flat and unramified, equivalently flat, locally of finite presentation, with $\Omega_{X/Y} = 0$, equivalently smooth of relative dimension $0$.
:::

::: {.remark}
Étale is the algebraic replacement for a local homeomorphism, and every clause is one half of that: unramified gives local injectivity and flatness gives local surjectivity, in the sense that nothing collapses and nothing is missing.
An étale morphism is open, and a finite étale morphism is the correct notion of a covering space, which is what makes the étale fundamental group possible.

Étale does not imply local isomorphism in the Zariski topology, and this is the standard follow-up: $\GG_m \to \GG_m$, $t \mapsto t^2$, over a field of characteristic not $2$ is finite étale of degree $2$ and is not an isomorphism over any nonempty Zariski open.
It becomes trivial only after an étale base change, which is the whole reason for introducing the étale topology.

A bijective étale morphism onto a connected target is an isomorphism, but only when it is also separated and the target is connected and one is over a field, so the safe statement is: a finite étale morphism of degree $1$ is an isomorphism.
:::
