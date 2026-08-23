---
schema: qual/card@1
id: P-CAF05D
kind: problem
title: "Using Runge-type approximation to separate values outside a compact set"
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
Let $K \subset G \subset \mathbb{C}$ with $K$ compact and $G$ open.
Suppose that for any $f$ analytic in an open neighborhood of $K$ and any $\epsilon > 0$ there is $g \in H(G)$ so that $|f(z) - g(z)| < \epsilon$ for all $z \in K$.
Let $z_0 \in G \setminus K$ be arbitrary.
Show that there exists $h \in H(G)$ such that $$|h(z_0)| > \sup_{w \in K} |h(w)|.$$
:::
