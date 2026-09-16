---
schema: qual/card@1
id: P-UTCT-4-3
kind: problem
title: The standard contact form on $S^3$
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Exercise 4.3 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the construction of the standard contact form on S^3 preceding the exercise, from p. 32 of Gompf Contact Topology.pdf.
---

::: {.problem}
Write $S^3 = \partial B^4 \subset \mathbb{C}^2$ as the preimage of $1$ of the function $r^2$, so that $\ker(d(r^2))$ along $S^3$ is $TS^3$.
There is a complex structure $J$ on $TS^3$ inherited from $\mathbb{C}^2$.
Write $\alpha = d(r^2) \circ J$, and let $\xi = \ker(\alpha|_{S^3})$, the standard structure on $S^3$.

Verify that this is a positive contact form by showing that
$$
d(r^2) \wedge \alpha \wedge d\alpha
$$
is a positive volume form on $\mathbb{C}^2$, and therefore $\alpha \wedge d\alpha$ is a positive volume form on $S^3$.
Do this by showing that
$$
\alpha = x_1\,dy_1 - y_1\,dx_1 + x_2\,dy_2 - y_2\,dx_2
$$
and computing $\alpha \wedge d\alpha$.
Can you show that this form restricted to $S^3 - \{*\}$ is contactomorphic to $(\mathbb{R}^3, dz + x\,dy)$?
:::
