---
schema: qual/card@1
id: P-AGH31CONICS
kind: problem
title: Conics, and varieties that are not isomorphic to one another
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms
  - Conics
  - Isomorphism
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all five parts with the retained Hartshorne I.3.1 transcription and checked the projective global-functions theorem at I.3.4(a). The conic normal form uses no division by two. The plane-topology obstruction is proved by closed curves and the height theorem, not by comparing rings of functions.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be algebraically closed.
A conic means the zero set of an irreducible polynomial of degree two, homogeneous in the projective case.

(a) Show that any conic in $\AA_k^2$ is isomorphic either to $\AA_k^1$ or to $\AA_k^1 \sm \theset{0}$.

(b) Show that $\AA_k^1$ is not isomorphic to any proper open subset of itself.

(c) Show that any conic in $\PP_k^2$ is isomorphic to $\PP_k^1$.

(d) Show that $\AA_k^2$ is not even homeomorphic to $\PP_k^2$.

(e) Show that if an affine variety is isomorphic to a projective variety, then it consists of a single point.
:::

::: {.solution}
All isomorphisms are isomorphisms of varieties over $k$, and all topologies are Zariski topologies on their classical point sets.

::: pf

::: {.pf-step #s1}

Every projective conic can be changed by projective linear coordinates to $x^2-yz=0$, parametrized isomorphically by
$$
[s:t]\longmapsto[st:s^2:t^2].
$$

::: pf-proof

Let $q$ be the irreducible homogeneous quadratic defining the conic, and choose a point on it.
Put that point at $[0:1:0]$ by a projective linear change of coordinates.
Then
$$
q=ax^2+bxy+cxz+eyz+fz^2.
$$
The pair $(b,e)$ is not zero: otherwise $q$ would be a binary quadratic in $x,z$, which factors into linear forms over the algebraically closed field.
Change the two coordinates $x,z$ so that $bx+ez$ becomes $z$.
The equation then has the form
$$
q=yz+Ax^2+Bxz+Cz^2.
$$
Replacing $y$ by $y'=y+Bx+Cz$ gives $q=y'z+Ax^2$.
Here $A\ne0$, since $A=0$ would make the equation reducible.
The invertible scaling $y''=-y'/A$ gives $q=A(x^2-y''z)$.
This proves the normal form without a characteristic restriction.

The displayed parametrization is the quadratic Veronese embedding of $\PP^1$, with reordered coordinates, and hence is an isomorphism onto its image by [[P-AGH212DUPLE]].
Its image is exactly $x^2-yz=0$.
On $y\ne0$, normalize $y=1$, so $z=x^2$ and the point is the image of $[1:x]$.
On $y=0$, the equation forces $x=0$, giving $[0:0:1]$, the image of $[0:1]$.

:::

:::

::: {.pf-step #s2}

An affine conic is isomorphic to $\AA^1$ or to $\AA^1\setminus\{0\}$, proving (a).

::: pf-proof

Homogenize its irreducible degree-two equation to obtain $\overline C\subseteq\PP^2$.
The homogenized polynomial is irreducible: a factorization would dehomogenize to a factorization of the original polynomial, unless one homogeneous factor were a power of the homogenizing variable times a scalar.
That exception is impossible because the degree-two part of the original polynomial is nonzero, so its homogenization is not divisible by the homogenizing variable.
Thus $\overline C$ is an irreducible projective conic, and the affine conic is its complement of the line at infinity.

By step [](#s1){.pf-ref}, $\overline C\cong\PP^1$ through quadratic coordinate polynomials.
The pullback of the line at infinity is therefore the zero set of a nonzero homogeneous binary quadratic.
It is nonzero because the line does not contain the conic.
Over $k$, its factorization into two linear forms shows that its zero set consists of either one point or two distinct points.
An automorphism of $\PP^1$ sends a single point to infinity, or two distinct points to $0$ and infinity, by choosing their representative vectors as coordinate vectors.
Taking complements gives respectively $\PP^1\setminus\{\infty\}=\AA^1$ or $\PP^1\setminus\{0,\infty\}=\AA^1\setminus\{0\}$.

:::

:::

::: {.pf-step #s3}

The affine line is not isomorphic to a proper open subset of itself, proving (b).

::: pf-proof

The empty open subset is not isomorphic to the nonempty affine line.
Let $U$ be a nonempty proper open subset, and choose a point $a\in\AA^1\setminus U$.
The regular function $t-a$ is a unit on $U$, with inverse $1/(t-a)$, and is not constant there: every nonempty open subset of $\AA^1$ is cofinite and infinite.

An isomorphism $\AA^1\cong U$ would give a $k$-algebra isomorphism between their rings of global regular functions.
The only units of $k[t]=\Gamma(\AA^1,\OO)$ are nonzero constants, because degrees add under multiplication.
The pullback of the nonconstant unit $t-a$ would thus be constant, and applying the inverse $k$-algebra isomorphism would make $t-a$ constant on $U$, a contradiction.

:::

:::

::: {.pf-step #s4}

Every projective conic is isomorphic to $\PP^1$, proving (c).

::: pf-proof

Step [](#s1){.pf-ref} gives a projective linear isomorphism from the conic to $x^2-yz=0$ and an isomorphism of the latter with $\PP^1$.
Composing these isomorphisms proves (c), including in characteristic two.

:::

:::

::: {.pf-step #s5}

The spaces $\AA^2$ and $\PP^2$ are not homeomorphic, proving (d).

::: pf-proof

First, any two irreducible closed curves in $\PP^2$ meet.
By [[P-AGH28HYPERSURFACE]], they are defined by irreducible homogeneous equations $f,g$ in $S=k[x,y,z]$.
If their projective intersection were empty, the affine common zero set of these positive-degree homogeneous polynomials would consist only of the origin.
The affine Nullstellensatz would then give $\sqrt{(f,g)}=(x,y,z)$ [@Har10a, Theorem I.1.3A].
The latter prime has height three, contradicting Krull's height theorem for an ideal with two generators.
This proves the intersection assertion.

In $\AA^2$, the two closed irreducible lines $x=0$ and $x=1$ are disjoint.
A homeomorphism to $\PP^2$ would carry them to disjoint irreducible closed subsets of dimension one: closedness, irreducibility and lengths of chains of irreducible closed subsets are all preserved by homeomorphisms.
Their images would be disjoint projective curves, contradicting the assertion just proved.
Therefore no such homeomorphism exists.

:::

:::

::: {.pf-step #s6}

A variety that is both affine and projective up to isomorphism is a single point, proving (e).

::: pf-proof

Let $V\subseteq\AA^m$ be affine and isomorphic to a projective variety $W$.
Every global regular function on $W$ is constant [@Har10a, Theorem I.3.4(a)], so the induced isomorphism of global function rings gives $\Gamma(V,\OO_V)=k$.
In particular, each of the $m$ affine coordinate functions restricts to a constant $c_i$ on $V$.
Thus every point of $V$ has coordinates $(c_1,\ldots,c_m)$.
Since a variety is nonempty, $V$ is precisely that one point.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} prove parts (a)--(e), respectively; step [](#s1){.pf-ref} supplies the characteristic-independent conic calculation used in (a) and (c).

:::

:::

:::
