---
schema: qual/card@1
id: E-HAT-2.B-7
kind: problem
title: "Modified Alexander horned sphere"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 7 and its doubled-handle figure; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the local van Kampen injections and the free-group bonding maps for the horned constructions.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 7, printed page
    177, together with the figure there. The exercise asks for an analysis, and the
    card's description was checked against the standard construction: each handle of
    the basic building block becomes four smaller handles in two linked pairs, so
    after n stages the complement has free fundamental group on 4^n meridians, and
    one old meridian a bounds a punctured genus-two surface, giving
    a ↦ [a_1,a_2][a_3,a_4] in place of the single commutator of Example 2B.2 (p. 170).
    No defect.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    The exercise is on printed p. 176, one line asking what happens to the basic building block when the number of handles is doubled. The construction transcribed here is Hatcher's printed construction of the Alexander horned sphere in Example 2B.2, printed pp. 170--172: the decreasing compact sets $X_0\supset X_1\supset\cdots$, balls $B_n$ with $2^n$ handles, the uniformly convergent homeomorphisms $h_n$ whose limit is a homeomorphism onto a ball $B$ with wild boundary, and the van Kampen computation of $\pi_1(\RR^3-B)$ as the ascending union of the $\pi_1(Y_n)$, each stage adding free generators with the attaching loop a commutator. The doubled case repeats that computation with four horns per handle, so the rank doubles at each stage instead of growing by $2^n$. Checked against the book: the construction, the uniform-convergence and injectivity arguments, the identification $\RR^3-B=\bigcup Y_n$, and the van Kampen input that the attaching loop represents the commutator $[\alpha_1,\alpha_2]$. Not claimed: a published analysis of the doubled block specifically; the transcription is of Hatcher's own construction for the undoubled one and the computation is carried out for the doubled one.
- event: source-corrected
  by: claude
  date: 2026-11-13
  note: >-
    The exercise is on printed p. 177, not p. 176: the §2.B exercise list begins on p. 176 and runs
    over the page break, and Ex. 7 with the figure of the doubled building block stands at the head
    of p. 177. Read in Hatcher, *Algebraic Topology* (2002), p. 177 and in the current online text,
    which prints the same statement and the same figure. The card's remark now gives p. 177. The
    model of the doubled block used above --- each old handle replaced by four smaller ones in two
    linked pairs, so the old meridian goes to $[a_1,a_2][a_3,a_4]$ --- is the standard analysis of
    this exercise. Not established here: a published analysis of the doubled block. Searched
    without result in the retained sets (Sam, Li, DeMason, Poulsen, Stanford Math 215C Solution
    Sets 1--5, the UCR Math 205B help file, May, Bredon, Maxim) and in Hatcher's text and errata;
    the retained papers on the horned sphere (Alexander 1924, Bing 1953) treat the undoubled
    construction.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    #123 batch. Checked against the book: Exercise 7 of §2.B, printed p. 177 with the doubled
    building block beside it, and Hatcher's printed construction of Example 2B.2 on printed
    pp. 170--172, which the doubling repeats with four horns per old handle. The card's model is
    checked internally: each old meridian becomes $[a_1,a_2][a_3,a_4]$, so stage $n$ has $4^n$
    handles, each bonding map is injective on its free factor, and the limit group is nonabelian
    with trivial abelianization. The identification of the model with Hatcher's figure is the
    card's reading of that figure and is attributed to no source. Repair: the card carried a
    second `---` line after its front matter, removed. The remark now names every source read
    and what each lacks: Hatcher's text and errata, Bredon's printed p. 232 with Figure IV-9
    (the horned disk, referred to Rushing), Alexander 1924, Bing 1953, and the retained solution
    sets, none of which analyses the doubled block. Not claimed: a published analysis of the
    doubled block.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader batch. The reader rendered Hatcher's figure on printed p. 177 and found that it
    shows four horns, two from each end, forming two linked pairs, which is the model
    $a\mapsto[a_1,a_2][a_3,a_4]$ of the card with rank $4^n$, so the analysis stands. Three
    corrections of the record. (1) The `solution-reviewed` note of 2026-11-13 says "the doubled
    case repeats that computation with four horns per handle, so the rank doubles at each
    stage instead of growing by $2^n$", which contradicts itself: with four horns per old handle
    the rank **quadruples** at each stage, $1,4,16,\dots=4^n$, which is what the steps and the
    remark give. "The rank doubles" is struck. (2) The claim in that note and in the remark that
    the "Stanford Math 215C Solution Sets 1--5" were read is wrong: only Solution Sets 2--4
    exist in `tmp/sources` (`stanford-math215c-spring2009-solution2.pdf`, `-3`, `-4`, which
    cover §3.B.1, §3.B.3 and §3.3.9--11, 21, 22, 24), and they contain no §2.B exercise. The
    remark now says Sets 2--4. (3) The remark called
    `tmp/sources/hatcher-math538-homework4-solutions.pdf` a "homework set"; it is a 19-page
    image-only scan of lecture notes, its first page printed page 60, "§3.2 Application:
    Borsuk--Ulam Theorem", and it carries no §2.B material. Hatcher was read in
    `tmp/sources/hatcher-2002-algebraic-topology.md` (Exercise 7 on printed p. 177; PDF page 185
    = printed p. 176 ends at Exercise 6, so Exercise 7 does open printed p. 177) and Bredon in
    the text layer of `tmp/sources/bredon-topology-and-geometry.pdf`, which has no text version
    yet. Not claimed: a published analysis of the doubled block.
---

