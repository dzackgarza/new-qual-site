---
schema: qual/card@1
id: P-AGH536ANALYTICEQUIV
kind: problem
title: Analytic isomorphism of curve singularities versus equivalence
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.3.6, the retained Egbert companion note, the earlier
    analytic-isomorphism exercise, and the local plane-singularity material.
    The retained source cites Wall for the equivalence between the Puiseux
    resolution data and Hartshorne's V.3.9.4 equivalence, and gives the
    standard counterexample y^3+x^7 and y^3+x^5 y+x^7. The forward
    implication is made intrinsic below by lifting an isomorphism of complete
    plane-curve local rings to a formal ambient automorphism and iterating
    blowups. For the counterexample, both branches have the single Puiseux
    pair (3,7), while their Tjurina numbers are 12 and 11.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.3,
    exercise 3.6, printed page 395, together with Remark 3.9.4 on printed page
    408, where equivalence is defined by matching monoidal transformations,
    multiplicities and incidence of the total transforms. Checked the card's
    forward step against that definition, and recomputed both Tjurina numbers:
    tau(y^3+x^7) = dim k[[x,y]]/(x^6,y^2) = 12, and for y^3+x^5y+x^7 the ideal
    reduces to (y^2+x^5/3, x^4y+7x^6/5, x^7) with standard monomials
    1,x,...,x^6,y,xy,x^2y,x^3y, so tau = 11; the Groebner basis claim was
    checked by hand on the three S-polynomials. Searched outside the twelve
    retained sets: Yang Pi-Yeh, Hartshorne Solutions, exercise 5.3.6, printed
    p. 108 (tmp/sources/lfwin-hartshorne-solutions.pdf), has the completion
    argument and asserts the counterexample without computation; Algebraic
    Geometry II, National Taiwan University, 2020 Spring, has no entry for
    Exercise 6 of section 3. Wall's Singular Points of Plane Curves was searched
    for and is a book, not downloaded; its Puiseux criterion is cited as
    printed. Not checked: the Puiseux characteristic of C_1 and C_2 beyond the
    leading pair (3,7), which the card computes by the implicit-function
    theorem for C_2 and by an explicit parametrization for C_1.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The text version of the NTU Chapter V homework now exists: it is read in
    tmp/sources/ntu-ag2-chapter5.pdf and in its MinerU text version
    tmp/sources/ntu-ag2-chapter5.md. The event above predates that file, records
    what was read from the PDF alone, and is left as it was dated.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.3,
    exercise 3.6, printed p. 395, and Remark 3.9.4 in the text version
    tmp/sources/hartshorne-1977-algebraic-geometry.md, whose page markers name
    PDF pages: the remark sits between the markers PDF page 408 and PDF page
    409, so printed p. 393, while exercise 3.6 follows the marker PDF page 410,
    printed p. 395. The event of 2026-11-11 above gives 408 for the remark,
    which is its PDF page; the published-solution remark below has been
    corrected to printed p. 393, and that event is left as dated. Recomputed
    both blowup chains, giving the two second strict transforms x+y''^3 and
    x(1+y'')+y''^3, and both Tjurina numbers: 12 from the ideal (x^6,y^2), and
    11 from the Groebner basis y^2+x^5/3, x^4y+7x^6/5, x^7 with standard
    monomials 1,x,...,x^6,y,xy,x^2y,x^3y, whose three S-polynomials reduce to
    zero. Corrected step c1-c2-equivalent: the two point blowups leave the
    strict transform nonsingular but tangent to E_2 with contact order 3, so the
    reduced total transform is not a normal crossing divisor and the two
    sequences are not embedded resolutions; equivalence in the sense of (3.9.4)
    rests instead on the two pairs at the last point being one pair, x = -y^3
    against x = 0, the factor 1+y'' being a unit removed by the coordinate
    change x -> x(1+y''). Corrected the word inequivalence to non-isomorphism in
    the last remark, the two germs being equivalent. Checked Yang Pi-Yeh, text
    version tmp/sources/lfwin-hartshorne-solutions.md, exercise 5.3.6, printed
    p. 108, which gives the forward implication by completion and asserts the
    counterexample with no computation. Also checked that the text version of
    Egbert, tmp/sources/hartshorne-solutions-egbert.md, exercise V.3.6, is the
    citation of Wall recorded on the card. Not checked: Wall's Singular Points
    of Plane Curves, which is not held and is cited as printed; and the National
    Taiwan University Chapter V homework, which has no entry for this exercise.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, fifth pass: the second occurrence of
    "inequivalence" in the published-solution remark. The 2026-11-16 event
    above records the correction of that word to non-isomorphism in the last
    remark; the same remark carried it a second time, "the inequivalence that
    he asserts is step not-analytically-isomorphic", where what the source
    asserts is non-isomorphism after equivalence, Egbert's two curves being
    equisingular and not analytically isomorphic. The remark now reads "the
    failure of analytic isomorphism that he asserts". No step, page or proof
    changes, and nothing was re-read in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, second pass: the published-solution remark
    ended with the sentence "Recorded in COMPLAINTS.", a pointer to the work
    record of the search rather than anything about the source. It is removed
    (PROSE-11, QUAL-08), and the remark ends with what Egbert's entry contains
    and which steps carry it. The search it pointed at is the entry for V.3.6
    in COMPLAINTS.md, which records it. No mathematical claim changes, and the
    statement, the steps, the pages and the citations are as they were. Not
    checked: nothing new; the proofs were not re-derived in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, third pass: the remark on Wall's book carried the
    book's availability on this machine and the history of which step stopped needing it
    --- that it is not in tmp/sources, that only its recorded statement is used, and that
    an earlier form of the proof wanted it where the card now proves the equivalence
    directly. A rendered remark carries neither (PROSE-11, QUAL-08). The paragraph now
    states what Wall's book says, that step c1-c2-equivalent does not use it, and that the
    non-isomorphism half is step not-analytically-isomorphic. Both facts are recorded in
    COMPLAINTS.md's V.3.6 entry, which says the book is not among the retained files. No
    mathematical claim changes, and nothing was re-read in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The same reader's finding, in the two places the event above did not reach. The
    solution's Puiseux step called Wall's book "the retained source for V.3.6", and the
    Egbert paragraph said the book "is not among the retained files, so both halves are
    citations". Which files this machine holds is no part of either statement
    (PROSE-11, QUAL-08). The step now attributes the theorem to Wall's book and records
    that Egbert's entry cites it; the Egbert paragraph says both halves rest on Wall's
    account as Egbert reports it. No mathematical claim changes, and nothing was re-read
    in this pass.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Transcribed for issue #121 from Greuel, Lossen and Shustin, Introduction to
    Singularities and Deformations (2007), §3.4, read in the text version
    tmp/sources/greuel-lossen-shustin-2007-singularities-deformations-pp200-220.md,
    whose marker names PDF pages 211-230 against the printed pages of its file
    name, so printed page = marker - 11; that offset was checked against the
    retained PDF page by page, Definition 3.30 sitting on printed p. 202 with
    its running head "202 I Singularity Theory", Theorem 3.42 on printed
    p. 217, Example 3.43.1(a) on printed p. 218 and Remark 3.43.3 on printed
    p. 219. What the source proves, and what is now on the card: Definition
    3.30 on printed p. 202, analytic and topological equivalence side by side,
    with analytic implying topological; Theorem 3.42 on printed p. 217 of
    Brauner and Zariski, topological type determined by and determining the
    system of multiplicity sequences defined on printed p. 216; Proposition
    3.41 on printed pp. 216-217, that data equal to the characteristic
    exponents with the pairwise intersection numbers, which replaces the
    card's earlier citation of Wall's Singular Points of Plane Curves, a book
    not held and not read; Example 3.43.1(a) on printed p. 218, the pair
    y^3-x^7 and y^3+x^5y-x^7 with multiplicity sequence 3,3,1,1,1 and the two
    Tjurina numbers 12 and 11 printed as Singular output; and Remark 3.43.3 on
    printed p. 219, that the Tjurina number is an analytic invariant. The
    substitution (x,y) -> (x,-y) carries the source's pair to the card's,
    y^3+x^7 and y^3+x^5y+x^7, up to the unit -1, which is recorded on step
    same-multiplicity-sequence. Left on the card as its own, and recorded in
    COMPLAINTS.md: the passage from that data to equivalence in the sense of
    (3.9.4), which the source does not make --- it lists the resolution graph
    as further data equivalent to the system of multiplicity sequences on
    printed p. 216 but proves the equivalence only for the Puiseux pairs and
    the characteristic exponents --- so steps ambient-automorphism-lift,
    automorphism-identifies-resolution-data and c1-c2-equivalent remain the
    card's argument; and the formal form of the Tjurina invariance, the source
    stating it for analytic equivalence of germs while the exercise's notion
    is isomorphism of completed local rings. Checked against Hartshorne
    (I, 5.6.1) and the definition before it, printed p. 34, (3.9.3) and
    (3.9.4) on printed p. 393, and exercise 3.6 on printed p. 395. Not
    checked: Wall's book, still not held; the printed copies of Greuel-Lossen-
    Shustin, only the text version beside the retained PDF being read; and the
    cross-reference to Proposition 3.21 of that book, cited inside Proposition
    3.41's proof and not read here.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Page correction to the event above, which is left as written. The system of
    multiplicity sequences is defined on printed p. 215, not p. 216: in the
    retained PDF of Greuel-Lossen-Shustin the paragraph "System of
    Multiplicity Sequences" opens PDF p. 226, whose running head reads 215,
    while printed p. 216 carries the list of further data equivalent to it and
    Proposition 3.41. The step topological-type-multiplicity-sequences and the
    remark now say p. 215; what the event above records at p. 216 --- the list
    naming the resolution graph, the Puiseux pairs, the characteristic
    exponents and the iterated torus knots --- keeps that page, so its argument
    about what the source leaves unproved is unaffected. Nothing else changes:
    Theorem 3.42 remains on printed p. 217, Definition 3.30 on p. 202, Example
    3.43.1(a) on p. 218 and Remark 3.43.3 on p. 219.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's findings on this batch, repaired here; the events of 2026-11-16
    above are left as written. The Puiseux computation for the two germs was
    carried inside the step that transcribes Greuel-Lossen-Shustin's Example
    3.43.1(a), which gives the multiplicity sequence 3,3,1,1,1 and no
    characteristic exponents; it is now its own step puiseux-pair, with the
    parametrisation for the first germ, the implicit-function argument for the
    second, and the remark that Proposition 3.41 is what ties the pair (3,7) to
    the multiplicity sequence. No cited source computes that pair, and
    COMPLAINTS.md now says so. The rendered text is reduced to mathematics and
    citation (QUAL-08): the sentences saying that a passage is not in the cited
    pages and that given steps carry it, that the topological statements are the
    source's, that a value is computed rather than quoted, and which books were
    or were not read, leave the solution and the remark. The remark opener takes
    the attribute form of STYLE-01.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's findings on the second round of this batch, repaired here; every
    event above is left as written. The pass above removed every mark of the
    card's own argument from the rendered steps together with the process text
    (QUAL-08), and the marks are put back where the step is not the source's:
    steps ambient-automorphism-lift, automorphism-identifies-resolution-data,
    puiseux-pair and c1-c2-equivalent now say in the step that they are the
    card's own, and the sentence introducing the argument of
    tjurina-number-invariant says the same of it, the statement of invariance
    being Greuel-Lossen-Shustin's Remark 3.43.3 on printed p. 219 while the
    form of it the exercise uses is the card's. No statement, page, citation or
    mathematical claim changes, and no proof is added: the marks record whose
    argument each step is, and what no located source proves is recorded in
    COMPLAINTS.md. Re-read for this pass in the text version
    tmp/sources/greuel-lossen-shustin-2007-singularities-deformations-pp200-220.md:
    Definition 3.30, the paragraph naming the system of multiplicity sequences,
    Proposition 3.41, Theorem 3.42, Example 3.43.1(a) and Remark 3.43.3. That
    file's markers name the range "PDF pages 211-230" only, so the printed
    pages were located in the retained PDF, where the folios read 202, 215,
    216, 217, 218 and 219, that is printed page = PDF page - 11, and they
    agree with the pages the events above give. Not read here: Wall's
    Singular Points of Plane Curves, still not held;
    Greuel-Lossen-Shustin's Proposition 3.21, cited inside Proposition 3.41's
    proof; and Yang Pi-Yeh's and Egbert's entries, which the previous passes
    read and which were not re-read this pass.
