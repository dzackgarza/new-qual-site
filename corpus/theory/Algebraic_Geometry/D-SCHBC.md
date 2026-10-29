---
schema: qual/card@1
id: D-SCHBC
kind: definition
title: Base change, and properties stable under it
classification:
  areas:
  - algebraic-geometry
  topics:
  - Base Change
  - Fibre Products
  - Morphisms Of Schemes
relations:
- kind: uses
  target: D-SCHFPR
review: draft
prompts:
- What is base change?
- What does it mean for a property of morphisms to be stable under base change, or local on the base?
---

::: {.definition}
For a morphism $f\colon X \to S$ and a morphism $T \to S$, the \dfn{base change} of $X$ to $T$ is $X_T \definedas \fiberprod{X}{S}{T}$, with its projection $X_T \to T$.

A property $P$ of morphisms is \dfn{stable under base change} if $f$ having $P$ forces $X_T \to T$ to have $P$ for every $T \to S$.
It is \dfn{local on the base} if for every open cover $\theset{V_i}$ of $S$,
$$
f\text{ has }P
\quad\Longleftrightarrow\quad
f^{-1}(V_i)\to V_i\text{ has }P\text{ for every }i.
$$
:::

::: {.remark}
Extension of the ground field is base change along $\Spec L\to\Spec k$ for a field extension $L/k$; a $k$-scheme $X$ is geometrically connected, or geometrically integral, if $X\times_kL$ is connected, or integral, for every field extension $L/k$.
Connectedness is not stable under this base change: $\Spec \CC$ is connected, and $\Spec\CC\times_{\RR}\Spec\CC=\Spec(\CC\tensor_\RR\CC)\cong\Spec\CC\sqcup\Spec\CC$ is not.
The fibre of $X\to Y$ over $y$ is the base change along $\Spec \kappa(y) \to Y$.

Closed immersion, separated, proper, finite, flat, smooth, and affine are stable under base change and local on the base.
Surjectivity is stable under base change.
Dominance is not: the open immersion $D(x)\to\AA^1_k$ is dominant, and its base change along the origin $\Spec k\to\AA^1_k$ is $\emptyset\to\Spec k$.
:::
