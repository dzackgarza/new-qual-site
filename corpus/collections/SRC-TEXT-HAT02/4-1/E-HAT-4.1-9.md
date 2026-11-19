---


schema: qual/card@1
id: E-HAT-4.1-9
kind: problem
title: "Extending the long exact sequence to $\\pi_0$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    #161, the state of the record, so that the second clause of the acceptance ("no note on the card
    says a half is open") can be read off the audit rather than found by searching it. Six events
    assert openness, each as the finding of its own day: 2026-11-14, "Withdraws the two counterexamples
    added earlier today" (the question open at $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$); 2026-11-14,
    "Three statements were wrong and are repaired" (a set-valued five-lemma for the triple not proved
    on the card); 2026-11-16 third pass, "The withdrawal stands at the two $\pi_1$ pointed-set
    windows" and "Printed part (b) remains unproved at the two $\pi_1$ pointed-set windows"; 2026-11-16
    third pass continued, "Open, and stated as open: both directions at those two $\pi_1$ pointed-set
    windows"; 2026-11-16 fourth pass, "The two windows centred at the pointed sets
    $\pi_1(A,B,x_0)$ and $\pi_1(X,B,x_0)$ remain unproved as claims"; and 2026-11-16 fifth and sixth
    passes, "their surjectivity halves are not proved" and "The surjectivity halves remain unproved".
    Each is superseded, and the pairs are: the two $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$ windows by the
    2026-11-14 event beginning "The printed (a) is now stated as proved at both set-valued terms",
    whose certificate is the `lean-categories` declarations; the two $\pi_1$ windows of the triple by
    the three events of 2026-11-16 at the head of this list, which prove the two surjectivity halves
    by explicit homotopies, prove full injectivity at both windows, and withdraw the sentence "The
    surjectivity halves remain unproved"; and the remaining caution in the fifth- and sixth-pass
    events by the same three. This date's events then add what those did not: exactness at the three
    degree-one terms, the all-basepoints clause as a stated hypothesis with the example that makes it
    necessary, the published sources, and the end-to-end review. No event of this date, and none of
    the three 2026-11-16 events at the head of the list, asserts any half of the five-lemma or any
    instance of exactness to be open. The earlier six stand as the record of their days and are not
    edited (QUAL-11).
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    #161. The card now checks its two parts against each other in the one case where they overlap.
    With $B=\{x_0\}$ and $D=\{y_0\}$ the triple sequence is the pair sequence of $(X,A)$ and
    $\pi_0(A,B,x_0)=\pi_0(A,x_0)$, so part (b) is part (a) there; its four set-valued windows are the
    windows of part (a) centred at $\pi_2(X,x_0)$, $\pi_2(X,A,x_0)$, $\pi_1(A,x_0)$ and
    $\pi_1(X,x_0)$, and the two hypotheses agree, "bijective at every basepoint of $B$" becoming
    "bijective at $x_0$". The windows part (a) has beyond those exist only in that degenerate case,
    where the sequence continues by the two steps to $\pi_0(X,x_0)$ that Hatcher notes after the
    triple display and then by the terminal term of part (a); the general triple has no such
    continuation, which is the card's example. The four-window inventory of part (b), repaired in the
    earlier passes of this date, is unchanged and is consistent with this. Checked against Hatcher's
    display and the sentence after it on printed p. 344 and the exercise on printed p. 358. Not
    checked: no new source, and the Lean declarations were not re-elaborated.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    #161. The Brown paragraph of the remark was read line by line against the text version and now
    carries the passage that matters most for this card's claim. Verified as stated: 4.9(a), printed
    p. 121, concludes that $f:\pi_0F\to\pi_0F'$ is surjective when $h:H\{v\}\to H'\{v'\}$, and
    $g:\pi_0G\to\pi_0G'$ are surjective and $h:\pi_0H\to\pi_0H'$ is injective; 4.9(b) concludes that
    $f$ is injective on $\ker(i:\pi_0F\to\pi_0G)$ when $h:H\{v\}\to H'\{v'\}$ is injective and
    $g:G\{x\}\to G'\{x'\}$ is surjective; and Corollary 4.11, printed p. 123, forces $f:F\to F'$ to be
    an equivalence when $h$ and $g$ are, its proof applying 4.9 to get $\pi_0F\cong\pi_0F'$ and then
    "the ordinary 5-lemma for groups" to diagram 4.8 for the vertex groups. Added: Brown's own remark
    after 4.9 and his Example 4.10, printed p. 122, which show that the groupoid analogue is strictly
    weaker --- the hypotheses of 4.9(b) do not make $f:\pi_0F\to\pi_0F'$ injective even when
    $g:\pi_0G\to\pi_0G'$ is injective --- so the groupoid statement cannot stand in for the
    space-level one at the pointed-set terms. Not changed: no argument on the card uses Brown.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    #161. The Lean caveat made precise, so that a later pass does not have to rediscover it. The two
    declarations this card links were read at the pinned commit `9b8b85840c` and their signatures
    match what the remark says of them: `relativePiOne_map_bijective` takes $\pi_0(A)\to\pi_0(B)$,
    $\pi_1(X,a)\to\pi_1(Y,fa)$ and $\pi_1(A,a)\to\pi_1(B,fa)$ bijective for every $a\in A$ together
    with $\pi_0(X)\to\pi_0(Y)$ bijective, and concludes $\pi_1(X,A,x_0)\to\pi_1(Y,B,y_0)$ bijective;
    `zerothHomotopySubtypeMap_bijective` is the $\pi_0(A,x_0)$ term, with the vertical maps at
    $\pi_1(X,A,a)$, at $\pi_1(X,a)$ for every $a$, at $\pi_0(X)$ and at $\pi_0(X,A,x_0)$ as its four.
    Re-elaboration is not possible in this image: no repository under
    `$HOME/sage-image/rootfs/repos` has a built Mathlib (none has
    `.lake/build/lib/lean/Mathlib`), so a Mathlib-importing file cannot be checked there, and the
    host toolchain at `/opt` is not the pinned baseline and may not be cited as one. What would
    settle it is a checkout of `lean-categories` at the pinned commit with its pinned Mathlib built;
    the corpus gate's link check already resolves the declaration URL at that commit.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Full read-through of the card after this date's repairs, against Hatcher's printed pp. 343--345
    and the exercise on printed p. 358. Re-read and accepted: part (a)'s chases at the five group
    windows, the four surrounding maps recorded for each set-valued term, the two $\pi_1$-centred
    windows of part (a) with the non-group step replaced by the exactness assertion at the centre's
    target, Claims 1 and 2, and, in part (b), the three exactness arguments at $n=1$ with their
    triple-homotopy checks, the example showing the sequence stops at $\pi_0(A,B,x_0)$, the four
    set-valued windows' five-lemma, and the hypothesis paragraph with the example that makes the
    clause necessary. The statement is the printed one with the errata's $i_*$, and part (b) is read
    with part (a)'s "for all choices of $x_0$", which the exercise's "the five lemma" carries.
    Structural change in this commit: the Hardie--Kamps comparison now follows the sentence that
    summarises exactness instead of interrupting the three arguments that establish it. Not verified
    here: the Lean certificate was not re-elaborated, its text having been read at the pinned commit
    and matching what the remark says of it; and no published proof of the exercise was located.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    #161. The card now says where its own steps sit in the published taxonomy, and why the published
    derivation stops short of them. (1) The fibre-coset computation for
    $q:\pi_1(A,x_0)\to\pi_1(A,B,x_0)$ is exactness of type (E2) of Hardie--Kamps, printed p. 5, the
    group $\pi_1(B,x_0)$ acting by left multiplication through $i_*$, stated there as
    $\beta(b)=\beta(b')$ iff $b'=a\cdot b$; that is the form of the lemma proved on the card.
    (2) Their §3.A derives the triple sequence from the three pair sequences and records that the
    derivation gives exactness at every term except $\pi_1(X,B,x_0)$, which has to be proved
    separately (printed pp. 15--16); the card now says why: their Theorem 2.1 assumes exactness of
    type (E3) or (E3*) in the left-hand column, a group-stage condition unavailable at the degree-one
    terms, whereas Hatcher's compression criterion is geometric and covers that term at $n=1$
    without an extra step. Checked: the two passages of the paper (pp. 5 and 15--16, read from the
    Numdam volume's text layer) and the comparison against Hatcher's three paragraphs on printed
    pp. 344--345, which are the card's arguments. Not checked: no published proof of the exercise or
    of a five-lemma at a set-valued term was found, *On exact orbit sequences* remains unobtained,
    and the Lean declarations were not re-elaborated in this pass.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    #161. A published treatment of the triple sequence and of its delicate term was obtained and is
    now cited by printed page: Hardie and Kamps, *Exact sequence interlocking and free homotopy
    theory*, Cahiers de topologie et géométrie différentielle catégoriques 26 (1985) 3--31, open
    access at Numdam (`http://www.numdam.org/item?id=CTGDC_1985__26_1_3_0`). §3.A, printed pp. 15--16,
    derives the exact homotopy sequence of a triple from the three pair sequences by Theorem 2.1 and
    says the derivation gives exactness "except at $\pi_1(X,B,x_0)$ where exactness has to be proved
    separately" --- the term this card proves by the compression criterion, which is also where the
    sequence leaves the group range. §1, printed pp. 4--5, defines the exactness types (E0)--(E4) for
    pointed sets, and (E2) is the fibre-coset structure of this card's coset lemma, the fibres of the
    next map being the orbits of the group action. Read from the Numdam PDF of the volume (30 pages,
    printed = PDF page $+ 1$; the scan's running heads read 4, 5, 15 and 16 on PDF pages 3, 4, 14 and
    15). Not claimed: the paper does not treat the exercise, does not prove a five-lemma at a
    set-valued term, and its Theorem 2.1 is an exactness result; and Heath--Kamps, *On exact orbit
    sequences*, Illinois J. Math. 26 (1982) 149--154, remains unobtained, Project Euclid answering
    automated requests with a bot challenge. The Lean declarations linked below were not
    re-elaborated; their source was read at the pinned commit and matches what the remark says of
    them.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    #161. The Sources remark said that no published source states the exercise. Two do, and both are
    now named by printed page. **tom Dieck, *Algebraic Topology* (EMS, 2008)**, §6.1 Problem 3,
    printed p. 125, states the exact sequence of a pointed triple and adds "The sequence ends with
    $\pi_1(X,A,b)$" --- which is where part (b) says the sequence stops before the extension by
    $\pi_0(A,B,x_0)$. §6.2 Problem 3, printed p. 129, is the five-lemma at the pointed-set end,
    stated for a map of pairs as "a Five Lemma type result", with the surjectivity half and the
    injectivity half separate: the injectivity hypothesis is required "for each $c\in A$" and the
    conclusion holds "for each $a\in A$", which is the restriction to every basepoint that part (b)
    states, now cited there as well. Both are problems: the book states the two facts and proves
    neither, so the remark says the form and the clause are published and no proof is. Checked: the
    two pages in the text version `tmp/sources/tomdieck-algebraic-topology-ranicki.md` and in the
    PDF's own text layer, whose running heads put §6.1 at printed p. 125 and §6.3 at printed p. 129
    (printed = PDF $- 13$ for this copy), so §6.2's problems fall on printed p. 129. Not checked: no
    published *proof* of the exercise was located, the Heath--Kamps paper remaining unobtained; and
    the Lean declarations linked below were not re-elaborated, the `lean-categories` checkout in the
    shared image being at another commit (`064b5cfd`) and containing no
    `LeanCategories/Topology/PairHomotopySequence.lean`, which the corpus gate's link check still
    resolves at the pinned commit.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    #161. Part (b) never stated the hypothesis of its five-lemma: the proof rebases at a point
    $b_0\in B$ other than $x_0$, so it uses the exercise's "for all choices of $x_0$", and the
    single-basepoint form is false. The hypothesis is now stated, and the example that shows the
    clause is necessary is on the card: $X=Y=[0,1]$ with the identity, $A=C=[0,1/8]\cup[3/4,7/8]$,
    $B=\{0,3/4,7/8\}$ and $D=\{0\}\cup[3/4,7/8]$, where the vertical map at $\pi_1(X,B,x_0)$ is three
    points onto two while the four surrounding maps at $x_0$ are $0\to0$, a bijection of one-point
    sets, the identity of two-point sets and a bijection of one-point sets; at $b=3/4\in B$ the
    vertical map at $\pi_1(A,B,b)$ is two points onto one, which is where the hypothesis fails. No
    other claim changes. Checked against Hatcher's printed pp. 343--345 and the exercise on printed
    p. 358, and against the counterexample computations written out above; the four windows' proofs
    are the ones already on the card and were re-read, not re-derived. Not checked: no published
    solution of the exercise was located, and the Lean declarations linked below were not
    re-elaborated.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    #161. Exactness of the triple sequence is now proved at every term rather than cited, and three
    defects of the proof are repaired. (1) The card said the sequence ends at $\pi_0(A,B,x_0)$ and
    that exactness is Theorem 4.3 printed p. 344, but exactness at $\pi_1(A,B,x_0)$ and at
    $\pi_1(X,B,x_0)$ is a degree-one statement and no argument for it stood on the card, and
    exactness at $\pi_1(X,A,x_0)$, which the extension by $\pi_0(A,B,x_0)$ adds, was neither stated
    nor proved. Three proofs are now on the card, each the corresponding paragraph of Hatcher's proof
    of Theorem 4.3 at $n=1$, with the homotopies checked to be homotopies of maps of triples: the
    compression criterion gives $\operatorname{im}i_*=\ker j_*$ at $\pi_1(X,B,x_0)$, the tacking of a
    homotopy of the start point gives $\operatorname{im}j_*=\ker\partial$ at $\pi_1(X,A,x_0)$, and
    Hatcher's tacking of $g$ onto $f$ gives $\operatorname{im}\partial=\ker i_*$ at
    $\pi_1(A,B,x_0)$. That proof's exactness paragraphs run over printed pp. 344--345 and the
    compression criterion is on printed pp. 343--344, so the citation of "Theorem 4.3 (p. 344)" as
    the whole of the exactness is corrected to pp. 344--345. (2) The coset lemma at the window
    centred at $\pi_2(X,A,x_0)$ passed from $h(x)=h(x')$ to
    $q(\partial(x')\partial(x)^{-1})=1$, which treats $q:\pi_1(A,x_0)\to\pi_1(A,B,x_0)$ as a
    homomorphism; $q$ is a map of pointed sets. The step it needs, that the fibre of $q$ through a
    point is a coset of $\ker q$, is now stated and proved by the boundary of the square, and the
    basepoint $a_0$ of the solution's coset lemma, which occurs nowhere else in the solution, is
    corrected to $x_0$. (3) The inventory justified the absence of a window centred at
    $\pi_1(X,A,x_0)$ by saying "only two terms following it", which would have made it a window; one
    term follows it. The closing paragraph of part (b) now states exactness at every term, and its
    quotient sentence wrote $i'_*\pi_0(B,x_0)$ where the target's subset $i'_*\pi_0(D,y_0)$ is meant.
    The card's solution and remark assert no half of the five-lemma, and no instance of exactness, to
    be open: the dated events in this list that assert it are records of the passes of 2026-11-16,
    and the three events of 2026-11-16 that follow this one, which prove full injectivity at both
    $\pi_1$ windows and withdraw the surjectivity caveat, supersede them, as does this event. Checked against
    Hatcher's printed pp. 343--345 (definitions, compression criterion, Theorem 4.3 and its proof,
    naturality) and the exercise on printed p. 358, in
    `tmp/sources/hatcher-2002-algebraic-topology.md` and in the PDF's own text layer. Not checked: no
    published solution of the exercise was located, and the Lean declarations linked below were not
    re-elaborated in this pass.
- event: source-corrected
  by: kimi
  date: 2026-11-16
  note: >-
    Withdraws only the sentence "The surjectivity halves remain unproved." in the
    2026-11-16 `source-corrected` event headed "#123 reader's report, sixth pass, on
    the fifth-pass event above." Both surjectivity halves at the two $\pi_1$ pointed-set
    windows are proved in the solution: the first lifts a relative $2$-disk and
    concatenates with its boundary, and the second concatenates with a lift of the
    reversed starting edge. The two arguments headed "Surjectivity" show that the maps
    are onto. No proof or earlier event is changed, and no other sentence of that event
    is withdrawn here.
- event: source-corrected
  by: kimi
  date: 2026-11-16
  note: >-
    #123 reader's report after the surjectivity repair. The report accepts both new
    surjectivity arguments and rejects the second window's step $b=\partial\mu$ from
    equality under $\gamma$: the old chase established only a trivial basepoint fibre,
    not full injectivity. That step is removed, and full injectivity at both windows is
    supplied. At $\pi_1(A,B,x_0)$, the valid basepoint-fibre chase is retained and used at
    a new basepoint. If $\gamma(c_0)=\gamma(c_1)$, injectivity at the next term lets the
    representatives be replaced, without changing their classes, so that they start at one
    $b_0\in B$. Their target equality makes the image of the difference loop
    $r_1r_0^{-1}$ a loop in $D$ at $\varphi(b_0)$. The basepoint-fibre chase at $b_0$
    therefore applies; exactness of $(A,B)$ then writes the difference as a $B$-loop,
    which disappears on prepending. This is full injectivity, not merely triviality of the
    fibre at the original $x_0$. At $\pi_1(X,B,x_0)$, a square comparison is made at
    $b_0=r_0(0)$: the target
    boundary is lifted by $\pi_2(X,A,b_0)\to\pi_2(Y,C,\varphi(b_0))$, and the first
    window's full injectivity at $b_0$, not its basepoint-fibre special case, identifies
    the correcting class. Exactness and concatenation with $r_0$ finish the proof. The
    accepted surjectivity constructions are unchanged. Thus both $\pi_1$ vertical maps
    are now proved bijective, and the closing statements no longer cautiously stop at
    trivial basepoint fibres. Checked against Hatcher's relative path and disk definitions
    and the exact pair and triple sequences on printed pp. 343--345 of
    `tmp/sources/hatcher-2002-algebraic-topology.md`. No new published treatment was
    located, and the linked Lean declarations were not re-elaborated.
- event: source-corrected
  by: kimi
  date: 2026-11-16
  note: >-
    #123, sixth pass on part (b): the two requested surjectivity halves are now proved
    by explicit homotopies. Hatcher's path convention is stated first: products traverse
    the first path first. At $\pi_1(A,B,x_0)$, the usual chase gives paths $p,q$ in $C$
    with the same image in $\pi_1(Y,D,y_0)$. Their homotopy $H$ has starting edge
    $\lambda$ in $D$ and is a relative $2$-disk for $(Y,C)$; its boundary is
    $p^{-1}\lambda q$. Surjectivity at $\pi_2(X,A,x_0)$ lifts this disk, and concatenating
    $c$ with the boundary of the lift corrects $p$ to $\lambda q$. A displayed
    start-point-varying homotopy absorbs the initial $D$-path $\lambda$ into the varying start
    point, giving $q$. At $\pi_1(X,B,x_0)$, the usual chase likewise leaves $p,q$ with the
    same image in $\pi_1(Y,C,y_0)$. If $p$ comes from a path based initially at $b_0\in B$,
    reverse the homotopy's starting edge, now in $C$, and lift it by surjectivity of
    $\pi_1(A,B,b_0)\to\pi_1(C,D,\varphi(b_0))$; this is where the hypothesis at every
    basepoint is essential. Concatenating the lift with the source path gives the required
    preimage. The old statements that these two surjectivity halves are open are corrected.
    Checked against Hatcher's cube and disk definitions on printed p. 343 and the exact
    triple sequence and its naturality on pp. 344--345 of
    `tmp/sources/hatcher-2002-algebraic-topology.md`. Not changed: the earlier fibre
    calculations and the Lean declarations, which were not re-elaborated in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A local reader found the pair sequence's two remaining windows mislabelled and left unproved,
    and part (b)'s set-valued tail untreated. All three are repaired. (1) The display at the old
    "Which windows these are" paragraph labelled $\pi_2(X,A)\to\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)\to\pi_0(A)$
    as the window centered at $\pi_1(A,x_0)$; it is the window centered at $\pi_1(X,x_0)$, its third
    term. The corrected paragraph gives the whole sequence and both windows, and the window centered
    at $\pi_1(A,x_0)$ is $\pi_2(X)\to\pi_2(X,A)\to\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)$. (2) Both windows
    are now proved. The group chase's step $h(\gamma(c)^{-1}c')=1$ needs a homomorphism out of the
    centre, which these windows lack; the replacement uses exactness at the centre's target instead,
    with the two-sided invertibility of the bijections at the surrounding terms. The only
    non-abstract step is the observation that two loops at $y_0$ with the same class in
    $\pi_1(Y,C,y_0)$ differ by the image of a loop in $C$, read off the boundary of the homotopy
    through paths from $C$ to $y_0$. (3) Part (b) now treats the set-valued tail: it names the two
    windows that exist, centred at $\pi_1(A,B,x_0)$ and $\pi_1(X,B,x_0)$, proves the injectivity half
    at each by the same chase, and states that the surjectivity halves are not established, with the
    reason (the difference of two classes over the same image in $\pi_1(Y,D)$ is a path in $C$
    between interior points, not a class ending at the basepoint). Neither half is asserted without
    proof. Every citation now names its text version: Hatcher in
    `tmp/sources/hatcher-2002-algebraic-topology.md`, Brown already in
    `tmp/sources/brown-1970-fibrations-of-groupoids.md`. Not checked: the Lean declarations the card
    links were not re-elaborated in this pass, and the printed pagination of the 2002 printing is
    quoted from its text version.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher Section 4.1 Exercise 9 and the 2021-06-02 correction; corrected i^* to i_* in the stored statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line. Correct in its two parts. The extension by `pi_0(X,A,x_0) = pi_0(X,x_0) /
    i_* pi_0(A,x_0)` is exact at the tail because the components of `X` mapping to the distinguished
    relative class are precisely those meeting `A`, and the quotient map is onto. (a) The five-lemma in
    degrees `>= 2` is the ordinary one; in the pointed-set tail the argument is the appropriate
    replacement — exactness says that the fiber of the next map over the distinguished element is the
    image of the preceding map — and the hypothesis that the four surrounding maps are bijections *for all
    basepoints* is exactly what allows rebasing at an arbitrary component, which is the one place the
    naive group-theoretic version fails. (b) The triple sequence stops at `pi_0(A,B,x_0)` because there is
    no distinguished element of `pi_0(B)` to feed the next term. No correction was needed.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The printed part (a) is not correct as stated, and the earlier note's claim that "the hypothesis
    that the four surrounding maps are bijections for all basepoints is exactly what allows rebasing"
    does not repair it: rebasing is not available, because the basepoint of the pair $(Y,B)$ must lie
    in $B$ while the component of $B$ whose surjectivity is in question need not meet the image of
    $A$. Counterexample on the card: $X$ the disjoint union of a point $x_0$ and a point $a$ with
    $A=\{x_0,a\}$, $Y$ the disjoint union of a point $y_0$ and the interval $[0,1]$ with
    $B=\{y_0,0,1\}$, and $\varphi(x_0)=y_0$, $\varphi(a)=0$. Then the vertical maps at
    $\pi_1(X,A,x_0)$, $\pi_1(X,x_0)$, $\pi_0(X,x_0)$ and $\pi_0(X,A,x_0)$ are all bijections of
    one-point or two-point sets, while $\pi_0(A,x_0)\to\pi_0(B,y_0)$ is 2 points into 3 and is not
    onto. The card now states the exercise as printed and proves what is true: the five-lemma at
    every term in degrees $\ge1$ (both chases written out), the bijectivity of the vertical at
    $\pi_0(X,A,x_0)$ from those at $\pi_0(A,x_0)$ and $\pi_0(X,x_0)$, and the surjectivity at
    $\pi_0(A,x_0)$ for the components of $B$ lying in the component of $y_0$ in $Y$. Part (b) is
    correct as printed and its example is checked point by point.
- event: source-checked
  by: claude
  date: 2026-11-13
  note: >-
    Read Hatcher's published errata list for *Algebraic Topology*
    (pi.math.cornell.edu/~hatcher/AT/ATerrata.pdf) for this exercise, as #123 asks. The only entry
    bearing on it is "§4.1, page 358, Exercise 9, first line. To avoid an abuse of notation, replace
    $\pi_0(A,x_0)$ by $i_*(\pi_0(A,x_0))$. (The previous version of this correction mistakenly said
    $i^*$ instead of the correct $i_*$.)" That is a notational correction of the displayed term and
    changes no hypothesis. The current online text of the book (AT.pdf, printed p. 358) carries it
    and is otherwise identical to the 2002 printing: part (a) still concludes that one of the maps
    is a bijection "if the four surrounding maps are bijections for all choices of $x_0$". So the
    errata supplies no corrected statement and does not repair the failure at the $\pi_0(A,x_0)$
    term; the counterexample on this card survives the corrected notation, since
    $i_*\pi_0(A,x_0)$ is the whole of $\pi_0(X,x_0)$ in it. The repaired statement proved above
    therefore stands as the card's own. Not established here: a published proof of that repaired
    statement. Searched without result in the retained sets (Sam, Li, DeMason, Poulsen, Stanford
    Math 215C Solution Sets 1--5, the UCR Math 205B help file, May's *Concise Course* §4, Maxim's
    Math 752 notes) and in Hatcher's text and errata.
- event: source-corrected
  by: claude
  date: 2026-11-14
  note: >-
    Withdraws the counterexample recorded on 2026-11-07, which does not satisfy the hypothesis it is
    offered against. That hypothesis is that the four surrounding maps are bijections for every
    choice of basepoint, and the basepoints admissible for the pair $(X,A,x_0)$ are the points of
    $A$. In the withdrawn example $X=\{x_0\}\sqcup\{a\}$ is discrete with $A=X$, while
    $Y=\{y_0\}\sqcup[0,1]$ and $B=\{y_0,0,1\}$; at the basepoint $a\in A$ the vertical map at
    $\pi_1(X,A,a)$ is one point into two, since the only path from $A$ to $a$ in the discrete $X$ is
    the constant one, while $\pi_1(Y,B,\varphi(a))=\pi_1(Y,B,0)$ contains the classes of the constant
    path at $0$ and of a path from $1$ to $0$, both starting in $B$. The example therefore fails the
    hypothesis at a basepoint in $A$, exactly as the brief for #123 asked to be checked, and it is
    withdrawn. It is replaced by two examples that do satisfy the hypothesis at every basepoint: for
    the term $\pi_1(X,A,x_0)$, $X=\RR\sqcup\RR$ with $A=\{1\}\cup\{2\}$ one point in each copy,
    $Y=\RR$ with $B=\{0,3\}$, and $\varphi$ equal to $0$ on the first copy and $3$ on the second; and
    for the term $\pi_0(A,x_0)$, $X=Y=\RR$ with $A=(-1,0]\cup(2,3)$, $B=(-1,1)$ and the piecewise map
    that is the identity on $(-\infty,0]$, $0$ on $[0,2]$ and $t-2$ on $[2,\infty)$. In each case the
    four surrounding maps are computed on the card, at every basepoint, and the conclusion fails.
- event: source-corrected
  by: claude
  date: 2026-11-14
  note: >-
    Corrects the claim, carried since 2026-11-07, that the printed five-lemma holds "at every term in
    degrees $\ge1$". The group chase on the card is a chase of five group terms, and in the pair
    sequence the windows of five group terms are exactly those centered at a term of degree $\ge2$;
    the window centered at the pointed set $\pi_1(X,A,x_0)$ is not one of them, and the first new
    example shows that the printed claim is false there too. So the printed (a) fails at two terms,
    $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$, and the card now says so. What survives is stated as Claim 1
    ($\pi_0(X,A,x_0)$ from $\pi_0(A,x_0)$ and $\pi_0(X,x_0)$), Claim 2 (unchanged), and a new Claim 3:
    surjectivity at $\pi_0(A,x_0)$ is forced by the hypothesis, using $\pi_1(X,A,x)$ onto at the
    relevant basepoints and $\pi_0(X,A,x_0)$ injective, so the failure at $\pi_0(A,x_0)$ is
    injectivity only and not, as the withdrawn example suggested, surjectivity. The windows centered
    at $\pi_1(A,x_0)$ and $\pi_1(X,x_0)$ are recorded on the card as not settled there. Part (b) is
    unchanged and still checked as printed.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    Read Brown, *Fibrations of groupoids*, Journal of Algebra 15 (1970) 103--132, in the text
    version `tmp/sources/brown-1970-fibrations-of-groupoids.md`, for the $\pi_0$ five-lemma the #123
    brief names: Theorem 4.9 on printed p. 121, whose (a) gives surjectivity of $f:\pi_0F\to\pi_0F'$
    from surjectivity of $h:H(v)\to H'(v')$ and of $g:\pi_0G\to\pi_0G'$ together with injectivity of
    $h:\pi_0H\to\pi_0H'$, and whose (b) gives injectivity of $f$ on $\ker(\pi_0F\to\pi_0G)$; and
    Corollary 4.11 on printed pp. 122--123, that equivalences $h:H\to H'$ and $g:G\to G'$ force
    $f:F\to F'$ to be an equivalence, hence $f:\pi_0F\to\pi_0F'$ bijective, by 4.9 followed by the
    ordinary five-lemma for groups on diagram 4.8. Cited on the card in a remark for exactly that,
    and not used in the argument: Brown's hypotheses are those of a fibration of groupoids with
    equivalences of the total groupoids and bases, which is stronger than the exercise's "for all
    choices of $x_0$", and the map of pairs $(X,A)\to(Y,B)$ is not a fibration of groupoids. No
    claim is made that Brown's theorem settles Hatcher's exercise. The extracted text of the paper
    writes some symbols as glyph substitutions (it is a scan of the 1970 print); the statements
    above were read against the displayed formulas of 4.9, 4.10 and 4.11, not from the running text
    alone.
