---
schema: qual/card@1
id: P-AGH554CONTRACTEDCURVES
kind: problem
title: Curves contracted by a birational morphism and negative definiteness of the intersection matrix
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Birational Geometry
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.5.4 as transcribed here, the retained Andrew Egbert
    companion argument, the Hodge index theorem, the point-blowup
    intersection formulas, and the surface factorization theorem. The
    retained note has the intended Hodge-index idea but says that the
    pullback of an ample divisor is ample; for a contraction this is false,
    since its pullback has intersection zero with every exceptional curve.
    What is needed is that f^*H has positive square, so the signature form
    of Hodge index makes its orthogonal complement negative definite. The
    proof below also supplies the missing independence of exceptional curve
    classes by factoring f into point blowups; the same factorization shows
    every irreducible contracted curve is a strict transform of an
    exceptional P^1.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read both parts against the factorization theorem and the signature
    form of Hodge index. Checked that each contracted prime is the final
    strict transform of a unique exceptional P^1, that the exceptional prime
    classes are triangular with diagonal 1 in the independent total-transform
    basis, and hence that every fibre-component subset is numerically
    independent. Also checked that D=f^*H has D^2=H^2>0 and D.Y_i=0 without
    being ample, so D-perp is negative definite. Therefore Y^2<0 in part (a)
    and a^T(Y_i.Y_j)a=(sum a_iY_i)^2<0 for every nonzero vector in part (b).
---

::: {.problem}
Let $f: X \rightarrow X^{\prime}$ be a birational morphism of nonsingular surfaces.

a. If $Y \subseteq X$ is an irreducible curve such that $f(Y)$ is a point, then $Y \cong \PP^1$ and $Y^2<0$.

b. Let $P^{\prime} \in X^{\prime}$ be a fundamental point of $f^{-1}$, and let $Y_1, \ldots, Y_r$ be the irreducible components of $f^{-1}\left(P^{\prime}\right)$.
Show that the matrix $\left\|Y_i . Y_j\right\|$ is negative definite.
:::

::: {.solution}
We use the standing hypotheses of the surfaces chapter, so $X$ and $X'$
are nonsingular projective surfaces.

<1>1. The birational morphism $f$ factors as a finite sequence of point
blowups:
$$
X=X_n
\xrightarrow{\pi_n}
X_{n-1}
\longrightarrow
\cdots
\longrightarrow
X_1
\xrightarrow{\pi_1}
X_0=X',
$$
where each
$$
\pi_j:X_j\longrightarrow X_{j-1}
$$
is the blowup of a point and has exceptional curve
$$
E_j\cong\PP^1.
$$

::: {.proof}
This is the factorization theorem for birational morphisms of nonsingular
projective surfaces [[T-SRFZMT]]. Each elementary factor is a monoidal
transformation at a point.
:::

<1>2. Every irreducible curve $Y\subseteq X$ contracted by $f$ is the final
strict transform of one of the exceptional curves $E_j$. In particular,
$$
\boxed{Y\cong\PP^1.}
$$

::: {.proof}
For
$$
0\le i\le n,
$$
let $Y_i\subseteq X_i$ be the image of $Y$ under
$$
X=X_n\longrightarrow X_i.
$$
We have $Y_n=Y$, while
$$
Y_0=f(Y)
$$
is a point. Choose the least index $j\ge1$ for which $Y_j$ is a curve.
Then $Y_{j-1}$ is a point and
$$
\pi_j(Y_j)=Y_{j-1}.
$$
The only irreducible curve contracted by the blowup morphism $\pi_j$ is its
exceptional curve, so
$$
Y_j=E_j.
$$

For every $i>j$, the morphism
$$
\pi_i:Y_i\longrightarrow Y_{i-1}
$$
does not contract $Y_i$, hence $Y_i$ is the strict transform of
$Y_{i-1}$. Blowing up a nonsingular surface at a point preserves a
nonsingular curve under strict transform: if the centre lies on the curve,
the restriction of the blowup to its strict transform is the blowup of a
nonsingular curve at a Cartier divisor, hence an isomorphism; if the centre
does not lie on it, nothing changes.

Starting from
$$
E_j\cong\PP^1
$$
therefore gives
$$
Y=Y_n\cong\PP^1.
$$
:::

<1>3. The numerical classes of all irreducible curves contracted by $f$ are
linearly independent in
$$
\operatorname{NS}(X)_\RR.
$$

::: {.proof}
At the $j$th blowup, the standard blowup decomposition gives
$$
\operatorname{NS}(X_j)_\RR
=
\pi_j^*\operatorname{NS}(X_{j-1})_\RR
\oplus
\RR[E_j],
$$
with
$$
E_j^2=-1
$$
and $E_j$ orthogonal to the pullback summand [[FE-SRFBLOW]].

