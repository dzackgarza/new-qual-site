---
schema: qual/card@1
id: E-HAT-2.C-1
kind: problem
title: Minimum number of edges for simplicial map $S^1 \to S^1$ of degree $n$
classification:
  areas:
  - topology
  topics:
  - Simplicial Approximation
  - Degree
  - Graphs
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.C, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the simplicial, Lefschetz-trace, or surface argument against the preceding section results.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.C Exercise 1, printed page
    184; the statement matches the book word for word. Proof checked: a simplicial
    map carries each edge of K onto an edge or a vertex, so f_*(z_K) = n z_L forces
    at least |n| edges of K over each edge of L, whence e(K) >= |n| e(L) >= 3|n| with
    e(L) >= 3; the polygon with 3|n| edges mapped periodically around a triangle
    attains the bound, and n = 0 is attained by two triangles with a constant map.
    No defect. Not claimed by the card: the total e(K) + e(L) minimised over e(L),
    which is 3|n| + 3 for the same reason.
- event: solution-written
  by: claude
  date: 2026-11-08
  note: >-
    Replaces the solution with the complete published fundamental-cycle argument in the answer to
    Simplicial map of the circle S1 (2019), at
    https://math.stackexchange.com/questions/3590105/simplicial-map-of-the-circle-s1. The lower
    bound is proved first from f_*(z_K)=n z_L: each target edge needs at least |n| nondegenerate
    preimages. A 3|n|-gon over a triangle attains it, and n=0 is attained by a constant map
    between triangles. This is a full source argument, not a citation attached to a different proof.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Read the published answer and checked it against Hatcher p.184. Each simplicial edge is sent
    to a vertex or homeomorphically to an edge, so signed coefficient n on a target edge requires
    at least |n| domain edges. Period three wraps the triangle |n| times with the required sign.
