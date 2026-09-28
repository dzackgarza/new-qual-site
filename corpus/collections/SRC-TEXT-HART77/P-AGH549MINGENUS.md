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
    positive, writing D=-K+N with N globally generated gives the stronger
    estimate D^2>=2d-6. If the contraction reaches
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
---

::: {.problem}
If $C$ is an irreducible non-singular curve of degree $d$ on the cubic surface, and if the genus $g>0$, then
\[
g \geqslant \begin{cases}\frac{1}{2}(d-6) & \text { if } d \text { is even, } d \geqslant 8 \\ \frac{1}{2}(d-5) & \text { if } d \text { is odd }, d \geqslant 13\end{cases}
\]
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

<1>1. Since $g>0$, the class $D$ is in alternative (c) of V.4.8:
$$
\boxed{
D\cdot L\ge0\text{ for every line }L,
\qquad
D^2>0.}
$$

::: {.proof}
By [[P-AGH548IRREDCLASSES]], an irreducible curve on the cubic surface is
either a line, a square-zero conic, or has the displayed properties. Lines
and conics are rational, hence have genus zero. Since $g>0$, only case (c)
can occur.
:::

<1>2. If a line $E$ satisfies
$$
D\cdot E=0,
$$
then contracting $E$ preserves the degree, self-intersection, and genus of
the curve.

::: {.proof}
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

<1>3. Repeat step <1>2 while a zero-intersection line exists. The process
either reaches $X_2$, or stops on some $X_r$ with $r\ge3$ at a class,
still denoted $D$, satisfying
$$
D\cdot E>0
$$
for every $(-1)$-curve $E$.

::: {.proof}
Each contraction lowers the Picard number by one, so after at most four
contractions either the degree-seven del Pezzo $X_2$ is reached or there is
no line of intersection zero. The preceding step shows that the numerical
quantities $d,D^2,g$ are unchanged throughout.

The argument in V.4.8 also shows that after each contraction the descended
class remains nonnegative on every $(-1)$-curve of the new del Pezzo
surface. Hence, if the process stops before $X_2$, all these intersections
are positive integers.
:::

<1>4. If the process stops on $X_r$ with $r\ge3$, then
$$
\boxed{D^2\ge2d-6.}
$$

::: {.proof}
Put
$$
A=-K_{X_r},
\qquad
A^2=9-r\le6.
$$
All intersections $D\cdot E$ with $(-1)$-curves are positive, so
$$
N=D-A
$$
is nonnegative on every $(-1)$-curve. By the global-generation lemma proved
in [[P-AGH548IRREDCLASSES]], $N$ is globally generated. In particular it is
nef, so
$$
N^2\ge0.
$$
Indeed, if $N\not\sim0$, choose two general effective members of $|N|$ with
no common irreducible component; their intersection number is $N^2\ge0$.
If $N\sim0$, the same inequality is immediate.

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

<1>5. In the situation of step <1>4,
$$
g\ge\frac{d-4}{2},
$$
which is stronger than either lower bound required in the problem.

::: {.proof}
Adjunction and step <1>4 give
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

<1>6. It remains only to analyze the case in which the contraction process
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
as in V.4.8. Put
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

::: {.proof}
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

<1>7. In the notation of step <1>6, the genus is
$$
\boxed{
g
=
1+\frac{c(c-3)}2+(c-1)s+p.}
$$

::: {.proof}
Substitute the formulas of step <1>6 into adjunction:
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

<1>8. Suppose $d$ is even. Then $c$ is even.

::: {.proof}
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

<1>9. If $d$ is even and $c=0$, then
$$
\boxed{
g=(b_1-1)(b_2-1).}
$$
Moreover $g>0$ forces
$$
b_1,b_2\ge2.
$$

::: {.proof}
For $c=0$, step <1>7 gives
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

<1>10. If $d$ is even, $c=0$, and $g>0$, then
$$
\boxed{g\ge\frac{d-6}{2}.}
$$

::: {.proof}
Here
$$
d=2(b_1+b_2)=2s.
$$
By step <1>9, put
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

<1>11. If $d$ is even and $c\ge2$, then again
$$
\boxed{g\ge\frac{d-6}{2}.}
$$

