---
schema: qual/card@1
id: D-NQZUY
kind: definition
title: Modules over a ring
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Algebras
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring.
A \dfn{left $R$-module} is an abelian group $(M,+)$ together with a map $R\times M\to M$, $(r,x)\mapsto rx$, such that for all $r,s\in R$ and $x,y\in M$:

- $r(x+y) = rx + ry$;
- $(r+s)x = rx + sx$;
- $(rs)x= r(sx)$;
- $1_Rx = x$.
:::

::: {.definition}
Let $R$ be a commutative ring.
An \dfn{$R$-algebra} structure on an $R$-module $M$ is an $R$-bilinear multiplication $M\times M\to M$, equivalently an $R$-linear map $m\colon M\otimes_R M\to M$; bilinearity means
$$
r\, m(a\otimes b) = m(ra \otimes b) = m(a\otimes rb) \qquad \text{for all } r\in R \text{ and } a,b \in M.
$$
:::
