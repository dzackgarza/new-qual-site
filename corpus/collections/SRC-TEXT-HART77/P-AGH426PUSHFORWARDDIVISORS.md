---
schema: qual/card@1
id: P-AGH426PUSHFORWARDDIVISORS
kind: problem
title: The pushforward $f_*$ on divisors and the determinant of $f_* \mcl(D)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Canonical Divisor
  - Jacobians
relations: []
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.2.6. Part (a) is proved by successive elementary
    modifications at points, avoiding an identification of f_*O_D with a
    single structure sheaf when several points lie over the same point. Parts
    (c)--(d) use finite duality, the projection formula, and the ramification
    line-bundle formula.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
review: draft
---

::: {.problem}
Let $f: X \to Y$ be a finite morphism of curves of degree $n$.
We define a homomorphism $f_*: \Div X \to \Div Y$ by $f_*(\sum n_i P_i)=\sum n_i f(P_i)$ for any divisor $D=\sum n_i P_i$ on $X$.

a. For any locally free sheaf $\mce$ on $Y$, of rank $r$, we define $\det \mce=\wedge^r \mce \in \Pic Y$ (II, Ex.
6.11). In particular, for any invertible sheaf $\mcm$ on $X$, $f_* \mcm$ is locally free of rank $n$ on $Y$, so we can consider $\det f_* \mcm \in \Pic Y$.
Show that for any divisor $D$ on $X$,
$$
\det\left(f_* \mcl(D)\right) \cong \det f_*(\OO_X) \tensor \mcl(f_* D).
$$
Note in particular that $\det(f_* \mcl(D)) \neq \mcl(f_* D)$ in general!
Hint: First consider an effective divisor $D$, apply $f_*$ to the exact sequence $0 \to \mcl(-D) \to \OO_X \to \OO_D \to 0$, and use (II, Ex.
6.11).

b. Conclude that $f_* D$ depends only on the linear equivalence class of $D$, so there is an induced homomorphism $f_*: \Pic X \to \Pic Y$.
Show that $f_* f^*: \Pic Y \to \Pic Y$ is just multiplication by $n$.

c. Use duality for a finite flat morphism (III, Ex.
6.10) and (III, Ex.
7.2) to show that $$\det f_* \Omega_X \cong \qty{ \det f_* \OO_X}^{-1} \tensor \Omega_Y^{\tensor n}.$$

d. Now assume that $f$ is separable, so we have the ramification divisor $R$.
We define the **branch divisor** $B$ to be the divisor $f_* R$ on $Y$.
Show that $$\left(\det f_* \OO_X\right)^2 \cong \mcl(-B).$$
:::

::: {.solution}
Write
$$
E=f_*\OO_X.
$$
Since $f$ is a finite morphism between nonsingular curves, it is flat; hence
$E$ is locally free of rank $n$.  More generally, $f_*\mcm$ is locally free
of rank $n$ for every invertible sheaf $\mcm$ on $X$.

<1>1. Let $Q\in Y$.  If
$$
0\longrightarrow E_0\longrightarrow E_1\longrightarrow k(Q)
\longrightarrow0
$$
is exact with $E_0,E_1$ locally free of the same rank, then
$$
\det E_1
\cong
\det E_0\tensor\mcl(Q).
$$

::: {.proof}
Away from $Q$ the two bundles are equal.  At $Q$, let
$$
A=\OO_{Y,Q}
$$
with uniformizer $t$.  After choosing bases, $E_{0,Q}\subset E_{1,Q}$ are
free $A$-lattices of the same rank and the quotient has length one.  The
elementary divisor theorem over the DVR $A$ gives bases in which
$$
E_{1,Q}=A^r,
\qquad
E_{0,Q}=tA\oplus A^{r-1}.
$$
Thus the determinant lattice of $E_1$ is obtained from that of $E_0$ by
multiplying by $t^{-1}$.  This is exactly the local modification defining
$\mcl(Q)$, so
$$
\det E_1\cong\det E_0\tensor\mcl(Q).
$$
:::

<1>2. For every divisor $D$ on $X$ and every closed point $P\in X$,
$$
\det f_*\mcl(D+P)
\cong
\det f_*\mcl(D)\tensor\mcl(f(P)).
$$

::: {.proof}
There is a short exact sequence
$$
0
\longrightarrow
\mcl(D)
\longrightarrow
\mcl(D+P)
\longrightarrow
k(P)
\longrightarrow0.
$$
Because $f$ is finite, $f_*$ is exact on quasicoherent sheaves.  Since the
ground field for the curves is algebraically closed,
$$
f_*k(P)=k(f(P))
$$
as a skyscraper sheaf.  Applying $f_*$ therefore gives
$$
0
\longrightarrow
f_*\mcl(D)
\longrightarrow
f_*\mcl(D+P)
\longrightarrow
k(f(P))
\longrightarrow0.
$$
Step <1>1 gives the claimed determinant relation.
:::

<1>3. For every divisor $D$ on $X$,
$$
\boxed{
\det\left(f_*\mcl(D)\right)
\cong
\det(f_*\OO_X)\tensor\mcl(f_*D).
}
$$

::: {.proof}
Starting with $D=0$, add the points occurring in the positive part of $D$
one at a time and apply step <1>2.  To subtract a point, apply step <1>2 to
$D-P$:
$$
\det f_*\mcl(D-P)
\cong
\det f_*\mcl(D)\tensor\mcl(-f(P)).
$$
Iterating over all coefficients of
$$
D=\sum_P n_P P
$$
gives
$$
\det f_*\mcl(D)
\cong
\det E
\tensor
\mcl\left(\sum_Pn_Pf(P)\right),
$$
which is exactly the formula in part (a).
:::

