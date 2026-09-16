---
schema: qual/card@1
id: P-UTCT-3-15
kind: problem
title: Generic characteristic foliations satisfy the hypotheses of Giroux's dividing set theorem
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
  note: Checked against Exercise 3.15 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the truncated statement with Exercise 3.15 and the hypotheses of Theorem 3.13 it refers to, from p. 25 of Gompf Contact Topology.pdf.
---

::: {.problem}
Let $F$ be a compact oriented surface with an oriented singular foliation $\mathcal{F}$.
For a closed leaf, the monodromy $\phi : I \to I$ along a normal interval is defined by following the foliation until it intersects the normal again; the leaf is *attractive* if $\phi'(0) < 1$ and *repellant* if $\phi'(0) > 1$.
Define
$$
K_+ = \{+ \text{ singular points}\} \cup \{\text{repellant closed leaves}\}, \qquad K_- = \{- \text{ singular points}\} \cup \{\text{attractive closed leaves}\}.
$$
Theorem 3.13 (Giroux et al.) assumes that $\partial F$ is a union of leaves and critical points and that:

1. Each leaf limits as $t \to \pm\infty$ to a singular point or closed leaf ($t$ is a parameter on the leaf).
2. Each singular point has nonzero divergence and each closed leaf is either repellant or attractive (i.e. $\phi'(0) \neq 1$).
3. No leaf runs from $K_-$ to $K_+$.
4. The collection of singular points of $\mathcal{F}$ has finitely many connected components which can be ordered so that each leaf between points of the same sign preserves that order.

Show that the hypotheses of Theorem 3.13 hold for generic a generic foliation of $F$.
:::
