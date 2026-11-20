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
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, second pass on this card: two defects of the record, both in the
    `source-corrected` note of this date above and in the remark. (1) That note assigned the claim
    "Stanford Math 215C Solution Sets 1--5 were read" to the `solution-reviewed` note of 2026-11-13. The
    claim is not in that note: it is in the `source-corrected` note of 2026-11-13, two events below it.
    The attribution is corrected here. (2) The coverage of the Stanford sets is not "§3.B and §3.3
    only": read again in the three PDFs this pass, Set 2 holds §3.2 exercises 1, 2, 11 and 15 together
    with §3.B exercises 1 and 3, Set 3 holds §3.3 exercises 9--11, and Set 4 holds §3.3 exercises 21, 22
    and 24 together with M&T 8.2, 8.5, 8.6 and 9.1. Neither Solution Set 1 nor Solution Set 5 exists in
    `tmp/sources`, so "Sets 1--5" is wrong as well. The remark now gives the four sections the sets
    actually cover, and the conclusion that none of them reaches §2.B stands: there is no §2.B exercise
    in any of the three. The same wrong range on `E-HAT-2.B-5`, `-2.C-1` and `-2.C-6` is corrected by a
    new event on each of those cards. Unchanged and re-checked: the statement as printed on p. 177 with
    its figure, and the analysis, which is the card's own.
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    #123 acceptance pass on this card: a published candidate for the doubled block was located and its
    full text could not be read. Norman William Riebe, *The Fundamental Groups of the Complements of
    Some Solid Horned Spheres*, MS thesis, Utah State University, 1968, DOI 10.26076/c3c1-48f0, open
    access at `https://digitalcommons.usu.edu/etd/6821/`. The published abstract, read there on
    2026-11-18, calls the classical Alexander horned sphere a 2-horned sphere of order 2, constructs
    2-horned spheres of orders 3 and 4 by the same generalization, computes the fundamental groups of
    the complements of all three, and states that the resulting groups are free of countably infinite
    rank, so the three embeddings cannot be distinguished by fundamental groups. The thesis PDF at the
    publisher's `viewcontent.cgi` endpoint answered with a Cloudflare challenge ("Just a moment...") on
    the same date, so no page of the thesis was read, no printed page is cited from it, and nothing on
    this card is transcribed from it. Whether Riebe's order-4 building block is Hatcher's doubled one
    (four horns per old handle, printed p. 177) is not settled by the abstract, and the free-group
    conclusion is recorded as the abstract's, not as a theorem checked here. The remark now carries
    that finding. The source obligation for the exercise stays open, and the analysis remains the
    card's own. Checked this pass and unchanged against the book: Example 2B.2 and its construction,
    printed pp. 170--172, and the exercise with its figure, printed p. 177.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    #123 pass, disposition of the doubled block: no published argument for it was located, and the
    part is named on this card and in `COMPLAINTS.md` item 11 as the card's own argument, not as a
    published solution. Checked this pass: Hatcher's construction, printed pp. 170--172, and the
    exercise with its figure, printed p. 177; and, for the record, that Riebe's 1968 Utah State
    thesis on 2-horned spheres of orders 3 and 4 is open access but answers with a Cloudflare
    challenge at its PDF endpoint, so no page of it has been read. Not claimed: a published analysis
    of the doubled block, and no transcription from Riebe.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The owner's acceptance rule of this date, third disposition, stated on this card: no published
    argument for the doubled-handle construction was found by either reader, so the part is named as
    the card's own here and in `COMPLAINTS.md` item 11, and that naming is a record of what the card
    owes rather than an acceptance of the part from a published source. The remark now says so.
    Checked this pass and unchanged: Hatcher's printed construction, pp. 170--172, and the exercise
    with its figure, printed p. 177.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The owner's acceptance rule applied to step \#s3: the injectivity of the bonding maps is
    Hatcher's argument for the undoubled block, printed pp. 170--172, and the word
    $[a_1,a_2][a_3,a_4]$ with the rank $4^{n+1}$ is the card's own reading of the figure on
    printed p. 177. The step now says both. Checked: Hatcher's injectivity argument at those pages.

- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    A false record corrected: the remark called `tmp/sources/hatcher-math538-homework4-solutions.pdf`
    a "19-page image-only scan". It has a text version,
    `tmp/sources/hatcher-math538-homework4-solutions.md`, 19 pages beginning with printed page 60,
    "§3.2 Application: Borsuk--Ulam Theorem", and the remark now cites it. The substantive point is
    unchanged and re-checked there: the file is lecture notes, not a solution set, and reaches no §2.B
    exercise.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The event above is itself wrong in one clause and is corrected here: it withdrew "19-page
    image-only scan" as a false record, and that description is true. `pdftotext` yields one byte per
    page for all nineteen pages of
    `tmp/sources/hatcher-math538-homework4-solutions.pdf`, so the PDF carries no text layer, and the
    `.md` beside it is an OCR of those scans. What the file holds is what `COMPLAINTS.md` line 526
    records: typed notes from printed page 60 (§3.2, Borsuk--Ulam) and handwritten Problem Sets 3
    and 4 on §3.1--§3.2. The remark now states both, and the substantive point stands: the file holds
    no §2.B exercise, so it does not bear on this card. Checked: the per-page text yield of the PDF,
    the `.md`'s opening and closing pages, and the coverage record.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    The card's own analysis tested, since no published argument exists for this part. (1) The figure
    on printed p. 177 was rendered at 500 dpi from `tmp/sources/hatcher-2002-algebraic-topology.pdf`
    (PDF page 186) and read: it shows the building block with four horns arranged as two hook-and-eye
    pairs, one pair in each half of the ball, each pair's two horns interlocking as chain links ---
    which is the model this card draws on, $a\mapsto[a_1,a_2][a_3,a_4]$ per old handle at rank
    $4^n$. (2) The group step \#s3 was decided by a free-group computation, run over the words
    $w=[a_1,a_2][a_3,a_4]$ with exact reduction: $w$ reduces to the eight-letter word
    $a_1a_2a_1^{-1}a_2^{-1}a_3a_4a_3^{-1}a_4^{-1}$, is not a proper power, and no power
    $w^{k}$ with $1\le k\le200$ is trivial, so $\ZZ\to F_4$, $1\mapsto w$ is injective as the step
    says (free groups are torsion-free); with a second factor written on its own four letters, powers
    of $w$ in distinct factors never cancel, so the free-product step is the standard universal
    property of free products. Output of the five tests: ok
    test_bonding_map_is_injective_on_a_sample; ok test_commutator_is_not_a_proper_power; ok
    test_free_product_step_is_the_standard_one; ok test_word_has_infinite_order; ok
    test_word_is_nontrivial. Checked: the figure, and the word-theoretic step. Not checked: no
    published source states the doubled case, so the source obligation is untouched by this entry;
    the functional-analytic and topological inputs of the surrounding construction are Hatcher's
    printed pp. 170--172 as the remark says.
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    Access to the one located published candidate re-tested, so that the blocker on this card is a
    record and not an assumption. Norman William Riebe, *The Fundamental Groups of the Complements of
    Some Solid Horned Spheres*, MS thesis, Utah State University 1968, DOI 10.26076/c3c1-48f0, is
    indexed as open access: OpenAlex W2767638993 reports `open_access.is_oa` true with
    `oa_status` green and `has_content.pdf` true. Every route to the bytes failed, with these
    statuses: OpenAlex's own content endpoint `https://content.openalex.org/works/W2767638993.pdf`
    returns HTTP 401 with a JSON body; the Semantic Scholar graph API for the DOI returns HTTP 404
    "Paper ... not found"; Unpaywall's v2 API for the DOI returns HTTP 404; `scholar.archive.org`'s
    search answers with an anti-scrape verification page, which was not worked around; and the
    publisher's `viewcontent.cgi?article=7892&context=etd` endpoint answers with a Cloudflare
    challenge, as recorded in the 2026-11-18 event above. The thesis's abstract, read from the
    landing page, still says only that M2, M3 and M4 are 2-horned spheres of orders 2, 3 and 4 and
    that the complement groups are free of countably infinite rank; whether its order-4 building
    block is Hatcher's doubled one is not settled by the abstract. Not read, therefore not cited,
    and the source obligation stays open.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The one published candidate was obtained and read, and it is excluded: its order-4 sphere is not
    the sphere Hatcher's figure draws. Obtained through the Internet Archive's public copy of the
    publisher's file (`https://web.archive.org/web/20240915224258/https://digitalcommons.usu.edu/cgi/
    viewcontent.cgi?article=7892&context=etd`, snapshot of 2024-09-15, 16104957 bytes, 34 pages, now
    retained as `tmp/sources/riebe-1968-horned-spheres.pdf`); the body pages carry no text layer ---
    one byte each from `pdftotext` --- so every page cited here was read as an image at 260--300 dpi.
    Read: printed p. 2, which describes the construction as using "three, four, or more interlocking
    loops" and names the resulting sphere a 2-horned sphere of order 4, $M_4$, with $M_3$ obtained by
    omitting one loop; printed p. 3, Figure 1, the drawing of $M_4$; printed p. 8, the classical case,
    where the relations reduce to $x_\alpha=[x_{\alpha_1},x_{\alpha_2}]$, a single commutator of the
    two loops; printed pp. 10--13, the generating elements, the six crossing relations and Figure 7,
    the graph for $M_4$; and printed p. 13, where those relations reduce to
    $x_\gamma=[x_{\gamma_1}x_{\gamma_2},\,x_{\gamma_3}x_{\gamma_4}]$. That is a commutator of two
    products of loops. Hatcher's figure on printed p. 177 was read again at 500 dpi: it shows two
    handles, each with two horns hooked through one another, which is a product of two commutators,
    $[a_1,a_2][a_3,a_4]$, and the card's step \#s3 uses that word. The two words are different
    reduced words, so Riebe's four-loop sphere is a different embedding from the one the exercise
    draws, and citing him here would attribute to him a construction he does not analyse. He is
    therefore not cited as this card's source. What he does prove, for his own $M_4$: printed p. 13's
    presentation, and, from printed p. 15 and the abstract on p. v, that the groups $G^k$, $k\ge2$,
    are free of countably infinite rank, so that his $M_2$, $M_3$ and $M_4$ are not distinguished by
    fundamental groups. Checked: every page named above. Not claimed: that the thesis contains
    Hatcher's doubled block, or that its Theorem on $G^k$ applies to it.
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    The published literature on fundamental groups of horned-sphere complements was enumerated from
    the source best placed to know it --- the Literature Cited of the thesis read in the event above,
    printed p. 33, read as an image. It lists exactly two items on horned spheres: W. A. Blankinship
    and R. H. Fox, "Remarks on Pathological Open Subsets of 3-Space and Their Fundamental Groups",
    Proc. Amer. Math. Soc. 1 (1950), 618--624, which is the classical two-horn case; and L. O.
    Cannon, "Sums of Solid Horned Spheres", Trans. Amer. Math. Soc. 122 (1966), 203--228, which
    belongs to the Schoenflies side --- sums of solid horned spheres that are 3-spheres, the Bing and
    Ball line --- and is not a computation of the complement group of a four-horn block. The rest of
    the list is Eilenberg--Steenrod, Crowell--Fox, Magnus--Karrass--Solitar, Massey and Rotman, all
    general references. Nothing in it analyses the block Hatcher's figure draws, and the direct
    searches recorded in the two events above returned no other candidate. The search for a published
    analysis of Hatcher's doubled block is therefore complete for everything reachable here, and what
    remains for this card is a disposition, not a file.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170, the correctness read of this card's own part, which is the model read off the
    figure. The model was wrong and the solution is rewritten. The figure on printed p. 177 was
    rendered at 600 dpi from PDF page 186 of `tmp/sources/hatcher-2002-algebraic-topology.pdf` and
    compared with Hatcher's drawing of the single handle on printed p. 171: each of the two structures
    in the figure has its own arch, its own pair of horns hooked through one another, and its own
    short handle drawn as a dashed arc at that end of the ball. The block therefore has **two**
    handles, one per end, and each handle is decomposed into one pair of horns at the next stage.
    The card had read the two pairs as four horns of a single handle, which gives the relation
    $a\mapsto[a_1,a_2][a_3,a_4]$ and the rank $4^n$; with one pair per handle the relation is the
    single commutator $a\mapsto[a_1,a_2]$ of Hatcher's computation on printed p. 171 and the rank is
    $2^{n+1}$, and the earlier audit events, the remark and `COMPLAINTS.md`'s description of a
    four-horn block record the withdrawn reading. Checked after the rewrite: the block $X_0$ is a
    ball with two handles, so $\pi_1(Y_0)=F_2$, and the complementary piece $Z$ of printed p. 171
    adjoins two free generators per handle, so $\pi_1(Y_n)=F_{2^{n+1}}$; the annulus loop of one
    handle represents a single commutator, the two meridians of that handle's pair being the free
    generators of the copy of $Z$; the bonding maps are injective because each generator goes to a
    nontrivial reduced word in its own rank-two free factor and a free product of injections is
    injective; and the doubled system $F_{2^{n+1}}\to F_{2^{n+2}}$ is the classical system at
    $n+1$, so the direct limit — a direct limit being unchanged on a cofinal subsystem — is the
    group of Example 2B.2 itself. The consequence is stated on the card: doubling the block does not
    change the complement group or its perfectness, and it does not change the homology, so the
    doubled sphere is not distinguished from the classical one by $\pi_1$ or $H_*$. The acyclicity
    of each complementary domain is Proposition 2B.1(b), printed p. 169, and the ball property is
    the uniform-convergence argument of printed pp. 170--172, which uses nothing about the number of
    handles. Not claimed: a published analysis of the doubled block, none having been located.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170, a second check on the figure reading, since it is the one judgment this card's
    repair rests on and three independent readers of the swarm verified the rank $4^n$ without
    reading the figure, saying so explicitly. The wording of the exercise settles it: it asks what
    happens when "the number of handles in the basic building block ... is doubled", and the basic
    building block of Example 2B.2 is a solid torus, which Hatcher introduces at printed p. 170 as a
    ball with one handle attached. Doubling the number of its handles gives two, not four, and the
    figure draws two, one at each end, each with its own pair of horns and its own dashed short
    handle. The reading of four horns on a single handle therefore contradicts the exercise's own
    sentence, and the rank is $2^{n+1}$. Checked again at the figure rendered at 600 dpi from PDF page
    186 of `tmp/sources/hatcher-2002-algebraic-topology.pdf`, and against Hatcher's drawing of the
    single handle on printed p. 171 (PDF page 180). What the three readers verified is the
    conditional statement, that four horns per handle would give $F_{4^n}$, $4^{n+1}$ and a perfect
    limit; that conditional is true and is not the exercise's block.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170, referee read of this card's own part, the model read off Hatcher's figure. The
    figure was read again from the book itself: `tmp/sources` no longer holds
    `hatcher-2002-algebraic-topology.pdf`, only the text version, so the book was taken from the
    author's own file at `https://pi.math.cornell.edu/~hatcher/AT/AT.pdf`, whose pagination is the
    one cited here (PDF page 186 carries printed p. 177 and the text of Exercise 7; PDF page 180
    carries printed p. 171), and both pages were rendered at 200 dpi. The figure on printed p. 177
    draws a ball with **two** handles, one at each end, each drawn the way the single handle of
    printed p. 171 is drawn --- an arch, a pair of horns hooked through one another beneath it, and
    a short handle as a dashed arc --- so the doubled basic block is a ball with two handles and the
    reading of four horns on one handle is not what the figure shows. The exercise's own sentence
    agrees: it doubles "the number of handles in the basic building block", and Hatcher's block
    $X_0$ is a solid torus, "$\pi_1(Y_0)\approx\ZZ$ since $X_0$ is a solid torus", with "$X_n$ is a
    ball $B_n$ with $2^n$ handles attached" on the same page. Stage $n$ therefore has $2^{n+1}$
    handles and $\pi_1(Y_n)\cong F_{2^{n+1}}$. Read with it and confirmed: a loop generating
    $\pi_1(A)$ "represents the commutator $[\alpha_1,\alpha_2]$", so an old meridian maps to one
    commutator and not a product of commutators; $Y_{n+1}$ is $Y_n$ with one copy of $Z$ adjoined
    per old handle, so distinct handles contribute disjoint free factors and no relation between
    them; and Hatcher's own sentence is that the inclusion induces an injection "as the infinite
    cyclic subgroup generated by $[\alpha_1,\alpha_2]$", which is the injectivity the card's step
    `s4` generalises. The comparison is right: the doubled system
    $F_2\hookrightarrow F_4\hookrightarrow F_8\hookrightarrow\cdots$ is the classical
    $\ZZ\hookrightarrow F_2\hookrightarrow F_4\hookrightarrow\cdots$ begun one stage later, and a
    direct limit is unchanged on a cofinal subsystem, so the complement group, its perfectness and
    the reduced homology are those of the classical horned sphere. Not claimed: a published analysis
    of the doubled block, none located.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Locator repair, no mathematics: no page number remains in the live text. The doubled block's figure is
    "the figure of Exercise 2.B.7", the undoubled construction is "Example 2B.2 and the construction that
    follows it", the handle computation and the injectivity argument are "in Example 2B.2", Riebe's thesis is
    cited by its Figure 1 and by what its later sections and abstract establish, Bredon's horned disk by its
    Chapter IV with Figure IV-9, and the Math 538 file by the sections of its notes. The sentence that dated
    the typed notes to an opening page now names their subject, the Borsuk--Ulam theorem of §3.2. No step,
    rank, or source obligation changed: the doubled block is still marked the card's own, and the 2026-11-19
    withdrawal of the four-horn reading stands. The dated events above keep their text, page references
    included, as QUAL-11 requires. `qualc.authoring check` passes.
