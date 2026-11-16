---
schema: qual/card@1
id: P-AGH56BLOWUPSING
kind: problem
title: Resolving nodes, tacnodes, and the cusp $y^3 = x^5$ by blowing up
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowing Up
  - Singularities
  - Plane Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all four parts with the retained Hartshorne I.5.6 transcription. The affine blowup-chart calculations prove the node, tacnode, and higher-cusp assertions directly. The solution also records the characteristic-7 and characteristic-13 exception inherited from I.5.1(c): blowing up only O cannot remove those additional singular points.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read Vakil, Foundations of Algebraic Geometry (Math 216 classes 49-50),
    Section 5.2, printed p. 9, the only published treatment of the nodal
    blow-up located outside the retained sets: it factors the strict
    transform, records the two points s=+-1 and leaves nonsingularity as an
    exercise, and prints 1-s^2-y^3 where substituting x=ys into y^2=x^3+x^2
    gives 1-s^2-ys^3. Rechecked the card's general node argument
    f=xy+f_3+... on both charts: the strict transform is t+x f_3(1,t)+...,
    its only exceptional point is t=0, and the derivative in t is 1.
    Rechecked the characteristic 7 and 13 claim inherited from I.5.1(c):
    with f=x^3-y^2-x^4-y^4 the remaining singular point needs x=3/4,
    y^2=-1/2 and 91/256=0, and 91=7.13.

- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), I.5.6(b),
    printed p. 37. Published treatment of the node located outside the twelve
    retained sets: A. Shichijo, R.Hartshorne "Algebraic Geometry" 演習問題への
    解答 (2020/March), Chapter 1 section 5, Exercise 5.6(b), printed p. 5 (not
    p. 4, which holds Exercise 5.5 and the start of 5.6), read in the MinerU
    extraction tmp/sources/shitijyou-ch1-section5.md. The source writes the node
    as f_2 = (ax-by)(cx-dy) with ad-bc != 0, gives the strict transforms on both
    charts V_0: y = vx and V_1: x = uy, records the two points
    P_1 = (0,0)x(b:a), P_2 = (0,0)x(d:c) of the exceptional divisor, and computes
    the Jacobian of Y-tilde cap V_0 at a point of E as a 2x3 matrix whose 2x2
    minor is nonvanishing because the entry 2bdv-(ad+bc) takes the values ad-bc
    and bc-ad at v = a/b and v = c/d. Two limits of that computation: the V_0
    chart displays P_1 and P_2 only when b, d != 0, since their second
    homogeneous coordinate is v = a/b resp. v = c/d, and the source omits the
    V_1 chart computation as similar -- so one of the two points is unchecked
    when b = 0 or d = 0. The card's step general-node-two-points transcribes the
    source's V_0 computation and supplies V_1, where the corresponding entry is
    2acu-(ad+bc). Checked against the book: (b) asks only for the two nonsingular
    points above the node, which is what is proved; no characteristic hypothesis
    enters, the two tangent directions being distinct by ad-bc != 0.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Step general-node-two-points is now the transcription of Shichijo's Exercise
    5.6(b), printed p. 5, in his general form (a,b,c,d) instead of the card's
    normalized form xy + f_3 + ..., with the citation on the step; the V_1 chart,
    which the source omits and which is needed when b = 0 or d = 0, is supplied
    there and marked as the card's. Steps for parts (a), (c) and (d) keep the
    card's chart computations, which agree with the same page.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Two statements of the event above were incomplete and are corrected here.
    (1) The card's step writes the Jacobian of Y-tilde cap V_0 as computed, with
    the row (-v, 1, -x) for the chart equation y - vx, while the source prints
    the row (0, -v, 0) there -- the partial derivative in y is printed as 0. The
    step now says so, and says why the rank conclusion is unaffected: on E the
    entry -x is 0, the source's sum restricted to i+j=3 is the first column at
    x=0, and the deciding minor is the one in the last two columns, which is
    -v(2bdv-(ad+bc)) from the printed matrix and -(2bdv-(ad+bc)) from the
    computed one, both nonzero at the two points. (2) The V_1 chart is not
    coordinatized by (y, u) alone: x = uy there, and the Jacobian is 2x3 in the
    ambient coordinates (x, y, u) of the blown-up surface, as on V_0 the columns
    are (x, y, v). The step said "with coordinates (y,u)" and now names the
    columns. Both readings were checked against printed p. 5 in
    pdftotext -layout -f 5 -l 5 of tmp/sources/shitijyou-ch1-section5.pdf, which
    prints the matrix and both strict transforms.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Correction, on a reader's report of issue #121: the event above said the
    printed Jacobian's missing 1 "does not affect the rank conclusion", and that
    the deciding minor is nonzero "from the printed matrix". Both are false at
    v = 0. The source orders its columns (y, x, v) and prints the chart-equation
    row of J_0 as (0, -v, 0), where the derivatives of y - vx in that order are
    (1, -v, -x); at v = 0 the whole printed row is zero, so the printed matrix
    has rank at most one there, and its minor in the last two columns,
    -v(2bdv-(ad+bc)), vanishes with it. The point with v = 0 is P_1 when a = 0
    and P_2 when c = 0, and only one of the two can occur there, since a = c = 0
    makes P_1 = (b:0) and P_2 = (d:0) coincide; for the node xy written at
    (a,b,c,d) = (0,1,-1,0) it is P_1 that has v = 0 and P_2 that has
    v = c/d = infinity. So the printed rank-two
    claim needs the missing 1. The step now records the source's column order and
    its second row (0, sum_{i+j=3}(i+j-2)c_ij v^j, 2bdv-(ad+bc)), which is the
    computed one, and takes the deciding minor from the computed matrix. Read in
    tmp/sources/shitijyou-ch1-section5.md at "Ex5.6 (b) Blowing Up at a Node",
    which prints J_0 as those two rows.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Correction on a reader's report of issue #121: at v = 0 the printed matrix
    has rank exactly one, not "at most one". The printed row (0,-v,0) is zero
    there, but the second row (0, sum_{i+j=3}(i+j-2)c_ij v^j, 2bdv-(ad+bc)) keeps
    its last entry -(ad+bc) at v = 0, and the points of E with v = 0 are those
    where (a-bv)(c-dv) vanishes, that is a = 0 or c = 0, where -(ad+bc) is -bc
    resp. -ad and in either case nonzero because ad - bc != 0. So the printed
    matrix has rank one and not the two the argument needs; what the printed row
    omits is the entry 1 alone, the printed 0 in place of -x being the value
    x = 0 on E. The step now says that instead of "rank at most one".
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Correction, on a reader's report of issue #121: the event above said of the
    point v = 0 that it is P_1 when a = 0 and P_2 when c = 0 "and both occur
    for the node xy", and the step said the same. They cannot both occur: a = 0
    and c = 0 together make P_1 = (b:0) and P_2 = (d:0) one point. For the node
    xy at (a,b,c,d) = (0,1,-1,0) it is P_1 = (1:0) that has v = a/b = 0 and
    P_2 = (0:1) that has v = c/d = infinity, so the printed row is zero at one
    of the two points. Both the event and the step now say that; the rank
    conclusion, rank one on E cap Y-tilde at the point with v = 0, is unchanged.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the quoted passage this pass. Printed exercise read: Hartshorne,
    Algebraic Geometry (1977), I.5.6(b), printed p. 37 (PDF p. 52 of the
    extraction). Shichijo, Chapter 1 section 5, Exercise 5.6(b), printed p. 5,
    read in tmp/sources/shitijyou-ch1-section5.md: his f_2 = (ax - by)(cx - dy)
    with ad - bc != 0, the two strict transforms on V_0 = {y = vx} and
    V_1 = {x = uy}, the two points P_1 = (0,0) x (b:a) and P_2 = (0,0) x (d:c) of
    E, the matrix J_0((0,0) x (u:v)) = [[0, -v, 0], [0, sum_{i+j=3}(i+j-2)c_ij
    v^j, 2bdv - (ad+bc)]], and his values of 2bdv - (ad+bc) at P_1 and P_2,
    which are +-(ad-bc). Confirmed the three limits the card records: his V_0
    chart displays both points only when b, d != 0; he omits V_1 ("同様なので略す");
    and the printed first row (0, -v, 0) is not the derivative of the chart
    equation y - vx in his column order (y, x, v), whose derivatives are
    (1, -v, -x). The card's step computes the matrix and takes the deciding
    minor from it; the V_1 chart is the card's.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The local reader's report; the mathematics accepted, three citations
    repaired. Recomputed both Jacobians from the card rather than from the
    source's print: on V_0 the minor in the last two columns is
    -(2bdv - (ad+bc)), taking the values -(ad-bc) at P_1 = (0,0) x (b:a) and
    +(ad-bc) at P_2 = (0,0) x (d:c); on V_1 the entry 2acu - (ad+bc) takes the
    values -(ad-bc) at u = b/a and +(ad-bc) at u = d/c; and the printed row
    (0,-v,0) has rank exactly one at v = 0, as the card says. Repairs: the
    Shichijo citations in the step and in the remark name the
    text version tmp/sources/shitijyou-ch1-section5.md. Of the reader's two
    Vakil items, one is false of this file: the remark at the end has named both
    tmp/sources/vakil-216-class49-50.pdf and its text version since it was
    written. The other is right in substance and wrong in detail: the note of
    2026-11-11 names no Vakil file at all, and the Math 216 classes 49-50 notes
    are tmp/sources/vakil-216-class49-50.pdf, text version
    tmp/sources/vakil-216-class49-50.md, whose line 217 carries the quoted
    factor 1 - s^2 - y^3 and the two points s = +-1; named here rather than
    inserted into the dated note.

