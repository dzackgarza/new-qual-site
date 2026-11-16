---
schema: qual/card@1
id: P-AGH537EMBRESOLUTION
kind: problem
title: Embedded resolutions and $\delta_P$ for a list of plane curve singularities
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.3.7, the retained Egbert/Singular resolution transcript,
    the preceding analytic-versus-resolution equivalence card, and the corpus
    delta/multiplicity formula. The retained transcript correctly identifies
    the common resolution configuration of (a), (b), and (d), but its final
    diagnostic command accidentally changes (d) from x^3+y^5+y^6 to
    x^4+y^5+y^6 and therefore raises a spurious doubt. Direct blowup charts
    show that (a), (b), and (d) are equivalent; (c) and (e) each have a
    different embedded-resolution pattern. The multiplicity sequences give
    delta values 4,4,3,4,4 respectively.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.3,
    exercise 3.7, printed page 395, with Remark 3.9.4 on printed page 408 for
    the meaning of equivalence, and the delta formula of Example 3.9.3,
    printed page 408. Rechecked the first blowups and the multiplicities: for
    (a), x = uv, y = v gives v^3(u^3+v^2); for (e), x^3+xy^3+y^5 gives
    v^3(u^3+uv+v^2), whose tangent cone is v^2 and which is smooth at the
    origin, so delta = 3 + 1 = 4 as the card says. Searched outside the twelve
    retained sets: NTU 2020, Exercise 7 of section 3, PDF pp. 12-13
    (tmp/sources/ntu-ag2-chapter5.pdf), has resolutions, the same five delta
    values 4,4,3,4,4 and the same equivalence classes; Yang Pi-Yeh,
    Hartshorne Solutions, printed pp. 108-109
    (tmp/sources/lfwin-hartshorne-solutions.pdf), writes the transforms
    without delta or equivalence. Not checked: whether a general ground field
    lacks the square root of -1 used in the chart of (e); the book assumes k
    algebraically closed, and over such a field the three points on the
    exceptional curve exist.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Page check against the text version: Remark 3.9.4 and the delta formula of
    Example 3.9.3 both stand between its markers for PDF pages 408 and 409, so
    their printed page is 393, and the "printed page 408" of the 2026-11-11
    note above is the PDF page; the remark below now cites printed p. 393 and
    gives the PDF page in brackets. The 2026-11-11 note had been rewritten in
    place; it is restored to the text it was dated with, and the corrections
    are in this event. A sentence that rewrite had added, that the equivalence
    of (a), (b) and (d) needs 3 and 5 invertible, is withdrawn: step abd-equivalent proves the equivalence from the
    embedded-resolution data of (3.9.4), the same succession of centres with
    the same multiplicities, incidences and tangencies, and divides by nothing
    and asks nothing of the ground field, while the formal changes
    x -> x(1+x)^{1/3} and y -> y(1+y)^{1/5} are only the alternative route that
    the step itself restricts to characteristic zero. Rechecked this pass: the
    first strict transform of (e) is v^3(u^3+uv+v^2), whose lowest part is
    v(u+v), two distinct linear forms, so the infinitely near point is an
    ordinary node; NTU 2020, Exercise 7 of section 3, PDF pp. 12-13 of
    tmp/sources/ntu-ag2-chapter5.pdf, text version
    tmp/sources/ntu-ag2-chapter5.md, whose page markers are coarse, stops at a
    nonsingular strict transform, gives delta 4,4,3,4,4 and puts (a), (b), (d)
    in one class; Yang Pi-Yeh, exercise 5.3.7, printed p. 108, PDF
    tmp/sources/lfwin-hartshorne-solutions.pdf with text version
    tmp/sources/lfwin-hartshorne-solutions.md, writes the third blowup of (a),
    (b) and (d) and says that one more gives the normal crossings, closes "So
    (a),(b),(d) are equivalent to each other. And (c),(e) are not equivalent to
    any others", and gives no delta. Both descriptions on the card stand. Not
    checked: Egbert's Singular transcript was not re-read in this pass; the
    pagination rests on the text version alone, no printed copy being
    consulted; and the equivalence is read off the displayed chart data rather
    than derived from a formal classification of the germs.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Partially transcribed for issue #121 from Algebraic Geometry II, National
    Taiwan University, 2020 Spring, Chapter V Surfaces homework solutions,
    Exercise 7 of §3 (Ping-Hsun Chuang), PDF pp. 12-13 of
    tmp/sources/ntu-ag2-chapter5.pdf, read in the text version
    tmp/sources/ntu-ag2-chapter5.md; its page markers are coarse, so the pages
    were read off the PDF, as the remark records. Transcribed onto the steps:
    the six coordinate computations, which agree with the card's up to the
    naming of the chart coordinates, each step now quoting the equation the
    source prints beside the card's; the multiplicities 3 and 2 of each germ;
    the five values of delta_P, printed there as 1/2*3*2 + 1/2*2*1 = 4 for
    (a), (b), (d), (e) and 1/2*3*2 = 3 for (c); and the classification into
    (a),(b),(d) against (c) and (e), which the entry states at the end of its
    five parts. The source does not prove what it concludes: its resolution
    graphs are pictures in the extraction, five image blocks, and the entry
    stops when the strict transform is nonsingular, so neither the embedded
    resolution in the sense of 3.9.4 nor the argument from the data to the
    classification is published there, and steps a-third-fourth-blowup,
    b-third-fourth-delta, d-third-fourth-delta, c-resolution-delta-three,
    e-resolution-delta-four, abd-equivalent, c-not-equivalent and
    e-not-equivalent remain the card's, marked as such on the steps. The
    identification of the double point of (e) as a node, and the reading of
    delta_P off the multiplicities by 3.9.3, are likewise the card's, the
    source giving only the multiplicities and the numbers. Checked against
    Hartshorne V.3.7, printed p. 395, and (3.9.3), (3.9.4) on printed p. 393.
    Not checked: the five resolution graphs, which are images in the text
    version and were not read as pictures; Yang Pi-Yeh's entry and Egbert's
    Singular session, which the previous pass read and which were not re-read
    this pass; and any printing of the NTU set other than the text version
    beside its PDF.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's findings on this batch, repaired here; the event of 2026-11-16
    above is left as written. Page corrections in Exercise 7 of §3 of the
    National Taiwan University set: parts (a) and (b) are both on PDF p. 12,
    part (b) having been cited at p. 13, and part (c)'s chart and equation are
    on PDF p. 12 with only its delta line on p. 13, the whole part having been
    cited at p. 13. Parts (d) and (e) are on p. 13 as cited. The rendered text
    is also reduced to mathematics and citation: the sentences saying what the
    source stops at, which blowups are the card's, and how its page markers
    stand leave the solution and the remark (QUAL-08), and the remark opener
    takes the attribute form of STYLE-01. What remains the card's own, and is
    recorded in COMPLAINTS.md rather than on the card, is unchanged: the
    blowups at smooth points that turn the resolution of each curve into an
    embedded resolution, the identification of the double point of (e) as a
    node, and the arguments from the source's multiplicity data to the
    equivalence class of (a), (b), (d) and to the separations of (c) and (e).
