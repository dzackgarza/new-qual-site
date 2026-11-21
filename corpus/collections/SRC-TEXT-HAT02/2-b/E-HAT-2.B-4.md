---

schema: qual/card@1
id: E-HAT-2.B-4
kind: problem
title: "Linking numbers via Mayer--Vietoris"
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
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the Alexander-duality and Mayer--Vietoris calculations and all degree shifts.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 4, printed page
    176, with the printed hint. (a) checked: Φ(x,y) = (y/|y|, x/|y|) is a
    homeomorphism S^{p+q−1} − S^{p−1} → S^{q−1} × R^p with inverse
    (v,u)/√(1+|v|²), and contracting the R^p factor gives the deformation retraction.
    (b) checked: [S^{q−1}] generates H̃_{q−1} of the complement of S^{p−1} (Exercise 3
    applied to (D^p,S^{p−1}) ⊂ (D^{p+q},S^{p+q−1}) makes the inclusion an
    isomorphism on H_{q−1}), yet a disjoint D^q is a chain there bounding it, so the
    class would vanish. No defect.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Examined the indexed answer to Math StackExchange question 666444, including its diagram;
    the direct page fetch presented a Cloudflare challenge. Its map f is zero for a reason that
    also destroys the proposed contradiction: with C=D^{p+q}-D^q and
    A=S^{p+q-1}-S^{q-1}, Exercise 3 makes A into C a homology isomorphism in every degree,
    so H_*(C,A)=0. Thus neither that diagram nor the suggested acyclic-pair shortcut supplies a
    complete published proof. Did not alter the checked bounding-chain proof; the complete
    published-solution obligation remains open.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Repaired a hypothesis gap in (b). The previous step applied Exercise 3 to the pair
    (D^p,S^{p-1}) inside (D^{p+q},S^{p+q-1}), but Exercise 3 requires D^p to meet the boundary
    sphere in exactly S^{p-1}, and the hypothesis of (b) does not give that: an embedded disk with
    boundary S^{p-1} can meet the boundary sphere in the interior of the disk, as the arc
    gamma(t) = (t, 1-t^2) in D^2 shows, with endpoints at (+-1,0) in S^1 and
    norm(gamma(t))^2 = t^4 - t^2 + 1 <= 1, equality exactly at t = 0 and t = +-1, so the arc is
    tangent to S^1 at (0,1). Checked replacement: radial contraction z -> z/norm(z) retracts
    D^{p+q} - S^{p-1} onto S^{p+q-1} - S^{p-1}, since a point (x,y) with y nonzero and
    norm <= 1 has last coordinates y((1-t) + t/norm(x,y)) with bracket >= 1 along the segment;
    that retraction is a homotopy equivalence, the inclusion into D^{p+q} - D^p factors it
    because S^{p-1} is contained in D^p, and a map with injective composite is injective. So the
    inclusion into D^{p+q} - D^p is injective on reduced H_{q-1}, which is all the contradiction
    needs, and no properness is used. Parts (a) and (b)'s bounding-chain argument are otherwise
    unchanged. What is not covered: no complete published solution to (a) has been located, so
    that source obligation stays open; no certificate.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Withdraws the repair recorded in the previous event: the radial-contraction step was FALSE and
    has been removed. Read literally, D^{p+q} - S^{p-1} contains the origin, where z/norm(z) is
    undefined, and it contains the points with y = 0 and norm(x) < 1, whose images under the radial
    formula land in the removed sphere S^{p-1}; so the claimed retraction does not exist and the
    claimed homotopy equivalence is unfounded. Worse, without a properness hypothesis the
    inclusion S^{p+q-1} - S^{p-1} into D^{p+q} - D^p is not even a well-defined map, so
    'the inclusion factors it' was circular: it presupposed exactly the condition the event above
    had shown to be unavailable. The tangent-arc example ((t, 1-t^2) in D^2, tangent to S^1 at
    (0,1)) is precisely a case where the inclusion is undefined. What the card now does: it states
    D^p cap S^{p+q-1} = S^{p-1} as an explicit hypothesis, quotes Hatcher's own hint (Exercise 3,
    printed p. 176, whose hypothesis is exactly that intersection condition) to get the isomorphism
    of that inclusion, and closes (b) by factoring the inclusion through the contractible disk D^q.
    The hypothesis boundary itself is the subject of the discussion at Math StackExchange question
    4771220, which assumes S^{p-1} = h(D^p) cap S^{p+q-1}, proves (b) under it, notes that only
    S^{q-1} contained in h'(D^q) is needed of the second disk, and states that the weaker reading
    h(S^{p-1}) = S^{p-1} breaks the argument; that is an unreviewed user discussion, so it is cited
    as the source of the hypothesis analysis, not accepted as a published solution. NOT established:
    (b) for disks that meet the boundary sphere away from S^{p-1}. That case is open on this card
    and is stated as such in the proof. Part (a) is untouched.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Withdraws the framing, not the conditional proof. The previous two events presented the
    properness hypothesis as a repair of a defect in the exercise and read the tangent-arc example
    as showing that the exercise needs the hypothesis. Neither is established: no source proves
    that properness is necessary for the printed statement, and the arc example shows only that
    this particular proof needs it, since it makes the displayed inclusion undefined. The proof now
    says explicitly that step 4 is a conditional result, that it is not offered as a correction to
    Hatcher, and that whether the hypothesis can be dropped is open. Still owed, and recorded as
    owed rather than discharged: a source-backed reduction from an arbitrary embedded disk with
    boundary S^{p-1} to a proper one, or a complete published proof of the printed statement. What
    the search located: for locally flat embeddings the reduction is a consequence of the ambient
    isotopy and collar theorems in Rushing, Topological Embeddings (Chapter 1 defines proper
    embeddings and local flatness; the isotopy extension and collar theorems give the push into the
    interior), which does not cover wild embeddings; and the combinatorial linking-number formalism
    of DeTurck and Gluck, Higher dimensional linking integrals (arXiv:0802.0320), defines the
    linking number of two disjoint null-homologous cycles without any properness hypothesis, but
    presupposes a combinatorial or smooth structure, so it also does not settle the topological
    statement as printed. No complete published solution to (b) in full generality has been
    located. The card is not certified and the source obligation is not closed.