::: {.proof}
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

<1>12. Therefore, for every even
$$
d\ge8,
$$
one has
$$
\boxed{g\ge\frac{d-6}{2}.}
$$

::: {.proof}
If the contraction process stops before $X_2$, step <1>5 is stronger. If it
reaches $X_2$, steps <1>8--<1>11 prove the displayed inequality. This covers
every possibility.
:::

<1>13. Suppose $d$ is odd. Then $c$ is odd.

::: {.proof}
Again
$$
d\equiv c\pmod2
$$
by step <1>6, so odd $d$ forces odd $c$.
:::

<1>14. If $d$ is odd and $c=1$, then
$$
g=p=b_1b_2.
$$
Since $g>0$, one has $b_1,b_2\ge1$, and therefore
$$
\boxed{g\ge\frac{d-5}{2}.}
$$

::: {.proof}
For $c=1$, step <1>7 gives
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

<1>15. If $d$ is odd and $c\ge3$, then
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

::: {.proof}
This is a direct subtraction using the formulas of steps <1>6--<1>7:
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

<1>16. If $d$ is odd,
$$
d\ge13,
$$
and $c\ge3$, then
$$
\boxed{g\ge\frac{d-5}{2}.}
$$

::: {.proof}
If $c=3$, then step <1>15 becomes
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

<1>17. Therefore, for every odd
$$
d\ge13,
$$
one has
$$
\boxed{g\ge\frac{d-5}{2}.}
$$

::: {.proof}
The case in which the contraction process stops before $X_2$ is covered by
the stronger bound in step <1>5. On $X_2$, step <1>14 treats $c=1$ and step
<1>16 treats every odd $c\ge3$.
:::

We now construct curves attaining equality.

<1>18. Contract the four pairwise disjoint exceptional lines
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

::: {.proof}
The four exceptional curves are disjoint $(-1)$-curves, so they can be
contracted successively. If a curve $C_2\in|M|$ avoids the four image points,
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

<1>19. Let $d=2s$ be even with $d\ge8$, so $s\ge4$. On $X_2$ set
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

::: {.proof}
This is the notation of step <1>6 with
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
and, by step <1>9,
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

<1>20. A general member of $|M_{\mathrm{ev}}|$ is nonsingular and
irreducible and can be chosen to avoid the four contraction points of
step <1>18. Its pullback to $S$ attains the even minimum.

::: {.proof}
The class $M_{\mathrm{ev}}$ is nonnegative on the three $(-1)$-curves of
$X_2$ and has positive square. By the lemma of V.4.8, a general member is
nonsingular and irreducible. The same lemma makes the system globally
generated, so requiring a member to pass through any one prescribed point is
a proper hyperplane condition. Hence a general smooth member avoids the four
contraction points.

Step <1>18 then pulls it back to a nonsingular irreducible curve on the cubic
surface of degree $d$ and genus
$$
\frac{d-6}{2}.
$$
:::

<1>21. Let $d=2s+3$ be odd with $d\ge13$, so $s\ge5$. On $X_2$ set
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

::: {.proof}
Here
$$
c=1,
\qquad
b_1=1,
\qquad
b_2=s-1.
$$
Step <1>6 gives
$$
d=3+2(1+s-1)=2s+3.
$$
Step <1>14 gives
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

<1>22. A general member of $|M_{\mathrm{odd}}|$ is nonsingular and
irreducible and can be chosen away from the four contraction points. Its
pullback to $S$ attains the odd minimum.

::: {.proof}
Again the coefficients
$$
c=1,
\qquad
b_1=1,
\qquad
b_2=s-1
$$
are nonnegative, so the class is nonnegative on every $(-1)$-curve of
$X_2$. Its square is positive by step <1>21. V.4.8 therefore gives a general
nonsingular irreducible member and global generation. Choose such a member
outside the four hyperplanes corresponding to the contraction points, and
apply step <1>18.
:::

<1>23. Q.E.D.

::: {.proof}
Steps <1>1--<1>17 prove the lower bounds. Steps <1>18--<1>20 construct an
equality curve for every even $d\ge8$, and steps <1>21--<1>22 construct one
for every odd $d\ge13$.
:::
:::
