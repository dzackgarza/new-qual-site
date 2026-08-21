---
schema: qual/card@1
id: E-HAT-4.1-9
kind: exercise
title: "Extending the long exact sequence to $\\pi_0$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
solved: false
---

Suppose we define $\pi_0(X, A, x_0)$ to be the quotient set $\pi_0(X, x_0) / i^*\bigl(\pi_0(A, x_0)\bigr)$ so that the long exact sequence of homotopy groups for the pair $(X, A)$ extends to $\cdots \to \pi_0(A, x_0) \stackrel{\iota_*}{\longrightarrow} \pi_0(X, x_0) \to \pi_0(X, A, x_0) \to 0$.

(a) Show that with this extension, the five-lemma holds for the map of long exact sequences induced by a map $(X, A, x_0) \to (Y, B, y_0)$, in the following form: One of the maps between the two sequences is a bijection if the four surrounding maps are bijections for all choices of $x_0$.

(b) Show that the long exact sequence of a triple $(X, A, B, x_0)$ can be extended only to the term $\pi_0(A, B, x_0)$ in general, and that the five-lemma holds for this extension.
