---
schema: qual/card@1
id: P-AGH2215VARTOSCH
kind: problem
title: Varieties over an algebraically closed field embed fully faithfully into schemes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Varieties
  - Schemes
  - Residue Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.15 statement and source-order placement after II.2.14.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
a. Let $V$ be a variety over the algebraically closed field $k$.
Show that a point $P \in t(V)$ is a closed point if and only if its residue field is $k$.

b. If $f: X \to Y$ is a morphism of schemes over $k$ and $P \in X$ is a point with residue field $k$, then $f(P) \in Y$ also has residue field $k$.

c. Now show that if $V, W$ are any two varieties over $k$, then the natural map
\[
\Hom_{\mathsf{Var}_k}(V, W) \to \Hom_{\Sch_k}\qty{t(V), t(W)}
\]
is bijective.
Injectivity follows because a morphism of varieties over $k$ is determined by its action on closed points; surjectivity requires the residue-field preservation established in parts (a) and (b).
:::

::: {.solution}
<1>1. A point of $t(V)$ corresponds to an irreducible closed subvariety
\[
Z\subseteq V,
\]
and its residue field is the function field
\[
\boxed{
\kappa(\eta_Z)=k(Z).
}
\]
::: {.proof}
Choose an affine open subset
\[
U=\operatorname{Spec}A
\]
of the associated scheme meeting the point $\eta_Z$.  In the classical variety, this corresponds to an affine open subset of $V$, and
\[
Z\cap U
\]
is defined by a prime ideal
\[
\mathfrak p\subseteq A.
\]
The point $\eta_Z$ is the prime $\mathfrak p$.  Its residue field is
\[
\kappa(\mathfrak p)
=\operatorname{Frac}(A/\mathfrak p),
\]
which is precisely the rational function field of the irreducible variety $Z$.
:::

<1>2. If $P\in t(V)$ is a closed point, then
\[
\boxed{\kappa(P)=k.}
\]
::: {.proof}
A closed point of $t(V)$ corresponds to an ordinary closed point
\[
p\in V.
\]
Choose an affine neighborhood with coordinate ring $A$.  The point is a maximal ideal
\[
\mathfrak m\subseteq A.
\]
Since $A$ is a finitely generated $k$-algebra and $k$ is algebraically closed, the weak Nullstellensatz gives
\[
A/\mathfrak m\cong k.
\]
This quotient is the residue field at the closed point.
:::

<1>3. Conversely, if
\[
P\in t(V)
\]
has residue field $k$, then $P$ is closed.
::: {.proof}
Let $Z$ be the irreducible closed subvariety whose generic point is $P$.  By <1>1,
\[
k(Z)=\kappa(P)=k.
\]
The transcendence degree of the function field of an irreducible variety equals its dimension, so
\[
\dim Z
=\operatorname{trdeg}_k k(Z)
=0.
\]

An irreducible zero-dimensional variety over an algebraically closed field is a single closed point.  Therefore
\[
Z=\{P\},
\]
so $P$ is closed in $t(V)$.
:::

<1>4. Hence
\[
\boxed{
P\in t(V)\text{ is closed}
\iff
\kappa(P)=k.
}
\]
::: {.proof}
Combine <1>2 and <1>3.
:::

<1>5. Let
\[
f:X\longrightarrow Y
\]
be a morphism of schemes over $k$, and let $P\in X$ satisfy
\[
\kappa(P)=k.
\]
Then
\[
\boxed{\kappa(f(P))=k.}
\]
::: {.proof}
Put
\[
Q=f(P).
\]
The local homomorphism
\[
f_P^\sharp:
\mathcal O_{Y,Q}
\longrightarrow
\mathcal O_{X,P}
\]
induces an injective homomorphism of residue fields
\[
\kappa(Q)
\hookrightarrow
\kappa(P)=k.
\]
Because $f$ is a morphism over $k$, the composite
\[
k
\longrightarrow
\kappa(Q)
\longrightarrow
k
\]
is the identity.  Thus the image of $\kappa(Q)$ inside $k$ contains the image of $k$, which is all of $k$.  Since it is also a subfield of $k$, the image is exactly $k$.

The injection is therefore a $k$-algebra isomorphism
\[
\kappa(Q)\cong k.
\]
:::

<1>6. Let
\[
F:t(V)\longrightarrow t(W)
\]
be a morphism of schemes over $k$.  Then $F$ sends closed points to closed points and therefore determines a set map
\[
\boxed{
f:V\longrightarrow W.
}
\]
::: {.proof}
By <1>4, the closed points of $t(V)$ are exactly the points with residue field $k$.  By <1>5, $F$ sends each such point to a point of $t(W)$ whose residue field is $k$, which by <1>4 is closed.

The closed points of $t(V)$ and $t(W)$ identify respectively with the ordinary points of the classical varieties $V$ and $W$.  Restricting the underlying map of $F$ to those closed points gives the stated set map $f$.
:::

<1>7. The map $f:V\to W$ is continuous in the Zariski topology.
::: {.proof}
The classical variety $V$ identifies with the subspace of closed points of $t(V)$, and similarly for $W$.  Let
\[
C\subseteq W
\]
be closed.  The corresponding subset
\[
t(C)\subseteq t(W)
\]
is closed, and its closed points are exactly $C$.

