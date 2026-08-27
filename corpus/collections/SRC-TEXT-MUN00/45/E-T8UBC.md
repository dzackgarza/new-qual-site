---
schema: qual/card@1
id: E-T8UBC
kind: exercise
title: Graphs as an imbedding of the function space into the hyperspace
subtitle: Munkres §45.8
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces; give $X \times Y$ the corresponding square metric; let $\mathcal{H}$ denote the collection of all nonempty closed, bounded subsets of $X \times Y$, in the resulting Hausdorff metric.
Consider the space $\mathcal{C}(X, Y)$ in the uniform metric; let $\operatorname{gr}: \mathcal{C}(X, Y) \to \mathcal{H}$ be the function that assigns, to each continuous function $f: X \to Y$, its graph

$$
G_f = \ts{x \times f(x) \mid x \in X}.
$$

(a) Show that the map $\operatorname{gr}$ is injective and uniformly continuous.

(b) Let $\mathcal{H}_0$ denote the image set of the map $\operatorname{gr}$; let $g: \mathcal{C}(X, Y) \to \mathcal{H}_0$ be the surjective map obtained from $\operatorname{gr}$.
Show that if $f: X \to Y$ is uniformly continuous, then the map $g^{-1}$ is continuous at the point $G_f$.

(c) Give an example where $g^{-1}$ is not continuous at the point $G_f$.

(d) Theorem.
If $X$ is compact, then $\operatorname{gr}: \mathcal{C}(X, Y) \to \mathcal{H}$ is an imbedding.
:::