- event: source-corrected
  by: claude
  date: 2026-11-14
  note: >-
    Withdraws the two counterexamples added earlier today and the claim they supported, that the
    printed (a) fails at the terms $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$. Both are disputed and neither
    is established. Against the first ($X=\RR\sqcup\RR$ with $A=\{1\}\cup\{2\}$, $Y=\RR$ with
    $B=\{0,3\}$): its vertical map $\pi_0(X)\to\pi_0(Y)$ is two components into one. Against the
    second ($X=Y=\RR$, $A=(-1,0]\cup(2,3)$, $B=(-1,1)$): $\pi_1(X,A,x_0)$ is read as having one class
    per component of $A$ rather than one per point of $A$, and then it is the surrounding map at
    $\pi_1(X,A,x_0)$ that fails rather than the one at $\pi_0(A,x_0)$. The second objection is about
    the definition of $\pi_1$ of a pointed pair, not about an example, so this reading is established
    neither on the card nor in prose: the question goes to a Lean declaration at
    <https://github.com/dzackgarza/lean-categories/issues/156>. The card now states the question as
    open at those two terms and asserts neither direction. The withdrawal of the 2026-11-07 example
    and the reason for it stand unchanged, and Claims 1, 2 and 3 stand: Claim 3 uses only that the
    map at $\pi_1(X,A,x)$ is onto at the relevant basepoints, so it holds under either reading of
    that set. Not claimed: that the printed (a) is correct, or that it is false; not verified: the
    contested reading of $\pi_1(X,A,x_0)$, which is what the issue is for.
