---
schema: qual/card@1
id: PR-RJ3P7
kind: proposition
title: Going up and going down on spectra
slogan: 'Integral extensions lift ascending prime chains; integrally closed-domain or flat hypotheses also lift descending chains.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Going Up
  - Finite Morphisms
  - Flatness
relations:
- kind: uses
  target: D-VKR54
review: draft
prompts:
- What does the going up theorem mean in algebraic geometry?
- What does going down mean geometrically?
---

::: {.theorem title="Lying over and going up"}
Let $\phi\colon A\to B$ be a ring map with $B$ integral over $\phi(A)$, and let
$$
f\colon\Spec B\longrightarrow\Spec A,
\qquad
f(\mfq)=\phi^{-1}(\mfq).
$$

- Lying over: if $\phi$ is injective, then for every prime $\mfp \subseteq A$ there is a prime $\mfq \subseteq B$ with $\phi^{-1}(\mfq) = \mfp$; hence $f$ is surjective.

- Going up: if $\mfp_1 \subseteq \cdots \subseteq \mfp_n$ is a chain of primes of $A$ and $\mfq_1 \subseteq \cdots \subseteq \mfq_m$, $m<n$, is a chain of primes of $B$ with $\phi^{-1}(\mfq_i)=\mfp_i$ for $1\leq i\leq m$, then it extends to a chain $\mfq_1 \subseteq \cdots \subseteq \mfq_n$ with $\phi^{-1}(\mfq_i)=\mfp_i$ for all $i$.

For every ideal $J\subseteq B$,
$$
f(V(J))=V(\phi^{-1}(J)),
$$
so $f$ is a closed map.
[@AM18]
:::

::: {.proof title="Closedness"}
The inclusion $f(V(J))\subseteq V(\phi^{-1}(J))$ is immediate. The quotient map
$$
A/\phi^{-1}(J)\longrightarrow B/J
$$
is injective and integral. Lying over therefore gives, for every prime $\mfp\supseteq\phi^{-1}(J)$, a prime $\mfq/J\in\Spec(B/J)$ lying over $\mfp/\phi^{-1}(J)$. Equivalently, $\mfq\supseteq J$ and $\phi^{-1}(\mfq)=\mfp$. Thus the reverse inclusion also holds.
:::

::: {.theorem title="Going down"}
Let $A \subseteq B$ be domains with $A$ integrally closed and $B$ integral over $A$.
If $\mfp_1 \supseteq \cdots \supseteq \mfp_n$ is a chain of primes of $A$ and $\mfq_1 \supseteq \cdots \supseteq \mfq_m$, $m < n$, is a chain of primes of $B$ with $\mfq_i \cap A = \mfp_i$, then it extends to a chain $\mfq_1 \supseteq \cdots \supseteq \mfq_n$ with $\mfq_i \cap A = \mfp_i$.
Going down also holds for every flat ring map $A \to B$.
[@AM18]
:::

::: {.remark}
Going up says that specializations in $\Spec A$ lift after choosing a point above the starting prime. The quotient-ring argument above converts lying over into the closedness of every integral morphism. Since integrality is preserved by base change, integral morphisms are universally closed. A finite morphism is integral, affine, and of finite type; affine morphisms are separated, so a finite morphism is proper.

For an integral extension of domains $A\subseteq B$, going up and incomparability imply
$$
\dim B=\dim A.
$$
Under the hypotheses of going down, the same chain comparison gives
$$
\operatorname{ht}\mfq=\operatorname{ht}(\mfq\cap A).
$$
Geometrically, going down says that every generization of the image of a point lifts to a generization of that point.

Thus a finite surjective morphism of integral schemes is closed, has finite fibres, and preserves Krull dimension.
:::
