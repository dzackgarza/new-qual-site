---
schema: qual/card@1
id: P-UTCT-2-24
kind: problem
title: Characteristic foliation of $dz+a\,dx+b\,dy$ on the $xy$-plane
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
  note: Checked against Exercise 2.24 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Recovered the foliation equation x^b y^a = c from p. 20 of Gompf Contact Topology.pdf, stated the definitions of sign and divergence, and noted that the printed form with constant a, b does not give that foliation.
---

::: {.problem}
For a surface $F$ in a $3$-manifold with a plane field $\xi = \ker(\alpha)$, the characteristic foliation $\mathcal{F}$ of $F$ is cut out by a vector field $v$ with $\iota_v \omega = \alpha|_F$ for a positive area form $\omega$ on $F$, where $\operatorname{div}_\omega v$ is defined by $\mathcal{L}_v \omega = (\operatorname{div}_\omega v)\,\omega$, and $\operatorname{sign}(\xi) = \operatorname{sign}(\alpha \wedge d\alpha)$.

Let $M = \mathbb{R}^3$ and let $\alpha = dz + a\,dx + b\,dy$ for $(a, b) \in \mathbb{R}^2 - \{0\}$.
Determine $\operatorname{sign}(\xi)$ and $\operatorname{div}_\omega v$ for $\mathcal{F}$ on the $x$-$y$ plane.
Check that the characteristic foliation is given by $x^b y^a = c$.
Draw a picture and observe how these vary with $a$ and $b$.
How is $\operatorname{sign}(\operatorname{div}_\omega \mathcal{F})$ visible?
:::

::: {.remark}
The first paragraph restates the definitions of Section 2 of the source (Definition 2.20, Theorem 2.23).
As printed, with $a$ and $b$ constants, $d\alpha = 0$, and $\alpha|_{xy\text{-plane}} = a\,dx + b\,dy$ has the lines $ax + by = c$ as leaves rather than the curves $x^b y^a = c$; the source does not say how $a$ and $b$ are meant to vary.
:::