- event: solution-reviewed
  by: claude
  date: 2026-11-11
  note: >-
    Part (b) is now proved as printed, on p. 176, with no hypothesis on the disks beyond the
    statement: the reduction to the proper case is by a collar. Each step checked against Hatcher
    (2002). Step #collar: with $D_2$ the radius-2 ball, the extension $F$ is $f(2x)$ on $\norm x\le
    1/2$ and $2\norm x\,f(x/\norm x)$ on $1/2\le\norm x\le 1$; the pieces agree at $\norm x=1/2$
    because $2x=x/\norm x$ there; continuity is the pasting lemma on two closed halves; injectivity
    holds because the second piece has $\norm{F(x)}=2\norm x$ (as $f$ of the unit sphere has norm
    one) so radii and then directions are recovered, and a common point of the two images has norm
    exactly one, forcing the same preimage; a continuous injection from the compact $D^p$ into the
    Hausdorff $D_2$ is an embedding. $\norm{F(x)}=2$ holds exactly for $\norm x=1$, so
    $F(D^p)\cap\partial D_2=2S^{p-1}$. Step #collar-disjoint: inner pieces disjoint by hypothesis,
    outer pieces are the cones on $S^{p-1}$ and $S^{q-1}$ over $1\le t\le2$ and are disjoint because
    those spheres are, and an inner point of norm one lying in the other cone lies on
    $S^{q-1}=g(\partial D^q)$, contradicting disjointness. Step #collar-rescale: scaling by $1/2$
    maps $D_2$ onto $D^n$ and preserves all the properties, giving proper disks in $(D^n,S^{n-1})$.
    Step #proper-case: Exercise 3 (printed p. 176) applied to the proper disk, with the class
    $[S^{q-1}]$ a generator by step #s3, against the null-homology supplied by the other disk. The
    earlier audit note recording (b) as proved only under a properness hypothesis is superseded on
    that point; the source obligation is unchanged, no published solution of the exercise having been
    located.