---

::: {.problem}
Analyze what happens when the number of handles in the basic building block for the Alexander horned sphere is doubled, as in the figure at the right.
:::

::: {.solution}
The figure printed with Exercise 2.B.7 doubles the basic building block, and the wording of the exercise says what that means: the block of Example 2B.2 is a solid torus, a ball with **one** handle, and doubling the number of its handles gives a ball with **two**. The figure draws exactly that — two handles, one at each end of the ball, each of them shown the way Hatcher draws his one, a pair of horns hooked through one another together with a short handle, the dashed arc at that end. Thereafter the construction is Hatcher's word for word, one decomposition per handle: each handle is written as a pair of horns and a short handle, the short handle is deleted, and the number of handles doubles. Stage $n$ therefore carries $2^{n+1}$ handles rather than $2^n$, the free groups grow as $F_2\subset F_4\subset F_8\subset\cdots$, and the complement of the limiting sphere has the same fundamental group as the complement of the Alexander horned sphere, the doubled system being the classical one begun one stage later.

::: pf

::: {.pf-step}
After $n$ stages the compact set $X_n$ is a ball $B_n$ with $2^{n+1}$ handles, and the complement $Y_n$ of $X_n$ has
$$\pi_1(Y_n)\cong F_{2^{n+1}}.$$