- event: source-corrected
  by: claude
  date: 2026-11-14
  note: >-
    The printed (a) is now stated as proved at both set-valued terms, and the card carries the
    certificate. lean-categories#156 is merged at `9b8b85840c`, and `relativePiOne_map_bijective`
    and `zerothHomotopySubtypeMap_bijective` in `LeanCategories/Topology/PairHomotopySequence.lean`
    prove the printed claim at $\pi_1(X,A,x_0)$ and at $\pi_0(A,x_0)$, each from exactly the four
    surrounding maps of its own term, bijective at every basepoint of $A$, with
    $\pi_1(X,A,x_0)$ built as Hatcher's quotient in which the start point moves inside $A$ (printed
    p. 343) — the reading the earlier dispute turned on. Both declarations were re-elaborated here
    on the pinned baseline, Lean 4.33.0 with Mathlib `db584cd6`: exit 0, axioms only `propext`,
    `Classical.choice`, `Quot.sound`, no `sorryAx`. The card now carries the two arguments in the
    required form and Claim 1, and no longer discusses either withdrawn counterexample; Claims 2
    and 3 are dropped with the question they served. The claim that injectivity at
    $\pi_1(X,x_0)$ follows from injectivity at $\pi_1(X,A,x_0)$ is dropped as well: under the
    quotient reading a relative class of a loop at $x_0$ need not be its loop class, so that
    inference is not established. The windows centred at $\pi_1(A,x_0)$ and $\pi_1(X,x_0)$ are not
    treated, and the card says so. Checked against Hatcher (2002), §4.1 Exercise 9 on printed
    p. 358, the errata's $i_*$ correction, and the definition of $\pi_n(X,A,x_0)$ on printed p. 343.
    Not claimed: that the printed (a) holds at $\pi_1(A,x_0)$ or at $\pi_1(X,x_0)$, or that a
    published treatment of the exercise exists.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    Three statements were wrong and are repaired. (1) The remark cited Brown's Corollary 4.11 on
    "printed pp. 122--123"; it is printed on p. 123 only. In the text version
    `tmp/sources/brown-1970-fibrations-of-groupoids.md` the page marker `<!-- PDF pages 21-30 -->`
    stands immediately before it, so 4.11 opens the run of pages beginning at PDF page 21, printed
    p. 123 of Journal of Algebra 15 (1970) 103--132; Theorem 4.9, which the card also cites, precedes
    that marker, on printed p. 121. (2) The last paragraph of part (b) invoked "the analogue of
    Claim 2", a claim the card no longer has — Claims 2 and 3 were dropped in the 2026-11-14 rewrite
    that kept Claim 1 only — and it asserted rather than proved a five-lemma for the ladder of triple
    sequences. It is replaced by what the card establishes and by a statement of what it does not:
    the windows of five group terms (degrees $\ge2$) are the chase of part (a), applied to the triple
    ladder, which is exact by Theorem 4.3 (p. 344) and commutative by naturality (p. 345); no window
    of five group terms is centred at $\pi_1(A,B,x_0)$, $\pi_1(X,B,x_0)$, $\pi_1(X,A,x_0)$ or
    $\pi_0(A,B,x_0)$, the first three being pointed sets and the last the terminal term, at which
    there is no map out and hence no exactness obligation; and a set-valued five-lemma for the triple
    is not proved on this card, its two set-valued statements being the pair sequence's. What is
    proved about the terminal term is the quotient statement Claim 1 rests on, that a bijection
    $\pi_0(A,x_0)\to\pi_0(C,y_0)$ carrying $i_*\pi_0(B,x_0)$ onto $i'_*\pi_0(D,y_0)$ induces a
    bijection $\pi_0(A,B,x_0)\to\pi_0(C,D,y_0)$, since the two are $\pi_0(A,x_0)/i_*\pi_0(B,x_0)$ and
    its image. (3) The paragraph on which windows are group windows now names the pointed sets in
    them, rather than leaving the count implicit. Checked, against a reader's claim that the windows
    centred at $\pi_1(A,x_0)$ and at $\pi_1(X,x_0)$ are windows of groups: they are not. The sequence
    in degrees $1$ and $0$ reads
    $\pi_2(X,A)\to\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)\to\pi_0(A)\to\pi_0(X)\to\pi_0(X,A)\to0$, so the
    window centred at $\pi_1(A,x_0)$ contains $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$ and the one centred
    at $\pi_1(X,x_0)$ contains those two and $\pi_0(X,x_0)$; Hatcher defines $\pi_1(X,A,x_0)$ as a set
    of path classes and states on printed p. 343 that it is in general not a group in any natural way,
    so the group five-lemma does not apply to either window and the card's statement that they are not
    treated stands. Not claimed: a five-lemma at those two windows, in either direction.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, second pass on this card. The text of the `source-corrected` event of this
    date above is restored from commit 6db04ca88a, which rewrote it in place after commit 857554a9b3 had
    pushed it, with no event of its own; the restored sentences stand as they were written and are
    corrected here. (1) The restored text says the chase's step "$h(\gamma(c)^{-1}c')=1$ needs a
    homomorphism out of the centre, which these windows lack". That is false of the first of the two
    windows, the one centred at $\pi_1(A,x_0)$: its chase runs exactly as the paragraph on
    $\pi_1(A,x_0)$ below has it, and it goes through. The step that needs a homomorphism is at the
    **second** window, where the map out of the centre's target is $k'=j':\pi_1(Y,y_0)\to\pi_1(Y,B,y_0)$,
    a map of pointed sets. The card now names $k'$ there; it had called that map $h'$, which is
    $i'_*:\pi_1(B,y_0)\to\pi_1(Y,y_0)$, and had therefore used one letter for two maps. (2) The same
    restored paragraph said of part (b) that it "names the two windows that exist": there are three
    windows of the triple ladder that contain a pointed set, and the one centred at $\pi_2(X,A,x_0)$ ---
    $\pi_2(A,B)\to\pi_2(X,B)\to\pi_2(X,A)\to\pi_1(A,B)\to\pi_1(X,B)$ --- was missing from the card. It is
    now stated and its chase is written out. (3) The restored text, and the card, said the injectivity
    half is proved at each of those windows. It is not: the chase shows that a class with $\gamma(c)=1$
    is trivial, which is triviality of the fibre over the base point, whereas injectivity of a map of
    pointed sets says that two classes with the same image are equal, and the fix-up that would give it
    multiplies by the difference of two such classes, which a pointed set does not supply. The card now
    says that, for all three windows and in the remark. (4) The sentence "Every one of the six windows
    is therefore settled on this card, and none of them by the group chase alone" contradicted the
    paragraph after it; the window centred at $\pi_2(X,A,x_0)$ is settled by the chase, the other five
    are not, and the sentence now says so. (5) The term $\pi_0(X,x_0)$ was said to be settled "by
    Claim 1", and Claim 1 was the statement about $\pi_0(X,A,x_0)$; bijectivity at $\pi_0(X,x_0)$ from
    its own four surrounding maps is now proved, as the new Claim 1, and the old statement is Claim 2.
    (6) Part (a) denoted the target pair $(Y,C,y_0)$ while the problem and the rest of the card use
    $(Y,B,y_0)$; part (a) now uses $(Y,B,y_0)$ throughout, and $C$, $D$ appear only in part (b), for the
    triple. Also repaired: the surjectivity step at $\pi_1(X,x_0)$ wrote the correction of $\delta(c)$
    to $c'$ as $\delta(c)^{-1}c'$ and multiplied on the right, which fails under Hatcher's convention,
    the first path traversed first; the correction is now $\omega=c'\delta(c)^{-1}$ and $c''=h(a)\cdot c$,
    with the convention stated, and the square at $\pi_1(Y,B,y_0)$ now reads $[a][b]^{-1}=[\lambda]$
    with $\lambda$ a loop in $B$, not $a^{-1}b$. Unchanged: the statement as printed on p. 358 with the
    errata's $i_*$, part (b)'s example that the triple sequence stops at $\pi_0(A,B,x_0)$, part (a)'s
    two set-valued arguments with their certificate on `lean-categories` main, and the citation of
    Brown's Theorem 4.9 and Corollary 4.11 as a related and unused statement. Not verified in this
    pass: the Lean declarations linked below, which were not re-elaborated.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, third pass on this card. (1) The vertical map $\varepsilon$ at the window
    centred at $\pi_1(A,x_0)$ was still written $\pi_1(X,A)\to\pi_1(Y,C)$; it is
    $\pi_1(X,A)\to\pi_1(Y,B)$, and with that correction the statement that $C$ and $D$ occur only in
    part (b) is true. (2) The description of the four surrounding maps of the window centred at
    $\pi_0(X,x_0)$ omitted the vertical map at $\pi_1(X,A,x_0)$ and substituted the horizontal
    terminal map; it now lists all four, the vertical maps at $\pi_1(X,A,x_0)$, $\pi_0(A,x_0)$,
    $\pi_0(X,A,x_0)$ and at the terminal $0$. (3) The blanket claim that triviality of the fibre is not
    injectivity at all three set-valued windows of the triple is false at the window centred at
    $\pi_2(X,A,x_0)$: there the centre and its vertical map are a group and a homomorphism, so trivial
    kernel is precisely injectivity, and the card now proves and claims it, saying that only the
    surjectivity half is open there. The withdrawal stands at the two $\pi_1$ pointed-set windows.
    (4) The step $c=gf(a)=1$ was attributed to exactness at $\pi_2(A,B)$; it is exactness at
    $\pi_2(X,B)$, where $\operatorname{im}f=\ker g$. (5) Printed part (b) remains unproved at the two
    $\pi_1$ pointed-set windows and at the surjectivity half of the $\pi_2(X,A)$ window; the card and
    the remark now say exactly that, and no claim of a complete proof of part (b) is made. Unchanged:
    part (a)'s arguments, the example showing that the triple sequence stops at $\pi_0(A,B,x_0)$, and
    the Brown citation. The Lean declarations linked on the card were not re-elaborated in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, third pass (continued): the coset lemma, and part (b) at the
    $\pi_2(X,A,x_0)$ window. The `source-corrected` event of this date says the surjectivity half at
    that window is open. It is not. The boundary map $h:\pi_2(X,A)\to\pi_1(A,B)$ is not a
    homomorphism into a group, but it factors as $q\circ\partial$: the map
    $\partial:\pi_2(X,A)\to\pi_1(A,a_0)$ is the boundary map of the pair $(X,A)$, a homomorphism, and
    $q:\pi_1(A,a_0)\to\pi_1(A,B,a_0)$ has kernel the image of $\pi_1(B,a_0)$. Hence
    $h(x)=h(x')$ exactly when $x'x^{-1}\in\ker h=\operatorname{im}(\pi_2(X,B)\to\pi_2(X,A))$; the
    fibres of $h$ are cosets of that image, and the same holds for $h'$ and the triple $(Y,C,D)$.
    The card now proves this lemma and runs the chase: for $c'\in\pi_2(Y,C)$ choose $d_0$ with
    $\delta(d_0)=h'(c')$, use exactness at $\pi_1(C,D)$ and at $\pi_1(A,B)$ to write
    $d_0=h(a)$, then $h'(\gamma(a))=h'(c')$, so $c'=k\gamma(a)$ with $k=g'(b')=\gamma(g(b))$, and
    $c'=\gamma(g(b)a)$. So the window centred at $\pi_2(X,A,x_0)$ is proved in both directions. The
    two $\pi_1$ pointed-set windows are unchanged: the chase there gives only triviality of the fibre
    over the base point, and neither direction of the exercise's claim is proved. The card, its
    remark and COMPLAINTS.md say that. Nothing else changes; the Lean declarations were not
    re-elaborated.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, fourth pass on part (b): the set-valued tail has four windows,
    not three, and the missing one is proved. The window centred at $\pi_2(X,B,x_0)$ is
    $\pi_3(X,A)\to\pi_2(A,B)\to\pi_2(X,B)\to\pi_2(X,A)\to\pi_1(A,B)$: it contains the
    pointed set $\pi_1(A,B,x_0)$ at its last term and was not counted, so the inventory
    said three and the exercise's claim at that window was neither proved nor named as
    open. Four of its five terms are groups, and the chase settles both directions there:
    injectivity by the five-lemma chase at the groups, and surjectivity by correcting
    $c'$ by $\gamma(c)^{-1}c'$, which is taken in the group $\pi_2(Y,D)$ and needs
    $h':\pi_2(Y,D)\to\pi_2(Y,C)$ to be a homomorphism, as it is. The inventory, the
    closing paragraph of part (b) and the remark now say four, and both $\pi_2$-centred
    windows are stated as proved in both directions. The two windows centred at the
    pointed sets $\pi_1(A,B,x_0)$ and $\pi_1(X,B,x_0)$ remain unproved as claims, which
    the card states, and no published treatment of the exercise was located in this
    pass either. Checked in this pass: the exactness statements the chase uses, against
    Theorem 4.3 on printed p. 344 of `tmp/sources/hatcher-2002-algebraic-topology.md`,
    and the composition of the maps in the tail of the triple sequence. Not checked: no
    page was read from a rendered copy, and the Lean declarations the card links were
    not re-elaborated.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, fifth pass: the sentence that opens part (b)'s inventory said
    "three windows that contain a pointed set" and the inventory below it then enumerated
    four, the window centred at $\pi_2(X,B,x_0)$ being the fourth. The sentence now says
    four. No mathematics changes, and what part (b) leaves unproved is unchanged and is
    stated where it stands: the two $\pi_1$ pointed-set windows, centred at
    $\pi_1(A,B,x_0)$ and at $\pi_1(X,B,x_0)$, have their injectivity halves proved by the
    chase in the two bullets above (the first does not multiply; the second takes the
    injectivity of the vertical map at $\pi_1(A,B,x_0)$ from the first), and their
    surjectivity halves are not proved. Not claimed: a published treatment of the
    exercise, which has not been located.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, sixth pass, on the fifth-pass event above. Its account of
    the two $\\pi_1$ windows was not true of the card it was committed with: it said
    their injectivity halves were proved by the chase in the two bullets, but each
    bullet established only that $\\gamma(c)=1$ implies $c=1$, triviality of the fibre
    over the basepoint, and not injectivity, which at a map of pointed sets is
    $\\gamma(c_0)=\\gamma(c_1)$ implying $c_0=c_1$; the second bullet then took the
    first window's basepoint-fibre result as the injectivity it needs. The event is a
    dated record and is left as written; the correction is this event. What the card
    now proves is stated by the event at the head of this list: the basepoint-fibre
    chase is retained and applied at a common basepoint reached by prepending a
    $B$-path, which gives full injectivity at both $\\pi_1$ windows, and the two
    bullets are rewritten to carry it. The surjectivity halves remain unproved, and no
    published treatment of the exercise has been located. Not checked: nothing new;
    the two rewritten arguments were not re-derived in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The owner's acceptance rule of this date applied: the card now says which part each cited source
    covers and which parts are its own. Hatcher's Theorem 4.3, printed p. 344, supplies exactness,
    and Hatcher's reading of $\pi_1(X,A,x_0)$ on printed p. 343 supplies the set that term is;
    Brown's Theorem 4.9 and Corollary 4.11, printed pp. 121 and 123, supply the related statement
    for a fibration of groupoids. The group chase at each window, Claim 1 at the $\pi_0(X,x_0)$
    term, the two windows centred at $\pi_1(A,x_0)$ and $\pi_1(X,x_0)$, and the counterexample to
    the printed form of (a) at $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$ are marked as the card's own.
    Checked: the Hatcher and Brown pages and that no cited source states the exercise. Not changed:
    any step of the proof itself.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The owner's acceptance rule applied at paragraph level: the solution opens with the provenance
    convention for a prose proof. Its remark already says which part Hatcher covers (Theorem 4.3,
    printed p. 344, and the reading of $\pi_1(X,A,x_0)$ on printed p. 343) and which part Brown
    covers (Theorem 4.9 and Corollary 4.11, printed pp. 121 and 123). Checked: the four pages.

