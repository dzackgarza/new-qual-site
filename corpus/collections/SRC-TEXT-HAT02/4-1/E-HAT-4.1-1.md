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
review: draft
---

::: {.problem}
Suppose a sum $f +' g$ of maps $f, g: (I^n, \partial I^n) \to (X, x_0)$ is defined using a coordinate of $I^n$ other than the first coordinate as in the usual sum $f + g$.
Verify the formula $(f + g) +' (h + k) = (f +' h) + (g +' k)$, and deduce that $f +' k \simeq f + k$ so the two sums agree on $\pi_n(X, x_0)$, and also that $g +' h \simeq h + g$ so the addition is abelian.
:::

::: {.solution}
Throughout $n\ge2$: for $n=1$ there is no coordinate other than the first. For $1\le i\le n$ define, on maps of pairs $(I^n,\partial I^n)\to(X,x_0)$,
$$
(f+_i g)(s)=\begin{cases}f(s_1,\dots,s_{i-1},2s_i,s_{i+1},\dots,s_n),&s_i\le\tfrac12,\\[2pt] g(s_1,\dots,s_{i-1},2s_i-1,s_{i+1},\dots,s_n),&s_i\ge\tfrac12.\end{cases}
$$
These are the group laws of tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), §4.3, printed p. 87, on $[\Sigma^kX,Y]_0$ in the cube model $\pi_n(X,x_0)=[I^n/\partial I^n,X]_0=[\Sigma^nS^0,X]_0$. The law $+_1$ is Hatcher's $+$ (printed pp. 340--341) and the exercise's $+'$ is $+_2$. A homotopy of representatives through maps of pairs induces a homotopy of $+_i$-sums, so each $+_i$ is well defined on the set $\pi_n(X,x_0)$, and the class of the constant map at $x_0$ is a two-sided unit: $f+_i0\simeq f$ by the stretching homotopy
$$
H_t(s)=f\Bigl(s_1,\dots,\frac{2s_i}{1+t},\dots,s_n\Bigr)\ \text{for } s_i\le\frac{1+t}{2},\qquad H_t(s)=x_0\ \text{otherwise},
$$
which is stationary on $\partial I^n$. The argument of this sentence is the card's own.

*The commutation rule.* Split $I^n$ into the four quarters according to $s_1\lessgtr\tfrac12$ and $s_2\lessgtr\tfrac12$. On the quarter $s_1\le\tfrac12,s_2\le\tfrac12$ the left side $(f+g)+'(h+k)$ takes the value $(f+g)(s_1,2s_2,\dots)=f(2s_1,2s_2,\dots)$, and the right side $(f+'h)+(g+'k)$ takes the value $(f+'h)(2s_1,s_2,\dots)=f(2s_1,2s_2,\dots)$. On $s_1\le\tfrac12,s_2\ge\tfrac12$ the left side is $(h+k)(s_1,2s_2-1,\dots)=h(2s_1,2s_2-1,\dots)$ and the right side is $(f+'h)(2s_1,s_2,\dots)=h(2s_1,2s_2-1,\dots)$. On $s_1\ge\tfrac12,s_2\le\tfrac12$ both sides are $g(2s_1-1,2s_2,\dots)$, and on $s_1\ge\tfrac12,s_2\ge\tfrac12$ both are $k(2s_1-1,2s_2-1,\dots)$. The two maps of $I^n$ into $X$ therefore agree everywhere, on the boundary included, so
$$
(f+g)+'(h+k)=(f+'h)+(g+'k)
$$
on the nose, not merely up to homotopy. tom Dieck states exactly this on printed p. 88, as $(a+_1b)+_2(c+_1d)=(a+_2c)+_1(b+_2d)$ for the two laws attached to two coordinates. The four-quarter computation is that of the accepted answer 161511 (KReiser, 2012-06-22) to Math Stack Exchange question 161507: with $f\cdot g$ the sum in the first coordinate and $f\star g$ the sum in the second, both $(f\cdot g)\star(h\cdot i)$ and $(f\star h)\cdot(g\star i)$ are the single map that is $f(2x,2y,\ldots)$ on $[0,\tfrac12]\times[0,\tfrac12]$, $g(2x-1,2y,\ldots)$ on $[\tfrac12,1]\times[0,\tfrac12]$, $h(2x,2y-1,\ldots)$ on $[0,\tfrac12]\times[\tfrac12,1]$ and $i(2x-1,2y-1,\ldots)$ on $[\tfrac12,1]\times[\tfrac12,1]$, which is the verification written out above clause by clause, and the answer concludes from it and the Eckmann--Hilton argument that the two compositions agree and are commutative.

*The source's proposition.* (tom Dieck (4.3.1), printed p. 88.) Suppose the set $M$ carries two composition laws $+_1$ and $+_2$ with neutral elements $e_i$, and suppose the commutation rule $(a+_1b)+_2(c+_1d)=(a+_2c)+_1(b+_2d)$ holds. Then $+_1=+_2=+$, $e_1=e_2=:e$, and $+$ is associative and commutative. The proof is the book's chain of equalities:
$$
a=a+_2e_2=(a+_1e_1)+_2(e_1+_1e_2)=(a+_2e_1)+_1(e_1+_2e_2)=(a+_2e_1)+_1e_1=a+_2e_1,
$$
so $e_1$ is a right unit for $+_2$; in the same way $e_1$ is a left unit for $+_2$ and $e_2$ is a left and right unit for $+_1$. Hence $e_1=e_1+_2e_2=e_2$. Then
$$
a+_2b=(a+_1e)+_2(e+_1b)=(a+_2e)+_1(e+_2b)=a+_1b
$$
shows $+_1=+_2=+$; then
$$
b+c=(e+b)+(c+e)=(e+c)+(b+e)=c+b
$$
is commutativity, and
$$
a+(b+c)=(a+e)+(b+c)=(a+b)+(e+c)=(a+b)+c
$$
is associativity.

*The exercise's two deductions.* The commutation rule holds in $M=\pi_n(X,x_0)$ with $+_1=+$ and $+_2=+'$, because it holds for representatives. So (4.3.1) applies and gives $+_1=+_2=+$, $e_1=e_2$, and commutativity. Therefore
$$
[f+'k]=[f]+_2[k]=[f]+_1[k]=[f+k],
$$
that is $f+'k\simeq f+k$ through maps of pairs, so the two sums agree on $\pi_n(X,x_0)$; and
$$
[g+'h]=[g]+_2[h]=[g]+[h]=[h]+[g]=[h]+_1[g]=[h+g],
$$
that is $g+'h\simeq h+g$, so the addition is abelian. The proposition also gives the associativity of the sum, which the exercise does not ask for. The same verification with the pair of coordinates $(i,j)$ in place of $(1,2)$ gives $+_i=+_j$ for all $i,j$, which is the book's conclusion on p. 88 that all the laws coincide and that they are abelian for $n\ge2$.

The exercise is Hatcher, *Algebraic Topology* (2002), §4.1 Exercise 1, printed p. 358. His $+$ is the first-coordinate sum of printed p. 340, and his commutativity homotopy on printed p. 341 is a different argument for the last deduction than the route taken here.
:::