Pull $[E_j]$ back through the later blowups by total transform and denote
its final class on $X$ by
$$
e_j.
$$
Iterating the displayed direct-sum decomposition shows that
$$
e_1,\ldots,e_n
$$
are linearly independent.

Let $\overline E_j\subseteq X$ be the final strict transform of $E_j$.
At any later blowup, a strict-transform class is either unchanged under
pullback or is the pullback minus the new exceptional class. Consequently
$$
[\overline E_j]
=
e_j+\sum_{\ell>j}a_{j\ell}e_\ell
$$
for some integers $a_{j\ell}$. Thus the change-of-basis matrix from the
$e_j$ to the $[\overline E_j]$ is triangular with every diagonal entry
equal to $1$. Hence
$$
[\overline E_1],\ldots,[\overline E_n]
$$
are linearly independent.

By step <1>2, every irreducible curve contracted by $f$ is one of the
$\overline E_j$. Any subset of these classes is therefore linearly
independent.
:::

<1>4. Let $H$ be a very ample divisor on $X'$ and put
$$
D=f^*H.
$$
Then
$$
\boxed{
D^2=H^2>0,
\qquad
D\cdot C=0
}
$$
for every curve $C$ contracted by $f$.

::: {.proof}
Because $f$ is birational of degree one, the projection formula for
intersection products gives
$$
(f^*H)^2=H^2.
$$
Very ampleness implies
$$
H^2>0.
$$

If $C$ is contracted, then $f_*C=0$ as a one-cycle. Hence the projection
formula gives
$$
D\cdot C
=
f^*H\cdot C
=
H\cdot f_*C
=0.
$$

Notice that $D$ is generally not ample: this zero intersection with the
exceptional curves is exactly why the retained source's statement
"pullback of ample is ample" cannot be used.
:::

<1>5. The intersection form is negative definite on the orthogonal
complement
$$
D^\perp
\subseteq
\operatorname{NS}(X)_\RR.
$$

::: {.proof}
The Hodge index theorem says that the intersection form on
$$
\operatorname{NS}(X)_\RR
$$
has signature
$$
(1,\rho(X)-1)
$$
[[T-SRFHODGE]].

Step <1>4 gives $D^2>0$. In a real vector space with a symmetric form of
signature $(1,\rho-1)$, the orthogonal complement of any positive-square
vector is negative definite: the positive index is already exhausted by
the line $\RR D$. Therefore every nonzero
$$
\alpha\in D^\perp
$$
satisfies
$$
\alpha^2<0.
$$
:::

<1>6. If $Y\subseteq X$ is an irreducible curve contracted by $f$, then
$$
\boxed{Y^2<0.}
$$

::: {.proof}
By step <1>4,
$$
D\cdot Y=0,
$$
so
$$
[Y]\in D^\perp.
$$
The numerical class $[Y]$ is nonzero: if $A$ is any ample divisor on $X$,
then
$$
A\cdot Y>0.
$$
Step <1>5 therefore gives
$$
Y^2<0.
$$
Together with step <1>2 this proves part (a).
:::

<1>7. For the components
$$
Y_1,\ldots,Y_r
$$
of the fibre over the fundamental point $P'$, every nonzero real vector
$(a_1,\ldots,a_r)$ satisfies
$$
\boxed{
\left(\sum_{i=1}^r a_iY_i\right)^2<0.}
$$

::: {.proof}
Each $Y_i$ is contracted by $f$, so step <1>4 gives
$$
D\cdot Y_i=0.
$$
Hence
$$
Z=\sum_{i=1}^r a_iY_i
$$
lies in $D^\perp$.

If the coefficient vector is nonzero, step <1>3 says that the numerical
classes $[Y_i]$ are linearly independent. Thus
$$
[Z]\ne0
$$
in $\operatorname{NS}(X)_\RR$. Step <1>5 now gives
$$
Z^2<0.
$$
:::

<1>8. The intersection matrix
$$
\boxed{
\bigl(Y_i\cdot Y_j\bigr)_{1\le i,j\le r}
\text{ is negative definite}.}
$$

::: {.proof}
Let
$$
A=(Y_i\cdot Y_j)_{i,j}.
$$
For a column vector
$$
a=(a_1,\ldots,a_r)^T\in\RR^r,
$$
bilinearity of the intersection product gives
$$
a^TAa
=
\left(\sum_{i=1}^r a_iY_i\right)^2.
$$
By step <1>7 this quantity is strictly negative for every nonzero $a$.
This is exactly negative definiteness of $A$, proving part (b).
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 identify contracted irreducible curves as independent
strict transforms of exceptional $\PP^1$'s. Steps <1>4--<1>6 combine the
positive-square pullback of a very ample divisor with Hodge index to prove
part (a). Steps <1>7--<1>8 apply the same negative-definite orthogonal
complement to the whole exceptional fibre and prove part (b).
:::
:::
