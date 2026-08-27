---
schema: qual/card@1
id: E-LS2QW
kind: exercise
title: The Stone-Cech construction is a functor
subtitle: Munkres §38.10
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

We have constructed a correspondence $X \to \beta(X)$ that assigns, to each completely regular space, its Stone-Čech compactification.
Now let us assign, to each continuous map $f: X \to Y$ of completely regular spaces, the unique continuous map $\beta(f): \beta(X) \to \beta(Y)$ that extends the map $i \circ f$, where $i: Y \to \beta(Y)$ is the inclusion map.
Verify the following:

(i) If $\mathsf{l}_X: X \to X$ is the identity map of $X$, then $\beta(\mathsf{l}_X)$ is the identity map of $\beta(X)$.

(ii) If $f: X \to Y$ and $g: Y \to Z$, then $\beta(g \circ f) = \beta(g) \circ \beta(f)$.

These properties tell us that the correspondence we have constructed is what is called a functor; it is a functor from the "category" of completely regular spaces and continuous maps of such spaces, to the "category" of compact Hausdorff spaces and continuous maps of such spaces.
:::
