---
schema: qual/card@1
id: P-AGH423DUALCURVE
kind: problem
title: The dual curve, its class $d(d-1)$, and the counts of inflection points and bitangents
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Genus
  - Embeddings
  - Linear Systems
relations: []
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.2.3 in the original text. The setup tacitly needs d>=2.
    More seriously, part (b) defines a bitangent as tangent at exactly two
    points, while part (h) counts hyperflex lines among the 28 bitangents; its
    parenthetical also misidentifies the dual singularity of a four-fold
    contact as a tacnode. The erratum below gives the corrected statement and
    an explicit smooth quartic counterexample to the literal convention.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Hartshorne IV.2.3 does not assume d >= 2, and part (h) says a quartic has exactly 28 bitangents, with a four-fold-contact tangent giving a tacnode on the dual curve; with the bitangent definition of part (b) a quartic with h hyperflexes has 28-h bitangents, and the dual point is a unibranch E6 cusp. The statement now assumes d >= 2, counts a four-fold-contact line as a bitangent in (h), and names the dual point as a unibranch multiplicity-3 singularity.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Printed exercise read again for this pass: Hartshorne, Algebraic Geometry
    (1977), IV.2.3, printed pp. 304--305 (PDF pp. 319--320 of the checked-in
    extraction tmp/sources/hartshorne-1977-algebraic-geometry.md), parts
    (a)--(h), with the hypothesis "We assume char k = 0 below" and, in part (h),
    the printed parenthesis "(This holds even if the curve has a tangent with
    four-fold contact, in which case the dual curve X* has a tacnode.)" -- read
    as printed; the card's statement keeps the corrected form recorded in the
    source-corrected event of 2026-10-29 and is not changed here. The two
    published treatments named in the brief were read at the cited places in
    their text versions: B. Reiser, Hartshorne Solutions (15 February 2022),
    Exercise IV.2.3, printed pp. 354--358, which is PDF pp. 355--359 of
    tmp/sources/reiser-hartshorne-solutions-pp351-358.md, the printed folio
    being one less than the PDF page -- part (a) at p. 355, (b) at p. 356,
    (c)--(f) at p. 357, (g)--(h) at p. 358 -- and O. Bergvall, Arithmetic and
    topology of classical structures associated to plane quartics,
    arXiv:2106.13072v1, section 2.2, printed pp. 3--4, where the definition of
    bitangent including a four-fold contact is on p. 3 and Theorem 2.2 with the
    count and the odd theta characteristics on p. 4, page positions fixed on
    tmp/sources/bergvall-2021-plane-quartics-arithmetic-topology.pdf.

    What the named sources do and do not prove: Reiser proves (a)--(g) and the
    general-case count of (h), and says nothing about the local form of X* at a
    hyperflex, which is the second half of the printed (h) and the card's own
    step s11; Bergvall states the count for arbitrary smooth quartics and the
    bitangent convention, but states Theorem 2.2 as a classical result of
    Plucker and Jacobi rather than proving it. What this pass did not do: it did
    not re-read Egbert, whose citation is that of an earlier event and stands
    unchanged, and it did not verify Reiser's citations of the book (I Ex 7.2,
    I Ex 7.3, IV Ex 1.8, II Ex 6.6) beyond their statements.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now transcribed from those two treatments, one step per
    published argument, each step naming the part and printed page it comes
    from: s1 (Reiser (b), p. 356, the parametrized form of the tangent lines),
    s2 (Reiser (a), p. 355, the two cases of the local equation), s3 (Reiser
    (a), p. 356), s4 (Reiser (b), p. 356, the formal parametrization of the
    branches of X*), s5 and s6 (Reiser (c), p. 357), s7 (Reiser (d), p. 357),
    s8, s9, s10 (Reiser (e), p. 357), s11's first paragraph (Reiser (f), p.
    357), s12 (Reiser (f), p. 357), s13 (Reiser (g), p. 358, the group-law
    argument, replacing the divisor computation this card carried), s14
    (Reiser (h), p. 358, and Bergvall section 2.2 with Theorem 2.2, printed
    pp. 3--4, for the hyperflex convention and the count). Steps s2, s4, s7,
    s13 and s14 were rewritten to the source's route; the rest keep their
    arguments and now name the page where the source gives them. Marked as the
    card's own: the second paragraph of s11 (the hyperflex point of X* is
    unibranch of multiplicity 3 with delta = 3) and the last paragraph of s14
    (b = 28 - h), neither of which either source proves; and the sentences that
    identify Reiser's I and B with ordinary flexes and strict bitangents in s12.
    Checked against the book after the transcription: that (a)'s two ramified
    classes are exactly P in L and the inflection points, that (b)'s conclusion
    is about ordinary r-fold points in the sense of I Ex 5.3, that (c)'s count is
    d(d-1) tangents through O and the class is d(d-1), that (d)'s count is
    (d+1)(d-2) at a point of X, that (e)'s weighted count is 3d(d-2) and the
    ordinary inflection is an ordinary cusp, that (f)'s formula is
    d(d-2)(d-3)(d+3)/2, and that (g)'s nine and (h)'s 28 are the d = 3 and d = 4
    cases.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    #121 reader's report on this round, and the two events of this date
    restored. Step s2 is headed Reiser's part (a) and now carries his argument in
    both of its cases: the repair of the first pass had replaced his case P not
    in L with a computation of e_P = v_P(df/dy) = r-1 that no source gives and
    that the step did not mark as the card's own. His criterion stands at the
    corrected point: the tangent at Q meets the line at infinity V(z) in
    [df/dy : -df/dx : 0], which at P is [0:1:0], and there the local coordinate
    is the ratio with the opposite sign from the one he prints at [1:0:0], which
    changes no valuation. What the step now transcribes from him, printed
    p. 356, is the form of the map on local rings, the expansion
    f = x + ax^2 + bxy + cy^2 + ..., the unit denominator 1 + 2ax + by + ...,
    the numerator bx + 2cy + ..., the valuation of x at least 2 and of y exactly
    1, and so the criterion c = 0, which is I_P(X, V(x)) >= 3. The index r-1 is
    not what his case decides, and the paragraph that gives it is marked as the
    card's own, with its derivation (df/dy = -(df/dx) x'(y) on the branch, of
    order r-1 in characteristic 0, where r = I_P(X, T_P(X))); step s9 uses it.
    Two further corrections. The heading cited part (a) at printed p. 355 alone,
    where the case P not in L is on p. 356 and part (a) runs over pp. 355--356.
    And the step wrote t = x/y for the coordinate on L at [0:1:0], in the letters
    that are the affine coordinates on the plane and on X, where the equation
    "t = x/y = -(df/dy)/(df/dx) on X" reads as a false identity between two
    different functions; the coordinate on L is now called tau, and x, y are the
    plane's. Where and how the sources were read: Reiser in
    tmp/sources/reiser-hartshorne-solutions-pp351-358.md, which is PDF
    pp. 352--359 of tmp/sources/reiser-hartshorne-solutions.pdf with the printed
    folio one less than the PDF page, the solution of (a) on printed pp. 355--356
    and the sentence on the tangent's meeting with V(z) on printed p. 356;
    Bergvall in tmp/sources/bergvall-2021-plane-quartics-arithmetic-topology.md,
    section 2.2 on printed pp. 3--4, positions fixed on its PDF; and the book in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, IV.2.3 on printed
    pp. 304--305. The rendered remark's three text-version paths and the page
    range of Egbert's IV.2.3 are out of it and recorded here: Egbert's IV.2.3
    runs over printed pp. 212--215. Not read in this pass: Egbert's IV.2.3
    itself, whose citation is that of an earlier event, and Reiser's citations
    of the book (I Ex 7.2, I Ex 7.3, IV Ex 1.8, II Ex 6.6) beyond their
    statements. The two events of this date above were rewritten in place by
    6a77ef9aab; they are restored to the text they carried when written, and
    this event is the correction.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the #121 reader's report, in the card's own paragraph of step s2
    that gives the index of the morphism. That paragraph ended the case P in L
    with "the image of t is x plus terms of higher order, of valuation r", which
    is false for r >= 3: the second term is (df/dy)/(df/dx) y = -x'(y) y on the
    branch, of the same order r-1 as the derivative it comes from, so it does not
    vanish to higher order than x and can raise the valuation. The term is
    -r a_r y^r against the a_r y^r of x, the image is x - y x'(y) =
    (1-r) a_r y^r + O(y^{r+1}), and its valuation is r only because 1 - r != 0 in
    characteristic 0, which the step's hypothesis supplies and which is what the
    paragraph now says. The expansion itself is the card's, not a source's: the
    card before this round carried exactly it, as h(t) - t h'(t) = (1-r) a_r t^r
    in the coordinates of step s1 at revision 0eaf611b02^, and the repair of the
    first pass dropped the factor. Step s9, which subtracts the d contributions of
    X cap L, is unaffected: its line L is chosen to contain no inflection point, so
    r = 2 there. No source was re-read for this paragraph, nothing else on the card
    changes, and the pages and paths of the sources are those of the events above.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    #121 reader's report on the event of this date above, which is left as written.
    Two errors in it. First, it calls the second term of the image,
    (df/dy)/(df/dx) y = -x'(y) y, "of the same order r-1 as the derivative it
    comes from". It is of order r: x'(y) has order r-1 and the multiplication by y
    raises that by one, so the term is -r a_r y^r, of the same order as x, which is
    why it can change the leading coefficient rather than vanishing against it.
    The rendered step states this correctly -- x - y x'(y) = (1-r) a_r y^r +
    O(y^{r+1}) -- and only the note was wrong. Second, the step gave the line L's
    not being tangent to X as the reason that r = 2 at a point of X cap L that is
    not an inflection point; that reason is wrong and is now out of the step. The
    line L's tangency governs ord(y) = 1 in the case P in L, and nothing else:
    r = I_P(X, T_P(X)) is at least 2 at every point of X, a tangent line meeting
    the curve with multiplicity at least 2, and is below 3 exactly off the
    inflection points, so r = 2 at such a point follows from the definition of an
    inflection point in part (a) of the book. The expansion, its characteristic-0
    hypothesis, and step s9, whose L carries no inflection point, are unchanged.
    Read for this: the book's part (a), in tmp/sources/hartshorne-1977-algebraic-geometry.md
    at IV.2.3, printed pp. 304--305, for the definition of an inflection point as
    I_P(X, T_P(X)) >= 3. Not read in this pass: neither published source, whose
    pages and paths are those of the events above; no other card is touched.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the #121 reader's report of this round, in the rendered text only:
    one undeclared notation and three positional references. The coordinate tau of
    step s2 was given as "the affine coordinate a/b on L = V(z)", where a and b
    were never declared and, ten lines later in the same step, are the
    coefficients of f = x + ax^2 + bxy + cy^2 + ..., so the definition read as
    that pair of coefficients. It is now the affine coordinate on L = V(z) at
    [0:1:0] that a point of L gives as the ratio of its first two homogeneous
    coordinates, with [1:0:0] as its point at infinity, which declares its value
    at both ends of L and leaves the letters of the plane, of X and of f
    untouched. The positional references: step s1's "The coordinates above are
    that line" now names them, (-h'(t), t h'(t) - h(t)); step s4's "by the
    paragraph above" is replaced by what that paragraph establishes, one branch
    for each contact point, each nonsingular with its own tangent direction; and
    step s12's "The paragraph above identifies the nodes with the strict
    bitangents" becomes "The identification this step proves". No mathematics
    changes: the map on local rings, the valuation of the paragraph, the branch
    count of s4 and the genus computation of s12 stand as they were. Not done in
    this pass: no source was re-read and no step re-derived, the pages and paths
    of the sources being those of the events above; no other card is touched.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the #121 reader's report of this round, in the rendered text only:
    the last positional reference of step s2. The paragraph that sets up the map on
    local rings closed "no valuation below depends on the sign", a reference
    forward by position of the same class as the three that 265d815466 replaced.
    What uses those valuations is one step: s9, which subtracts the d contributions
    of X cap L at index 2 and counts r-2 at an inflection point, both read off the
    index that step s2 computes. The sentence now says that a sign changes no order,
    so the index of varphi that step [](#s9){.pf-ref} uses does not depend on it,
    naming the step rather than pointing at it. No mathematics changes: the map on
    local rings, the value e_P(varphi) = r-1 and the index 2 of the other case stand
    as they were, and step s9 is unchanged. Not done in this pass: no source was
    re-read, no step re-derived, the pages and paths of the sources being those of
    the events above; no other card is touched.
review: draft
---

::: {.problem}
Let $X$ be a curve of degree $d \geq 2$ in $\PP^2$.
For each point $P \in X$, let $T_P(X)$ be the tangent line to $X$ at $P$ (I, Ex.
7.3). Considering $T_P(X)$ as a point of the dual projective plane $(\PP^2)^*$, the map $P \mapsto T_P(X)$ gives a morphism of $X$ to its \dfn{dual curve} $X^*$ in $(\PP^2)^*$ (I, Ex.
7.3).

Note that even though $X$ is nonsingular, $X^*$ in general will have singularities.
We assume $\characteristic k=0$ below.

(a) Fix a line $L \subseteq \PP^2$ which is not tangent to $X$.
Define a morphism $\varphi: X \to L$ by $\varphi(P)=T_P(X) \intersect L$, for each point $P \in X$.
Show that $\varphi$ is ramified at $P$ if and only if either (1) $P \in L$, or (2) $P$ is an inflection point of $X$, which means that the intersection multiplicity (I, Ex.
5.4) of $T_P(X)$ with $X$ at $P$ is $\geq 3$.
Conclude that $X$ has only finitely many inflection points.

(b) A line of $\PP^2$ is a \dfn{multiple tangent} of $X$ if it is tangent to $X$ at more than one point.
It is a \dfn{bitangent} if it is tangent to $X$ at exactly two points.
If $L$ is a multiple tangent of $X$, tangent to $X$ at the points $P_1, \ldots, P_r$, and if none of the $P_i$ is an inflection point, show that the corresponding point of the dual curve $X^*$ is an ordinary $r$-fold point, which means a point of multiplicity $r$ with distinct tangent directions (I, Ex.
5.3). Conclude that $X$ has only finitely many multiple tangents.

(c) Let $O \in \PP^2$ be a point which is not on $X$, nor on any inflectional or multiple tangent of $X$.
Let $L$ be a line not containing $O$.
Let $\psi: X \to L$ be the morphism defined by projection from $O$.
Show that $\psi$ is ramified at a point $P \in X$ if and only if the line $OP$ is tangent to $X$ at $P$, and in that case the ramification index is 2. Use Hurwitz's theorem and (I, Ex.
7.2) to conclude that there are exactly $d(d-1)$ tangents of $X$ passing through $O$.
Hence the degree of the dual curve (sometimes called the \dfn{class} of $X$) is $d(d-1)$.

