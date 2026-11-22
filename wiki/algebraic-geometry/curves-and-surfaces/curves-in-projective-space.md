---
title: Curves in projective space
order: 7
topics:
- Space Curves
- Projection
- Quadric Surface
---

# Curves in projective space

A curve in $\PP^n$ is studied through three numbers — its degree, its genus, and the dimension of its linear span — together with the projection that lowers $n$ without changing the curve.
The degree of an embedding is the degree of the divisor that defines it, and the two inequalities of Riemann--Roch decide when a divisor of a given degree is base-point free or very ample ([[PR-CRVDEGBD]]).
Once the curve is in $\PP^3$ two theorems take over: Castelnuovo's bound limits the genus of a nondegenerate space curve by its degree, and the intersection theory of a quadric surface describes the curves that attain it ([[T-CRVCAST]], [[FE-CRVQUAD]]).

## Degrees that embed

[[PR-CRVDEGBD]]

On a smooth projective curve a divisor is ample exactly when its degree is positive, $\linearsystem{D}$ is base-point free when $\deg D\ge2g$, and $D$ is very ample when $\deg D\ge2g+1$ ([[PR-CRVDEGBD]]).
Both bounds are sufficient and not necessary: the canonical divisor of a smooth plane quartic has degree $4<2g+1=7$ and is very ample, because its complete linear system is the plane embedding [@Har77, Proposition IV.5.2].
An elliptic curve is very ample in degree at least $3$, where degree $3$ gives the plane cubic, and a curve of genus $2$ embeds in $\PP^3$ by any divisor of degree at least $5$ ([[PR-CRVDEGBD]]).
If $\varphi$ is the embedding attached to $D$, then $\deg\varphi(C)=\deg D$, so the degree of a projective curve is the degree of the divisor that produced the embedding ([[PR-CRVDEGBD]]).

## Rational normal curves

[[FE-VARVERONESE]]

The $d$-uple embedding of $\PP^1$ is a curve of degree $d$ in $\PP^d$, the rational normal curve of degree $d$, and it spans its projective space, since the monomials of degree $d$ span the whole of $H^0(\PP^1,\OO(d))$ [@Har77, Exercise IV.3.4] ([[FE-VARVERONESE]]).
The converse is what makes the notion useful: a curve of degree $d$ in $\PP^n$ with $d\le n$ that is not contained in any hyperplane has $d=n$, genus $0$, and is the rational normal curve up to a projectivity of $\PP^n$ [@Har77, Exercise IV.3.4].
So among curves of degree $d$ spanning $\PP^d$ there is exactly one, and it is the one of minimal genus.

## Projection

[[T-CRVEMBP3]]

Every smooth projective curve embeds in $\PP^3$: start from a very ample divisor of degree at least $2g+1$, then project from a point outside the curve, which is possible because secant lines sweep a subvariety of dimension at most $3$ and tangent lines one of dimension at most $2$, so successive projections preserve the embedding until the ambient space is $\PP^3$ ([[T-CRVEMBP3]]).
Projection from a point $O\notin C\subseteq\PP^N$ is a closed immersion exactly when $O$ lies on no secant line through two distinct points of $C$ and on no embedded tangent line, which is the geometric reading of the very-ampleness criterion ([[T-CRVEMBP3]], [[T-D8TUX]]).

One further projection, to $\PP^2$, cannot keep the curve smooth, and over a field of characteristic zero a general centre produces a plane model whose only singularities are ordinary nodes.
The genus is then recoverable from the node count: a plane curve of degree $d$ with $r$ nodes and no worse singularity has normalization of genus $\binom{d-1}{2}-r$ ([[T-CRVEMBP3]], [[D-CRVPLSING]]).
This is the classical trade of a space curve for a plane model with controlled singularities, and it is what makes the Severi varieties — the loci of plane curves of degree $d$ with a prescribed number of nodes — the standard parameter space for curves of a given degree and genus.

## Plane curve singularities

[[D-CRVPLSING]]

At a singular point $p$ of a curve $C$ with normalization $\nu\colon\tilde C\to C$, the invariant $\delta_p=\dim_k(\nu_*\OO_{\tilde C}/\OO_C)_p$ measures how much the local ring fails to be a discrete valuation ring, and the genus drops by exactly the sum of the $\delta_p$: $p_a(C)-g(\tilde C)=\sum_p\delta_p$ ([[D-CRVPLSING]]).
The standard local models are the node $\delta_p=1$ with two branches, the cusp $\delta_p=1$ with one branch, and the tacnode $\delta_p=2$; an ordinary point of multiplicity $r$ has $\delta_p=\binom{r}{2}$ ([[D-CRVPLSING]]).
For a plane curve of degree $d$ the genus formula becomes $g=\binom{d-1}{2}-\sum_p\delta_p$, which is why the node count of a plane model determines the genus it came from ([[D-CRVPLSING]]).

