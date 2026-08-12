---
schema: qual/card@1
id: P-3TOOU
kind: problem
title: "Main Idea: Deformation retract $M$ onto its center circle; two\u2026"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

5. **Main Idea**: Deformation retract $M$ onto its center circle; two spaces that deformation retract onto a common space are themselves homotopy equivalent.

Claim: $S^1 \cross I \homotopic S^1 \cross \theset{*}$ This is because $I$ is contractible, so $I \homotopic \theset{*}$.
(Maybe needs further proof)

Claim: $M \homotopic S^1 \cross \theset{*}$.

If both of these claims hold, then we will have $M \homotopic S^1 \cross I$ as two spaces that deformation retract onto a common space.
Identifying $M = I \cross I / \sim$ where $(x, 0) \sim (1-x, 1)$, fix $x=1/2$.

Then consider the subspace $U = \theset{(1/2, y) \mid y \in [0,1]} \subset M$.
Claim: $U \cong \theset{*} \cross S^1$ for some point $*$.

$U$ can be written $\theset{1/2} \cross (I/\sim)$, and since $(1/2, 0) \sim (1/2,1)$, we have $I/ \sim =  I /\bd I \cong S^1$, so $U \cong \theset{1/2}\cross S^1$ as desired (taking $* = \frac{1}{2}$).

However, we can define a homotopy from $M$ onto $U$, in the form of a deformation retract.

Let $F: M \cross I \into M$ be defined by $F((x,y), t) = F_t(x,y) = ((1-t)x + \frac{1}{2}t, y)$.
Then $F((x,y), 0) = (x,y) = \id_M$, and $F((x,y), 1) = (\frac{1}{2}, y) \subseteq U$.
Moreover, if $(x,y) \in U$, then $(x,y) = (\frac{1}{2}, y)$ and $F((x,y), t) = ((1-t)\frac{1}{2} + \frac{1}{2}t, y) = (\frac{1}{2} - t\frac{1}{2} + \frac{1}{2}t, y) = (\frac{1}{2}, y) = (x,y)$, so $F = \id_U$.
This makes $F$ a deformation retract from $M$ onto $U$, and so $M \homotopic U$.

But then, summarizing our results, we have $S^1 \cross I \homotopic S^1 \cross \theset{*} \cong S^1 \cross \theset{\frac{1}{2}} = U \homotopic M$, and so $S^1 \cross I \homotopic M$ as desired.