::: pf-proof
The argument is Hatcher's, from Example 2B.2 and the construction that follows it, with the initial handle count doubled. The block $X_0$ is a ball with two handles, so $\pi_1(Y_0)$ is free on the two meridians of those handles, $F_2$. At each stage every old handle is decomposed as a pair of horns and a short handle and the short handle is deleted; each handle is replaced by two, so the count doubles, $2,4,8,\ldots$, and stage $n$ has $2^{n+1}$ handles. In the complement, the replacement of one handle adjoins a copy of the piece $Z$ of Hatcher's page 171, a ball with two straight tubes removed, along an annulus; van Kampen's theorem applies to the copies one at a time, since their attaching annuli are disjoint, and each copy contributes two free generators, the meridians of its two new handles, so the free rank doubles at each stage. No relation between different handles is introduced, the pieces being disjoint.
:::

:::

::: {.pf-step #s3}
For one handle of the doubled block the old meridian $a$ goes to the single commutator $[a_1,a_2]$ of the two new meridians, not to a product of commutators.

::: pf-proof
The argument is Hatcher's computation in Example 2B.2, applied to one handle. There the loop $\alpha$ generating the fundamental group of the attaching annulus $A$ of the deleted short handle is homotopic, in the closure of the new complement piece $Z$, to the boundary of the disk removed from a torus adjoined to $Z$, and that boundary is in turn homotopic to the commutator of the meridian and longitude circles of that torus; the two meridians of $Z$ are the two new handles, so $\alpha$ represents $[a_1,a_2]$, and van Kampen's theorem identifies the old generator $a$ with it. The word is a single commutator because one handle is replaced by one pair of horns: the figure of Exercise 2.B.7 gives each of the two handles its own pair, at its own end of the ball. A product of commutators would arise only from an old handle whose meridian bounded a punctured surface of genus two, which is not the block the exercise draws; the card read the figure as four horns on one handle until 2026-11-19, and that reading is withdrawn.
:::

:::

::: {.pf-step #s4}
Every bonding map
$$\pi_1(Y_n)\longrightarrow\pi_1(Y_{n+1})$$
is injective.

::: pf-proof
The argument is Hatcher's injectivity argument in Example 2B.2, run once per handle. The group $F_{2^{n+2}}$ is the free product of $2^{n+1}$ free groups of rank two, one pair of meridians for each old handle, and on each cyclic free factor generated by an old meridian the map sends the generator to the commutator $[a_1,a_2]$, a nontrivial reduced word of length four in the corresponding rank-two factor. A homomorphism $\ZZ\to F_2$ carrying $1$ to a nontrivial element is injective, since free groups are torsion-free, and a free product of injective homomorphisms is injective; so the bonding map is injective. The amalgamated-product description of the two steps above gives the same conclusion, the map of the annulus group into $\pi_1(Y_n)$ being onto a free factor and the map into $F_2$ being injective.
:::

:::

::: {.pf-step}
The exterior group is the increasing union
$$
\pi_1(\RR^3-B)\cong
\varinjlim\left(
F_2\hookrightarrow F_4\hookrightarrow F_8\hookrightarrow\cdots
\right),
$$
which is the group of Example 2B.2 — the doubled system at stage $n$ is the classical system at stage $n+1$ — and it is nontrivial with trivial abelianization.

::: pf-proof
As in Hatcher's construction the horned ball $B$ is the intersection of the nested compact sets and its complement is the increasing union of the $Y_n$, and every loop and every nullhomotopy has compact image and so lies in some finite stage; hence $\pi_1(\RR^3-B)$ is the direct limit of the $\pi_1(Y_n)$ over injective bonding maps, and the class of any meridian survives, so the group is nontrivial.

For the comparison with the classical sphere: in both constructions the bonding map carries each generator to the commutator of the two generators of its own block, so the doubled system is $F_{2^{n+1}}\to F_{2^{n+2}}$, which is the classical system $F_{2^m}\to F_{2^{m+1}}$ at $m=n+1$. A direct limit is unchanged on passing to a cofinal subsystem, so the two limits are the same group: doubling the block does not change the complement group, it only begins the same sequence one stage later.

On abelianization each bonding map sends every generator to the class of a commutator, which is zero, so every class dies at the next stage; the abelianization of the direct limit is the direct limit of the abelianizations, hence zero. The group is therefore perfect.
:::

:::

::: {.pf-step}
The reduced homology of the exterior is zero, as for the classical horned sphere.

::: pf-proof
The limiting sphere $S=\partial B$ is an embedded $2$-sphere in $S^3$, so Proposition 2B.1(b), gives $\widetilde H_0(S^3-S)=\ZZ$ and $\widetilde H_i(S^3-S)=0$ for $i\geq1$; the two complementary domains are the two path components, each nonempty and connected, so each is acyclic. The exterior, the unbounded one, is the domain whose fundamental group was just computed, and its $H_1$ vanishes again by the perfectness of that group. This is the same statement as for the classical sphere, and it is what makes the two indistinguishable by homology.
:::

:::

::: {.pf-step}
The limiting compact set is still a topological $3$-ball: the shrinking-horn homeomorphisms of Hatcher's construction converge uniformly, now with two handles in the base block and each handle replaced by two horns at every stage. Thus the doubled construction again produces a wild $2$-sphere.

::: pf-proof
The argument is Hatcher's, from Example 2B.2 and what follows it, and uses nothing about the number of handles: $B_n$ is obtained from $B_{n-1}$ by attaching $2^{n+1}$ horns, there are homeomorphisms $h_n:B_{n-1}\to B_n$ that are the identity outside a small neighbourhood of $B_n-B_{n-1}$, the composition $h_n\cdots h_1$ converges uniformly because the diameters of the moved sets are summable, the limit $f$ is one-to-one off a Cantor set carried into the intersection of all the handles, and by compactness $f$ is a homeomorphism onto its image, a ball whose boundary is the limiting sphere.
:::

:::

:::

:::

::: {.remark title="Source"}
Hatcher, *Algebraic Topology* (2002), read in `tmp/sources/hatcher-2002-algebraic-topology.md`: Example 2B.2 and the construction that follows it, the decreasing sequence $X_n$, the balls $B_n$ with $2^n$ handles, the limit homeomorphism, and the van Kampen computation of $\pi_1(\RR^3-B)$ as the ascending union of the $\pi_1(Y_n)$ with the attaching loop a commutator. The exercise is Exercise 7 of §2.B, with the figure of the doubled building block beside it; the doubled-handle case is that computation with two handles in the base block, each decomposed in the standard way and contributing one commutator.

A published candidate was obtained and read, and it is a different sphere: N. W. Riebe, *The Fundamental Groups of the Complements of Some Solid Horned Spheres* (MS thesis, Utah State University, 1968, DOI 10.26076/c3c1-48f0), read in the Internet Archive's copy of the publisher's file and retained as `tmp/sources/riebe-1968-horned-spheres.pdf` (34 pages; the body pages carry no text layer and were read as images at 260--300 dpi). Its sphere of order 4 is built from four interlocking loops, drawn in its Figure 1, and the relations for the complement of that sphere reduce there to $x_\gamma=[x_{\gamma_1}x_{\gamma_2},\,x_{\gamma_3}x_{\gamma_4}]$, a commutator of two products of loops, where its classical case gives the single commutator $[x_{\alpha_1},x_{\alpha_2}]$. The figure of Exercise 2.B.7 shows a ball with two handles, each with its own pair of horns hooked through one another; each handle's attaching word is the single commutator $[a_1,a_2]$, the word step [](#s3){.pf-ref} uses, and the two words are different reduced words. The card read the figure as four horns on a single handle until 2026-11-19; that reading, the word $[a_1,a_2][a_3,a_4]$ it produced, and the rank $4^n$ that followed from it are withdrawn in the event of that date. Since the two words are different reduced words, the thesis analyses a different embedding and is not cited as the source of this exercise. What it proves for its own sphere is that presentation, and, from its later sections and its abstract, that the groups $G^k$, $k\ge2$, are free of countably infinite rank, so that its $M_2$, $M_3$ and $M_4$ are not distinguished by fundamental groups.

No published analysis of the doubled block was read in full, and the doubling is not worked out in any source read: Hatcher's own text and errata carry only the printed construction for the undoubled block; Bredon, *Topology and Geometry*, in its Chapter IV with Figure IV-9, describes the Alexander horned disk and refers to Rushing for details, without the doubled variant, and was read in the text layer of `tmp/sources/bredon-topology-and-geometry.pdf`, which has no checked-in text version; Alexander (1924) and Bing (1953), the retained papers on the horned sphere, treat the undoubled construction; and the retained solution sets do not solve this exercise --- Sam's has no §2.B section at all, Li's holds 2.B.10 and 2.B.11 only, DeMason's 2.B.1, 2.B.2 and 2.B.8, and Poulsen's 2.B.10; the Stanford Math 215C sets held here are Solution Sets 2--4, which hold §3.2 exercises 1, 2, 11 and 15 with §3.B exercises 1 and 3 (Set 2), §3.3 exercises 9--11 (Set 3), and §3.3 exercises 21, 22 and 24 with M&T 8.2, 8.5, 8.6 and 9.1 (Set 4), and no §2.B exercise; the UCR Math 205B help file has no §2.B exercise, and `tmp/sources/hatcher-math538-homework4-solutions.pdf` is not a solution set for these sections: it is a 19-page image-only scan whose text version is `tmp/sources/hatcher-math538-homework4-solutions.md`, holding typed notes on the Borsuk--Ulam theorem in §3.2 and handwritten Problem Sets 3 and 4 on §3.1--§3.2; it reaches no §2.B exercise. The analysis above is therefore the card's own, checked against Hatcher's printed construction. The doubled block is named as the card's own argument: no published proof of it has been found, and it is recorded as the card's own in `COMPLAINTS.md` item 11 rather than described as a published solution. That record is what the card owes, not an acceptance of the part from a source.
:::
