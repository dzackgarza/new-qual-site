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
Let $\characteristic k = p$ with $k = \kbar$, let $n \geq 1$, and let $F : \PP^n_k \to \PP^n_k$ be the Frobenius, given on coordinates by $x \mapsto x^p$.
Then $F$ is finite, flat, surjective, and a homeomorphism, and it is nowhere smooth.
Since $d(t^p) = 0$, the map $F^* \Omega_{\PP^n/k} \to \Omega_{\PP^n/k}$ is zero, so the relative cotangent sheaf $\Omega_F = \operatorname{coker}(F^*\Omega_{\PP^n/k} \to \Omega_{\PP^n/k}) = \Omega_{\PP^n/k}$ is locally free of rank $n$ while the relative dimension of $F$ is $0$.
:::

::: {.remark}
This example separates smoothness from flatness and from the topology of the underlying map.
$F$ is finite flat of degree $p^n$ and bijective on points, so no condition on fibres as sets or on flatness detects the failure; only the differentials do.

It also shows that "étale equals flat plus finite fibres" is false: $F$ is flat with one point in every fibre and is not étale, because the fibres are nonreduced rather than reduced points.
On an affine chart around a geometric point, the fibre is
$$
\Spec
k[t_1,\ldots,t_n]/(t_1^p,\ldots,t_n^p),
$$
a one-point scheme of length $p^n$.
The condition $\mathfrak m_y \OO_{X,x} = \mathfrak m_x$ in the definition of unramified is what rules this out.
:::
