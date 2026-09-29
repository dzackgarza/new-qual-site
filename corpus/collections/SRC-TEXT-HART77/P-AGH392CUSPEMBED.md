---
schema: qual/card@1
id: P-AGH392CUSPEMBED
kind: problem
title: An embedded point at the cusp of a plane cubic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Flat Families
  - Embedded Points
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise III.9.2, Example III.9.8.4, and the twisted-cubic projection of I.3.14. The proof works on the affine chart at the cusp, eliminates the parameter for the scaled twisted cubic, proves the resulting family is flat by identifying its coordinate ring with the torsion-free k[a]-subalgebra k[a,t^2,t^3,at], and identifies the special-fibre maximal ideal as an embedded associated prime.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Do the calculation of (9.8.4) for the curve of (I, Ex.
3.14). Show that you get an embedded point at the cusp of the plane cubic curve.
:::

::: {.solution}
In I.3.14 the twisted cubic is parametrized in homogeneous coordinates by
$$
[t:u]\longmapsto[t^3:t^2u:tu^2:u^3]
$$
in $\PP^3$, and projection from $[0:0:1:0]$ forgets the third coordinate.
On the affine chart $u=1$ around the point mapping to the cusp, write the ambient coordinates as $(x,y,z)$.

::: pf

::: {.pf-step #s1}

The projected plane curve is the cuspidal cubic
$$
\boxed{x^2=y^3}.
$$

::: pf-proof

On $u=1$ the twisted cubic has parametrization
$$
x=t^3,\qquad y=t^2,\qquad z=t.
$$
Projection forgets $z$, so the image in the $(x,y)$-plane satisfies
$$
x^2=t^6=y^3.
$$
Conversely the map $t\mapsto(t^3,t^2)$ has dense image in the irreducible plane curve $x^2-y^3=0$.
Thus the projected curve is the cusp
$$
C=V(x^2-y^3),
$$
with cusp at the origin.

:::

:::

::: {.pf-step #s2}

For $a\ne0$, scale the omitted coordinate as in III.9.8.3. The resulting affine curve $X_a\subseteq\AA^3$ is parametrized by
$$
x=t^3,\qquad y=t^2,\qquad z=at.
$$

::: pf-proof

The automorphism used in III.9.8.3 multiplies the coordinate in the projection direction by $a$ and fixes the other coordinates.
Hence the affine parametrization of the twisted cubic becomes exactly the displayed one.
For $a\ne0$ this is isomorphic to the original twisted cubic by rescaling $z$.

:::

:::

::: {.pf-step #s3}

The flat closure of these curves over $\AA_a^1$ is cut out in $\AA^1_a\times\AA^3_{x,y,z}$ by
$$
\boxed{
J=(x^2-y^3,\ z^2-a^2y,\ yz-ax,\ xz-ay^2)}.
$$

::: pf-proof

Consider the $k$-algebra homomorphism
$$
\Phi:k[a,x,y,z]\longrightarrow k[a,t]
$$
defined by
$$
a\mapsto a,\qquad
x\mapsto t^3,\qquad
y\mapsto t^2,\qquad
z\mapsto at.
$$
Every generator of $J$ maps to zero, so
$$
J\subseteq\ker\Phi.
$$

Modulo $J$, use the relations
$$
x^2=y^3,\qquad
z^2=a^2y,\qquad
yz=ax,\qquad
xz=ay^2
$$
to reduce every monomial to a $k[a]$-linear combination of
$$
y^j,\qquad xy^j\quad(j\ge0),\qquad z.
$$
Their images under $\Phi$ are respectively
$$
t^{2j},\qquad t^{2j+3},\qquad at.
$$
These are $k[a]$-linearly independent: they have distinct powers of $t$, and a relation involving $at$ would have coefficient $c(a)a=0$ in the domain $k[a]$, hence $c(a)=0$.
Thus the induced map
$$
k[a,x,y,z]/J\longrightarrow k[a,t]
$$
is injective.
Consequently
$$
J=\ker\Phi,
$$
and the quotient identifies with the subalgebra
$$
B=k[a,t^2,t^3,at]\subseteq k[a,t].
$$

For $a\ne0$, adjoining $a^{-1}$ makes $t=z/a$ available, so the fibre is exactly the scaled twisted cubic of step [](#s2){.pf-ref}.
Hence $J$ is the scheme-theoretic closure of the family over $a\ne0$.

:::

:::

::: {.pf-step #s4}

The family
$$
\mathcal X=\Spec B\longrightarrow\AA_a^1
$$
is flat.

::: pf-proof

The ring $B$ is a subring of the domain $k[a,t]$ containing $k[a]$.
Hence $B$ is torsion-free as a $k[a]$-module.
The ring $k[a]$ is a principal ideal domain, and every torsion-free module over a principal ideal domain is flat.
Therefore $B$ is flat over $k[a]$.

Thus the closed family defined by $J$ is the flat extension prescribed in III.9.8.3--9.8.4.

:::

:::

::: {.pf-step #s5}

The special fibre at $a=0$ has ideal
$$
\boxed{
J_0=(x^2-y^3,\ z^2,\ yz,\ xz)\subseteq k[x,y,z]}.
$$

::: pf-proof

The special fibre is obtained by tensoring with $k[a]/(a)$, equivalently by adding $a$ to the total ideal and then setting $a=0$.
The four generators of $J$ become
$$
x^2-y^3,\qquad z^2,\qquad yz,\qquad xz,
$$
which gives the displayed ideal.

:::

:::

::: {.pf-step #s6}

The support of the special fibre is the cuspidal cubic in the plane $z=0$.

::: pf-proof

The radical of $J_0$ is
$$
\sqrt{J_0}=(z,x^2-y^3).
$$
Indeed, $z^2\in J_0$ forces $z$ into the radical, and after quotienting by $z$ the remaining reduced equation is the irreducible cusp equation $x^2-y^3$.
Therefore
$$
|X_0|=V(z,x^2-y^3),
$$
which is exactly the projected cuspidal cubic of step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s7}

The special fibre has an embedded associated point at the cusp $(0,0,0)$.

::: pf-proof

Let
$$
A_0=k[x,y,z]/J_0
$$
and denote residue classes by the same letters.
The element $z\in A_0$ is nonzero.
Indeed, the normal form of step [](#s3){.pf-ref} makes the class of $z$ a $k[a]$-basis element independent from the classes $y^j,xy^j$.
If $z$ belonged to $aB$, comparison of the coefficient of that basis element would give $1\in a,k[a]$, which is impossible.
Thus its image in $B/aB=A_0$ is nonzero.
The special-fibre relations give
$$
xz=yz=z^2=0.
$$
Thus the maximal ideal
$$
\mathfrak m=(x,y,z)
$$
annihilates $z$.
Every element outside $\mathfrak m$ has the form $c+h$ with $c\in k^\times$ and $h\in\mathfrak m$.
Since $\mathfrak m z=0$, such an element sends $z$ to $cz\ne0$.
Therefore
$$
\operatorname{Ann}_{A_0}(z)=\mathfrak m.
$$
Hence $\mathfrak m$ is an associated prime of $A_0$.

The unique minimal prime is
$$
\mathfrak p=(z,x^2-y^3),
$$
and
$$
\mathfrak p\subsetneq\mathfrak m.
$$
Therefore $\mathfrak m$ is an embedded associated prime.
Its closed point is precisely the cusp at the origin.
So the special fibre is the cuspidal cubic together with an embedded point at its cusp.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} construct the flat degeneration, steps [](#s5){.pf-ref} and [](#s6){.pf-ref} identify its special-fibre support with the cuspidal cubic, and step [](#s7){.pf-ref} proves that the cusp is an embedded associated point.

:::

:::

:::
