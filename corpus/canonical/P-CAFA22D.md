---
schema: qual/card@1
id: P-CAFA22D
kind: problem
title: "Mean value inequality and completeness of A^1(G)"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
solved: false
---

::: problem
Let $G \subset \mathbb{C}$ be a bounded region.

(i) Show that if $f \in H(G)$ and $B = B(a,r) \subset G$, then
$$
|f(a)| \leq \frac{1}{|B|} \int_B |f(z)|\,dx\,dy,
$$
where $|B|$ denotes the area of $B$.

(ii) Show that the space
$$
A^1(G) = \{f \in H(G) : \|f\|_1 := \int_G |f(z)|\,dx\,dy < \infty\}
$$
endowed with the metric $d(f,g) = \|f - g\|_1$ is complete.

Note: You may use the result in part (i) even if you did not prove this.
:::
