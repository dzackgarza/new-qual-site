---
schema: qual/card@1
id: E-XIHWT
kind: exercise
title: Distance to a set in a metric space
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Compactness
relations: []
review: draft
---

::: {.exercise title="Munkres §27.2"}

Let $X$ be a metric space with metric $d$; let $A \subset X$ be nonempty.

(a) Show that $d(x, A) = 0$ if and only if $x \in \overline{A}$.

(b) Show that if $A$ is compact, $d(x, A) = d(x, a)$ for some $a \in A$.

(c) Define the $\epsilon$-neighborhood of $A$ in $X$ to be the set

$$
U(A, \epsilon) = \ts{x \mid d(x, A) < \epsilon}.
$$

Show that $U(A, \epsilon)$ equals the union of the open balls $B_d(a, \epsilon)$ for $a \in A$.

(d) Assume that $A$ is compact; let $U$ be an open set containing $A$.
Show that some $\epsilon$-neighborhood of $A$ is contained in $U$.

(e) Show the result in (d) need not hold if $A$ is closed but not compact.
:::