---

::: {.problem}
Show that analytically isomorphic curve singularities (I, 5.6.1) are equivalent in the sense of (3.9.4), but not conversely.
:::

::: {.solution}
The exercise has two halves: analytic isomorphism implies equivalence in the sense of (3.9.4), and equivalence does not imply analytic isomorphism.

Greuel, Lossen and Shustin, *Introduction to Singularities and Deformations* (2007), §3.4, supply the frame of both. Their Definition 3.30, distinguishes analytic from topological equivalence of a germ; their Theorem 3.42, a theorem of Brauner and Zariski, says that the topological type of a reduced plane curve singularity is determined by, and determines, the system of multiplicity sequences; their Proposition 3.41, identifies that data with the characteristic exponents of the branches and their pairwise intersection numbers; their Example 3.43.1(a), is a pair with equal multiplicity sequence and different analytic type, separated by Tjurina numbers; and their Remark 3.43.3, records that the Tjurina number is an analytic invariant.

Hartshorne's equivalence is stated in terms of embedded resolutions, so the forward implication needs the blowup of a point to be carried along by an isomorphism of completed local rings, which steps [](#ambient-automorphism-lift){.pf-ref} and [](#automorphism-identifies-resolution-data){.pf-ref} supply, and the example needs embedded resolutions that correspond, which step [](#c1-c2-equivalent){.pf-ref} exhibits.

