---
schema: qual/card@1
id: E-HAT-4.1-1
kind: problem
title: "Alternative sum of maps and abelian $\\pi_n$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line. Correct. The interchange law is checked region by region: with `+` using the
    first coordinate and `+'` the second, the two composites `(f+g)+'(h+k)` and `(f+'h)+(g+'k)` put
    `f, g, h, k` on the same four half-size sub-cubes of `I^n` and send the same separating faces to
    `x_0`, so the maps agree on the nose, not merely up to homotopy. The two deductions are right and
    use the constant map as a two-sided identity up to homotopy relative to the boundary: with
    `g = h = 0` the interchange law gives `f +' k ~ f + k` in `pi_n`, and with `f = k = 0` it gives
    `g +' h ~ h + g`, which combined with the agreement of the two sums gives
    `[g] + [h] = [g] +' [h] = [h] + [g]`. The dimension restriction `n >= 2` is exactly what makes two
    coordinates available. No correction was needed.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.1 Exercise 1, printed p. 358; the statement
    matches the print. The proof is now written out rather than sketched: the sum formulas in both
    coordinates are displayed, the interchange identity is checked on each of the four quarters of
    $I^n$ with the value on each quarter named, the two-sided unit laws are given by explicit
    stretching homotopies that are stationary on $\partial I^n$, and the two deductions (agreement of
    the sums, and abelianness) are read off the interchange identity with $g=h=0$, respectively
    $f=k=0$. The case $n\ge2$ is stated and the passage from the second coordinate to an arbitrary
    coordinate is justified by permuting coordinates. No published solution of this exercise is in
    the retained sets — Sam's §4.1 covers 2, 3, 5, 10-15 and 19, DeMason's covers 2, 8 and 11, and
    Li's §4.1 Exercise 4.1.1 is blank — recorded in COMPLAINTS.md.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    The exercise is on printed p. 358. The published argument is Hatcher's printed treatment of the sum in $\pi_n$, pp. 340--341: the sum uses only the first coordinate, and the homotopy $f+g\simeq g+f$ is obtained by shrinking the two domains to disjoint subcubes of $I^n$, sliding them past each other using the remaining coordinates, and enlarging them again. The card's proof is that argument written with the coordinate bookkeeping made explicit: the same sliding homotopy with the pair of coordinates $(s_1,s_2)$ gives the interchange law $(f+g)+'(h+k)=(f+'h)+(g+'k)$, and specialising it ($h$ and $g$ constant) gives $f+'k\simeq f+k$ and $g+'h\simeq h+g$. Checked against the book: the printed definition of $+$ on p. 340, the printed commutativity homotopy and its remark that only $s_1$ and $s_2$ are needed, and the converse conventions for the relative groups on p. 343. Not claimed: that the book prints this exercise; it prints the homotopy the exercise asks to verify.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The proof is now the source's: tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics,
    2008), §4.3, printed pp. 87--88 — the composition laws $+_i$ on $[\Sigma^kX,Y]_0$ with their
    formula on p. 87, the commutation rule stated on p. 88 and left there to "unravel the
    definitions", and Proposition (4.3.1) with its proof on p. 88, which is the published proof of
    both deductions of the exercise. The four-quarter verification of the commutation rule is written
    out on the card, and the card says that this is the one step the source does not print. The
    previous route to the deductions — specialising the commutation rule at $g=h=0$ and at $f=k=0$
    and using the unit laws — is replaced by (4.3.1), which additionally gives the associativity the
    exercise does not ask for and the coincidence of all $n$ laws under relabelling. The stretching
    homotopy for the neutral element is kept, and the card says why: (4.3.1) takes the neutral
    elements as given and the source records the group axioms in one sentence on p. 87. Checked
    against Hatcher (2002), §4.1 Exercise 1, printed p. 358, quoted on the card, with Hatcher's $+$
    the first-coordinate sum of p. 340 and his commutativity homotopy on p. 341 a different argument
    for the last deduction. Not claimed: that tom Dieck states Hatcher's exercise.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Every citation on the card now names its source's text version. Hatcher is read in
    `tmp/sources/hatcher-2002-algebraic-topology.md` and tom Dieck in
    `tmp/sources/tomdieck-algebraic-topology-ranicki.md`, named in the solution where the two
    sources are first cited, in the closing quotation of the exercise, and in the remark. This was
    the only finding a local reader raised on the card; the mathematics is unchanged, and the
    reader's checks — tom Dieck §4.3 on printed pp. 87--88 with the commutation rule left to
    "unravel the definitions", the absence of any printed interchange in Davis--Kirk and May, and
    the four-quarter verification written out on the card — are recorded as holding. Not checked
    in this pass: the pagination of the 2008 bound volume, the pages quoted being those of the
    Ranicki translation's printed folios.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, third pass: the phrase "the Ranicki translation's printed folios" at the end
    of the `source-corrected` event of this date is false and is withdrawn. tom Dieck's *Algebraic
    Topology* (EMS Textbooks in Mathematics, 2008) is his own English text; "ranicki" is only in the
    file name of the reading copy, `tmp/sources/tomdieck-algebraic-topology-ranicki.md`, and names no
    translator. The pages quoted are those of tom Dieck's own printed folios, and every citation on
    the card already names the reading copy. Nothing in the statement or the proof changes.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    #123 transcription batch: the four-quarter verification, which this card had written out as
    its own because no publication prints one, is printed as the accepted answer 161511 (KReiser,
    posted 2012-06-22) to Math Stack Exchange question 161507, read in
    `tmp/sources/mse-161507-eckmann-hilton-higher-homotopy.md`. The answer writes both
    $(f\cdot g)\star(h\cdot i)$ and $(f\star h)\cdot(g\cdot i)$ as one piecewise map with the same
    four clauses the card's paragraph states, one per quarter of $I^2$, and concludes from the
    Eckmann--Hilton argument that the two compositions coincide and are commutative. It is a user
    answer and not a publication, and the card says so. Every step of the solution now names its
    source, numbered statement and printed page: the laws $+_i$ on $[\Sigma^kX,Y]_0$ and their
    formula, tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), §4.3, printed
    p. 87, read in the text version `tmp/sources/tomdieck-algebraic-topology-ranicki.md`; the
    commutation rule, same source, printed p. 88, where its printed proof is the words "unravel the
    definitions", with answer 161511 for the verification; Proposition (4.3.1) with its proof, the
    same printed page, for both deductions the exercise asks for; and the neutral element, which
    (4.3.1) takes as given and the source records in one sentence on printed p. 87, with the
    stretching homotopy the card writes out. The printed pages were confirmed against
    `tmp/sources/tomdieck-algebraic-topology-ranicki.pdf`: page 100 carries the running head
    "4.3. Suspension. Homotopy Groups 87" and the formula for $+_i$, and page 101 the running head
    "88 Chapter 4. Elementary Homotopy Theory", the commutation rule and (4.3.1) with its proof.
    Checked against Hatcher (2002), §4.1 Exercise 1 on printed p. 358, read in
    `tmp/sources/hatcher-2002-algebraic-topology.md` and confirmed at PDF page 367 = printed
    p. 358, with the first-coordinate sum on printed p. 340 = PDF page 349 and the commutativity
    homotopy on printed p. 341 = PDF page 350. Not claimed: that any publication prints the
    commutation rule's verification, and no page was read from a rendered image.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report on this round: the answer's formula was mistranscribed, and the rendered
    text carried curation. (1) Answer 161511 to question 161507 writes that both $(f\cdot g)\star(h\cdot i)$
    and $(f\star h)\cdot(g\star i)$ are the following piecewise map. The card, and the event of this
    day above, wrote the second term $(f\star h)\cdot(g\cdot i)$, which is not the answer's and does
    not match the right side of the exercise's own identity; both are corrected here, the rendered
    text to the answer's form and this day's event in place, and `COMPLAINTS.md` likewise. (2) Out of
    the rendered solution and remarks, and into this event, go: the `tmp/sources` paths; the words
    "that is the only step of the argument the source does not print"; "It is a user answer on Math
    Stack Exchange and not a publication"; the description of what tom Dieck prints and omits in the
    remark titled "Published solution", which is deleted whole; and the quotation of Hatcher's
    exercise, which the card's statement already carries. What remains in the rendered text is the
    mathematics with its citations by source, numbered statement and printed page, and the
    one-sentence marker on the unit law, which is the card's own argument. Where and how the sources
    were read: tom Dieck in `tmp/sources/tomdieck-algebraic-topology-ranicki.md`, §4.3 — the laws
    $+_i$ and their formula at the start of the section, then, after the marker "PDF pages 101-120"
    in the extraction, the sentence "We show in a moment that all these group structures coincide"
    with the commutation rule, the printed words "unravel the definitions" and Proposition (4.3.1)
    with its printed proof; the printed folios 87 and 88 confirmed on pages 100 and 101 of
    `tmp/sources/tomdieck-algebraic-topology-ranicki.pdf`. Answer 161511 read in full in
    `tmp/sources/mse-161507-eckmann-hilton-higher-homotopy.md`, where its four clauses are one
    displayed map and its last sentence invokes the Eckmann--Hilton argument; the answer is a user
    answer, and the published statement of the commutation rule with no printed verification is tom
    Dieck's, printed p. 88. Hatcher in `tmp/sources/hatcher-2002-algebraic-topology.md`, Exercise 1
    of §4.1 at the §4.1 exercises and the sum on printed p. 340, confirmed at pages 367 and 349 of
    `tmp/sources/hatcher-2002-algebraic-topology.pdf`. Davis--Kirk, Exercise 111 on printed p. 154,
    and May's *Concise Course*, Chapter 9 §1, print no two-coordinate identity, so a printed
    verification of the commutation rule was not located; `COMPLAINTS.md` records that on this date.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report on the round, correcting a rewrite made in place. The `source-checked` event
    of this date above is restored to the text it carried when written, which writes answer 161511's
    second term as $(f\star h)\cdot(g\cdot i)$; commit bce0d2e4c2 had changed that formula inside the
    event, and a dated event records what its session found, so the original stands as the record. The
    correction is this event: answer 161511 writes both $(f\cdot g)\star(h\cdot i)$ and
    $(f\star h)\cdot(g\star i)$ as its displayed piecewise map, the second being the right side of the
    exercise's own identity, and the rendered solution carries that form. Read again for this event in
    `tmp/sources/mse-161507-eckmann-hilton-higher-homotopy.md`: the answer is a user answer to Math
    Stack Exchange question 161507, its four clauses are one displayed map, and its last sentence
    invokes the Eckmann--Hilton argument. The same restoration and correction are recorded in a new
    `COMPLAINTS.md` record of this date. Nothing in the statement or the proof changes.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, tom Dieck (4.3.1) as its own step and the
    four-quarter computation as another. Re-checked: the $+_i$ formula gives maps of pairs because on
    the boundary some coordinate is 0 or 1; the stretching homotopy is continuous in $(s,t)$ and
    stationary on the boundary; the commutation rule holds on the nose, each of the four quarters
    agreeing; and the proposition's chain of equalities gives coincidence of the laws, the
    commutativity and the associativity, from which the two deductions follow. Added: the
    well-definedness on homotopy classes, the verification that the unit homotopy stays inside maps
    of pairs, and the observation that the same computation with coordinates $(i,j)$ gives
    $+_i=+_j$. No defect found in the statement, §4.1 Exercise 1 on printed p. 358; the card's remark
    on Hatcher's different commutativity homotopy stands.
