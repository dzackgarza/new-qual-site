---
schema: qual/card@1
id: P-AGH5217CONORMALSPLIT
kind: problem
title: Splitting type of the conormal bundle of rational space curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ruled Surfaces
  - Picard Group
relations: []
review: draft
---

::: {.problem}
a. Let $\varphi: \PP_k^1 \rightarrow \PP_k^3$ be the 3-uple embedding (I, Ex. 2.12). Let $\mathcal{I}$ be the sheaf of ideals of the twisted cubic curve $C$ which is the image of $\varphi$. Then $\mathcal{I} / \mathcal{I}^2$ is a locally free sheaf of rank 2 on $C$, so $\varphi^*\left(\mathcal{I} / \mathcal{I}^2\right)$ is a locally free sheaf of rank 2 on $\PP^1$.
  By (2.14), therefore,
  \[
\varphi^*\left(\mathcal{I} / \mathcal{I}^2\right) \cong \mathcal{O}(l) \oplus \mathcal{O}(m)
  .\]
  for some $l, m \in \ZZ$. Determine $l$ and $m$.

b. Repeat part (a) for the embedding $\varphi: \PP^1 \rightarrow \PP^3$ given by $x_0=t^4$, $x_1=t^3 u$, $x_2=t u^3$, $x_3=u^4$, whose image is a nonsingular rational quartic curve.

  Answer: If $\operatorname{char} k \neq 2$, then $l=m=-7$; if $\operatorname{char} k=2$, then $l, m=-6,-8$.
:::
