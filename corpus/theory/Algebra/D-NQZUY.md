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
An \dfn{$R$-algebra} structure on an $R$-module $M$ is an associative multiplication $M\times M\to M$, $(a,b)\mapsto ab$, with an identity element, that is $R$-bilinear:
$$
(a+a')b = ab + a'b,\qquad a(b+b') = ab + ab',\qquad r(ab) = (ra)b = a(rb)
$$
for all $r\in R$ and $a,a',b,b'\in M$.
Equivalently, the multiplication is an $R$-linear map $M\otimes_R M\to M$, $a\otimes b\mapsto ab$.
:::