(d) Show that for all but a finite number of points of $X$, a point $O$ of $X$ lies on exactly $(d+1)(d-2)$ tangents of $X$, not counting the tangent at $O$.

(e) Show that the degree of the morphism $\varphi$ of (a) is $d(d-1)$.
Conclude that if $d \geq 2$, then $X$ has $3d(d-2)$ inflection points, properly counted.
(If $T_P(X)$ has intersection multiplicity $r$ with $X$ at $P$, then $P$ should be counted $r-2$ times as an inflection point.
If $r=3$ we call it an ordinary inflection point.)
Show that an ordinary inflection point of $X$ corresponds to an ordinary cusp of the dual curve $X^*$.

(f) Now let $X$ be a plane curve of degree $d \geq 2$, and assume that the dual curve $X^*$ has only nodes and ordinary cusps as singularities (which should be true for sufficiently general $X$). Then show that $X$ has exactly $\frac{1}{2} d(d-2)(d-3)(d+3)$ bitangents.
Hint: Show that $X$ is the normalization of $X^*$.
Then calculate $p_a(X^*)$ two ways: once as a plane curve of degree $d(d-1)$, and once using (Ex.
1.8).

(g) For example, a plane cubic curve has exactly 9 inflection points, all ordinary.
The line joining any two of them intersects the curve in a third one.

