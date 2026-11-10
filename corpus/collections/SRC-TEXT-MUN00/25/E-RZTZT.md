---
schema: qual/card@1
id: E-RZTZT
kind: problem
title: Components of R^omega in product, uniform, and box topologies
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §25 Exercise 2, printed p. 162, with Example 7 of
    §23, Exercise 23.8 and Exercise 19.8; the three parts and the two hints are stored as
    printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.2, PDF pp. 7-8. The product topology gives one
    component; in the uniform topology the bounded and unbounded sequences separate the
    space and the segment t -> t z joins the origin to a bounded sequence; in the box
    topology the coordinatewise affine homeomorphism of Exercise 19.8 sends the pair to a
    bounded and an unbounded sequence exactly when the difference is not eventually zero.
    The reference to the connectedness of R^omega is corrected to §23 Example 7.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

(a) What are the components and path components of $\RR^\omega$ (in the product topology)?

(b) Consider $\RR^\omega$ in the uniform topology.
Show that $\mathbf{x}$ and $\mathbf{y}$ lie in the same component of $\RR^\omega$ if and only if the sequence

$$
\mathbf{x} - \mathbf{y} = (x_1 - y_1, x_2 - y_2, \dots)
$$

is bounded.
[Hint: It suffices to consider the case where $\mathbf{y} = 0$.]

(c) Give $\RR^\omega$ the box topology.
Show that $\mathbf{x}$ and $\mathbf{y}$ lie in the same component of $\RR^\omega$ if and only if the sequence $\mathbf{x} - \mathbf{y}$ is "eventually zero."
[Hint: If $\mathbf{x} - \mathbf{y}$ is not eventually zero, show there is a homeomorphism $h$ of $\RR^\omega$ with itself such that $h(\mathbf{x})$ is bounded and $h(\mathbf{y})$ is unbounded.]
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.2, PDF pp. 7--8** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all three parts are theirs, with one citation corrected: the connectedness of $\RR^{\omega}$ in the product topology is Example 7 of §23, not of §13.

(a) In the product topology $\RR^{\omega}$ is connected (Example 7 of §23), so the whole space is its only component; it is path connected because $\RR$ is and a product of path-connected spaces is path connected (Exercise 24.8(a)), so the whole space is its only path component.

(b) In the uniform topology, $\mathbf{x}$ and $\mathbf{y}$ lie in the same component if and only if $\mathbf{x}-\mathbf{y}$ is bounded. Translation by $-\mathbf{x}$ is a homeomorphism, so it suffices to treat $\mathbf{y}=\mathbf{0}$. If $\mathbf{z}$ is unbounded then $\mathbf{z}$ and $\mathbf{0}$ are separated by the two open sets of bounded and unbounded sequences (Exercise 23.8), so $\mathbf{z}$ is not in the component of $\mathbf{0}$. If $\mathbf{z}$ is bounded, say $\abs{z_{n}}<M$, then $t\mapsto t\mathbf{z}$ is continuous from $[0,1]$ (for $\abs{t-t_{0}}<\varepsilon/M$ the uniform distance is $<M\cdot\varepsilon/M=\varepsilon$), giving a path from $\mathbf{0}$ to $\mathbf{z}$.

(c) In the box topology, $\mathbf{x}$ and $\mathbf{y}$ lie in the same component if and only if $\mathbf{x}-\mathbf{y}$ is eventually zero. If $\mathbf{x}-\mathbf{y}$ has finite support then $t\mapsto\mathbf{y}+t(\mathbf{x}-\mathbf{y})$ is a path: on the finitely many nonzero coordinates it is continuous and all other coordinates are fixed. If $\mathbf{x}-\mathbf{y}$ is not eventually zero, the homeomorphism of Exercise 19.8 given by $w_{i}=z_{i}-x_{i}$ where $x_{i}=y_{i}$ and $w_{i}=(z_{i}-x_{i})/\abs{x_{i}-y_{i}}$ otherwise sends $\mathbf{x}$ to $\mathbf{0}$ (bounded) and $\mathbf{y}$ to an unbounded sequence, and boundedness is a property of a sequence in the box topology that separates the two points as in (b).
:::