- event: source-checked
  by: claude
  date: 2026-11-13
  note: >-
    Re-read the printed statement for #123: the exercise is Exercise 1 of §2.C on printed p. 184,
    identical in the current online text, and the card states it word for word. The obligation that
    #123 records is unchanged and stays open: the retained solution sets do not solve this exercise,
    and none was located elsewhere. The card's citation is the final answer to MSE question 3590105,
    which is not a published solution set; the argument transcribed from it is checked on the card.
    Searched without result in the retained sets (Sam, Li, DeMason, Poulsen, Stanford Math 215C
    Solution Sets 1--5, the UCR Math 205B help file, May, Bredon, Maxim's Math 752 notes) and in
    Hatcher's text and errata.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    #123 batch. The card's source is now named by answer id. The published argument is the
    accepted answer 3590397 (2019) to Math StackExchange question 3590105, whose bound runs
    through the universal cover of $S^1$: a degree-$n$ simplicial map lifts to a simplicial map
    of the induced triangulations of $\RR$, an interval spanning $k$ domain vertices goes onto
    one spanning $n\ell$ target vertices, so $k\ge n\ell$ with $\ell\ge 3$; and answer
    4874176 to the same question states the same bound in fundamental-cycle form, which is the
    form the card's step proves, with $n=0$ and the attainment left to the card. Checked against
    the book: Exercise 1 of §2.C on printed p. 184, the answer $e(L)=3$,
    $e(K)=3\max\{1,\abs{n}\}$, the lower bound $e(K)\ge\abs{n}\,e(L)$ (a simplicial edge maps to a
    vertex or homeomorphically to an edge, so its chain coefficient is $0$ or $\pm1$ and each
    target edge needs $\abs{n}$ preimages), the attainment by a $3\abs{n}$-gon over a triangle, and
    $n=0$ by a constant map between triangles. Repairs: the card carried a second `---` line
    after its front matter, removed; and its body mathematics wrote raw bars for the absolute
    value of $n$, now written with the semantic macro `\abs` (STYLE-04), which the file also
    failed before this batch. Not claimed: a solution in a printed solution set; among
    the retained sets only Poulsen (2.C.2, 2.C.8, 2.C.9), Li (2.C.2, 2.C.4, 2.C.5) and DeMason
    (2.C.2, 2.C.3, 2.C.4, 2.C.9) reach §2.C at all.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader batch. The reader accepted the mathematics and named two defects in the record.
    (1) The date is wrong wherever it was given: question 3590105 and its accepted answer
    3590397 were posted **2020-03-22**, not in 2019. Read through the Stack Exchange API on
    2026-11-16: question `creation_date` 1584866748 and answer `creation_date` 1584866744, both
    2020-03-22. The card's opening sentence now gives the date; the "(2019)" in the
    `solution-written` note of 2026-11-08 ("Simplicial map of the circle S1 (2019)") and in the
    `source-checked` note of even date above is wrong and is struck here rather than rewritten
    there. The answer 4874176 is dated 2024-03-02 by the same reading. (2) The text above calls
    3590397 "the published argument", which this batch's own convention elsewhere denies: in
    §3 an answer of Wofsey's on Math StackExchange is refused as "a user answer rather than a
    publication", and the 2.B-5 audit does the same. 3590397 is a user answer on Math
    StackExchange and is cited as the source of the argument, not as a published solution; the
    body now says so. Checked, unchanged: the descriptions of 3590397 (a lift to the universal
    cover, $k\ge n\ell$ with $\ell\ge3$) and of 4874176 (fundamental cycle, at least $3n$
    edges), the exercise as printed on p. 184, and every step of the proof on the card. Not
    claimed: a published solution of Exercise 2.C.1.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, second pass on this card: two defects of the record, repaired here as a new
    event rather than in the notes they concern. (1) The `source-corrected` note of this date gives the
    answer's `creation_date` as 1584866744. That is the question's number, not the answer's: read again
    through the Stack Exchange API on 2026-11-16, question 3590105 has `creation_date` 1584866748 and
    the accepted answer 3590397 has **1584888044**. Both are 2020-03-22, so the date on the card stands
    and only the timestamp in that note is wrong. (2) The `source-checked` note of 2026-11-13 says the
    exercise was searched for in "Stanford Math 215C Solution Sets 1--5". `tmp/sources` holds only
    `stanford-math215c-spring2009-solution2.pdf`, `-3` and `-4`: Solution Sets 1 and 5 do not exist
    there, so that range is not what was read, and the range is Solution Sets 2--4. The same wrong
    range appears in the notes of the same date on `E-HAT-2.B-5`, `-2.B-7` and `-2.C-6` and is
    corrected by a new event on each of those cards. Unchanged and re-checked: the statement as printed
    on p. 184, every step of the proof, and the description of the two Stack Exchange answers. Not
    claimed: a published solution of Exercise 2.C.1.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, third pass on this card: the timestamps are right, and the attribution of
    them is wrong in two places of this date. Read again through the Stack Exchange API on 2026-11-16:
    question 3590105 has `creation_date` **1584866748** and the accepted answer 3590397 has
    **1584888044**; both are 2020-03-22. (1) The first `source-corrected` event of this date gives
    "question `creation_date` 1584866748 and answer `creation_date` 1584866744", so its answer value
    is wrong. (2) The second `source-corrected` event of this date calls 1584866744 "the question's
    number": it is not, the question's being 1584866748, and it is neither the question's nor the
    answer's. The repaired answer value 1584888044 in that event is correct, and the date 2020-03-22
    stands. Nothing else changes: the statement as printed on p. 184, every step of the proof, and the
    description of the two answers stand. The same correction is made in COMPLAINTS.md.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, third pass on this card: one sentence of the record, and one false
    attribution in it. The `source-corrected` event of this date beginning "#123 reader's
    report, second pass on this card" says the value 1584866744 "is the question's number,
    not the answer's". Read again through the Stack Exchange API on 2026-11-16, question
    3590105 has `creation_date` **1584866748** and the accepted answer 3590397 has
    **1584888044**, so 1584866744 is neither the question's nor the answer's: the
    correction that event makes is right about the answer's number and wrong about whose
    number the old one was. The date 2020-03-22 stands, answer 4874176 is dated 2024-03-02,
    and the body of the card names both by date only, so nothing on the card changes. Not
    claimed: a published solution of Exercise 2.C.1, which has not been located.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    #123 transcription batch. The solution was rewritten as the two answers' argument for
    $n>0$, each step citing its answer and paragraph: answer 3590397 (accepted, Paul Frost,
    posted 2020-03-22) for the universal-cover bound (the lift $\bar f$ of the simplicial map to
    the induced triangulations of $\RR$, $\bar f(w_{k+1})=w'_1+n$, then $n\ell+1$ vertices in
    $[w'_1,w'_1+n]$ each in the image of $w_1,\ldots,w_{k+1}$ by the intermediate value theorem,
    so $k\ge n\ell$) and answer 4874176 (D Ford, posted 2024-03-02) for the fundamental-cycle
    form the card's bound step states. Both read in
    `tmp/sources/mse-3590105-simplicial-map-circle-degree.md`, the text version of the thread.
    Two things the transcription settles that the card had left implicit: 4874176 writes that
    every edge is sent homeomorphically to an edge, and the vertex case is the one whose
    coefficient is $0$, so the card's step keeps the disjunction; and 3590397's last sentence
    ("Obviously there are solutions with $3n$ vertices") is the source of the attainment step.
    Not transcribed, because neither answer treats them: $n<0$ and $n=0$. The card keeps its own
    constructions for those two cases, now in a step that says so, and `COMPLAINTS.md` carries a
    record of this date naming them as having no published proof. Checked against Hatcher (2002),
    §2.C Exercise 1 on printed p. 184, read in
    `tmp/sources/hatcher-2002-algebraic-topology.md`; the printed page was confirmed against the
    PDF, whose page 193 carries the printed folio 184 at §2.C's exercises. Not claimed: a proof of
    the $n<0$ or $n=0$ cases in any publication.

---

::: {.problem}
What is the minimum number of edges in simplicial complex structures $K$ and $L$ on $S^1$ such that there is a simplicial map $K \to L$ of degree $n$?
:::

::: {.solution}
The case $n>0$ is the argument of the two answers to *[Simplicial map of the circle $S^1$](https://math.stackexchange.com/questions/3590105/simplicial-map-of-the-circle-s1)*, Math StackExchange question 3590105, read in `tmp/sources/mse-3590105-simplicial-map-circle-degree.md`: the accepted answer 3590397 (Paul Frost, posted 2020-03-22) bounds the domain through the universal cover of $S^1$, and answer 4874176 (D Ford, posted 2024-03-02) states the same bound in fundamental-cycle form. Both answers treat $n>0$ only. Write $e(K)$ and $e(L)$ for the numbers of edges, and orient both simplicial circles.

::: pf

::: {.pf-step #cover}
If $f:K\to L$ is a simplicial map of degree $n>0$ and $L$ has $\ell$ vertices, then $K$ has at least $n\ell$ vertices.

::: pf-proof
This is the argument of answer 3590397, paragraphs 4--8. A triangulation $\tau$ of $S^1$ with $k$ vertices induces a triangulation $\bar\tau$ of $\RR$ for which the standard covering $p(t)=e^{2\pi it}$ is simplicial, and a simplicial map $f:(\tau)\to(\tau')$, with $\ell$ vertices in $\tau'$, lifts to a simplicial map $\bar f:(\RR,\bar\tau)\to(\RR,\bar\tau')$. Choose consecutive lifts $w_1<w_2<\cdots<w_k<w_{k+1}=w_1+1$ of the $k$ vertices of $K$, and $w'_1$ a lift of the image of $w_1$. Then $\bar f(w_{k+1})=w'_1+n$ for an integer $n$, since $p\bar f(w_{k+1})=f(v_1)=p\bar f(w_1)$; and since the degree of $f$ is $\bar f(t+1)-\bar f(t)$ for any $t$, that integer is $\deg f=n$. For $n>0$ the segment $[w'_1,w'_1+n]$ contains exactly $n\ell+1$ vertices of $\bar\tau'$, and each of them is the image of one of $w_1,\ldots,w_{k+1}$, since otherwise $\bar f([w_1,w_{k+1}])$ could not contain the whole interval $[w'_1,w'_1+n]$ — this is where the answer uses the intermediate value theorem. Hence $k+1\ge n\ell+1$, that is $k\ge n\ell$. A simplicial complex structure on $S^1$ has as many edges as vertices here, so the same count is $e(K)\ge n\,e(L)$.
:::

:::

::: {.pf-step #bound}
If $f:K\to L$ is a simplicial map of degree $n>0$, then
$$
e(K)\ge n\,e(L)\ge 3n.
$$

::: pf-proof
The first inequality is answer 4874176 in fundamental-cycle form: write $z_K=\sum_e\epsilon_e e$ and $z_L=\sum_a\epsilon_a a$ for the two simplicial fundamental cycles. The answer's computation is $f_*(\tilde e_1+\cdots+\tilde e_k)=n(e_1+e_2+e_3)$, and a simplicial map sends an edge either to a vertex or homeomorphically to an edge, so its coefficient on chains is $0$ or $\pm1$; every target edge therefore receives total signed coefficient $n$ from at least $n$ distinct domain edges. (The answer prints that each edge is sent homeomorphically to one of the three, the vertex case being the one in which its coefficient is zero.) Hence $e(K)\ge n\,e(L)$. A simplicial complex on $S^1$ cannot have a loop edge or two edges with the same pair of endpoints, so it has at least three edges: this is the observation the question itself opens with, that a simplicial structure on $S^1$ must have at least $3$ vertices, and answer 3590397 closes by applying it to $\tau'$, whose minimal number of vertices is $3$. With $e(L)\ge3$ the second inequality follows. Answer 3590397 draws the same conclusion in vertex form: for $\deg(f)=n>1$ the two triangulations cannot coincide, and $\tau$ must have at least $n$ times as many vertices as $\tau'$, hence a minimum of $3n$.
:::

:::

::: {.pf-step #attain}
For every $n>0$ the bound $e(L)=3$, $e(K)=3n$ is attained.

::: pf-proof
Let $L$ be a triangle and $K$ a polygon with $3n$ edges, and map successive triples of edges of $K$ around the three edges of $L$, repeating exactly $n$ times with the positive orientation. On the circle this is the map $z\mapsto z^n$ from the $3n$-th roots of unity to the third roots of unity, which is simplicial of degree $n$: this is the construction in the question's second paragraph, and answer 3590397 closes by asserting that a minimum of $3n$ vertices suffices, "obviously there are solutions with $3n$ vertices".
:::

:::

::: {.pf-step #negative-and-zero}
The cases $n<0$ and $n=0$ are not in either source, and the card states them itself.

::: pf-proof
Neither answer treats a non-positive degree: 3590397 assumes $n>0$ before its vertex count, and 4874176 counts at least $n$ preimages. The card supplies the two cases rather than leaving the exercise half-answered. For $n<0$ the polygon of step [](#attain) traversed with the reverse orientation is a simplicial map of degree $n$ with $e(K)=3\abs{n}$, and the count of step [](#bound) with $\abs{n}$ in place of $n$ gives $e(K)\ge\abs{n}\,e(L)$ in the same way. For $n=0$ take both complexes to be triangles and $f$ constant: it is simplicial and of degree zero, with $e(K)=e(L)=3$. These two constructions are the card's own; no published proof of either case has been located, and `COMPLAINTS.md` records that on this date.
:::

:::

:::

For $n>0$ the minimum is therefore $e(L)=3$ and $e(K)=3n$, by steps [](#bound){.pf-ref} and [](#attain){.pf-ref}; with the card's own constructions for $n\le0$ the exercise's answer is
$$
\boxed{e(L)=3,\qquad e(K)=3\max\{1,\abs{n}\}.}
$$

The exercise is Exercise 1 of §2.C, printed p. 184 of Hatcher, *Algebraic Topology* (2002), read in `tmp/sources/hatcher-2002-algebraic-topology.md`; the two Math StackExchange answers were read in `tmp/sources/mse-3590105-simplicial-map-circle-degree.md`, which is the thread's text version.
:::
