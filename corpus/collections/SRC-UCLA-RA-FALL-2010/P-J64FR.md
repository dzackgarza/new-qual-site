---
schema: qual/card@1
id: P-J64FR
kind: problem
title: Boundedness of $f\mapsto f(1)$ on a weighted Hardy space, its Riesz representer,
  and the maximum of $\operatorname{Re}f(1)$ on $\{f:\|f\|\le 1,\,f(0)=0\}$
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Riesz Representation
  - Series of Functions
relations: []
review: draft
---

::: {.problem}
Consider the complex Hilbert space $$H := \left\{f:\overline{\mathbb{D}}\to\mathbb{C}: f(z)=\sum_{k=0}^\infty \widehat{f}(k)z^k \text{ with } ||f||^2 := \sum_{k=0}^\infty (1+k^2)|\widehat{f}(k)|^2 < \infty\right\}.$$

a. Prove that the linear function $L:f\mapsto f(1)$ is bounded.

b. Find the element $g\in H$ representing $L$.

c. Show that $f\mapsto \text{Re}\,L(f)$ achieves its maximal value on the set $$B := \{f\in H: ||f||\le1 \text{ and } f(0)=0\},$$ that this maximum occurs at a unique point, and determine this maximal value.
:::
