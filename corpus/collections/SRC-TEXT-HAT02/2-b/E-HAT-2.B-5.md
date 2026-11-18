---



schema: qual/card@1
id: E-HAT-2.B-5
kind: problem
title: "Homology of complements of spheres in spheres"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 5, printed page
    176; the statement matches word for word. Checked: Alexander duality gives
    H̃_i(S^n − S) ≅ H̃^{n−i−1}(S^k) = Z exactly in degree r = n−k−1, matching
    H̃_*(S^r); the normal disk D^{n−k} meets S in one transverse point of the
    coordinate disk, so the Alexander-duality coordinate of the image of [S^r] is
    ±1 and the inclusion is an isomorphism in degree r and hence in all degrees,
    with the r = 0 case read on reduced H_0. No defect.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Added the omitted case k = n. Then the embedded n-sphere is all of S^n by
    invariance of domain, so S^{n-k-1} = S^{-1} and S^n - S are both empty and the
    inclusion is an isomorphism on homology. Alexander duality for a proper subsphere
    is now invoked only after reducing to k < n. The previous r = -1 calculation did
    not cover this case.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Rechecked all cases against Hatcher p.176 and Corollary 2B.4: k = n holds
    trivially, while for k < n the normal disk meets S in one transverse point, giving
    Alexander-duality coordinate plus or minus one for the image of the normal-sphere
    fundamental class. The r = 0 reduced-H_0 interpretation remains included.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Withdrew the added MSE 4773641 transcription as unverified. Independent review establishes
    that ell is the image of a half-sized open k-disk, not a closed subset, and that the omitted
    definitions of D and D' prevent checking excision and generalized Schoenflies. The previous
    text also repeated the thread's h'(S^k) notation although h' has domain D^n. The earlier
    Alexander-intersection proof and k=n case are unchanged; #105's complete-solution obligation
    for this card remains open. The excision condition is evaluated on closure_X(Z) and
    interior_X(A), not on interior of A minus Z; no counterexample based on the latter is
    asserted. Pairwise acyclicity of D and its ambient complement is not enough to deduce that
    the relative group vanishes in every degree, so the relative degrees still require checking
    before this source is accepted.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Added an independent second proof, step 4, following the answer to MSE 4773641 with each
    auxiliary set and each hypothesis checked, and supplying the generalized Schoenflies theorem
    that answer invokes. Checked: ell is the image of the half-sized open k-disk, hence an open
    k-disk in S and not an open subset of S^n when k < n, so the excision closure condition
    relative to X = S^n - D' is met through the ambient open set h'(int D^n) - h'(L), which is
    contained in D; D = h'(D^n - L) is contractible because the straight-line contraction of
    D^n - L to the origin stays outside L; D' = S - ell is a compact k-manifold with boundary by
    the coordinate chart, since the half-sized boundary sphere lies in h'(int D^k) and
    S meets h'(int D^n) in h'(int D^k) there, so Putman's Generalized Schoenflies Theorem makes
    D' a closed k-disk; Hatcher Proposition 2B.1(a), printed p. 169, then makes X acyclic; and in
    the exact sequence of the excised pair the inclusion-induced map
    H_j(D - ell) -> H_j(S^n - S) sits between two vanishing relative groups, so it is an
    isomorphism in every degree. Corrected in a forward commit: the earlier version called ell
    open in S^n, wrongly took S - Sigma to be ell disjoint-union D', and mislabelled the
    connecting map of the pair sequence as the inclusion isomorphism. Not checked and not claimed: the
    MSE thread is an unreviewed user answer rather than a peer-reviewed publication, so what is
    recorded is verification of its argument, not acceptance of the thread as a published
    solution; no use is made of the retracted interior-of-A-minus-Z condition. The
    Alexander-intersection proof, the k = n case and the statement are unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    The exercise is on printed p. 176. Its published proof is Putman, *The generalized Schoenflies theorem*, printed pp. 3--4 (Mazur's proof): a topological embedding $\varphi:S^{n-1}\to S^n$ whose image has a collar on one side bounds a ball. The card's use of it is checked: the intersection hypothesis gives $D'$ a collar on the side away from $\Sigma$, so Putman's theorem makes $D'$ a closed $k$-disk in $S^n$; Hatcher's Proposition 2B.1(a), printed p. 169 with its proof on pp. 169--170, then makes $X=S^n-D'$ acyclic, and the excision and Mayer--Vietoris steps of the card give the isomorphism. Checked against the book: the printed statement, the hypothesis on $D^n$, and the case $k=n$. Not claimed: a published solution of the exercise itself; the transcription is of Putman's theorem and of Hatcher's printed proposition, and the assembly between them is the card's own and is checked.
- event: source-checked
  by: claude
  date: 2026-11-13
  note: >-
    Re-read the printed statement for #123: the exercise is Exercise 5 of §2.B on printed p. 176,
    identical in the current online text, and the card states it word for word. The obligation that
    #123 records is unchanged and stays open: no published solution of this exercise was located.
    Putman is a published proof of the Schoenflies theorem used in the second proof, not of the
    exercise. Searched without result for the exercise itself in the retained sets (Sam, Li,
    DeMason, Poulsen, Stanford Math 215C Solution Sets 1--5, the UCR Math 205B help file, May,
    Bredon, Maxim's Math 752 notes) and in Hatcher's text and errata.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The citation of the second proof changed and one attribution is withdrawn. The step that
    isolates the two complementary disks cited "the answer to Math StackExchange question
    4773641"; that question now carries no answers at all (answer_count 0, read through the
    Stack Exchange API on 2026-11-16), so no answer there can be cited for the construction and
    the card no longer attributes it to one. The construction's one external input is now cited
    to a published book: Bredon, *Topology and Geometry*, Theorem 19.11 (Generalized Schoenflies
    Theorem), printed p. 236, proved on printed pp. 236--238 by Brown's argument, whose
    hypothesis (an embedding of $S^{k-1}\times[-1,1]$) is what the disk $D^n$ of the exercise
    supplies. The two complement computations the card takes from Hatcher's Proposition 2B.1 and
    from Alexander duality are also Bredon's Corollary 19.3 and Theorem 19.4, printed p. 233.
    Checked against the book: Hatcher's printed statement on p. 176, its hypothesis on $D^n$,
    the case $k=n$, and every step of the excision argument on the card. Not claimed: a
    published solution of Exercise 2.B.5; the retained solution sets contain none, recorded in
    COMPLAINTS.md item 11.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader batch. Three corrections, on the reader's report; the reader found no defect in
    the mathematics of either proof. (1) The construction of the second proof is the asker's own
    solution carried in the **body of the question** 4773641, not in an answer to it: the
    thread's `answer_count` is 0 (Stack Exchange API, 2026-11-16), and the question post
    defines $\ell$, $D$ and $D'$, uses excision and writes $h'(S^k)$. The step said the
    construction "was read in an answer", and the note of even date above rests on the same
    misreading; both are withdrawn. It remains a user post rather than a publication, and the
    card does not claim it as a published solution. The sentence inside the proof that read
    "the answer writes $h'(S^k)$ where $h(S^k)$ is meant" --- a dangling reference once the
    answer was withdrawn --- now reads "the question post writes". (2) Bredon's Theorem 19.11 is
    stated on printed p. 236 and its proof runs through printed **p. 239**, not p. 238; so the
    range "pp. 236--238" in the note above and in the remark is corrected to "pp. 236--239".
    Checked against the text layer of `tmp/sources/bredon-topology-and-geometry.pdf`: PDF
    page 131 carries printed pp. 236--237 with the statement and Lemmas 19.12--19.13, and PDF
    page 132 carries printed pp. 238--239 with Lemma 19.15, the main proof and the closing
    argument. (3) The step invoking the Schoenflies theorem called Bredon's hypothesis satisfied
    by the disk $D^n$ of the exercise, but what the theorem's hypothesis needs is a **bicollar
    of $\Sigma$ in $S$**, and the step had only shown that $D'$ is a manifold with boundary
    $\Sigma$, a one-sided collar. The bicollar is now written out: $\beta(h'(x),t)=h'((1+t/2)x)$
    for $\norm{x}=\tfrac12$ and $t\in[-1,1]$ is an embedding of $\Sigma\times[-1,1]$ into $S$
    onto $h'(\{\tfrac14\le\norm{x}\le\tfrac34\})\subset h'(\operatorname{int}D^k)$, so it lies in
    $S$ and restricts to the identity on $\Sigma\times\{0\}$. Also recorded: Hatcher read in
    `tmp/sources/hatcher-2002-algebraic-topology.md`; Putman and Bredon have no text versions in
    `tmp/sources` and were read in the text layer of their PDFs. Not claimed: a published
    solution of Exercise 2.B.5.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, second pass on this card: three repairs, none of them to the mathematics of
    the statement. (1) The `source-checked` note of 2026-11-13 says the exercise was searched for in
    "Stanford Math 215C Solution Sets 1--5"; `tmp/sources` holds Solution Sets 2, 3 and 4 only, so the
    range is corrected to 2--4. The same wrong range on `E-HAT-2.B-7`, `-2.C-1` and `-2.C-6` is
    corrected by a new event on each of those cards. (2) The remark said that "§2.1 supplies the
    collar" in Putman, which can be read as §2.1 of the notes; the collaring is **Theorem 2.1, in §2**,
    and it is what extends the embedding $\varphi$ to $\varphi:S^{n-1}\times[0,1]\to S^n$, as Putman
    uses it in his proofs of the theorem in §3 and §4. Read at printed p. 2 of
    `tmp/sources/putman-generalized-schoenflies.pdf`. (3) The intersection-number step of the first
    proof was heuristic: it asserted that Alexander duality's evaluation of the image of the normal
    sphere's fundamental class "is the intersection number", which is the linking-number description of
    the duality isomorphism and was never proved on the card. It is now stated as what it is --- the
    geometric account of which generator $[S^r]$ is, with $[S^r]=[\partial B]$ from the annulus of the
    normal disk and the intersection number computed as one transverse point --- and the nonvanishing
    that makes $[S^r]$ a generator is supplied by the independent second proof, step
    [](#schoenflies-pair){.pf-ref}, which is complete. So the exercise is proved on the card, the first
    route is kept as the book's duality computation with its one geometric assertion labelled, and
    nothing rests on an unproved evaluation. Checked against Hatcher (2002), the printed statement on
    p. 176 and Proposition 2B.1(a) on pp. 169--170. Not claimed: a published solution of Exercise
    2.B.5.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, third pass on this card: one false implication repaired. The step
    `#normal-generator` said that, the two reduced homology groups being $\ZZ$ in degree $r$, "it is
    enough that the class $[S^r]$ be nonzero ... and a nonzero class in a copy of $\ZZ$ is a
    generator". The implication is false: $2\in\ZZ$ is nonzero and generates the proper subgroup
    $2\ZZ$, so nonvanishing does not give generation. What the step needs is that the inclusion
    carries the fundamental class of $S^r$ to a generator, and that is what step `#schoenflies-pair`
    proves: the inclusion induces an isomorphism on homology in every degree. The two paragraphs are
    rewritten to say exactly that, and the duality route remains the geometric account of which
    generator it is, not the proof that it is one. Unchanged and re-checked: the statement as printed
    on p. 176, the second proof's excision and bicollar steps, and the first proof's label. Not
    claimed: a published solution of Exercise 2.B.5.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    #123 pass: Brown's paper, which Hatcher's §2.B points at, is now cited on this card for the
    flatness the second proof uses. Read this pass in the supplied text version
    `tmp/sources/brown-1960-generalized-schoenflies.md` (PDF beside it, three pages, printed page =
    PDF page): Theorem 5 on printed p. 76, "Let h be a homeomorphic embedding of $S^{n-1}\times I$
    into $S^n$. Then the closure of either complementary domain of $h(S^{n-1}\times 1/2)$ is an
    $n$-cell", which with $n=k$ is the step the bicollar $\beta$ feeds; and Theorem 0 on printed
    p. 74, the disk-complement statement under an inverse-set hypothesis. Checked in Hatcher that the
    pointer is at printed p. 169 ("See [Brown 1960] for a precise statement and proof"), in the
    paragraph after Proposition 2B.1. The paper's own cross-reference on printed p. 76 prints the
    first of those as "Theorem 0", and the extraction renders the numeral as the letter O. Checked:
    both theorem statements and both page numbers. Not checked: Brown's proofs of Theorems 1--5,
    which the card does not use; the card quotes Theorem 5's statement only. The homology isomorphism
    itself remains assembled on this card from Hatcher's Proposition 2B.1(a) and (b), printed
    pp. 169--170, with excision and Mayer--Vietoris, and Bredon's Theorem 19.11 remains cited as a
    second statement of the same theorem. Not claimed: a published solution of Exercise 2.B.5.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The owner's acceptance rule of this date applied, with the disposition the owner fixed for this
    card: Brown, Theorem 5, printed p. 76, is cited at the step that needs the flatness, and
    Hatcher's Proposition 2B.1(b), printed p. 169, at the step that computes the homology of the
    complement, with Proposition 2B.1(a) for the acyclicity of $S^n-D'$ in the second proof; the
    excision and Mayer--Vietoris assembly between them is marked as the card's own, and the remark
    says that no single source states the exercise. Brown is named first in the Schoenflies step's
    statement and in the application, with Bredon's Theorem 19.11, printed p. 236, as the same
    theorem. Checked this pass: both step statements, their page numbers, and the acyclicity step's
    citation. Not re-verified: Brown's proof of Theorem 5, whose statement is what the card uses.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    A false record corrected: the remark said that Putman and Bredon have no text versions in
    `tmp/sources` and were read in their PDFs' text layers. Putman's notes do have one,
    `tmp/sources/putman-generalized-schoenflies.md`, whose §3 "Schoenflies via infinite repetition"
    is Mazur's proof and carries Theorem 2.1; the remark now cites that text version. Bredon still
    has only the PDF, and the remark keeps the reading copy and the page arithmetic for it
    (PDF page 131 = printed pp. 236--237). Checked: the presence of the two files, and that the
    Putman text version contains §3 and Theorem 2.1. Not changed: any page number or argument.
---

::: {.problem}
Let $S$ be an embedded $k$-sphere in $S^n$ for which there exists a disk $D^n \subset S^n$ intersecting $S$ in the disk $D^k \subset D^n$ defined by the first $k$ coordinates of $D^n$.
Let $D^{n-k} \subset D^n$ be the disk defined by the last $n-k$ coordinates, with boundary sphere $S^{n-k-1}$.
Show that the inclusion $S^{n-k-1} \hookrightarrow S^n - S$ induces an isomorphism on homology groups.
:::

::: {.solution}
Put $r=n-k-1$.

::: pf

::: pf-step
If $k=n$, then the inclusion in the statement is an isomorphism on homology.

::: pf-proof
An embedded $n$-sphere in $S^n$ is all of $S^n$ by invariance of domain. Hence both $S^r=S^{-1}$ and $S^n-S$ are empty.
:::

:::

::: {.pf-step #complement-homology}
For $k<n$, both $S^r$ and $S^n-S$ have reduced homology $\ZZ$ in degree $r$ and zero in every other degree.

::: pf-proof
Now $r\ge0$, and Alexander duality for the embedded proper subsphere $S\cong S^k$, Theorem 3.44, printed p. 254 --- the same two values being what Proposition 2B.1(b), printed p. 169, gives for the complement of an embedded sphere --- gives
$$
\widetilde H_i(S^n\setminus S)\cong\widetilde H^{\,n-i-1}(S)
\cong
\begin{cases}\ZZ,&i=r,\\0,&i\ne r.\end{cases}
$$
The source sphere $S^r$ has the same reduced homology groups.
:::

:::

::: {.pf-step #normal-generator}
The image of the oriented fundamental class of $S^r$ is a generator of $\widetilde H_r(S^n\setminus S)$.

::: pf-proof
By step [](#complement-homology){.pf-ref} both reduced homology groups are $\ZZ$ in degree $r$ and zero elsewhere. What has to be shown is that the inclusion $S^r\hookrightarrow S^n-S$ carries the fundamental class of $S^r$ to a generator of $\widetilde H_r(S^n\setminus S)\cong\ZZ$; nonvanishing alone would not suffice, since $2\in\ZZ$ is nonzero and generates the proper subgroup $2\ZZ$.

That the class is a generator is proved, not asserted: step [](#schoenflies-pair){.pf-ref} below proves, without Alexander duality, that the inclusion $S^{n-k-1}\hookrightarrow S^n-S$ is an isomorphism on homology in every degree, so it carries the fundamental class of $S^r$ to a generator. What the duality route adds is which generator it is, and that is a statement about the pairing, not a step of the proof: inside the coordinate disk $D^n$ the normal disk $D^{n-k}$ meets $S\cap D^n=D^k$ in the single point $0$, which is interior to $D^{n-k}$, and $S^r=\partial D^{n-k}$. The concentric sphere $\partial B$ of radius $\tfrac12$ lies in $D^{n-k}$ and the annulus $\{\tfrac12\le\norm{x}\le1\}$ of the last $n-k$ coordinates joins the two spheres inside $D^{n-k}-\{0\}\subset S^n-S$, so $[S^r]=[\partial B]$ in $\widetilde H_r(S^n-S)$; the intersection number of $S$ with the disk $B$ is $\pm1$, one transverse point, which is the linking-number description of Alexander duality's coordinate of $[\partial B]$ under $\widetilde H_r(S^n-S)\cong\widetilde H^{\,k}(S)$, Theorem 3.44, printed p. 254. That description is stated here as the geometric account of the isomorphism and is not used as a step: the nonvanishing it reports is what the second route proves.
:::

:::

::: {.pf-step #schoenflies-pair}
A second proof, independent of Alexander duality and of any intersection number, cuts $S$ along an equatorial sphere into the two disks whose union it is and reaches the isomorphism through excision; its one external input is the generalized Schoenflies theorem for a bicollared sphere, M. Brown's Theorem 5, printed p. 76, the statement Hatcher's §2.B points at on printed p. 169 (Bredon's Theorem 19.11, printed p. 236 and proved on printed pp. 236--239, is the same theorem, proved by Brown's argument). The construction is the asker's own solution to Hatcher's exercise, carried in the body of Math StackExchange question 4773641 rather than in an answer --- that thread has no answers at all (`answer_count` 0, read through the Stack Exchange API on 2026-11-16) --- and it is a user post, not a publication, so every step below is checked directly.

::: pf-proof
Let $h\colon S^k\to S^n$ and $h'\colon D^n\to S^n$ be embeddings with $S=h(S^k)$ and $h'(D^n)\cap S=h'(D^k)$, the second being the hypothesis of the exercise. Put $\ell_0=\{x\in D^k:\norm{x}<\tfrac12\}$, $L=D^k\setminus\ell_0$, and
$$
\ell=h'(\ell_0),\qquad
D=h'(D^n\setminus L),\qquad
D'=h(S^k)\setminus\ell .
$$
Thus $L=\{x\in D^k:\tfrac12\le\norm{x}\le1\}$ is a closed shell and $D^k=L\sqcup\ell_0$. Since $h'(D^n)\cap S=h'(D^k)$, we have $D\cap S=h'(D^k\setminus L)=\ell$, so $D\cap D'=\varnothing$, and $(S^n\setminus D')\setminus\ell=S^n\setminus h(S^k)$. The question post writes $h'(S^k)$ where $h(S^k)$ is meant, since $h'$ has domain $D^n$.

$D$ is acyclic. A point of $D^n\setminus L$ whose last $n-k$ coordinates all vanish has its first $k$ coordinates in $\ell_0$. For a point with some last coordinate nonzero, every point of the segment joining it to $0$ except $0$ itself again has a nonzero last coordinate, hence lies outside $D^k\supseteq L$, while the whole segment lies in the convex set $D^n$. So the straight-line contraction of $D^n\setminus L$ to $0$ stays in $D^n\setminus L$, and $D$ is contractible.

For $k\ge1$, $D'$ is a closed $k$-disk. Let $\Sigma=h'(\{x\in\RR^k:\norm{x}=\tfrac12\})$, an embedded $(k-1)$-sphere in $S$ lying in $h'(D^k)$, and $\bar\ell=h'(\{x\in\RR^k:\norm{x}\le\tfrac12\})$. Then $S\setminus\Sigma=\ell\sqcup(S\setminus\bar\ell)$ and $D'\setminus\Sigma=S\setminus\bar\ell$, while $\Sigma\subseteq D'$, so $D'$ is not contained in $S\setminus\Sigma$. By Proposition 2B.1(b) applied in the $k$-sphere $S$, $\widetilde H_0(S\setminus\Sigma)\cong\ZZ$, and $S\setminus\Sigma$ is open in $S$ hence locally path connected, so it has exactly two components; as $\ell$ and $S\setminus\bar\ell$ are nonempty disjoint open sets covering it, they are those two components. Since $\norm{x}=\tfrac12$ on $\Sigma$ while $\norm{x}=1$ on $\partial D^n$, the compact set $\Sigma$ lies in $h'(\operatorname{int}D^k)$; and there $S$ agrees with the coordinate chart, because $h'(\operatorname{int}D^n)$ is open in $S^n$ by invariance of domain and
$$
S\cap h'(\operatorname{int}D^n)=h'(D^k)\cap h'(\operatorname{int}D^n)=h'(\operatorname{int}D^k).
$$
Hence $h'^{-1}$ carries $D'$ near $\Sigma$ to the closed half-space $\{x\in\operatorname{int}D^k:\norm{x}\ge\tfrac12\}$, whose boundary sphere $\{\norm{x}=\tfrac12\}$ maps onto $\Sigma$, while $D'\setminus\Sigma=S\setminus\bar\ell$ is open in $S$. Thus $D'=\overline{S\setminus\bar\ell}$ is a compact $k$-manifold with boundary $\Sigma$, namely the closure of that component of $S\setminus\Sigma$. That manifold hypothesis is not automatic --- for the non-simply-connected side of the Alexander horned sphere the corresponding closure is not a manifold --- but the coordinate chart supplies it here. $\Sigma$ is also bicollared in $S$: for $x$ with $\norm{x}=\tfrac12$ the formula $\beta(h'(x),t)=h'((1+\tfrac t2)x)$, $t\in[-1,1]$, defines an embedding $\beta:\Sigma\times[-1,1]\to S$ onto $h'(\{\tfrac14\le\norm{x}\le\tfrac34\})$, a subset of $h'(\operatorname{int}D^k)$ because $\tfrac34<1$ and $\tfrac14>0$, and $\beta(-,0)$ is the identity of $\Sigma$. That is the hypothesis Bredon's theorem asks for. For $k\ge2$ the Generalized Schoenflies Theorem (Brown, Theorem 5, printed p. 76; Bredon, *Topology and Geometry*, Theorem 19.11, printed p. 236, states it in the same bicollar form: for an embedding $S^{k-1}\times[-1,1]\to S^k$, the closure of each component of the complement of the embedded $S^{k-1}$ is homeomorphic to $D^k$), applied to the bicollar $\beta:\Sigma\times[-1,1]\to S\cong S^k$ and to the component $S\setminus\bar\ell$, whose closure is $D'$, then makes that closure a disk, so $D'\cong D^k$; for $k=1$, $S\cong S^1$, $\ell$ is an open interval and $D'$ a closed interval.

So $D'$ is an embedded closed $k$-disk in $S^n$, and Hatcher's Proposition 2B.1(a), printed p. 169, gives
$$
\widetilde H_i(S^n\setminus D')=0\qquad\text{for all }i .
$$
Set $X=S^n\setminus D'$ and $A=D$; then $X$ is path-connected and $A\ne\varnothing$. With $Z=\ell$ we have $Z\subset A\subset X$. The closure of $\ell$ in $S^n$ is $\bar\ell=\ell\cup\Sigma$ with $\Sigma\subseteq D'$, so $\overline Z^{\,X}=\ell$. Also $\ell$ lies in the ambient open set $U=h'(\operatorname{int}D^n)\setminus h'(L)$, which is contained in $D=A$: $h'(\operatorname{int}D^n)$ is open in $S^n$ because $h'$ is an open embedding on $\operatorname{int}D^n$ by invariance of domain, $h'(L)$ is compact hence closed in $S^n$, and $\ell\cap h'(L)=h'(\ell_0\cap L)=\varnothing$. Hence $\ell\subseteq\operatorname{int}_{S^n}(A)\subseteq\operatorname{int}_X(A)$. Note that $\ell$ is an open $k$-disk in $S$ and is not open in $S^n$ when $k<n$; the closure condition is met through the ambient neighbourhood $U$, not through $\ell$ itself. The hypothesis of Hatcher's excision theorem, Theorem 2.20, therefore holds, and excision gives isomorphisms in every degree
$$
H_j(X,A)\cong H_j\bigl((S^n\setminus D')\setminus\ell,\,D\setminus\ell\bigr)
=H_j\bigl(S^n\setminus h(S^k),\,h'(D^n\setminus D^k)\bigr),
$$
the right-hand side using $D'\cup\ell=S$ and $(D^n\setminus L)\setminus\ell_0=D^n\setminus D^k$.

Both $X$ and $A$ are acyclic, so the exact sequence of the pair $(X,A)$ gives $H_j(X,A)=0$ for $j>0$, and also $H_0(X,A)=0$ because $X$ is path-connected and $A\ne\varnothing$. Now $D\setminus\ell=h'(D^n\setminus D^k)$, and $D^n\setminus D^k$ deformation retracts onto $\{0\}^k\times S^{n-k-1}$: collapse the first $k$ coordinates to $0$, which keeps every point outside $D^k$ since its last coordinates stay nonzero, then push the last $n-k$ coordinates radially out to the unit sphere. Hence $D\setminus\ell$ is homotopy equivalent to the sphere $S^{n-k-1}$ of the statement. In the exact sequence of the excised pair
$$
\cdots\to H_j(S^n\setminus S,\,D\setminus\ell)\to H_{j-1}(D\setminus\ell)\xrightarrow{\ i_*\ }H_{j-1}(S^n\setminus S)\to H_{j-1}(S^n\setminus S,\,D\setminus\ell)\to\cdots
$$
both relative groups adjacent to $H_{j-1}(D\setminus\ell)\to H_{j-1}(S^n\setminus S)$ vanish, so the map $i_*$ induced by the inclusion $D\setminus\ell\hookrightarrow S^n\setminus S$ is an isomorphism in every degree, $j\ge1$ covering every degree. Composing $i_*$ with the homotopy equivalence of $D\setminus\ell$ with $S^{n-k-1}$, the inclusion $S^{n-k-1}\hookrightarrow S^n\setminus S$ induces an isomorphism on homology in every degree, which is the statement, reached without the Alexander-duality steps above.

For $k=0$ no Schoenflies theorem is needed: $D^0$ is a point, $L=\varnothing$, $D=h'(D^n)$, $\ell=h'(D^0)$, $S=S^0$, and $D'=S^0\setminus\ell$ is a single point, so $X=S^n\setminus D'\cong\RR^n$ is acyclic by Proposition 2B.1(a) itself, $D\setminus\ell=h'(D^n\setminus D^0)\simeq h'(\partial D^n)=S^{n-1}$, and both closure conditions hold because $\ell$ lies in the $S^n$-open set $h'(\operatorname{int}D^n)\subseteq D$.
:::

:::

::: pf-step
By the Alexander-duality route of steps [](#complement-homology){.pf-ref} and [](#normal-generator){.pf-ref}, the inclusion induces an isomorphism on reduced homology in every degree, and also on ordinary $H_0$.

::: pf-proof
For $k<n$, step [](#complement-homology){.pf-ref} leaves only degree $r$ to check, and step [](#normal-generator){.pf-ref} shows that the inclusion sends a generator to a generator. For $r=0$, the oriented fundamental class of $S^0$ is the difference of its two points, so the same local intersection calculation applies in reduced $H_0$. Reduced homology determines ordinary homology in positive degrees and determines ordinary $H_0$ here since both spaces are nonempty. The case $k=n$ was already verified directly.
:::

:::

:::
:::

::: {.remark title="Source"}
Andrew Putman, *The generalized Schoenflies theorem*, printed p. 1 and §3, printed pp. 3--4, of `tmp/sources/putman-generalized-schoenflies.pdf`: for a topological embedding $\varphi:S^{n-1}\to S^n$ with $n\ge2$ whose image bounds a component whose closure $A$ is a manifold with boundary, $A\cong D^n$ (Mazur's proof is §3, printed pp. 3--4; it is Theorem 2.1, in §2, that extends $\varphi$ to an embedding $S^{n-1}\times[0,1]\to S^n$ and so supplies the collar such an $A$ has), together with Hatcher, *Algebraic Topology* (2002), Proposition 2B.1(a) and its printed proof, pp. 169--170, read in `tmp/sources/hatcher-2002-algebraic-topology.md`. The exercise is Exercise 5 of §2.B, printed p. 176; the disk $D^n$ supplies the collar Putman's theorem needs, and Hatcher's (a) is what makes $X=S^n-D'$ acyclic.

Brown's theorem is the one Hatcher's §2.B points at, and it is the statement the second proof's collaring uses. Hatcher, §2.B, printed p. 169, read in `tmp/sources/hatcher-2002-algebraic-topology.md`: "it is known that any locally nicely embedded $S^{n-1}$ in $S^n$ is equivalent to the standard $S^{n-1}\subset S^n$ ... In particular, both complementary regions are homeomorphic to open balls. See [Brown 1960] for a precise statement and proof." M. Brown, *A proof of the generalized Schoenflies theorem*, Bull. Amer. Math. Soc. 66 (1960), 74--76, read in `tmp/sources/brown-1960-generalized-schoenflies.md` with its PDF beside it, three pages, so printed page and PDF page agree here (74, 75, 76): Theorem 5, printed p. 76, "Let $h$ be a homeomorphic embedding of $S^{n-1}\times I$ into $S^n$. Then the closure of either complementary domain of $h(S^{n-1}\times 1/2)$ is an $n$-cell", which with $n=k$ is exactly the step the bicollar $\beta:\Sigma\times[-1,1]\to S\cong S^k$ feeds into the second proof; and Theorem 0, printed p. 74, the disk-complement statement under the hypothesis that the map has finitely many inverse sets, from which Theorems 1--5 are derived (the extraction prints that numeral as the letter O, and the paper's own cross-reference on printed p. 76 prints it as "Theorem 0"). Bredon's Theorem 19.11 states the same theorem and follows Brown's argument, so either may be cited for it. Brown's paper does not do the exercise, and neither does any single source: what the card records is two citations, each attached to the step it decides --- Brown's Theorem 5, printed p. 76, for the flatness that makes $D'$ a disk, and Hatcher's Proposition 2B.1(b), printed p. 169 (equivalently Corollary 19.3 and Theorem 19.4 of Bredon, printed p. 233), for the homology of the complements, with Proposition 2B.1(a) for the acyclicity of $S^n-D'$ in the second proof. The excision and Mayer--Vietoris assembly between them is the card's own and is marked as such.

The input quoted for the second proof is Bredon, *Topology and Geometry*, Theorem 19.11 (Generalized Schoenflies Theorem), printed p. 236, whose proof occupies printed pp. 236--239 and follows M. Brown's argument; it needs an embedding $S^{k-1}\times[-1,1]\to S^k$, which the bicollar $\beta$ of $\Sigma$ in the proof supplies. The same section proves, by Mayer--Vietoris induction and without duality, the two complement computations this card uses: Corollary 19.3, printed p. 233, that $S^n-f(D^r)$ has trivial reduced homology for an embedding $f:D^r\to S^n$, and Theorem 19.4 (Generalized Jordan Curve Theorem), printed p. 233, that $\widetilde H_i(S^n-f(S^r))=\ZZ$ for $i=n-r-1$ and $0$ otherwise. Those are Hatcher's Proposition 2B.1(a) and (b), printed pp. 169--170, so either book may be cited for them; Putman's notes are a second published proof of the Schoenflies input, read in the text version `tmp/sources/putman-generalized-schoenflies.md` (its §3, "Schoenflies via infinite repetition", is Mazur's proof; the PDF is beside it). Bredon has no text version in `tmp/sources` and was read in the text layer of `tmp/sources/bredon-topology-and-geometry.pdf`, PDF page 131 = printed pp. 236--237.
:::