---

::: {.problem}
(a) Let $Y$ be the cusp or node of [[P-AGH51PLANECURVESING]].
Show that the curve $\tilde{Y}$ obtained by blowing up $Y$ at $O = (0,0)$ is nonsingular (cf. (4.9.1) and (Ex. 4.10)).

(b) We define a \dfn{node} (also called \dfn{ordinary double point}) to be a double point (i.e., a point of multiplicity $2$) of a plane curve with distinct tangent directions ([[P-AGH53MULTIPLICITY]]).
If $P$ is a node on a plane curve $Y$, show that $\varphi^{-1}(P)$ consists of two distinct nonsingular points on the blown-up curve $\tilde{Y}$.
We say that "blowing up $P$ resolves the singularity at $P$".

(c) Let $P \in Y$ be the tacnode of [[P-AGH51PLANECURVESING]].
If $\varphi: \tilde{Y} \to Y$ is the blowing-up at $P$, show that $\varphi^{-1}(P)$ is a node.
Using (b) we see that the tacnode can be resolved by two successive blowings-up.

(d) Let $Y$ be the plane curve $y^3 = x^5$, which has a "higher order cusp" at $O$.
Show that $O$ is a triple point; that blowing up $O$ gives rise to a double point (what kind?) and that one further blowing up resolves the singularity.

Note: We will see later (V, 3.8) that any singular point of a plane curve can be resolved by a finite sequence of successive blowings-up.
:::

::: {.solution}
For the blowup of $\AA^2$ at the origin, use homogeneous coordinates $[u:v]$ on the exceptional $\PP^1$ and the equation
$$
xv=yu.
$$
On the chart $u\ne0$, put $t=v/u$, so $y=xt$.
On the chart $v\ne0$, put $s=u/v$, so $x=ys$.
For a curve of multiplicity $m$ at the origin, substituting in either chart produces a factor $x^m$ or $y^m$; removing that exceptional factor gives the strict-transform equation.

::: pf