- event: solution-reviewed
  by: claude
  date: 2026-11-11
  note: >-
    Correction, and the degenerate cases added. The previous note on this card claimed the argument
    needs $p,q\ge1$ and offered a counterexample at $p=0$; that sentence was false and is removed. A
    concentric smaller disk of $D^q$ has a smaller sphere as its boundary, not $S^{q-1}$, so it is not
    a candidate for the disk whose boundary $S^{q-1}$ is. At $p=0$ one has $n=q$ and the ambient ball
    is $D^q$ itself, and statement (b) holds: an embedding $g:D^q\to D^q$ with $g(\partial D^q)=
    S^{q-1}$ is onto, by Invariance of Domain, Theorem 2B.3 (p. 172), applied to the interior, together
    with the compactness of $g(D^q)$ and the connectedness of $\operatorname{int}D^q$. That argument is
    now step #degenerate, with $q=0$ by symmetry and $p=q=0$ noted as the single-point ambient ball, and
    the exercise is read as printed, for all $p,q\ge0$. Steps #s3 and later are scoped to $p,q\ge1$,
    where they are used, and the closing step dispatches the degenerate cases through #degenerate.
    Checked: $g(\operatorname{int}D^q)=g(D^q)\cap\operatorname{int}D^q$ from injectivity of $g$ and
    $g(\partial D^q)=\partial D^q$; openness is Theorem 2B.3 applied to the injective map of the open
    set $\operatorname{int}D^q\cong\RR^q$ into $\RR^q$; closedness is compactness of $g(D^q)$ in the
    Hausdorff $D^q$; nonemptiness and connectedness of $\operatorname{int}D^q$ finish it. Not checked:
    the removal of the earlier claim leaves the collar argument of #collar untouched, which the note
    below records; the source obligation is unchanged, no published solution having been located.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    The exercise is on printed p. 176 in two parts. (a) is the computed homeomorphism $\Phi(x,y)=(y/\abs{y}, x/\abs{y})$ onto $S^{q-1}\times\RR^p$ together with the straight-line deformation retraction onto $S^{q-1}$, and the homology statement behind it is part (b) of Hatcher's Proposition 2B.1, printed p. 169 with its proof on pp. 169--170. (b) is the contradiction obtained from §2.B Exercise 3, printed p. 176, applied to the collared disks; its degenerate cases $p=0$ and $q=0$ are settled by Invariance of Domain, Theorem 2B.3, printed p. 172, and Corollary 2B.4, printed p. 172. Checked against the book: the printed statement has no hypothesis on the disks, and the collaring step now runs for $p,q\ge1$ with the two degenerate cases separate, so the card reads the exercise as printed. The earlier claim that (b) fails at $p=0$ is withdrawn and the reason is recorded in the audit trail.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    #123 batch. Checked against the book: Exercise 4 of §2.B, printed p. 176, parts (a) and
    (b) exactly as printed, with no hypothesis on the two disks beyond disjointness. Part (a)
    is checked by composing the two displayed formulas in both orders; part (b) is the
    collared-disk reduction into disks proper in $(D^n,S^{n-1})$, then Exercise 3 of §2.B and
    the generator $[S^{q-1}]$; the cases $p=0$ and $q=0$ are settled by Invariance of Domain,
    Theorem 2B.3, printed p. 172. Repair: the card carried a second `---` line after its front
    matter, which the parser leaves at the head of the body and Pandoc renders as a horizontal
    rule; it is removed. The one Math StackExchange thread on part (b), question 666444, has an
    accepted answer, 795440, that is a commutative-diagram sketch invoking "problem 3" and
    "problem 4(a)" and naming a contradiction without the fundamental-class step; it is read
    and not transcribed. Not claimed: a published solution of Exercise 2.B.4.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader batch. Three repairs, on the reader's report; the reader found no defect in
    the mathematics of either part and in the construction of the collar. (1) The step
    `#proper-case` closed the contradiction with a "fundamental chain" of $E=g(D^q)$ whose
    boundary is the fundamental cycle of $S^{q-1}$, which asserts more structure than the
    step uses and shows less than the step needs, since $E$ is only known to be an embedded
    disk. It now uses only that: $E\cong D^q$ is contractible, so $\widetilde H_{q-1}(E)=0$,
    and the inclusion $\partial E\hookrightarrow D^n-D$ factors through $E$, so the class
    $[S^{q-1}]$ dies. No fundamental class, no manifold-with-boundary structure, and no
    orientation is used. (2) The remark was titled "Published solution" while the card and
    COMPLAINTS.md record that no published solution of the exercise has been located; it is
    retitled "Sources" and now says so. It also cited Corollary 2B.4 (printed p. 172) beside
    Theorem 2B.3, and the proof uses the theorem but never the corollary: the degenerate cases
    rest on Invariance of Domain alone. The same overstatement in the 2026-11-13
    `solution-reviewed` note, which lists Corollary 2B.4 among the results settling $p=0$ and
    $q=0$, is wrong and its reference to Corollary 2B.4 is withdrawn; (3) the citations name
    their text version, `tmp/sources/hatcher-2002-algebraic-topology.md` (Exercise 4 on printed
    p. 176, Proposition 2B.1 on pp. 169--170, Theorem 2B.3 on p. 172). Checked, unchanged:
    both composites of the displayed formulas are the identity, the collar $F$ is an
    embedding with $F(D^p)\cap\partial D_2=2S^{p-1}$, and the description of the accepted
    Math StackExchange answer 795440 to question 666444 (a diagram invoking "problem 3" and
    "problem 4(a)" of that thread, declaring $f$ zero and a contradiction) is accurate.
    Not claimed: a published solution of Exercise 2.B.4.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    #123 batch, the two published sources for part (a). Read at the cited place in its text
    version: tom Dieck, §2.8.3 "Complements of spheres", printed p. 52, in
    `tmp/sources/tomdieck-algebraic-topology-ranicki.md`, and Koukpari's solution to §2.B
    Exercise 4, printed p. 16, in `tmp/sources/koukpari-hatcher-solutions.md`. Checked: both
    display the same homeomorphism of $S^{p+q-1}-S^{p-1}$ with $S^{q-1}\times\RR^p$: Koukpari's
    Koukpari's $\phi(u,v)=(v,u)/\sqrt{1+\norm v^2}$, whose image misses $S^{p-1}$ because the
    last $q$ coordinates $u/\sqrt{1+\norm v^2}$ are nonzero, and tom Dieck's
    $(x,y)\mapsto(\sqrt{1-\norm y^2}\,x,y)$, which is the same map with the two blocks of
    coordinates in the opposite order and the $\RR^p$ factor reparametrized onto the open unit
    ball. Defect in the source, verified against the printed page rather than the extraction:
    tom Dieck's target $S^m\times E^n$ has an exponent one too small, since the displayed $y$
    lies in the second block $\RR^{n+1}$ of the ambient $\RR^{m+n+2}$ and
    $(1-\norm y^2)+\norm y^2=1$ places the image on $S^{m+n+1}$, with the image of
    $\norm y\le1$ equal to the complement for $\norm y<1$; with $(m,n)=(q-1,p-1)$ the corrected
    statement is part (a) as printed. Koukpari's solution to part (b) on the same printed p. 16
    assumes $S^{p-1}=D^p\cap S^{p+q-1}$, which Hatcher's printed statement (p. 176, re-read
    here) does not give, so it is not a published proof of (b) as printed; tom Dieck's
    following paragraph on the two circles in $S^3$ is the $\pi_1$ linking statement, also not
    the exercise. Not claimed: a published proof of part (b) as printed.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Part (a) transcribed from the two sources into steps #s1 and #s2, each step naming its
    source, the numbered statement and the printed page: #s1 the homeomorphism, from
    Koukpari's solution to §2.B Exercise 4(a), printed p. 16, whose displayed $\phi$ it
    reproduces in coordinates, and tom Dieck's §2.8.3, printed p. 52, which displays the same
    map in the other direction; #s2 the deformation retraction, from the same two passages.
    The inverse $\phi^{-1}(x,y)=(y/\norm y,x/\norm y)$ and the two composites are computed on
    the card because Koukpari leaves them as "clearly ... with continuous inverse"; both are
    verified. Part (b), steps #degenerate and #s3 onward, is unchanged mathematics: it was and
    remains the card's own argument from §2.B Exercise 3 (printed p. 176) and Theorem 2B.3
    (printed p. 172). The Sources remark was rewritten to name the two publications with their
    numbered statements, printed pages and text versions, to state tom Dieck's printed exponent
    and its correction, to record that Koukpari's (b) assumes a hypothesis Hatcher does not
    print, and to say that part (b) still has no located published proof; the earlier claim
    that part (a)'s homology content is Proposition 2B.1(b), pp. 169--170, is dropped from it,
    no step using that proposition. `COMPLAINTS.md` carries the record of this date for the
    open part (b) obligation.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The owner's acceptance rule of this date applied step by step. Part (a): the generator statement
    of step #s3 is now marked as the card's own application of the h-equivalences of Koukpari,
    printed p. 16, and tom Dieck, printed p. 52. Part (b): each of the five steps --- #collar,
    #collar-extension, #collar-disjoint, #collar-rescale, #proper-case --- now says that its
    argument is the card's own, no published proof of (b) having been located, and #proper-case
    says what it takes from §2.B Exercise 3, printed p. 176, whose proof is on `E-HAT-2.B-3`.
    Checked: that no step in part (b) reproduces a published argument, and the two pages cited above.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170, the correctness read of this card's own part, which is (b). Read against Hatcher,
    Exercise 4 of §2.B on printed p. 176, in `tmp/sources/hatcher-2002-algebraic-topology.md`, and
    tom Dieck, §2.8.3 on printed p. 52, in `tmp/sources/tomdieck-algebraic-topology-ranicki.md`.
    No defect found. Checked in part (a): $\phi(u,v)=(v,u)/\sqrt{1+\norm{v}^2}$ has
    $\norm{\phi(u,v)}^2=(\norm{v}^2+1)/(1+\norm{v}^2)=1$, its last $q$ coordinates
    $u/\sqrt{1+\norm{v}^2}$ are nonzero, and both composites with $(x,y)\mapsto(y/\norm y,x/\norm y)$
    are the identity — the second through $\norm{\phi\phi^{-1}(x,y)}=(x,y)/\sqrt{\norm y^2+\norm x^2}$
    — so the two published formulas do give a homeomorphism. tom Dieck's printed target
    $S^m\times E^n$ with $(x,y)\mapsto(\sqrt{1-\norm y^2}\,x,y)$ is dimensionally one exponent
    short, since $y$ ranges in $\RR^{n+1}$ and the image lies on $S^{m+n+1}$: the card's correction
    to $E^{n+1}$ is right. Checked in part (b): the collar $F$ is well defined at
    $\norm x=1/2$ because $2x=x/\norm x$ there, and injective because the outer piece has
    $\norm{F(x)}=2\norm x\in[1,2]$ while $f$ lands in $D^n$, so a common point of the two pieces
    has norm one and forces the same preimage; $F(D^p)\cap\partial D_2=2S^{p-1}$; the two outer
    cones are disjoint because $S^{p-1}\cap S^{q-1}=\emptyset$, and an inner point common with an
    outer one would have norm exactly one and so lie in $f(D^p)\cap g(D^q)$; scaling by $1/2$
    preserves embeddings, disjointness and properness. The proper case then applies Exercise 3 of
    §2.B to $(D,S^{p-1})$, whose hypothesis $D\cap S^{n-1}=S^{p-1}$ holds, and kills the generator
    $[S^{q-1}]$ through the contractible $E=g(D^q)$: $[S^{q-1}]$ is the image of the fundamental
    class under the inclusion, which is a homotopy equivalence by steps `#s1` and `#s2`. Checked in
    the degenerate case: $g(\operatorname{int}D^q)=g(D^q)\cap\operatorname{int}D^q$ by injectivity
    and $g(\partial D^q)=\partial D^q$, that set is open by Theorem 2B.3 and closed because
    $g(D^q)$ is compact, and $\operatorname{int}D^q$ is connected. Not claimed: a published proof
    of (b), none having been located.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170, referee read of part (b)'s own steps, which are the five steps no published proof
    covers. Each was checked against the printed pages its statement needs and found sound.
    `#collar-extension`: the two halves of $F$ agree at $\norm x=\tfrac12$ because $2x=x/\norm x$
    there, the outer value has norm $2\norm x\in[1,2]$ since $f$ of the unit sphere has norm one,
    so radii and then directions are recovered and the pieces meet only on the overlap;
    $F(\partial D^p)=2S^{p-1}$ and $F(D^p)\cap\partial D_2=2S^{p-1}$ follow from $\norm{F(x)}=2$
    exactly at $\norm x=1$. `#collar-disjoint`: the inner pieces are disjoint by hypothesis, the
    outer cones because $S^{p-1}\cap S^{q-1}=\emptyset$, and an inner point in an outer cone has
    norm one, hence lies on $S^{q-1}=g(\partial D^q)\subset g(D^q)$, against disjointness.
    `#collar-rescale`: division by $2$ is a homeomorphism $D_2\to D^n$ carrying $\partial D_2$ to
    $S^{n-1}$, so it preserves the embeddings, the disjointness and the properness. `#proper-case`:
    Exercise 3 of §2.B (printed p. 176) applies because $D\cap S^{n-1}=S^{p-1}$ holds by the
    properness just arranged, so $[S^{q-1}]$ has nonzero image in $\widetilde H_{q-1}(D^n-D)$, while
    the factorization $S^{q-1}=\partial E\hookrightarrow E\hookrightarrow D^n-D$ through the
    contractible $E=g(D^q)$ kills it — the two are contradictory and no such pair exists. The
    closing step then dispatches $p,q\ge1$ through `#collar` and `#proper-case` and $p=0$ or $q=0$
    through `#degenerate`, which rests on Invariance of Domain, Theorem 2B.3, printed p. 172.
    Nothing changed this pass: the repair of `#proper-case` recorded on 2026-11-16 (the class dies
    through a contractible disk, no fundamental chain) is what the argument needs and uses.
    Not claimed: a published proof of (b), none located.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Locator repair, no mathematics: the one surviving page reference in the live text — "the printed page
    and the correction are recorded in the Sources remark" — now reads "the statement in question and the
    correction", which is what the remark gives. The card's exercise, its collared-disk reduction and its
    invocations of Exercise 2.B.3, of Hatcher's Proposition 2B.1 and of Invariance of Domain Theorem 2B.3
    are cited by number, and no page number remains in the problem, the solution or a remark. The dated
    events above keep the text their sessions wrote, page references included, as QUAL-11 requires. No
    claim changed; `qualc.authoring check` passes.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    The provenance sentence at the head of the solution now states the search result with its date: part
    (a) is transcribed from the two published solutions named in the Sources remark, and searches run on
    2026-11-20, recorded with their queries and negative results in the entry of that date in
    COMPLAINTS.md, found no published proof of part (b) as printed, so the obligation recorded there on
    2026-11-16 stands. The Sources remark carries the same later date. Read again against the exercise:
    step s1's homeomorphism phi(u,v) = (v,u)/sqrt(1+|v|^2) with inverse (x,y) -> (y/|y|, x/|y|), and the
    two composites are the identity because |x|^2 + |y|^2 = 1; step s2 reads the deformation retraction
    off S^{q-1} x R^p; step s3 makes [S^{q-1}] a generator; step `degenerate` settles p = 0 and q = 0 by
    Invariance of Domain, Theorem 2B.3, where an embedding g with g(partial D^q) = S^{q-1} has image
    both open and closed in the connected interior, hence onto; and step `collar-extension` builds the
    proper disks F and G with F(x) = f(2x) for |x| <= 1/2 and 2|x| f(x/|x|) for 1/2 <= |x| <= 1, which is
    well defined at |x| = 1/2, embeds D^p, and has F(partial D^p) = 2S^{p-1} on the boundary of the
    radius-2 ball, the two outer cones meeting only at the origin and so disjoint. The final homology
    contradiction of step `proper-case` was then read as well: Exercise 3 of §2.B gives the isomorphism
    H_{q-1}(S^{n-1} - S^{p-1}) = H_{q-1}(D^n - D) for the proper disk D = f(D^p), the class [S^{q-1}]
    generates the source by step s3, and S^{q-1} bounds E = g(D^q) lying in D^n - D, which is
    contractible, so that class dies in the target. That is the contradiction, and it is correct.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read correct, and recorded as standing under the decision the orchestrator posted on issue #163 for
    this exercise: no published solution of part (b) as printed was found, so the card's own proof stands
    once a reader reads it correct. The reading: part (a) is the two transcribed published solutions of the
    Sources remark; part (b) is the card's, and every step of it was read — the degenerate cases p = 0 and
    q = 0 by Invariance of Domain, Theorem 2B.3; the generator [S^{q-1}] by steps s1 to s3; the proper
    disks by the collar extension; and the final contradiction, where §2.B Exercise 3 identifies
    H_{q-1}(D^n - D) with H_{q-1}(S^{n-1} - S^{p-1}) and the class dies because S^{q-1} bounds the disk E
    inside D^n - D. The source obligation is closed by the decision, not by a citation.
