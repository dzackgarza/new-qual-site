---
schema: qual/card@1
id: P-AGH453MODULIGENUSFOUR
kind: problem
title: Dimensions of the families of curves of genus $4$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Canonical Divisor
  - Hyperelliptic Curves
  - Linear Systems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.5.3 and the canonical genus-four complete-intersection
    description referenced by the hint. Cross-checked that a nonhyperelliptic
    genus-four canonical curve is a (2,3) complete intersection and that its
    g^1_3's correspond to the rulings of its unique quadric.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
The hyperelliptic curves of genus 4 form an irreducible family of dimension 7. The nonhyperelliptic ones form an irreducible family of dimension 9. The subset of those having only one $g_3^1$ is an irreducible family of dimension 8.

Hint: Use (5.2.2) to count how many complete intersections $Q \intersect F_3$ there are.
:::

::: {.solution}
We work over an algebraically closed field of characteristic $0$, as in the
surrounding discussion.

<1>1. Hyperelliptic curves of genus $4$ are parametrized by unordered
configurations of $10$ distinct points of $\PP^1$, modulo $\PGL_2$.

::: {.proof}
A hyperelliptic genus-$4$ curve is a double cover
$$
f:X\longrightarrow\PP^1.
$$
Riemann--Hurwitz gives
$$
2g-2
=
2(-2)+\deg R_f,
$$
so for $g=4$ the branch divisor has degree
$$
2g+2=10.
$$
In characteristic $0$ these are $10$ distinct points.

Conversely, an unordered reduced divisor of degree $10$ on $\PP^1$
determines a double cover branched exactly there, unique up to isomorphism:
one takes the square root of the corresponding section of
$\OO_{\PP^1}(10)$, and scalar choices differ by a square over the
algebraically closed field.  Changing coordinates on $\PP^1$ changes the
cover only by isomorphism.  Hence the asserted parametrization.
:::

<1>2. The hyperelliptic genus-$4$ locus is irreducible of dimension
$$
\boxed{7}.
$$

::: {.proof}
The open configuration space of $10$ ordered distinct points of $\PP^1$ is
irreducible of dimension $10$.  Quotienting by the finite symmetric group
does not change dimension or irreducibility, so unordered branch divisors
also form an irreducible $10$-dimensional family.

The group
$$
\PGL_2
$$
has dimension $3$.  The stabilizer of a reduced set of at least three points
is finite, since an automorphism of $\PP^1$ fixing three points is the
identity.  Thus the orbit dimension is $3$, and the family of isomorphism
classes has dimension
$$
10-3=7.
$$
Its image is irreducible because the parameter space is irreducible.
:::

<1>3. A nonhyperelliptic genus-$4$ curve has canonical model
$$
\boxed{C=Q\cap F_3\subset\PP^3,}
$$
where $Q$ is its unique quadric, and the cubic $F_3$ is unique modulo
addition of $Q$ times a linear form.

::: {.proof}
This is the canonical genus-$4$ description recalled in (5.2.2).  The
canonical system embeds a nonhyperelliptic genus-$4$ curve as a degree-$6$
curve in $\PP^3$.  It lies on a unique quadric $Q$ and on a cubic not
divisible by $Q$.  Since
$$
\deg(Q\cap F_3)=2\cdot3=6=\deg C,
$$
the complete intersection is exactly $C$.

The degree-$3$ part of the ideal of a $(2,3)$ complete intersection is
$$
kF_3+Q\cdot H^0(\PP^3,\OO(1)).
$$
Thus replacing $F_3$ by
$$
cF_3+QL,
\qquad
c\in k^*,
\quad
L\in H^0(\PP^3,\OO(1)),
$$
does not change $C$, and these are precisely the redundancies.
:::

<1>4. Canonically embedded smooth $(2,3)$ complete intersections form an
irreducible parameter space of dimension
$$
\boxed{24}.
$$

::: {.proof}
Quadrics in $\PP^3$ form
$$
\PP H^0(\PP^3,\OO(2))
\cong
\PP^9,
$$
because
$$
h^0(\PP^3,\OO(2))=10.
$$
For a fixed nonzero quadric $Q$, the cubic is determined by a line in
$$
H^0(\PP^3,\OO(3))
\big/
QH^0(\PP^3,\OO(1)).
$$
The two vector-space dimensions are
$$
20
\qquad\text{and}\qquad
4,
$$
so this quotient has dimension $16$ and its projectivization is
$\PP^{15}$.

As $Q$ varies, these quotients form a rank-$16$ vector bundle over
$\PP^9$: multiplication by the tautological quadric gives an injective
bundle map
$$
\OO_{\PP^9}(-1)
\tensor H^0(\PP^3,\OO(1))
\longrightarrow
H^0(\PP^3,\OO(3))\tensor\OO_{\PP^9}.
$$
Its projectivized cokernel is therefore irreducible of dimension
$$
9+15=24.
$$
The condition that $Q\cap F_3$ be a smooth curve is open and nonempty, so
the smooth-complete-intersection locus is still irreducible of dimension
$24$.
:::

