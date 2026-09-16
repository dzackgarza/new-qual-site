---
schema: qual/card@1
id: FE-Y12XB
kind: example
title: A surjection of sheaves that is not surjective on sections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Exact Sequences
  - Line Bundles
  - Cohomology
relations:
- kind: uses
  target: PR-C9ZEK
review: draft
prompts:
- Give a surjection of sheaves which is not surjective on global sections.
- On $\PP^1$, find the cokernel of a map $\OO(-2) \to \OO$.
---

::: {.example}
On $X = \PP^1$ take two distinct points $p \neq q$ and the evaluation sequence
\[
0 \to \OO(-p-q) \to \OO_X \to \OO_p \oplus \OO_q \to 0 .
\]
The right map is surjective: at $p$ it is the surjection $\OO_{X,p} \to k$, at $q$ likewise, and at every other point the target stalk is $0$.

On global sections it is the map $k \to k^2$ sending a constant $c$ to $(c,c)$, which is not surjective: a regular function on $\PP^1$ taking the value $0$ at $p$ and $1$ at $q$ would be a nonconstant global regular function.
The cokernel is one-dimensional, and indeed $H^1(\PP^1, \OO(-2)) \cong k$.
:::

::: {.example}
A nonzero map $\OO_{\PP^1}(-2) \to \OO_{\PP^1}$ is multiplication by a nonzero section $s \in H^0(\OO(2))$, whose zero scheme $Z$ has degree $2$.
Its cokernel is $\OO_Z$: either $\OO_p \oplus \OO_q$ when $s$ has two distinct zeros $p, q$, as above, or $\OO_{\PP^1,p}/\mfm_p^2$, of length $2$ at $p$, when $s$ vanishes to order $2$ at $p$.
In both cases $H^0$ of the cokernel is $2$-dimensional.
:::

::: {.remark}
The example is worth carrying because it makes the failure numerical rather than atmospheric: the sequence fails to be right exact on sections by exactly the dimension that $H^1$ of the kernel predicts.

The same shape recurs as the classical exponential sequence on a complex manifold, where the failure of $\OO \to \OO^*$ on sections is the existence of line bundles, and $H^1(X,\OO^*) = \Pic(X)$.
:::