---

::: {.problem}
Suppose we define $\pi_0(X, A, x_0)$ to be the quotient set $\pi_0(X, x_0) / i_*\bigl(\pi_0(A, x_0)\bigr)$ so that the long exact sequence of homotopy groups for the pair $(X, A)$ extends to $\cdots \to \pi_0(A, x_0) \stackrel{\iota_*}{\longrightarrow} \pi_0(X, x_0) \to \pi_0(X, A, x_0) \to 0$.

(a) Show that with this extension, the five-lemma holds for the map of long exact sequences induced by a map $(X, A, x_0) \to (Y, B, y_0)$, in the following form: One of the maps between the two sequences is a bijection if the four surrounding maps are bijections for all choices of $x_0$.

(b) Show that the long exact sequence of a triple $(X, A, B, x_0)$ can be extended only to the term $\pi_0(A, B, x_0)$ in general, and that the five-lemma holds for this extension.
:::

::: {.solution}
Provenance, paragraph by paragraph: a paragraph that names a printed source records that source's argument at the page given, and a paragraph that names none is the card's own, possibly applying a result cited in another paragraph.

Define, for a pointed pair $(X,A,x_0)$,
$$
\pi_0(X,A,x_0)=\pi_0(X,x_0)\big/\,i_*\pi_0(A,x_0),
$$
the quotient pointed set, so that every component of $X$ meeting $A$ becomes the distinguished element. Then
$$
\pi_0(A,x_0)\xrightarrow{i_*}\pi_0(X,x_0)\xrightarrow{j_*}\pi_0(X,A,x_0)\longrightarrow0
$$
is exact as a sequence of pointed sets: the components mapping to the distinguished relative class are exactly those meeting $A$, and $j_*$ is onto. Exactness of the whole extended sequence at every other term is Hatcher's Theorem 4.3 (printed p. 344, read in the text version `tmp/sources/hatcher-2002-algebraic-topology.md`).

Throughout, a map of pairs $\varphi:(X,A,x_0)\to(Y,B,y_0)$ induces a ladder between the two sequences, commutative by naturality of the long exact sequence (p. 345), and "exact" for pointed sets means that the image of one map is the fiber of the next over the distinguished element.

### (a) The five-lemma

*Terms of degree $\ge2$: the group case.* The standard five-lemma argument applies verbatim in a window of five group terms, since every map there is a homomorphism. Write the ladder as
$$
A\xrightarrow{f}B\xrightarrow{g}C\xrightarrow{h}D\xrightarrow{k}E
\quad\text{over}\quad
A'\xrightarrow{f'}B'\xrightarrow{g'}C'\xrightarrow{h'}D'\xrightarrow{k'}E'
$$
with all four squares commutative and both rows exact.

- *Injectivity of $\gamma:C\to C'$*, given $\alpha$ onto and $\beta,\delta$ one-to-one: if $\gamma(c)=1$ then $\delta h(c)=h'\gamma(c)=1$, so $h(c)=1$ and $c=g(b)$ for some $b$. Then $g'\beta(b)=\gamma g(b)=1$, so $\beta(b)=f'(a')$ for some $a'$, and $a'=\alpha(a)$ because $\alpha$ is onto. Hence $\beta(b)=\beta f(a)$, so $b=f(a)$ by injectivity of $\beta$, and $c=g(b)=gf(a)=1$.
- *Surjectivity of $\gamma$*, given $\beta$ and $\delta$ onto and $\varepsilon$ one-to-one: for $c'\in C'$ put $d'=h'(c')$ and choose $d\in D$ with $\delta(d)=d'$. Then $\varepsilon k(d)=k'\delta(d)=k'h'(c')=1$, so $k(d)=1$ because $\varepsilon$ is injective, and hence $d=h(c)$ for some $c\in C$. Now $h'(\gamma(c))=\delta h(c)=d'=h'(c')$, so $h'(\gamma(c)^{-1}c')=1$ and therefore $\gamma(c)^{-1}c'=g'(b')$ for some $b'\in B'$; choose $b\in B$ with $\beta(b)=b'$ and put $c''=c\,g(b)$. Then $\gamma(c'')=\gamma(c)g'(b')=c'$.

*Which windows these are.* The four terms of degree one or zero in the extended sequence are the pointed sets $\pi_1(X,A,x_0)$, $\pi_0(A,x_0)$, $\pi_0(X,x_0)$ and $\pi_0(X,A,x_0)$, and the whole sequence reads

$$
\cdots\to\pi_2(X)\to\pi_2(X,A)\to\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)\to\pi_0(A)\to\pi_0(X)\to\pi_0(X,A)\to0 .
$$

A window of five consecutive terms is one centered at its third term. So a window of five consecutive terms all of which are groups is exactly one centered at a term of degree $\ge2$; the window centered at $\pi_1(A,x_0)$ is $\pi_2(X)\to\pi_2(X,A)\to\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)$, which ends at the pointed set $\pi_1(X,A,x_0)$; and the window centered at $\pi_1(X,x_0)$ is $\pi_2(X,A)\to\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)\to\pi_0(A)$, which contains the two pointed sets $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$. The window centered at $\pi_1(X,A,x_0)$ is $\pi_1(A)\to\pi_1(X)\to\pi_1(X,A)\to\pi_0(A)\to\pi_0(X)$ and the one centered at $\pi_0(A,x_0)$ is $\pi_1(X)\to\pi_1(X,A)\to\pi_0(A)\to\pi_0(X)\to\pi_0(X,A)$. The last two are proved below, the term $\pi_0(X,x_0)$ by Claim 1 below, and the two centred at $\pi_1(A,x_0)$ and $\pi_1(X,x_0)$ at the end of this part. Every one of the six windows is therefore settled on this card: the one centred at $\pi_2(X,A,x_0)$ by the group chase, all five of its terms being groups, and the other five by the arguments below, each of which replaces the chase at a point where a term is only a pointed set.

*The term $\pi_1(X,A,x_0)$, and which set that is.* Hatcher defines $\pi_n(X,A,x_0)$ as the homotopy classes of maps of triples $(I^n,\partial I^n,J^{n-1})\to(X,A,x_0)$ (printed p. 343); for $n=1$ the $0$-end of $I$ is constrained only to lie in $A$, so $\pi_1(X,A,x_0)$ is the set of path classes from a point of $A$ to $x_0$, modulo homotopies through such paths, in which the start point moves inside $A$ and two classes with different start points may agree. With that reading the four surrounding maps of the term are
$$
\pi_1(A,a)\to\pi_1(B,\varphi a),\qquad \pi_1(X,a)\to\pi_1(Y,\varphi a)\quad(a\in A),\qquad \pi_0(A)\to\pi_0(B),\qquad \pi_0(X)\to\pi_0(Y),
$$
and the printed claim is that bijectivity of these four families forces the vertical map $\pi_1(X,A,x_0)\to\pi_1(Y,B,\varphi x_0)$ to be bijective. It does.

- *Injectivity.* Two relative classes with the same image have the same class of start point in $B$, because $\partial$ commutes with the map of pairs; injectivity at $\pi_0(A)$ puts their start points in one component of $A$, so a path $\delta$ in $A$ joins them, and translating one class along $\delta$ puts both at the same start point $a$. Their images then differ by a loop in $B$ at $\varphi a$, which lifts to a loop $\varepsilon$ in $A$ at $a$ because $\pi_1(A,a)\to\pi_1(B,\varphi a)$ is surjective; correcting by $\varepsilon$, the two representative paths have the same image in $Y$ from $\varphi a$ to $\varphi x_0$, hence agree by injectivity at $\pi_1(X,a)$.
- *Surjectivity.* A target class starts at some $b\in B$. By surjectivity at $\pi_0(A)$ its start point is $\varphi a$ for some $a\in A$ up to a path in $B$, and prepending that path makes the target path run from $\varphi a$ to $\varphi x_0$; the target lies over the class of $\varphi x_0$ in $\pi_0(Y)$, so by injectivity at $\pi_0(X)$ the point $a$ lies in the component of $x_0$ in $X$. A path in $X$ from $a$ to $x_0$ can then be corrected by a loop at $a$ so that its image is the target path, by surjectivity at $\pi_1(X,a)$, and the corrected path represents a relative class mapping onto the target.

*The term $\pi_0(A,x_0)$.* Its four surrounding maps are
$$
\pi_1(X,A,a)\to\pi_1(Y,B,\varphi a),\qquad \pi_1(X,a)\to\pi_1(Y,\varphi a)\quad(a\in A),\qquad \pi_0(X)\to\pi_0(Y),\qquad \pi_0(X,A,x_0)\to\pi_0(Y,B,\varphi x_0),
$$
and bijectivity of these families forces the vertical map $\pi_0(A)\to\pi_0(B)$ to be bijective, which is the printed claim at that term.

- *Injectivity.* Two points of $A$ whose images lie in the same component of $B$ lie in the same component of $X$, by injectivity at $\pi_0(X)$; a path in $X$ between them can be corrected by a loop so that its image is a prescribed path in $B$, by surjectivity at $\pi_1(X,a)$. The relative class of the constant path at the first point and that of the reversed corrected path at the second then have the same image in $\pi_1(Y,B,\varphi a)$, so by injectivity at $\pi_1(X,A,a)$ they agree, and applying $\partial$ gives that the two points lie in the same component of $A$.
- *Surjectivity.* A component $\beta$ of $B$ is the component of some $b\in B$; since $\pi_0(X)\to\pi_0(Y)$ is surjective, some component of $X$ maps into the component of $b$, and the class of that component in $\pi_0(X,A,x_0)$ is the base class by injectivity at $\pi_0(X,A,x_0)$, so a path in $A$ joins some $a\in A$ to a point of it. The path in $Y$ from $b$ to $\varphi a$ is a relative class at $\varphi a$, and it lifts along $\pi_1(X,A,a)\to\pi_1(Y,B,\varphi a)$ by surjectivity there; the image under $\partial$ of the lift is a component of $A$ mapping onto $\beta$.

