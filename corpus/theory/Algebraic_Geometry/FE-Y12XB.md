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
Let $k$ be an algebraically closed field, let $X=\PP^1_k$, and let $p\neq q$ be two points. The evaluation sequence is
$$
0 \to \OO(-p-q) \to \OO_X \to \OO_p \oplus \OO_q \to 0 .
$$
Since $p$ and $q$ have degree one, $\OO(-p-q)\cong\OO_{\PP^1}(-2)$.
The right map is surjective: at $p$ it is the surjection $\OO_{X,p} \to k$, at $q$ likewise, and at every other point the target stalk is $0$.

On global sections it is the map $k \to k^2$ sending a constant $c$ to $(c,c)$, which is not surjective: a regular function on $\PP^1$ taking the value $0$ at $p$ and $1$ at $q$ would be a nonconstant global regular function.
The cokernel is one-dimensional, and indeed $H^1(\PP^1, \OO(-2)) \cong k$.
:::

::: {.example}
A nonzero map $\OO_{\PP^1}(-2) \to \OO_{\PP^1}$ is multiplication by a nonzero section $s \in H^0(\PP^1,\OO(2))$, whose zero scheme $Z$ has degree $2$.
Its cokernel is $\OO_Z$: either $\OO_p \oplus \OO_q$ when $s$ has two distinct zeros $p, q$, as above, or $\OO_{\PP^1,p}/\mfm_p^2$, of length $2$ at $p$, when $s$ vanishes to order $2$ at $p$.
In both cases $\dim_k H^0(\PP^1,\OO_Z)=2$.
:::

::: {.remark}
The long exact cohomology sequence contains
$$
k\longrightarrow k^2\longrightarrow H^1(\PP^1,\OO(-2))\longrightarrow H^1(\PP^1,\OO)=0.
$$
Hence the cokernel of $H^0(\OO_X)\to H^0(\OO_p\oplus\OO_q)$ is canonically isomorphic to $H^1(\PP^1,\OO(-2))\cong k$.
:::
