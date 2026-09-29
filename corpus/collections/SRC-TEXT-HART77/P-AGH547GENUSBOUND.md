---
schema: qual/card@1
id: P-AGH547GENUSBOUND
kind: problem
title: Maximal arithmetic genus of a divisor of given degree on a cubic surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Adjunction
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.7, the retained Egbert calculation, the cubic-surface
    blowup/anticanonical description, V.1.9 Hodge index, and the ample-line-
    bundle/Bertini inputs. The retained source passes to a standard-form
    coordinate calculation; the sharp bound is more directly obtained from
    H=-K_S, H^2=3, Hodge index D^2<=d^2/3, and the parity
    D^2 congruent d mod 2 forced by adjunction. The maximizing numerical
    classes are mH for d=3m, mH+L for d=3m+1, and mH+Q for d=3m+2,
    where L is a line and Q=H-L is a smooth residual conic. Their required
    linear systems are shown below to contain smooth irreducible members
    without using the later V.4.8 classification.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete Hodge/parity bound and all three sharpness families.
    Tightened the conic construction to use a base-point-free residual
    subpencil rather than claiming completeness, and used the standard
    Bertini irreducibility theorem for the base-point-free birational system
    |H+L|. Verified the low-degree cases d=1,2,3 separately within the same
    line/conic/hyperplane construction.
---

::: {.problem}
If $D$ is any divisor of degree $d$ on the cubic surface (4.7.3), show that
\[
p_a(D) \leqslant \begin{cases}\frac{1}{6}(d-1)(d-2) & \text { if } d \equiv 1,2\, (\bmod 3) \\ \frac{1}{6}(d-1)(d-2)+\frac{2}{3} & \text { if } d \equiv 0\, (\bmod 3)\end{cases}
\]
Show furthermore that for every $d>0$, this maximum is achieved by some irreducible nonsingular curve.
:::

::: {.solution}
Let
$$
S\subseteq\PP^3
$$
be the nonsingular cubic surface, and let $H$ denote its hyperplane class.
The anticanonical description of the cubic surface gives
$$
\boxed{H=-K_S,\qquad H^2=3.}
$$
For a divisor $D$ of degree $d$ we therefore have
$$
d=D\cdot H.
$$

::: pf

