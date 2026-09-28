---
schema: qual/card@1
id: P-AGH435PROJECTIONFROMSPACECURVE
kind: problem
title: A space curve projects to a singular plane curve, and $g<\frac{1}{2}(d-1)(d-2)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Embeddings
  - Linear Systems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.5 together with IV.1.8 and the projection
    degeneration III.9.8.3. The proof compares O_X(1) before and after a
    hypothetical smooth birational plane projection, then uses the
    normalization delta formula to make the plane genus inequality strict.
    The same strict inequality forces the flat special fibre to be nonreduced.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be a curve in $\PP^3$, which is not contained in any plane.

a. If $O \notin X$ is a point, such that the projection from $O$ induces a birational morphism $\varphi$ from $X$ to its image in $\PP^2$, show that $\varphi(X)$ must be singular.
Hint: Calculate $\dim H^0(X, \OO_X(1))$ two ways.

b. If $X$ has degree $d$ and genus $g$, conclude that $g<\frac{1}{2}(d-1)(d-2)$.
(Use (Ex.
1.8).)

c. Now let $\ts{X_t}$ be the flat family of curves induced by the projection (III, 9.8.3) whose fibre over $t=1$ is $X$, and whose fibre $X_0$ over $t=0$ is a scheme with support $\varphi(X)$.
Show that $X_0$ always has nilpotent elements.
Thus the example (III, 9.8.4) is typical.
:::

::: {.solution}
Let
$$
Y=\varphi(X)\subseteq\PP^2.
$$
Projection from $O$ is defined by the three-dimensional space of hyperplanes
through $O$, so
$$
\varphi^*\mco_Y(1)\cong\mco_X(1).
$$

<1>1. Since $X\subseteq\PP^3$ is not contained in a plane,
$$
h^0(X,\mco_X(1))\ge4.
$$

::: {.proof}
Restriction gives a linear map
$$
H^0(\PP^3,\mco_{\PP^3}(1))
\longrightarrow
H^0(X,\mco_X(1)).
$$
Its kernel consists of linear forms vanishing identically on $X$, equivalently
planes containing $X$. By hypothesis there is no such plane, so the map is
injective. The source has dimension $4$, proving the claim.
:::

<1>2. If $Y$ were nonsingular, then
$$
h^0(X,\mco_X(1))=3.
$$

::: {.proof}
The morphism
$$
\varphi:X\longrightarrow Y
$$
is birational by hypothesis. If $Y$ were nonsingular, then both $X$ and $Y$
would be smooth projective curves. A birational morphism between smooth
projective curves is an isomorphism.

Therefore
$$
H^0(X,\mco_X(1))
\cong
H^0(Y,\mco_Y(1)).
$$
The integral plane curve $Y$ is not a line: if it were, then $X$, being
isomorphic to $Y\cong\PP^1$, would have
$$
\deg\mco_X(1)
=
\deg\varphi^*\mco_Y(1)
=1,
$$
and hence would be a line in $\PP^3$, contrary to nondegeneracy.

Thus the defining equation of $Y$ has degree at least $2$. Twisting its
ideal sequence by $\mco_{\PP^2}(1)$ gives
$$
0
\longrightarrow
\mco_{\PP^2}(1-\deg Y)
\longrightarrow
\mco_{\PP^2}(1)
\longrightarrow
\mco_Y(1)
\longrightarrow0.
$$
The first sheaf has no global sections, and
$$
H^1(\PP^2,\mco(q))=0
$$
for every $q$. Hence restriction gives
$$
H^0(\PP^2,\mco(1))
\xrightarrow{\sim}
H^0(Y,\mco_Y(1)).
$$
The left side has dimension $3$, proving the claim.
:::

<1>3. The plane image $Y$ is singular.

::: {.proof}
If $Y$ were nonsingular, steps <1>1 and <1>2 would give simultaneously
$$
h^0(X,\mco_X(1))\ge4
$$
and
$$
h^0(X,\mco_X(1))=3,
$$
a contradiction. Hence
$$
\boxed{Y\text{ is singular}.}
$$
This proves (a).
:::

<1>4. If $\deg X=d$, then
$$
\deg Y=d.
$$

::: {.proof}
Because
$$
\varphi^*\mco_Y(1)\cong\mco_X(1)
$$
and $\varphi$ is birational, it has degree one on function fields.  A
nonconstant morphism of projective curves is finite, so the usual degree
formula for pullback of a line bundle applies. Therefore
$$
\deg\mco_X(1)
=
\deg\varphi\cdot\deg\mco_Y(1)
=
\deg\mco_Y(1).
$$
The two sides are respectively $\deg X$ and $\deg Y$, so both equal $d$.
:::

<1>5. The arithmetic genus of the singular plane image is
$$
p_a(Y)=\frac12(d-1)(d-2)>g(X).
$$

::: {.proof}
The plane-curve genus formula gives
$$
p_a(Y)
=
\frac12(d-1)(d-2).
$$

Since $\varphi:X\to Y$ is a birational morphism from the nonsingular curve
$X$, it is the normalization of $Y$. By
[[P-AGH418ARITHGENUSSINGULAR|Exercise IV.1.8]],
$$
p_a(Y)
=
g(X)
+
\sum_{P\in Y}\delta_P.
$$
Step <1>3 says that $Y$ is singular, so at least one local ring is not
normal and the corresponding normalization quotient has positive length.
Hence
$$
\sum_{P\in Y}\delta_P>0.
$$
Therefore
$$
\boxed{
g(X)
<
\frac12(d-1)(d-2)
}.
$$
This proves (b).
:::

<1>6. In the flat projection family, the special fibre satisfies
$$
p_a(X_0)=g(X).
$$

::: {.proof}
The family in Hartshorne III.9.8.3 is flat and projective over the parameter
curve. Flatness preserves the Hilbert polynomial, hence the arithmetic genus
of the one-dimensional fibres. Since the fibre at $t=1$ is the nonsingular
curve $X$,
$$
p_a(X_0)=p_a(X)=g(X).
$$
:::

<1>7. The special fibre $X_0$ is not reduced.

::: {.proof}
By construction the support of $X_0$ is the plane curve $Y$.
Suppose $X_0$ were reduced. Since $Y$ is integral,
$$
X_0=Y
$$
as schemes. Step <1>6 would then give
$$
p_a(Y)=g(X).
$$
But step <1>5 gives the strict inequality
$$
p_a(Y)>g(X),
$$
a contradiction.
Thus $X_0$ is nonreduced.
:::

<1>8. The structure sheaf of $X_0$ has nonzero nilpotent elements.

::: {.proof}
A scheme is reduced exactly when its structure sheaf has zero nilradical.
By step <1>7, $X_0$ is not reduced, so its nilradical is nonzero. Hence
$$
\boxed{X_0\text{ has nilpotent elements}.}
$$
This proves (c).
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>3 proves (a), step <1>5 proves (b), and steps <1>6--<1>8 prove
(c).
:::
:::
