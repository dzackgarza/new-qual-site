---
schema: qual/card@1
id: P-AGH2320DIMENSION
kind: problem
title: Dimension of an integral scheme of finite type over a field
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension Theory
  - Function Fields
  - Codimension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.20 statement and the standard dimension formulas for finite-type algebras over fields.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17

- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), II.3.20,
    printed pp. 94--95. A. Shichijo, R.Hartshorne "Algebraic Geometry" 演習問題
    への解答 (2020/March), Chapter 2 section 3, Exercise 3.20, printed pp. 17--18,
    read in the MinerU extraction tmp/sources/shitijyou-ch2-section3.md, proves
    (a) through (d) from Hartshorne I.1.8(a),(b) and I.3.6: dim X = dim O_{X,P}
    at a closed point, dim X = trdeg K(X)/k, and for a closed subset Y the
    identity codim(Y,X) = inf{dim O_{X,P} : P in Y} by reading a maximal chain of
    primes of an affine chart and localizing at the generic point of each
    irreducible Z contained in Y, then dim Y + codim(Y,X) = dim X from I.1.8(b).
    Its (e) is left unfinished (the sentence ends at "thus by Lemma I"); (f) is
    proved. It is not counted here as a located solution of the card's statement:
    its (b), (c), (d) are proved first for Y irreducible closed ("Y ::
    irreducible closed subset と仮定し") and then extended to a general closed Y
    by the infimum over the irreducible Z contained in Y, so at Y empty the
    infimum is over an empty family and nothing is said about it -- the case this
    card's remark is about. The source therefore confirms the card's reading of
    the printed exercise and does not supply the missing convention; the card's
    own proof, which treats the nonempty case and records the empty one, stands.
    The source is cited in the body for the nonempty case only.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    One misprint of the source is now recorded on the card, in step
    codim-y-equals-inf-dim-op, and the earlier note's wording is corrected with
    it. Shichijo derives, for irreducible closed Z with generic point zeta_Z,
    codim(Z,X) = dim O_{X,zeta_Z} -- the length of the maximal chain of primes he
    localizes at p_Y -- but prints dim Z = dim O_{X,zeta_Z}, and his next display
    then reads codim(Y,X) = inf{dim Z : Z inside Y} = inf{dim O_{X,zeta_Z} : Z
    inside Y}. Both are misprints of dim Z for codim(Z,X): inf{dim Z} over the
    irreducible Z inside Y is 0 whenever Y contains a closed point. Read with
    codim(Z,X) in place of dim Z, the two displays prove (c) exactly as the card
    states it, so the source's argument stands and only its typography is
    recorded. The empty case and (e) are as the earlier note says.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Transcription pass for issue #121, on parts (c) and (d). Read at the
    cited places: Dongryul Kim, Exercise 2.3.20, PDF pp. 31--32, text
    version tmp/sources/hartshorne-solutions-kim.md, and A. Shichijo,
    Exercise 3.20, printed pp. 17--18, text version
    tmp/sources/shitijyou-ch2-section3.md. Checked against the book in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed p. N
    is PDF p. N+15: II.3.20(c) and (d) as printed on p. 95, for an
    arbitrary closed subset, with no nonemptiness hypothesis. What the
    transcription changed. Step codim-z-equals-dim-op is now Shichijo's
    argument for irreducible closed Z, a maximal chain of primes below the
    prime of Z localized at that prime, with a chain in A localized being
    maximal so that its length is the dimension of the local ring, together
    with Kim's computation of the same codimension inside an affine chart;
    the earlier text asserted the correspondence of chains to chains of
    primes without the localization. Step codim-y-equals-inf-dim-op now
    carries Kim's reduction to irreducible Y before Shichijo's argument.
    Step dimz-plus-codimz-equals-dimx is now Shichijo's use of Chapter I
    Theorem 1.8(b), dim A over p plus height p equals dim A, and Kim's
    version of it, with the card's trdeg form kept beside them. Step
    dimy-plus-codimy-equals-dimx now carries Kim's sentence that dim Y is
    the maximum over components and codim(Y,X) the minimum over them, and
    spells the reduction out. Both sources take an infimum over the
    irreducible closed subsets of Y, so neither treats Y empty; that part
    of the printed statement has no published proof, which the COMPLAINTS
    record of 2026-11-16 names. Not checked: no source outside the two
    named was read in this pass, and parts (a), (b), (e) and (f) were not
    re-derived.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, two items. (i) The transcription of Kim,
    Exercise 2.3.20(c), PDF p. 32, had written the fibre product as
    X times_Z K(Z), with a Z that Kim does not use and over which X is not
    a scheme; Kim writes X times_Y K(Y), Y being his closed subset and
    K(Y) the residue field of its generic point, and the card now carries
    that expression with the reason it is defined. The error was the
    card's transcription, not the source's. (ii) The order-reversing
    correspondence used in step codim-z-equals-dim-op was cited as
    "Exercise I.1.7"; Shichijo cites Ch. I Prop. 1.7, and Chapter I
    Proposition 1.7, printed p. 6, is the statement that an affine
    algebraic set has the dimension of its coordinate ring, whose proof is
    that correspondence. The card now cites the proposition and its printed
    page. Checked against the book in
    tmp/sources/hartshorne-1977-algebraic-geometry.md (printed p. N is PDF
    p. N+15): II.3.20 on printed pp. 94--95 and Proposition I.1.7 on
    printed p. 6. Not checked: no other passage was re-read, and no step
    was re-derived.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, on two passages the previous pass of this
    date introduced. (i) Kim's X times_Y K(Y). The previous pass kept Kim's
    expression and said it is defined because X is a scheme over Y and K(Y)
    is the residue field of its generic point. That reason is false: Y here
    is a closed subset of X, and there is no morphism X -> Y, so X times_Y
    K(Y) is not the fibre product of schemes over Y. What the equality
    computes, and what dim A_p measures, is Spec O_{X,eta_Y}, the spectrum
    of the local ring at the generic point of Y; the step now says so and
    records the notation as Kim's rather than as a construction. The source's
    defect is a defect of notation, named on the card and not repaired in
    the source's name. (ii) The correspondence between irreducible closed
    subsets and prime ideals. The previous pass cited Chapter I Proposition
    1.7 for it, printed p. 6. Proposition I.1.7 is dim Y = dim A(Y); the
    correspondence is Corollary I.1.4, printed p. 4, together with the
    sentence there that an algebraic set is irreducible exactly when its
    ideal is prime. Shichijo cites Ch. I Prop. 1.7 in his Claim Ex3.20.1,
    and there for dim R = dim Spec R, his correspondence being stated for
    Spec R of a ring and not for an affine variety. The step now cites
    Corollary I.1.4 and says what Shichijo's citation is. Checked against
    the book in tmp/sources/hartshorne-1977-algebraic-geometry.md, where
    printed p. N is PDF p. N+15: Corollary I.1.4 and Proposition I.1.7 in
    Chapter I section 1, printed pp. 4 and 6 of the text version, and II.3.20
    on printed pp. 94--95; Shichijo's Claim Ex3.20.1 and Exercise 3.20(c)
    were re-read in tmp/sources/shitijyou-ch2-section3.md, printed pp.
    17--18, and Kim's Exercise 2.3.20(c) in
    tmp/sources/hartshorne-solutions-kim.md, PDF p. 32. Not checked: parts
    (a), (b), (e) and (f) were not re-read in this pass, and no step was
    re-derived beyond the two passages above.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, on the correspondence cited in step
    codim-z-equals-dim-op. Corollary I.1.4, printed p. 4, is the one-to-one
    inclusion-reversing correspondence between the algebraic sets in A^n and the
    radical ideals of k[x_1,...,x_n], with an algebraic set irreducible exactly
    when its ideal is prime; k is algebraically closed there, and the ring in
    this step is a finitely generated algebra over an arbitrary field, not the
    coordinate ring of an affine variety, so the corollary does not state what
    the step uses and does not apply. The step now cites the correspondence
    between the irreducible closed subsets of Spec A and the prime ideals of A
    where it is stated for Spec of a ring, A. Shichijo's Claim Ex3.20.1, printed
    p. 17, and says that his citation of Ch. I Prop. 1.7 there is the analogue
    for an affine variety. The audit event of even date above, which introduced
    the citation of Corollary I.1.4, is left as written; its item (ii) does not
    hold, for the reason just given, and this event is its correction. Read in
    this pass: Corollary I.1.4 and Proposition I.1.7 in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed p. N is PDF
    p. N+15, Corollary I.1.4 standing on PDF p. 19 (printed p. 4) and
    Proposition I.1.7 on printed p. 6; and Shichijo, Claim Ex3.20.1 with the
    proof of Exercise 3.20(c), in tmp/sources/shitijyou-ch2-section3.md, the
    heading "Ex3.20 Dimension" at line 791 of the extraction, printed p. 17,
    which is page 17 of tmp/sources/shitijyou-ch2-section3.pdf, its printed
    folio being its page. Not checked: II.3.20 itself was not re-read in this
    pass, Shichijo's printed pp. 18--20 were not opened, and no step was
    re-derived.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, on the rendered card only. The head of the
    solution and the remark on the published solution named the text versions of
    the two sources, tmp/sources/hartshorne-solutions-kim.md and
    tmp/sources/shitijyou-ch2-section3.md, beside the citations they support.
    Those paths are the repository's file store and stay in the transcription
    event of even date, which names both with the pages read there; the two
    rendered passages now cite Kim by exercise, PDF page and source revision and
    Shichijo by exercise and printed page, and say nothing about where the files
    are (PROSE-11, QUAL-08, SEC-7). No mathematics changes, no page moves, and
    no step was re-read in this pass. Read in this pass: nothing beyond the two
    rendered sentences; the sources were not reopened.

- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, on the rendered card and on nothing else.
    (i) The remark carried a stray closing line "Agree.", the residue of a note
    on a source, which says nothing about the mathematics; it is removed.
    (ii) A remark block stood between the problem and the solution, against the
    order STYLE-07 fixes for a problem card: the problem, then hints, then
    solutions, then remarks. That block, the one recording that (c) and (d) are
    stated for an arbitrary closed subset and that they are meaningful only for
    nonempty $Y$, now stands after the solution and before the remark on the
    published solution, and its phrase "the proof below treats that case" is
    "the proof on this card treats that case", the proof now preceding it. The
    text of both remarks is otherwise unchanged: the conventions
    $\codim(\emptyset,X)=+\infty$ and $\krulldim\emptyset=-1$, and Shichijo's
    Exercise 3.20 at printed pp. 17--18 not treating $Y=\emptyset$ either. No
    step, page or statement moves. Read in this pass: the block order of this
    card and the two remarks; no source was reopened and no step was re-derived.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, two items. (i) QUAL-01: parts (c) and (d)
    carried the printed text verbatim, "If Y is a closed subset of X", which is
    false at Y empty and therefore ill-posed as printed: the right-hand side of
    (c) is then an infimum over the empty family, and with the usual conventions
    codim(empty, X) = +infinity and dim empty = -1 the identity of (d) fails.
    Both statements now read "If Y is a nonempty closed subset of X", which is the
    hypothesis the proofs on this card use; the displays themselves are unchanged,
    as are parts (a), (b), (e) and (f). The remark on the problem states what the
    exercise prints and why the empty case has no content, without saying anything
    about how the card was written. The printed text is the one the events of
    2026-11-15 record, read in tmp/sources/hartshorne-1977-algebraic-geometry.md at
    printed pp. 94--95; it was not re-read in this pass. (ii) STYLE-08: the pf-qed
    only listed which step proves which part. It now carries the argument, resting
    on the two facts stated at the head of the solution, dim A = trdeg_k K and the
    dimension formula for a prime, and saying for each part which of the two it
    reads and at which prime. No step is re-derived beyond that reading, and no
    source was reopened.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, six items on the rendered card. (i) QUAL-01:
    the statement had dropped the exercise's own instruction. Hartshorne II.3.20
    opens, on printed p. 94, "Let X be an integral scheme of finite type over a
    field k, not necessarily algebraically closed. Use appropriate results from
    (I, §1) to prove the following, where for rings, we always mean the Krull
    dimension", and the statement again carries the second sentence, which the
    card had reduced to "Prove the following". The text version's OCR of that
    sentence is garbled --- it reads "Use appropriate results from (, ) to prove
    the follw", losing the cross-reference --- and the reading taken is Kim's,
    who transcribes the exercise at the head of his solution with the words
    "Use appropriate results from ( I , § 1 ) to prove the following". (ii) The
    head of the solution said that "the two sources agree with those proofs" of
    (a), (b), (e) and (f). That holds of (a) and (b) and of neither (e) nor (f):
    Kim's (e) is one sentence, "Then we can use (a)", and Shichijo's (e) stops
    at "したがって Lemma より", his Lemma Ex3.20.2, and reaches no
    conclusion; for (f) Kim reduces to
    algebraic extensions and then to algebraically closed k and k', and
    Shichijo passes through k_T = k(T), so neither follows the route of step
    component-of-xprime-dim-d. The head now says which parts each source proves
    and which are proved here. (iii) Step component-of-uprime-dim-d asserted
    that the contraction of a minimal prime of A' is a minimal prime of R
    "under an integral extension", which is false: for R = k[t] ⊂ k[t] × k, f ↦
    (f, f(0)), the extension is integral and the minimal prime k[t] × 0
    contracts to (t). The step now derives q ∩ R = (0) from torsion-freeness:
    A is a domain and a finite k[t_1,...,t_d]-module, hence torsion-free over
    that ring and a submodule of a free module, and tensoring the injection with
    k' over k, which is exact, makes A' torsion-free over k'[t_1,...,t_d]; a
    minimal prime of a noetherian ring consists of zero divisors, so it meets R
    in 0. The ring map R → A'/q is then injective, finite and integral, and the
    dimension d follows from lying over, going up and incomparability. (iv) The
    book's number is Theorem 1.8A(b), not 1.8(b): the text version prints
    "Theorem 1.8A. Let k be a field, and let B be an integral domain which is a
    finitely generated k-algebra ... (b) For any prime ideal p in B, we have
    height p + dim B/p = dim B". Step dimz-plus-codimz-equals-dimx now cites
    Theorem I.1.8A(b), and the event of 2026-11-16 whose note begins
    "Transcription pass for issue #121" carries the same number wrongly and is
    left as written; Shichijo's "Ch I,Thm1.8b" is his own abbreviation. (v) The
    pf-qed said that everything follows from the two facts at the head of the
    solution. It does not: step codim-z-equals-dim-op proves (c) from the
    correspondence between irreducible closed subsets and primes together with a
    localized maximal chain, step dimu-equals-dimx proves (e) without localizing,
    by a nonempty affine open V ⊆ U ⊆ X, and (f) needs the flatness and
    going-down argument of step component-dominates-x as well. The pf-qed now
    states for each part what it uses. (vi) Three references to exercises were
    written as if they were theorems: "Hartshorne II.3.3(c)", "Hartshorne
    II.3.6" and "Hartshorne II.3.14" now read "Exercise II.3.3(c)", "Exercise
    II.3.6" and "Exercise II.3.14"; II.3.3 also collides with Theorem II.3.3 on
    fibre products, which the first step's argument does not use. Checked
    against the book in tmp/sources/hartshorne-1977-algebraic-geometry.md, where
    printed p. N is PDF p. N+15: the exercise's opening sentence on printed p. 94
    (PDF p. 109, line 2874 of the extraction) and its parts (a)--(f) on printed
    pp. 94--95, and Theorem 1.8A with Proposition 1.7 above it on printed p. 6
    (PDF p. 21). Read in this pass: Kim's Exercise 2.3.20, both his statement of
    it at line 879 and his solutions to (a)--(f), in
    tmp/sources/dongryul-kim-hartshorne-solutions.md, PDF pp. 31--32; and
    Shichijo's Exercise 3.20, Claim Ex3.20.1 through his (f), in
    tmp/sources/shitijyou-ch2-section3.md, from the heading "Ex3.20 Dimension."
    to the claims of Ex3.20.3, printed pp. 17--18. Not checked: the printed book
    itself was not in hand, both passages being read in the text versions named;
    Shichijo's printed pp. 17 and 18 could not be collated against his PDF for
    the place his (c) stands; and no step beyond the four named was re-derived.

---

::: {.problem}
Let $X$ be an integral scheme of finite type over a field $k$, not necessarily algebraically closed.
Use appropriate results from (I, §1) to prove the following, where for rings $\krulldim$ always means the Krull dimension.

(a) For any closed point $P \in X$, $\krulldim X = \krulldim \OO_P$.

(b) Let $K(X)$ be the function field of $X$.
Then
$$
\krulldim X = \trdeg\qty{K(X)/k}.
$$

(c) If $Y$ is a nonempty closed subset of $X$, then
$$
\codim(Y, X) = \inf \theset{\krulldim \OO_{P, X} \st P \in Y}.
$$

(d) If $Y$ is a nonempty closed subset of $X$, then
$$
\krulldim Y + \codim(Y, X) = \krulldim X.
$$

(e) If $U$ is a nonempty open subset of $X$, then $\krulldim U = \krulldim X$.

(f) If $k \subseteq k'$ is a field extension, then every irreducible component of $X' = \fiberprod{X}{k}{k'}$ has dimension equal to $\krulldim X$.
:::

::: {.solution}
Parts (c) and (d) are proved by Dongryul Kim, Exercise 2.3.20, and by A. Shichijo, Exercise 3.20, at the steps that cite them, and parts (a) and (b) by both as well.  Parts (e) and (f) are proved here: Kim proves (e) by his (a), and Shichijo's sentence for it stops before the conclusion; for (f), Kim reduces to algebraic base extensions and then to algebraically closed $k$ and $k'$, and Shichijo passes through the purely transcendental intermediate field $k_T$, while the proof below reads the dimension off a Noether normalization after the base change.

We use the following standard affine dimension theorem.

If $A$ is a finitely generated integral $k$-algebra with fraction field $K$, then
$$
\dim A=\operatorname{trdeg}_kK,
$$
every maximal localization $A_{\mathfrak m}$ has this same dimension, and for every prime $\mathfrak p\subseteq A$,
$$
\boxed{
\dim A_{\mathfrak p}
+\operatorname{trdeg}_k\kappa(\mathfrak p)
=\operatorname{trdeg}_kK.}
$$
The first two assertions follow from Noether normalization and going up; the last is the dimension formula for finite-type algebras over a field.  These are Stacks Project, Tags 00P0 and 00P1.

::: pf

::: {.pf-step #affine-open-dim-equals-trdeg}
Every nonempty affine open
$$
U=\Spec A\subseteq X
$$
has
$$
\dim U
=
\operatorname{trdeg}_kK(X).
$$

::: pf-proof
Since $X$ is integral, $A$ is a domain.  Since $X$ is of finite type over $k$, Exercise II.3.3(c) shows that $A$ is a finitely generated $k$-algebra.

By Exercise II.3.6,
$$
\operatorname{Frac}(A)\cong K(X).
$$
The affine dimension theorem therefore gives
$$
\dim U=\dim A=\operatorname{trdeg}_kK(X).
$$
:::

:::

::: {.pf-step #dimx-leq-r}
Put
$$
r=\operatorname{trdeg}_kK(X).
$$
Then
$$
\dim X\le r.
$$

::: pf-proof
Take any strict chain of irreducible closed subsets
$$
Z_0\subsetneq Z_1\subsetneq\cdots\subsetneq Z_n
$$
in $X$.

The closed subscheme $Z_0$ with its reduced induced structure is of finite type over $k$.  By Exercise II.3.14, it contains a closed point $P$.  Since $Z_0$ is closed in $X$, this point is closed in $X$ as well.

Choose an affine open neighborhood
$$
U\subseteq X
$$
of $P$.  Each intersection
$$
Z_i\cap U
$$
is nonempty and irreducible.  Moreover the inclusions remain strict.  Indeed, if
$$
Z_i\cap U=Z_{i+1}\cap U,
$$
then the nonempty open subset $Z_{i+1}\cap U$ of the irreducible space $Z_{i+1}$ would lie in the proper closed subset $Z_i$, impossible.

Thus
$$
Z_0\cap U\subsetneq\cdots\subsetneq Z_n\cap U
$$
is a chain of length $n$ in $U$.  By step [](#affine-open-dim-equals-trdeg){.pf-ref},
$$
n\le\dim U=r.
$$
Taking the supremum over all chains gives $\dim X\le r$.
:::

:::

::: {.pf-step #dimx-geq-r}
One has
$$
\dim X\ge r.
$$

::: pf-proof
Any nonempty affine open $U\subseteq X$ is a subspace of $X$, so every chain of irreducible closed subsets in $U$ gives a chain of the same length in $X$ after taking closures in $X$.  Hence
$$
\dim U\le\dim X.
$$
By step [](#affine-open-dim-equals-trdeg){.pf-ref}, $\dim U=r$.
:::

:::

::: {.pf-step #dimx-equals-trdeg}
Therefore
$$
\boxed{
\dim X=\operatorname{trdeg}_kK(X).}
$$

::: pf-proof
Combine steps [](#dimx-leq-r){.pf-ref} and [](#dimx-geq-r){.pf-ref}.  This proves part (b).
:::

:::

::: {.pf-step #dim-op-equals-dimx-closed-point}
Let $P\in X$ be a closed point.  Then
$$
\boxed{\dim\mathcal O_{X,P}=\dim X.}
$$

::: pf-proof
Choose an affine neighborhood
$$
U=\Spec A
$$
of $P$, and let $\mathfrak m\subseteq A$ be the corresponding maximal ideal.  Then
$$
\mathcal O_{X,P}=A_{\mathfrak m}.
$$
By step [](#affine-open-dim-equals-trdeg){.pf-ref}, the fraction field of $A$ is $K(X)$ and
$$
\operatorname{trdeg}_kK(X)=\dim X.
$$
The maximal-localization part of the affine dimension theorem gives
$$
\dim A_{\mathfrak m}
=
\operatorname{trdeg}_kK(X)
=
\dim X.
$$
This proves part (a).
:::

:::

::: {.pf-step #codim-z-equals-dim-op}
If $P\in X$ and
$$
Z=\overline{\{P\}},
$$
then
$$
\boxed{
\codim(Z,X)=\dim\mathcal O_{X,P}.}
$$

::: pf-proof
Shichijo, Exercise 3.20(c): take $Z=V(\mathfrak p_Z)\subseteq\Spec A$ for an irreducible closed $Z$ in an affine chart $X=\Spec A$, and a maximal chain of primes
$$
(0)\subsetneq\cdots\subsetneq\mathfrak p_Z,
$$
whose length is $\codim(Z,X)$ by the order-reversing correspondence between the irreducible closed subsets of $\Spec A$ and the prime ideals of $A$.  Shichijo states that correspondence for $\Spec R$ of a ring in his Claim Ex3.20.1, where the irreducible closed subsets of $\Spec R$ stand in bijection with the primes of $R$ and the inclusion is reversed, and cites Ch. I Prop. 1.7 there only as the analogue for an affine variety; Proposition I.1.7, is the equality of the dimension of an affine algebraic set with that of its coordinate ring.  Localizing at $\mathfrak p_Z$ gives a chain of the same length
$$
(0)_{\mathfrak p_Z}\subsetneq\cdots\subsetneq(\mathfrak p_Z)_{\mathfrak p_Z},
$$
and a chain of that length in $A_{\mathfrak p_Z}$ is maximal, so its length is
$$
\dim\mathcal O_{X,\mathfrak p_Z}.
$$
He writes $\zeta_Z$ for the generic point of an irreducible closed $Z$ and concludes
$$
\codim(Z,X)=\dim\mathcal O_{X,\zeta_Z}
$$
for every irreducible closed $Z$, the map $Z\mapsto\zeta_Z$ being a bijection onto the points of $X$.

Kim, Exercise 2.3.20(c), proves the same identity for irreducible closed $Y$ (his letter) by computing with an affine chart and the prime $\mathfrak p$ of $Y$: he has $\dim Y=\dim A/\mathfrak p$ and
$$
\codim(Y,X)=\dim\bigl(X\times_YK(Y)\bigr)=\dim\bigl(\Spec A\times_YK(Y)\bigr)=\dim A_{\mathfrak p},
$$
and that display is not a fibre product: $Y$ is here a closed subset of $X$, not the base of a morphism $X\to Y$, so $X\times_YK(Y)$ has no meaning as one.  What his equality computes is $\dim\Spec\mathcal O_{X,\eta_Y}$, the spectrum of the local ring at the generic point $\eta_Y$ of $Y$, which is $\Spec A_{\mathfrak p}$; the display is read that way, and the notation is his, not a construction this card makes.  His computation of that dimension is the one that needs $A$ to be a finitely generated $k$-algebra with $A/\mathfrak p$ a domain.
:::

:::

::: {.pf-step #codim-y-equals-inf-dim-op}
For every nonempty closed subset $Y\subseteq X$,
$$
\boxed{
\codim(Y,X)
=
\inf_{P\in Y}\dim\mathcal O_{X,P}.}
$$

::: pf-proof
The reduction to irreducible $Y$ is Kim's, Exercise 2.3.20(c): "Since $\operatorname{codim}(Y,X)$ is defined as the infimum of codimension of irreducible closed subsets, it suffices to show this for $Y$ irreducible closed."  The irreducible case is A. Shichijo's argument, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (Solutions to the exercises in Hartshorne's *Algebraic Geometry*), 2020/March version, <https://shitijyou-a.github.io/math/alg-geo/har-ag-solutions/>, Chapter 2 section 3, Exercise 3.20(c): he proves it for $Y$ irreducible closed by reading a maximal chain of primes in an affine chart and localizing it at the generic point, which counts the height of the prime $\mathfrak p_Y$ of $Y$ --- the computation of step [](#codim-z-equals-dim-op){.pf-ref} --- and with it the codimension of $Y$, that is
$$
\codim(Z,X)=\dim\mathcal O_{X,\zeta_Z};
$$
his display prints $\dim Z$ on the left where the codimension belongs, and that is a misprint: the length of the chain he has just localized at $\mathfrak p_Y$ is the codimension of $Z$ in $X$, not its dimension, and the two differ --- a point of a surface has $\dim 0$ and $\codim 2$. The display that follows carries the same misprint, $\codim(Y,X)=\inf\theset{\dim Z \st Z\subseteq Y}=\inf\theset{\dim\mathcal O_{X,\zeta_Z} \st Z\subseteq Y}$, where the first infimum is over $\codim(Z,X)$: the infimum of $\dim Z$ over the irreducible $Z\subseteq Y$ is $0$ as soon as $Y$ contains a closed point, and not $\codim(Y,X)$. He then takes the infimum over the irreducible $Z\subseteq Y$; that last step is over an empty family when $Y=\emptyset$, which is why the hypothesis $Y\ne\emptyset$ is kept here.

By definition,
$$
\codim(Y,X)
$$
is the infimum of $\codim(Z,X)$ over irreducible closed subsets $Z\subseteq Y$.

Every point $P\in Y$ gives such an irreducible closed subset
$$
\overline{\{P\}}\subseteq Y,
$$
and step [](#codim-z-equals-dim-op){.pf-ref} identifies its codimension with $\dim\mathcal O_{X,P}$.

Conversely every irreducible closed $Z\subseteq Y$ has a generic point $P\in Y$, and
$$
Z=\overline{\{P\}}.
$$
Thus the two sets of numbers over which the infima are taken are identical.  This proves part (c).
:::

:::

::: {.pf-step #dimz-plus-codimz-equals-dimx}
Let $Z\subseteq X$ be irreducible closed with generic point $\zeta$.  Then
$$
\boxed{
\dim Z+\codim(Z,X)=\dim X.}
$$

::: pf-proof
Shichijo, Exercise 3.20(d): with $X=\Spec A$ affine and $\mathfrak p$ the prime of the irreducible closed $Z$, Chapter I Theorem 1.8A(b) gives
$$
\dim\frac{A}{\mathfrak p}+\operatorname{height}\mathfrak p=\dim A,
$$
that is, since $\dim A/\mathfrak p=\dim Z$ and $\operatorname{height}\mathfrak p=\codim(Z,X)$ by step [](#codim-z-equals-dim-op){.pf-ref},
$$
\dim Z+\codim(Z,X)=\dim X .
$$

Kim, Exercise 2.3.20(d), proves it the same way: "in (c) we have computed $\dim Y=\dim A/\mathfrak p$ and $\operatorname{codim}(Y,X)=\operatorname{height}\mathfrak p$. Then $\dim X=\dim A$."

The card's form of the same statement, by the affine dimension formula of the head, is step [](#dimx-equals-trdeg){.pf-ref} applied to $Z$ together with the identity of step [](#codim-z-equals-dim-op){.pf-ref}:
$$
\dim Z=\operatorname{trdeg}_k\kappa(\zeta),\qquad
\codim(Z,X)=\dim\mathcal O_{X,\zeta},
$$
which add up to $\operatorname{trdeg}_kK(X)=\dim X$ because $\dim A_{\mathfrak p}+\operatorname{trdeg}_k\kappa(\mathfrak p)=\operatorname{trdeg}_kK(X)$.
:::

:::

::: {.pf-step #dimy-plus-codimy-equals-dimx}
For every nonempty closed subset $Y\subseteq X$,
$$
\boxed{
\dim Y+\codim(Y,X)=\dim X.}
$$

::: pf-proof
Kim, Exercise 2.3.20(d): "Since $\dim Y$ is the maximum among the dimensions of the irreducible components and $\operatorname{codim}(Y,X)$ is the minimum among the codimensions of the irreducible components, it suffices to show the formula for irreducible $Y$" --- which is step [](#dimz-plus-codimz-equals-dimx){.pf-ref}.

The two facts of that reduction, spelled out: for the irreducible components
$$
Y_1,\ldots,Y_m
$$
of a nonempty $Y$ one has
$$
\dim Y=\max_i\dim Y_i,
$$
and by step [](#dimz-plus-codimz-equals-dimx){.pf-ref},
$$
\codim(Y_i,X)=\dim X-\dim Y_i.
$$
Any irreducible closed subset of $Y$ is contained in some $Y_i$, and its dimension is at most $\dim Y_i$, so its codimension is at least $\codim(Y_i,X)$; hence
$$
\codim(Y,X)
=
\min_i\codim(Y_i,X)
=
\dim X-\max_i\dim Y_i.
$$
This proves part (d).
:::

:::

::: {.pf-step #dimu-equals-dimx}
If $U\subseteq X$ is nonempty open, then
$$
\boxed{\dim U=\dim X.}
$$

::: pf-proof
Choose a nonempty affine open
$$
V\subseteq U.
$$
Since $V$ is also a nonempty affine open of $X$, steps [](#affine-open-dim-equals-trdeg){.pf-ref} and [](#dimx-equals-trdeg){.pf-ref} give
$$
\dim V=\dim X.
$$
As subspaces,
$$
V\subseteq U\subseteq X,
$$
so
$$
\dim V\le\dim U\le\dim X.
$$
Therefore all three dimensions are equal.  This proves part (e).
:::

:::

::: {.pf-step #component-dominates-x}
Let $k\subseteq k'$ be a field extension and put
$$
X'=X\times_k k'.
$$
Every irreducible component of $X'$ maps dominantly to $X$.

::: pf-proof
The projection
$$
\pi:X'\to X
$$
is flat, because it is obtained by base change from the flat field extension $k\to k'$.

Let $C$ be an irreducible component of $X'$ with generic point $\xi_C$.  Work in an affine neighborhood
$$
U=\Spec A\subseteq X
$$
of the image of $\xi_C$.  On the corresponding affine base change
$$
U'=\Spec(A\otimes_k k'),
$$
the generic point of $C$ is represented by a minimal prime $\mathfrak q$.  Flatness gives going down, so the contraction of the minimal prime $\mathfrak q$ is a minimal prime of the domain $A$, hence is $(0)$.

Thus $\xi_C$ maps to the generic point of $X$, and $C\to X$ is dominant.
:::

:::

::: {.pf-step #noether-normalization-base-change}
Choose a nonempty affine open
$$
U=\Spec A\subseteq X
$$
and put
$$
d=\dim X.
$$
There is a finite injective Noether-normalization map
$$
k[t_1,\ldots,t_d]\hookrightarrow A.
$$
After base change,
$$
k'[t_1,\ldots,t_d]
\hookrightarrow
A'=A\otimes_k k'
$$
is again finite and injective.

::: pf-proof
By step [](#dimx-equals-trdeg){.pf-ref},
$$
d=\operatorname{trdeg}_kK(X)=\operatorname{trdeg}_k\operatorname{Frac}(A).
$$
Noether normalization gives algebraically independent elements $t_1,\ldots,t_d\in A$ such that $A$ is finite over the polynomial subring $k[t_1,\ldots,t_d]$.

Tensoring with the flat $k$-module $k'$ preserves injectivity, and tensoring a finite module with $k'$ remains finite.  This gives the asserted map.
:::

:::

::: {.pf-step #component-of-uprime-dim-d}
Every irreducible component of
$$
U'=U\times_k k'=\Spec A'
$$
has dimension $d$.

::: pf-proof
Let $\mathfrak q$ be a minimal prime of $A'$, and put
$$
R_0=k[t_1,\ldots,t_d],\qquad R=R_0\otimes_kk'=k'[t_1,\ldots,t_d],
$$
so that $A'$ is integral over $R$ by step [](#noether-normalization-base-change){.pf-ref}.

The contraction $\mathfrak q\cap R$ is not computed from integrality alone: the minimal primes of an integral extension of a domain need not contract to $(0)$.  What settles it here is that $A'$ is torsion-free over $R$.  The ring $A$ is a domain and a finite $R_0$-module, so no nonzero element of $R_0$ annihilates a nonzero element of $A$; a finite torsion-free module over a domain embeds in a finite free module, so $A\hookrightarrow R_0^N$ for some $N$, as $R_0$-modules.  Tensoring this injection with $k'$ over $k$ is exact, and the result is an injective $R$-linear map
$$
A'=A\otimes_kk'\hookrightarrow R_0^N\otimes_kk'=R^N .
$$
Hence every nonzero element of $R$ is a nonzerodivisor on $A'$.

The ring $A'$ is noetherian, and a minimal prime of a noetherian ring consists of zero divisors.  Since no nonzero element of $R$ is a zero divisor of $A'$,
$$
\mathfrak q\cap R=(0).
$$

Therefore
$$
R\hookrightarrow A'/\mathfrak q
$$
is injective, and it is finite and integral.  A finite injective ring map preserves the Krull dimension: lying over and going up carry a chain of primes of $R$ to a chain of the same length above it, and incomparability carries a chain of primes of $A'/\mathfrak q$ to a chain of the same length below it.  So
$$
\dim(A'/\mathfrak q)
=
\dim R
=d.
$$
This is the dimension of the irreducible component $V(\mathfrak q)$.
:::

:::

::: {.pf-step #component-of-xprime-dim-d}
Every irreducible component $C$ of $X'$ has dimension $d=\dim X$.

::: pf-proof
By step [](#component-dominates-x){.pf-ref}, $C$ contains a point mapping to the generic point of $X$, so it meets the inverse image $U'$ of every nonempty open $U\subseteq X$.  Hence
$$
C\cap U'
$$
is a nonempty open subset of $C$.  It is an irreducible component of $U'$: if it were properly contained in a larger irreducible closed subset of $U'$, its closure in $X'$ would be an irreducible closed subset properly containing the component $C$.

By step [](#component-of-uprime-dim-d){.pf-ref},
$$
\dim(C\cap U')=d.
$$
Give $C$ its reduced induced structure.  It is an integral scheme of finite type over $k'$.  Part (e), already proved in step [](#dimu-equals-dimx){.pf-ref}, gives
$$
\dim C=\dim(C\cap U')=d.
$$
This proves part (f).
:::

:::

::: pf-qed
Part (a) is step [](#dim-op-equals-dimx-closed-point){.pf-ref}: at a closed point the maximal-localization part of the affine dimension theorem gives $\krulldim\OO_{X,P}=\trdeg_kK(X)=\krulldim X$. Part (b) is steps [](#dimx-leq-r){.pf-ref} and [](#dimx-geq-r){.pf-ref}: a nonempty affine open has dimension $r$, a chain of irreducible closed subsets of $X$ restricts, after intersecting with that open, to a chain of the same length, and a chain in an open has closures in $X$ forming a chain of the same length. Part (c) is step [](#codim-y-equals-inf-dim-op){.pf-ref}: $\codim(Y,X)$ is the infimum of $\codim(Z,X)$ over the irreducible closed $Z\subseteq Y$, each such $Z$ is the closure of its generic point, and step [](#codim-z-equals-dim-op){.pf-ref} reads $\codim(Z,X)$ as the dimension of the local ring at that point, by a maximal chain of primes in an affine chart localized at the prime of $Z$. Part (d) is step [](#dimy-plus-codimy-equals-dimx){.pf-ref}: for an irreducible closed $Z$, Chapter I Theorem 1.8A(b) at the prime of $Z$ gives $\krulldim Z+\codim(Z,X)=\krulldim X$, and an arbitrary nonempty closed $Y$ has finitely many components, over which $\krulldim$ takes its maximum and $\codim$ its minimum. Part (e) is step [](#dimu-equals-dimx){.pf-ref}: a nonempty affine open $V\subseteq U$ is a nonempty affine open of $X$, so $\krulldim V=\krulldim X$, and $V\subseteq U\subseteq X$ gives $\krulldim V\le\krulldim U\le\krulldim X$. Part (f) is steps [](#component-dominates-x){.pf-ref}, [](#noether-normalization-base-change){.pf-ref}, [](#component-of-uprime-dim-d){.pf-ref} and [](#component-of-xprime-dim-d){.pf-ref}: flatness of the base change and going down make every component of $X'$ dominate $X$, such a component therefore meets the inverse image $U'$ of an affine chart $U$, the base-changed Noether normalization makes $A'$ a torsion-free finite module over $k'[t_1,\ldots,t_d]$ so that each component of $U'$ has dimension $d$, and part (e) carries that dimension from the open piece $C\cap U'$ to the component $C$.
:::

:::

:::

::: {.remark}
The exercise prints (c) and (d) for an arbitrary closed subset $Y$.  For $Y=\emptyset$ the right-hand side of (c) is an infimum over the empty family, and with the usual conventions $\codim(\emptyset,X)=+\infty$ and $\krulldim\emptyset=-1$ the identity of (d) fails, so the two assertions are meaningful only for nonempty $Y$, which is the hypothesis the statements above carry. A. Shichijo, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (2020/March), Chapter 2 section 3, Exercise 3.20, proves (a)--(d) for irreducible $Y$ and then passes to an arbitrary closed $Y$ by the same infimum, so it does not treat $Y=\emptyset$ either.
:::

::: {.remark title="Published solution"}
Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter II §3, Exercise 3.20, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: Kim computes dimensions through Noether normalization and going up, observes that the local rings at all closed points have the same dimension, and for (f) first reduces to algebraic base extensions and then to algebraically closed $k$ and $k'$ by comparing $X_{k'}$ with the two closures.
The proof above uses the dimension formula $\dim A_{\mathfrak p}+\operatorname{trdeg}_k\kappa(\mathfrak p)=\operatorname{trdeg}_kK$ for a finitely generated algebra over a field, derives (b) from the affine case together with a chain argument, and for (f) tensors a Noether normalization of an affine chart with $k'$ and reads the dimension of each component off the normalization.
:::