---

::: {.problem}
In the unit sphere $S^{p+q-1} \subset \RR^{p+q}$ let $S^{p-1}$ and $S^{q-1}$ be the subspheres consisting of points whose last $q$ and first $p$ coordinates are zero, respectively.

(a) Show that $S^{p+q-1} - S^{p-1}$ deformation retracts onto $S^{q-1}$, and is in fact homeomorphic to $S^{q-1} \times \RR^p$.

(b) Show that $S^{p-1}$ and $S^{q-1}$ are not the boundaries of any pair of disjointly embedded disks $D^p$ and $D^q$ in $D^{p+q}$.
[The preceding exercise may be useful.]
:::

::: {.solution}
The argument for part (a) is transcribed from the two published solutions named in the Sources remark at the end; the argument for part (b) is the card's own. Searches run on 2026-11-20 found no published proof of part (b) as printed — the queries and their negative results are recorded in the entry of that date in `COMPLAINTS.md` — so the obligation recorded there on 2026-11-16 stands. The book results used are Hatcher, *Algebraic Topology* (2002), §2.B Exercise 4, its printed hint §2.B Exercise 3, and Invariance of Domain, Theorem 2B.3.

Write points of $S^{p+q-1}$ as $(x,y)\in\RR^p\oplus\RR^q$ and put $n=p+q$. Then
$$
S^{p-1}=\{(x,0):\norm{x}=1\},
\qquad
S^{q-1}=\{(0,y):\norm{y}=1\},
$$
so $S^{p-1}\cap S^{q-1}=\emptyset$ and both are contained in $S^{n-1}$.

