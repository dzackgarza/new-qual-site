---
schema: qual/card@1
id: P-UTCT-1-23
kind: problem
title: Homotopy classes of plane fields on the lens space $L(p,q)$
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
  note: Checked against Exercise 1.23 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the construction of Gamma_tau, Corollary 1.21 and Example 1.22, on which the exercise depends, from pp. 5-6 of Gompf Contact Topology.pdf.
---

::: {.problem}
Let $M$ be a closed, oriented $3$-manifold with a trivialization $\tau$ of $TM$, so that oriented plane fields on $M$ up to homotopy correspond to $[M, S^2]$ and hence to framed cobordism classes of framed links in $M$.
Let $\Gamma_\tau$ be the map taking an oriented plane field $\xi$ to the class in $H_1(M)$ of the corresponding framed link; it is onto, and the Euler class satisfies $\operatorname{PD}(e(\xi)) = 2\Gamma_\tau(\xi)$.
Consequently an oriented plane bundle $\xi$ on $M$ is realized as a plane field if and only if $e(\xi) = 2x$ for some $x \in H_1(M)$.

Example: consider $M = \mathbb{RP}^3$.
We know $H_1(\mathbb{RP}^3) = \mathbb{Z}/2\mathbb{Z}$.
Note that only $0 \in H_1$ can be represented as $2x$, so every plane field in $\mathbb{RP}^3$ is trivial as a plane bundle.
For fixed choice of $\tau$, however, we get two values of $\Gamma_\tau$ and therefore there are at least two different plane fields that are not homotopic.

Analyze the lens space $L(p,q)$ in the same way.
(Hint: $H_1(L(p,q)) = \mathbb{Z}/p\mathbb{Z}$.)
:::