*The certificate for those two terms.* Both statements are proved formally on `lean-categories` main, and those declarations are this card's certificate: `relativePiOne_map_bijective` and `zerothHomotopySubtypeMap_bijective` in [`LeanCategories/Topology/PairHomotopySequence.lean`](https://github.com/dzackgarza/lean-categories/blob/9b8b85840c2b5cef55942b971c65e3b4bfc0d252/LeanCategories/Topology/PairHomotopySequence.lean), the merge of <https://github.com/dzackgarza/lean-categories/issues/156> at commit `9b8b85840c`. Each takes the four surrounding maps of its own term as hypotheses, bijective at every basepoint of $A$, and concludes bijectivity of the vertical map at that term; the same file builds $\pi_1(X,A,x_0)$ as that quotient and proves exactness at the two joins that are not group statements. Elaborated on the pinned baseline (Lean 4.33.0, Mathlib `db584cd6`), both are free of `sorryAx`, with axioms only `propext`, `Classical.choice` and `Quot.sound`.

*The terms $\pi_1(A,x_0)$ and $\pi_1(X,x_0)$.* The first of the two windows is settled by the group chase of the group case, which does not in fact need all five terms to be groups: the fifth term $\pi_1(X,A,x_0)$ is a pointed set, but it enters the chase only through the bijection $\varepsilon$, while every product and inverse is taken in the groups $\pi_1(A,x_0)$ and $\pi_1(B,y_0)$. The second window is not: there the chase ends with the step $k'(\delta(c)^{-1}c')=k'\delta(c)^{-1}k'(c')$, which needs $k'$ to be a homomorphism, and at that window $k'$ is the map $j':\pi_1(Y,y_0)\to\pi_1(Y,B,y_0)$ of pointed sets. That one step is replaced below by a reading of the fibre of $k'$, and nothing else in the chase changes.

Write $\partial:\pi_2(X,A)\to\pi_1(A)$ and $\partial':\pi_2(Y,B)\to\pi_1(B)$ for the boundary maps of the two rows, $f:\pi_2(X)\to\pi_2(X,A)$ and $f':\pi_2(Y)\to\pi_2(Y,B)$ for the maps into their domains, $\beta:\pi_2(X,A)\to\pi_2(Y,B)$ for the vertical map there, and $h=i_*:\pi_1(A)\to\pi_1(X)$, $h'=i'_*:\pi_1(B)\to\pi_1(Y)$, $k=j:\pi_1(X)\to\pi_1(X,A)$, $k'=j':\pi_1(Y)\to\pi_1(Y,B)$ for the maps of the two rows at the two centres and to their right. The target pair is the problem's $(Y,B,y_0)$ throughout this part; the letters $C$ and $D$ are used only in part (b), for the triple $(X,A,B)$ over $(Y,C,D)$. All of $h$, $h'$, $k$ and $k'$ are maps of pointed sets; $h$ and $h'$ are group homomorphisms, and $k$ and $k'$ are not.

*The window centered at $\pi_1(A,x_0)$: the vertical map $\gamma:\pi_1(A,x_0)\to\pi_1(B,y_0)$.* Its four surrounding maps are $\alpha:\pi_2(X)\to\pi_2(Y)$, $\beta$, $\delta:\pi_1(X)\to\pi_1(Y)$ and $\varepsilon:\pi_1(X,A)\to\pi_1(Y,B)$.

- *Injectivity.* Let $\gamma(c)=1$. Then $\delta h(c)=h'\gamma(c)=1$, so $h(c)=1$ because $\delta$ is injective, hence $c=\partial(b)$ for some $b\in\pi_2(X,A)$ by exactness at $\pi_1(A)$. Then $1=\gamma(c)=\gamma\partial(b)=\partial'\beta(b)$, so $\beta(b)\in\ker\partial'=\operatorname{im}f'$, say $\beta(b)=f'(a')$; since $\alpha$ is onto, $a'=\alpha(a)$, so $\beta(b)=\beta f(a)$ and $b=f(a)$ because $\beta$ is injective. Therefore $c=\partial f(a)=1$ by exactness at $\pi_2(X,A)$.

