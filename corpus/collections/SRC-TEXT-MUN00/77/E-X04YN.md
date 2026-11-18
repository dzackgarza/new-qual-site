---
schema: qual/card@1
id: E-X04YN
kind: problem
title: Elementary operations behind the classification figures
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §77 Exercise 2, printed p. 470. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md. No source was saved. The queries were the Stack Exchange advanced
    search "Munkres elementary operations Figures 77.1" (no hits) and the similar-question search from
    "Elementary operations on labelling schemes in Munkres classification of surfaces" (15 items), whose
    threads restate operations (i) to (v) of §76 and answer no part of this exercise; the figures themselves
    are not in the checkout's extraction of the book, which drops them, so a source reproducing the figures
    could not be checked against them in any case. The card keeps its own proof, which is the sequence of
    operations for each figure.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 77 Exercise 2, printed p. 470. The operation sequences for Figures 77.1 to 77.5, whose net effects are the equivalences (i) and (iii) that the book states for the same lemmas: Lemma 77.1 and the last display of Lemma 77.3, w ~ w_0aba^{-1}b^{-1}[y_1y_4y_3y_2y_5]. The card's final boxed word is exactly that. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof, and the doubt recorded in the earlier audit resolved: the five
    figures are legible on the PDF pages that carry them (printed pp. 464, 466, 467 and 468), so the
    sequences were checked against the drawings and against the schemes the book derives from them. The
    earlier note had concluded that the figures could not be checked at all, which was true of checking a
    *third-party source* against them and not of reading them. Each sequence is now named in the
    operations (i)--(vii) of Section 76, with the side conditions the operations carry --- the auxiliary
    label unused, both pieces of the cut having at least three sides, the pasted label occurring nowhere
    else --- instead of being described as a generic cut and paste. The net words are unchanged and match
    the proofs of Lemmas 77.1 and 77.3.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    A review reported that the relabelling recorded for Figures 77.4 and 77.5 does not produce the
    schemes displayed. Confirmed for 77.4 and repaired: relabelling c by b alone gives
    w_0 b [y_1y_4y_3] a^-1 b^-1 a [y_2y_5], not w_0 a [y_1y_4y_3] b a^-1 b^-1 [y_2y_5]; the card now
    records the three relabellings that do (a by b, c by a, then reversing every b exponent). For
    77.5 the review proposed a cyclic permutation after c by b; that does not work, and the card
    now says so with the computation: a rotation of the word moves the prefix w_0 and the block Y as
    well, so it cannot turn w_0 b a^-1 b^-1 a [Y] into w_0 a b a^-1 b^-1 [Y]. What does work, and
    is now recorded, is the chain a by d, b by a, d by b, then reversing every b exponent, each step
    an instance of operation (iii) of Section 76 (printed pp. 460-461). The net words are unchanged.
---

::: {.exercise}

(a) Write down the sequence of elementary operations required to carry out the arguments indicated in Figures 77.1 and 77.2.

(b) Write down the sequence of elementary operations required to carry out the arguments indicated in Figures 77.3, 77.4, and 77.5.
:::

::: {.solution}

No complete published solution of this exercise was located; the sets searched are listed in the `COMPLAINTS.md` entry for §§74--85 of `SRC-TEXT-MUN00`, and the scheme computations below are the book's own, from the proofs of Lemma 77.1 and Lemma 77.3. What the card supplies is the part the exercise asks for and the book leaves to the reader: the name of each elementary operation in the sequence, and the effect of each on the labelling scheme.

The five figures were read from the pages of the PDF on which they are printed --- Figure 77.1 and Figure 77.2 on printed p. 464, Figure 77.3 on p. 466, Figure 77.4 on p. 467, Figure 77.5 on p. 468 --- because the extraction at `tmp/sources/munkres-2000-topology.md` drops the figures and leaves only their captions. An earlier audit of this card recorded that no source reproducing the figures could be checked against them; that applied to a *source*, and the figures themselves are legible on those pages, so the sequences below were checked against the drawings and against the schemes the book derives from them.

The statement was checked against Munkres, *Topology* (2000), §77 Exercise 2, printed p. 470, with the elementary operations (i)--(vii) of §76 on printed pp. 460--461 and the proofs of Lemma 77.1 (printed p. 463) and Lemma 77.3 (printed p. 465). Throughout, a scheme is a word in labels with exponents $\pm1$, $[y]$ denotes the bracketed subword, $y^{-1}$ its formal inverse, and the operations used are: **(i) cut** along an arc with a new label $c$, replacing one polygon by two, allowed when the label $c$ is unused and both pieces have at least three sides; **(ii) paste**, the inverse of (i); **(iii) relabel**, replacing a label by an unused one or reversing all its exponents; **(iv) permute**, a cyclic permutation of a scheme; **(v) flip**, replacing a scheme by its formal inverse.

::: pf

