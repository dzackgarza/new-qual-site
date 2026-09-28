---
schema: qual/card@1
id: P-AGH532MULTINTER
kind: problem
title: Intersection multiplicity drops by the product of multiplicities under a blowup
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Blowups
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.3.2, the retained Egbert companion calculation, and the
    repository blowup intersection formulas. The source route is to write
    pi^*C=\tilde C+mu_P(C)E and similarly for D, then use E^2=-1 and
    pi^*C.E=pi^*D.E=0. Iterating the identity through point blowups until
    the strict transforms are disjoint gives the sum over ordinary and
    infinitely near common points. The concluding finite sum is understood
    for curves with no common component, as required for proper intersection.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
Let $C$ and $D$ be curves on a surface $X$, meeting at a point $P$. Let $\pi: \tilde{X} \rightarrow X$ be the monoidal transformation with center $P$.

Show that
\[
\tilde{C} \cdot \tilde{D}=C . D-\mu_P(C) \cdot \mu_P(D)
.\]
Conclude that $C . D=\sum \mu_P(C) \cdot \mu_P(D)$, where the sum is taken over all intersection points of $C$ and $D$, including infinitely near intersection points.
:::

::: {.solution}
Write
$$
r=\mu_P(C),
\qquad
s=\mu_P(D),
$$
and let $E$ be the exceptional curve of the blowup
$$
\pi:\widetilde X\longrightarrow X.
$$

<1>1. The total transforms satisfy
$$
\pi^*C=\widetilde C+rE,
\qquad
\pi^*D=\widetilde D+sE.
$$

::: {.proof}
For a curve through the centre of a blowup, the exceptional divisor occurs
in the total transform with coefficient equal to the multiplicity at the
centre. Thus the standard strict-transform formula [[FE-SRFBLOW]] gives
$$
\pi^*C=\widetilde C+\mu_P(C)E
$$
and the analogous formula for $D$.
:::

<1>2. The blowup intersection identities are
$$
\pi^*C\cdot\pi^*D=C\cdot D,
\qquad
\pi^*C\cdot E=\pi^*D\cdot E=0,
\qquad
E^2=-1.
$$

::: {.proof}
These are the standard intersection formulas for the blowup of a
nonsingular surface at a point [[FE-SRFBLOW]].  Pullback preserves the
intersection product of divisors from $X$, every pulled-back divisor has
intersection zero with the exceptional curve, and the exceptional curve has
self-intersection $-1$.
:::

<1>3. One has
$$
\boxed{
\widetilde C\cdot\widetilde D
=
C\cdot D-rs.}
$$

::: {.proof}
By step <1>1,
$$
\widetilde C=\pi^*C-rE,
\qquad
\widetilde D=\pi^*D-sE.
$$
Therefore step <1>2 gives
$$
\begin{aligned}
\widetilde C\cdot\widetilde D
&=(\pi^*C-rE)\cdot(\pi^*D-sE)\\
&=\pi^*C\cdot\pi^*D
-s\,\pi^*C\cdot E
-r\,\pi^*D\cdot E
+rsE^2\\
&=C\cdot D-rs.
\end{aligned}
$$
Substituting the definitions of $r$ and $s$ gives
$$
\widetilde C\cdot\widetilde D
=
C\cdot D-
\mu_P(C)\mu_P(D),
$$
which is the first assertion.
:::

<1>4. Assume $C$ and $D$ have no common irreducible component. There is a
finite sequence of point blowups after which their strict transforms are
disjoint.

::: {.proof}
Resolve the reduced divisor $C\cup D$ by finitely many point blowups on the
nonsingular surface.  After resolution, its irreducible strict transforms
are nonsingular and meet, if at all, only transversely.  If the strict
transforms of $C$ and $D$ still meet at such a transverse point, blow up that
point once more.  Their two strict transforms then meet the exceptional
curve at the two distinct points corresponding to their distinct tangent
directions, so they no longer meet there.

There are only finitely many intersections after resolution. Blowing up each
remaining common point therefore produces a surface on which the final
strict transforms of $C$ and $D$ are disjoint.
:::

<1>5. Along the sequence in step <1>4, let
$$
C_0=C,
\qquad
D_0=D,
$$
and let $C_{i+1},D_{i+1}$ be the strict transforms after blowing up a point
$P_i$ on the $i$th surface. Then
$$
C_i\cdot D_i
-
C_{i+1}\cdot D_{i+1}
=
\mu_{P_i}(C_i)\mu_{P_i}(D_i).
$$

::: {.proof}
Apply step <1>3 on the $i$th surface. If the centre $P_i$ lies on only one
of the two strict transforms, the multiplicity of the other there is zero,
so the same formula still applies and contributes zero.  The nonzero terms
are exactly the points at which the current strict transforms meet: the
ordinary intersection points on $X$ and their infinitely near successors.
:::

<1>6. The global intersection number is the sum of the products of
multiplicities at all ordinary and infinitely near common points:
$$
\boxed{
C\cdot D
=
\sum_P \mu_P(C)\mu_P(D).}
$$

::: {.proof}
Sum the identities of step <1>5 over the finite blowup sequence. The left
side telescopes:
$$
\sum_i
\bigl(C_i\cdot D_i-C_{i+1}\cdot D_{i+1}\bigr)
=
C_0\cdot D_0-C_N\cdot D_N.
$$
By step <1>4 the final strict transforms are disjoint, so
$$
C_N\cdot D_N=0.
$$
Consequently
$$
C\cdot D
=
\sum_i\mu_{P_i}(C_i)\mu_{P_i}(D_i).
$$
Omitting the zero terms leaves precisely the sum over all common points of
$C$ and $D$, including infinitely near common points.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>3 proves the single-blowup formula, and steps <1>4--<1>6 give the
iterated intersection-multiplicity formula.
:::
:::
