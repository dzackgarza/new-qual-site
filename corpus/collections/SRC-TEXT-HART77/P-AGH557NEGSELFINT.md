---
schema: qual/card@1
id: P-AGH557NEGSELFINT
kind: problem
title: A curve contracted to a point on a projective surface has negative self-intersection
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
  date: 2026-09-20
  note: >-
    Read Hartshorne V.5.7 as transcribed here, the retained Andrew Egbert
    note, the completed V.5.4 contraction argument, and the Hodge index
    theorem. The retained note says simply that V.5.4 applies. As literally
    transcribed, however, the statement omits the hypothesis that f has
    two-dimensional image: C x P^1 -> C followed by an embedding of C into
    a projective surface has a fibre Y with Y^2=0. The intended contraction
    statement is correct once dim f(X)=2 (in particular for a birational
    contraction). The proof below records this erratum and proves the
    corrected statement using D=f^*H: D^2=deg(f)H^2>0, D.Y=0, and the
    signature form of Hodge index.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read the literal statement, counterexample, corrected hypothesis, and
    Hodge-index proof. Checked that the one-dimensional-image counterexample
    has f^{-1}(P)=Y and Y^2=0. Under dim f(X)=2, properness makes f
    surjective onto the irreducible surface X_0 and therefore generically
    finite, so (f^*H)^2=deg(f)H^2>0. The hyperplane H_1 avoiding P gives
    f^*H.Y=0, an ample divisor on X shows [Y] is numerically nonzero, and
    the signature form of Hodge index gives Y^2<0. Also checked that the
    H_0 decomposition in the printed hint has only Y over P because
    f^{-1}(P)=Y.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source did not require f surjective, and C x P^1 -> C -> C x P^1 contracts a fibre Y with Y^2 = 0; the statement now takes f surjective, and the solution proves that statement.'
---

::: {.problem}
Let $Y$ be an irreducible curve on a surface $X$, and suppose there is a surjective morphism $f: X \rightarrow X_0$ to a projective variety $X_0$ of dimension 2, such that $f(Y)$ is a point $P$ and $f^{-1}(P)=Y$.
Then show that $Y^2<0$.

Hint: Let $\linearsystem{H}$ be a very ample (Cartier) divisor class on $X_0$, let $H_0 \in\linearsystem{H}$ be a divisor containing $P$, and let $H_1 \in\linearsystem{H}$ be a divisor not containing $P$.
Then consider $f^* H_0, f^* H_1$ and $\tilde{H}_0=f^*\left(H_0-P\right)^{-}$.
:::

::: {.solution}
::: pf

::: {.pf-step #generically-finite}
$f$ is dominant and generically finite.

::: pf-proof
$f$ is surjective onto the irreducible surface $X_0$, so it is dominant, and $\dim X = \dim X_0 = 2$ makes the generic fibre finite.
:::

:::

::: {.pf-step #pullback-square-positive}
Let $H$ be a very ample Cartier divisor on $X_0$ and put
$$
D=f^*H.
$$
Then
$$
\boxed{D^2>0.}
$$

::: pf-proof
By step [](#generically-finite){.pf-ref}, $f$ has a positive degree
$$
d=[K(X):K(X_0)]>0.
$$
The projection formula for intersection products gives
$$
D^2
=(f^*H)^2
=d\,H^2.
$$
Very ampleness of $H$ gives
$$
H^2>0,
$$
so
$$
D^2>0.
$$
:::

:::

::: {.pf-step #pullback-meets-y-zero}
One has
$$
\boxed{D\cdot Y=0.}
$$

::: pf-proof
Choose
$$
H_1\in\linearsystem{H}
$$
with
$$
P\notin H_1,
$$
as in the hint. Since
$$
f(Y)=P,
$$
the divisor
$$
f^*H_1
$$
is disjoint from $Y$. Therefore
$$
f^*H_1\cdot Y=0.
$$
Because
$$
f^*H_1\sim f^*H=D,
$$
intersection depends only on numerical equivalence, and hence
$$
D\cdot Y=0.
$$
Equivalently, the projection formula gives
$$
f^*H\cdot Y=H\cdot f_*Y=0
$$
because $Y$ is contracted to a point.
:::

:::

::: {.pf-step #y-class-nonzero}
The numerical class
$$
[Y]\in\operatorname{NS}(X)_\RR
$$
is nonzero.

::: pf-proof
Let $A$ be any ample divisor on the nonsingular projective surface $X$.
Since $Y$ is an irreducible curve,
$$
A\cdot Y>0.
$$
Thus $Y$ cannot be numerically equivalent to zero.
:::

:::

::: {.pf-step #orthogonal-complement-negative-definite}
The intersection form is negative definite on
$$
D^\perp
=
\left\{
\alpha\in\operatorname{NS}(X)_\RR:
\alpha\cdot D=0
\right\}.
$$

::: pf-proof
The Hodge index theorem [[T-SRFHODGE]] says that the intersection form on
$$
\operatorname{NS}(X)_\RR
$$
has signature
$$
(1,\rho(X)-1).
$$
Step [](#pullback-square-positive){.pf-ref} gives
$$
D^2>0.
$$
Hence the line
$$
\RR D
$$
already supplies the unique positive direction, so its orthogonal
complement $D^\perp$ is negative definite. Therefore every nonzero
$$
\alpha\in D^\perp
$$
satisfies
$$
\alpha^2<0.
$$
:::

:::

::: {.pf-step #y-negative-square}
The contracted curve satisfies
$$
\boxed{Y^2<0.}
$$

::: pf-proof
By step [](#pullback-meets-y-zero){.pf-ref},
$$
[Y]\in D^\perp.
$$
By step [](#y-class-nonzero){.pf-ref} this class is nonzero. Step [](#orthogonal-complement-negative-definite){.pf-ref} therefore gives
$$
Y^2<0.
$$
:::

:::

::: {.pf-step #hint-divisors-reconciled}
The divisors appearing in the printed hint are compatible with the
same calculation.

::: pf-proof
Choose
$$
H_0\in\linearsystem{H},
\qquad
P\in H_0,
$$
and let $\widetilde H_0$ denote the closure of the pullback away from the
contracted point, as in the hint. Since
$$
f^{-1}(P)=Y,
$$
the pullback has the form
$$
f^*H_0=\widetilde H_0+mY
$$
for some integer
$$
m>0.
$$
Intersecting with $Y$ and using step [](#pullback-meets-y-zero){.pf-ref} gives
$$
0
=
f^*H_0\cdot Y
=
\widetilde H_0\cdot Y+mY^2.
$$
Step [](#y-negative-square){.pf-ref} says $Y^2<0$, so necessarily
$$
\widetilde H_0\cdot Y=-mY^2>0.
$$
Thus the two hyperplanes in the hint encode the same geometry: the
hyperplane avoiding $P$ gives zero intersection with $Y$, while a
hyperplane through $P$ acquires the exceptional component $mY$.
:::

:::

::: pf-qed
Steps [](#pullback-square-positive){.pf-ref}, [](#pullback-meets-y-zero){.pf-ref}, [](#y-class-nonzero){.pf-ref} and [](#orthogonal-complement-negative-definite){.pf-ref}
place the nonzero class of $Y$ in the negative-definite orthogonal
complement of the positive-square divisor $f^*H$. Step [](#y-negative-square){.pf-ref} gives
$Y^2<0$, and step [](#hint-divisors-reconciled){.pf-ref} reconciles the proof with the printed hint.
:::

:::
:::
