---
schema: qual/card@1
id: E-2M0XQ
kind: problem
title: Fundamental groups of twelve standard spaces
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 58 Exercise 2, printed p. 366,
    with Theorem 58.7, that a homotopy equivalence induces an isomorphism on fundamental groups, and Theorem 59.3. Each of the twelve answers is a deformation retraction onto a circle, a point, or a wedge of two circles, or a homeomorphism onto one of those. What was corrected: the reason given for (j), $S^1\cup(\RR_+\times\RR)$, was a radial formula that is undefined at the origin and on the part of the $y$-axis outside the circle. The half-plane part is contractible, its intersection with the circle is the right semicircle, an arc, and collapsing that arc turns the union into a wedge of $S^1$ with a contractible space; the answer $\ZZ$ is unchanged and the card now gives that reason. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published answer has now been located: Pearse, *Topology (2nd ed.) — James R. Munkres*,
    solutions, Cornell 2005, §58 Exercise 2, his pp. 20-22, read in the MinerU extraction
    tmp/sources/cornell-erin-munkres.md. Nine of the twelve parts are that answer transcribed: (a)
    and (c)-(d) by the straight-line homotopies onto a copy of $S^1$, (b) by the square model of
    the torus retracted to its boundary, (f) onto $2S^1$, (g) onto $S^1$, (h) and (l) onto a point,
    (k) onto the theta space and thence to the figure eight through Examples 2 and 3. The source
    is wrong in two parts and heuristic in a third, and the card does not follow it there: (i) and
    (j) are answered *trivial*, but the homotopy the source writes for them,
    $H(x,t)=(1-t)x+t\,x/\norm x$, is a strong deformation retraction onto $S^1$, so Theorem 58.3
    gives $\ZZ$; and (e) is argued from a picture, with generation by two loops and
    non-commutativity both asserted, so the card decides (e) by the radial retraction onto $S^2$
    minus three points and Example 2, which gives the same answer as the source. Checked against
    the book: the exercise on printed pp. 366-367, the definition of a deformation retract on
    printed p. 360, Theorem 58.3 on printed p. 361, Examples 1-3 on printed p. 362, Theorem 58.7
    on printed p. 364, Theorem 54.5 on printed p. 345, and the printed definition of $\RR_+$ as
    the positive reals on printed p. 31, which is what keeps $\mathbf 0$ out of the spaces of (i)
    and (j). Correction to the note of 2026-11-11 above: the radial formula for (j) is defined on
    that space, since the origin and the $y$-axis are not in it; the objection recorded there
    rested on reading $\RR_+$ as the nonnegative reals, and the answer $\ZZ$ now rests on the
    deformation retraction. Not claimed: that the source's nine transcriptions are proofs of
    generation or non-generation anywhere -- each is a deformation retraction, and Theorem 58.3
    supplies the rest.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, one step per part, with the sources,
    the corrections and the book's numbers named in its own text.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    Two repairs. (b): the card said $H$ "induces a continuous $\bar H$" without naming a quotient
    map or showing that one is a quotient map; the step now names $q_0\times\operatorname{id}_I$ on
    $(I^2-\theset c)\times I$, shows $q_0=\restrictionof{q}{I^2-\theset c}$ is a quotient map by
    Theorem 22.1 (the deleted point is interior, so $I^2-\theset c$ is open and saturated), shows
    that its product with the identity of $I$ is a quotient map because $I$ is compact Hausdorff by
    the lemma of §29 Exercise *11(a), and then gets $\bar H$ from Theorem 22.2. (e): the card
    projected stereographically from a point of $S^2$ *outside* $\theset{e_1,e_2,e_3}$, which is
    undefined on part of $Z$ and carries the three deleted points to three points of $\RR^2$, so
    that $Z$ would be $\RR^2$ minus three points, not the doubly punctured plane Example 2
    applies to; the projection is now from $e_1$, so the two remaining punctures are $e_2$ and
    $e_3$. The answers are unchanged, and the desk-checked corrections of the earlier note to (i),
    (j) and (e)'s answer stand. Checked against the book: the exercise on printed pp. 366-367,
    Theorem 58.3 on printed p. 361, Examples 2 and 3 on printed p. 362, Theorem 58.7 on printed
    p. 364, Theorem 22.1 on printed p. 140, Theorem 22.2 on printed p. 142, and §29 Exercise *11 on
    printed p. 186.