<1>5. Nonhyperelliptic genus-$4$ curves form an irreducible family of
dimension
$$
\boxed{9}.
$$

::: {.proof}
Two canonical models represent isomorphic curves exactly when they differ by
a projective coordinate change in $\PP^3$.  The group
$$
\PGL_4
$$
has dimension
$$
4^2-1=15.
$$
By [[P-AGH452AUTOMORPHISMGROUPFINITE|Exercise IV.5.2]], the stabilizer of a
smooth genus-$4$ canonical curve is finite.  Thus every orbit has dimension
$15$.

Step <1>4 gives an irreducible $24$-dimensional parameter space dominating
the nonhyperelliptic genus-$4$ family, so the latter is irreducible and has
dimension
$$
24-15=9.
$$
:::

<1>6. Let $C=Q\cap F_3$ be a nonhyperelliptic canonical genus-$4$ curve.
Its $g^1_3$'s are in bijection with the rulings of $Q$.

::: {.proof}
First, every ruling of $Q$ gives a $g^1_3$.  Indeed, a ruling line
$$
\ell\subset Q
$$
meets the cubic $F_3$ in a divisor of degree $3$ on $C$, and the
one-parameter family of ruling lines gives a base-point-free pencil of such
divisors.

Conversely, let $|D|$ be a $g^1_3$ on $C$.  Thus
$$
\deg D=3,
\qquad
\ell(D)=2.
$$
Riemann--Roch gives
$$
\ell(K-D)
=
\ell(D)-\deg D-1+g
=
2-3-1+4
=2.
$$
In the canonical embedding, hyperplanes containing $D$ therefore form a
pencil.  Their common intersection is a line
$$
\ell_D\subset\PP^3
$$
containing the degree-$3$ divisor $D$.

The restriction of the quadratic equation of $Q$ to $\ell_D$ has degree
$2$, but it vanishes on the length-$3$ divisor $D$.  Hence it vanishes
identically:
$$
\ell_D\subset Q.
$$
As $D$ varies in its pencil, these lines vary in a ruling of $Q$.
The ruling recovers $|D|$ by intersection with $C$, proving the bijection.
:::

<1>7. The curve $C$ has exactly two $g^1_3$'s when $Q$ is smooth and exactly
one when $Q$ has rank $3$.

::: {.proof}
A smooth quadric surface is
$$
Q\cong\PP^1\times\PP^1
$$
and has exactly two rulings.  Their induced pencils on $C$ are distinct:
if the two projection maps on $C$ differed only by an automorphism of
$\PP^1$, then the image of $C$ in
$\PP^1\times\PP^1$ would lie in the graph of that automorphism, a curve
of bidegree $(1,1)$, whereas
$$
C\sim(3,3).
$$
Thus step <1>6 gives exactly two $g^1_3$'s.

An irreducible singular quadric containing a nondegenerate smooth canonical
curve has rank $3$, hence is a quadric cone.  Such a cone has exactly one
ruling by lines, so step <1>6 gives exactly one $g^1_3$.
:::

<1>8. The rank-$3$ quadrics form an irreducible locally closed subset of
$\PP^9$ of dimension
$$
\boxed{8}.
$$

::: {.proof}
A quadric in $\PP^3$ is represented by a symmetric $4\times4$ matrix,
up to scalar.  Every rank-$3$ quadric is projectively equivalent to
$$
x_0^2+x_1^2+x_2^2=0.
$$
Hence the rank-$3$ locus is the image of the irreducible group
$\PGL_4$ acting on this quadric, and its closure is irreducible.

That closure is exactly the locus of quadrics of rank at most $3$: matrix
rank can only drop under specialization, and every lower-rank diagonal
quadric is a limit of rank-$3$ diagonal quadrics.  This locus is also the
zero set of the determinant, so it is a proper hypersurface in $\PP^9$ and
therefore has dimension $8$.

The locus of rank at most $2$ is a proper closed subset of this
hypersurface.  Therefore its complement, the rank-$3$ locus, is irreducible
and still has dimension $8$.
:::

<1>9. Nonhyperelliptic genus-$4$ curves having exactly one $g^1_3$ form an
irreducible family of dimension
$$
\boxed{8}.
$$

::: {.proof}
By step <1>7, this is precisely the locus whose unique canonical quadric has
rank $3$.  Restrict the parameter construction of step <1>4 to the
irreducible $8$-dimensional rank-$3$ quadric locus.  The cubic fibre remains
$\PP^{15}$, so the resulting parameter space has dimension
$$
8+15=23.
$$
The condition that the complete intersection be smooth is open and nonempty,
so the smooth locus is irreducible of the same dimension.

Again quotienting by projective coordinate changes removes
$$
\dim\PGL_4=15
$$
dimensions, and Exercise IV.5.2 gives finite stabilizers.  Hence the family
of isomorphism classes is irreducible of dimension
$$
23-15=8.
$$
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>2 proves the hyperelliptic assertion, step <1>5 proves the
nonhyperelliptic assertion, and step <1>9 proves the assertion about curves
with a unique $g^1_3$.
:::
:::