---

::: {.problem}
For each of the following singularities at $(0,0)$ in the plane, give an embedded resolution, compute $\delta_P$, and decide which ones are equivalent.

(a) $x^3+y^5=0$.

(b) $x^3+x^4+y^5=0$.

(c) $x^3+y^4+y^5=0$.

(d) $x^3+y^5+y^6=0$.

(e) $x^3+x y^3+y^5=0$.
:::

::: {.solution}
All blowups below are point blowups of the ambient plane or of the smooth
surface obtained at the preceding stage. We keep blowing up after the strict
transform becomes smooth whenever this is needed to make the total transform
a simple normal-crossings divisor. For the delta invariant we use
[[D-CRVPLSING]]:
$$
\delta_P
=
\sum_Q\binom{m_Q}{2},
$$
where only singular points $Q$ of the successive strict transforms
contribute, since a smooth point has multiplicity one.

The blowups of the five germs, the multiplicities they produce and the five values of $\delta_P$ are Exercise 7 of §3 of Algebraic Geometry II, National Taiwan University, 2020 Spring, *Chapter V Surfaces* homework solutions (course of Chin-Lung Wang), the solution of parts (a) to (e) by Ping-Hsun Chuang, PDF pp. 12--13; each step below that computes a transform or a value of $\delta_P$ cites that entry and quotes its equation.