---

::: {.exercise}

For each of the following spaces, the fundamental group is either trivial, infinite cyclic, or isomorphic to the fundamental group of the figure eight.
Determine for each space which of the three alternatives holds.

(a) The "solid torus," $B^2 \times S^1$.

(b) The torus $T$ with a point removed.

(c) The cylinder $S^1 \times I$.

(d) The infinite cylinder $S^1 \times \RR$.

(e) $\RR^3$ with the nonnegative $x$, $y$, and $z$ axes deleted.

The following subsets of $\RR^2$:

(f) $\theset{x \mid \norm{x} > 1}$

(g) $\theset{x \mid \norm{x} \geq 1}$

(h) $\theset{x \mid \norm{x} < 1}$

(i) $S^1 \cup (\RR_+ \times 0)$

(j) $S^1 \cup (\RR_+ \times \RR)$

(k) $S^1 \cup (\RR \times 0)$

(l) $\RR^2 - (\RR_+ \times 0)$
:::

::: {.solution}
The exercise is §58 Exercise 2, printed pp. 366--367, and its question is which
of three alternatives holds for each of the twelve spaces. The proofs for (a),
(b), (c), (d), (f), (g), (h), (k) and (l) are transcribed from Pearse,
*Topology (2nd ed.) — James R. Munkres*, solutions, Cornell 2005, §58 Exercise 2,
his pp. 20--22, read in `tmp/sources/cornell-erin-munkres.md`; each of them
exhibits a deformation retraction and applies Theorem 58.3 (printed p. 361),
together with the computation $\pi_1(S^1)\cong\ZZ$ of Theorem 54.5 (printed
p. 345) and the two deformation retracts of the doubly punctured plane listed as
Examples 2 and 3 on printed p. 362.

