---
schema: qual/card@1
id: P-AGH214SEGRE
kind: problem
title: The Segre embedding of $\PP^r \times \PP^s$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Segre Embedding
  - Projective Varieties
  - Homogeneous Ideals
relations: []
review: draft
---

::: problem
Let $\psi: \PP^r \times \PP^s \to \PP^N$ be the map sending the ordered pair $\tv{a_0 : \cdots : a_r} \times \tv{b_0 : \cdots : b_s}$ to the point with coordinates $a_i b_j$ in lexicographic order, where $N = rs + r + s$.
The map $\psi$ is well defined and injective; it is called the **Segre embedding**. Show that the image of $\psi$ is a subvariety of $\PP^N$.

*Hint:* let the homogeneous coordinates of $\PP^N$ be $\ts{z_{ij} \st 0 \leq i \leq r,\ 0 \leq j \leq s}$, and let $\mfa$ be the kernel of the homomorphism $k[\ts{z_{ij}}] \to k[x_0,\ldots,x_r,y_0,\ldots,y_s]$ sending $z_{ij} \mapsto x_i y_j$.
Then show $\im \psi = Z(\mfa)$.
:::
