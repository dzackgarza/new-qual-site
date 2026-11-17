---
schema: qual/card@1
id: P-AGH549MINGENUS
kind: problem
title: Minimal positive genus of a curve of given degree on the cubic surface
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
    Read Hartshorne V.4.9 and the retained Egbert coordinate attempt, then
    used the immediately preceding V.4.8 classification/global-generation
    lemma. A positive-genus smooth curve is in case (c) of V.4.8. Contracting
    any line of intersection zero preserves its degree, self-intersection,
    and genus. If one stops on X_r with r>=3 and all line intersections
    positive, writing N=D+K shows N is effective by Riemann-Roch with
    chi(N)=g>0, and that N is nef because a component C of N with N.C<0
    would satisfy C^2=-1 and C.A=1 by adjunction, contradicting line
    positivity; hence N^2>=0 and D^2>=2d-6. If the contraction reaches
    X_2=Bl_{P_1,P_2} P^2, write
    D=c h+b_1(h-e_1)+b_2(h-e_2); then d=3c+2(b_1+b_2) and adjunction gives an
    explicit genus formula. Its parity cases yield the stated lower bounds,
    and explicit X_2 classes realize equality. General smooth members can be
    chosen away from the four points whose blowups recover the fixed cubic
    surface.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete proof against V.4.9, the V.4.8 contraction and
    global-generation lemma, and the X_2 intersection form. Checked the
    even/odd parity algebra and both equality families. Added the explicit
    justification that the globally generated remainder N has N^2>=0; no
    later-card input is used.
- event: source-checked
  by: claude
  date: 2026-11-17
  note: >-
    Read Gruson-Peskine II in its supplied text version: the definitions of
    r(O_S(C)) and F_d(r), Proposition 2.1 (printed p. 407), the proof of
    Proposition 2.1 through Lemma 2.2, Theorem 2.5 (printed p. 409), its
    necessity argument with Lemmas 2.6, 2.7, 2.9 and Proposition 2.10, and the
    table of gaps (printed p. 411). Read Bourbaki 592 printed pp. 301-302,
    Theorems 0.1-0.3 and Remark 2, and its Sections 1 and 5. Derived the case
    r = 2 of the criterion by hand from F_d(1) = 5/8 and F_d(2) = (d-1)/2 and
    checked it against all 32 rows of the table, whose F_d(2) column is the
    initial segment below (d-6)/2 for even d and below (d-5)/2 for odd d.
    Confirmed the printed statement of Ex. V.4.9 in the book text and the
    standing hypothesis of an algebraically closed field. What was not
    checked: the article body was read as an extraction whose Section 2
    statements carry a rendered-page check but whose remaining formulas do
    not, so Lemma 2.6, the Appendices and Corollary 2.3 are read from the
    extraction only; no independent file of Gruson-Peskine was consulted; and
    whether Bourbaki's Theorem 5.1 transports the attainment to characteristic
    p in this setting is not settled here.
- event: solution-reviewed
  by: claude
  date: 2026-11-17
  note: >-
    Read the whole proof and repaired two missing justifications in step
    repeat-contraction-until-x2-or-positive, which stated its conclusion for
    (-1)-curves and argued for lines: a (-1)-curve is the same curve as a line
    of X_r by adjunction, and every line of X_{r-1} is the strict transform of
    a line of X_r because a nonzero multiplicity would give an effective curve
    of nonpositive anticanonical degree. Nothing else in the proof changed,
    and the arithmetic of the even and odd cases and of both equality
    families was rechecked and stands. The remark on published solutions now
    carries Gruson-Peskine and Bourbaki 592 with their printed pages, and it
    corrects the earlier description of Egbert's V.4.9, which is a draft and
    not a proof. Not checked here: certification, and the characteristic p
    question recorded in the source-checked event above.
---

::: {.problem}
If $C$ is an irreducible non-singular curve of degree $d$ on the cubic surface, and if the genus $g>0$, then
$$
g \geqslant \begin{cases}\frac{1}{2}(d-6) & \text{if $d$ is even, } d \geqslant 8 \\ \frac{1}{2}(d-5) & \text{if $d$ is odd, } d \geqslant 13\end{cases}
$$
and this minimum value of $g>0$ is achieved for each $d$ in the range given.
:::