Three parts of that answer are not taken over.
- (i) and (j): the source answers *trivial*, and the homotopy it writes down for
  both is $H(x,t)=(1-t)x+t\,x/\norm x$. That homotopy is a strong deformation
  retraction onto $S^1$, which is contained in both spaces, so Theorem 58.3 gives
  $\pi_1\cong\pi_1(S^1)\cong\ZZ$, not the trivial group; steps
  [](#i){.pf-ref} and [](#j){.pf-ref} give the corrected argument. The error is
  in the conclusion drawn from the homotopy, not in the homotopy.
- (e): the source argues from a picture, that loops $\alpha$ and $\beta$ about
  two of the axes generate and that $\beta*\alpha\simeq\bar\gamma\ne\gamma$ shows
  the group is not abelian. Neither assertion is proved there, and a picture is
  not an argument; step [](#e){.pf-ref} decides (e) instead by retracting the
  space onto $S^2$ minus three points and quoting Example 2. The answer agrees
  with the source.

Notation. For a space with a closed subspace $W$, "$W$ is a deformation retract
of $X$" is the book's notion on printed p. 360, and then
$\pi_1(X)\cong\pi_1(W)$ by Theorem 58.3 (printed p. 361); a homeomorphism or
homotopy equivalence induces an isomorphism of fundamental groups by Theorem
58.7 (printed p. 364). Both facts are used without further comment below.

::: pf

::: {.pf-step #a}
(a) The solid torus: $\boxed{\pi_1(B^2\times S^1)\cong\ZZ}$.

::: pf-proof
For $(x,y)\in B^2\times S^1$ put $H((x,y),t)=((1-t)x,y)$. This is continuous,
$H(\cdot,0)$ is the identity, $H(\cdot,1)$ carries $B^2\times S^1$ into
$\theset{0}\times S^1$, and $H$ fixes $\theset{0}\times S^1$ pointwise. So
$\theset{0}\times S^1$, a copy of $S^1$, is a deformation retract of the solid
torus, and $\pi_1\cong\pi_1(S^1)\cong\ZZ$ by Theorem 58.3 and Theorem 54.5.
:::

:::

::: {.pf-step #b}
(b) The torus with a point removed: $\boxed{\pi_1(T-\theset{p})\cong\pi_1(\text{figure eight})}$.

::: pf-proof
Write $T$ as the quotient $q:I^2\to T$ of the square by the identifications
$(x,0)\sim(x,1)$ and $(0,y)\sim(1,y)$, and let $c=(\tfrac12,\tfrac12)$, so that
$q^{-1}(q(c))=\theset c$ because $c$ is interior. Let
$\pi:I^2-\theset c\to\partial I^2$ be the radial projection from $c$, and
$H(x,t)=(1-t)x+t\,\pi(x)$ on $(I^2-\theset c)\times I$. Then $H$ is continuous,
$H(x,0)=x$, $H(x,1)=\pi(x)\in\partial I^2$, and $H$ fixes $\partial I^2$
pointwise because $\pi$ does.

Two points of $I^2-\theset c$ that $q$ identifies lie on $\partial I^2$, so $H$
carries them to themselves at every $t$; hence $H$ is constant on the fibres of
$$
q_0\times\operatorname{id}_I:\ (I^2-\theset c)\times I\longrightarrow
(T-\theset{q(c)})\times I,
$$
where $q_0=\restrictionof{q}{I^2-\theset c}$. That map is a quotient map, so by
Theorem 22.2 (printed p. 142) there is a continuous
$\bar H:(T-\theset{q(c)})\times I\to T-\theset{q(c)}$ with
$\bar H\circ(q_0\times\operatorname{id}_I)=H$. It is a quotient map for two
reasons: $I^2-\theset c$ is open in $I^2$ and saturated for $q$, because
$q^{-1}(q(c))=\theset c$, so $q_0$ is a quotient map onto $T-\theset{q(c)}$ by
Theorem 22.1 (printed p. 140); and $I$ is compact Hausdorff, hence locally compact
Hausdorff, so a quotient map times $\operatorname{id}_I$ is a quotient map by the
lemma in §29 Exercise *11(a) (printed p. 186).

It satisfies $\bar H(y,0)=y$, $\bar H(y,1)\in q(\partial I^2)$ and
$\bar H(y,t)=y$ for $y\in q(\partial I^2)$.

The set $q(\partial I^2)$ is the union of the two circles $q(I\times
\theset 0)$ and $q(\theset 0\times I)$, which meet in the single point
$q(0,0)$: it is a wedge of two circles, that is, the figure eight. So the figure
eight is a deformation retract of $T-\theset p$ with $p=q(c)$, and Theorem 58.3
gives the isomorphism.
:::

:::

::: {.pf-step #c}
(c) The cylinder: $\boxed{\pi_1(S^1\times I)\cong\ZZ}$.

::: pf-proof
$H((x,y),t)=(x,(1-t)y)$ is a deformation retraction of $S^1\times I$ onto
$S^1\times\theset 0$, a copy of $S^1$; Theorem 58.3 and Theorem 54.5 give
$\ZZ$.
:::

:::

::: {.pf-step #d}
(d) The infinite cylinder: $\boxed{\pi_1(S^1\times\RR)\cong\ZZ}$.

::: pf-proof
The same homotopy $H((x,y),t)=(x,(1-t)y)$ is a deformation retraction of
$S^1\times\RR$ onto $S^1\times\theset 0$; Theorem 58.3 and Theorem 54.5 give
$\ZZ$.
:::

:::

::: {.pf-step #e}
(e) $\RR^3$ with the three nonnegative axes deleted:
$\boxed{\pi_1\cong\pi_1(\text{figure eight})}$.

::: pf-proof
Let $R_x,R_y,R_z$ be the three closed rays of the exercise and
$X=\RR^3-(R_x\cup R_y\cup R_z)$; let $e_1,e_2,e_3$ be the unit points of the
three rays and $Z=S^2-\theset{e_1,e_2,e_3}$.

For $x\in X$ we have $x\ne\mathbf 0$, so $H(x,t)=(1-t)x+t\,x/\norm x
=\bigl((1-t)+t/\norm x\bigr)x$ is defined; it is a positive multiple of $x$ for
every $t$, and a positive multiple of a point of $X$ lies in $X$, because such a
multiple lies on $R_i$ only if the point does. So $H$ maps $X\times I$ into $X$,
it fixes $Z$ pointwise, and $H(x,1)=x/\norm x\in Z$; so $Z$ is a deformation
retract of $X$ and $\pi_1(X)\cong\pi_1(Z)$ by Theorem 58.3.

Stereographic projection from $e_1$ is a homeomorphism of $S^2-\theset{e_1}$
onto $\RR^2$, and it carries the other two deleted points $e_2,e_3$ to two points
of $\RR^2$; restricted to the subspace $Z=S^2-\theset{e_1,e_2,e_3}$ it is
therefore a homeomorphism onto $\RR^2$ with those two points deleted — the doubly
punctured plane, which is the space $Z'$ of Example 2. So
$\pi_1(Z)\cong\pi_1(Z')$ by Theorem 58.7. By Example 2, printed p. 362, the figure
eight is a deformation retract of the doubly punctured plane $Z'$, so
$\pi_1(Z')$ is the fundamental group of the figure eight by Theorem 58.3.

Projection from a point of $S^2$ outside $\theset{e_1,e_2,e_3}$ would not do
here: it is undefined at that point, which is in $Z$, and it would carry the three
deleted points to three points of $\RR^2$.
:::

:::

::: {.pf-step #f}
(f) $\theset{x:\norm x>1}$: $\boxed{\pi_1\cong\ZZ}$.

::: pf-proof
Put $X=\theset{x:\norm x>1}$ and $W=\theset{x:\norm x=2}=2S^1$. For $x\in X$
and $t\in I$,
$$
H(x,t)=(1-t)x+\frac{2t}{\norm x}x
$$
lies on the ray through $x$ with norm $(1-t)\norm x+2t$, which is at least
$\min(\norm x,2)>1$, so $H$ maps $X\times I$ into $X$; it fixes $W$ pointwise and
carries $X$ onto $W$ at $t=1$. So $2S^1$ is a deformation retract of $X$ and
$\pi_1(X)\cong\pi_1(2S^1)$ by Theorem 58.3, while $x\mapsto x/2$ is a
homeomorphism $2S^1\to S^1$, so $\pi_1(2S^1)\cong\pi_1(S^1)\cong\ZZ$ by Theorem
58.7 and Theorem 54.5.
:::

:::

::: {.pf-step #g}
(g) $\theset{x:\norm x\ge1}$: $\boxed{\pi_1\cong\ZZ}$.

::: pf-proof
$H(x,t)=(1-t)x+t\,x/\norm x$ has norm $(1-t)\norm x+t\ge1$ for
$\norm x\ge1$, so it maps $X\times I$ into $X$, fixes $S^1$ pointwise and
carries $X$ onto $S^1$ at $t=1$. Hence $S^1$ is a deformation retract of $X$ and
$\pi_1\cong\ZZ$ by Theorem 58.3 and Theorem 54.5.
:::

:::

::: {.pf-step #h}
(h) $\theset{x:\norm x<1}$: $\boxed{\pi_1\ \text{is trivial}}$.

::: pf-proof
$X=\theset{x:\norm x<1}$ is convex and contains $\mathbf 0$, and
$H(x,t)=(1-t)x$ is a deformation retraction of $X$ onto $\theset{\mathbf 0}$; so
$\pi_1(X)\cong\pi_1(\theset{\mathbf 0})$, which is trivial, the only loop in a
one-point space being constant. Theorem 58.3 gives the isomorphism.
:::

:::

::: {.pf-step #i}
(i) $S^1\cup(\RR_+\times 0)$: $\boxed{\pi_1\cong\ZZ}$.

::: pf-proof
Recall that $\RR_+$ is the set of positive reals (printed p. 31), so
$\mathbf 0\notin\RR_+\times 0$ and $\mathbf 0$ is not in $X=S^1\cup(\RR_+\times
0)$. For $x\in X$ we have $x\ne\mathbf 0$, and
$$
H(x,t)=(1-t)x+\frac{t}{\norm x}x=\Bigl((1-t)+\frac{t}{\norm x}\Bigr)x
$$
is a positive multiple of $x$. A positive multiple of a point of $\RR_+\times
0$ lies in $\RR_+\times 0$, and for $x\in S^1$ the coefficient is
$(1-t)+t=1$, so $H(x,t)=x$; hence $H$ maps $X\times I$ into $X$, it fixes $S^1$
pointwise and carries $X$ onto $S^1$ at $t=1$. Thus $S^1$ is a deformation
retract of $X$ and
$\pi_1(X)\cong\pi_1(S^1)\cong\ZZ$ by Theorem 58.3 and Theorem 54.5. This is the
homotopy the source writes down, with the conclusion the source draws from it
corrected.
:::

:::

::: {.pf-step #j}
(j) $S^1\cup(\RR_+\times\RR)$: $\boxed{\pi_1\cong\ZZ}$.

::: pf-proof
The same formula $H(x,t)=\bigl((1-t)+t/\norm x\bigr)x$ is defined on
$X=S^1\cup(\RR_+\times\RR)$, since $\mathbf 0\notin X$ for the same reason. A
positive multiple of a point of $\RR_+\times\RR$ lies in $\RR_+\times\RR$, and
for $x\in S^1$ the coefficient is $1$, so $H$ fixes $S^1$ pointwise; hence $H$ is
a deformation retraction of $X$ onto $S^1$. Theorem 58.3 and
Theorem 54.5 give $\pi_1(X)\cong\ZZ$.
:::

:::

::: {.pf-step #k}
(k) $S^1\cup(\RR\times 0)$: $\boxed{\pi_1\cong\pi_1(\text{figure eight})}$.

::: pf-proof
Let $X=S^1\cup(\RR\times 0)$ and put
$$
H(x,t)=\begin{cases} x, & \norm x\le1,\\[2pt] (1-t)x+\dfrac{t}{\norm x}x, & \norm x>1.\end{cases}
$$
The two formulas agree where $\norm x=1$, so $H$ is continuous by the pasting
lemma on the closed sets $\theset{\norm x\le1}\times I$ and
$\theset{\norm x\ge1}\times I$. A point of $X$ of norm greater than $1$ lies on
the $x$-axis, since every point of $S^1$ has norm $1$; for such a point
$H(x,t)$ is a positive multiple of $x$ and so again lies in $\RR\times 0
\subseteq X$, while for $\norm x\le1$ the map is the identity. Thus $H$ is a
deformation retraction of $X$ onto
$S^1\cup([-1,1]\times 0)$, which is the theta space of Example 3 under a
rotation, and $\pi_1(X)\cong\pi_1(\theta)$ by Theorem 58.3. Example 3, printed
p. 362, records that the theta space is a deformation retract of the doubly
punctured plane, of which the figure eight is a deformation retract by Example 2;
two applications of Theorem 58.3 give
$\pi_1(\theta)\cong\pi_1(\RR^2-p-q)\cong\pi_1(\text{figure eight})$.
:::

:::

::: {.pf-step #l}
(l) $\RR^2-(\RR_+\times 0)$: $\boxed{\pi_1\ \text{is trivial}}$.

::: pf-proof
Let $X=\RR^2-(\RR_+\times 0)$ and $c=(-1,0)\in X$; the formula
$H(x,t)=(1-t)x+tc$ is continuous and satisfies $H(x,0)=x$ and $H(x,1)=c$, so it
remains to check that it stays in $X$. Let $x\in X$ and $t\in I$ with
$t<1$. If $x_2\ne0$ then $H(x,t)_2=(1-t)x_2\ne0$, so $H(x,t)$ is not on the
$x$-axis. If $x_2=0$ then $x$ is on the $x$-axis and $x\in X$ forces $x_1\le0$,
so $H(x,t)_1=(1-t)x_1-t<0$ and again $H(x,t)\notin\RR_+\times 0$. Hence $H$
maps $X\times I$ into $X$ and is a deformation retraction of $X$ onto the point
$c$; so $\pi_1(X)\cong\pi_1(\theset c)$ is trivial by Theorem 58.3.
:::

:::

:::
:::
