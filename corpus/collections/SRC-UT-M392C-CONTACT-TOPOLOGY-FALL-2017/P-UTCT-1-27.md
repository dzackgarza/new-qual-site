---
schema: qual/card@1
id: P-UTCT-1-27
kind: problem
title: Poincaré--Hopf theorem for surfaces with boundary via the relative Euler class
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
  note: Checked against Exercise 1.27 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated Definition 1.24 and Example 1.26, on which the exercise depends, from pp. 6-7 of Gompf Contact Topology.pdf.
---

::: {.problem}
Let $F$ be a compact, oriented, connected surface with $\partial F \neq \emptyset$, and let $\xi \to F$ be an oriented plane bundle.
Given a nowhere zero section $v$ of $\xi$ over $\partial F$, the relative Euler class $e(\xi, v)$ is $[w^{-1}(0)]$ for an extension $w$ of $v$ to all of $F$ transverse to the zero section, that is, the signed count
$$
e(\xi, v) = \sum_{v(x) = 0} \operatorname{sign}_v(x).
$$
Changing $e(\xi, v)$ by $\pm 1$ is the same as adding $\pm 1$ twists to $v|_{\partial F}$, so for suitable $v$ (the "fix" on $v$) the zeros can be pushed to the boundary and $e(\xi, v) = 0$.

Show that not doing the fix on $v$ above retrieves the Poincaré--Hopf theorem as in the boundaryless case.
That is, for $F$ compact and connected, show that
$$
\chi(F) = e(TF, v),
$$
where on each component of $\partial F$, either $v$ is parallel to $\partial F$ or $v$ is perpendicular to $\partial F$.
:::
