---
schema: qual/card@1
id: P-AGXGATHPULLBACK
kind: problem
title: Morphisms of affine varieties against the induced maps of coordinate rings
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms of Varieties
  - Coordinate Rings
  - Automorphisms
relations: []
review: draft
---

::: {.problem}
Let $f:X\to Y$ be a morphism of affine varieties and $f^*: A(Y) \to A(X)$ the induced map on coordinate rings.
Determine whether the following statements are true or false:

(a) $f$ is surjective $\iff$ $f^*$ is injective.

(b) $f$ is injective $\iff$ $f^*$ is surjective.

(c) If $f:\AA^1\to\AA^1$ is an isomorphism, then $f$ is *affine linear*, i.e. $f(x) = ax+b$ for some $a, b\in k$.

(d) If $f:\AA^2\to\AA^2$ is an isomorphism, then $f$ is *affine linear*, i.e. $f(x) = Ax+b$ for some $A \in \Mat(2\times 2, k)$ and $b\in k^2$.
:::

::: {.solution}
Let $k$ be the algebraically closed ground field.
For a morphism $f$, the map $f^*$ sends $p \in A(Y)$ to $p \circ f \in A(X)$.

::: pf

::: {.pf-step}
Part (a) is false: surjectivity of $f$ implies injectivity of $f^*$, but the converse fails.

::: pf-proof
Suppose $f$ is surjective and $f^*p = f^*q$, that is, $p \circ f = q \circ f$.
Every $y \in Y$ is $f(x)$ for some $x \in X$, so $p(y) = q(y)$; hence $p = q$, and $f^*$ is injective.

For the converse, let $X \coloneqq V(xy-1) \subseteq \AA^2$ and let $f: X \to \AA^1$ be $(x,y) \mapsto x$.
Its image is $\AA^1 \sm \theset{0}$, so $f$ is not surjective.
The ring $k[x,y]/\generators{xy-1}$ is isomorphic to $k[x,x^{-1}]$ by $y \mapsto x^{-1}$, and under this isomorphism $f^*$ is the inclusion $k[x] \hookrightarrow k[x,x^{-1}]$, which is injective.
:::

:::

::: {.pf-step}
Part (b) is false: surjectivity of $f^*$ implies injectivity of $f$, but the converse fails.

::: pf-proof
Suppose $f^*$ is surjective, $X \subseteq \AA^n$, and $f(a) = f(b)$ for $a, b \in X$.
Each coordinate function $x_j \in A(X)$ equals $p \circ f$ for some $p \in A(Y)$, so $x_j(a) = p(f(a)) = p(f(b)) = x_j(b)$.
Hence $a = b$, and $f$ is injective.

For the converse, let $Y \coloneqq V(y^2 - x^3) \subseteq \AA^2$ and let $f: \AA^1 \to Y$ be $t \mapsto (t^2, t^3)$.
A point $(x,y) \in Y$ with $x \neq 0$ has the unique preimage $t = y/x$, and $(0,0)$ has the unique preimage $t = 0$, so $f$ is bijective.
The map $f^*: k[x,y]/\generators{y^2-x^3} \to k[t]$ sends $x \mapsto t^2$ and $y \mapsto t^3$, so its image is spanned by the monomials $t^{2a+3b}$ with $a, b \geq 0$.
No such exponent equals $1$, so $t$ is not in the image and $f^*$ is not surjective.
:::

:::

::: {.pf-step}
Part (c) is true: every isomorphism $f: \AA^1 \to \AA^1$ is $x \mapsto ax+b$ with $a \neq 0$.

::: pf-proof
Morphisms $\AA^1 \to \AA^1$ are polynomial maps, so $f$ and its inverse $g$ are polynomials with $f(g(x)) = x$ for all $x \in k$.
Since $k$ is infinite, this is an identity of polynomials.
Neither $f$ nor $g$ is constant, because the composite is not constant.
For nonconstant polynomials, $\deg(f \circ g) = \deg f \cdot \deg g$, because the leading term of $f \circ g$ is the leading coefficient of $f$ times the $(\deg f)$-th power of the leading term of $g$, which is nonzero since $k$ is a field.
So $\deg f \cdot \deg g = 1$, hence $\deg f = 1$, and $f(x) = ax + b$ with $a \neq 0$.
:::

:::

::: {.pf-step}
Part (d) is false: there are isomorphisms $\AA^2 \to \AA^2$ that are not affine linear.

::: pf-proof
Let $f(x,y) \coloneqq (x,\, y + x^2)$ and $g(x,y) \coloneqq (x,\, y - x^2)$.
Both are polynomial maps, so both are morphisms.
Substitution gives $g(f(x,y)) = (x,\, y + x^2 - x^2) = (x,y)$ and $f(g(x,y)) = (x,\, y - x^2 + x^2) = (x,y)$, so $f$ is an isomorphism.
The second coordinate of $f$ has degree $2$, so $f$ is not of the form $Ax + b$.
:::

:::

:::
:::