(h) A plane quartic curve has exactly 28 bitangents.
(This holds even if the curve has a tangent with four-fold contact, provided such a line is counted as a bitangent; the corresponding point of the dual curve $X^*$ is a unibranch singular point of multiplicity $3$.)
:::

::: {.solution}
Let
$$
\gamma:X\longrightarrow X^*\subset(\PP^2)^*
$$
denote the Gauss map $P\mapsto T_P(X)$.

::: pf

::: {.pf-step #s1}
If $P\in X$ and
$$
r=I_P\bigl(X,T_P(X)\bigr),
$$
then, in suitable local coordinates, the Gauss map is
$$
t\longmapsto
\bigl(-h'(t),\,t h'(t)-h(t)\bigr),
\qquad
h(t)=a_rt^r+O(t^{r+1}),\quad a_r\ne0.
$$

::: pf-proof

This step is the card's own.
Choose affine coordinates with
$$
P=(0,0),
\qquad
T_P(X)=V(y).
$$
Since $X$ is nonsingular at $P$, a local parameter $t=x$ writes the curve as
$$
y=h(t),
$$
where $h(0)=h'(0)=0$.  The order of $h$ is precisely the intersection
multiplicity with the tangent line, so
$$
h(t)=a_rt^r+O(t^{r+1}),
\qquad
r\geq2.
$$

The tangent line at $(t,h(t))$ is
$$
y-h(t)=h'(t)(x-t),
$$
or
$$
-h'(t)x+y+t h'(t)-h(t)=0.
$$
In the dual affine chart where the coefficient of $y$ is $1$, this is exactly
the displayed parametrization of $\gamma$.

Reiser, Exercise IV.2.3(b), printed p. 356, computes the same tangent lines in parametrized form: for $\Spec k[[t]]\to\AA^2$ given by $t\mapsto(f(t),g(t))$, the tangent line at $t=t_0$ is
$$
g'(t_0)\bigl(x-f(t_0)\bigr)-f'(t_0)\bigl(y-g(t_0)\bigr)=0,
$$
and for the branch $t\mapsto(ut^2,t)$ at a simple tangency he reads off the dual parametrization $t\mapsto[1:-(u't^2+2u(t)t):u't^3+u(t)t^2]$. The coordinates $(-h'(t),\,t h'(t)-h(t))$ are that line for a branch written as a graph, at contact order $r$.
:::

:::

::: {.pf-step #s2}
The morphism $\varphi:X\to L$ of part (a) is ramified at $P$ if and
only if $P\in L$ or $P$ is an inflection point.

::: pf-proof
Reiser, Exercise IV.2.3(a), printed pp. 355--356. Take an affine chart and change
coordinates so that $P=(0,0)\in\AA^2$ and $X\cap\AA^2$ is cut out by a polynomial
$f$ whose linear term is $x$; then $T_P(X)=V(x)$.

Suppose first that $P\in L$. Since $L$ is not tangent to $X$, a further change of
coordinates puts $L=V(y)$. The tangent line at $Q=(Q_x,Q_y)$ is
$$
V\Bigl(\frac{\partial f}{\partial x}(Q)(x-Q_x)+\frac{\partial f}{\partial y}(Q)(y-Q_y)\Bigr),
$$
so $\varphi(Q)$ is found by setting $y=0$ and solving for $x$, which gives
$$
x=\frac{\frac{\partial f}{\partial x}(Q)Q_x+\frac{\partial f}{\partial y}(Q)Q_y}{\frac{\partial f}{\partial x}(Q)}.
$$
On local rings, with $t$ a coordinate on $L$, the map is therefore
$$
k[t]_{(t)}\longrightarrow k[x,y]_{(x,y)}/(f),
\qquad
t\longmapsto\frac{\frac{\partial f}{\partial x}(x,y)\,x+\frac{\partial f}{\partial y}(x,y)\,y}{\frac{\partial f}{\partial x}(x,y)}.
$$
Here $\frac{\partial f}{\partial x}=1+\cdots$ is a unit, and
$\frac{\partial f}{\partial y}(P)=0$ because the tangent at $P$ is $V(x)$, so
$\frac{\partial f}{\partial y}$ lies in the maximal ideal at $P$. The valuation
of $x$ in $\mco_{X,P}$ is the intersection multiplicity $I_P(X,V(x))\ge2$, the
line $V(x)$ being the tangent, and the valuation of $y$ is
$I_P(X,V(y))=1$, the line $V(y)=L$ not being tangent; so both terms of the
numerator have valuation at least $2$, the image of $t$ has valuation at least
$2$, and $\varphi$ is ramified at $P$.

Suppose now that $P\notin L$. Then $L=V(z)$ is the line at infinity. Reiser's
case, printed p. 356: homogenizing the tangent line at $Q$,
$$
\frac{\partial f}{\partial x}(Q)\,x+\frac{\partial f}{\partial y}(Q)\,y
-\Bigl(\frac{\partial f}{\partial x}(Q)Q_x+\frac{\partial f}{\partial y}(Q)Q_y\Bigr)z=0,
$$
shows that it meets $L=V(z)$ in
$$
\Bigl[\frac{\partial f}{\partial y}(Q):-\frac{\partial f}{\partial x}(Q):0\Bigr].
$$
He prints this intersection as $[\partial f/\partial x:\partial f/\partial y:0]$
and puts the local coordinate at $[1:0:0]$; at $Q=P$ the intersection is
$[0:1:0]$, and that is where the coordinate is read. With $\tau$ the affine
coordinate on $L=V(z)$ at $[0:1:0]$, the one that a point of $L$ gives as the
ratio of its first two homogeneous coordinates and that has $[1:0:0]$ as its point
at infinity, the map on local rings is
$$
k[\tau]_{(\tau)}\longrightarrow k[x,y]_{(x,y)}/(f),
\qquad
\tau\longmapsto-\frac{\partial f/\partial y}{\partial f/\partial x},
$$
the minus sign being what the corrected point changes; his coordinate at
$[1:0:0]$ carries the same ratio without it, and a sign changes no order, so the
index of $\varphi$ that step [](#s9){.pf-ref} uses does not depend on it.

Write $f=x+ax^2+bxy+cy^2+\cdots$. The denominator is the unit
$1+2ax+by+\cdots$ and the numerator is $bx+2cy+\cdots$, which has valuation at
least $2$ exactly when $c=0$, because $\operatorname{ord}(x)\ge2$ and
$\operatorname{ord}(y)=1$. And $c=0$ is exactly the statement that $V(x)$ meets
$X$ at $P$ with multiplicity at least $3$, that is, that $P$ is an inflection
point: the length of $\mco_{\AA^2,P}/(x,f)$ is the least $e$ with $y^e$ appearing
in $f$.

So $\varphi$ is ramified at $P$ if and only if $P\in L$ or $P$ is an inflection
point. The index is not what Reiser's case decides and is the card's own: on the
branch through $P$ write $x=x(y)$, so that $f(x(y),y)=0$ gives
$\partial f/\partial y=-(\partial f/\partial x)x'(y)$ along $X$, with
$\partial f/\partial x$ a unit; $x(y)$ has order $r=I_P(X,T_P(X))$ and, in
characteristic $0$, $x'(y)$ has order $r-1$, so
$$
e_P(\varphi)=r-1
$$
in the case $P\notin L$. In the case $P\in L$ the image of $t$ is
$x+(\partial f/\partial y)/(\partial f/\partial x)\,y$, which on the branch is
$x-y\,x'(y)$; writing $x(y)=a_ry^r+O(y^{r+1})$ with $a_r\ne0$, that series is
$(1-r)a_ry^r+O(y^{r+1})$, of valuation $r$ because $r\ge2$ and $1-r\ne0$ in
characteristic $0$. At a point of $X\cap L$ that is not an inflection point
$r=2$, an inflection point being one at which $I_P(X,T_P(X))\ge3$ and every
point of $X$ having $I_P(X,T_P(X))\ge2$; the hypothesis that the line $L$ is
not tangent to $X$ is what gives $\operatorname{ord}(y)=1$ in the case $P\in L$,
and it is not what fixes $r$. Part (a) of the book asks only for ramification.

:::

:::

::: {.pf-step #s3}
The curve $X$ has only finitely many inflection points.

::: pf-proof

This step is the card's own.
The map $\varphi$ is nonconstant.  Indeed, if it were constant with value
$Q\in L$, every tangent line to $X$ would pass through $Q$.  Projection from
$Q$ gives a nonconstant map from $X$ to $\PP^1$: it has degree $d$ if
$Q\notin X$, and after removing the base point it has degree $d-1$ if
$Q\in X$.  Away from $Q$, its differential would vanish everywhere because
the tangent line at every point passes through the centre of projection.
That would make the projection inseparable, which is impossible in
characteristic $0$.

Hence $\varphi$ is a nonconstant morphism of projective curves and therefore
finite and separable.  Its ramification locus is finite.  By step [](#s2){.pf-ref} every
inflection point outside the finite set $X\cap L$ lies in that ramification
locus, so the set of inflection points is finite.

Reiser, Exercise IV.2.3(a), printed p. 356, draws the same conclusion in one line --- "by Hurwitz's formula, $\deg R<\infty$, so $X$ must have finitely many inflection points" --- where the finiteness of $\deg R$ is finiteness of the ramification divisor of the morphism $\varphi$ shown nonconstant here.
:::

:::

::: {.pf-step #s4}
If a line $M$ is tangent to $X$ at distinct non-inflection points
$P_1,\ldots,P_s$, then the corresponding point $[M]\in X^*$ is an ordinary
$s$-fold point.  Consequently $X$ has only finitely many multiple tangents.

::: pf-proof
Reiser, Exercise IV.2.3(b), printed pp. 356--357. An equation for the dual curve
is hard to get at, so the branches are computed from a formal parametrization of
$X$. Put coordinates so that $M=V(x)$ and one contact point is $[0:0:1]$, with no
contact point an inflection point. Locally at $[0:0:1]$ the curve is cut out by
$x-uy^2$ with $u$ a unit, and $y$ generates $\mco_{X,[0:0:1]}$, so $X$ is
parametrized by $t\mapsto(ut^2,t)$; the corresponding branch of $X^*$ in dual
coordinates $[A:B:C]$ is
$$
t\longmapsto[1:-(u't^2+2u(t)t):u't^3+u(t)t^2].
$$
Its derivative at $t=0$ is $(-2u(0),0)\ne0$, so the branch is nonsingular there,
with tangent line $V(C)$ --- and $V(C)$ is the dual line of $[0:0:1]$, that is, the
set of primal lines through $[0:0:1]$. At the contact point $[0:1:0]$ the same
computation with the coordinates exchanged gives the branch tangent $V(B)$, the
dual line of $[0:1:0]$. Distinct contact points therefore give nonsingular
branches through $[M]$ with pairwise distinct tangent directions, which is a
point of multiplicity $s$ with distinct tangent directions, an ordinary $s$-fold
point in the sense of [[P-AGH53MULTIPLICITY|Exercise I.5.3]].

For finiteness, by step [](#s3){.pf-ref} only finitely many tangents are
inflectional; every other multiple tangent gives a point of $X^*$ with at least
two branches, one for each of its contact points and each nonsingular with its own
tangent direction, hence a singular point of the projective curve $X^*$, and a
projective curve has only finitely many singular points. Reiser
concludes at the same place "that $X$ has only finitely many multiple tangents".

:::

:::

::: {.pf-step #s5}
Let $O\notin X$ lie on no inflectional or multiple tangent.  Projection
from $O$ gives a degree-$d$ morphism
$$
\psi:X\longrightarrow\PP^1
$$
whose ramification points are exactly the points $P$ for which $OP=T_P(X)$,
and each has ramification index $2$.

::: pf-proof

This step is the card's own.
A fibre of the projection is the intersection of $X$ with a line through
$O$.  At a point $P$, choose a local coordinate on the pencil of lines through
$O$ whose value at $P$ corresponds to the line $OP$.  The difference from
that target value is, up to a unit, a local equation for $OP$ restricted to
$X$.  Hence
$$
e_P(\psi)=I_P(X,OP).
$$
It follows that $e_P(\psi)>1$ exactly when $OP=T_P(X)$.  Since $O$ lies on no
inflectional tangent, the contact order is then exactly $2$.  The hypothesis
that $O$ lies on no multiple tangent ensures that different ramification
points give different tangent lines through $O$.

Because $O\notin X$, a general line through $O$ meets $X$ in $d$ points,
counted with multiplicity, so $\deg\psi=d$.

Reiser, Exercise IV.2.3(c), printed p. 357, computes this in coordinates $O=[0:0:1]$, $L=V(z)$, where $\psi$ is $(x,y)\mapsto[x:y]$ and $x/y$ is a local coordinate at $[0:1]$: $\psi$ is ramified at $P$ exactly when $x$ lies in the square of the maximal ideal at $P$, that is, exactly when $V(x)=OP$ meets $X$ at $P$ with multiplicity at least $2$; $O$ on no inflectional tangent makes the index exactly $2$, and $O$ on no multiple tangent makes distinct ramification points correspond to distinct lines through $O$.
:::

:::

::: {.pf-step #s6}
Exactly $d(d-1)$ tangent lines to $X$ pass through such a point $O$,
and
$$
\deg X^*=d(d-1).
$$

::: pf-proof

This step is the card's own.
By [[P-AGH72ARITHGENUS|Exercise I.7.2]],
$$
g(X)=\frac{(d-1)(d-2)}2,
$$
so
$$
2g(X)-2=d^2-3d.
$$
Apply Riemann--Hurwitz to the degree-$d$ map of step [](#s5){.pf-ref}.  Its ramification
divisor has degree
$$
\deg R_\psi
=2g(X)-2+2d
=d^2-d
=d(d-1).
$$
Every ramification point is simple and corresponds to exactly one tangent
through $O$, so this is the desired number of tangents.

In the dual plane, the lines through $O$ form a line $O^*$.  Its intersection
with $X^*$ consists of the tangent lines to $X$ passing through $O$.  At each
of the $d(d-1)$ points just found, $X^*$ is smooth by step [](#s4){.pf-ref}, and its
tangent line is $P^*$ for the corresponding tangency point $P$.  Since
$O\ne P$, the lines $O^*$ and $P^*$ are distinct, so the intersection is
transverse.  Therefore
$$
O^*\cdot X^*=d(d-1),
$$
which is the degree of $X^*$.

Reiser, Exercise IV.2.3(c), printed p. 357, runs the same count: $g(X)=\frac{(d-1)(d-2)}{2}$ by (I, Ex. 7.2), so Hurwitz gives $\deg R=(d-1)(d-2)-2-d(-2)=d(d-1)$, and $R$ is a sum of distinct points each corresponding uniquely to a tangent to $X$ through $O$. The passage from that count of tangents to $\deg X^*$ is the transversal intersection $O^*\cap X^*$ computed here.
:::

:::

::: {.pf-step #s7}
For all but finitely many $O\in X$, exactly
$$
(d+1)(d-2)
$$
tangent lines to $X$, other than $T_O(X)$, pass through $O$.

::: pf-proof
Reiser, Exercise IV.2.3(d), printed p. 357. By steps [](#s3){.pf-ref} and
[](#s4){.pf-ref} there are only finitely many inflectional and multiple tangent
lines, each meeting $X$ in finitely many points; excluding those points and the
inflection points of $X$ removes only finitely many $O$.

For a remaining $O$, remove the fixed point $O$ from each line of the pencil
through $O$: this is a morphism
$$
\psi_O:X\longrightarrow\PP^1
$$
of degree $d-1$, unramified at $O$, since with $O=(0,0)$, $T_O(X)=V(y)$ and
$y=a_2x^2+O(x^3)$, a local coordinate on the pencil is the slope
$$
\frac{y}{x}=a_2x+O(x^2),
$$
of order $1$.

At a point $P\ne O$ the argument of part (c), step [](#s5){.pf-ref}, applies:
$\psi_O$ is ramified at $P$ exactly when $OP=T_P(X)$, and by the choice of $O$
such a tangent is neither inflectional nor multiple, so every ramification index
is $2$ and distinct ramification points give distinct tangents. Riemann--Hurwitz
gives
$$
\begin{aligned}
\#\{\text{tangents through }O\text{ other than }T_O(X)\}
&=2g(X)-2+2(d-1)\\
&=d^2-d-2\\
&=(d+1)(d-2),
\end{aligned}
$$
which is Reiser's rearrangement of $(d-1)(d-2)-2=(d-1)(-2)+\deg R$.

:::

:::

::: {.pf-step #s8}
The morphism $\varphi:X\to L$ of part (a) has degree
$$
d(d-1).
$$

::: pf-proof

This step is the card's own.
Choose a general point $Q\in L$.  We may arrange that $Q\notin X$ and that
$Q$ lies on no inflectional or multiple tangent.  By step [](#s6){.pf-ref} there are
exactly $d(d-1)$ tangent lines to $X$ through $Q$.

The fibre $\varphi^{-1}(Q)$ consists exactly of their tangency points, since
$$
\varphi(P)=Q
\quad\Longleftrightarrow\quad
Q\in T_P(X).
$$
The choice of $Q$ makes those points distinct and unramified in this fibre.
Thus a general fibre has $d(d-1)$ points and
$$
\deg\varphi=d(d-1).
$$

Reiser, Exercise IV.2.3(e), printed p. 357: $\varphi^{-1}(P)$ is exactly the set of points $Q\in X$ with $P\in T_Q(X)$, which by part (c) has $d(d-1)$ points for a general $P$, so $\deg\varphi=d(d-1)$.
:::

:::

::: {.pf-step #s9}
The inflection points of $X$, counted with weight
$$
I_P(X,T_P(X))-2,
$$
have total weight
$$
3d(d-2).
$$

::: pf-proof

This step is the card's own.
Choose the line $L$ in part (a) generally enough that it contains no
inflection point.  Since it is not tangent to $X$, it meets $X$ transversely
in exactly $d$ points.  At each $P\in X\cap L$, step [](#s2){.pf-ref} gives
$$
e_P(\varphi)=2,
$$
so these points contribute $d$ to the ramification divisor.

If $P\notin L$ is an inflection point with
$$
r=I_P(X,T_P(X))\geq3,
$$
step [](#s2){.pf-ref} gives
$$
e_P(\varphi)=r-1,
$$
so its ramification contribution is $r-2$.  Step [](#s2){.pf-ref} shows that there is no
other ramification.

By step [](#s8){.pf-ref} and Riemann--Hurwitz,
$$
\begin{aligned}
\deg R_\varphi
&=2g(X)-2+2d(d-1)\\
&=d^2-3d+2d^2-2d\\
&=3d^2-5d.
\end{aligned}
$$
Subtracting the $d$ contributions from $X\cap L$ leaves
$$
3d^2-6d=3d(d-2),
$$
which is exactly the asserted weighted inflection count.

Reiser, Exercise IV.2.3(e), printed p. 357: Hurwitz gives $\deg R=(d-1)(d-2)-2+2d(d-1)=3d^2-5d$, and subtracting the $d$ points of $L\cap X$ leaves $3d^2-6d=3d(d-2)$.
:::

:::

::: {.pf-step #s10}
An ordinary inflection point of $X$ maps to an ordinary cusp of
$X^*$.

::: pf-proof

This step is the card's own.
At an ordinary inflection point, step [](#s1){.pf-ref} has
$$
h(t)=a_3t^3+O(t^4),
\qquad a_3\ne0.
$$
Hence the local parametrization of the dual branch is
$$
u=-3a_3t^2+O(t^3),
\qquad
v=2a_3t^3+O(t^4).
$$
Thus the branch has multiplicity $2$ and its tangent line meets it with
multiplicity $3$.  Equivalently, after formal changes of local coordinates it
has parametrization $(t^2,t^3)$, the ordinary cusp.

Reiser, Exercise IV.2.3(e), printed p. 357, obtains the same branch in parametrized form: at an ordinary inflection point $X$ is cut out by $x-uy^3$ with $u$ a unit, so $X$ is formally parametrized by $(ut^3,t)$ and the dual curve by
$$
t\longmapsto[1:3ut^2+u't^3:-(4ut^3+u't^4)]=[1:t^2(3u+u't):-t^3(4u+u't)],
$$
"which is a cusp under any reasonable definition (Hartshorne does not supply one)". The multiplicities read off here are the definition the card uses.
:::

:::

::: {.pf-step #s11}
The Gauss map $\gamma:X\to X^*$ is the normalization of $X^*$.
If $P$ is a hyperflex, then $\gamma(P)$ is a unibranch multiplicity-$3$
singularity with $\delta=3$.

::: pf-proof
The Gauss map is nonconstant by the argument of step [](#s3){.pf-ref}, hence finite onto
its image.  By step [](#s4){.pf-ref} there are only finitely many multiple tangents, so a
general point of $X^*$ is the tangent line at exactly one point of $X$.
Therefore $\gamma$ is generically one-to-one and hence birational.  Since
$X$ is nonsingular and thus normal, the finite birational map
$$
\gamma:X\longrightarrow X^*
$$
is the normalization morphism.

Now suppose
$$
I_P(X,T_P(X))=4.
$$
Step [](#s1){.pf-ref} gives
$$
h(t)=a_4t^4+O(t^5),
\qquad a_4\ne0,
$$
and hence
$$
u=-4a_4t^3+O(t^4),
\qquad
v=3a_4t^4+O(t^5).
$$
This is one branch, of multiplicity $3$.  Its value semigroup has initial
values $3$ and $4$.  Hence it contains the numerical semigroup
$\langle3,4\rangle$, which contains every integer at least $6$.  Conversely,
no element of the completed local ring can have valuation $1$ or $2$, and an
element of valuation $5$ cannot occur: below valuation $6$, the only
nonconstant monomials in the two local coordinates have the distinct
valuations $3$ and $4$, so there are no equal leading terms whose
cancellation could create valuation $5$.  Thus the only gaps are
$$
1,2,5,
$$
and the normalization quotient has length
$$
\delta=3.
$$
This is the $E_6$ cusp (characteristic parametrization $(t^3,t^4)$).

The first paragraph is Reiser, Exercise IV.2.3(f), printed p. 357: "it's clear that $\varphi:X\to X^*$ is finite, as it's a nonconstant map of curves", and "since we're in characteristic zero, this implies that $\varphi$ is in fact birational. As $X$ is smooth, it is normal, so by the universal property of normalization we find that $\varphi:X\to X^*$ is actually the normalization". The second paragraph, the local form of $X^*$ at a hyperflex and its $\delta$-invariant, is the card's own: Reiser's part (h), printed p. 358, only substitutes $d=4$ in part (f), and Bergvall's §2.2, printed pp. 3--4, counts hyperflex lines as bitangents but says nothing about the singularity of the dual curve there.
:::

:::

::: {.pf-step #s12}
If $X^*$ has only nodes and ordinary cusps, then the number $b$ of
bitangents in the strict sense of part (b) is
$$
b=\frac12d(d-2)(d-3)(d+3).
$$

::: pf-proof

This step is the card's own.
Under the stated hypothesis every inflection point is ordinary.  Indeed, if
its tangent contact had order $r\geq4$, step [](#s1){.pf-ref} would give a dual branch of
multiplicity $r-1\geq3$, which is neither a node nor an ordinary cusp.
Therefore step [](#s9){.pf-ref} shows that the number of cusps of $X^*$ is
$$
\kappa=3d(d-2).
$$

Under the stated singularity hypothesis, a multiple tangent cannot contain
an inflection point: otherwise the corresponding point of $X^*$ would have
at least one singular branch together with another branch, hence would be
neither a node nor an ordinary cusp.  It also cannot be tangent at three or
more distinct points, because step [](#s4){.pf-ref} would give an ordinary multiple
point with at least three branches.  Thus every multiple tangent is tangent
at exactly two non-inflection points, i.e. is a strict bitangent, and step
[](#s4){.pf-ref} shows that it gives an ordinary node of $X^*$.  Conversely, by step
[](#s11){.pf-ref} the two branches of a node lift under the normalization to two distinct
points of $X$ having the same tangent line.  Hence the number of nodes is
exactly $b$.

Put
$$
m=\deg X^*=d(d-1).
$$
The arithmetic genus of the plane curve $X^*$ is
$$
p_a(X^*)=\frac{(m-1)(m-2)}2.
$$
Since $X$ is its normalization, [[P-AGH418ARITHGENUSSINGULAR|Exercise
IV.1.8]] gives
$$
g(X)=p_a(X^*)-b-\kappa,
$$
because a node and an ordinary cusp each have $\delta$-invariant $1$.
Substituting
$$
g(X)=\frac{(d-1)(d-2)}2,
\qquad
m=d(d-1),
\qquad
\kappa=3d(d-2)
$$
gives
$$
\begin{aligned}
2b
&=(m-1)(m-2)-(d-1)(d-2)-6d(d-2)\\
&=d^4-2d^3-9d^2+18d\\
&=d(d-2)(d-3)(d+3).
\end{aligned}
$$
Dividing by $2$ proves part (f).

Reiser, Exercise IV.2.3(f), printed p. 357, computes the same number by the same route: $p_a(X^*)=p_a(X)+I+B$ from (IV, Ex. 1.8), with $p_a(X^*)=\binom{d(d-1)-1}{2}$ and $I=3d(d-2)$ from (e), so
$$
B=\binom{d(d-1)-1}{2}-\binom{d-1}{2}-3d(d-2),
$$
"which after a little light algebra may be confirmed to be $\frac12 d(d-2)(d-3)(d+3)$". The identification this step proves --- that the nodes of $X^*$ are the strict bitangents and its ordinary cusps the ordinary inflections --- is what lets his $I$ and $B$ be read as those two classes.
:::

:::

::: {.pf-step #s13}
A plane cubic has exactly nine inflection points, all ordinary, and
the line through any two of them meets the cubic in a third inflection point.

::: pf-proof
Reiser, Exercise IV.2.3(g), printed p. 358. Part (e) with $d=3$ gives the total
weight
$$
3\cdot3\cdot(3-2)=9,
$$
and, since a tangent line to a nonsingular cubic has contact at most $3$ by
Bézout --- a sentence of the card's own, not Reiser's --- every weight $r-2$ is
exactly $1$: there are exactly nine inflection points, all ordinary.

For the second sentence, fix one inflection point as the zero of the group law on
the cubic. In (II, Ex. 6.6) a point has order $3$ in that group law exactly when
it is an inflection point, and three points $P,Q,R$ are collinear exactly when
$P+Q+R=0$. So for distinct inflection points $P,Q$ and the third point $R$ of the
line through them, $R=-P-Q$ is again $3$-torsion, hence again an inflection
point.

:::

:::

::: {.pf-step #s14}
For an arbitrary nonsingular plane quartic, if $h$ is the number of
hyperflex lines and $b$ the number of strict bitangents, then
$$
b=28-h.
$$
Consequently there are always exactly $28$ bitangent lines when
hyperflex lines are counted as bitangents.

::: pf-proof
Reiser, Exercise IV.2.3(h), printed p. 358, substitutes $d=4$ in part (f):
$$
\frac12\cdot4\cdot2\cdot1\cdot7=28.
$$
Under the hypothesis of part (f) every inflection is ordinary and every multiple
tangent is a strict bitangent, so this is the count for a general smooth quartic.

For an arbitrary smooth quartic, hyperflexes included, the count is Bergvall's.
His definition, §2.2, printed p. 3, is the one part (h) needs: "a bitangent to a
plane quartic $C$ is a line $L$ which is tangent to $C$ at two points or has
contact order $4$ at one point", a line of the second kind being a hyperflex line.
For such a line the divisor $L.C=2P+2Q$ is canonical, with $P=Q$ allowed, so the
class of $P+Q$ is a theta characteristic, and "this construction yields a bijection
between the set of bitangents of $C$ and the set of odd theta characteristics of
$C$" (printed p. 4); a curve of genus $g$ has $2^{2g}$ theta characteristics, of
which $2^{g-1}(2^g-1)$ are odd, so for $g=3$ there are $64$ and $28$. That is
Theorem 2.2 there, printed p. 4, attributed to Plücker and Jacobi, and it counts
$28$ for every smooth quartic, hyperflex or not.

For the formula, write $f$ for the number of ordinary flexes. Then $f+2h=24$ by
step [](#s9){.pf-ref}, and by step [](#s11){.pf-ref} the singular points of $X^*$
are the $b$ nodes of strict bitangents, the $f$ ordinary cusps of flexes and the
$h$ hyperflex points, each of $\delta$-invariant $3$; the genus formula of (IV,
Ex. 1.8) gives $3=55-(b+f+3h)$, whence $b=52-f-3h=28-h$. This computation is the
card's own, as is the local analysis of step [](#s11){.pf-ref} that it uses.

:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, and [](#s3){.pf-ref} prove part (a), step [](#s4){.pf-ref} proves part (b), steps [](#s5){.pf-ref} and [](#s6){.pf-ref}
prove part (c), step [](#s7){.pf-ref} proves part (d), steps [](#s8){.pf-ref}, [](#s9){.pf-ref}, and [](#s10){.pf-ref} prove part (e),
step [](#s12){.pf-ref} proves part (f), step [](#s13){.pf-ref} proves part (g), and step [](#s14){.pf-ref} proves
the count in part (h), and step [](#s11){.pf-ref} proves its parenthetical.
:::

:::
:::

::: {.remark title="Published solution"}
B. Reiser, *Hartshorne Solutions* (15 February 2022), Exercise IV.2.3, printed pp. 354--358, solves every part: (a) at printed pp. 355--356, by the local equation $f=x+ax^2+bxy+cy^2+\cdots$; (b) at pp. 356--357, by a formal parametrization of $X$ and its dual; (c) and (d) at p. 357, by Riemann--Hurwitz for the projection from a point off $X$ and from a general point of $X$; (e) at p. 357, by the degree of the Gauss map $d(d-1)$ and the weighted count $3d(d-2)$; (f) at p. 357, by $X\to X^*$ being the normalization and $p_a(X^*)$ computed twice; (g) at p. 358, by the group law on the cubic and (II, Ex. 6.6); and (h) at p. 358, by substituting $d=4$ in (f).

O. Bergvall, *Arithmetic and topology of classical structures associated to plane quartics* (arXiv:2106.13072v1, 24 June 2021), §2.2, printed pp. 3--4, states the count of part (h) in the convention part (h) needs: a bitangent is a line tangent at two points *or* of contact order $4$ at one point, and Theorem 2.2 (printed p. 4, after Plücker and Jacobi) counts $28$ for every smooth quartic. He also records the bijection with the odd theta characteristics, $2^{g-1}(2^g-1)=28$ of them for $g=3$, which is why a hyperflex does not change the count.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.2.3, printed pp. 212--215, identifies the multiple points of the dual curve with the lines tangent at several points or tangent with higher contact, so that the dual map is ramified exactly at inflection points, and counts inflection points and bitangents by projecting from a general point.
:::