::: {.pf-step #fig-77-1}

(a) Figure 77.1 carries $a[y_{1}]a[y_{2}]$ to $aa[y_{1}^{-1}y_{2}]$ by three operations: cut along an auxiliary arc $c$, paste the two $a$-edges, relabel $c$ by $a$.

::: pf-proof

On printed p. 464 the polygon has boundary $a\,y_{1}\,a\,y_{2}$, with the two $a$-edges drawn on the left and on the right, and the dashed auxiliary arc joins two of its vertices; the right-hand drawing shows the two $a$-edges pasted to a single interior edge, labelled $a$ in the middle, and the boundary of the resulting polygon carrying the two cut edges labelled $c$ with the subwords $y_{1}$ and $y_{2}$ between them.

In the language of §76: operation (i) cuts along that arc, introducing the new label $c$, allowable because $c$ is unused and both pieces have at least three sides — $y_{1}$ and $y_{2}$ are nonempty, which is the case the proof is in; operation (ii) pastes the pair of edges labelled $a$, which occurs nowhere else and so may be pasted away; operation (iii) relabels $c$ by $a$, which is now unused. The boundary of the single polygon that remains reads $c\,[y_{1}^{-1}]\,c\,[y_{2}]$ up to a cyclic permutation, since going once round the cut polygon reverses the orientation of $y_{1}$; relabelling $c$ to $a$ gives $aa[y_{1}^{-1}y_{2}]$, the scheme of Step 1 of the proof of Lemma 77.1 (printed p. 463).

:::

:::

::: {.pf-step #fig-77-2}

(a) Figure 77.2 carries $[y_{0}]a[y_{1}]a[y_{2}]$ to $b[y_{2}]b[y_{1}y_{0}^{-1}]$ by the same three operations with the auxiliary label $b$.

::: pf-proof

On printed p. 464 the polygon has boundary $y_{1}$ along the top, $a$ on the left, $y_{2}$ and then $y_{0}$ along the bottom, and the second $a$ at the lower right; the dashed arc labelled $b$ runs from the upper right to the bottom edge, and the right-hand drawing shows the $a$-edges pasted to an interior edge and the boundary carrying $b$ on the left and $b$ on the right with $y_{0}$ and $y_{1}$ at the top and $y_{2}$ at the bottom.

So the sequence is again operation (i) along the arc $b$, operation (ii) pasting the $a$-pair, and operation (iii) relabelling the new pair — here nothing is relabelled, the new label $b$ being the one the scheme displays — together with a cyclic permutation (iv) that puts $y_{2}$ first. The result is $b[y_{2}]b[y_{1}y_{0}^{-1}]$, which is the scheme Step 2 of the proof of Lemma 77.1 obtains (printed p. 463). From it the proof reaches the lemma by operation (i) of Step 1 applied to the pair of $b$'s, then flipping (v), then permuting and relabelling (iv) and (iii):
$$
b[y_{2}]b[y_{1}y_{0}^{-1}]\sim bb[y_{2}^{-1}y_{1}y_{0}^{-1}]\sim[y_{0}y_{1}^{-1}y_{2}]b^{-1}b^{-1}\sim aa[y_{0}y_{1}^{-1}y_{2}].
$$

:::

:::

::: {.pf-step #fig-77-3}

(b) Figure 77.3 carries $w=w_{0}[y_{1}]a[y_{2}by_{3}]a^{-1}[y_{4}b^{-1}y_{5}]$ to $w^{\prime}=w_{0}a[y_{2}]b[y_{3}]a^{-1}[y_{1}y_{4}]b^{-1}[y_{5}]$.

::: pf-proof

On printed p. 466 the polygon has $y_{3},b,y_{2}$ along the top, $a$ on both sides, and $y_{4},b,y_{5},w_{0},y_{1}$ along the bottom, with the dashed arc $c$ joining two vertices; the right-hand drawing shows the $a$-edges pasted to an interior edge and the cut edges labelled $c$ at the far left and far right. The book states the intermediate scheme
$$
w_{0}c[y_{2}by_{3}]c^{-1}[y_{1}y_{4}b^{-1}y_{5}],
$$
and notes that the cut at $c$ may be made because both resulting polygons have at least three sides.

The sequence is therefore operation (i) along $c$, operation (ii) pasting the $a$-pair, and operation (iii) relabelling $c$ by $a$; the bracketed subwords then regroup as $a[y_{2}]b[y_{3}]a^{-1}[y_{1}y_{4}]b^{-1}[y_{5}]$, which is the scheme $w^{\prime}$ of the first cutting and pasting in the proof of Lemma 77.3.

:::

:::

::: {.pf-step #fig-77-4}

(b) Figure 77.4 carries $w^{\prime}$ to $w^{\prime\prime}=w_{0}a[y_{1}y_{4}y_{3}]ba^{-1}b^{-1}[y_{2}y_{5}]$.

::: pf-proof

On printed p. 467 the polygon has $b,y_{3},y_{2}$ along the top, $a$ on both sides, and $y_{1},y_{4},y_{5},w_{0},c$ along the bottom, with the pasted edge $b$ now interior and drawn in the middle; the right-hand drawing carries $c$ twice, at the top and at the bottom. The book states
$$
w^{\prime}\sim w_{0}c[y_{1}y_{4}y_{3}]a^{-1}c^{-1}a[y_{2}y_{5}],
$$
and then the scheme $w^{\prime\prime}$ by relabelling.

The sequence is operation (i) along the arc $c$, operation (ii) pasting the $b$-pair --- the label $b$ occurs nowhere else once the pasting is made --- and then operation (iii) three times, which is what the book's "by relabelling" leaves to be spelled out: relabelling $a$ by $b$ turns $w_{0}c[y_{1}y_{4}y_{3}]a^{-1}c^{-1}a[y_{2}y_{5}]$ into $w_{0}c[y_{1}y_{4}y_{3}]b^{-1}c^{-1}b[y_{2}y_{5}]$, relabelling $c$ by $a$ turns that into $w_{0}a[y_{1}y_{4}y_{3}]b^{-1}a^{-1}b[y_{2}y_{5}]$, and reversing the exponent of every occurrence of $b$ gives $w_{0}a[y_{1}y_{4}y_{3}]ba^{-1}b^{-1}[y_{2}y_{5}]$, which is $w^{\prime\prime}$. Relabelling $c$ by $b$ alone would give $w_{0}b[y_{1}y_{4}y_{3}]a^{-1}b^{-1}a[y_{2}y_{5}]$, which is not $w^{\prime\prime}$; the bracketed subword $y_{1}y_{4}y_{3}$ collects the bottom labels in the order the drawing gives them.

:::

:::

::: {.pf-step #fig-77-5}

(b) Figure 77.5 carries $w^{\prime\prime}$ to $w_{0}aba^{-1}b^{-1}[y_{1}y_{4}y_{3}y_{2}y_{5}]$, the scheme of Lemma 77.3.

::: pf-proof

On printed p. 468 the first polygon has $y_{3},y_{4},y_{1},a,w_{0},y_{5},y_{2}$ along the top and $b$ on both sides, and the second shows the cut edges labelled $c$ and the pasted edges $a$ at the bottom; the book states
$$
w^{\prime\prime}\sim w_{0}ca^{-1}c^{-1}a[y_{1}y_{4}y_{3}y_{2}y_{5}]\sim w_{0}aba^{-1}b^{-1}[y_{1}y_{4}y_{3}y_{2}y_{5}],
$$
the second by relabelling.

So the sequence is operation (i) along the arc $c$, operation (ii) pasting the $a$-pair, and then operation (iii) four times: relabelling $a$ by a fresh label $d$, then $b$ by $a$, then $d$ by $b$, and finally reversing the exponent of every occurrence of $b$. Letter by letter,
$$
w_{0}ca^{-1}c^{-1}a[Y]\mapsto w_{0}bd^{-1}b^{-1}d[Y]\mapsto w_{0}ad^{-1}a^{-1}d[Y]\mapsto w_{0}ab^{-1}a^{-1}b[Y]\mapsto w_{0}aba^{-1}b^{-1}[Y],
$$
where $Y=y_{1}y_{4}y_{3}y_{2}y_{5}$ and the first step is the relabelling $c$ by $b$ followed by $a$ by $d$. Relabelling $c$ by $b$ alone leaves $w_{0}ba^{-1}b^{-1}a[Y]$, and no cyclic permutation of that word is $w_{0}aba^{-1}b^{-1}[Y]$ --- a rotation moves the block $w_{0}$ and the block $[Y]$ as well --- so a cyclic permutation is not what carries the intermediate to the target; the relabelling chain above is. The resulting word $w_{0}aba^{-1}b^{-1}[y_{1}y_{4}y_{3}y_{2}y_{5}]$ is exactly the scheme $w^{\prime\prime\prime}$ that the third cutting and pasting of Lemma 77.3 produces, so the operations named are the ones the figure indicates.

:::

:::

::: pf-step

Each of the five figures is carried out by a cut, a paste and a relabelling, and the resulting schemes are the ones the proofs of Lemmas 77.1 and 77.3 use.

::: pf-proof

Steps [](#fig-77-1){.pf-ref} and [](#fig-77-2){.pf-ref} answer part (a): the two sequences are operation (i), (ii), (iii) with auxiliary labels $c$ and $b$, and the schemes they produce, $aa[y_{1}^{-1}y_{2}]$ and $b[y_{2}]b[y_{1}y_{0}^{-1}]$, are those of Step 1 and Step 2 of Lemma 77.1. Steps [](#fig-77-3){.pf-ref}, [](#fig-77-4){.pf-ref} and [](#fig-77-5){.pf-ref} answer part (b): the same three operations with auxiliary label $c$, producing $w^{\prime}$, $w^{\prime\prime}$ and $w_{0}aba^{-1}b^{-1}[y_{1}y_{4}y_{3}y_{2}y_{5}]$, which are the three schemes the successive cuttings and pastings of Lemma 77.3 produce.

:::

:::

:::

:::