Since $F$ is continuous,
\[
F^{-1}(t(C))
\]
is closed in $t(V)$.  Intersecting with the closed-point subspace $V$ gives
\[
f^{-1}(C),
\]
which is therefore closed in $V$.  Hence $f$ is continuous.
:::

<1>8. Fix $P\in V$.  There are affine open neighborhoods
\[
P\in V_0\subseteq V,
\qquad
f(P)\in W_0\subseteq W,
\]
such that
\[
f(V_0)\subseteq W_0.
\]
::: {.proof}
Choose an affine open neighborhood
\[
W_0\subseteq W
\]
of $f(P)$.  The corresponding open subscheme
\[
t(W_0)\subseteq t(W)
\]
has open inverse image
\[
F^{-1}(t(W_0))
\subseteq t(V).
\]
Its closed points form the open subset
\[
f^{-1}(W_0)\subseteq V,
\]
which contains $P$.

Affine opens form a basis for a variety, so choose an affine open
\[
P\in V_0\subseteq f^{-1}(W_0).
\]
Then
\[
f(V_0)\subseteq W_0.
\]
:::

<1>9. Write
\[
V_0=\operatorname{Spec}_{\mathrm{var}}A,
\qquad
W_0=\operatorname{Spec}_{\mathrm{var}}B
\]
for their affine coordinate rings.  The restriction
\[
F|_{t(V_0)}:
t(V_0)=\operatorname{Spec}A
\longrightarrow
t(W_0)=\operatorname{Spec}B
\]
is induced by a $k$-algebra homomorphism
\[
\varphi:B\longrightarrow A.
\]
::: {.proof}
By <1>8, the scheme morphism $F$ maps the open subscheme $t(V_0)$ into $t(W_0)$.  Both are affine schemes associated to the affine varieties.  The affine anti-equivalence therefore identifies the restricted morphism with a unique ring homomorphism
\[
B\to A.
\]
Because $F$ is a morphism over $k$, this homomorphism is a $k$-algebra homomorphism.
:::

<1>10. The $k$-algebra map $\varphi:B\to A$ defines a morphism of affine varieties
\[
f_0:V_0\longrightarrow W_0,
\]
and on closed points
\[
f_0=f|_{V_0}.
\]
::: {.proof}
The classical affine-coordinate correspondence sends a $k$-algebra homomorphism
\[
B\to A
\]
to a morphism of affine varieties
\[
\operatorname{Spec}_{\mathrm{var}}A
\to
\operatorname{Spec}_{\mathrm{var}}B.
\]

The associated scheme morphism is exactly the affine scheme morphism induced by the same ring map, namely
\[
F|_{t(V_0)}.
\]
Hence their maps on closed points agree.  By definition of $f$ in <1>6, this says
\[
f_0=f|_{V_0}.
\]
:::

<1>11. The set map $f:V\to W$ is a morphism of varieties.
::: {.proof}
Every point $P\in V$ has an affine neighborhood $V_0$ on which <1>10 identifies $f$ with a morphism of affine varieties.  Regularity of a map of varieties is local on the source and target.  Therefore $f$ is a morphism globally.
:::

<1>12. The associated scheme morphism
\[
t(f):t(V)\longrightarrow t(W)
\]
is the original morphism $F$.
::: {.proof}
On each affine neighborhood $V_0$ from <1>8, both
\[
t(f)|_{t(V_0)}
\quad\text{and}\quad
F|_{t(V_0)}
\]
are the affine scheme morphism induced by the same ring homomorphism
\[
\varphi:B\to A
\]
from <1>9.  Thus they agree on an open cover of $t(V)$, hence agree globally.
:::

<1>13. Therefore the natural map
\[
\operatorname{Hom}_{\mathsf{Var}_k}(V,W)
\longrightarrow
\operatorname{Hom}_{\mathsf{Sch}_k}(t(V),t(W))
\]
is surjective.
::: {.proof}
Given any scheme morphism $F$, steps <1>6--<1>12 construct a variety morphism $f$ satisfying
\[
t(f)=F.
\]
:::

<1>14. The same natural map is injective.
::: {.proof}
If
\[
t(f)=t(g),
\]
then the two associated scheme morphisms have the same map on closed points.  Under the identification of the closed points of $t(V)$ and $t(W)$ with the ordinary points of $V$ and $W$, this means
\[
f(P)=g(P)
\]
for every $P\in V$.

A morphism of varieties is in particular a function on the underlying point sets, so equality pointwise gives
\[
f=g.
\]
:::

<1>15. Hence the functor
\[
t:\mathsf{Var}_k\longrightarrow\mathsf{Sch}_k
\]
is fully faithful:
\[
\boxed{
\operatorname{Hom}_{\mathsf{Var}_k}(V,W)
\xrightarrow{\sim}
\operatorname{Hom}_{\mathsf{Sch}_k}(t(V),t(W)).
}
\]
::: {.proof}
Surjectivity is <1>13 and injectivity is <1>14.
:::

<1>16. Q.E.D.
::: {.proof}
Steps <1>1--<1>4 prove part (a), <1>5 proves part (b), and <1>6--<1>15 prove part (c).
:::
:::