<1>4. If $D\sim D'$ on $X$, then
$$
f_*D\sim f_*D'
$$
on $Y$.  Hence $f_*$ descends to a homomorphism
$$
f_*:\Pic X\longrightarrow\Pic Y.
$$

::: {.proof}
Linear equivalence $D\sim D'$ is equivalent to
$$
\mcl(D)\cong\mcl(D').
$$
Applying $f_*$ preserves this isomorphism, so their determinants are
isomorphic.  Step <1>3 gives
$$
\det E\tensor\mcl(f_*D)
\cong
\det E\tensor\mcl(f_*D').
$$
Cancelling $\det E$ yields
$$
\mcl(f_*D)\cong\mcl(f_*D'),
$$
which is the desired linear equivalence.  Since the divisor pushforward is
additive, the induced map on divisor classes is a group homomorphism.
:::

<1>5. The composite
$$
f_*f^*:\Pic Y\longrightarrow\Pic Y
$$
is multiplication by $n$.

::: {.proof}
It is enough to check a closed point $Q\in Y$.  The pullback divisor is
$$
f^*Q
=
\sum_{P\mapsto Q}e_P P.
$$
Therefore
$$
f_*f^*Q
=
\left(\sum_{P\mapsto Q}e_P\right)Q.
$$
For a finite morphism of degree $n$ between curves over an algebraically
closed field, the degree of every fibre counted with multiplicity is $n$:
$$
\sum_{P\mapsto Q}e_P=n.
$$
Thus
$$
f_*f^*Q=nQ.
$$
By additivity this holds for every divisor and hence every divisor class.
Equivalently, on line bundles the composite sends $\mcm$ to
$\mcm^{\tensor n}$.
:::

<1>6. Finite duality gives an isomorphism
$$
f_*\Omega_X
\cong
\mathcal Hom_Y(E,\Omega_Y)
\cong
E^\vee\tensor\Omega_Y.
$$

::: {.proof}
By [[P-AGH3610FINITEFLATDUAL|Exercise III.6.10]] and
[[P-AGH372FINITEDUAL|Exercise III.7.2]], finite duality identifies the
pushforward of the dualizing sheaf of $X$ with the dual of $f_*\OO_X$
relative to the dualizing sheaf of $Y$:
$$
f_*\omega_X
\cong
\mathcal Hom_Y(f_*\OO_X,\omega_Y).
$$
On a nonsingular curve the dualizing sheaf is the sheaf of differentials, so
$$
\omega_X\cong\Omega_X,
\qquad
\omega_Y\cong\Omega_Y.
$$
Because $E$ is locally free,
$$
\mathcal Hom_Y(E,\Omega_Y)
\cong
E^\vee\tensor\Omega_Y,
$$
which proves the displayed formula.
:::

<1>7. One has
$$
\boxed{
\det f_*\Omega_X
\cong
(\det f_*\OO_X)^{-1}\tensor\Omega_Y^{\tensor n}.
}
$$

::: {.proof}
Take determinants in step <1>6.  Since $E$ has rank $n$,
$$
\det(E^\vee\tensor\Omega_Y)
\cong
\det(E^\vee)\tensor\Omega_Y^{\tensor n}.
$$
Also
$$
\det(E^\vee)\cong(\det E)^{-1}.
$$
Substituting $E=f_*\OO_X$ gives exactly the formula in part (c).
:::

<1>8. Assume now that $f$ is separable, with ramification divisor $R$ and
branch divisor
$$
B=f_*R.
$$
Then
$$
\Omega_X
\cong
f^*\Omega_Y\tensor\mcl(R).
$$

::: {.proof}
For a finite separable morphism of nonsingular curves, the differential
$$
f^*\Omega_Y\longrightarrow\Omega_X
$$
is a nonzero map of line bundles.  Its divisor of zeros is the ramification
divisor $R$.  A nonzero map of line bundles whose zero divisor is $R$
identifies the target with the source tensored by $\mcl(R)$, giving
$$
\Omega_X
\cong
f^*\Omega_Y\tensor\mcl(R).
$$
:::

<1>9. The determinant of $E=f_*\OO_X$ satisfies
$$
\boxed{
(\det E)^2\cong\mcl(-B).
}
$$

::: {.proof}
By step <1>8 and the projection formula,
$$
f_*\Omega_X
\cong
\Omega_Y\tensor f_*\mcl(R).
$$
Taking determinants and using step <1>3 with $D=R$ gives
$$
\begin{aligned}
\det f_*\Omega_X
&\cong
\Omega_Y^{\tensor n}\tensor\det f_*\mcl(R)\\
&\cong
\Omega_Y^{\tensor n}\tensor\det E\tensor\mcl(f_*R)\\
&=
\Omega_Y^{\tensor n}\tensor\det E\tensor\mcl(B).
\end{aligned}
$$
On the other hand, step <1>7 gives
$$
\det f_*\Omega_X
\cong
(\det E)^{-1}\tensor\Omega_Y^{\tensor n}.
$$
Cancel $\Omega_Y^{\tensor n}$ and tensor by $\det E$.  The result is
$$
(\det E)^2\tensor\mcl(B)\cong\OO_Y,
$$
or equivalently
$$
(\det E)^2\cong\mcl(-B).
$$
This proves part (d).
:::

<1>10. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove part (a), steps <1>4--<1>5 prove part (b), steps
<1>6--<1>7 prove part (c), and steps <1>8--<1>9 prove part (d).
:::
:::
