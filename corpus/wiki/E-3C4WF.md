---
schema: qual/card@1
id: E-3C4WF
kind: exercise
title: The Hausdorff metric on closed bounded subsets
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise title="Munkres §45.7"}

Let $(X, d)$ be a metric space.
If $A \subset X$ and $\epsilon > 0$, let $U(A, \epsilon)$ be the $\epsilon$-neighborhood of $A$.
Let $\mathcal{H}$ be the collection of all (nonempty) closed, bounded subsets of $X$.
If $A, B \in \mathcal{H}$, define

$$
D(A, B) = \inf\ts{\epsilon \mid A \subset U(B, \epsilon) \text{ and } B \subset U(A, \epsilon)}.
$$

(a) Show that $D$ is a metric on $\mathcal{H}$; it is called the Hausdorff metric.

(b) Show that if $(X, d)$ is complete, so is $(\mathcal{H}, D)$.
[Hint: Let $A_n$ be a Cauchy sequence in $\mathcal{H}$; by passing to a subsequence, assume $D(A_n, A_{n+1}) < 1/2^n$. Define $A$ to be the set of all points $x$ that are the limits of sequences $x_1, x_2, \ldots$ such that $x_i \in A_i$ for each $i$ and $d(x_i, x_{i+1}) < 1/2^i$. Show $A_n \to \overline{A}$.]

(c) Show that if $(X, d)$ is totally bounded, so is $(\mathcal{H}, D)$.
[Hint: Given $\epsilon$, choose $\delta < \epsilon$ and let $S$ be a finite subset of $X$ such that the collection $\ts{B_d(x, \delta) \mid x \in S}$ covers $X$. Let $\mathcal{A}$ be the collection of all nonempty subsets of $S$; show that $\ts{B_D(A, \epsilon) \mid A \in \mathcal{A}}$ covers $\mathcal{H}$.]

(d) Theorem.
If $X$ is compact in the metric $d$, then the space $\mathcal{H}$ is compact in the Hausdorff metric $D$.
:::
