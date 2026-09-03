---
schema: qual/card@1
id: E-UAMGV
kind: problem
title: The coarsest topology making a family of maps continuous
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Topological Spaces
relations: []
review: draft
---

::: {.exercise}

Let $A$ be a set; let $\ts{X_\alpha}_{\alpha \in J}$ be an indexed family of spaces; and let $\ts{f_\alpha}_{\alpha \in J}$ be an indexed family of functions $f_\alpha: A \to X_\alpha$.

(a) Show there is a unique coarsest topology $\mathcal{T}$ on $A$ relative to which each of the functions $f_\alpha$ is continuous.

(b) Let

$$
\mathcal{S}_\beta = \ts{f_\beta^{-1}(U_\beta) \mid U_\beta \text{ is open in } X_\beta},
$$

and let $S = \bigcup \mathcal{S}_\beta$.
Show that $S$ is a subbasis for $\mathcal{T}$.

(c) Show that a map $g: Y \to A$ is continuous relative to $\mathcal{T}$ if and only if each map $f_\alpha \circ g$ is continuous.

(d) Let $f: A \to \prod X_\alpha$ be defined by the equation

$$
f(a) = (f_\alpha(a))_{\alpha \in J};
$$

let $Z$ denote the subspace $f(A)$ of the product space $\prod X_\alpha$.
Show that the image under $f$ of each element of $\mathcal{T}$ is an open set of $Z$.
:::