::: pf

::: {.pf-step #analytic-implies-topological}
An analytic isomorphism of plane curve germs is a homeomorphism of the ambient germs carrying one curve onto the other, so analytically equivalent germs are topologically equivalent, and every topological invariant is an analytic one.

::: pf-proof
This is Greuel--Lossen--Shustin, Definition 3.30, which defines the two notions side by side for germs of isolated hypersurface singularities: $(X,z)$ and $(Y,w)$ are *analytically equivalent*, or contact equivalent, if there is a local analytic isomorphism $(\CC^n,z)\to(\CC^n,w)$ carrying one to the other, and *topologically equivalent* if there is a homeomorphism of the ambient germs doing so; a number attached to a singularity is an analytic, respectively topological, invariant when it does not change its value within that class. A local analytic isomorphism is a homeomorphism, so the first class is contained in the second.

The exercise's own notion is the one Hartshorne states just before (I, 5.6.1), where $P\in X$ and $Q\in Y$ are analytically isomorphic if their completed local rings are isomorphic as $k$-algebras; for a plane curve singularity the completed local ring is $k[[x,y]]/(f)$. The two formal steps that follow prove the forward implication for this notion of analytic isomorphism itself.
:::

:::

::: {.pf-step #topological-type-multiplicity-sequences}
Two reduced plane curve singularities are topologically equivalent if and only if they have the same system of multiplicity sequences. Hence analytically isomorphic plane curve singularities have the same system of multiplicity sequences.

::: pf-proof
This is Greuel--Lossen--Shustin, Theorem 3.42, a result they attribute to Brauner and Zariski. The system of multiplicity sequences is defined in the paragraph headed "System of Multiplicity Sequences" that precedes Proposition 3.41: for an irreducible germ it is the sequence
$$
(m_0,m_1,\ldots,m_{n-1}),\qquad m_0=\mu_0(C),\quad m_i=\mu_{q^{(i)}}(C^{(i)}),
$$
where $q^{(i)}$ is the unique point in which the $i$-th strict transform meets the $i$-th exceptional curve, and $m_n=1$; for a germ with branches $(C_1,0),\ldots,(C_r,0)$ it is their extended multiplicity sequences together with, for each level $i\ge0$, the partition $\mathcal P_i$ of $\{(1,i),\ldots,(r,i)\}$ whose classes are the branches whose strict transforms still meet at level $i$. With step [](#analytic-implies-topological){.pf-ref}, an analytic isomorphism forces equality of this data.
:::

:::

::: {.pf-step #characteristic-exponents}
The system of multiplicity sequences is determined by, and determines, the characteristic exponents of the branches together with their pairwise intersection numbers.

::: pf-proof
This is Greuel--Lossen--Shustin, Proposition 3.41, whose induction step is that the characteristic exponents of a blown-up branch, and its intersection number with the exceptional curve, are determined by the characteristic exponents of the branch; the partitions are determined by the pairwise intersection numbers by Proposition 3.21 of the same book, and conversely. The paragraph preceding Proposition 3.41 that begins "There are many data equivalent to the system of multiplicity sequences" lists the resolution graph, the Puiseux pairs with the pairwise intersection numbers, the characteristic exponents with those numbers, and the iterated torus knots as further data equivalent to the system of multiplicity sequences, and proves the equivalence only for the Puiseux pairs and the characteristic exponents, Proposition 3.41 being that proof.
:::

:::

::: {.pf-step #ambient-automorphism-lift}
Let
$$
A_f=k[[x,y]]/(f),
\qquad
A_g=k[[x,y]]/(g)
$$
be two singular plane-curve complete local rings. Any analytic isomorphism
$$
A_f\xrightarrow{\sim}A_g
$$
lifts to an automorphism
$$
\Phi:k[[x,y]]\xrightarrow{\sim}k[[x,y]]
$$
such that
$$
\Phi(f)=u g
$$
for a unit $u\in k[[x,y]]^\times$.

::: pf-proof
An analytic isomorphism is, by (I, 5.6.1), an isomorphism of completed local
rings. Choose lifts $X,Y\in k[[x,y]]$ of the images of the residue classes
of $x,y$ under the isomorphism. Since the induced map on cotangent spaces
$$
\mathfrak m_f/\mathfrak m_f^2
\longrightarrow
\mathfrak m_g/\mathfrak m_g^2
$$
is an isomorphism, the linear parts of $X,Y$ are linearly independent.
The formal inverse-function theorem therefore makes
$$
x\longmapsto X,
\qquad
y\longmapsto Y
$$
an automorphism $\Phi$ of $k[[x,y]]$ lifting the given quotient-ring
isomorphism.

The kernel of the quotient map to $A_f$ is the principal ideal $(f)$, and
the kernel on the other side is $(g)$. Hence
$$
\Phi((f))=(g).
$$
Two generators of the same principal ideal in the domain $k[[x,y]]$ differ
by a unit, so
$$
\Phi(f)=ug.
$$

This step is the card's own.
:::

:::

::: {.pf-step #automorphism-identifies-resolution-data}
A formal ambient automorphism as in step [](#ambient-automorphism-lift){.pf-ref} identifies the complete
embedded resolution data obtained by successive point blowups.

::: pf-proof
The automorphism $\Phi$ carries the maximal ideal $(x,y)$ to itself and
identifies the two curve ideals. The blowup of the closed point is the
Proj of the Rees algebra of this maximal ideal. Therefore $\Phi$ induces an
isomorphism of the two formal blowups carrying exceptional divisor to
exceptional divisor and strict transform to strict transform.

At every point where a further blowup is required, the induced isomorphism
of completed local rings again identifies the maximal ideals and the strict
transform ideals. Applying the same Rees-algebra construction recursively
identifies the next blowups. Thus the entire sequence of infinitely near
points, exceptional components, branch incidences, proximity relations, and
multiplicities is preserved.

This is precisely the embedded-resolution data entering equivalence in
(3.9.4). Hence analytically isomorphic curve singularities are
equivalent, which is the forward implication of the exercise.

This step is the card's own.
:::

:::

::: {.pf-step #same-multiplicity-sequence}
Over $k=\CC$ the two irreducible germs
$$
C_1:\quad f_1=y^3+x^7=0,
\qquad
C_2:\quad f_2=y^3+x^5y+x^7=0
$$
have the same multiplicity sequence
$$
\boxed{3\longrightarrow3\longrightarrow1\longrightarrow1\longrightarrow1}.
$$

::: pf-proof
Greuel--Lossen--Shustin, Example 3.43.1(a), take $f=y^3-x^7$ and $g\in I=\langle x^\alpha y^\beta\mid3\alpha+7\beta>21\rangle$ and record that "in both cases the multiplicity sequence reads $3\longrightarrow3\longrightarrow1\longrightarrow1\longrightarrow1$". The monomial $x^5y$ satisfies $3\cdot5+7\cdot1=22>21$, so $f+x^5y$ is one of those $f+g$, and the substitution $(x,y)\mapsto(x,-y)$ carries $y^3-x^7$ to $-(y^3+x^7)$ and $y^3+x^5y-x^7$ to $-(y^3+x^5y+x^7)$; a unit multiple of the defining equation is the same germ.
:::

:::

::: {.pf-step #puiseux-pair}
Each of the two germs is a single branch with characteristic exponents $(3,7)$.

::: pf-proof
$C_1$ has the parametrization $x=t^3$, $y=-t^7$, so its branch has characteristic pair $(3,7)$. For $C_2$ substitute $x=t^3$ and $y=t^7z(t)$; the equation becomes
$$
t^{21}\bigl(z^3+tz+1\bigr)=0,
$$
and $z^3+1=0$ has the root $z=-1$ at $t=0$ with
$$
\frac{\partial}{\partial z}(z^3+tz+1)\evalfrom_{(0,-1)}=3\ne0,
$$
so the formal implicit-function theorem gives $z(t)\in\CC[[t]]$ with $z(0)=-1$ and $z^3+tz+1=0$, that is $y=-t^7$ plus higher-order terms. Since $\gcd(3,7)=1$ the gcd of the characteristic exponents has dropped to $1$ at the exponent $7$, so there is no further Puiseux pair, and the three choices of cube root of $-1$ give the same branch after $t\mapsto\zeta t$ with $\zeta^3=1$. Thus $C_2$ is irreducible with the single Puiseux pair $(3,7)$ as well, and by Proposition 3.41 the pair is what the multiplicity sequence $3,3,1,1,1$ of step [](#same-multiplicity-sequence){.pf-ref} encodes.

This step is the card's own.
:::

:::

::: {.pf-step #c1-c2-equivalent}
The singularities $C_1$ and $C_2$ are equivalent in the sense of
(3.9.4).

::: pf-proof
Two point blowups at the origin and at the point over it give, for each germ,
the same data, so step [](#characteristic-exponents){.pf-ref} is not needed
here.

Both equations have order $3$ with tangent cone $y^3$, so after the blowup of
the origin only the chart $y=xy^{\prime}$ meets the strict transforms, and
there
$$
f_1=y^3+x^7\ \mapsto\ x^3\bigl(y^{\prime 3}+x^4\bigr),
\qquad
f_2=y^3+x^5y+x^7\ \mapsto\ x^3\bigl(y^{\prime 3}+x^3y^{\prime}+x^4\bigr).
$$
Each strict transform has multiplicity $3$ at its point $(0,0)$ on the
exceptional curve $E_1$, and each has tangent cone $y^{\prime 3}$, so the
second blowup is again taken at that one point and again in the chart
$y^{\prime}=xy^{\prime\prime}$:
$$
y^{\prime 3}+x^4\ \mapsto\ x^3\bigl(y^{\prime\prime 3}+x\bigr),
\qquad
y^{\prime 3}+x^3y^{\prime}+x^4\ \mapsto\ x^3\bigl(y^{\prime\prime 3}+xy^{\prime\prime}+x\bigr).
$$
Both second strict transforms are nonsingular at the origin --- the partial
derivative with respect to $x$ is $1$ there in the first case and
$y^{\prime\prime}+1$ in the second --- and each meets the new exceptional curve
$E_2$ in the single point $y^{\prime\prime}=0$ with multiplicity $3$, being
tangent to it. So the reduced total transform is not a divisor with normal
crossings, and these two point blowups, while they do resolve both germs, are
not yet embedded resolutions.

What they do give is one and the same pair at the last point. Read in the chart
$y^{\prime}=xy^{\prime\prime}$ and written as equations in $x$ and
$y^{\prime\prime}$, the second strict transforms are
$$
x+y^{\prime\prime 3}
\qquad\text{and}\qquad
x\,(1+y^{\prime\prime})+y^{\prime\prime 3},
$$
the first for $C_1$ and the second for $C_2$, and the new exceptional curve is
$E_2:x=0$ in both cases. Since $1+y^{\prime\prime}$ is a unit at the origin,
$$
x\longmapsto x\,(1+y^{\prime\prime}),
\qquad
y^{\prime\prime}\longmapsto y^{\prime\prime}
$$
is an automorphism of the affine plane near the origin --- its inverse is
$x\mapsto x/(1+y^{\prime\prime})$ --- which carries the line $x=0$ to itself
and the second equation to the first. Both germs therefore present the same pair
at the last point, $x=-y^{\prime\prime 3}$ against $x=0$.

A monoidal transformation is local: the blowup of a point depends only on the
maximal ideal there, and the strict transform only on the local equations of the
curve and of the exceptional curves. So from that point on the two germs are
blown up at corresponding points, with the same multiplicities and the same
incidence with the exceptional curves already present. Blowing up until the total
transform is a normal crossing divisor therefore gives for the two germs the
same components ($E_1$, $E_2$, the further exceptional curves, one strict
transform of the curve, meeting in the same way), the same multiplicities at the
same centres, the same single branch over the origin, and the same behaviour at
the last step; by (3.9.4) that is equivalence. It is the common pair at the last
point, and not the two displayed blowups on their own, that makes the final
resolution sequences coincide.

The same chain gives the cross-check: by (3.9.3),
$$
\delta=\binom32+\binom32=6
$$
for both germs, which is $\frac{(3-1)(7-1)}2$, the value the pair $(3,7)$ of step [](#puiseux-pair){.pf-ref} predicts.

This step is the card's own.
:::

:::

::: {.pf-step #tjurina-number-invariant}
For a plane hypersurface germ $f=0$, put
$$
\tau(f)
=
\dim_k
\frac{k[[x,y]]}{(f,f_x,f_y)}.
$$
The Tjurina number $\tau(f)$ is invariant under analytic isomorphism of the
curve germ.

::: pf-proof
That it is an analytic invariant is Greuel--Lossen--Shustin, Remark 3.43.3: "the Tjurina number $\tau$ is not a topological invariant, but it is an analytic invariant, that is, $\tau(C,z)=\tau(D,w)$ whenever $(C,z)$ and $(D,w)$ are analytically equivalent". The argument below, which is the card's own, gives the same statement in the form the exercise uses, where an analytic isomorphism is an isomorphism of completed local rings.

By step [](#ambient-automorphism-lift){.pf-ref}, such an isomorphism is induced by a formal coordinate
automorphism $\Phi$ together with multiplication of the equation by a unit:
$$
\Phi(f)=ug.
$$

The chain rule says that the two partial derivatives of $\Phi(f)$ are
invertible $k[[x,y]]$-linear combinations of $\Phi(f_x),\Phi(f_y)$, because
the Jacobian matrix of a formal coordinate automorphism is invertible.
Thus $\Phi$ carries
$$
(f,f_x,f_y)
$$
to the Tjurina ideal of $\Phi(f)$.

On the other hand,
$$
(ug,(ug)_x,(ug)_y)
=
(ug,u g_x+u_xg,u g_y+u_yg)
=
(g,g_x,g_y),
$$
because $u$ is a unit. Hence the two Tjurina algebras are isomorphic and
have the same dimension.
:::

:::

::: {.pf-step #tjurina-f1-twelve}
The first germ has
$$
\boxed{\tau(f_1)=12}.
$$

::: pf-proof
Greuel--Lossen--Shustin print this number in Example 3.43.1(a), as the output of the Singular command `tjurina(f)` for $f=y^3-x^7$: "//-> 12". For $f_1=y^3+x^7$, which differs from it by the unit $-1$, the computation is the following.

Since
$$
(f_1)_x=7x^6,
\qquad
(f_1)_y=3y^2,
$$
and the coefficients $3,7$ are units over $\CC$, one has
$$
(f_1,(f_1)_x,(f_1)_y)=(x^6,y^2).
$$
Therefore the residue classes
$$
x^i y^j,
\qquad
0\le i\le5,
\quad
0\le j\le1,
$$
form a basis of the Tjurina algebra. There are $6\cdot2=12$ such monomials.
:::

:::

::: {.pf-step #tjurina-f2-eleven}
The second germ has
$$
\boxed{\tau(f_2)=11}.
$$

::: pf-proof
The same display of Example 3.43.1(a), prints $11$ for $f+x^5y$: "tjurina(f+x5y); //-> 11". That germ is $y^3+yx^5-x^7$, which the substitution $(x,y)\mapsto(x,-y)$ of step [](#same-multiplicity-sequence){.pf-ref} carries to $-f_2$; the computation for $f_2$ itself is the following.

The derivatives are
$$
(f_2)_x=5x^4y+7x^6,
\qquad
(f_2)_y=3y^2+x^5.
$$
Modulo the Tjurina ideal, therefore,
$$
y^2=-\frac13x^5,
\qquad
x^4y=-\frac75x^6.
$$
Using the first relation in $f_2=0$ gives
$$
2x^5y+3x^7=0,
$$
while multiplying $(f_2)_x=0$ by $x$ gives
$$
5x^5y+7x^7=0.
$$
The coefficient matrix
$$
\begin{pmatrix}2&3\\5&7\end{pmatrix}
$$
has determinant $-1$, so
$$
x^5y=x^7=0.
$$
Consequently the Tjurina ideal is generated by
$$
y^2+\frac13x^5,
\qquad
x^4y+\frac75x^6,
\qquad
x^7.
$$
For lexicographic order with $y>x$, these three generators have leading
terms
$$
y^2,
\qquad
x^4y,
\qquad
x^7,
$$
and their three $S$-polynomials reduce to zero using these same relations.
They are therefore a Gröbner basis. Hence the standard monomials are
$$
1,x,\ldots,x^6,
\qquad
y,xy,x^2y,x^3y.
$$
There are $7+4=11$ of them.
:::

:::

::: {.pf-step #not-analytically-isomorphic}
The equivalent singularities $C_1$ and $C_2$ are not analytically
isomorphic.

::: pf-proof
If they were analytically isomorphic, step [](#tjurina-number-invariant){.pf-ref} would give
$$
\tau(f_1)=\tau(f_2).
$$
But steps [](#tjurina-f1-twelve){.pf-ref} and [](#tjurina-f2-eleven){.pf-ref} give
$$
12\ne11.
$$
Thus the germs are not analytically isomorphic. Together with step [](#c1-c2-equivalent){.pf-ref},
this proves that equivalence in the sense of (3.9.4) does not imply analytic
isomorphism.
:::

:::

::: pf-qed
Steps [](#ambient-automorphism-lift){.pf-ref} and [](#automorphism-identifies-resolution-data){.pf-ref} prove that analytic isomorphism implies equivalence, and steps [](#analytic-implies-topological){.pf-ref} to [](#characteristic-exponents){.pf-ref} give the chain from an analytic isomorphism to equality of the Puiseux data. Steps [](#same-multiplicity-sequence){.pf-ref}, [](#c1-c2-equivalent){.pf-ref}, [](#tjurina-number-invariant){.pf-ref}, [](#tjurina-f1-twelve){.pf-ref}, [](#tjurina-f2-eleven){.pf-ref} and [](#not-analytically-isomorphic){.pf-ref} give two equivalent singularities which are not analytically
isomorphic, proving that the converse fails.
:::

:::
:::

::: {.remark title="Published solution"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.3, exercise 3.6, with the definition of equivalence in (3.9.4) and of analytic isomorphism before (I, 5.6.1).

Greuel, Lossen and Shustin, *Introduction to Singularities and Deformations* (2007), carries the frame of both halves. Definition 3.30, states analytic and topological equivalence of a germ side by side; Theorem 3.42, is the theorem of Brauner and Zariski that the topological type of a reduced plane curve singularity is determined by, and determines, the system of multiplicity sequences defined before Proposition 3.41; Proposition 3.41, identifies that data with the characteristic exponents of the branches and their pairwise intersection numbers. Example 3.43.1(a), gives the pair $y^3-x^7$ and $y^3+x^5y-x^7$, which have the same multiplicity sequence $3\longrightarrow3\longrightarrow1\longrightarrow1\longrightarrow1$ and are not analytically equivalent, the printed Singular output being $\tau=12$ for the first and $\tau=11$ for the second; Remark 3.43.3, records that the Tjurina number is an analytic invariant.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.3.6, gives the forward implication through completion: the strict transform's local ring splits over the points of the exceptional curve, completion commutes with that splitting, and so the completed local ring determines the resolution. He then states that $y^3+x^7$ and $y^3+x^5y+x^7$ are equivalent and not analytically isomorphic, without computing either. Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.3.6, cites Wall, *Singular Points of Plane Curves*, for both halves and states the same pair; Wall's criterion there is that equisingularity of plane branches is equivalent to equality of Puiseux characteristics.
:::