## Curves on a quadric

[[FE-CRVQUAD]]

A smooth quadric $Q\subseteq\PP^3$ is isomorphic to $\PP^1\times\PP^1$ by the Segre map, so $\Pic Q\cong\ZZ^2$ with generators the two ruling classes $A,B$ satisfying $A^2=B^2=0$ and $A\cdot B=1$ ([[FE-CRVQUAD]]).
A curve of type $(a,b)$ then has $\deg C=a+b$ and arithmetic genus $p_a(C)=(a-1)(b-1)$ [@Har77, Exercise III.5.6] ([[FE-CRVQUAD]]).
The canonical class of the quadric is $K_Q=(-2,-2)$, and adjunction reproduces the same genus identity $2p_a-2=C\cdot(C+K_Q)$; the curves of low type are the two rulings $(1,0)$ and $(0,1)$ and the conics $(1,1)$ ([[FE-CRVQUAD]]).
The description is a description of the split quadric: over an arbitrary field a smooth quadric need not be isomorphic to $\PP^1\times\PP^1$, and the real quadric $x_0^2+x_1^2+x_2^2+x_3^2=0$ has no real point at all ([[FE-CRVQUAD]]).

## Castelnuovo's bound

[[T-CRVCAST]]

For a smooth connected curve of degree $d$ and genus $g$ in $\PP^3$ that is not contained in a plane, $d\ge3$ and
$$
g\le\left\lfloor\frac{(d-2)^2}{4}\right\rfloor ,
$$
equivalently $\tfrac14d^2-d+1$ for even $d$ and $\tfrac14(d^2-1)-d+1$ for odd $d$ [@Har77, Theorem IV.6.4] ([[T-CRVCAST]]).
The bound is attained for every $d\ge3$, and a curve attaining it lies on a quadric surface: a curve of type $(a,a)$ on $\PP^1\times\PP^1$ has $d=2a$ and $g=(a-1)^2$, and one of type $(a,a+1)$ has $d=2a+1$ and $g=a(a-1)$, which are exactly the two formulas ([[T-CRVCAST]], [[FE-CRVQUAD]]).
Nonplanarity cannot be dropped, since a smooth plane curve of degree $d$ has genus $\binom{d-1}{2}$, which exceeds the bound for $d\ge3$ ([[T-CRVCAST]]).

## Which degrees and genera occur

[[FE-CRVDEGS]]

In degree at most $6$ the possibilities are small and can be listed: degree $1$ is a line, degree $2$ a plane conic, degree $3$ either a plane cubic of genus $1$ or the twisted cubic of genus $0$, degree $4$ a plane quartic of genus $3$, a rational quartic, or an elliptic quartic cut by two quadrics, and degree $5$ or $6$ adds the plane curves of genus $6$ and $10$ together with nonspecial curves of smaller genus ([[FE-CRVDEGS]]).
The general statement behind the list is that for $g\ge2$ a curve of genus $g$ has a nonspecial very ample divisor of degree $d$ exactly when $d\ge g+3$, and the corresponding embedding lands in $\PP^3$; if the hyperplane section is special and $C$ is not planar, then $d\ge6$ and $g\ge\tfrac12d+1$, the only such curve with $d=6$ being the canonical curve of genus $4$ ([[FE-CRVDEGS]]).
Degree $7$ and genus $5$ is the first case where the construction is not a complete intersection: $|K-P|$ has degree $7$ and $h^0=4$, and it is very ample whenever $h^0(P+Q+R)=1$ for all $Q,R$, which holds for a curve of genus $5$ with no $g^1_3$ ([[FE-CRVDEGS]]).

## Dual curves

[[D-CRVDUAL]]

For an irreducible plane curve $C$ over an algebraically closed field of characteristic zero, the tangent lines at smooth points sweep out the dual curve $C^\vee\subseteq(\PP^2)^\vee$, and the degree of $C^\vee$ is the class of $C$, the number of tangent lines through a general point of the plane [@Har77, Exercise IV.2.3] ([[D-CRVDUAL]]).
For a smooth curve of degree $d\ge2$ the Gauss map $C\to C^\vee$ has degree $d(d-1)$, so a smooth conic is self-dual and a smooth cubic has dual of degree $6$ whose nine cusps are the nine flexes of the cubic ([[D-CRVDUAL]]).
With nodes and cusps the count is Plücker's: if the only singularities of $C$ are $\delta$ nodes and $\kappa$ ordinary cusps, then $\deg C^\vee=d(d-1)-2\delta-3\kappa$, and biduality says $(C^\vee)^\vee=C$ ([[D-CRVDUAL]]).