::: {.pf-step #adjunction-genus-formula}
Adjunction gives
$$
\boxed{
p_a(D)=1+\frac{D^2-d}{2}.}
$$

::: pf-proof
On a nonsingular surface,
$$
2p_a(D)-2=D\cdot(D+K_S).
$$
Since $K_S=-H$ and $D\cdot H=d$,
$$
D\cdot(D+K_S)=D^2-d.
$$
Solving for $p_a(D)$ gives the formula.
:::

:::

::: {.pf-step #hodge-index-bound}
The self-intersection of $D$ satisfies
$$
\boxed{3D^2\le d^2.}
$$

::: pf-proof
The hyperplane class $H$ is ample. The Hodge index inequality
[[P-AGH519HODGEINDEX]] gives
$$
(D^2)(H^2)\le(D\cdot H)^2.
$$
Substituting
$$
H^2=3,
\qquad
D\cdot H=d
$$
gives
$$
3D^2\le d^2.
$$
:::

:::

::: {.pf-step #parity-condition}
One also has the parity condition
$$
\boxed{D^2\equiv d\pmod2.}
$$

::: pf-proof
Step [](#adjunction-genus-formula){.pf-ref} shows that
$$
D^2-d=2p_a(D)-2
$$
is even. Hence $D^2$ and $d$ have the same parity.
:::

:::

::: {.pf-step #bound-d-equiv-0}
If
$$
d=3m,
$$
then
$$
\boxed{D^2\le3m^2.}
$$

::: pf-proof
Step [](#hodge-index-bound){.pf-ref} gives
$$
D^2\le\frac{d^2}{3}=3m^2.
$$
No parity correction is needed because
$$
3m^2\equiv3m=d\pmod2.
$$
:::

:::

::: {.pf-step #bound-d-equiv-1}
If
$$
d=3m+1,
$$
then
$$
\boxed{D^2\le3m^2+2m-1.}
$$

::: pf-proof
Step [](#hodge-index-bound){.pf-ref} gives
$$
D^2\le\frac{(3m+1)^2}{3}
=
3m^2+2m+\frac13.
$$
Thus
$$
D^2\le3m^2+2m.
$$
But
$$
(3m^2+2m)-(3m+1)
=
3m^2-m-1
$$
is odd, so the integer $3m^2+2m$ has the wrong parity for $D^2$ by step
[](#parity-condition){.pf-ref}. The next smaller integer has the required parity, giving
$$
D^2\le3m^2+2m-1.
$$
:::

:::

::: {.pf-step #bound-d-equiv-2}
If
$$
d=3m+2,
$$
then
$$
\boxed{D^2\le3m^2+4m.}
$$

::: pf-proof
Step [](#hodge-index-bound){.pf-ref} gives
$$
D^2\le\frac{(3m+2)^2}{3}
=
3m^2+4m+1+\frac13,
$$
so
$$
D^2\le3m^2+4m+1.
$$
The difference
$$
(3m^2+4m+1)-(3m+2)
=
3m^2+m-1
$$
is odd. Hence the top integer allowed by Hodge has the wrong parity, and
step [](#parity-condition){.pf-ref} forces
$$
D^2\le3m^2+4m.
$$
:::

:::

::: {.pf-step #genus-bound-mod-0}
If $d\equiv0\pmod3$, then
$$
\boxed{
p_a(D)
\le
\frac16(d-1)(d-2)+\frac23.}
$$

::: pf-proof
Write $d=3m$. By steps [](#adjunction-genus-formula){.pf-ref} and [](#bound-d-equiv-0){.pf-ref},
$$
\begin{aligned}
p_a(D)
&\le
1+\frac{3m^2-3m}{2}\\
&=
\frac{3m^2-3m+2}{2}.
\end{aligned}
$$
On the other hand,
$$
\frac16(d-1)(d-2)+\frac23
=
\frac{(3m-1)(3m-2)+4}{6}
=
\frac{3m^2-3m+2}{2}.
$$
:::

:::

::: {.pf-step #genus-bound-mod-1}
If $d\equiv1\pmod3$, then
$$
\boxed{
p_a(D)
\le
\frac16(d-1)(d-2).}
$$

::: pf-proof
Write $d=3m+1$. Steps [](#adjunction-genus-formula){.pf-ref} and [](#bound-d-equiv-1){.pf-ref} give
$$
\begin{aligned}
p_a(D)
&\le
1+
\frac{(3m^2+2m-1)-(3m+1)}2\\
&=
\frac{m(3m-1)}2.
\end{aligned}
$$
Since
$$
\frac16(d-1)(d-2)
=
\frac{(3m)(3m-1)}6
=
\frac{m(3m-1)}2,
$$
this is the required bound.
:::

:::

::: {.pf-step #genus-bound-mod-2}
If $d\equiv2\pmod3$, then
$$
\boxed{
p_a(D)
\le
\frac16(d-1)(d-2).}
$$

::: pf-proof
Write $d=3m+2$. By steps [](#adjunction-genus-formula){.pf-ref} and [](#bound-d-equiv-2){.pf-ref},
$$
\begin{aligned}
p_a(D)
&\le
1+
\frac{(3m^2+4m)-(3m+2)}2\\
&=
\frac{m(3m+1)}2.
\end{aligned}
$$
Also
$$
\frac16(d-1)(d-2)
=
\frac{(3m+1)(3m)}6
=
\frac{m(3m+1)}2.
$$
This proves the numerical inequality in every residue class.
:::

:::

::: {.pf-step #line-conic-decomposition}
Choose one of the $27$ lines
$$
L\subseteq S.
$$
There is a nonsingular irreducible conic $Q\subseteq S$ with
$$
\boxed{H=L+Q,\qquad Q\sim H-L.}
$$

::: pf-proof
Planes in $\PP^3$ containing $L$ form a pencil. For such a plane $\Pi$,
the plane section $S\cap\Pi$ has degree $3$ and contains $L$, so
scheme-theoretically
$$
S\cap\Pi=L+Q_\Pi
$$
for a residual conic $Q_\Pi$.

A singular plane conic is reducible or nonreduced. In either case its
support contains a line. Hence a singular residual conic would make $\Pi$
contain a line on $S$ other than $L$ (or give a doubled line). Since a
nonsingular cubic surface has only finitely many lines, only finitely many
planes in the pencil can give such a residual conic. A general plane through
$L$ therefore gives a nonsingular irreducible conic $Q$. Its divisor class
satisfies
$$
L+Q\sim H.
$$
:::

:::

::: {.pf-step #line-conic-numerics}
The line and conic classes satisfy
$$
\boxed{
L^2=-1,
\qquad
H\cdot L=1,
\qquad
Q^2=0,
\qquad
H\cdot Q=2.}
$$

::: pf-proof
The first two equalities are the defining numerical properties of a line on
the cubic surface [[FE-SRFCUBIC]]. Since $Q=H-L$,
$$
H\cdot Q
=
H^2-H\cdot L
=
3-1
=2,
$$
and
$$
Q^2
=(H-L)^2
=
3-2-1
=0.
$$
:::

:::

::: {.pf-step #conic-globally-generated}
The residual conics cut out by planes through $L$ form a base-point
free pencil in $|H-L|$. Consequently
$$
\boxed{\OO_S(Q)\text{ is globally generated}.}
$$

::: pf-proof
Every residual conic has class $H-L=Q$, so these residual conics form a
one-dimensional linear subsystem of $|Q|$.

If $x\notin L$, choose a plane through $L$ not containing $x$; its residual
conic does not contain $x$.

Now let $x\in L$. Choose local homogeneous coordinates in which
$$
I_L=(u,v).
$$
Because the cubic equation vanishes on $L$, it can be written
$$
F=uA+vB
$$
with quadratic forms $A,B$. Smoothness of $S$ at $x$ implies
$$
(A(x),B(x))\ne(0,0).
$$
A plane through $L$ has equation
$$
\alpha u+\beta v=0.
$$
After removing the component $L$, its residual conic contains $x$ exactly
when
$$
\alpha B(x)-\beta A(x)=0.
$$
This is one linear condition on $[\alpha:\beta]\in\PP^1$, not every member
of the pencil. Hence some residual conic avoids $x$. Thus $|Q|$ has no base
point anywhere on $S$: already this residual-conic subpencil has no base
point. Therefore $\OO_S(Q)$ is globally generated.
:::

:::

::: {.pf-step #h-plus-l-globally-generated}
The line bundle
$$
\OO_S(H+L)
$$
is globally generated.

::: pf-proof
The section cutting out $L$ gives the exact sequence
$$
0
\longrightarrow
\OO_S(H)
\longrightarrow
\OO_S(H+L)
\longrightarrow
\OO_L(H+L)
\longrightarrow0.
$$
Since
$$
(H+L)\cdot L=1-1=0,
$$
and $L\cong\PP^1$, one has
$$
\OO_L(H+L)\cong\OO_{\PP^1}.
$$

Also
$$
H^1(S,\OO_S(H))=0.
$$
Indeed, twisting the cubic hypersurface sequence by $\OO_{\PP^3}(1)$ gives
$$
0
\longrightarrow
\OO_{\PP^3}(-2)
\longrightarrow
\OO_{\PP^3}(1)
\longrightarrow
\OO_S(H)
\longrightarrow0,
$$
and the intermediate cohomology of projective space gives the desired
vanishing.

Therefore restriction
$$
H^0(S,\OO_S(H+L))
\longrightarrow
H^0(L,\OO_L)
$$
is surjective. Choose a section restricting to the nonzero constant $1$;
it has no zero on $L$.

Off $L$, the subsystem obtained by multiplying hyperplane sections by the
section of $L$ has no base point because $H$ is very ample. Hence
\(\OO_S(H+L)\) is globally generated everywhere.
:::

:::

::: {.pf-step #h-plus-l-birational}
The morphism defined by $|H+L|$ is birational onto its image.

::: pf-proof
On the open set $S\setminus L$, the subsystem
$$
s_L\,H^0(S,\OO_S(H))
\subseteq
H^0(S,\OO_S(H+L))
$$
has the same ratios as the hyperplane system $|H|$. Since $|H|$ is the
given embedding
$$
S\hookrightarrow\PP^3,
$$
these sections separate general points of $S\setminus L$. The complete
system $|H+L|$ therefore defines a generically one-to-one morphism, hence a
birational morphism onto its image.
:::

:::

::: {.pf-step #general-mh-irreducible}
For every $m\ge1$, a general member of
$$
|mH|
$$
is nonsingular and irreducible.

::: pf-proof
The hyperplane bundle $\OO_S(H)$ is very ample, and every positive power of
a very ample bundle is very ample. Thus $|mH|$ is the hyperplane system of
an embedding. Bertini's hyperplane theorem gives a nonsingular general
member; since $S$ is irreducible of dimension two, a general hyperplane
section is connected, hence a nonsingular connected curve is irreducible.
:::

:::

::: {.pf-step #nh-minus-l-irreducible}
For every $n\ge1$, the class
$$
nH-L
$$
contains a nonsingular irreducible curve.

::: pf-proof
For $n=1$ this is the nonsingular irreducible conic
$$
Q\sim H-L
$$
from step [](#line-conic-decomposition){.pf-ref}.

For $n\ge2$,
$$
nH-L=(n-1)H+Q.
$$
The bundle $\OO_S((n-1)H)$ is very ample and $\OO_S(Q)$ is globally
generated by step [](#conic-globally-generated){.pf-ref}. Exercise II.7.5(d), proved in
[[P-AGH275AMPLEPROPS]], says that the tensor product of a very ample bundle
and a globally generated bundle is very ample. Hence $\OO_S(nH-L)$ is very
ample. A general member is therefore nonsingular and irreducible by the same
Bertini argument as in step [](#general-mh-irreducible){.pf-ref}.
:::

:::

::: {.pf-step #nh-minus-q-irreducible}
For every $n\ge1$, the class
$$
nH-Q
$$
contains a nonsingular irreducible curve.

::: pf-proof
Since $Q=H-L$,
$$
nH-Q=(n-1)H+L.
$$
For $n=1$ this is the line $L$ itself.

For $n=2$, the class is
$$
H+L.
$$
By step [](#h-plus-l-globally-generated){.pf-ref} its complete linear system is base-point free, and by step
[](#h-plus-l-birational){.pf-ref} the associated morphism is birational, hence separable. Bertini's
theorem for a base-point-free separable linear system therefore gives a
nonsingular general member. Since the associated morphism has
two-dimensional image, Bertini's irreducibility theorem for a base-point-free
linear system also gives an irreducible general member.

For $n\ge3$,
$$
nH-Q=(n-2)H+(H+L).
$$
The first summand is very ample and the second is globally generated by step
[](#h-plus-l-globally-generated){.pf-ref}. Again [[P-AGH275AMPLEPROPS]] makes their tensor product very ample,
and a general member is nonsingular and irreducible.
:::

:::

::: {.pf-step #sharp-mod-0-realized}
If
$$
d=3m>0,
$$
the class
$$
\boxed{D_m=mH}
$$
has degree $d$, reaches the upper bound, and contains a nonsingular
irreducible curve.

::: pf-proof
Since $m\ge1$,
$$
H\cdot(mH)=3m=d,
\qquad
(mH)^2=3m^2.
$$
Thus equality holds in the self-intersection bound of step [](#bound-d-equiv-0){.pf-ref}, hence in
the genus bound of step [](#genus-bound-mod-0){.pf-ref}. Step [](#general-mh-irreducible){.pf-ref} supplies a nonsingular irreducible
member.
:::

:::

::: {.pf-step #sharp-mod-1-realized}
If
$$
d=3m+1>0,
$$
the class
$$
\boxed{D_m=mH+L=(m+1)H-Q}
$$
has degree $d$, reaches the upper bound, and contains a nonsingular
irreducible curve.

::: pf-proof
Put $n=m+1$. Since $d>0$, one has $n\ge1$. By step [](#line-conic-numerics){.pf-ref},
$$
H\cdot D_m
=
3m+1
=d,
$$
and
$$
\begin{aligned}
D_m^2
&=(mH+L)^2\\
&=3m^2+2m-1.
\end{aligned}
$$
This is equality in step [](#bound-d-equiv-1){.pf-ref}, so step [](#genus-bound-mod-1){.pf-ref} gives the maximal arithmetic
genus. Since
$$
D_m=nH-Q,
$$
step [](#nh-minus-q-irreducible){.pf-ref} gives a nonsingular irreducible member.
:::

:::

::: {.pf-step #sharp-mod-2-realized}
If
$$
d=3m+2>0,
$$
the class
$$
\boxed{D_m=mH+Q=(m+1)H-L}
$$
has degree $d$, reaches the upper bound, and contains a nonsingular
irreducible curve.

::: pf-proof
Put $n=m+1\ge1$. Using step [](#line-conic-numerics){.pf-ref},
$$
H\cdot D_m
=
3m+2
=d,
$$
and
$$
\begin{aligned}
D_m^2
&=(mH+Q)^2\\
&=3m^2+4m.
\end{aligned}
$$
Thus equality holds in step [](#bound-d-equiv-2){.pf-ref}, and step [](#genus-bound-mod-2){.pf-ref} gives the maximal genus.
Because
$$
D_m=nH-L,
$$
step [](#nh-minus-l-irreducible){.pf-ref} supplies a nonsingular irreducible member.
:::

:::

::: pf-qed
Steps [](#adjunction-genus-formula){.pf-ref}, [](#hodge-index-bound){.pf-ref}, [](#parity-condition){.pf-ref}, [](#bound-d-equiv-0){.pf-ref}, [](#bound-d-equiv-1){.pf-ref}, [](#bound-d-equiv-2){.pf-ref}, [](#genus-bound-mod-0){.pf-ref}, [](#genus-bound-mod-1){.pf-ref} and [](#genus-bound-mod-2){.pf-ref} prove the stated sharp genus bound for every divisor of
degree $d$. Steps [](#line-conic-decomposition){.pf-ref}, [](#line-conic-numerics){.pf-ref}, [](#conic-globally-generated){.pf-ref}, [](#h-plus-l-globally-generated){.pf-ref}, [](#h-plus-l-birational){.pf-ref}, [](#general-mh-irreducible){.pf-ref}, [](#nh-minus-l-irreducible){.pf-ref} and [](#nh-minus-q-irreducible){.pf-ref} construct the smooth line/conic auxiliary
classes and prove the needed linear systems contain nonsingular irreducible
curves. Steps [](#sharp-mod-0-realized){.pf-ref}, [](#sharp-mod-1-realized){.pf-ref} and [](#sharp-mod-2-realized){.pf-ref} realize equality for every positive degree in the
three residue classes modulo $3$.
:::

:::
:::
