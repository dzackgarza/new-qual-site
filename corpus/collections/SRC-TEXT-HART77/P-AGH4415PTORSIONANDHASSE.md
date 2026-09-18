---
schema: qual/card@1
id: P-AGH4415PTORSIONANDHASSE
kind: problem
title: The $p$-torsion subgroup is $\ZZ/p$ exactly when the Hasse invariant is $1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
  - Riemann-Hurwitz
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.15 together with Remark IV.4.10.7, the definition of
    the Hasse invariant preceding Proposition IV.4.21, and Exercise IV.4.7 on
    dual isogenies. Cross-checked the ordinary/supersingular p-torsion
    dichotomy against standard elliptic-curve references.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be an elliptic curve over a field $k$ of characteristic $p$.
Let $F': X_p \to X$ be the $k$-linear Frobenius morphism (2.4.1). Use (4.10.7) to show that the dual morphism $\hat{F}': X \to X_p$ is separable if and only if the Hasse invariant of $X$ is 1.

Now use (Ex.
4.7) to show that if the Hasse invariant is 1, then the subgroup of points of order $p$ on $X$ is isomorphic to $\ZZ/p$; if the Hasse invariant is 0, it is 0.
:::

::: {.solution}
Let
$$
F':X_p\longrightarrow X
$$
be the $k$-linear Frobenius morphism and let
$$
V=\widehat{F'}:X\longrightarrow X_p
$$
be its dual.

<1>1. Under the identifications of an elliptic curve with its Jacobian, the
map $V$ is the morphism of Jacobians induced by pullback along $F'$.

::: {.proof}
Exercise IV.4.7 defines the dual of a morphism
$$
f:Y\longrightarrow Z
$$
by the pullback homomorphism
$$
f^*:\Pic^0(Z)\longrightarrow\Pic^0(Y),
$$
after identifying each elliptic curve with its degree-zero Picard variety.
Applying this to $F'$ gives exactly the assertion.
:::

<1>2. The tangent map of $V$ at the origin identifies with
$$
(F')^*:
H^1(X,\OO_X)
\longrightarrow
H^1(X_p,\OO_{X_p}).
$$

::: {.proof}
Remark IV.4.10.7 identifies the Zariski tangent space at the origin of the
Jacobian of a curve $Y$ with
$$
T_0\Pic^0(Y)\cong H^1(Y,\OO_Y).
$$
This identification is functorial for pullback of line bundles. By step <1>1,
$V$ is precisely the pullback map on the two Jacobians, so its differential
at the origin is $(F')^*$ on $H^1(\OO)$.
:::

<1>3. The dual Frobenius $V$ is separable if and only if the Hasse invariant
of $X$ is $1$.

::: {.proof}
The map in step <1>2 is the $k$-linear form of the Frobenius action
$$
F^*:H^1(X,\OO_X)\longrightarrow H^1(X,\OO_X)
$$
used to define the Hasse invariant. Since $H^1(X,\OO_X)$ is
one-dimensional, the Hasse invariant is $1$ exactly when this map is
nonzero.

An isogeny between smooth curves is separable exactly when its differential
is nonzero. For a group homomorphism it suffices to test the differential at
the origin, because translations identify all tangent maps. Therefore, by
step <1>2,
$$
V\text{ is separable}
\iff
dV_0\ne0
\iff
F^*\ne0
\iff
\operatorname{Hasse}(X)=1.
$$
This proves the first assertion.
:::

<1>4. The Frobenius $F'$ has degree $p$, and Exercise IV.4.7 gives
$$
\boxed{
F'\circ V=[p]_X.
}
$$

::: {.proof}
The $k$-linear Frobenius is purely inseparable of degree $p$. Exercise
IV.4.7(c), applied to $F'$, says that composition with the dual is
multiplication by the degree, hence
$$
F'\circ\widehat{F'}=[p]_X.
$$
:::

<1>5. The geometric $p$-torsion points of $X$ are exactly the geometric
kernel points of $V$:
$$
\boxed{X[p](k)=\ker V(k).}
$$

::: {.proof}
The inclusion
$$
\ker V(k)\subseteq X[p](k)
$$
follows immediately from step <1>4.

Conversely, let $P\in X[p](k)$. Then step <1>4 gives
$$
F'(V(P))=[p](P)=0.
$$
The Frobenius $F'$ is radicial, so its geometric kernel has only the identity
point. Hence $V(P)=0$, proving the reverse inclusion.
:::

<1>6. If the Hasse invariant is $1$, then
$$
\boxed{X[p](k)\cong\ZZ/p\ZZ.}
$$

::: {.proof}
By step <1>3, $V$ is separable. Exercise IV.4.7(f) gives
$$
\deg V=\deg F'=p.
$$
For a separable isogeny, the number of geometric kernel points equals its
degree, so
$$
\#\ker V(k)=p.
$$
By step <1>5 this is $X[p](k)$. A group of prime order is cyclic, hence
$$
X[p](k)\cong\ZZ/p\ZZ.
$$
:::

<1>7. If the Hasse invariant is $0$, then
$$
\boxed{X[p](k)=0.}
$$

::: {.proof}
By step <1>3, $V$ is inseparable. Since $\deg V=p$ is prime, its inseparable
degree is $p$ and its separable degree is $1$. Thus its geometric kernel has
only the identity point. Step <1>5 now gives
$$
X[p](k)=\ker V(k)=\{0\}.
$$
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>3 proves the separability criterion, while steps <1>6--<1>7 give the
two possible groups of $p$-torsion points.
:::
:::