::: {.pf-step #node-blowup-separates-branches}
Blowing up the node
$$
xy=x^6+y^6
$$
separates its two branches into two nonsingular points above the origin.

::: pf-proof
On the chart $y=xt$, the equation becomes
$$
x^2t=x^6+x^6t^6,
$$
so the strict transform is
$$
h(x,t)=t-x^4(1+t^6)=0.
$$
On the exceptional divisor $x=0$, this gives $t=0$.
At $(0,0)$ one has
$$
h_t=1,
$$
so this point of the strict transform is nonsingular.

On the other chart, $x=ys$, the same calculation gives
$$
s-y^4(1+s^6)=0,
$$
with the unique exceptional point $(y,s)=(0,0)$, again nonsingular because the derivative with respect to $s$ is $1$ there.
The two points are distinct points of the exceptional $\PP^1$: they are $[u:v]=[1:0]$ and $[0:1]$, corresponding to the two tangent directions $y=0$ and $x=0$.
Away from the exceptional divisor the blowup is an isomorphism, and [[P-AGH51PLANECURVESING]] shows that the original node curve has no other singular point.
Thus its strict transform is nonsingular.
:::

:::

::: {.pf-step #cusp-quartic-blowup-nonsingular}
Blowing up the cusp at the origin of
$$
x^3=y^2+x^4+y^4
$$
gives a nonsingular point above the cusp.

::: pf-proof
The tangent direction is $y=0$, so use $y=xt$.
Substitution gives
$$
x^3=x^2t^2+x^4+x^4t^4,
$$
and after removing the factor $x^2$ the strict transform is
$$
h(x,t)=x-t^2-x^2(1+t^4)=0.
$$
Its intersection with the exceptional divisor $x=0$ is the single point $t=0$.
On the other chart, $x=ys$, the strict transform is $ys^3=1+y^2(1+s^4)$, which does not meet $y=0$.
At this point
$$
h_x=1,
$$
so the strict transform is nonsingular there.

Outside the exceptional divisor the blowup is an isomorphism.
Hence the whole strict transform is nonsingular whenever the original curve has no other singular points, in particular in characteristic zero and in every characteristic other than $2,7,13$ by [[P-AGH51PLANECURVESING]].
In characteristics $7$ and $13$, the two additional singular points found on that card lie away from the origin and remain singular after this blowup.
:::

:::

::: {.pf-step #general-node-two-points}
More generally, blowing up any node produces two distinct nonsingular points above it.

::: pf-proof
This is A. Shichijo's argument, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (Solutions to the exercises in Hartshorne's *Algebraic Geometry*), 2020/March version, <https://shitijyou-a.github.io/math/alg-geo/har-ag-solutions/>, Chapter 1 section 5, Exercise 5.6(b), printed p. 5, read in `tmp/sources/shitijyou-ch1-section5.md`, the MinerU extraction of `tmp/sources/shitijyou-ch1-section5.pdf`, transcribed, with the second chart supplied at the end.

Translate the node to the origin $O=(0,0)$.
A node is a double point whose lowest homogeneous part is a product of two distinct linear forms, so
$$
f_2=(ax-by)(cx-dy),\qquad \det\begin{pmatrix}a&b\\ c&d\end{pmatrix}=ad-bc\ne0,
$$
the nonvanishing of the determinant being exactly the statement that the two lines are distinct; write
$$
f=(ax-by)(cx-dy)+\sum_{i+j>2}c_{ij}x^iy^j .
$$

On the chart $V_0=\theset{y=vx}$ of the blowup of $\AA^2$ at $O$ the strict transform is
$$
\tilde Y\cap V_0=Z_a\Big((a-bv)(c-dv)+\sum_{i+j>2}c_{ij}v^jx^{i+j-2},\ y-vx\Big),
$$
and on the chart $V_1=\theset{x=uy}$ it is
$$
\tilde Y\cap V_1=Z_a\Big((au-b)(cu-d)+\sum_{i+j>2}c_{ij}u^iy^{i+j-2},\ uy-x\Big).
$$

On $V_0$, with coordinates $(x,y,v)$, the exceptional divisor is $E=\theset{x=0}$ and the two defining equations have Jacobian
$$
\begin{pmatrix}
\sum_{i+j>2}(i+j-2)c_{ij}v^jx^{i+j-3} & 0 & 2bdv-(ad+bc)\\
-v & 1 & -x
\end{pmatrix},
$$
whose first row is the derivative of the strict-transform equation and takes the entry $2bdv-(ad+bc)$ on $E$, and whose second row is the derivative of the chart equation and is nonzero on $E$.

The source prints this matrix in the column order $(y,x,v)$: its second row there is $(0,\sum_{i+j=3}(i+j-2)c_{ij}v^j,2bdv-(ad+bc))$, the derivative of the strict-transform equation read in that order, and its first row, for the chart equation $y-vx$, is $(0,-v,0)$ where the derivatives in that order are $(1,-v,-x)$ --- the $1$ and the $-x$ are missing.
The missing $-x$ is harmless, being $0$ on $E$; only the missing $1$ is not, and the rank-two claim needs it at the point where $v=0$: there the printed row $(0,-v,0)$ is the zero row, so the printed matrix has rank exactly one, and its minor in the last two columns $-v\bigl(2bdv-(ad+bc)\bigr)$ vanishes with it. It is exactly one and not zero because the second row keeps the entry $2bdv-(ad+bc)$, which at $v=0$ is $-(ad+bc)$: the strict transform meets $E$ at $v=0$ only where $(a-bv)(c-dv)=0$, that is where $a=0$ or $c=0$, and then $-(ad+bc)$ is $-bc\ne0$ or $-ad\ne0$ because $ad-bc\ne0$.
That point is $P_1$ when $a=0$ and $P_2$ when $c=0$, and the two cannot both happen, since $a=c=0$ would make $P_1=(b:0)$ and $P_2=(d:0)$ the same point. For a node whose two tangent lines are the coordinate axes, $f_2=(ax-by)(cx-dy)$ is $xy$ at $(a,b,c,d)=(0,1,-1,0)$, where $P_1=(1:0)$ has $v=a/b=0$ and $P_2=(0:1)$, the other point, has $v=c/d=\infty$.
With the $1$ restored, the minor in the last two columns is $-\bigl(2bdv-(ad+bc)\bigr)$, nonzero at $P_1$ and $P_2$ by the computation below, so the computed matrix has rank two at both points; the source's conclusion follows only with that entry supplied.
The strict transform meets $E$ where $(a-bv)(c-dv)=0$, that is at the points
$$
P_1=(0,0)\times(b:a),\qquad P_2=(0,0)\times(d:c)
$$
of $E\cong\PP^1$, and at those points the entry takes the values
$$
2bd\cdot\tfrac ab-(ad+bc)=ad-bc\ne0,\qquad
2bd\cdot\tfrac cd-(ad+bc)=-(ad-bc)\ne0 .
$$
So the Jacobian has rank two at both points, and $\tilde Y\cap V_0$ is nonsingular at $P_1$ and $P_2$.

The source remarks that the computation on $V_1$ is similar and omits it; that chart is needed, because $P_1$ and $P_2$ have $v=a/b$ and $v=c/d$ and so are not points of $V_0$ when $b=0$ or $d=0$. The computation is the card's, and it is the same one: on $V_1$, where $x=uy$, the exceptional divisor is $y=0$ and the Jacobian is taken in the three ambient coordinates $(x,y,u)$ of the blown-up $\AA^2\times\PP^1$; the strict transform meets $y=0$ where $(au-b)(cu-d)=0$, and the Jacobian
$$
\begin{pmatrix}
0 & \sum_{i+j>2}(i+j-2)c_{ij}u^iy^{i+j-3} & 2acu-(ad+bc)\\
-1 & u & y
\end{pmatrix}
$$
has rank two there because $2acu-(ad+bc)$ takes the values $-(ad-bc)\ne0$ at $u=b/a$ and $ad-bc\ne0$ at $u=d/c$.

These are the two different points of $E\cong\PP^1$ determined by the two distinct tangent lines, and there are no other points over $P$: away from $E$ the blowup is an isomorphism.
Therefore
$$
\boxed{\varphi^{-1}(P)=\{P_1,P_2\}}
$$
with both $P_i$ nonsingular on the strict transform, proving part (b).
:::

:::

::: {.pf-step #tacnode-blowup-gives-node}
Blowing up the tacnode
$$
x^2=x^4+y^4
$$
once produces a node.

::: pf-proof
The tacnode has double tangent line $x=0$, so use the chart $x=ys$.
The equation becomes
$$
y^2s^2=y^4s^4+y^4.
$$
After removing the exceptional factor $y^2$, the strict transform is
$$
h(y,s)=s^2-y^2(s^4+1)=0.
$$
Its intersection with the exceptional divisor $y=0$ is the single point $s=0$.
On the other chart, $y=xt$, the strict transform is $1=x^2(1+t^4)$, which does not meet $x=0$.
The lowest-degree homogeneous part of $h$ at that point is
$$
s^2-y^2=(s-y)(s+y).
$$
Because the tacnode exercise assumes $\operatorname{char}k\ne2$, these are two distinct tangent directions.
The point therefore has multiplicity two and distinct tangents: it is a node.
Step [](#general-node-two-points){.pf-ref} shows that one further blowup resolves it.
This proves part (c).
:::

:::

::: {.pf-step #cusp-y3x5-first-blowup}
The origin of
$$
Y=V(y^3-x^5)
$$
has multiplicity three, and its first blowup produces an ordinary cusp.

::: pf-proof
The first nonzero homogeneous part of $y^3-x^5$ is $y^3$, so
$$
\boxed{\mu_O(Y)=3.}
$$
Its unique tangent direction is $y=0$.
Use the chart $y=xt$.
Then
$$
y^3-x^5=x^3t^3-x^5=x^3(t^3-x^2),
$$
so the strict transform is
$$
t^3=x^2.
$$
It meets the exceptional divisor $x=0$ only at $(x,t)=(0,0)$.
On the other chart, $x=ys$, the strict transform is $1=y^2s^5$, which does not meet $y=0$.
The lowest-degree term there is $-x^2$, so the new point has multiplicity two and a double tangent.
Its equation is the ordinary cusp form
$$
x^2=t^3.
$$
Thus the triple point becomes a cuspidal double point after one blowup.
:::

:::

::: {.pf-step #cusp-y3x5-second-blowup}
A second blowup resolves the cusp from step [](#cusp-y3x5-first-blowup){.pf-ref}.

::: pf-proof
For the cusp $t^3=x^2$, the tangent line is $x=0$.
On the blowup chart adapted to that tangent, put
$$
x=ts.
$$
Then
$$
t^3-x^2=t^3-t^2s^2=t^2(t-s^2).
$$
After removing the exceptional factor, the strict transform is
$$
t=s^2.
$$
On the other chart, $t=xw$, the strict transform is $xw^3=1$, which does not meet $x=0$.
This is nonsingular everywhere; at its unique exceptional point $(t,s)=(0,0)$ the derivative of $t-s^2$ with respect to $t$ is $1$.
Away from that point the blowup is an isomorphism and the preceding strict transform had no other singular point.
Hence the second blowup resolves the singularity, completing part (d).
:::

:::

::: pf-qed
Steps [](#node-blowup-separates-branches){.pf-ref} and [](#cusp-quartic-blowup-nonsingular){.pf-ref} establish the requested explicit node and cusp calculations in part (a), with the necessary characteristic qualification for the cusp quartic.
Step [](#general-node-two-points){.pf-ref} proves the general node statement in part (b), step [](#tacnode-blowup-gives-node){.pf-ref} proves part (c), and steps [](#cusp-y3x5-first-blowup){.pf-ref} and [](#cusp-y3x5-second-blowup){.pf-ref} prove part (d).
:::

:::
:::

::: {.remark title="Characteristic exception inherited from Exercise I.5.1"}
Under only the source's assumption $\operatorname{char}k\ne2$, the cusp quartic in part (a) has two additional singular points in characteristics $7$ and $13$.
Blowing up the origin is an isomorphism near those points, so it cannot make the entire strict transform nonsingular in those characteristics.
The chart computation in step [](#cusp-quartic-blowup-nonsingular){.pf-ref} proves that the singularity over the origin itself is resolved in every characteristic different from $2$; the global nonsingularity assertion requires excluding $7$ and $13$ as well.
:::

::: {.remark title="Published solution"}
The closest published argument for (b) is Ravi Vakil, *Foundations of Algebraic Geometry* (Math 216, Stanford; classes 49 and 50 notes), Section 5.2 "The proper transform of a nodal curve", printed p. 9, read in `tmp/sources/vakil-216-class49-50.pdf` and in its MinerU text version `tmp/sources/vakil-216-class49-50.md`: for $y^2=x^3+x^2$ in the patch $[X:Y]=[s:1]$, where $x=ys$, he gets $y^2-s^2y^2-s^3y^3=0$, "This factors: we get the exceptional divisor $y$ with multiplicity two, and the curve $1-s^2-y^3=0$. Easy exercise: check that the proper transform is nonsingular. Also, notice where the proper transform meets the exceptional divisor: at two points, $s=\pm1$." Two things are missing there and are supplied by step [](#general-node-two-points){.pf-ref}: the nonsingularity, which he leaves as an exercise and which is $\partial/\partial s=-2s\neq0$ at $s=\pm1$ together with the isomorphism away from the exceptional divisor, and the printed factor, which the substitution $x=ys$ gives as $1-s^2-ys^3$ rather than $1-s^2-y^3$. He also treats the one model $y^2=x^3+x^2$ rather than an arbitrary node.

A. Shichijo, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (Solutions to the exercises in Hartshorne's *Algebraic Geometry*), 2020/March version, <https://shitijyou-a.github.io/math/alg-geo/har-ag-solutions/>, Chapter 1 section 5, Exercise 5.6(b), printed p. 5, text version `tmp/sources/shitijyou-ch1-section5.md`, proves part (b) for a general node: he keeps the two tangent directions as $(ax-by)(cx-dy)$ with $ad-bc\ne0$, writes both strict transforms, finds the two points $P_1=(0,0)\times(b:a)$ and $P_2=(0,0)\times(d:c)$ of the exceptional divisor, and computes their Jacobian, whose rank-two claim needs the entry his display omits. Step [](#general-node-two-points){.pf-ref} transcribes it, adds the $V_1$ chart, which he omits as "similar" and which carries one of the two points when $b=0$ or $d=0$, and records that his $V_0$ chart sees both points only when $b,d\ne0$.

Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), text version `tmp/sources/hartshorne-solutions-borcherds.md`, gives no solution to 5.6; his Chapter 1.5 answers stop at 5.5.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), text version `tmp/sources/hartshorne-solutions-troiani.md`, gives no solution to 5.6.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.5.6, PDF p. 46, text version `tmp/sources/hartshorne-solutions-egbert.md`: (a) the cusp $y^2-x^3+x^4+y^4$ blown up as $ys-xt$, with the strict transforms $1-yt+y^2t^2+y^3$ on $t=1$ and $x^2(t^2-x^2+t^2x^2)$ on $s=1$, both checked by the Jacobian criterion; (c) the tacnode $x^2=x^4+y^4$ with strict transform $t^2-y^2-y^2t^4$ on $s=1$, "the lowest degree terms $t^2-y^2$ of the strict transform factor linearly, so we get a node"; (d) $y^3=x^5$ giving $x^3(x^2-u^3)=0$ after one blowup, "which gives a cusp", and one more blowup resolving. His (b) is a paragraph about the blow-up surface and tangent directions rather than a proof of the two-point statement, and it does not show that the two points above the node are nonsingular.

The chart computations for (a), (c) and (d) agree with Egbert's, including the characteristic-7 and 13 caveat for the cusp quartic. Part (b) is Shichijo's, transcribed in step [](#general-node-two-points){.pf-ref}.
:::
