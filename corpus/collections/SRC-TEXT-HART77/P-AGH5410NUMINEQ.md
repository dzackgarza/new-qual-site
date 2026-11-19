---
schema: qual/card@1
id: P-AGH5410NUMINEQ
kind: problem
title: A numerical inequality underlying the ampleness criterion on the cubic surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.10 and the retained Egbert note, which supplies no
    proof and points only to Nagata/case analysis. The direct proof below is
    elementary. First prove that positive x_i with x_i+x_j<A and total sum
    at most 2A satisfy sum x_i^2<A^2. If s=sum b_i is at most 2a, this
    applies immediately. If s>2a, put t=s-2a and c_i=b_i-t. The five-term
    inequalities give c_i>0; the pair inequalities give
    c_i+c_j<a-2t; and sum c_i<2(a-2t). Applying the lemma and expanding
    sum(c_i+t)^2 gives exactly a^2 as the comparison value.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete elementary proof. Checked strictness in both cases
    of the auxiliary lemma, the positivity of A=a-2t after translation, the
    identity sum c_i=2a-5t, and the final expansion back to a^2. No geometric
    input or later-card result is used.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Published-solution pass for issue #121. Read the printed exercise in
    Hartshorne, Algebraic Geometry (1977), V.4.10, printed p. 408 (text
    version tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed
    p. N is PDF p. N+15), with (4.11) and (4.13)(a), printed p. 406, whose
    inequalities its hypotheses are. Read at the cited places: Math
    StackExchange 2475661, answer 2476483 by Dap, text version
    tmp/sources/mse-2475661-hart-v410-freshman-calculus.md; National Taiwan
    University Algebraic Geometry II (2020 Spring), Chapter V §4 Exercise 10
    (Shuang-Yen Lee), printed p. 17, text version
    tmp/sources/ntu-ag2-chapter5.md, and the same page of the PDF, where the
    text version damages two formulas. Checked: the exercise's hypotheses
    imply the sorted weak thresholds b_5+b_6 <= a and b_2+...+b_6 <= 2a, so
    the sources' reduction to the weak form needs no separate equivalence;
    and each endpoint value the sources print (a^2, 15a^2/16, 24a^2/25,
    2b_4b_5-2b_5^2, 2b_4b_5-b_5^2) recomputed from the maximiser displayed
    with it. Defects found: the MSE answer's Case 1 prints 4b_4^2 for the
    five equal terms 5b_4^2 of its own maximiser while reporting a^2 at both
    endpoints, which is the value for 5b_4^2; its Case 2 is stated for
    a/3 <= b_4 <= a/2 although its own ordering forces b_4 = a/3; the NTU
    second case leaves its constant term as * and its printed vertex line
    has (1/3)(2b_2-(b_3+b_4+b_5)) on the right where the left side is
    (1/3)(b_2-2(b_3+b_4+b_5)). Not checked: no source outside these two was
    read for this card.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now the two published arguments transcribed, each step
    naming its source with its answer id or printed page; the card's earlier
    elementary proof, which was not a transcription of any source, is
    replaced by it. Steps sorted-hypotheses and strict-from-weak are the
    book's hypotheses and the MSE passage from the sharp to the weak form;
    steps maximiser, case-small-max, case-large-max and case-open transcribe
    that answer's four bullets and its Cases 1, 2a, 2b and 0; step
    second-argument transcribes NTU's Exercise 10 with both of its cases,
    including the three defects the remark names.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the whole card beside both sources. Checked the arithmetic of
    every displayed maximiser and of every endpoint value; checked that
    steps case-small-max, case-large-max and case-open exhaust the
    maximisers step maximiser allows, namely b_5+b_6 = a with b_4 <= a/3,
    the same with b_4 >= a/3, and b_5+b_6 < a; checked that step
    second-argument's two cases are the two branches of a = max{b_1+b_2,
    (b_1+...+b_5)/2} and that its endpoint inequalities need only
    0 < b_5 <= b_4. Not reviewed and not supplied: a proof of the three
    reduction assertions the sources make without proof (the three
    "otherwise one can increase" bullets of the first answer and NTU's
    reduction of its second case to b_1+b_2 = b_3+b_4+b_5), and no such
    proof was added; the 2026-11-16 COMPLAINTS record names what is left
    open.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass, on the reader's findings for this card. The first pass had
    sorted the variables decreasingly while transcribing an answer that sorts
    them increasingly (text version
    tmp/sources/mse-2475661-hart-v410-freshman-calculus.md, line 31:
    "0 <= b_1 <= ... <= b_6"); in the decreasing order the answer's b_5+b_6
    is the pair of the two smallest variables and its b_2+...+b_6 the sum
    that omits the largest, so the two thresholds read off in that order
    were not the answer's; the step is rewritten in the answer's increasing
    order, where
    b_5+b_6 is the pair of the two largest and b_2+...+b_6 the sum omitting
    the smallest, so both thresholds are the book's own hypotheses. Three
    findings of the first pass are withdrawn as misreadings and removed from
    the card and from the COMPLAINTS record of this date: that the first
    answer's Case 2 is empty for b_4 > a/3 (with increasing order its own
    ordering gives a-2b_4 <= b_2 <= (a-b_4)/2, nonempty exactly for
    b_4 >= a/3, and its 2b subcase is the maximiser (0,0,a/2,a/2,a/2,a/2)
    that it lists); that its Case 0 refers forward as a defect (the answer
    says its later cases do not depend on Case 0); and that the NTU second
    case misidentifies its vertex (PDF p. 17: the line compares the vertex
    with the midpoint of the range, the comparison is correct because
    2b_2 <= b_3+b_4+b_5 follows from b_1+b_2 <= b_3+b_4+b_5 and b_1 >= b_2,
    and the only slip is a factor 2 on the right-hand side; the constant is
    not needed). Checked in this pass: the two NTU endpoint computations,
    the midpoint comparison, the vertex at (b_2+b_3+b_4+b_5)/3, and the
    replacement of three entries that preserves b_1+b_2, b_1+...+b_5 and
    the ordering while not decreasing the sum of squares. Found in this
    pass and now named on the card: NTU's increase of b_3,b_4,b_5 to reach
    b_1+b_2 = b_3+b_4+b_5 fails once b_1 > 2b_2, for instance at
    (10,1,1,1,1,1); and the first answer's equalities b_2=b_3=b_4 and
    b_2+b_3+b_4=a rest on its one-clause reason. The step that said the
    chosen a keeps the strict hypotheses is corrected: a is replaced by
    max{b_1+b_2,(b_1+...+b_5)/2}, at which one hypothesis holds with
    equality. Not checked: no source outside these two was read, and no
    proof of the two open reductions was supplied.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Rewritten in the increasing order of the first answer, with the four
    cases of its maximiser analysis, the two open reductions named as its
    reasons, and the NTU argument in its own decreasing order with the
    b_1 <= 2b_2 condition on its first case. Provenance and process
    commentary is removed from the rendered card; the sources and their
    pages are named at the steps and in the remark.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Re-read against both sources. Recomputed every displayed value: a^2 and
    a^2 at the endpoints of 5b_4^2+(a-b_4)^2; a^2 and 15a^2/16 for
    7(a-b_4)^2/4+2b_4^2; a^2 at both ends for
    2(a-2b_4)^2+3b_4^2+(a-b_4)^2; 24a^2/25 at the all-equal vector;
    2b_4b_5-2b_5^2 and 2b_4b_5-b_5^2 at the two endpoints of the quadratic
    in b_2. Checked that the three cases exhaust the maximisers allowed by
    b_5+b_6 = a or b_5+b_6 < a together with b_4 <= a/3 or b_4 >= a/3.
    Left open and recorded in COMPLAINTS: the two reductions the answer
    states without proof, and the range of NTU's first case.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass, on the second reader's findings for this card. Read again:
    answer 2476483 in
    tmp/sources/mse-2475661-hart-v410-freshman-calculus.md, whose line 31
    carries the weak order 0 <= b_1 <= ... <= b_6 with a >= b_5+b_6 and
    2a >= b_2+...+b_6, and whose line 76 lists (0,0,0,0,0,a) among its
    maximisers; and Chapter V §4 Exercise 10 of
    tmp/sources/ntu-ag2-chapter5.md, printed p. 17, read in the text version
    and checked on printed p. 17 of tmp/sources/ntu-ag2-chapter5.pdf, whose
    folio is the PDF page. The set M of step maximiser now carries the
    answer's 0 <= b_1: the earlier 0 < b_1 excluded the source's own
    maximiser (0,0,0,0,0,a) and, with it, the closedness the step invokes.
    The vector of step case-large stands and its justification is corrected:
    b_1 = b_2, b_5 = b_4 and b_6 = a-b_4 come from step maximiser and
    b_3 = a-b_4-b_2 from b_2+b_3+b_4 = a, so b_2 = b_3 is not assumed there.
    The NTU comparison line, printed p. 17, is described as printed: its
    fraction is the vertex b_1^* = (1/3)(b_2+b_3+b_4+b_5), so the printed left
    side is b_1^*-(b_3+b_4+b_5) = (1/3)(b_2-2(b_3+b_4+b_5)), negative at every
    datum, while the printed right side (1/3)(2b_2-(b_3+b_4+b_5)) =
    2b_1^*-(b_3+b_4+b_5) is the midpoint comparison the proof uses; the slip
    is the printed denominator -(3/4).2 where -(3/4) is meant. The earlier
    account, that the left side was b_1^*-T/2 and the right side twice it, of
    the same sign, is false of the printed line and is withdrawn. The answer's
    equalities b_2 = b_3 = b_4 and b_2+b_3+b_4 = a are its own one-clause
    reasons, of the same kind as its b_6 and b_1 increases, so the card names
    them as the answer's and counts neither as open; the COMPLAINTS record of
    this date, which called them open, and the earlier version of that record,
    which called the monotone increases open, are corrected in a new record of
    this date. The claim of step second-argument now carries the range
    b_1 <= 2b_2, the condition under which its first case's increase of
    b_3,b_4,b_5 is available, and the clause that said the increase was
    available only while b_3 <= b_2, which holds of every datum, is replaced by
    it. Not checked in this pass: the printed text of that page beyond its
    folio, and no source outside these two was read for this card.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The four corrections above: the set M stated with 0 <= b_1 as the answer
    states it, each reduction attributed to the answer it comes from, step
    second-argument's claim restricted to b_1 <= 2b_2, and the NTU printed
    line described as printed. No proof of any part was added; the reductions
    are the answer's one clause each and none was expanded.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the whole card beside both sources. Rechecked that every
    maximiser of M with 0 <= b_1 falls under steps case-small, case-large and
    case-open, that the endpoint values a^2, 15a^2/16 and 24a^2/25 and the
    values 2b_4b_5-2b_5^2 and 2b_4b_5-b_5^2 are those of the vectors
    displayed with them, and that the printed left and right sides of NTU's
    comparison line are the two computed above. Not verified: nothing beyond
    those two sources, and no third reading of the NTU page as an image.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The three reductions the sources state in one clause each are now proved
    on the card, so its proof of V.4.10 is complete and stands on its own
    where the sources stop. Read for this pass: Hartshorne V.4.10, printed
    p. 408, with (4.13)(a) on printed p. 406; answer 2476483 in
    tmp/sources/mse-2475661-hart-v410-freshman-calculus.md; and NTU Chapter V
    §4 Exercise 10, printed p. 17. The reductions, now marked on their steps
    as the card's own: (i) at a maximiser with b_5+b_6=a and b_4<=a/3, one
    has b_2=b_3=b_4, since with t=b_1=b_2, u=b_3, v=b_4=b_5 the constraint
    t+u+v<=a is automatic for t,u<=v<=a/3 and 2t^2+u^2 is increasing in each
    variable on that range, so t=u=v; (ii) at one with b_5+b_6=a and
    b_4>=a/3, one has b_2+b_3+b_4=a, since if t+u+v<a then either u<v and
    increasing u raises 2t^2+u^2, or u=v and t<v, so increasing t does;
    (iii) in the case b_5+b_6<a, write t=b_1=b_2, x=b_3-t, y=b_4-b_3; then
    u=t+x, v=t+x+y, w=2a-5t-3x-2y, the constraints w>=v and v+w<=a become
    6t+4x+3y<=2a and 4t+2x+y>=a, and the sum of squares is a convex
    quadratic on that polygon, whose vertices (0,a/2,0), (a/3,0,0),
    (a/4,0,0) and (a/6,0,a/3) give a^2, 2a^2/3, 7a^2/8 and 5a^2/6. Checked:
    the endpoint quadratics of steps case-small and case-large have maximum
    1 on their intervals, and the four vertex values above. The
    transcriptions of the rest of the two arguments are unchanged. Not
    checked: no source outside these two and the book was read, and the
    card's other steps were not re-derived in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Issue #165: the two events of 2026-11-16 that record what was then not
    supplied are corrected here, in a new event; neither earlier text is
    rewritten. The event whose note reads "Not reviewed and not supplied: a
    proof of the three reduction assertions ... and no such proof was added"
    records the card before c820143f0f; that commit proves all three on the
    card, at steps case-small (b_2 = b_3 = b_4 when b_5+b_6 = a and
    b_4 <= a/3), case-large (b_2+b_3+b_4 = a when b_5+b_6 = a and
    b_4 >= a/3) and case-open (the vertex check on the polygon in t, x, y),
    each marked there as the card's own and each naming the answer's
    one-clause reason that it replaces. The event whose note reads "Left open
    and recorded in COMPLAINTS: the two reductions the answer states without
    proof, and the range of NTU's first case" is corrected the same way: the
    two reductions are proved above, and the range b_1 <= 2b_2 is not open but
    is the exact range of NTU's first case, carried in the claim of step
    second-argument, with (10,1,1,1,1,1) outside it where the increase of
    b_3, b_4, b_5 to b_1+b_2 = b_3+b_4+b_5 is unavailable. The constant that
    the rendered step left as an asterisk is now written out: with
    a = (b_1+...+b_5)/2 it is
    (b_2+b_3+b_4+b_5)^2/4 - (b_2^2+b_3^2+b_4^2+b_5^2) - b_6^2, the value of
    a^2 - sum b_i^2 at b_1 = 0; the argument does not use it, the minimum on
    the range being read at the right endpoint, and the card now says so.
    Checked in this pass: the three reductions recomputed; the four
    properties of a maximiser; the endpoint values a^2 and a^2 of
    5v^2+(a-v)^2, a^2 and 15a^2/16 of 7(a-b_4)^2/4+2b_4^2, and a^2 and a^2
    of 2(a-2b_4)^2+3b_4^2+(a-b_4)^2; the endpoint values 2b_4b_5-2b_5^2 and
    2b_4b_5-b_5^2 of the quadratic in b_2; the four vertex values a^2,
    2a^2/3, 7a^2/8 and 5a^2/6; the identity for the constant at b_1 = 0 and
    its coefficients -3/4 and (1/2)(b_2+b_3+b_4+b_5); and the printed line of
    NTU, printed p. 17, whose fraction is the vertex
    b_1^* = (1/3)(b_2+b_3+b_4+b_5) and whose denominator -3/4.2 should read
    -3/4. Not checked: no source outside answer 2476483, NTU Exercise 10 and
    Hartshorne V.4.10 with (4.13)(a) was read, and the card's other steps were
    not re-derived.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Issue #165, reader's report on the card: two proof steps are corrected, and
    the earlier events that certified them are named. (1) Step case-open
    carried the maximiser constraint of the wrong set of indices. With
    t=b_1=b_2, u=b_3, v=b_4=b_5 and w=b_6, the constraint b_2+...+b_6=2a is
    t+u+2v+w=2a, not the 2t+u+2v+w=2a printed, which is b_1+...+b_6=2a. The
    equation, the formula w=2a-4t-3x-2y, the two inequalities
    5t+4x+3y<=2a and 3t+2x+y>=a, the four vertices (0,a/2,0), (a/3,0,0),
    (2a/5,0,0), (a/4,0,a/4) and their values a^2, a^2, 24a^2/25, 15a^2/16 are
    now correct, and the answer's remaining case b_1=b_6=2a/5 is the vertex
    (2a/5,0,0), so the sentence claiming that the vertex check covers that
    form is now true. This corrects the vertex values a^2, 2a^2/3, 7a^2/8 and
    5a^2/6 asserted by the event of this date whose note reads "The three
    reductions the sources state in one clause each are now proved ...", and
    repeated by the event of this date whose note reads "the constant that the
    rendered step left as an asterisk is now written out"; the COMPLAINTS
    record of this date carries the same computation and is corrected in a
    record of this date there. (2) Step maximiser's proof of b_5=b_4 said that
    b_5=a/2 "gives a smaller value than either endpoint does", which is not
    the comparison that decides the claim and fails at b_4=a/2. The proof now
    compares the two endpoints b_5=S/2 and b_5=b_4 of the convex function
    b_5^2+(S-b_5)^2, whose values are S^2/2 and S^2/2+2(b_4-S/2)^2, so the
    endpoint b_5=S/2 is dominated unless b_4=S/2 and a maximiser has b_5=b_4.
    (3) The event of 2026-11-16 whose note says "the only slip is a factor 2
    on the right-hand side" of NTU's comparison line is false of the printed
    line and is corrected here: the printed fraction is the vertex and the
    slip is the doubled denominator -(3/4).2, which halves the vertex term, as
    the rendered step says. (4) The event of this date above whose note reads
    "the argument does not use it, the minimum on the range being read at the
    right endpoint, and the card now says so" said so of the rendered step
    before the step said it; the step now says that only the two coefficients
    and the sign of the leading one are used. Checked in this pass: the
    corrected constraint, polygon, four vertices and their values, with the
    b-vectors they give, all in M with b_2+...+b_6=2a and sums a^2, a^2,
    24a^2/25, 15a^2/16; the two endpoint values of b_5^2+(S-b_5)^2; the
    constant (b_2+b_3+b_4+b_5)^2/4-(b_2^2+b_3^2+b_4^2+b_5^2)-b_6^2 with its
    two coefficients -3/4 and (1/2)(b_2+b_3+b_4+b_5); and the printed NTU line
    at printed p. 17. Not checked: no source outside answer 2476483, NTU
    Exercise 10 and Hartshorne V.4.10 with (4.13)(a) was read.