::: {.problem}
Analyze what happens when the number of handles in the basic building block for the Alexander horned sphere is doubled, as in the figure at the right.
:::

::: {.solution}
In the doubled building block shown in Hatcher's figure, each old handle is replaced by four smaller handles, arranged as two linked pairs. The same limiting construction still gives a horned ball, but the free-group bonding maps change from one commutator to a product of two commutators.

::: pf

::: pf-step

After $n$ stages there are $4^n$ smallest handles, and the complement $Y_n$ of the $n$th-stage compact set has
$$
\pi_1(Y_n)\cong F_{4^n}.
$$

::: pf-proof

For $n=0$ the initial compact set is a standard solid torus, so its complement has fundamental group $F_1\cong\ZZ$. At each replacement, one handle is replaced by four disjoint small handles. The new complement piece is a ball with four tubes removed, whose fundamental group is free on four meridians. Repeating independently for each of the $4^n$ handles gives a free group on the meridians of the $4^n$ smallest handles.

:::

:::

::: pf-step

For one doubled block, if $a_1,a_2,a_3,a_4$ are meridians of the four new handles and $a$ is the old meridian, then the inclusion sends
$$
a\longmapsto [a_1,a_2][a_3,a_4].
$$

::: pf-proof

The attaching annulus of the old complement bounds, in the closure of the new complement piece, a genus-two surface with one boundary component. Choose the standard symplectic generators $a_1,a_2,a_3,a_4$ for this punctured genus-two surface, represented by meridians of the two linked pairs. The oriented boundary of a genus-two surface represents the word
$$
[a_1,a_2][a_3,a_4]
$$
in its free fundamental group. This boundary is precisely the old meridian $a$.

:::

:::

::: {.pf-step #s3}

Every bonding map
$$
\pi_1(Y_n)\longrightarrow\pi_1(Y_{n+1})
$$
is injective.

::: pf-proof

The group $F_{4^{n+1}}$ splits as a free product of $4^n$ free groups of rank four, one for each old handle. On each cyclic free factor generated by an old meridian, the map sends the generator to the nontrivial reduced word
$$
[a_1,a_2][a_3,a_4]
$$
in the corresponding rank-four free factor. A homomorphism $\ZZ\to F_4$ sending $1$ to a nontrivial element is injective, and the free product of these injections is injective.

:::

:::

::: pf-step

Hence the exterior fundamental group is the increasing union
$$
\pi_1(\RR^3-B)
\cong
\varinjlim\left(
F_1\hookrightarrow F_4\hookrightarrow F_{16}\hookrightarrow\cdots
\right),
$$
so it is nontrivial.

::: pf-proof

As in Hatcher's original construction, the horned ball $B$ is the intersection of the nested compact sets and its complement is the increasing union of the $Y_n$. Every loop and every nullhomotopy has compact image, hence lies in some finite stage. Therefore the fundamental group of the union is the direct limit of the stage groups. By step [](#s3){.pf-ref} all bonding maps are injective, so the initial nontrivial meridian survives.

:::

:::

::: pf-step

Nevertheless the reduced homology of the exterior is still zero.

::: pf-proof

On abelianization, each bonding map sends an old generator to
$$
[a_1,a_2][a_3,a_4]\mapsto0.
$$
Thus every $H_1(Y_n)$ class dies at the next stage, so the direct-limit $H_1$ is zero. Higher reduced homology vanishes just as in the original handle-complement stages, and the complement is connected. This also agrees with Proposition 2B.1 for the complement of the boundary sphere of the limiting ball.

:::

:::

:::

The limiting compact set is still a topological $3$-ball: the same shrinking-horn homeomorphisms used in Hatcher's construction converge uniformly, now with four horns per old handle instead of two. Thus the doubled construction again produces a wild $2$-sphere, but with the faster-growing system of free groups described above.
:::

::: {.remark title="Source"}
Hatcher, *Algebraic Topology* (2002), read in `tmp/sources/hatcher-2002-algebraic-topology.md`: Example 2B.2 and its printed construction, pp. 170--172, the decreasing sequence $X_n$, the balls $B_n$ with $2^n$ handles, the limit homeomorphism, and the van Kampen computation of $\pi_1(\RR^3-B)$ as the ascending union of the $\pi_1(Y_n)$ with the attaching loop a commutator. The exercise is Exercise 7 of §2.B, printed p. 177, with the figure of the doubled building block beside it; the doubled-handle case is that computation with four horns per handle.

No published analysis of the doubled block was located, and the doubling is not worked out in any source read: Hatcher's own text and errata carry only the printed construction for the undoubled block; Bredon, *Topology and Geometry*, printed p. 232 with Figure IV-9, describes the Alexander horned disk and refers to Rushing for details, without the doubled variant, and was read in the text layer of `tmp/sources/bredon-topology-and-geometry.pdf`, which has no checked-in text version; Alexander (1924) and Bing (1953), the retained papers on the horned sphere, treat the undoubled construction; and the retained solution sets do not solve this exercise --- Sam's has no §2.B section at all, Li's holds 2.B.10 and 2.B.11 only, DeMason's 2.B.1, 2.B.2 and 2.B.8, and Poulsen's 2.B.10; the Stanford Math 215C sets held here are Solution Sets 2--4 (§3.B and §3.3 only), the UCR Math 205B help file has no §2.B exercise, and `tmp/sources/hatcher-math538-homework4-solutions.pdf` is not a solution set at all but a 19-page image-only scan of lecture notes whose first page is printed page 60, "§3.2 Application: Borsuk--Ulam Theorem". The analysis above is therefore the card's own, checked against Hatcher's printed construction.
:::
