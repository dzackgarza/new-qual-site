---
schema: qual/card@1
id: PR-Z3YWJ
kind: proposition
title: First isomorphism theorem for rings
classification:
  areas:
  - algebra
  topics:
  - Isomorphism Theorems
  - Rings
  - Homomorphisms
relations: []
review: draft
---

::: {.proposition}
Let $f\colon A\to B$ be a [[D-GXMDW|ring homomorphism]].
Then $\ker f$ is an [[D-GOFWL|ideal]] of $A$, $\im f$ is a subring of $B$, and $f$ induces a ring isomorphism
$$
\bar f\colon A/\ker f \to \im f,\qquad a+\ker f\mapsto f(a).
$$
In particular, if $f$ is surjective, then $A/\ker f \cong B$.
As abelian groups, $0 \to \ker f \to A \mapsvia{f} \im f \to 0$ is exact.
:::

::: {.proof}
If $x,y\in\ker f$ and $a\in A$, then $f(x-y)=0$ and $f(ax)=f(a)f(x)=0=f(x)f(a)=f(xa)$, so $\ker f$ is an ideal.
The image contains $1_B=f(1_A)$ and is closed under subtraction and multiplication, so it is a subring.
The map $\bar f$ is well defined and injective because $f(a)=f(a')$ if and only if $a-a'\in\ker f$; it is surjective onto $\im f$ by construction, and it is a ring homomorphism because $f$ is.
:::
