---
schema: qual/card@1
id: P-UTCT-1-53
kind: problem
title: Contactomorphism from the cylindrically symmetric to the standard contact structure on $\mathbb R^3$
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
  note: Checked against Exercise 1.53 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the forms alpha (Example 1.48) and alpha-prime (Example 1.52) from p. 12 of Gompf Contact Topology.pdf, with a remark on the missing dz in the source.
---

::: {.problem}
On $\mathbb{R}^3$ let $\alpha = dz + x\,dy$ be the standard contact form, and let $\xi' = \ker(\alpha')$, where
$$
\alpha' = dz + \tfrac{1}{2} r^2\, d\theta = dz + \frac{x\,dy - y\,dx}{2}
$$
is the cylindrically symmetric contact form.
Let $\phi : \mathbb{R}^3 \to \mathbb{R}^3$ be
$$
\phi(x, y, z) = (x, y, z + xy/2).
$$
Show that $\phi^*\alpha' = \alpha$, where $\alpha'$ is from the example above and $\alpha$ is the standard contact structure.
This is an example of a contactomorphism.
:::

::: {.remark}
Example 1.52 of the source prints $\alpha' = dx + \frac{1}{2} r^2 d\theta$ and gives its rectangular form as $\frac{x\,dy - y\,dx}{2}$; both omit $dz$, which is needed for $\alpha'$ to be a contact form and for $\phi^*\alpha' = \alpha$ to hold.
:::