- *Surjectivity.* Let $c'\in\pi_1(B)$. Put $d'=h'(c')\in\pi_1(Y)$ and choose $d\in\pi_1(X)$ with $\delta(d)=d'$, which is possible because $\delta$ is onto. Then $\varepsilon k(d)=k'\delta(d)=k'h'(c')=1$ because $\operatorname{im}h'\subseteq\ker k'$ by exactness at $\pi_1(Y)$, so $k(d)=1$ because $\varepsilon$ is injective, and hence $d=h(a)$ for some $a\in\pi_1(A)$ by exactness at $\pi_1(X)$. Now $h'\bigl(\gamma(a)^{-1}c'\bigr)=h'\gamma(a)^{-1}h'(c')=1$, because $h'$ is a homomorphism, so $\gamma(a)^{-1}c'\in\ker h'=\operatorname{im}\partial'$ by exactness at $\pi_1(B)$; write $\gamma(a)^{-1}c'=\partial'(\nu)$ and $\nu=\beta(\mu)$ with $\mu\in\pi_2(X,A)$, which is possible because $\beta$ is onto. Then $\gamma(a)^{-1}c'=\partial'\beta(\mu)=\gamma\partial(\mu)$, so $c''=a\cdot\partial(\mu)$ satisfies $\gamma(c'')=\gamma(a)\gamma\partial(\mu)=c'$.

*The window centered at $\pi_1(X,x_0)$: the vertical map $\delta:\pi_1(X,x_0)\to\pi_1(Y,y_0)$.* Its four surrounding maps are $\beta$, $\gamma$, $\varepsilon$ and $\theta:\pi_0(A,x_0)\to\pi_0(B,y_0)$.

- *Injectivity.* Let $\delta(c)=1$. Then $\varepsilon k(c)=k'\delta(c)=1$, so $k(c)=1$ because $\varepsilon$ is injective, hence $c=h(a)$ for some $a\in\pi_1(A)$ by exactness at $\pi_1(X)$. Then $1=\delta(c)=h'\gamma(a)$, so $\gamma(a)\in\ker h'=\operatorname{im}\partial'$, say $\gamma(a)=\partial'(\nu)=\partial'\beta(\mu)=\gamma\partial(\mu)$; hence $a=\partial(\mu)$ because $\gamma$ is injective, and $c=h\partial(\mu)=1$ by exactness at $\pi_2(X,A)$.

- *Surjectivity.* Let $c'\in\pi_1(Y)$ and put $d=\varepsilon^{-1}k'(c')\in\pi_1(X,A)$. Then $\theta\partial(d)=\partial'\varepsilon(d)=\partial'k'(c')=1$ because $\operatorname{im}k'\subseteq\ker\partial'$ by exactness at $\pi_1(Y,B)$, so $\partial(d)=1$ because $\theta$ is injective, and hence $d=k(c)$ for some $c\in\pi_1(X)$ by exactness at $\pi_1(X,A)$. Now $\delta(c)$ and $c'$ are loops at $y_0$ with the same image under $k'$, and that fixes the class only up to $\ker k'$. Products in $\pi_1$ are written in Hatcher's convention throughout this card, the first path traversed first, so $[a][b]^{-1}$ is $a$ followed by $b$ reversed. If $a$ and $b$ are loops at $y_0$ with $k'(a)=k'(b)$, a homotopy through paths from $B$ to $y_0$ joining them is a map of the square whose bottom edge is $a$, whose top edge is $b$, whose right edge is the constant loop at $y_0$ and whose left edge is a loop $\lambda$ in $B$ at $y_0$; reading the boundary of that square, the constant edge contributes nothing and $[a][b]^{-1}=[\lambda]$. Hence $[a][b]^{-1}\in\operatorname{im}i'_*=\ker k'$ by exactness at $\pi_1(Y)$, and with $a=\delta(c)$ and $b=c'$ this says
$$
\omega:=c'\cdot\delta(c)^{-1}=\bigl(\delta(c)\cdot c'^{-1}\bigr)^{-1}\in\operatorname{im}i'_* .
$$
Since $\gamma$ is onto, $\omega=i'_*\gamma(a)=\delta h(a)$ for some $a\in\pi_1(A)$, and then $c'':=h(a)\cdot c$ satisfies $\delta(c'')=\delta h(a)\cdot\delta(c)=\omega\cdot\delta(c)=c'\cdot\delta(c)^{-1}\cdot\delta(c)=c'$. The correction is therefore made on the left, $c''=h(a)\cdot c$, which is the order the convention requires: the earlier reading $\delta(c)^{-1}c'$ is the other of the two elements of the fibre, and its product with $\delta(c)$ on the right does not return $c'$.

Both arguments use one exactness assertion outside their window, at the centre's target, and both use the two-sided invertibility of the bijections at the surrounding terms; the products and inverses are taken in groups, and no map into a pointed set is treated as a homomorphism.

*Claim 1: the term $\pi_0(X,x_0)$.* If the vertical maps at $\pi_0(A,x_0)$ and at $\pi_0(X,A,x_0)$ are bijections, then so is the vertical map $\Phi:\pi_0(X,x_0)\to\pi_0(Y,y_0)$. The four surrounding maps of the window centred at $\pi_0(X,x_0)$ are the vertical maps at $\pi_1(X,A,x_0)$, at $\pi_0(A,x_0)$, at $\pi_0(X,A,x_0)$ and at the terminal $0$, the last being $0\to0$; the argument below uses the two at $\pi_0(A,x_0)$ and $\pi_0(X,A,x_0)$.

- *Injectivity.* Let $\Phi[x_1]=\Phi[x_2]$. Then $\theta j[x_1]=\theta j[x_2]$ by commutativity of the ladder, so $j[x_1]=j[x_2]$ because $\theta$, the vertical map at $\pi_0(X,A,x_0)$, is injective. Two components of $X$ have the same class in $\pi_0(X,A,x_0)=\pi_0(X,x_0)/i_*\pi_0(A,x_0)$ exactly when they are the same component or both meet $A$; in the second case injectivity of the vertical map at $\pi_0(A,x_0)$ puts them in one component of $A$, hence of $X$. So $[x_1]=[x_2]$.
- *Surjectivity.* Let $[y]\in\pi_0(Y,y_0)$. If $[y]$ meets $B$, choose $b\in B$ and $[a]\in\pi_0(A,x_0)$ with $\Phi[a]=[b]=[y]$, which exists because the vertical map at $\pi_0(A,x_0)$ is onto. Otherwise $[y]$ does not meet $B$, so $j'[y]$ is not the base class, and $\theta$ is onto, so $j'[y]=\theta[x]$ for some $[x]\in\pi_0(X,A,x_0)$; for a representative $x_1$ of $[x]$, $j'\Phi[x_1]=\theta j[x_1]=j'[y]$, so $\Phi[x_1]$ meets $B$ exactly when $[y]$ does, and it does not, hence $\Phi[x_1]=[y]$.

*Claim 2: the term $\pi_0(X,A,x_0)$.* If the vertical maps at $\pi_0(A,x_0)$ and at $\pi_0(X,x_0)$ are bijections, then so is the vertical map at $\pi_0(X,A,x_0)$. Indeed that map is induced by a bijection $\pi_0(X,x_0)\to\pi_0(Y,y_0)$ which carries the subset $i_*\pi_0(A,x_0)$ bijectively onto $i_*\pi_0(B,y_0)$, and a bijection of sets carrying one subset onto another induces a bijection of the quotients.

The two claims are conditional statements about the same four surrounding maps and are not circular: Claim 1 uses the bijections at $\pi_0(A,x_0)$ and at $\pi_0(X,A,x_0)$, Claim 2 those at $\pi_0(A,x_0)$ and at $\pi_0(X,x_0)$, so under the exercise's hypothesis every one of the three $\pi_0$ terms is settled.

### (b) The triple sequence

For $B\subset A\subset X$ the triple sequence of Theorem 4.3 ends
$$
\cdots\longrightarrow\pi_1(X,A,x_0)\xrightarrow{\partial}\pi_0(A,B,x_0),
$$

*Exactness at every term.* The sequence is exact at each of its terms for every $n\ge1$, and the extended sequence is exact at $\pi_1(X,A,x_0)$ as well; $\pi_0(A,B,x_0)$ is its last term, so nothing is asserted at it beyond its existence. The argument is Hatcher's proof of Theorem 4.3, printed pp. 344--345, which is a proof of the triple sequence and not only of the pair sequence; in degrees $n\ge2$ its three paragraphs apply verbatim, every term in sight there being a group and every map a homomorphism. In degree $1$ the same three arguments prove the pointed-set statements and nothing else is needed, but each homotopy written down has to be checked to be a homotopy of maps of triples: at $n=1$ a map $([0,1],\{0,1\},\{1\})\to(X,A,x_0)$ is a path in $X$ from a varying point of $A$ to the fixed point $x_0$ (printed p. 343), so a homotopy of such maps keeps the start point in $A$ and the endpoint at $x_0$, and at the terms $\pi_1(X,B,x_0)$ and $\pi_1(A,B,x_0)$ the start point has to stay in $B$. The three cases follow; the disk model of printed p. 343, in which a class in $\pi_n(X,A,x_0)$ is a map $(D^n,S^{n-1},s_0)\to(X,A,x_0)$ and $\partial$ is restriction to $S^{n-1}$, is used where it is shorter, Hatcher identifying the two models on that page.

- *At $\pi_1(X,B,x_0)$: $\operatorname{im}i_*=\ker j_*$.* For the inclusion, let $f:([0,1],\{0,1\},\{1\})\to(A,B,x_0)$ be a path in $A$ from a point of $B$ to $x_0$. The formula $H(s,u)=f\bigl(s(1-u)+u\bigr)$ defines a homotopy of maps of triples from $f$ to the constant path at $x_0$: it takes values in $A\subseteq X$, and $H(0,u)=f(u)\in A$, $H(1,u)=f(1)=x_0$, $H(s,0)=f(s)$, $H(s,1)=f(1)=x_0$. Hence the image of $[f]$ in $\pi_1(X,A,x_0)$ is the basepoint. For the converse, let $f:([0,1],\{0,1\},\{1\})\to(X,B,x_0)$ have trivial image in $\pi_1(X,A,x_0)$, through a homotopy $F:I^2\to X$ with $F(s,0)=f(s)$, $F(s,1)=x_0$, $F(0,u)\in A$ and $F(1,u)=x_0$. Its left edge $\lambda(u)=F(0,u)$ is a path in $A$ from $f(0)\in B$ to $x_0$, hence represents a class in $\pi_1(A,B,x_0)$. Reading the boundary of the square from the corner $(0,0)$ gives the loop $f\cdot x_0\cdot x_0\cdot\lambda^{-1}$, which is null-homotopic in $X$ because the square maps to $X$; so $f\simeq\lambda$ with endpoints fixed and $[f]=i_*[\lambda]$. This is the compression criterion of printed p. 343 at $n=1$: $f$ is homotopic rel $\partial I^1$ to the map $\lambda$ with image in $A$.
- *At $\pi_1(X,A,x_0)$: $\operatorname{im}j_*=\ker\partial$.* A class in the image of $j_*$ is represented by a path $f$ in $X$ from a point $b\in B$ to $x_0$; its boundary is the class of $b$ in $\pi_0(A,B,x_0)=\pi_0(A,x_0)/i_*\pi_0(B,x_0)$, which is the base class because the component of $b$ in $A$ meets $B$. Conversely, let $f$ be a path in $X$ from $a\in A$ to $x_0$ whose boundary is the base class, that is, the component of $a$ in $A$ meets $B$, and choose a path $\gamma$ in $A$ from a point $b\in B$ to $a$. Then $\gamma\cdot f$ is a path in $X$ from $B$ to $x_0$, and $\gamma\cdot f$ is homotopic to $f$ through paths from $A$ to $x_0$, the start point moving along $\gamma$ inside $A$; so $[f]=j_*[\gamma\cdot f]$. This is the tacking step of printed p. 344 at $n=1$, the restriction of $f$ to the face $I^0=\{0\}$ being the point $a$ that $\gamma$ carries into $B$.
- *At $\pi_1(A,B,x_0)$: $\operatorname{im}\partial=\ker i_*$.* For the inclusion, let $F:(D^2,S^1,s_0)\to(X,A,x_0)$ represent a class in $\pi_2(X,A,x_0)$ and let $\gamma=\restrictionof{F}{S^1}$, a loop in $A$ at $x_0$ whose class in $\pi_1(A,B,x_0)$ is $\partial[F]$. Parametrizing $S^1$ by $z:[0,1]\to S^1$ with $z(0)=s_0$ and putting $G_u(s)=F((1-u)z(s)+u s_0)$, whose argument lies in the disk, gives $G_u(0)=G_u(1)=F(s_0)=x_0$, $G_0=\gamma$ and $G_1$ constant; so $\gamma$ is null-homotopic in $X$ through loops at $x_0$, which is a homotopy of maps $([0,1],\{0,1\},\{1\})\to(X,B,x_0)$, and $i_*\partial[F]=1$. Conversely, let $f:([0,1],\{0,1\},\{1\})\to(A,B,x_0)$ be a path in $A$ from $b\in B$ to $x_0$ whose class in $\pi_1(X,B,x_0)$ is trivial, through a homotopy $F:I^2\to X$ with $F(s,0)=f(s)$, $F(s,1)=x_0$, $F(0,u)\in B$ and $F(1,u)=x_0$. Read as a map of the disk, $F$ carries $\partial I^2$ into $A$ --- the bottom edge to $f$, the left edge to $B$, the top and right edges to $x_0$ --- and the corner $(1,0)$ to $x_0$, so it represents a class $\xi\in\pi_2(X,A,x_0)$, and $\partial\xi$ is the class of the loop $g^{-1}\cdot f$, where $g=F(0,\,\cdot\,)$ is a path in $B$. Since $g^{-1}$ lies in $B$, $[g^{-1}\cdot f]=[f]$ in $\pi_1(A,B,x_0)$, so $[f]=\partial\xi$. This is Hatcher's tacking of $g$ onto $f$, printed p. 345, at $n=1$.

Every term of the triple sequence is therefore exact in degree $1$ as well, at the pointed sets $\pi_1(A,B,x_0)$ and $\pi_1(X,B,x_0)$, and the extended sequence is exact at $\pi_1(X,A,x_0)$.

Hardie--Kamps derive the same sequence algebraically, from the three exact pair sequences, and record that the derivation gives exactness at every term but one, the term $\pi_1(X,B,x_0)$, "where exactness has to be proved separately" (printed pp. 15--16 of the paper cited in the remark). The reason sits in their hypotheses: their Theorem 2.1 assumes exactness of type (E3) or (E3*) --- a group-stage condition --- in the left-hand column, and at the degree-one terms that column has only pointed sets. The three arguments above are Hatcher's geometric ones and need no extra step at that term: at $n=1$ the compression criterion supplies the homotopy of triples that the algebraic derivation does not.

It cannot in general be continued by $\pi_0(X,B,x_0)$. Take $X$ the disjoint union of a point $b_0$ and an interval, $x_0=b_0$, and $B=\{b_0,b_1\}$ with $b_1$ a point of the interval; let $A=\{b_0,b_1,a_1\}$ with $a_1\neq b_1$ a further point of the interval, so that $b_1$ and $a_1$ lie in different components of the subspace $A$ while lying in the same component of $X$. Then the class of $a_1$ in $\pi_0(A,B,x_0)=\pi_0(A,x_0)/i_*\pi_0(B,x_0)$ is not the distinguished element, because its component of $A$ does not meet $B$; but its image in $\pi_0(X,B,x_0)$ is distinguished, because every component of $X$ that meets $B$ is collapsed and $a_1$ lies in the component of $b_1$. On the other hand the class of $a_1$ is not in the image of $\partial:\pi_1(X,A,x_0)\to\pi_0(A,B,x_0)$, since a path in $X$ starting in $A$ and ending at $x_0=b_0$ stays in the component $\{b_0\}$ of $X$, so its starting point lies in the component $\{b_0\}$ of $A$, which is collapsed. Hence appending $\pi_0(X,B,x_0)$ would destroy exactness at $\pi_0(A,B,x_0)$.

*The hypothesis, and why it is stated for every basepoint.* The claim proved below is the five-lemma in the form of part (a): the four vertical maps surrounding a window are bijections for every admissible basepoint, and for the triple the admissible basepoints are the points of $B$. The clause is also tom Dieck's own: §6.2 Problem 3, printed p. 129, requires the injectivity hypothesis "for each $c\in A$". It is used and not merely inherited, because the arguments at the windows centred at $\pi_1(A,B,x_0)$ and at $\pi_1(X,B,x_0)$ rebase at a point $b_0\in B$ that need not be $x_0$. It is also necessary. Take $X=Y=[0,1]$, $\varphi$ the identity, $A=C=[0,\tfrac18]\cup[\tfrac34,\tfrac78]$, $B=\{0,\tfrac34,\tfrac78\}$ and $D=\{0\}\cup[\tfrac34,\tfrac78]$, with $x_0=y_0=0$. A relative path moves its start point only inside the base subspace and $[0,1]$ is contractible, so $\pi_1(X,B,x_0)$ has one class per point of $B$, namely three, and $\pi_1(Y,D,y_0)$ one per component of $D$, namely two; the vertical map at $\pi_1(X,B,x_0)$ is therefore three points onto two, the classes starting at $\tfrac34$ and at $\tfrac78$ having the same image, and it is not injective. At $x_0$ the four surrounding maps of that window are nevertheless bijections: $\pi_2(X,A,x_0)=0$ because $[0,1]$ is contractible and $\pi_1(A,x_0)=0$, while $\pi_1(A,B,x_0)$ is one point (only $0\in B$ lies in the component of $x_0$ in $A$), $\pi_1(X,A,x_0)$ is two points (the components of $A$) and $\pi_0(A,B,x_0)$ is one point (both components of $A$ meet $B$), and the target terms are the corresponding terms of the same subspaces, so the four maps are $0\to0$, a bijection of one-point sets, the identity of two-point sets and a bijection of one-point sets. What the clause removes is exactly this: at $b=\tfrac34\in B$ the vertical map at $\pi_1(A,B,b)$ is not injective, $\pi_1(A,B,\tfrac34)$ having the two classes starting at $\tfrac34$ and at $\tfrac78$ and $\pi_1(C,D,\tfrac34)$ one, those two points lying in one component of $D$. So the example refutes the single-basepoint form only, and the printed clause is what makes the theorem true.

*The degenerate case $B=\{x_0\}$, and why the two parts agree.* Taking $B=\{x_0\}$ in the triple and $D=\{y_0\}$ in the target turns part (b) into part (a): the triple sequence reads $\pi_n(A,x_0)\to\pi_n(X,x_0)\to\pi_n(X,A,x_0)\to\pi_{n-1}(A,x_0)$, which is the pair sequence of $(X,A)$, and $\pi_0(A,B,x_0)=\pi_0(A,x_0)/i_*\pi_0(\{x_0\},x_0)=\pi_0(A,x_0)$ is Hatcher's extension, while in the target $\pi_0(C,D,y_0)=\pi_0(C,y_0)$. The four set-valued windows of part (b) then have centres $\pi_2(X,x_0)$, $\pi_2(X,A,x_0)$, $\pi_1(A,x_0)$ and $\pi_1(X,x_0)$, which are four of the six windows settled in part (a), and the hypothesis "bijective at every basepoint of $B$" is the hypothesis at the single point $x_0$, which is what part (a)'s "for all choices of $x_0$" says at this degenerate case. So the two parts agree on the four windows they share. The windows centred at $\pi_1(X,A,x_0)$, at $\pi_0(A,x_0)$, at $\pi_0(X,x_0)$ and at $\pi_0(X,A,x_0)$ exist only in this degenerate case, where the sequence continues by the two steps to $\pi_0(X,x_0)$ that Hatcher notes after the triple display and then by the terminal term of part (a); for a general triple there is no such continuation, which is the example below. The two parts therefore neither overlap nor contradict each other.

With the sequence ending at $\pi_0(A,B,x_0)$, the ladder of triple sequences has group windows, settled by the chase of part (a), and four windows that contain a pointed set. *The group windows.* The terms of the triple sequence in degree $\ge2$ are groups and every map between them is a homomorphism, so a window of five consecutive terms which all lie in degree $\ge2$ is a window of five group terms, and the chase of part (a) applies to it verbatim; exactness of the triple sequence is Theorem 4.3 and its proof (printed pp. 344--345), exactness at the three degree-one terms being the three arguments of the paragraph above the inventory, and the ladder commutes by naturality (p. 345). *The set-valued windows.* The tail reads $\pi_2(A,B)\to\pi_2(X,B)\to\pi_2(X,A)\to\pi_1(A,B)\to\pi_1(X,B)\to\pi_1(X,A)\to\pi_0(A,B)$, and since the terminal term has no map out of it, the windows of five consecutive terms there that contain a pointed set are **four**: the one centred at $\pi_2(X,B,x_0)$, namely $\pi_3(X,A)\to\pi_2(A,B)\to\pi_2(X,B)\to\pi_2(X,A)\to\pi_1(A,B)$, whose centre is a group and whose last term is only a pointed set; the one centred at $\pi_2(X,A,x_0)$, namely $\pi_2(A,B)\to\pi_2(X,B)\to\pi_2(X,A)\to\pi_1(A,B)\to\pi_1(X,B)$, whose last two terms are only pointed sets; and the two centred at $\pi_1(A,B,x_0)$ and at $\pi_1(X,B,x_0)$, namely $\pi_2(X,B)\to\pi_2(X,A)\to\pi_1(A,B)\to\pi_1(X,B)\to\pi_1(X,A)$ and $\pi_2(X,A)\to\pi_1(A,B)\to\pi_1(X,B)\to\pi_1(X,A)\to\pi_0(A,B)$. No window is centred at $\pi_1(X,A,x_0)$, only the single term $\pi_0(A,B,x_0)$ following it, and none at $\pi_0(A,B,x_0)$, there being no exactness assertion at a last term with no map out of it. At the two windows centred at a $\pi_2$ term the centre and its vertical map $\gamma$ are a group and a homomorphism, so a trivial kernel is exactly injectivity of $\gamma$, and both directions are proved there: the surjectivity half of the chase corrects by $\gamma(c)^{-1}c'$, which needs the centre to be a group and the map out of it to be a homomorphism, and both of its ends are groups at these two windows; the coset lemma supplies the rest at the window centred at $\pi_2(X,A,x_0)$. At the two windows centred at the pointed sets $\pi_1(A,B,x_0)$ and $\pi_1(X,B,x_0)$, the explicit homotopy arguments below prove both injectivity and surjectivity. No full-injectivity conclusion is drawn merely from triviality of the fibre over the base point.

- *The window centred at $\pi_2(X,B,x_0)$*, whose four surrounding maps are $\alpha:\pi_3(X,A)\to\pi_3(Y,C)$, $\beta:\pi_2(A,B)\to\pi_2(C,D)$, $\delta:\pi_2(X,A)\to\pi_2(Y,C)$ and $\varepsilon:\pi_1(A,B)\to\pi_1(C,D)$, and whose centre's neighbours are $h:\pi_2(X,B)\to\pi_2(X,A)$ and $k:\pi_2(X,A)\to\pi_1(A,B)$, primed for the row of $(Y,C,D)$. Four of its five terms are groups, $\pi_1(A,B,x_0)$ entering only as the target of $k$ and as the pointed set whose vertical map $\varepsilon$ is a bijection of pointed sets. *Injectivity.* Let $\gamma(c)=1$. Then $\delta h(c)=h'\gamma(c)=1$, so $h(c)=1$ because $\delta$ is injective, hence $c=g(b)$ for some $b\in\pi_2(A,B)$ by exactness at $\pi_2(X,B)$. Then $g'\beta(b)=\gamma g(b)=1$, so $\beta(b)=f'(a')$ for some $a'$ by exactness at $\pi_2(C,D)$, and $a'=\alpha(a)$ because $\alpha$ is onto, so $\beta(b)=\beta f(a)$ and $b=f(a)$ by injectivity of $\beta$; hence $c=gf(a)=1$ by exactness at $\pi_2(A,B)$. Every equality is an exactness statement at a group, and no product is taken. *Surjectivity.* Let $c'\in\pi_2(Y,D)$ and put $d'=h'(c')\in\pi_2(Y,C)$. Since $\delta$ is onto, $d'=\delta(d)$ for some $d\in\pi_2(X,A)$. Exactness at $\pi_2(Y,C)$ gives $k'h'(c')=1$, so $\varepsilon(k(d))=k'\delta(d)=k'h'(c')=1$, and $\varepsilon$ injective gives $k(d)=1$; exactness at $\pi_2(X,A)$ then gives $d=h(c)$ for some $c\in\pi_2(X,B)$. Now $h'$ is a homomorphism, both of its ends being groups, so $h'\bigl(\gamma(c)^{-1}c'\bigr)=h'\gamma(c)^{-1}h'(c')=d'^{-1}d'=1$; hence $\gamma(c)^{-1}c'\in\ker h'=\operatorname{im}g'$ by exactness at $\pi_2(Y,D)$, say $\gamma(c)^{-1}c'=g'(b')$, and $b'=\beta(b)$ because $\beta$ is onto. Then $\gamma\bigl(c\,g(b)\bigr)=\gamma(c)\gamma g(b)=\gamma(c)g'\beta(b)=c'$, so $\gamma$ is onto with $c''=c\,g(b)$. Both directions at this window are therefore proved.
- *The window centred at $\pi_2(X,A,x_0)$*, whose four surrounding maps are $\alpha:\pi_2(A,B)\to\pi_2(C,D)$, $\beta:\pi_2(X,B)\to\pi_2(Y,D)$, $\delta:\pi_1(A,B)\to\pi_1(C,D)$ and $\varepsilon:\pi_1(X,B)\to\pi_1(Y,D)$, and whose centre's neighbours are $h:\pi_2(X,A)\to\pi_1(A,B)$ and $h':\pi_2(Y,C)\to\pi_1(C,D)$. Let $\gamma(c)=1$. Then $\delta h(c)=h'\gamma(c)=1$, so $h(c)=1$ because $\delta$ is injective, hence $c=g(b)$ for some $b\in\pi_2(X,B)$ by exactness at $\pi_2(X,A)$; then $g'\beta(b)=\gamma g(b)=1$, so $\beta(b)=f'(a')$ for some $a'$, and $a'=\alpha(a)$ because $\alpha$ is onto, so $\beta(b)=\beta f(a)$ and $b=f(a)$ by injectivity of $\beta$; hence $c=gf(a)=1$ by exactness at $\pi_2(X,B)$. Every equality in this paragraph is an exactness statement at a group --- $\pi_2$ of a pair is a group for $n\ge2$ --- and the pointed sets enter only through the bijections at the surrounding terms. The injectivity half is therefore proved. *The surjectivity half needs a fact about the boundary map that the abstract five-lemma does not see.* The map $h:\pi_2(X,A)\to\pi_1(A,B)$ is not a homomorphism into a group, but it factors as $h=q\circ\partial$, where $\partial:\pi_2(X,A)\to\pi_1(A,x_0)$ is the boundary map of the pair $(X,A)$, a homomorphism, and $q:\pi_1(A,x_0)\to\pi_1(A,B,x_0)$ is the map of pointed sets induced by the inclusion of pairs. Two facts about $q$ are used, and both are proved rather than assumed, $q$ being a map of pointed sets and not a homomorphism. First, $\ker q=\operatorname{im}\bigl(\pi_1(B,x_0)\to\pi_1(A,x_0)\bigr)$: this is exactness of the pair sequence at $\pi_1(A,x_0)$, the $n=1$ case of the second of Hatcher's three paragraphs on printed pp. 344--345. Second, *the fibre of $q$ through a point is a coset of $\ker q$*: for $\alpha,\alpha'\in\pi_1(A,x_0)$, $q(\alpha)=q(\alpha')$ exactly when $\alpha'\alpha^{-1}\in\ker q$. If $q(\alpha)=q(\alpha')$, let $H:I^2\to A$ be a homotopy with $H(s,0)=\alpha(s)$, $H(s,1)=\alpha'(s)$, $H(0,u)\in B$ and $H(1,u)=x_0$; reading the boundary of the square from the corner $(0,0)$ gives $\alpha\cdot x_0\cdot\alpha'^{-1}\cdot\eta^{-1}\simeq1$, where $\eta=H(0,\,\cdot\,)$ is a loop in $B$ at $x_0$, so $\alpha\alpha'^{-1}=[\eta]\in\ker q$ and hence $\alpha'\alpha^{-1}=[\eta]^{-1}\in\ker q$. Conversely, if $\alpha'\alpha^{-1}=[\beta]$ with $\beta$ a loop in $B$ at $x_0$, then $\alpha'=[\beta\cdot\alpha]$; the paths $\beta\cdot\alpha$ and $\alpha$ are respectively the fold and the inclusion of a single map on a wedge of two intervals into $A$, and since that wedge is homeomorphic to an interval the two paths are homotopic rel endpoints, so $q(\alpha')=q(\alpha)$. Hence for $x,x'\in\pi_2(X,A)$, written multiplicatively, $h(x)=h(x')$ exactly when $\partial(x')\partial(x)^{-1}\in\ker q$, that is, exactly when $\partial(x'x^{-1})\in\operatorname{im}\pi_1(B)=\ker q$, which is exactly $x'x^{-1}\in\ker h=\operatorname{im}g$; so the fibre of $h$ through $x$ is the coset $(\ker h)x$. The same holds for $h'$ and the triple $(Y,C,D)$. This second computation is exactness of the pair sequence at $\pi_1(A,x_0)$ in the strengthened sense that Hardie--Kamps call type (E2), printed p. 5 of the paper cited in the remark: the group $\pi_1(B,x_0)$ acts on $\pi_1(A,x_0)$ by left multiplication through $i_*$, and $q(\alpha)=q(\alpha')$ exactly when $\alpha'=\beta\cdot\alpha$ for some $\beta\in\pi_1(B,x_0)$, which is the statement proved above in the form $\alpha'\alpha^{-1}\in\ker q$.

Now let $c'\in\pi_2(Y,C)$ and put $y=h'(c')$. Since $\delta$ is onto, $y=\delta(d_0)$ for some $d_0\in\pi_1(A,B)$. Exactness at $\pi_1(C,D)$ gives $i'(y)=1$, so $\varepsilon(i(d_0))=i'(\delta(d_0))=1$, and $\varepsilon$ injective gives $i(d_0)=1$; exactness at $\pi_1(A,B)$ then gives $d_0=h(a)$ for some $a\in\pi_2(X,A)$. Then $h'(\gamma(a))=\delta(h(a))=y=h'(c')$. By the coset lemma for $h'$, $c'=k\gamma(a)$ with $k\in\ker h'=\operatorname{im}g'$; write $k=g'(b')$ and $b'=\beta(b)$, using that $\beta$ is onto. Then $c'=g'(\beta(b))\gamma(a)=\gamma(g(b))\gamma(a)=\gamma(g(b)a)$, since $\gamma$ is a homomorphism. So $\gamma$ is onto, and both halves at this window are proved.
- *At $\pi_1(A,B,x_0)$*, with $i:\pi_1(A,B)\to\pi_1(X,B)$, $j:\pi_1(X,B)\to\pi_1(X,A)$ and $\partial:\pi_2(X,A)\to\pi_1(A,B)$ the boundary map of the triple, and the corresponding primed maps. *The basepoint fibre.* Let $\gamma(c)=1$. Then $\delta i(c)=i'\gamma(c)=1$, so $i(c)=1$ because $\delta$ is injective, hence $c=\partial(b)$ for some $b$ by exactness at $\pi_1(A,B)$. Then $1=\gamma(c)=\partial'\beta(b)$, so $\beta(b)\in\ker\partial'=\operatorname{im}\bigl(\pi_2(Y,D)\to\pi_2(Y,C)\bigr)$, say $\beta(b)=f'(a')$, and $a'=\alpha(a)$ because $\alpha$ is onto, so $\beta(b)=\beta f(a)$ and $b=f(a)$ by injectivity of $\beta$; hence $c=\partial f(a)=1$ by exactness at $\pi_2(X,A)$. The same calculation applies at every admissible basepoint.

  *Injectivity.* Let $\gamma(c_0)=\gamma(c_1)$, and choose representative paths $r_0,r_1$ in $A$, with image paths $p_0,p_1$ in $C$. Since $\delta$ is injective, $\delta i(c_0)=\delta i(c_1)$ gives $i(c_0)=i(c_1)$. The starting edge of a homotopy witnessing this equality is a path $\eta$ in $B$ from $r_0(0)$ to $r_1(0)$. Replace $r_1$ by $\eta\cdot r_1$ and $p_1$ by its new image. Prepending $\eta$ does not change $c_1$, since $\eta$ lies in $B$; thus $c_0,c_1$ are unchanged, but now $r_0,r_1$ have the common start point $b_0=r_0(0)$, and $p_0,p_1$ have the common start point $p_0(0)$.

  The equality $\gamma(c_0)=\gamma(c_1)$ now gives a homotopy $H$ in $C$ from $p_0$ to $p_1$ whose starting edge $\lambda$ is a loop in $D$ at $p_0(0)$ and whose ending edge is constant at $y_0$. Reading the boundary of $H$ gives $p_0\simeq\lambda\cdot p_1$ with endpoints fixed, and therefore
  $$
  p_1\cdot p_0^{-1}\simeq\lambda^{-1}.
  $$
  Form the loop $\ell=r_1\cdot r_0^{-1}$ in $A$ at $b_0$. Its image in $\pi_1(C,D,p_0(0))$ is the class of $p_1\cdot p_0^{-1}\simeq\lambda^{-1}$, a loop in $D$ at the basepoint, so $\gamma_{b_0}([\ell])=1$. The basepoint-fibre calculation, applied at $b_0$, gives $[\ell]=1$ in $\pi_1(A,B,b_0)$. By exactness of the pair $(A,B)$ at $\pi_1(A,b_0)$, the absolute loop $\ell$ is homotopic in $A$ to a loop $\beta$ in $B$ at $b_0$. Hence $r_1\simeq\beta\cdot r_0$ in $A$ with endpoints fixed. Prepending the $B$-loop $\beta$ does not change a class in $\pi_1(A,B,x_0)$, so $c_1=[r_1]=[r_0]=c_0$. Thus $\gamma$ is injective.

  *Surjectivity.* Products below use Hatcher's convention throughout this card: the first path is traversed first, and $p^{-1}$ is $p$ reversed. Let $c'\in\pi_1(C,D,y_0)$. Since $\delta$ is onto, choose $d\in\pi_1(X,B,x_0)$ with $\delta(d)=i'(c')$. Then $\varepsilon j(d)=j'\delta(d)=j'i'(c')=1$, so $j(d)=1$ because $\varepsilon$ is injective. Exactness at $\pi_1(X,B,x_0)$ therefore gives $c\in\pi_1(A,B,x_0)$ with $i(c)=d$, and hence $i'\gamma(c)=i'(c')$.

  Choose representative paths for $c$ and $c'$, and let $p$ and $q$ be their image paths in $C$; thus $p,q$ run from points of $D$ to $y_0$. The equality $i'\gamma(c)=i'(c')$ supplies a homotopy
  $$
  H:I^2\longrightarrow Y,\qquad H(s,0)=p(s),\quad H(s,1)=q(s),\quad H(0,t)=\lambda(t)\in D,\quad H(1,t)=y_0 .
  $$
  All of $\partial I^2$ maps into $C$. In Hatcher's disk model (printed p. 343), $H$ therefore represents a class $\eta\in\pi_2(Y,C,y_0)$, based at the bottom-right corner of the square. Reading its boundary from that corner, first along the reversed bottom edge and then along the left and top edges, gives
  $$
  \partial\eta=[\ell]\in\pi_1(C,y_0),\qquad \ell=p^{-1}\cdot\lambda\cdot q .
  $$
  Since $\beta:\pi_2(X,A,x_0)\to\pi_2(Y,C,y_0)$ is onto, choose $\mu$ with $\beta(\mu)=\eta$. Let $\nu=\partial\mu\in\pi_1(A,x_0)$, and write $\bar\nu$ for its image in $\pi_1(A,B,x_0)$. Naturality of the pair boundary gives $\gamma(\bar\nu)=q_C([\ell])$, where $q_C:\pi_1(C,y_0)\to\pi_1(C,D,y_0)$ is induced by inclusion. Concatenation with the loop $\nu$ at the endpoint is well-defined on relative classes, and the corrected class $c\cdot\bar\nu$ has image $[p\cdot\ell]$ in $\pi_1(C,D,y_0)$.

  The usual endpoint-fixed cancellation of $p\cdot p^{-1}$ in $C$ gives $[p\cdot\ell]=[\lambda\cdot q]$. The remaining initial segment lies in $D$ and can be absorbed into the varying start point. Explicitly, parametrize $\lambda\cdot q$ by $\lambda(2s)$ on $0\le s\le1/2$ and $q(2s-1)$ on $1/2\le s\le1$, and define
  $$
  K(s,t)=\begin{cases}
  \lambda(t+2s),&0\le s\le(1-t)/2,\\[2pt]
  q\!\left(\dfrac{2s-1+t}{1+t}\right),&(1-t)/2\le s\le1 .
  \end{cases}
  $$
  This is continuous, with $K(s,0)=(\lambda\cdot q)(s)$ and $K(s,1)=q(s)$; also $K(0,t)=\lambda(t)\in D$ and $K(1,t)=y_0$. It is therefore a homotopy through paths representing classes in $\pi_1(C,D,y_0)$. Consequently
  $$
  \gamma(c\cdot\bar\nu)=[p\cdot\ell]=[\lambda\cdot q]=[q]=c',
  $$
  so $\gamma$ is onto.
- *At $\pi_1(X,B,x_0)$.* *Injectivity.* Let $\delta(c_0)=\delta(c_1)$. Since $\varepsilon$ is injective, $\varepsilon j(c_0)=\varepsilon j(c_1)$ gives $j(c_0)=j(c_1)$. Choose representative paths $r_0,r_1$ in $X$, with endpoints in $B$ and $x_0$, and let $p_0,p_1$ be their image paths in $Y$. The equality $j(c_0)=j(c_1)$ gives a homotopy $K$ in $X$ from $r_0$ to $r_1$ whose starting edge $\eta$ lies in $A$ and whose ending edge is constant at $x_0$. Set $b_0=r_0(0)$, and write $\eta_C$ for the image of $\eta$ in $C$. Reading the boundary of $K$ gives $r_0\simeq\eta\cdot r_1$ with endpoints fixed, so
  $$
  c_1=[\eta^{-1}\cdot r_0].
  $$
  Moreover $\eta^{-1}$ represents a class $b\in\pi_1(A,B,b_0)$, because it lies in $A$, starts at $r_1(0)\in B$, and ends at $b_0$.

  Let $H$ be the homotopy in $Y$ from $p_0$ to $p_1$ supplied by $\delta(c_0)=\delta(c_1)$, with starting edge $\lambda$ in $D$ and ending edge constant at $y_0$. From $K$ and $H$ respectively we obtain $p_0\simeq\eta_C\cdot p_1$ and $p_0\simeq\lambda\cdot p_1$, all with endpoints fixed. Hence $\eta_C\simeq\lambda$ in $Y$ with endpoints fixed, so the loop $\lambda\cdot\eta_C^{-1}$ in $C$ at $p_0(0)$ is nullhomotopic in $Y$. Its nullhomotopy is a relative $2$-disk representing $\zeta\in\pi_2(Y,C,p_0(0))$. Absorbing the initial $D$-path $\lambda$ into the varying start point shows that
  $$
  \partial'\zeta=[\eta_C^{-1}]=\gamma_{b_0}(b)
  $$
  in $\pi_1(C,D,p_0(0))$.

  Surjectivity of $\alpha_{b_0}:\pi_2(X,A,b_0)\to\pi_2(Y,C,p_0(0))$ gives $\xi$ with $\alpha_{b_0}(\xi)=\zeta$. Naturality gives $\gamma_{b_0}(b)=\gamma_{b_0}(\partial\xi)$, and the first window's injectivity, applied at the basepoint $b_0$, gives $b=\partial\xi$. Therefore $i_{b_0}(b)=1$ by exactness at $\pi_1(A,B,b_0)$. Concatenating the resulting homotopy from $\eta^{-1}$ to the constant path at $b_0$ with $r_0$ gives $[\eta^{-1}\cdot r_0]=[r_0]$ in $\pi_1(X,B,x_0)$. Hence $c_1=c_0$, so $\delta$ is injective; in particular its fibre over the base point is trivial.

  *Surjectivity.* Let $c'\in\pi_1(Y,D,y_0)$. Since $\varepsilon:\pi_1(X,A,x_0)\to\pi_1(Y,C,y_0)$ is onto, choose $d\in\pi_1(X,A,x_0)$ with $\varepsilon(d)=j'(c')$. Then $\partial'\varepsilon(d)=\partial'j'(c')=1$, so $\partial(d)=1$ by injectivity of the vertical map at $\pi_0(A,B,x_0)$. Exactness at $\pi_1(X,A,x_0)$ gives $c\in\pi_1(X,B,x_0)$ with $j(c)=d$, and consequently $j'\delta(c)=j'(c')$.

  Choose a representative path $r$ of $c$, with $r(0)=b_0\in B$ and $r(1)=x_0$, and write $p$ for its image path in $Y$. Let $q$ be a representative path of $c'$. Since $j'\delta(c)=j'(c')$, there is a homotopy
  $$
  H:I^2\longrightarrow Y,\qquad H(s,0)=p(s),\quad H(s,1)=q(s),\quad H(0,t)=\lambda(t)\in C,\quad H(1,t)=y_0 .
  $$
  Here $\lambda$ runs from $p(0)$ to $q(0)$. The square $H$ is a nullhomotopy in $Y$ of the loop $p^{-1}\cdot\lambda\cdot q$, so $p\simeq\lambda\cdot q$ with start and end points fixed; reversing the starting edge gives $q\simeq\lambda^{-1}\cdot p$, also with start and end points fixed.

  Now use the hypothesis at the basepoint $b_0$, not merely at $x_0$. The path $\lambda^{-1}$ lies in $C$, starts at $q(0)\in D$, and ends at $p(0)\in D$, so it represents a class in $\pi_1(C,D,p(0))$. Surjectivity of
  $$
  \gamma_{b_0}:\pi_1(A,B,b_0)\longrightarrow\pi_1(C,D,p(0))
  $$
  gives a class $b$ with $\gamma_{b_0}(b)=[\lambda^{-1}]$. Choose a representative path $\rho$ of $b$; it lies in $A$, starts at a point of $B$, and ends at $b_0$. If $\rho'$ is its image path in $C$, the equality $\gamma_{b_0}(b)=[\lambda^{-1}]$ supplies a homotopy from $\rho'$ to $\lambda^{-1}$ whose starting point stays in $D$ and whose endpoint is fixed at $p(0)$. Concatenating that homotopy with $p$ shows that $[\rho'\cdot p]=[\lambda^{-1}\cdot p]$ in $\pi_1(Y,D,y_0)$.

  The concatenation $\rho\cdot r$ is defined because $\rho$ ends at $b_0=r(0)$, and it represents a class in $\pi_1(X,B,x_0)$. Its image is $[\rho'\cdot p]$. Since $q\simeq\lambda^{-1}\cdot p$ with endpoints fixed,
  $$
  \delta([\rho\cdot r])=[\rho'\cdot p]=[\lambda^{-1}\cdot p]=[q]=c'.
  $$
  Thus $\delta$ is onto.

Exactness at every term is proved above, at $\pi_n(X,B,x_0)$, $\pi_n(X,A,x_0)$ and $\pi_n(A,B,x_0)$ for every $n\ge1$, by Hatcher's three paragraphs; in degree $1$, where the terms are pointed sets, they are the three bullets of the paragraph above the inventory, which also prove exactness at $\pi_1(X,A,x_0)$, the term the extension adds. With that, at all four set-valued windows the card proves both halves of the five-lemma. At the two centred at a $\pi_2$ term, $\pi_2(X,B,x_0)$ and $\pi_2(X,A,x_0)$, injectivity follows because the centre is a group and the vertical map a homomorphism with trivial kernel, and surjectivity uses a correction taken in a group, with the coset lemma at the second window. At $\pi_1(A,B,x_0)$, full injectivity is obtained by aligning the two representatives' start points and applying the basepoint-fibre calculation to their difference loop at the common start; surjectivity lifts $H$ to a relative $2$-disk and concatenates with its boundary. At $\pi_1(X,B,x_0)$, both halves are rebased at $b_0$: injectivity uses the first window's full injectivity there, and surjectivity concatenates with a lift of the reversed starting edge. The two vertical maps of pointed sets are bijective, not merely maps with trivial basepoint fibre. What is proved about the terminal term is the quotient statement on which Claim 2 rests: $\pi_0(A,B,x_0)=\pi_0(A,x_0)/i_*\pi_0(B,x_0)$, and a bijection $\pi_0(A,x_0)\to\pi_0(C,y_0)$ which carries $i_*\pi_0(B,x_0)$ onto $i'_*\pi_0(D,y_0)$ induces a bijection $\pi_0(A,B,x_0)\to\pi_0(C,D,y_0)$; so bijectivity of the vertical maps at $\pi_0(A,x_0)$ and at $\pi_0(B,x_0)$ forces bijectivity at $\pi_0(A,B,x_0)$.
:::

::: {.remark title="Sources"}

The exercise is Exercise 9 of §4.1, printed p. 358, read in the text version `tmp/sources/hatcher-2002-algebraic-topology.md`, stated with the errata's $i_*$ in place of $i^*$. Which part each source covers, and which are the card's own: Hatcher's Theorem 4.3 and its three exactness paragraphs, printed pp. 344--345, together with the compression criterion of printed pp. 343--344, supply exactness of the pair and of the triple sequence at every term, the degree-one terms included, and Hatcher's reading of $\pi_1(X,A,x_0)$ on printed p. 343 supplies the set that the $\pi_1$ term is; Brown's Theorem 4.9 and Corollary 4.11, printed pp. 121 and 123, supply the related statement for a fibration of groupoids and nothing of the exercise's own sequence; everything else — the group chase at each window, Claim 1 at the $\pi_0(X,x_0)$ term, the two windows centred at $\pi_1(A,x_0)$ and $\pi_1(X,x_0)$, the verification that Hatcher's degree-one homotopies are homotopies of triples, the coset lemma at the $\pi_2(X,A,x_0)$ window, and the example showing that the triple sequence stops at $\pi_0(A,B,x_0)$ — is the card's own argument. The two statements the exercise asks for are stated, in the same generality, in Friedrich tom Dieck, *Algebraic Topology* (EMS, 2008): the exact sequence of a triple, ending at $\pi_1(X,A,b)$, is Problem 3 of §6.1, printed p. 125; and the five-lemma at the pointed-set end is Problem 3 of §6.2, printed p. 129, where the hypotheses are the two directions at $\pi_1(X,A,a)$ separately, with the injectivity half required "for each $c\in A$" and concluded "for each $a\in A$" — the same restriction to every basepoint that this card's part (b) states, and Hatcher's (a) at the term $\pi_1(X,A,x_0)$ follows from that problem, its four bijections giving tom Dieck's hypotheses in both halves. Both are problems there: the book states the two facts and proves neither, so it supplies the form and the clause, not a proof (reading copy `tmp/sources/tomdieck-algebraic-topology-ranicki.md`, whose running heads put §6.1 at printed p. 125 and §6.3 at printed p. 129). The printed claim (a) is proved on this card at every window: at every term of degree $\ge2$, by the group chase; at both set-valued terms $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$, where it is carried by the declarations `relativePiOne_map_bijective` and `zerothHomotopySubtypeMap_bijective` of [`LeanCategories/Topology/PairHomotopySequence.lean`](https://github.com/dzackgarza/lean-categories/blob/9b8b85840c2b5cef55942b971c65e3b4bfc0d252/LeanCategories/Topology/PairHomotopySequence.lean) on `lean-categories` main, with $\pi_1(X,A,x_0)$ read as Hatcher's quotient in which the start point moves inside $A$ (printed p. 343); at the term $\pi_0(X,x_0)$, by Claim 1; and at the two windows centered at $\pi_1(A,x_0)$ and at $\pi_1(X,x_0)$, by the argument of part (a), whose only non-group step is replaced by the exactness assertion at the centre's target. For part (b), exactness at every term of the triple sequence is Hatcher's argument at $n\ge1$, written out at $n=1$ where the terms are pointed sets, and no further term exists by the card's example. The group windows of the ladder are proved. At the two windows centred at a $\pi_2$ term, $\pi_2(X,B,x_0)$ and $\pi_2(X,A,x_0)$, whose centres are groups and whose vertical maps are homomorphisms, the card proves both directions, injectivity by the chase and surjectivity by the chase up to the coset lemma. At the two windows centred at $\pi_1(A,B,x_0)$ and $\pi_1(X,B,x_0)$ it proves full injectivity as well as surjectivity: the first aligns the representatives' start points and applies the basepoint-fibre chase to their difference loop at the common start, while the second rebases at $b_0$ and applies that full injectivity there. The two surjectivity constructions lift a relative $2$-disk and a reversed starting edge, respectively. Hence every vertical map in every five-term window of the truncated triple ladder is a bijection. No published proof of this exercise was located, in the retained sets or in the sources searched for it; the two tom Dieck problems state its two halves and prove neither.

A published treatment of the exact sequence of a triple, and of which of its terms is the delicate one: **K. A. Hardie and K. H. Kamps, *Exact sequence interlocking and free homotopy theory*, Cahiers de topologie et géométrie différentielle catégoriques **26** (1985), 3--31**, open access at `http://www.numdam.org/item?id=CTGDC_1985__26_1_3_0`. Their §3.A, printed pp. 15--16, derives the exact homotopy sequence of a triple $(X,A,B,x_0)$ from the three exact sequences of its pairs by their Theorem 2.1, and states that the derivation yields exactness "except at $\pi_1(X,B,x_0)$ where exactness has to be proved separately" (the running text is a 1985 scan; the OCR prints the symbol as "Tri", and the term is the one this card proves separately, at the point where the sequence leaves the group range). Their §1, printed pp. 4--5, lists the exactness types (E0)--(E4) for pointed sets and pointed maps, and type (E2) there is exactly the structure of this card's coset lemma: a group acting on a pointed set $B$ with $\beta(b)=\beta(b')$ exactly when $b'=a\cdot b$ for some $a$ of the group, that is, the fibres of the next map are the orbits. What the paper gives is the published form of the two facts and not the exercise: Theorem 2.1 is an exactness result, not a five-lemma, it says nothing at the set-valued terms of a ladder, and the exercise itself is not treated.

A related published statement, cited for exactly what it proves: **R. Brown, *Fibrations of groupoids*, Journal of Algebra 15 (1970), 103--132**, Theorem 4.9 on printed p. 121 and Corollary 4.11 on printed p. 123 (reading copy `tmp/sources/brown-1970-fibrations-of-groupoids.md`). For a fibration of groupoids $p:G\to H$ with fibre $F$ over an object $v$, Brown's 4.9(a) concludes that $f:\pi_0F\to\pi_0F'$ is surjective if the maps of vertex groups $h:H(v)\to H'(v')$ and of components $g:\pi_0G\to\pi_0G'$ are surjective and $h:\pi_0H\to\pi_0H'$ is injective, and 4.9(b) concludes that $f$ is injective on $\ker(i:\pi_0F\to\pi_0G)$ if $h:H(v)\to H'(v')$ is injective and $g:G(x)\to G'(x')$ is surjective; Corollary 4.11 concludes that $h:H\to H'$ and $g:G\to G'$ being equivalences of groupoids forces $f:F\to F'$ to be an equivalence, in particular $f:\pi_0F\to\pi_0F'$ to be a bijection, the proof applying 4.9 and then the ordinary five-lemma for groups to Brown's diagram 4.8. That is a five-lemma at the $\pi_0$ term, and its hypotheses are stronger than the exercise's: an equivalence of groupoids is a bijection on hom-sets at every object and on components, which is the exercise's "for all choices of $x_0$" in a setting where a fibration supplies the exact sequence. It is a statement about fibrations of groupoids, and the map of pairs $(X,A)\to(Y,B)$ is not one, so nothing on this card rests on it: it is the related statement, for groupoids, of the five-lemma at the $\pi_0$ term that the two declarations above prove for the pair sequence. Brown is explicit that the groupoid analogue is weaker than the space-level statement, and his own Example 4.10, printed p. 122, is a map of fibrations of groupoids for which the hypotheses of 4.9(b) hold and $f:\pi_0F\to\pi_0F'$ is nevertheless not injective: he says in the remark before it that "the conclusion of 4.9(b) is weaker than in the usual 5-lemma" and that the example shows the assumptions "do not imply $f:\pi_0F\to\pi_0F'$ injective even when $g:\pi_0G\to\pi_0G'$ is injective". That is the sharpest form of the reason this card proves its own statement instead of quoting the groupoid one.

:::