::: {.solution}
Let
$$
S=X_6=\operatorname{Bl}_{P_1,\ldots,P_6}\PP^2
$$
be the cubic surface, and put
$$
H=-K_S.
$$
If $C\subseteq S$ is the given nonsingular irreducible curve, write
$$
D=[C],
\qquad
d=H\cdot D.
$$
Adjunction gives throughout
$$
\boxed{
g
=
1+\frac{D^2-d}{2}.}
$$

::: pf

::: {.pf-step #case-c-applies}
Since $g>0$, the class $D$ is in alternative (c) of V.4.8:
$$
\boxed{
D\cdot L\ge0\text{ for every line }L,
\qquad
D^2>0.}
$$

::: pf-proof
By [[P-AGH548IRREDCLASSES]], an irreducible curve on the cubic surface is
either a line, a square-zero conic, or has the displayed properties. Lines
and conics are rational, hence have genus zero. Since $g>0$, only case (c)
can occur.
:::

:::

::: {.pf-step #contraction-preserves-invariants}
If a line $E$ satisfies
$$
D\cdot E=0,
$$
then contracting $E$ preserves the degree, self-intersection, and genus of
the curve.

::: pf-proof
Because $C$ and $E$ are distinct irreducible curves with intersection zero,
they are disjoint. Contract
$$
\sigma:X_r\longrightarrow X_{r-1}
$$
with exceptional curve $E$. Then
$$
D=\sigma^*D'
$$
for the image curve $C'$, and $C\to C'$ is an isomorphism because $C$ avoids
$E$. Thus the genus is unchanged and
$$
D^2=(D')^2.
$$

The canonical formula for a point blowup is
$$
-K_{X_r}=\sigma^*(-K_{X_{r-1}})-E.
$$
Since $D\cdot E=0$,
$$
(-K_{X_r})\cdot D
=
(-K_{X_{r-1}})\cdot D'.
$$
Thus the anticanonical degree $d$ is unchanged as well.
:::

:::

::: {.pf-step #repeat-contraction-until-x2-or-positive}
Repeat step [](#contraction-preserves-invariants){.pf-ref} while a zero-intersection line exists. The process
either reaches $X_2$, or stops on some $X_r$ with $r\ge3$ at a class,
still denoted $D$, satisfying
$$
D\cdot E>0
$$
for every $(-1)$-curve $E$.

::: pf-proof
Each contraction lowers the Picard number by one, so the process stops after
finitely many steps, on some $X_s$ with $0\le s\le6$. If $s\le2$, then $X_2$
occurs among the surfaces $X_6,X_5,\ldots,X_s$ of the process; if $s\ge3$ the
process stops on some $X_r$ with $r\ge3$. So exactly one of the two
alternatives of the step holds. Step
[](#contraction-preserves-invariants){.pf-ref} shows that $d,D^2,g$ are unchanged
throughout.

It remains to check that the descended class keeps nonnegative intersection
with every line, in the sense in which the claim speaks of $(-1)$-curves. On
$X_r$, a curve $L$ with $L^2=-1$ has $L\cdot K_{X_r}=-1$ exactly when
$p_a(L)=0$, by adjunction, so the $(-1)$-curves are the curves of
anticanonical degree $1$ and square $-1$; that is what a line on $X_r$ means,
and on $X_6$ these are the $27$ lines of the book's Theorem 4.9 (twenty-seven
lines). Let
$\sigma:X_r\to X_{r-1}$ contract the zero-intersection line $E$, let
$D=\sigma^*D'$, let $F'\subseteq X_{r-1}$ be a line and let
$F\subseteq X_r$ be its strict transform. Then
$$\sigma^*F'=F+mE$$
where $m\ge0$ is the multiplicity of $F'$ at the contracted point, hence
$$D'\cdot F'=\sigma^*D'\cdot\sigma^*F'=D\cdot F+m\,(D\cdot E)=D\cdot F,$$
because $D\cdot E=0$. Here $m=0$: if $m\ge1$ then, since
$-K_{X_r}=\sigma^*(-K_{X_{r-1}})-E$ and
$F\cdot\sigma^*(-K_{X_{r-1}})=F'\cdot(-K_{X_{r-1}})=1$, the effective curve
$F$ would have
$$F\cdot(-K_{X_r})=1-m\le0,$$
which ampleness of $-K_{X_r}$ forbids. So every line of $X_{r-1}$ is the
strict transform of a line of $X_r$, and the intersection numbers of the
descended class with the lines of the new surface are those of $D$ with the
corresponding strict transforms. Since $D\cdot L\ge0$ for all $27$ lines of
$X_6$ by step [](#case-c-applies){.pf-ref}, induction gives $D\cdot L\ge0$ for
every line $L$ of the surface on which the process stops. On that surface no
line has intersection zero, so all these intersections are positive.
:::

:::

::: {.pf-step #d-squared-bound-r-geq-3}
If the process stops on $X_r$ with $r\ge3$, then
$$
\boxed{D^2\ge2d-6.}
$$

::: pf-proof
Put
$$
A=-K_{X_r},
\qquad
A^2=9-r\le6,
\qquad
N=D-A=D+K_{X_r}.
$$
Step [](#contraction-preserves-invariants){.pf-ref} identifies $A$ with the pullback of the
hyperplane class of the cubic surface, so $d=A\cdot D$ and $A\cdot N=d-A^2$.

*$N$ is effective.* Since $A$ is ample on $X_r$ and $d=A\cdot D>0$, no
effective divisor is linearly equivalent to $-D$, so
$$
h^2\bigl(X_r,\OO_{X_r}(N)\bigr)
=
h^0\bigl(X_r,\OO_{X_r}(K_{X_r}-N)\bigr)
=
h^0\bigl(X_r,\OO_{X_r}(-D)\bigr)
=
0 .
$$
The surface $X_r$ is rational, so Riemann--Roch gives
$$
\chi\bigl(\OO_{X_r}(N)\bigr)
=
1+\frac{N\cdot(N-K_{X_r})}{2}
=
1+\frac{N\cdot D}{2}
=
1+\frac{D^2-d}{2}
=
g>0,
$$
hence $h^0(N)\ge\chi(N)-h^2(N)=g>0$: the class $N$ is effective.

*$N$ is nef.* Let $C\subseteq X_r$ be an irreducible curve with
$N\cdot C<0$. Since $N$ is effective and $C$ is irreducible, $C$ is then a
component of $N$: a curve outside $\operatorname{Supp}N$ meets every
component of $N$ nonnegatively, hence meets $N$ nonnegatively. Writing
$N=aC+N'$ with $a\ge1$ and $N'$ effective and supported away from $C$, we get
$N\cdot C=aC^2+N'\cdot C$ with $N'\cdot C\ge0$, hence $C^2<0$. Adjunction and
ampleness of $A$ give
$$
2p_a(C)-2=C^2+C\cdot K_{X_r}=C^2-C\cdot A\ge-2,
\qquad
C\cdot A\ge1,
$$
so $C^2\ge C\cdot A-2\ge-1$, and $C^2<0$ forces $C^2=-1$ and $C\cdot A=1$.
Then $p_a(C)=1+\frac12(C^2-C\cdot A)=0$, so $C$ is a $(-1)$-curve, and
$$
N\cdot C=D\cdot C-A\cdot C=D\cdot C-1\ge0
$$
by the positivity proved in step [](#repeat-contraction-until-x2-or-positive){.pf-ref},
contradicting $N\cdot C<0$. Hence $N\cdot C\ge0$ for every irreducible curve
$C$, that is, $N$ is nef.

*A nef class has nonnegative self-intersection.* For an ample class $L$ and
$\epsilon>0$ the class $N+\epsilon L$ is ample while $N\cdot L\ge0$, so
$$
0<(N+\epsilon L)^2=N^2+2\epsilon\,N\cdot L+\epsilon^2L^2
$$
for every $\epsilon>0$; letting $\epsilon\to0$ gives $N^2\ge0$.

Since
$$
d=A\cdot D=A^2+A\cdot N,
$$
one has
$$
\begin{aligned}
D^2
&=(A+N)^2\\
&=A^2+2A\cdot N+N^2\\
&=2d-A^2+N^2\\
&\ge2d-A^2\\
&\ge2d-6.
\end{aligned}
$$
:::

:::

::: {.pf-step #genus-bound-r-geq-3}
In the situation of step [](#d-squared-bound-r-geq-3){.pf-ref},
$$
g\ge\frac{d-4}{2},
$$
which is stronger than either lower bound required in the problem.

::: pf-proof
Adjunction and step [](#d-squared-bound-r-geq-3){.pf-ref} give
$$
g
=
1+\frac{D^2-d}{2}
\ge
1+\frac{(2d-6)-d}{2}
=
\frac{d-4}{2}.
$$
For even $d$ this is larger than $(d-6)/2$, and for odd $d$ it is larger
than $(d-5)/2$.
:::

:::

::: {.pf-step #x2-degree-and-square-formulas}
It remains only to analyze the case in which the contraction process
reaches
$$
X_2=\operatorname{Bl}_{P_1,P_2}\PP^2.
$$
Write
$$
D
=
c h
+
b_1(h-e_1)
+
b_2(h-e_2),
$$
with
$$
c,b_1,b_2\ge0,
$$
Put
$$
s=b_1+b_2,
\qquad
p=b_1b_2.
$$
Then
$$
\boxed{
d=3c+2s,
\qquad
D^2=c^2+2cs+2p.}
$$

::: pf-proof
On $X_2$ the classes $h$, $h-e_1$, $h-e_2$ form a basis of $\Pic X_2$, and
$$c=D\cdot(h-e_1-e_2)=D\cdot F_{12},\qquad b_i=D\cdot E_i$$
for $i=1,2$, so $c,b_1,b_2\ge0$ because $D$ meets every line nonnegatively
(step [](#repeat-contraction-until-x2-or-positive){.pf-ref}).

The anticanonical class of $X_2$ is
$$
A_2=3h-e_1-e_2.
$$
The intersection table gives
$$
A_2\cdot h=3,
\qquad
A_2\cdot(h-e_i)=2.
$$
Hence
$$
d=A_2\cdot D=3c+2b_1+2b_2=3c+2s.
$$

Also
$$
h^2=1,
\qquad
(h-e_i)^2=0,
\qquad
h\cdot(h-e_i)=1,
\qquad
(h-e_1)\cdot(h-e_2)=1.
$$
Expanding $D^2$ gives
$$
D^2=c^2+2c(b_1+b_2)+2b_1b_2
=
c^2+2cs+2p.
$$
:::

:::

::: {.pf-step #x2-genus-formula}
In the notation of step [](#x2-degree-and-square-formulas){.pf-ref}, the genus is
$$
\boxed{
g
=
1+\frac{c(c-3)}2+(c-1)s+p.}
$$

::: pf-proof
Substitute the formulas of step [](#x2-degree-and-square-formulas){.pf-ref} into adjunction:
$$
\begin{aligned}
g
&=1+\frac{D^2-d}{2}\\
&=1+
\frac{c^2+2cs+2p-(3c+2s)}2\\
&=1+\frac{c(c-3)}2+(c-1)s+p.
\end{aligned}
$$
:::

:::

::: {.pf-step #even-d-even-c}
Suppose $d$ is even. Then $c$ is even.

::: pf-proof
The formula
$$
d=3c+2s
$$
shows
$$
d\equiv c\pmod2.
$$
Thus even $d$ forces even $c$.
:::

:::

::: {.pf-step #even-c-zero-genus-formula}
If $d$ is even and $c=0$, then
$$
\boxed{
g=(b_1-1)(b_2-1).}
$$
Moreover $g>0$ forces
$$
b_1,b_2\ge2.
$$

::: pf-proof
For $c=0$, step [](#x2-genus-formula){.pf-ref} gives
$$
g=1-s+p
=
1-(b_1+b_2)+b_1b_2
=
(b_1-1)(b_2-1).
$$

Also
$$
D^2=2b_1b_2>0,
$$
so $b_1,b_2>0$. If either were $1$, the displayed genus would be zero.
Thus positive genus forces both to be at least $2$.
:::

:::

::: {.pf-step #even-c-zero-bound}
If $d$ is even, $c=0$, and $g>0$, then
$$
\boxed{g\ge\frac{d-6}{2}.}
$$

::: pf-proof
Here
$$
d=2(b_1+b_2)=2s.
$$
By step [](#even-c-zero-genus-formula){.pf-ref}, put
$$
x=b_1-1\ge1,
\qquad
y=b_2-1\ge1.
$$
Then
$$
x+y=s-2
$$
and
$$
g=xy.
$$
Since
$$
xy-(x+y-1)=(x-1)(y-1)\ge0,
$$
we obtain
$$
g\ge x+y-1=s-3
=
\frac{d-6}{2}.
$$
:::

:::

::: {.pf-step #even-c-geq-two-bound}
If $d$ is even and $c\ge2$, then again
$$
\boxed{g\ge\frac{d-6}{2}.}
$$

::: pf-proof
Subtract the desired lower bound from the genus formula. Using
$$
d=3c+2s,
$$
one finds
$$
\begin{aligned}
g-\frac{d-6}{2}
&=
4+
\frac{c(c-6)}2
+
(c-2)s
+
p.
\end{aligned}
$$

The even integer $c$ is at least $2$. If $c=2$, the right-hand side is
$$
p\ge0.
$$
If $c=4$, it is
$$
2s+p\ge0.
$$
If $c\ge6$, every displayed term is nonnegative and the constant term is
positive. Thus the difference is always nonnegative.
:::

:::

::: {.pf-step #even-d-bound-established}
Therefore, for every even
$$
d\ge8,
$$
one has
$$
\boxed{g\ge\frac{d-6}{2}.}
$$

::: pf-proof
If the contraction process stops before $X_2$, step [](#genus-bound-r-geq-3){.pf-ref} is stronger. If it
reaches $X_2$, steps [](#even-d-even-c){.pf-ref}, [](#even-c-zero-genus-formula){.pf-ref}, [](#even-c-zero-bound){.pf-ref} and [](#even-c-geq-two-bound){.pf-ref} prove the displayed inequality. This covers
every possibility.
:::

:::

::: {.pf-step #odd-d-odd-c}
Suppose $d$ is odd. Then $c$ is odd.

::: pf-proof
Again
$$
d\equiv c\pmod2
$$
by step [](#x2-degree-and-square-formulas){.pf-ref}, so odd $d$ forces odd $c$.
:::

:::

::: {.pf-step #odd-c-one-bound}
If $d$ is odd and $c=1$, then
$$
g=p=b_1b_2.
$$
Since $g>0$, one has $b_1,b_2\ge1$, and therefore
$$
\boxed{g\ge\frac{d-5}{2}.}
$$

::: pf-proof
For $c=1$, step [](#x2-genus-formula){.pf-ref} gives
$$
g=p.
$$
Positive genus therefore forces both $b_i$ to be positive. Since
$$
(b_1-1)(b_2-1)\ge0,
$$
we have
$$
p=b_1b_2\ge b_1+b_2-1=s-1.
$$
But
$$
d=3+2s,
$$
so
$$
s-1=\frac{d-5}{2}.
$$
:::

:::

::: {.pf-step #odd-c-geq-three-difference}
If $d$ is odd and $c\ge3$, then
$$
g-\frac{d-5}{2}
=
\frac72+
\frac{c(c-6)}2
+
(c-2)s
+
p.
$$

::: pf-proof
This is a direct subtraction using the formulas of steps [](#x2-degree-and-square-formulas){.pf-ref} and [](#x2-genus-formula){.pf-ref}:
$$
\frac{d-5}{2}
=
\frac{3c+2s-5}{2}.
$$
Subtracting this from
$$
1+\frac{c(c-3)}2+(c-1)s+p
$$
gives the displayed expression.
:::

:::

::: {.pf-step #odd-c-geq-three-bound}
If $d$ is odd,
$$
d\ge13,
$$
and $c\ge3$, then
$$
\boxed{g\ge\frac{d-5}{2}.}
$$

::: pf-proof
If $c=3$, then step [](#odd-c-geq-three-difference){.pf-ref} becomes
$$
g-\frac{d-5}{2}
=
s+p-1.
$$
The degree condition gives
$$
13\le d=9+2s,
$$
so $s\ge2$, and therefore the difference is nonnegative.

If $c=5$, the difference is
$$
1+3s+p>0.
$$
For every odd $c\ge7$, one has
$$
\frac{c(c-6)}2>0,
\qquad
(c-2)s\ge0,
\qquad
p\ge0,
$$
so the difference is again positive.
:::

:::

::: {.pf-step #odd-d-bound-established}
Therefore, for every odd
$$
d\ge13,
$$
one has
$$
\boxed{g\ge\frac{d-5}{2}.}
$$

::: pf-proof
The case in which the contraction process stops before $X_2$ is covered by
the stronger bound in step [](#genus-bound-r-geq-3){.pf-ref}. On $X_2$, step [](#odd-c-one-bound){.pf-ref} treats $c=1$ and step
[](#odd-c-geq-three-bound){.pf-ref} treats every odd $c\ge3$.

We now construct curves attaining equality.
:::

:::

::: {.pf-step #contraction-pullback-preserves-invariants}
Contract the four pairwise disjoint exceptional lines
$$
E_3,E_4,E_5,E_6\subseteq S.
$$
This gives a morphism
$$
\pi:S\longrightarrow X_2
=
\operatorname{Bl}_{P_1,P_2}\PP^2.
$$
If a divisor $M$ on $X_2$ has a nonsingular irreducible member avoiding the
four contraction points, its pullback is a nonsingular irreducible curve on
$S$ with the same degree and genus.

::: pf-proof
The four exceptional curves are disjoint $(-1)$-curves, so they can be
contracted successively. If a curve $C_2\in\linearsystem{M}$ avoids the four image points,
its inverse image is its strict transform and is isomorphic to $C_2$.

If $D=\pi^*M$, then $D\cdot E_i=0$ for $i=3,\ldots,6$. Applying the
canonical blowup formula four times gives
$$
H_S\cdot D
=
(-K_{X_2})\cdot M.
$$
Self-intersection is also preserved under pullback:
$$
D^2=M^2.
$$
Hence adjunction gives the same genus on both surfaces.
:::

:::

::: {.pf-step #even-equality-class}
Let $d=2s$ be even with $d\ge8$, so $s\ge4$. On $X_2$ set
$$
\boxed{
M_{\mathrm{ev}}
=
2(h-e_1)
+
(s-2)(h-e_2).}
$$
Then
$$
\deg M_{\mathrm{ev}}=d,
\qquad
g(M_{\mathrm{ev}})=\frac{d-6}{2}.
$$

::: pf-proof
This is the notation of step [](#x2-degree-and-square-formulas){.pf-ref} with
$$
c=0,
\qquad
b_1=2,
\qquad
b_2=s-2.
$$
Thus
$$
d=2(2+s-2)=2s
$$
and, by step [](#even-c-zero-genus-formula){.pf-ref},
$$
g
=(2-1)((s-2)-1)
=
s-3
=
\frac{d-6}{2}.
$$
Also
$$
M_{\mathrm{ev}}^2=4(s-2)>0.
$$
:::

:::

::: {.pf-step #even-equality-realized}
A general member of $\linearsystem{M_{\mathrm{ev}}}$ is nonsingular and
irreducible and can be chosen to avoid the four contraction points of
step [](#contraction-pullback-preserves-invariants){.pf-ref}. Its pullback to $S$ attains the even minimum.

::: pf-proof
Write
$$M_{\mathrm{ev}}=2(h-e_1)+(s-2)(h-e_2):$$
a nonnegative integral combination of $h-e_1$ and $h-e_2$, and each of
these is the class of a base-point-free pencil on $X_2$, namely the strict
transforms of the lines through $P_1$ and through $P_2$. The lemma of V.4.8
is proved for $X_2$ precisely by exhibiting classes in this form, so a
general member of $\linearsystem{M_{\mathrm{ev}}}$ is nonsingular and
irreducible, and the system is globally generated. Requiring a member to pass
through a prescribed point is then a proper hyperplane condition, so a
general smooth member avoids the four contraction points.


Step [](#contraction-pullback-preserves-invariants){.pf-ref} then pulls it back to a nonsingular irreducible curve on the cubic
surface of degree $d$ and genus
$$
\frac{d-6}{2}.
$$
:::

:::

::: {.pf-step #odd-equality-class}
Let $d=2s+3$ be odd with $d\ge13$, so $s\ge5$. On $X_2$ set
$$
\boxed{
M_{\mathrm{odd}}
=
h
+
(h-e_1)
+
(s-1)(h-e_2).}
$$
Then
$$
\deg M_{\mathrm{odd}}=d,
\qquad
g(M_{\mathrm{odd}})=\frac{d-5}{2}.
$$

::: pf-proof
Here
$$
c=1,
\qquad
b_1=1,
\qquad
b_2=s-1.
$$
Step [](#x2-degree-and-square-formulas){.pf-ref} gives
$$
d=3+2(1+s-1)=2s+3.
$$
Step [](#odd-c-one-bound){.pf-ref} gives
$$
g=b_1b_2=s-1
=
\frac{(2s+3)-5}{2}
=
\frac{d-5}{2}.
$$
The square is
$$
M_{\mathrm{odd}}^2
=
1+2s+2(s-1)
=
4s-1>0.
$$
:::

:::

::: {.pf-step #odd-equality-realized}
A general member of $\linearsystem{M_{\mathrm{odd}}}$ is nonsingular and
irreducible and can be chosen away from the four contraction points. Its
pullback to $S$ attains the odd minimum.

::: pf-proof
Again
$$M_{\mathrm{odd}}=h+(h-e_1)+(s-1)(h-e_2)$$
is a nonnegative integral combination of $h,h-e_1,h-e_2$, the three
base-point-free classes for which the $X_2$ lemma of V.4.8 is proved, and its
square is positive by step [](#odd-equality-class){.pf-ref}. V.4.8 therefore gives a general
nonsingular irreducible member and global generation. Choose such a member
outside the four hyperplanes corresponding to the contraction points, and
apply step [](#contraction-pullback-preserves-invariants){.pf-ref}.
:::

:::

::: pf-qed
Steps [](#case-c-applies){.pf-ref}, [](#contraction-preserves-invariants){.pf-ref}, [](#repeat-contraction-until-x2-or-positive){.pf-ref}, [](#d-squared-bound-r-geq-3){.pf-ref}, [](#genus-bound-r-geq-3){.pf-ref}, [](#x2-degree-and-square-formulas){.pf-ref}, [](#x2-genus-formula){.pf-ref}, [](#even-d-even-c){.pf-ref}, [](#even-c-zero-genus-formula){.pf-ref}, [](#even-c-zero-bound){.pf-ref}, [](#even-c-geq-two-bound){.pf-ref}, [](#even-d-bound-established){.pf-ref}, [](#odd-d-odd-c){.pf-ref}, [](#odd-c-one-bound){.pf-ref}, [](#odd-c-geq-three-difference){.pf-ref}, [](#odd-c-geq-three-bound){.pf-ref} and [](#odd-d-bound-established){.pf-ref} prove the lower bounds. Steps [](#contraction-pullback-preserves-invariants){.pf-ref}, [](#even-equality-class){.pf-ref} and [](#even-equality-realized){.pf-ref} construct an
equality curve for every even $d\ge8$, and steps [](#odd-equality-class){.pf-ref} and [](#odd-equality-realized){.pf-ref} construct one
for every odd $d\ge13$.
:::

:::
:::

::: {.remark title="Published solution"}
The published proof is L. Gruson and C. Peskine, *Genre des courbes de l'espace projectif. II*, Ann. Sci. École Norm. Sup. (4) **15** (1982), 401--418, read in the text version `tmp/sources/gruson-peskine-1982-genre-courbes-espace-projectif-ii.md`. For a class on a smooth cubic surface they set $d=-C\cdot K_S$, $r=d-\max\{C\cdot E: E^2=E\cdot K_S=-1\}$ and $F_d(r)=1+\frac12\bigl((r-1)d-\frac34r^2\bigr)$. Proposition 2.1, statement on printed p. 407, is the existence half: for integers $0\le r\le 2d/3$ and $g$ with $F_d(r-1)<g\le F_d(r)$ such that $8(F_d(r)-g)$ is a sum of squares of five integers of one parity and of absolute value at most $r$, there is a nonsingular connected curve of degree $d$ and genus $g$ on $S$. Theorem 2.5, statement on printed p. 409, is the converse, so the two decide every pair $(d,g)$ with $g\le1+d(d-3)/6$, the printed exceptions being $(d,g,r)=(9,1,2)$, $(23,22,4)$ and $(27,28,4)$. The five integers of the criterion are read as nonnegative: the proof of 2.1 runs with $0\le\alpha_i\le r/2$ in the even case, where the five entries are $2\alpha_i$ and may vanish, and with five odd $\beta_i$ of absolute value at most $r$ in the odd case.

Both halves of the exercise are the case $r=2$. Since $F_d(1)=5/8$, a genus $g>0$ has $r\ge2$; and if $g\le F_d(2)=(d-1)/2$, the criterion reads $8(F_d(2)-g)=4\bigl((d-1)-2g\bigr)$ as a sum of five squares drawn from $\{0,4\}$, so $(d-1)-2g\in\{0,\dots,5\}$ and $g\in\{(d-1)/2-j/2\}$. For even $d$ only $j=1,3,5$ give an integer, so the genera at most $(d-1)/2$ are $(d-2)/2$, $(d-4)/2$ and $(d-6)/2$, the least of which Proposition 2.1 attains with $(2,2,2,2,2)$; for odd $d$ only $j=0,2,4$ do, giving $(d-1)/2$, $(d-3)/2$ and $(d-5)/2$, the last attained with $(2,2,0,0,0)$. A genus above $F_d(2)$ is at least $\lfloor(d-1)/2\rfloor+1$, which already exceeds both bounds. So (2.5) gives the lower bound for every even $d\ge8$ and every odd $d\ge13$, and (2.1) the attainment; of the three exceptional triples only $(9,1,2)$ lies below $F_d(2)$, at the odd degree $9$ that the printed range excludes. The table on printed p. 411 is the independent check: its rows begin at $d=10$ --- no degree at most $9$ has a gap --- and in each of the $32$ rows the column headed $F_d(2)$ reads $\{1,\dots,(d-6)/2-1\}$ for even $d$ and $\{1,\dots,(d-5)/2-1\}$ for odd $d$, which leaves the bound itself as the least genus.

R. Hartshorne, *Genre des courbes algébriques dans l'espace projectif [d'après L. Gruson et C. Peskine]*, Séminaire Bourbaki exposé 592, Astérisque **92--93** (1982), 301--313, text version `tmp/sources/hartshorne-1982-genre-courbes-bourbaki-592.md`, treats a different question and does not close the exercise. Theorem 0.1, printed pp. 301--302, classifies the pairs $(d,g)$ of a curve in $\PP^3$ according to the surface containing it, and Theorem 0.2, printed p. 302, produces a curve of degree $d$ and genus $g$ on a smooth cubic surface only for $g>\frac{1}{\sqrt3}d^{3/2}-d+1$, which for $d\ge10$ exceeds $(d-6)/2$: it says nothing about the bottom of the range, where the exercise's minimum sits. What it supplies is the framework. Its §1, beginning on printed p. 302, quotes the class criterion of Hartshorne V.4.12 and Ex. V.4.8 in the form $a\ge b_1+b_2+b_3$, $b_1\ge\cdots\ge b_6\ge0$ imply an irreducible nonsingular member, except for the classes $(n;n,0,\dots,0)$ with $n>1$, which is what step [](#contraction-pullback-preserves-invariants){.pf-ref} and the equality constructions use; and Remark 2 on printed p. 302 states that the converse of its Lemma 1.1 is what computes the list of gaps for a given degree, and that converse is (2.5). Its §5 records that Gruson and Peskine assumed characteristic $0$ in order to apply Bertini, and supplies a characteristic-free substitute, Theorem 5.1. The lower bound above uses no Bertini and so holds in every characteristic; the attainment in characteristic $p$ would rest on that theorem, and the sources read here do not carry it out in this setting. Hartshorne's standing convention is that a variety is over an algebraically closed field, with no characteristic fixed, which is the setting of the exercise.

The proof above is independent of both articles: it contracts the zero-intersection lines to $X_2$, applies Ex. V.4.8 on $X_r$ for $r\ge3$ and on $X_2$, and exhibits the equality curves as explicit classes on $X_2$ pulled back to $X_6$. It uses neither the invariant $r$, nor the five-squares criterion, nor the table.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, V.4.9, printed p. 290, is a working draft and not a proof: its lower-bound half is a chain of unattributed algebraic manipulations that does not close, and its existence half fixes $b_6^2=3$ and then applies the five-squares lemma of Bourbaki's Proposition 2.1 with $k=a$, which does not respect the degree $d=3a-\sum b_i$ that it is meant to realize.
:::
