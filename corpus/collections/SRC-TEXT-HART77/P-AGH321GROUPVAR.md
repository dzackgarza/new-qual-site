---
schema: qual/card@1
id: P-AGH321GROUPVAR
kind: problem
title: Group varieties $\GG_a$ and $\GG_m$, and the group structure on $\Hom(X,G)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Group Varieties
  - Morphisms
  - Regular Functions
relations:
- kind: uses
  target: P-AGH316QPPRODUCT
- kind: uses
  target: P-AGH310SUBVARIETY
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all five parts with Hartshorne I.3.21. The proof uses the variety-product universal property to define pointwise multiplication on Hom(X,G), and identifies maps to G_a and G_m directly with global regular functions and units.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the group axioms, morphism closure, and the two Hom identifications against the source and published solution notes. The proof does not assume X affine when identifying Hom(X,G_a) with O(X).'
---

::: {.problem}
A **group variety** consists of a variety $Y$ together with a morphism $\mu: Y \times Y \to Y$ such that the set of points of $Y$ with the operation given by $\mu$ is a group, and such that the inverse map $y \mapsto \inverseof{y}$ is also a morphism $Y \to Y$.

(a) The **additive group** $\GG_a$ is the variety $\AA^1$ with the morphism $\mu: \AA^1 \times \AA^1 \to \AA^1$ defined by $\mu(a,b) = a+b$.
    Show that it is a group variety.

(b) The **multiplicative group** $\GG_m$ is the variety $\AA^1 \sm \ts{0}$ with the morphism $\mu(a,b) = ab$.
    Show that it is a group variety.

(c) If $G$ is a group variety and $X$ is any variety, show that the set $\Hom(X, G)$ has a natural group structure.

(d) For any variety $X$, show that $\Hom(X, \GG_a)$ is isomorphic to $\mco(X)$ as a group under addition.

(e) For any variety $X$, show that $\Hom(X, \GG_m)$ is isomorphic to the group of units in $\mco(X)$, under multiplication.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The variety $\GG_a=\AA^1$ with addition is a group variety.

::: pf-proof

The underlying set is the field $k$, which is an abelian group under addition with identity $0$.
The multiplication map in the sense of group varieties is
$$
\mu:\AA^2\to\AA^1,
\qquad
(a,b)\longmapsto a+b,
$$
whose coordinate function $a+b$ is polynomial, hence $\mu$ is a morphism.
The inverse map is
$$
\iota:\AA^1\to\AA^1,
\qquad
a\longmapsto-a,
$$
also polynomial and therefore a morphism.
Thus all requirements in the definition are satisfied, proving (a).

:::

:::

::: {.pf-step #s2}

The variety $\GG_m=\AA^1\setminus\{0\}$ with multiplication is a group variety.

::: pf-proof

Its underlying set is $k^\times$, a group under multiplication with identity $1$.
The multiplication map
$$
\mu:\GG_m\times\GG_m\to\GG_m,
\qquad
(a,b)\longmapsto ab
$$
is the restriction of the polynomial multiplication morphism $\AA^2\to\AA^1$ and its image avoids $0$.
Hence it is a morphism to $\GG_m$.

On the principal affine open $\GG_m=D(x)$, the function $x^{-1}$ is regular.
Therefore
$$
\iota:\GG_m\to\GG_m,
\qquad
a\longmapsto a^{-1}
$$
is a morphism.
Thus $\GG_m$ is a group variety, proving (b).

:::

:::

::: {.pf-step #s3}

For morphisms $f,g:X\to G$, define
$$
f*g=\mu\circ(f,g):X\to G.
$$
This equips $\Hom(X,G)$ with a group structure, proving (c).

::: pf-proof

By [[P-AGH316QPPRODUCT]], the pair
$$
(f,g):X\to G\times G,
\qquad
x\longmapsto(f(x),g(x))
$$
is a morphism.
Composing with the group multiplication morphism $\mu:G\times G\to G$ shows that $f*g$ is again a morphism.

Let $e\in G$ be the identity element.
The constant map
$$
e_X:X\to G,
\qquad
x\longmapsto e
$$
is a morphism and is an identity for $*$ pointwise.
If $\iota:G\to G$ is the inverse morphism, then
$$
f^{-1}=\iota\circ f
$$
is a morphism and is a pointwise inverse to $f$.
Associativity follows pointwise from associativity in the underlying group of $G$:
$$
((f*g)*h)(x)=(f(x)g(x))h(x)=f(x)(g(x)h(x))=(f*(g*h))(x).
$$
Thus all group axioms hold.

:::

:::

::: {.pf-step #s4}

The map
$$
\Phi_a:\Hom(X,\GG_a)\longrightarrow\mco(X),
\qquad
h\longmapsto h^*(t)=t\circ h
$$
is an isomorphism of additive groups.

::: pf-proof

A morphism $h:X\to\AA^1$ pulls the affine coordinate $t$ back to a global regular function on $X$, so $\Phi_a$ is well-defined.

Conversely, if $f\in\mco(X)$, the map
$$
h_f:X\to\AA^1,
\qquad
x\longmapsto f(x)
$$
is a morphism: locally $f$ is a quotient of regular coordinate functions with nonvanishing denominator, which is exactly the local criterion for a morphism to affine space.
Clearly
$$
\Phi_a(h_f)=f,
$$
and a map to $\AA^1$ is determined by its coordinate function, so this construction is inverse to $\Phi_a$.

Finally, for $h_1,h_2:X\to\GG_a$,
$$
\Phi_a(h_1*h_2)(x)=h_1(x)+h_2(x)
=\Phi_a(h_1)(x)+\Phi_a(h_2)(x).
$$
Hence $\Phi_a$ is a group isomorphism, proving (d).

:::

:::

::: {.pf-step #s5}

The map
$$
\Phi_m:\Hom(X,\GG_m)\longrightarrow\mco(X)^\times,
\qquad
h\longmapsto t\circ h
$$
is an isomorphism of multiplicative groups.

::: pf-proof

If $h:X\to\GG_m$ is a morphism, then
$$
u=t\circ h
$$
is a global regular function which never vanishes.
Composing $h$ with the inversion morphism on $\GG_m$ shows that
$$
u^{-1}=t\circ\iota\circ h
$$
is also globally regular.
Thus $u\in\mco(X)^\times$.

Conversely, let $u\in\mco(X)^\times$ and let $v\in\mco(X)$ satisfy $uv=1$.
Then $u(x)\ne0$ for every $x\in X$, so the morphism
$$
x\longmapsto u(x)
$$
to $\AA^1$ factors set-theoretically through the open subvariety $\GG_m$.
By the subvariety restriction criterion, it is a morphism $X\to\GG_m$.
These constructions are inverse.

Pointwise multiplication gives
$$
\Phi_m(h_1*h_2)=\Phi_m(h_1)\Phi_m(h_2),
$$
so $\Phi_m$ is a group isomorphism, proving (e).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove (a)--(e), respectively.

:::

:::

:::