---

::: {.problem}
A curious consequence of the implication (iv) $\Rightarrow$ (iii) of (4.11) is the following numerical fact: Given integers $a, b_1, \ldots, b_6$ such that $b_i>0$ for each $i$, $a-b_i-b_j>0$ for each $i, j$ and $2 a-\sum_{i \neq j} b_i>0$ for each $j$, we must necessarily have $a^2-\sum b_i^2>0$.
Prove this directly (for $a, b_1, \ldots, b_6 \in \RR$) using methods of freshman calculus.
:::

::: {.solution}

The exercise's hypotheses are the conditions of (4.13)(a) of the book for the class
$D=a\ell-\sum_ib_ie_i$ on the cubic surface, with the pair condition read for $i\ne j$, and its
conclusion $a^2-\sum_ib_i^2>0$ is $D^2>0$; the exercise asks for integers and then for real
$a,b_1,\ldots,b_6$.

Math StackExchange question 2475661, answer 2476483 (Dap, 2017-10-17), orders the variables
increasingly and supplies the maximiser analysis of steps [](#ordered-hypotheses){.pf-ref} to
[](#case-open){.pf-ref}; the three reductions in that analysis are its own one-clause reasons, and
each is proved on the card.
Chapter V §4 Exercise 10 of the National Taiwan University *Algebraic Geometry II* homework (2020
Spring), by Shuang-Yen Lee, printed p. 17, orders them decreasingly and supplies the argument of step
[](#second-argument){.pf-ref}, which is transcribed in that order.

::: pf

::: {.pf-step #ordered-hypotheses}
After reordering the indices one may assume
$$
0<b_1\le b_2\le\cdots\le b_6,
$$
and then
$$
a\ge b_5+b_6,
\qquad
2a\ge b_2+\cdots+b_6 .
$$

::: pf-proof
The hypotheses are symmetric in the indices, so reordering preserves them. Among the conditions
$a>b_i+b_j$ with $i\ne j$ the strongest is the one at the two largest variables, namely
$a>b_5+b_6$; among the conditions $2a>\sum_{j\ne i}b_j$ the strongest is the sum that omits the
smallest variable, namely $b_2+\cdots+b_6<2a$. These two are the hypotheses of the argument that
follows.
:::

:::

::: {.pf-step #smaller-a}
It suffices to prove
$$
a^2\ge\sum_{i=1}^6b_i^2
$$
under the two weak inequalities of step [](#ordered-hypotheses){.pf-ref}.

::: pf-proof
If $a>b_5+b_6$ and $2a>b_2+\cdots+b_6$, then $a-\varepsilon$ satisfies the same strict inequalities
for small $\varepsilon>0$; a proof of $(a-\varepsilon)^2\ge\sum_ib_i^2$ for that smaller number gives
$a^2>\sum_ib_i^2$.
:::

:::

::: {.pf-step #maximiser}
Fix $a>0$ and let $M$ be the set of $b$ with
$$
0\le b_1\le\cdots\le b_6,
\qquad
b_5+b_6\le a,
\qquad
b_2+\cdots+b_6\le 2a .
$$
The function $\sum_ib_i^2$ attains a maximum on $M$, and at every maximiser
$$
b_2+\cdots+b_6=2a
\quad\text{or}\quad
b_5+b_6=a,
$$
$$
b_1=b_2,
\qquad
b_5\le\frac a2,
\qquad
b_5=b_4 .
$$

::: pf-proof
$M$ is closed and bounded, so a maximum is attained. If both $b_2+\cdots+b_6<2a$ and
$b_5+b_6<a$, then $b_6$ can be increased, which keeps $b$ in $M$ and raises $\sum_ib_i^2$. If
$b_1<b_2$ then $b_1$ can be increased, which keeps $b$ in $M$ and raises the sum, since $b_1$ occurs
in neither constraint. If $b_5>a/2$ then $b_6\ge b_5$ gives $b_5+b_6>a$. Last, for fixed
$b_5+b_6=S$ the function $b_5^2+(S-b_5)^2$ on $b_4\le b_5\le S/2$ is convex, so it attains its
maximum at an endpoint. At $b_5=S/2$ its value is $S^2/2$; at $b_5=b_4$ it is
$b_4^2+(S-b_4)^2=S^2/2+2(b_4-S/2)^2$, which is strictly larger unless $b_4=S/2$. Hence a maximiser
has $b_5=b_4$.
:::

:::

::: {.pf-step #case-small}
If a maximiser satisfies $b_5+b_6=a$ and $b_4\le a/3$, then
$$
\sum_{i=1}^6b_i^2\le a^2 .
$$

::: pf-proof
At such a maximiser $b_2=b_3=b_4$. Write $t=b_1=b_2$, $u=b_3$ and $v=b_4=b_5$, so that
$b_6=a-v$ and $0\le t\le u\le v\le a/3$. The second constraint is $t+u+v\le a$, and it is
automatic on this range because $t+u\le2v\le a-v$; for fixed $v$ the function $2t^2+u^2$ is
increasing in $t$ and in $u$ on $0\le t\le u\le v$, so its maximum there is at $t=u=v$. Hence
$b_1=\cdots=b_5=v$ and $b_6=a-v$, so
$$
\sum_ib_i^2=5v^2+(a-v)^2=6v^2-2av+a^2 .
$$
This is a quadratic in $v$ with positive leading coefficient, so on $0\le v\le a/3$ it is at most
the larger endpoint value; at $v=0$ the value is $a^2$ and at $v=a/3$ it is
$5a^2/9+4a^2/9=a^2$. The reduction to $b_1=\cdots=b_5=v$ is the card's own; answer 2476483 states it
with the reason that otherwise $b_3$ or $b_2$ could be increased. The answer writes $4b_4^2$ in
place of the five equal terms $5b_4^2$ and reports $a^2$ at both endpoints, which are the endpoint
values of $5b_4^2+(a-b_4)^2$.
:::

:::

::: {.pf-step #case-large}
If a maximiser satisfies $b_5+b_6=a$ and $b_4\ge a/3$, then
$$
\sum_{i=1}^6b_i^2\le a^2 .
$$

::: pf-proof
At such a maximiser $b_2+b_3+b_4=a$. If $t=b_2$, $u=b_3$ and $v=b_4=b_5$, then $b_6=a-v$, and the
constraints are $0\le t\le u\le v$, $v\in[a/3,a/2]$ and $t+u+v\le a$. If $t+u+v<a$, then either
$u<v$, and increasing $u$ preserves the ordering and raises $2t^2+u^2$, or $u=v$, and then $t<v$
because $t+2v<a$, so increasing $t$ raises the sum; in neither case is the point a maximiser. Hence
$t+u+v=a$. This reduction is the card's own; the answer states it with the reason that otherwise
$b_3$ or $b_2$ could be increased. With $b_1=b_2$, $b_5=b_4$ and $b_6=a-b_4$ from step
[](#maximiser){.pf-ref} this gives
$$
b=(b_2,b_2,a-b_4-b_2,b_4,b_4,a-b_4).
$$
The ordering forces $a-2b_4\le b_2\le\frac12(a-b_4)$, an interval nonempty exactly for $b_4\ge a/3$,
and the part of $\sum_ib_i^2$ depending on $b_2$ is
$$
2b_2^2+(a-b_4-b_2)^2 ,
$$
a quadratic with positive leading coefficient, so its maximum on that interval is at an endpoint. At
$b_2=\frac12(a-b_4)$ it gives
$$
b=\left(\tfrac12(a-b_4),\tfrac12(a-b_4),\tfrac12(a-b_4),b_4,b_4,a-b_4\right),
\qquad
\sum_ib_i^2=\tfrac74(a-b_4)^2+2b_4^2,
$$
which is $a^2$ at $b_4=a/3$ and $\frac{15}{16}a^2$ at $b_4=a/2$; at $b_2=a-2b_4$ it gives
$$
b=(a-2b_4,a-2b_4,b_4,b_4,b_4,a-b_4),
\qquad
\sum_ib_i^2=2(a-2b_4)^2+3b_4^2+(a-b_4)^2,
$$
which is $a^2$ at both $b_4=a/3$ and $b_4=a/2$, the second being the vector
$(0,0,\frac a2,\frac a2,\frac a2,\frac a2)$. In each subcase the value is a convex function of $b_4$
on $[\frac a3,\frac a2]$, so it is at most the larger endpoint value, namely $a^2$.
:::

:::

::: {.pf-step #case-open}
If a maximiser satisfies $b_5+b_6<a$, then
$$
\sum_{i=1}^6b_i^2\le a^2 .
$$

::: pf-proof
By step [](#maximiser){.pf-ref} such a maximiser has $b_2+\cdots+b_6=2a$. Write $t=b_1=b_2$,
$u=b_3$, $v=b_4=b_5$ and $w=b_6$, so that $0\le t\le u\le v\le w$, $v+w<a$ and
$t+u+2v+w=2a$. Put $x=u-t\ge0$ and $y=v-u\ge0$; then $u=t+x$, $v=t+x+y$,
$w=2a-4t-3x-2y$, and the inequalities $w\ge v$ and $v+w\le a$ become
$$
5t+4x+3y\le2a,
\qquad
3t+2x+y\ge a .
$$
On this polygon the sum
$$
\sum_ib_i^2=2t^2+(t+x)^2+2(t+x+y)^2+(2a-4t-3x-2y)^2
$$
is a convex quadratic, so its maximum is attained at a vertex, and the vertices are
$(t,x,y)=(0,a/2,0)$, $(a/3,0,0)$, $(2a/5,0,0)$ and $(a/4,0,a/4)$, where the sum is $a^2$,
$a^2$, $24a^2/25$ and $15a^2/16$. Hence $\sum_ib_i^2\le a^2$. This reduction is the card's own
completion of the answer's boundary sketch: the answer states it in the form
$b=(b_1,b_1,b_1,b_5,b_5,b_6)$ with a remaining case $b_1=b_6=\frac{2a}{5}$, which is the vertex
$(2a/5,0,0)$ and one of the four vertices checked.
:::

:::

::: {.pf-step #second-argument}
The inequality holds as well by the second argument, which needs no maximiser, for those data of the
decreasing order that satisfy $b_1\le2b_2$.

::: pf-proof
The second argument keeps the decreasing order $b_1\ge b_2\ge\cdots\ge b_6$ and opens with the
observation that
$$
x+y=z+w
\quad\text{and}\quad
\abs{x-y}>\abs{z-w}
\quad\Longrightarrow\quad
x^2+y^2>z^2+w^2,
$$
which is the identity $x^2+y^2=\frac12\left((x+y)^2+(x-y)^2\right)$ applied to both pairs. In that
order the hypotheses give $a>b_1+b_2$ and $2a>b_1+\cdots+b_5$, so
$$
a\ge\max\left\{b_1+b_2,\ \tfrac12(b_1+\cdots+b_5)\right\},
$$
and since the conclusion $a^2\ge\sum_ib_i^2$ becomes harder as $a$ decreases, it suffices to prove it
for the value $a=\max\{b_1+b_2,\frac12(b_1+\cdots+b_5)\}$.

If $b_1+b_2\ge b_3+b_4+b_5$ then $a=b_1+b_2$, and the argument increases $b_3,b_4,b_5$ so as to have
$b_1+b_2=b_3+b_4+b_5$; the three entries are at most $b_2$, so that increase is available only while
$b_1\le2b_2$, and it fails once $b_1>2b_2$, for instance at $b=(10,1,1,1,1,1)$, where
$b_3+b_4+b_5$ cannot reach $b_1+b_2=11$ under the ordering. Under $b_1+b_2=b_3+b_4+b_5$, replacing the three entries $b_1,b_2,b_6$ by
$b_1+b_2-b_3$, $b_3$ and $b_5$ keeps $b_1+b_2$ and $b_1+\cdots+b_5$, keeps the ordering, and by the
observation does not decrease $\sum_ib_i^2$, so one may assume $b_2=b_3$ and $b_5=b_6$. Then
$b_1=b_4+b_5\ge b_2$ and
$$
a^2-\sum_ib_i^2=2b_2b_4+2b_2b_5-b_2^2-b_4^2-2b_5^2,
$$
a quadratic in $b_2$, so on the range $b_4\le b_2\le b_4+b_5$ it suffices to check the endpoints,
where it is
$$
2b_4b_5-2b_5^2\ge0
\qquad\text{and}\qquad
2b_4b_5-b_5^2\ge0,
$$
both nonnegative since $0<b_5\le b_4$.

If $b_1+b_2\le b_3+b_4+b_5$ then $a=\frac12(b_1+\cdots+b_5)$ and
$$
a^2-\sum_ib_i^2=-\tfrac34b_1^2+\tfrac12(b_2+b_3+b_4+b_5)b_1+\ast
$$
for the constant $\tfrac14(b_2+b_3+b_4+b_5)^2-(b_2^2+b_3^2+b_4^2+b_5^2)-b_6^2$ in $b_1$; only the two
coefficients and the sign of the leading one are used below. This is a quadratic in $b_1$ opening downwards, with vertex
$b_1^{*}=\frac13(b_2+b_3+b_4+b_5)$; its argument range is $b_2\le b_1\le b_3+b_4+b_5-b_2$, whose
midpoint is $\frac12(b_3+b_4+b_5)$. Since $b_1+b_2\le b_3+b_4+b_5$ and $b_1\ge b_2$ give
$2b_2\le b_3+b_4+b_5$, one has
$$
b_1^{*}-\tfrac12(b_3+b_4+b_5)=\tfrac16\left(2b_2-(b_3+b_4+b_5)\right)\le0,
$$
so the vertex lies at or to the left of the midpoint, the right endpoint is the farther one, and the
minimum on the range is at $b_1=b_3+b_4+b_5-b_2$, that is, at $b_1+b_2=b_3+b_4+b_5$, which is the
preceding case. The printed line makes this comparison and leaves the constant term unwritten, but
its vertex term carries one factor of $2$ too few: its fraction
$\frac{-\frac12(b_2+b_3+b_4+b_5)}{-\frac34\cdot2}$ is the vertex
$b_1^{*}=\frac13(b_2+b_3+b_4+b_5)$, so the left side as printed is
$b_1^{*}-(b_3+b_4+b_5)=\frac13\left(b_2-2(b_3+b_4+b_5)\right)$, which is negative because
$b_2\le b_3+b_4+b_5$, and is not the quantity the printed line compares with $0$. With $-\frac34$ in
the denominator that fraction would be $2b_1^{*}$, and the left side would read
$2b_1^{*}-b_2-(b_3+b_4+b_5-b_2)=\frac13\left(2b_2-(b_3+b_4+b_5)\right)$, which is the right side as
printed and is $\le0$ by $2b_2\le b_3+b_4+b_5$: the comparison and the sign are the printed ones, and
the missing factor is in the vertex term.
:::

:::

::: {.pf-step #conclusion}
Consequently
$$
a^2-\sum_{i=1}^6b_i^2>0 .
$$

::: pf-proof
The maximiser of $\sum_ib_i^2$ on $M$ falls under step [](#case-open){.pf-ref} if $b_5+b_6<a$, and
otherwise under step [](#case-small){.pf-ref} or [](#case-large){.pf-ref} according as $b_4\le a/3$ or
$b_4\ge a/3$, so $a^2\ge\sum_ib_i^2$ in every case; step [](#second-argument){.pf-ref} gives the same
inequality by the second route, for the data its first case reaches. Step
[](#smaller-a){.pf-ref} turns the weak inequality into the strict one required by the exercise.
:::

:::

::: pf-qed
Steps [](#ordered-hypotheses){.pf-ref}, [](#smaller-a){.pf-ref} and [](#maximiser){.pf-ref} set up the
maximisation, steps [](#case-small){.pf-ref}, [](#case-large){.pf-ref} and [](#case-open){.pf-ref}
bound the sum of squares at a maximiser, and step [](#second-argument){.pf-ref} is the second
argument, which reaches the first case's equality configuration only while $b_1\le 2b_2$.
:::

:::
:::

::: {.remark title="Published solution"}
Math StackExchange 2475661, *Freshman calculus question in Hartshorne, chapter V*, answer 2476483 by
Dap (2017-10-17): the weak threshold form of the hypotheses, the four properties of a maximiser of
$\sum b_i^2$ on the feasible set, and the four cases bounding that maximum by $a^2$. The answer
writes $4b_4^2$ in place of $5b_4^2$ in its first case, and its equalities $b_2=b_3=b_4$ and
$b_2+b_3+b_4=a$ are stated with the reason that otherwise $b_3$ or $b_2$ could be increased.

National Taiwan University, *Algebraic Geometry II* (2020 Spring, Chin-Lung Wang), Chapter V §4,
Exercise 10, by Shuang-Yen Lee, printed p. 17: the observation on $x+y=z+w$ and $\abs{x-y}>\abs{z-w}$, the
reduction to $a=\max\{b_1+b_2,\frac12(b_1+\cdots+b_5)\}$ in the decreasing order, and the two cases;
the first is carried out at the two endpoint values of the quadratic in $b_2$, and its initial
increase of $b_3,b_4,b_5$ to $b_1+b_2=b_3+b_4+b_5$ needs $b_1\le2b_2$; the second compares the vertex
of a downward quadratic with the midpoint of its range, the printed line carrying one factor of $2$
too few in that vertex term.
:::