::: pf

::: {.pf-step #a-first-blowup}
For (a),
$$
C_a:\quad x^3+y^5=0,
$$
the first blowup has strict-transform equation
$$
u^3+v^2=0
$$
in the chart
$$
x=uv,
\qquad
y=v.
$$

::: pf-proof
Substitution gives
$$
x^3+y^5
=
v^3(u^3+v^2).
$$
Thus the exceptional curve is
$$
E_1:(v=0)
$$
and the strict transform is
$$
C_{a,1}:(u^3+v^2=0).
$$
The point
$$
Q_1=(0,0)
$$
is its unique point over the origin. It has multiplicity $2$, and its
tangent is $v=0$, the exceptional curve $E_1$.

The chart and the transformed equation are Exercise 7 of §3, part (a), PDF p. 12: it writes the chart as $(y,s)=(y,x/y)$, that is $x=sy$, and the equation as $s^3+y^2=0$ with $E_1=\{y=0\}$, and says that the curve has one singularity, of multiplicity $2$ at $(0,0)$. Its $s$ is this card's $u$.
:::

:::

::: {.pf-step #a-second-blowup}
Blowing up $Q_1$ in (a), with
$$
v=uw,
$$
gives
$$
C_{a,2}:\quad u+w^2=0.
$$
This strict transform is smooth but passes through the intersection of the
two exceptional curves and is tangent to the new exceptional curve.

::: pf-proof
Substitution gives
$$
u^3+u^2w^2
=
u^2(u+w^2).
$$
Hence the new exceptional curve is
$$
E_2:(u=0),
$$
while the strict transform of $E_1$ is
$$
E_1':(w=0).
$$
The curve $u+w^2=0$ is smooth at their intersection $(0,0)$, but its tangent
is $u=0=E_2$. Thus the total transform is not yet normal crossings.

The second chart of Exercise 7 of §3, part (a), PDF p. 12, is $(v,s)=(y/s,s)$, and its equation there is $s+v^2=0$ with $E_1=\{v=0\}$ and $E_2=\{s=0\}$; its $s$ is the $u$ above and its $v$ is $w$.
:::

:::

::: {.pf-step #a-third-fourth-blowup}
The third blowup in (a) produces a point at which the strict transform
and two exceptional curves meet with three distinct tangent directions; a
fourth blowup separates these three branches and completes an embedded
resolution.

::: pf-proof
At the point of step [](#a-second-blowup){.pf-ref} use
$$
u=st,
\qquad
w=s.
$$
Then
$$
u+w^2
=
s(t+s),
$$
so the strict transform is
$$
C_{a,3}:(t+s=0).
$$
In this chart the new exceptional curve is $E_3:(s=0)$ and the strict
transform of $E_2$ is $E_2':(t=0)$. At $(s,t)=(0,0)$ the three curves
$$
s=0,
\qquad
t=0,
\qquad
t+s=0
$$
have distinct tangent directions. A fourth blowup at this triple point
therefore makes their strict transforms meet the new exceptional $E_4$ at
three distinct points. All remaining intersections are transverse, so the
total transform is simple normal crossings.

The fourth blowup is what makes the reduced total transform a normal-crossings divisor, which the resolution of the curve in Exercise 7 of §3, part (a), does not ask for.
:::

:::

::: {.pf-step #a-delta-four}
For (a),
$$
\boxed{\delta_P(C_a)=4}.
$$

::: pf-proof
The strict transform is singular only at the original point, of multiplicity
$3$, and at $Q_1$, of multiplicity $2$. All later centres lie on a smooth
strict transform. Hence
$$
\delta_P(C_a)
=
\binom32+\binom22
=
3+1
=4.
$$

Exercise 7 of §3, part (a), PDF p. 12, computes $\delta_p=\tfrac12 3\cdot 2+\tfrac12 2\cdot 1=4$ from the same two multiplicities.
:::

:::

::: {.pf-step #b-first-two-blowups}
For (b),
$$
C_b:\quad x^3+x^4+y^5=0,
$$
the first two strict transforms are
$$
u^3+u^4v+v^2=0
$$
and
$$
u+w^2+u^3w=0.
$$

::: pf-proof
The same first chart $x=uv$, $y=v$ gives
$$
x^3+x^4+y^5
=
v^3(u^3+u^4v+v^2).
$$
The unique point over the origin again has multiplicity $2$ and tangent
$v=0$. Blowing it up with $v=uw$ gives
$$
u^3+u^5w+u^2w^2
=
u^2(u+w^2+u^3w).
$$
Thus the second strict transform is smooth, passes through $E_1'\cap E_2$,
and is tangent to $E_2:(u=0)$ exactly as in (a).

Both transforms are Exercise 7 of §3, part (b), PDF p. 12: in the chart $x=sy$ it prints $s^3+s^4y+y^2=0$, of multiplicity $2$ at the origin, and in the chart $(v,s)=(y/s,s)$ it prints $s+vs^3+v^2=0$, nonsingular, with the same two exceptional curves; its $s$ is the $u$ above and its $v$ is $w$.
:::

:::

::: {.pf-step #b-third-fourth-delta}
The third and fourth blowups for (b) have the same incidence pattern
as for (a), and
$$
\boxed{\delta_P(C_b)=4}.
$$

::: pf-proof
At the third centre put $u=st$, $w=s$. The second strict-transform equation
becomes
$$
s\bigl(t+s+s^3t^3\bigr)=0,
$$
so the third strict transform is
$$
t+s+s^3t^3=0.
$$
Its tangent at the origin is $t+s=0$, distinct from the two exceptional
directions $s=0$ and $t=0$. Thus, exactly as in step [](#a-third-fourth-blowup){.pf-ref}, a fourth blowup
of the triple point completes the embedded resolution.

The only singular strict transforms have multiplicities $3$ and $2$.
Therefore
$$
\delta_P(C_b)=\binom32+\binom22=4.
$$

Exercise 7 of §3, part (b), PDF p. 12, computes the same value, $\tfrac12 3\cdot2+\tfrac12 2\cdot1=4$.
:::

:::

::: {.pf-step #d-first-two-blowups}
For (d),
$$
C_d:\quad x^3+y^5+y^6=0,
$$
the first two strict transforms are
$$
u^3+v^2+v^3=0
$$
and
$$
u+w^2+uw^3=0.
$$

::: pf-proof
The first blowup gives
$$
x^3+y^5+y^6
=
v^3(u^3+v^2+v^3),
$$
so the infinitely near point again has multiplicity $2$ and tangent $v=0$.
Under the second blowup $v=uw$ one obtains
$$
u^3+u^2w^2+u^3w^3
=
u^2(u+w^2+uw^3).
$$
The second strict transform is smooth and tangent to $E_2:(u=0)$ at
$E_1'\cap E_2$, just as in (a) and (b).

These are the transforms of Exercise 7 of §3, part (d), PDF p. 13: $s^3+y^2+y^3=0$, of multiplicity $2$, in the chart $x=sy$, and $s+v^2+sv^3=0$, nonsingular, in the chart $(v,s)=(y/s,s)$.
:::

:::

::: {.pf-step #d-third-fourth-delta}
The third and fourth blowups for (d) again have the same incidence
pattern as (a), and
$$
\boxed{\delta_P(C_d)=4}.
$$

::: pf-proof
With $u=st$, $w=s$, the second strict-transform equation becomes
$$
s\bigl(t+s+s^3t\bigr)=0.
$$
Thus the third strict transform has tangent $t+s=0$ at the triple point of
the two relevant exceptional components, and one final blowup separates the
three distinct directions. The singular multiplicity sequence is again
$$
3,2,
$$
so
$$
\delta_P(C_d)=4.
$$

Exercise 7 of §3, part (d), PDF p. 13, computes $\tfrac12 3\cdot 2+\tfrac12 2\cdot 1=4$ from the same two multiplicities.
:::

:::

::: {.pf-step #abd-equivalent}
The singularities (a), (b), and (d) are equivalent.

::: pf-proof
Steps [](#a-first-blowup){.pf-ref}, [](#a-second-blowup){.pf-ref} and [](#a-third-fourth-blowup){.pf-ref}, steps [](#b-first-two-blowups){.pf-ref} and [](#b-third-fourth-delta){.pf-ref}, and steps [](#d-first-two-blowups){.pf-ref} and [](#d-third-fourth-delta){.pf-ref} exhibit the same succession of
centres, exceptional-component incidences, tangencies, and multiplicities:
the curve has multiplicities $3,2,1,1$ at the four centres; after the first
blowup it is a double point tangent to $E_1$; after the second it is smooth,
tangent to $E_2$, and passes through $E_1'\cap E_2$; after the third it
passes through a triple point with a third distinct tangent direction; the
fourth blowup separates the three branches.

This is the same embedded-resolution data in the sense of (3.9.4), so the
three singularities are equivalent. In characteristic zero this also follows
from the formal changes
$$
x\mapsto x(1+x)^{1/3}
$$
for (b) and
$$
y\mapsto y(1+y)^{1/5}
$$
for (d), which analytically identify both germs with (a).

Exercise 7 of §3 closes, PDF p. 13, "By the resolution graph, we conclude that the sigularity of (0,0) of (a) (b) (d) are equivalent and (c) (e) are different from the others". Its transforms for the three germs, quoted on steps [](#a-first-blowup){.pf-ref} to [](#d-first-two-blowups){.pf-ref}, coincide, and its multiplicities are $3$ and $2$ for each.
:::

:::

::: {.pf-step #c-first-blowup}
For (c),
$$
C_c:\quad x^3+y^4+y^5=0,
$$
the first blowup gives the smooth strict transform
$$
u^3+v+v^2=0,
$$
which is tangent to the exceptional curve.

::: pf-proof
With $x=uv$, $y=v$,
$$
x^3+y^4+y^5
=
v^3(u^3+v+v^2).
$$
The strict transform is smooth at the origin because the coefficient of
$v$ in its linear term is $1$. Its tangent is $v=0=E_1$.

This is Exercise 7 of §3, part (c), PDF p. 12, which in the chart $x=sy$ prints $s^3+y+y^2=0$ and records that the curve is nonsingular there and that this one blowup resolves it.
:::

:::

::: {.pf-step #c-resolution-delta-three}
Three further blowups give an embedded resolution of (c), and
$$
\boxed{\delta_P(C_c)=3}.
$$

::: pf-proof
Blow up the tangency in step [](#c-first-blowup){.pf-ref} by setting $v=uw$. Then
$$
u^3+uw+u^2w^2
=
u(u^2+w+uw^2),
$$
so the second strict transform is
$$
u^2+w+uw^2=0.
$$
It is smooth, tangent to the strict transform $E_1':(w=0)$, and passes
through $E_1'\cap E_2$.

Blow up this point with $w=us$. The equation becomes
$$
u\bigl(u+s+u^2s^2\bigr)=0,
$$
so the third strict transform has tangent $u+s=0$, distinct from the two
exceptional directions through the resulting triple point. A fourth blowup
separates these directions and gives simple normal crossings.

The curve itself was singular only at the original point, where its
multiplicity is $3$. Hence
$$
\delta_P(C_c)=\binom32=3.
$$

Exercise 7 of §3, part (c), PDF p. 13, prints $\delta_p=\tfrac12 3\cdot 2=3$.
:::

:::

::: {.pf-step #c-not-equivalent}
The singularity (c) is not equivalent to any of (a), (b), or (d).

::: pf-proof
After the first blowup, (c) is already smooth, whereas the strict transforms
of (a), (b), and (d) have multiplicity $2$. Thus their infinitely near
multiplicity data differ. Equivalently, the delta invariant of (c) is $3$
while that of (a), (b), and (d) is $4$.

Exercise 7 of §3 separates (c) from the others, PDF p. 13; the comparison above uses the multiplicities its transforms give.
:::

:::

::: {.pf-step #e-first-blowup-node}
For (e),
$$
C_e:\quad x^3+xy^3+y^5=0,
$$
the first blowup gives
$$
u^3+uv+v^2=0.
$$
At the infinitely near point this is an ordinary node with tangent cone
$$
v(u+v)=0.
$$

::: pf-proof
With $x=uv$, $y=v$,
$$
x^3+xy^3+y^5
=
v^3(u^3+uv+v^2).
$$
At $(u,v)=(0,0)$ the lowest-degree part is
$$
uv+v^2=v(u+v),
$$
the product of two distinct linear forms. Hence the strict transform has an
ordinary node of multiplicity $2$ there. One branch is tangent to the old
exceptional curve $E_1:(v=0)$ and the other has tangent $u+v=0$.

The transform is that of Exercise 7 of §3, part (e), PDF p. 13: in the chart $x=sy$ it prints $s^3+sy+y^2=0$ with $E_1=\{y=0\}$, says that the curve has one singularity, of multiplicity $2$, and then gives the next chart $(v,s)=(y/s,s)$, where the equation is $s+v+v^2=0$ and the curve is nonsingular.
:::

:::

::: {.pf-step #e-resolution-delta-four}
Two further blowups give an embedded resolution of (e), and
$$
\boxed{\delta_P(C_e)=4}.
$$

::: pf-proof
Blow up the node with $v=uw$. Then
$$
u^3+u^2w+u^2w^2
=
u^2(u+w+w^2).
$$
Thus the two branches meet the new exceptional curve $E_2:(u=0)$ at the
two distinct points
$$
w=0,
\qquad
w=-1.
$$
The point $w=-1$ is already transverse and lies away from $E_1'$. At
$w=0$, the strict transform passes through $E_1'\cap E_2$ with tangent
$u+w=0$, distinct from both exceptional directions. One final blowup at
this triple point separates the three components and completes the embedded
resolution.

The singular strict-transform multiplicities are $3$ at the origin and $2$
at the node after the first blowup. Hence
$$
\delta_P(C_e)
=
\binom32+\binom22
=4.
$$

Exercise 7 of §3, part (e), PDF p. 13, computes $\delta_p=\tfrac12 3\cdot2+\tfrac12 2\cdot1=4$.
:::

:::

::: {.pf-step #e-not-equivalent}
The singularity (e) is not equivalent to any of (a)--(d).

::: pf-proof
The first strict transform of (e) is a node and therefore has two analytic
branches. In contrast, (a), (b), (c), and (d) have a single branch through
every infinitely near point in their displayed resolutions. Correspondingly,
(e) reaches simple normal crossings after three blowups, while each of
(a)--(d) requires four in the embedded resolution described above.

Branch incidence and the exceptional-resolution graph are part of the
equivalence data in (3.9.4), so (e) is inequivalent to all four others.

Exercise 7 of §3 separates (e) from the others, PDF p. 13.
:::

:::

::: {.pf-step #summary-table}
The complete answer is
$$
\boxed{
\begin{array}{c|ccccc}
& (a)&(b)&(c)&(d)&(e)\\ \hline
\delta_P&4&4&3&4&4
\end{array}}
$$
and the equivalence classes are
$$
\boxed{\{(a),(b),(d)\},\qquad\{(c)\},\qquad\{(e)\}.}
$$

::: pf-proof
The delta values are steps [](#a-delta-four){.pf-ref}, [](#b-third-fourth-delta){.pf-ref}, [](#c-resolution-delta-three){.pf-ref}, [](#d-third-fourth-delta){.pf-ref}, and [](#e-resolution-delta-four){.pf-ref}.
Step [](#abd-equivalent){.pf-ref} proves the equivalence of (a), (b), and (d); steps [](#c-not-equivalent){.pf-ref} and
[](#e-not-equivalent){.pf-ref} separate (c) and (e) from all other classes.
:::

:::

::: pf-qed
Steps [](#a-first-blowup){.pf-ref}, [](#a-second-blowup){.pf-ref}, [](#a-third-fourth-blowup){.pf-ref}, [](#a-delta-four){.pf-ref}, [](#b-first-two-blowups){.pf-ref}, [](#b-third-fourth-delta){.pf-ref}, [](#d-first-two-blowups){.pf-ref}, [](#d-third-fourth-delta){.pf-ref}, [](#abd-equivalent){.pf-ref}, [](#c-first-blowup){.pf-ref}, [](#c-resolution-delta-three){.pf-ref}, [](#c-not-equivalent){.pf-ref}, [](#e-first-blowup-node){.pf-ref}, [](#e-resolution-delta-four){.pf-ref}, [](#e-not-equivalent){.pf-ref} and [](#summary-table){.pf-ref} give an embedded resolution, delta invariant, and
equivalence classification for every singularity in the exercise.
:::

:::
:::

::: {.remark title="Published solution"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.3, exercise 3.7, printed p. 395, with (3.9.3) and (3.9.4) on printed p. 393.

Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework solutions, Exercise 7 of §3, the solution of the five parts by Ping-Hsun Chuang, PDF pp. 12--13: in the chart $x=sy$ it prints $s^3+y^2$, $s^3+s^4y+y^2$, $s^3+y+y^2$, $s^3+y^2+y^3$ and $s^3+sy+y^2$ for (a) to (e), and in the chart $(v,s)=(y/s,s)$ the equations $s+v^2$, $s+vs^3+v^2$, $s+v^2+sv^3$ and $s+v+v^2$; it reads the multiplicities $3$ and $2$ off them, computes $\delta_P=\tfrac12\cdot3\cdot2+\tfrac12\cdot2\cdot1=4$ for (a), (b), (d) and (e) and $\tfrac12\cdot3\cdot2=3$ for (c), and concludes "By the resolution graph, we conclude that the sigularity of (0,0) of (a) (b) (d) are equivalent and (c) (e) are different from the others". Its letters differ from the ones above: its $s$ is $u$, and in the second chart its $v$ is $w$.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.3.7, printed p. 108, writes the successive strict transforms for the same five germs, three blowups for (a), (b) and (d), the third at a point where the strict transform is smooth, after which he writes "we may take one more blow-up to get the normal crossing" without carrying it out, and closes "So $(a),(b),(d)$ are equivalent to each other. And $(c),(e)$ are not equivalent to any others"; he gives no value of $\delta_P$.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.3.7, PDF pp. 279--282, is a Singular session: it prints the chart trees from `resolve`, gives no $\delta_P$, and ends "these commands should show that (d) is not equivalent".
:::
