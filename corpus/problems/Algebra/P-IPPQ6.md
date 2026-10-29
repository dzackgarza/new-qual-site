---
schema: qual/card@1
id: P-IPPQ6
kind: problem
title: Holomorphic maps of compact Riemann surfaces and extensions of function fields
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Geometry
relations: []
review: draft
---

::: {.problem}
Consider a nonconstant function between two compact Riemann Surfaces.
How is it related to Galois theory?
:::

::: {.solution}
Let $f\colon X\to Y$ be a nonconstant holomorphic map of compact connected Riemann surfaces, and write $\CC(X)$ and $\CC(Y)$ for their fields of meromorphic functions.

::: pf

::: pf-step

Pullback $f^*\colon\CC(Y)\to\CC(X)$, $h\mapsto h\circ f$, is an injective field homomorphism, and $\CC(X)/f^*\CC(Y)$ is a finite extension of degree $\deg(f)$.

::: pf-proof

A field homomorphism is injective. Since $f$ is nonconstant and $X$ and $Y$ are compact, $f$ is a finite branched covering, and the equality $[\CC(X):f^*\CC(Y)]=\deg(f)$ is the standard degree formula. It is an instance of the anti-equivalence between compact connected Riemann surfaces with nonconstant holomorphic maps and function fields of transcendence degree one over $\CC$.

:::

:::

::: pf-step

The deck group of $f$ is isomorphic to $\Aut_{\CC(Y)}\bigl(\CC(X)\bigr)$, and $f$ is a Galois (regular) branched covering exactly when $\CC(X)/f^*\CC(Y)$ is a Galois extension, in which case the deck group is the Galois group.

::: pf-proof

A deck transformation $\gamma\colon X\to X$ with $f\circ\gamma=f$ acts on $\CC(X)$ by pullback and fixes $f^*\CC(Y)$. Under the anti-equivalence, every $f^*\CC(Y)$-automorphism of $\CC(X)$ arises from a unique such $\gamma$, and $\gamma\mapsto(\gamma^{-1})^*$ is an isomorphism of groups. The covering is Galois when the deck group acts transitively on fibres, that is, when the deck group has order $\deg(f)=[\CC(X):f^*\CC(Y)]$, which is the condition for the extension to be Galois.

:::

:::

::: pf-step

Intermediate fields $f^*\CC(Y)\subseteq L\subseteq\CC(X)$ correspond to factorizations $X\to Z\to Y$ of $f$ through compact Riemann surfaces $Z$ with $\CC(Z)\cong L$, up to isomorphism.

::: pf-proof

This is the anti-equivalence applied to the inclusions $f^*\CC(Y)\subseteq L\subseteq\CC(X)$, since $L$ is a function field of transcendence degree one over $\CC$.

:::

:::

:::

:::
