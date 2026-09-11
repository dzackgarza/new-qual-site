---
schema: qual/card@1
id: FE-MORFROB
kind: example
title: The Frobenius morphism is nowhere smooth
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smooth Morphisms
  - Frobenius
  - Counterexamples
relations:
- kind: uses
  target: D-MORSM
review: draft
prompts:
- Give an example of a morphism that is not smooth.
- What does Frobenius do to differentials?
---

::: {.example}
Let $\characteristic k = p$ with $k = \kbar$ and let $F : \PP^n_k \to \PP^n_k$ be the Frobenius, given on coordinates by $x \mapsto x^p$.
Then $F$ is finite, flat, surjective, and a homeomorphism, and it is nowhere smooth.
Since $d(t^p) = 0$, the map $F^* \Omega_{\PP^n/k} \to \Omega_{\PP^n/k}$ is zero, so $\Omega_{\PP^n/\PP^n} = \Omega_{\PP^n/k}$ is locally free of rank $n$ while the relative dimension of $F$ is $0$.
:::

::: {.remark}
This is the standard example, and it is standard because it defeats every cheap criterion at once.
$F$ is finite flat of degree $p^n$ and bijective on points, so no condition on fibres as sets or on flatness detects the failure; only the differentials do.
It is the sharpest illustration that smoothness is not a topological or even a flat-family condition.

It also shows that "étale equals flat plus finite fibres" is false: $F$ is flat with one point in every fibre and is not étale, because the fibres are the non-reduced $\Spec k[x]/(x^p)$ rather than reduced points.
The separability clause in the definition of unramified is precisely what rules this out.
:::