review: draft
---

::: {.problem}
Suppose a sum $f +' g$ of maps $f, g: (I^n, \partial I^n) \to (X, x_0)$ is defined using a coordinate of $I^n$ other than the first coordinate as in the usual sum $f + g$.
Verify the formula $(f + g) +' (h + k) = (f +' h) + (g +' k)$, and deduce that $f +' k \simeq f + k$ so the two sums agree on $\pi_n(X, x_0)$, and also that $g +' h \simeq h + g$ so the addition is abelian.
:::

::: {.solution}
The group laws and the proposition are those of tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), §4.3, printed pp. 87--88; the four-quarter computation is also the accepted answer 161511 (2012-06-22) to Math Stack Exchange question 161507. The stretching homotopy and the presentation as numbered steps are the card's own. Throughout $n\ge2$, since for $n=1$ there is no coordinate other than the first.

::: pf

::: {.pf-step #laws}
For $1\le i\le n$ the formula
$$
(f+_ig)(s)=\begin{cases}f(\ldots,2s_i,\ldots),&s_i\le\tfrac12,\\ g(\ldots,2s_i-1,\ldots),&s_i\ge\tfrac12\end{cases}
$$
defines a sum on maps of pairs $(I^n,\partial I^n)\to(X,x_0)$, with $+_1$ Hatcher's $+$ and $+_2$ the exercise's $+'$.

::: pf-proof
Both halves are maps of $I^n$ into $X$, they agree on $s_i=\tfrac12$, and each is continuous; on the boundary $\partial I^n$ at least one coordinate is $0$ or $1$, so the corresponding input of $f$ or of $g$ lies on $\partial I^n$ and the value is $x_0$. Hence the sum is again a map of pairs. The identification of the cube model $\pi_n(X,x_0)=[I^n/\partial I^n,X]_0=[\Sigma^nS^0,X]_0$ with tom Dieck's is [loc. cit., p. 87], where $+_1$ and $+_2$ are the laws attached to the first and second coordinates.
:::

:::

::: {.pf-step #unit}
Each $+_i$ is well defined on $\pi_n(X,x_0)$, and the class of the constant map is a two-sided unit for it.

::: pf-proof
A homotopy of representatives through maps of pairs induces a homotopy of $+_i$-sums, since the formula is built from the representatives by continuous reparametrisation of coordinates, so $+_i$ passes to homotopy classes. For the unit, if $0$ denotes the constant map at $x_0$ then $f+_i0$ is homotopic to $f$ through maps of pairs by the stretching homotopy
$$
H_t(s)=f\Bigl(s_1,\ldots,\frac{2s_i}{1+t},\ldots,s_n\Bigr)\text{ for } s_i\le\frac{1+t}{2},\qquad H_t(s)=x_0\text{ otherwise},
$$
which is continuous in $(s,t)$, starts at $f+_i0$, ends at $f$, and is stationary on $\partial I^n$ because $f$ is a map of pairs; the same formula with $0+_if$ gives the other side.
:::

:::

::: {.pf-step #commutation}
$(f+g)+'(h+k)=(f+'h)+(g+'k)$ holds as an identity of maps, not merely up to homotopy.

::: pf-proof
Split $I^n$ according to $s_1\lessgtr\tfrac12$ and $s_2\lessgtr\tfrac12$. On $s_1\le\tfrac12,s_2\le\tfrac12$ the left side equals $(f+g)(s_1,2s_2,\ldots)=f(2s_1,2s_2,\ldots)$ and the right side equals $(f+'h)(2s_1,s_2,\ldots)=f(2s_1,2s_2,\ldots)$. On $s_1\le\tfrac12,s_2\ge\tfrac12$ the left side is $(h+k)(s_1,2s_2-1,\ldots)=h(2s_1,2s_2-1,\ldots)$ and the right side is again $(f+'h)(2s_1,s_2,\ldots)=h(2s_1,2s_2-1,\ldots)$. On $s_1\ge\tfrac12,s_2\le\tfrac12$ both sides are $g(2s_1-1,2s_2,\ldots)$, and on $s_1\ge\tfrac12,s_2\ge\tfrac12$ both are $k(2s_1-1,2s_2-1,\ldots)$. The two maps agree at every point of $I^n$, boundary included. This is tom Dieck's identity $(a+_1b)+_2(c+_1d)=(a+_2c)+_1(b+_2d)$ on printed p. 88, and the clause-by-clause computation is the one in the accepted answer 161511.
:::

:::

::: {.pf-step #proposition}
If a set $M$ carries two composition laws $+_1,+_2$ with neutral elements $e_1,e_2$ satisfying the commutation rule, then $+_1=+_2=+$, $e_1=e_2$, and $+$ is associative and commutative.

::: pf-proof
tom Dieck's (4.3.1), printed p. 88, by the chain
$$
a=a+_2e_2=(a+_1e_1)+_2(e_1+_1e_2)=(a+_2e_1)+_1(e_1+_2e_2)=(a+_2e_1)+_1e_1=a+_2e_1,
$$
so $e_1$ is a right unit for $+_2$, and symmetrically $e_1$ is a left unit for $+_2$ and $e_2$ both a left and a right unit for $+_1$; then $e_1=e_1+_2e_2=e_2$. Next $a+_2b=(a+_1e)+_2(e+_1b)=(a+_2e)+_1(e+_2b)=a+_1b$ gives $+_1=+_2=+$, then $b+c=(e+b)+(c+e)=(e+c)+(b+e)=c+b$ gives commutativity, and $a+(b+c)=(a+e)+(b+c)=(a+b)+(e+c)=(a+b)+c$ associativity.
:::

:::

::: {.pf-step}
$\boxed{f+'k\simeq f+k\text{ and }g+'h\simeq h+g}$, so the two sums agree on $\pi_n(X,x_0)$ and the addition is abelian.

::: pf-proof
Take $M=\pi_n(X,x_0)$ with $+_1=+$ and $+_2=+'$; the commutation rule of step [](#commutation){.pf-ref} holds for representatives and hence on classes, and step [](#unit){.pf-ref} supplies the neutral elements, so step [](#proposition){.pf-ref} applies and gives $+_1=+_2=+$ with $+$ commutative. Then
$$
[f+'k]=[f]+_2[k]=[f]+_1[k]=[f+k]\quad\text{and}\quad [g+'h]=[g]+_2[h]=[g]+[h]=[h]+[g]=[h+'g]=[h+g],
$$
which is the two assertions; the proposition also yields associativity, which the exercise does not ask for. Writing $+_i,+_j$ for the laws attached to coordinates $i,j$ and repeating the same verification with the pair $(i,j)$ in place of $(1,2)$ gives $+_i=+_j$ for all $i,j$, the book's conclusion on p. 88.
:::

:::

:::
:::