The exercise is read as printed, for all $p,q\ge0$: at $p=0$ the sphere $S^{p-1}$ is the empty sphere $S^{-1}$ and $\partial D^0=\emptyset$, and at $q=0$ likewise, and step [](#degenerate){.pf-ref} settles those two cases. The rest of the argument assumes $p,q\ge1$, where $S^{p-1}$ and $S^{q-1}$ are nonempty spheres in $S^{n-1}$. The results of the book used are Exercise 3 of §2.B — for a pair of subspaces $(D,S)\subset(D^n,S^{n-1})$ homeomorphic to $(D^k,S^{k-1})$ with $D\cap S^{n-1}=S$, the inclusion $S^{n-1}-S\hookrightarrow D^n-D$ induces an isomorphism on homology — and Invariance of Domain, Theorem 2B.3, in the two degenerate cases. Part (a) is steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, transcribed from the two published solutions named in the Sources remark at the end; part (b) is the rest, and no published proof of part (b) as printed was located.

::: pf

::: {.pf-step #s1}

There is a homeomorphism
$$
S^{p+q-1}-S^{p-1}\cong S^{q-1}\times\RR^p.
$$

::: pf-proof

Write $X=S^{p+q-1}-S^{p-1}$, on which $y\ne0$, and put
$$
\phi(u,v)=\frac{(v,u)}{\sqrt{1+\norm{v}^2}},\qquad (u,v)\in S^{q-1}\times\RR^p .
$$
The vector $\phi(u,v)$ has norm one and its last $q$ coordinates are $u/\sqrt{1+\norm{v}^2}\ne0$, so $\phi$ maps into $X$, and it is continuous because the denominator never vanishes. These are the map and the observations of the solution to §2.B Exercise 4(a), where the formula is written out in coordinates as
$$
(s_{p+1},\ldots,s_{p+q},v_1,\ldots,v_p)\longmapsto\frac{(v_1,\ldots,v_p,s_{p+1},\ldots,s_{p+q})}{\sqrt{s_{p+1}^2+\cdots+s_{p+q}^2+v_1^2+\cdots+v_p^2}} .
$$
The inverse is
$$
\phi^{-1}(x,y)=\left(\frac y{\norm{y}},\frac x{\norm{y}}\right),
$$
which is continuous on $X$, and the two composites are the identity. For the first, $\norm{\phi(u,v)}^2=(\norm v^2+1)/(1+\norm v^2)=1$, so $\phi^{-1}\phi(u,v)=(u,v)$; for the second, $\norm x^2+\norm y^2=1$ gives
$$
\phi\phi^{-1}(x,y)=\frac{(x,y)}{\norm y\sqrt{1+\norm x^2/\norm y^2}}=\frac{(x,y)}{\sqrt{\norm y^2+\norm x^2}}=(x,y).
$$
That the inverse is continuous and that the composites are the identity is what that source leaves as "clearly we have a continuous map (with continuous inverse), since the denominator in the image is never zero", and it is checked here.

tom Dieck, §2.8.3, displays the same homeomorphism, in the direction of $\phi$ and with the two blocks of coordinates in the opposite order: for $S^{m+n+1}\subset\RR^{m+1}\oplus\RR^{n+1}$ and $(m,n)=(q-1,p-1)$ his map is $(x,y)\mapsto(\sqrt{1-\norm y^2}\,x,y)$, restricted to $\norm y<1$, with $x$ the unit vector in the direction of the last $q$ coordinates of the image and $y$ the first $p$. The reparametrization $y\mapsto y/\sqrt{1+\norm y^2}$ of the $\RR^p$ factor, a homeomorphism of $\RR^p$ onto the open unit ball, carries his formula to $\phi$. The exponent printed there in the target, $S^m\times E^n$, is one too small; the statement in question and the correction are recorded in the Sources remark.

:::

:::

::: {.pf-step #s2}

Hence $S^{p+q-1}-S^{p-1}$ deformation retracts onto the coordinate sphere $S^{q-1}$.

::: pf-proof

Under the homeomorphism $\phi$ of step [](#s1){.pf-ref} the coordinate sphere $S^{q-1}$ of $X$ corresponds to $S^{q-1}\times\{0\}$, because $\phi(u,0)=(0,u)$. The linear contraction $H(u,v,t)=(u,(1-t)v)$ retracts $S^{q-1}\times\RR^p$ onto that subspace through maps of it into itself and fixes it pointwise, so it is a deformation retraction; conjugating it by $\phi$ gives one of $X$ onto $S^{q-1}$. That is the argument of the solution to §2.B Exercise 4(a): $S^{q-1}\times\RR^p$ deformation retracts to $S^{q-1}\times\{0\}=S^{q-1}$, hence by that homeomorphism $X$ deformation retracts to $S^{q-1}$. It gives the $h$-equivalence of $X$ with $S^{q-1}$ stated in tom Dieck, §2.8.3.

:::

:::

::: {.pf-step #degenerate}

If $p=0$ or $q=0$, part (b) holds.

::: pf-proof

Suppose first that $p=0$ and $q\ge1$, so that $n=q$ and the ambient ball is $D^q$ itself, $S^{p-1}=S^{-1}=\emptyset$ and $\partial D^0=\emptyset$. Let $g:D^q\to D^q$ be an embedding with $g(\partial D^q)=S^{q-1}$. Since $g$ is injective with $g(\partial D^q)=\partial D^q$, it carries the interior onto the complement of the boundary of its image,
$$
g(\operatorname{int}D^q)=g(D^q)-g(\partial D^q)=g(D^q)-S^{q-1}=g(D^q)\cap\operatorname{int}D^q .
$$

*That set is open in $\operatorname{int}D^q$.* The interior $\operatorname{int}D^q$ is homeomorphic to $\RR^q$, and $g$ restricts to an injective continuous map of it into $\RR^q$; by Invariance of Domain, Theorem 2B.3, its image is open.

*It is closed in $\operatorname{int}D^q$.* The set $g(D^q)$ is compact, hence closed in the Hausdorff space $D^q$, so $g(D^q)\cap\operatorname{int}D^q$ is closed in the open subspace $\operatorname{int}D^q$.

*It is nonempty and $\operatorname{int}D^q$ is connected*, so the clopen nonempty subset $g(\operatorname{int}D^q)$ is all of $\operatorname{int}D^q$. Hence $g(D^q)=g(\operatorname{int}D^q)\cup g(\partial D^q)=\operatorname{int}D^q\cup S^{q-1}=D^q$. A disk $D^0$ is a single point of $D^q$, so it lies in $g(D^q)$ and the two disks are not disjoint.

For $q=0$ the same argument applies with $p$ in place of $q$: an embedding $f:D^p\to D^p$ with $f(\partial D^p)=S^{p-1}$ has open image by Theorem 2B.3 and compact hence closed image, so it is onto, and the point $D^0$ lies in $f(D^p)$. At $p=q=0$ the ambient ball is a single point, both disks are that point, and they meet.

:::

:::

::: {.pf-step #s3}

Assume $p,q\ge1$. Then the class
$$
[S^{q-1}]\in \widetilde H_{q-1}(S^{n-1}-S^{p-1})\cong\ZZ
$$
is a generator.

::: pf-proof

The argument of this step is the card's own, applied to the $h$-equivalences of Koukpari's Exercise 2.B.4 and tom Dieck's §2.8.3: by steps [](#s1){.pf-ref} and [](#s2){.pf-ref} the coordinate sphere $S^{q-1}$ is a deformation retract of $S^{n-1}-S^{p-1}$, so its fundamental reduced homology class generates $\widetilde H_{q-1}$ there. For $q=1$ this class is the difference of the two points of $S^0$.

:::

:::

::: {.pf-step #collar}

Let $f:D^p\to D^n$ and $g:D^q\to D^n$ be disjoint embeddings with $f(\partial D^p)=S^{p-1}$ and $g(\partial D^q)=S^{q-1}$. Then $D^n$ contains disjoint embedded disks $\widehat D^p$ and $\widehat D^q$ with $\partial\widehat D^p=S^{p-1}$ and $\partial\widehat D^q=S^{q-1}$ which are proper, that is $\widehat D^p\cap S^{n-1}=S^{p-1}$ and $\widehat D^q\cap S^{n-1}=S^{q-1}$.

::: pf-proof
The argument of this step is the card's own: no published proof of part (b) was located.

Let $D_2$ be the closed ball of radius $2$ about the origin, so $D^n\subset D_2$. A point of $D^n$ has norm at most $1$, so an embedding whose boundary is $S^{p-1}$ extends to a proper disk in $D_2$.

::: {.pf-step #collar-extension}

The formula
$$
F(x)=\begin{cases} f(2x), & \norm x\le\tfrac12,\\[2pt] 2\norm x\, f\bigl(x/\norm x\bigr), & \tfrac12\le\norm x\le 1,\end{cases}
$$
defines an embedding $F:D^p\to D_2$ with $F(\partial D^p)=2S^{p-1}$ and $F(D^p)\cap\partial D_2=2S^{p-1}$.

::: pf-proof
The argument of this step is the card's own: no published proof of part (b) was located.

*Well defined.* For $\norm x\le\tfrac12$ the point $2x$ lies in $D^p$, so $F(x)\in f(D^p)\subset D^n$. For $\tfrac12\le\norm x\le1$ one has $x/\norm x\in\partial D^p$, so $f(x/\norm x)\in S^{p-1}$ has norm one and $\norm{F(x)}=2\norm x\in[1,2]$. At $\norm x=\tfrac12$ the two formulas coincide, since then $2x=x/\norm x$ and $2\norm x=1$. Both pieces are continuous and their domains are closed and cover $D^p$, so $F$ is continuous by the pasting lemma.

*Injective.* On the first piece $F=f\circ(2\,\cdot\,)$ is injective. On the second write $x=ru$ with $u\in\partial D^p$ and $\tfrac12\le r\le1$, so that $F(x)=2r\,f(u)$ and $\norm{F(x)}=2r$ because $\norm{f(u)}=1$; then $2r\,f(u)=2r'f(u')$ gives $r=r'$ and, by injectivity of $f$, $u=u'$. If $x$ is in the first piece and $x'$ in the second with $F(x)=F(x')$, then $\norm{F(x)}\le1$ and $\norm{F(x')}=2\norm{x'}\ge1$, so both equal $1$; hence $\norm{x'}=\tfrac12$ and $F(x')=f(x'/\norm{x'})=f(2x')$, while $F(x)=f(2x)$, and injectivity of $f$ gives $2x=2x'$, that is $x=x'$. So the two pieces agree on their overlap and nowhere else.

Since $D^p$ is compact and $D_2$ is Hausdorff, $F$ is an embedding. For $\norm x=1$ the second formula gives $F(x)=2f(x)$, so $F(\partial D^p)=2f(\partial D^p)=2S^{p-1}\subset\partial D_2$, and conversely an $F(x)$ of norm $2$ is either of norm at most $1$ from the first piece or has $\norm x=1$. The same construction applied to $g$, whose boundary is $S^{q-1}$, gives an embedding $G:D^q\to D_2$ with $G(\partial D^q)=2S^{q-1}$ and $G(D^q)\cap\partial D_2=2S^{q-1}$.

:::

:::

::: {.pf-step #collar-disjoint}

$F(D^p)\cap G(D^q)=\emptyset$.

::: pf-proof
The argument of this step is the card's own: no published proof of part (b) was located.

The inner pieces are $f(D^p)$ and $g(D^q)$, disjoint by hypothesis. The outer pieces are the cones
$$
\{ts: s\in S^{p-1},\ 1\le t\le2\},
\qquad
\{ts: s\in S^{q-1},\ 1\le t\le2\},
$$
which are disjoint because $S^{p-1}\cap S^{q-1}=\emptyset$. For an inner and an outer piece: a point of $f(D^p)$ lies in $D^n$ and so has norm at most $1$, while a point of the cone on $S^{q-1}$ has norm at least $1$; a common point therefore has norm exactly $1$, lies on $S^{n-1}$ and, being in the cone on $S^{q-1}$, lies on $S^{q-1}=g(\partial D^q)\subset g(D^q)$, contradicting the disjointness of $f(D^p)$ and $g(D^q)$. The same argument exchanges the roles of $F$ and $G$.

:::

:::

::: {.pf-step #collar-rescale}

After the scaling $y\mapsto y/2$, the disks $F(D^p)/2$ and $G(D^q)/2$ lie in $D^n$, are disjoint, have boundaries $S^{p-1}$ and $S^{q-1}$, and are proper.

::: pf-proof
The argument of this step is the card's own: no published proof of part (b) was located.

Dividing by $2$ maps $D_2$ onto $D^n$ and $\partial D_2$ onto $S^{n-1}$, and is a homeomorphism, so it preserves embedded disks and disjointness. By step [](#collar-extension){.pf-ref}, $F(D^p)\cap\partial D_2=2S^{p-1}$, so
$$
\bigl(F(D^p)/2\bigr)\cap S^{n-1}=S^{p-1}=\partial\bigl(F(D^p)/2\bigr),
$$
and likewise for $G(D^q)/2$ and $S^{q-1}$.

:::

:::

:::

:::

::: {.pf-step #proper-case}

There are no disjoint embeddings $f:D^p\to D^n$, $g:D^q\to D^n$ with $f(\partial D^p)=S^{p-1}$, $g(\partial D^q)=S^{q-1}$ and $f(D^p)\cap S^{n-1}=S^{p-1}$, $g(D^q)\cap S^{n-1}=S^{q-1}$.

::: pf-proof
The argument of this step is the card's own: no published proof of part (b) was located, and what it takes from §2.B Exercise 3  is the isomorphism of that exercise, proved on `E-HAT-2.B-3`.

Put $D=f(D^p)$ and $E=g(D^q)$. Exercise 3 of §2.B applies to the pair $(D,S^{p-1})\subset(D^n,S^{n-1})$, whose hypothesis $D\cap S^{n-1}=S^{p-1}$ holds by assumption, and says that $S^{n-1}-S^{p-1}\hookrightarrow D^n-D$ induces an isomorphism on homology. By step [](#s3){.pf-ref} the class $[S^{q-1}]$ generates the left-hand group in degree $q-1$, so its image generates $\widetilde H_{q-1}(D^n-D)$ and is nonzero. But $E=g(D^q)$ is homeomorphic to $D^q$, hence contractible, so $\widetilde H_{q-1}(E)=0$; the inclusion $S^{q-1}=\partial E\hookrightarrow D^n-D$ is the composite $\partial E\hookrightarrow E\hookrightarrow D^n-D$, so $[S^{q-1}]$ maps to zero in $\widetilde H_{q-1}(D^n-D)$. This contradicts the nonvanishing, so no such pair exists.

:::

:::

::: pf-step

Part (b) holds: no disjoint embeddings as in the exercise exist.

::: pf-proof

Suppose $f,g$ are as in the exercise. If $p=0$ or $q=0$ the claim is step [](#degenerate){.pf-ref}. Otherwise $p,q\ge1$, and by step [](#collar){.pf-ref} there are then disjoint disks $\widehat D^p,\widehat D^q\subset D^n$ with the same boundaries which are proper, while step [](#proper-case){.pf-ref} says no such pair of disks exists. So the assumption fails.

:::

:::

:::

:::

::: {.remark title="Sources"}
Hatcher, *Algebraic Topology* (2002), read in `tmp/sources/hatcher-2002-algebraic-topology.md`: the statement is Exercise 4 of §2.B, and it carries no hypothesis on the two disks beyond disjointness; its printed hint is Exercise 3 of §2.B, whose hypothesis $D\cap S^{n-1}=S$ is what step [](#collar){.pf-ref} arranges; Invariance of Domain is Theorem 2B.3.

Part (a) is transcribed from two published solutions.

**Tammo tom Dieck, *Algebraic Topology*, EMS Textbooks in Mathematics, European Mathematical Society 2008**, §2.8.3 "Complements of spheres", read in `tmp/sources/tomdieck-algebraic-topology-ranicki.md`. For $S_0^m=S^{m+n+1}\cap(\RR^{m+1}\times0)$ and $S_1^n=S^{m+n+1}\cap(0\times\RR^{n+1})$ it states that $X=S^{m+n+1}-S_1^n$ is homeomorphic to $S^m\times E^n$, displays the homeomorphism $(x,y)\mapsto(\sqrt{1-\norm y^2}\,x,y)$, and concludes that $X$ is $h$-equivalent to $S^m$. The exponent printed there in the target is one too small: the printed $y$ lies in the second block $\RR^{n+1}$ of the ambient $\RR^{m+n+2}$, and $(1-\norm y^2)+\norm y^2=1$ puts $(x,y)\mapsto(\sqrt{1-\norm y^2}\,x,y)$ on $S^{m+n+1}$, its image being the complement exactly for $\norm y<1$, so the statement is $S^m\times E^{n+1}$; nothing else in the passage is affected. With $(m,n)=(q-1,p-1)$ that is part (a) as printed, his first block being the last $q$ coordinates of the image and his second block the first $p$.

**Tiam Koukpari, *Hatcher's Algebraic Topology - Solutions*** (IMPA), solution to §2.B Exercise 4, read in `tmp/sources/koukpari-hatcher-solutions.md`. It displays the homeomorphism $\phi(u,v)=(v,u)/\sqrt{1+\norm v^2}$ from $S^{q-1}\times\RR^p$ onto $S^{p+q-1}-S^{p-1}$, checks that the image misses $S^{p-1}$ and that the denominator in it does not vanish, and reads the deformation retraction off $S^{q-1}\times\RR^p\to S^{q-1}\times\{0\}=S^{q-1}$. Both sources display $\phi$, and the inverse and the two composites in step [](#s1){.pf-ref} are the check this one leaves as evident.

Part (b) has no located published proof of the statement as printed, and its proof on this card is the card's own. Koukpari's solution to Exercise 2.B.4(b) assumes the inclusion $S^{p-1}=D^p\cap S^{p+q-1}$ as "the assumption of the question", which Hatcher's printed statement does not give, and under that hypothesis its ladder is the argument of step [](#proper-case){.pf-ref}. tom Dieck's §2.8.3 continues with the two standard circles in $S^3$, that $W=S^1\times\{0\}$ spans no disk in the complement of the axis $Z$ because it is a nonzero class in $\pi_1$ of that complement, which is the linking obstruction in its $\pi_1$ form and not the exercise. The one Math StackExchange thread on part (b), question 666444, carries a commutative-diagram sketch as its accepted answer and no complete argument. The published-solution obligation of issue #123 for part (b) therefore remains open, and `COMPLAINTS.md` records it on 2026-11-16 and again on 2026-11-20, the later entry carrying the queries run that day and their negative results.
:::
