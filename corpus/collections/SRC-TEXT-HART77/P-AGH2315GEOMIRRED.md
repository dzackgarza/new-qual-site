---
schema: qual/card@1
id: P-AGH2315GEOMIRRED
kind: problem
title: Geometric irreducibility, reducedness, and integrality after base change
classification:
  areas:
  - algebraic-geometry
  topics:
  - Base Change
  - Irreducibility
  - Reduced Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.15 statement and the standard separable-closure/perfect-closure tests for geometric irreducibility and reducedness.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the Stacks Project Lemma 33.8.9 (tag 038I) and Lemma 33.6.4 (tag
    035U) in full: the first lists geometric irreducibility, irreducibility
    after every finite separable extension, and irreducibility of X over a
    separable algebraic closure as equivalent; the second lists geometric
    reducedness, reducedness after every field extension, after every finite
    purely inseparable extension, after k^{1/p}, after k^{perf} and after
    the algebraic closure. Those are exactly the three conditions of each
    part with k_s and k_p in place. Rechecked the card's own steps: the
    purely inseparable base change being a homeomorphism, Lemma 10.47.2 for
    the minimal prime over an algebraically closed field, and injectivity of
    A tensor k_p to A tensor kbar.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Tag correction, on a reader's report of issue #121: Lemma 33.6.4 is tag
    035X, not 035U; 035U is Section 33.6 (Geometrically reduced schemes) and
    035X is its Lemma 33.6.4. Corrected here and in the remark, and the
    remark now also lists the lemma's item (7) instead of implying that its
    list stops at the closures. The reason for the citation is unchanged:
    items (2), (5) and (6) of 035X are the three conditions of part (b), and
    the proof was read in tmp/sources/stacks-tags/035X.md.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Both parts are now the Stacks Project's proof transcribed rather than
    cited: step affine-irreducibility-tfae is Algebra Lemma 10.47.3 (tag
    037K, printed pp. 544--545), steps xbark-irred-implies-xk-irred and
    xks-irred-implies-xbark-irred are the proof of Lemma 33.8.9 (tag 038I,
    printed pp. 2832--2833), step affine-reducedness-tfae is the first two
    paragraphs of the proof of Lemma 33.6.4 (tag 035X, printed p. 2821), and
    step purely-inseparable-reducedness-tests is Algebra Lemma 10.44.4
    (tag 030V, printed pp. 537--538). Pages are those of the retained
    compiled book tmp/sources/stacks-project-book.pdf, whose PDF page is its
    printed page; each page was read in that PDF. Read against the book:
    Hartshorne II Ex. 3.15 on printed p. 93 asks exactly the three closures
    and the perfect closure that 038I and 035X list, and its X is of finite
    type over k, which no step uses beyond the definitions. Not checked:
    the examples in part (c), which are the card's own and not in the
    source; and Algebra Lemma 10.44.4's own cited lemmas 10.43.4, 10.42.4,
    10.43.6, 10.43.7 and 10.44.2 were read as statements at the pages given,
    not transcribed.
- event: source-corrected
  by: claude
  date: 2026-11-17
  note: >-
    Reader's report on issue #121, third pass. The repair of the 2026-11-16
    note's three defects was applied but never committed, so it is committed
    here together with what the reader found still open.
    (1) The remark on irreducibility and domain-ness is replaced. It claimed
    that over an algebraically closed k of characteristic p the ring
    A = k[x,y]/(y^p - x^p - x) is a domain whose base change to K = Frac(A)
    acquires the nonzero nilpotent y - s. That is false: in
    A tensor_k K = K[X,Y]/(Y^p - X^p - X) the symbols X and Y are the images
    of the two generators, and X in K is a different element from the variable
    X, so (Y - s)^p = Y^p - s^p = Y^p - c for the constant c = X^p + X, which
    is not the relation. The relation has partial/partial X = -1 and so is
    squarefree, whence A tensor_k K is reduced, and it is in fact a domain. Over
    an algebraically closed field no counterexample exists, by the argument now
    in the remark: k = kbar makes X_K irreducible by step irreducibility-tfae,
    and A tensor_k K is reduced by Algebra Lemma 10.43.6 (tag 030U, printed
    p. 534), the separable-extension case that step 030V records. The example the
    remark now gives is the non-perfect one, k = F_p(u) and A = k[x]/(x^p - u),
    which is step integral-not-geom-reduced itself. A perfect base that is not
    algebraically closed fails the other half: over k = R the field A = C gives
    C tensor_R C = C x C, which is step integral-not-geom-irreducible, so
    irreducibility of A tensor_k K is not decided by A being a domain even
    then.
    (2) Step xks-irred-implies-xbark-irred is item (3) => (4) of Algebra
    Lemma 10.47.3 (tag 037K, tmp/sources/stacks-tags/037K.md, printed p. 544),
    whose third paragraph is the purely inseparable passage from the separable
    to the algebraic closure through Lemma 10.46.7. It is not the proof of
    Lemma 33.8.9, whose second paragraph runs the other way, from a reducible
    X over the separable closure to a reducible X over some finite separable
    subextension. The 2026-11-16 note and the remark said otherwise; both are
    corrected in the solution, the note left as written.
    (3) Pages. Lemma 33.6.4's statement begins on printed p. 2821 and breaks
    after item (5), so items (6), (7) and the whole proof are on p. 2822 and
    the 2026-11-16 note's "printed p. 2821" for the proof paragraphs is wrong;
    the step and the remark now cite p. 2822. Algebra Lemma 10.44.4 is on
    p. 537 alone, p. 538 being the first page of Section 10.45. All pages were
    checked page by page in tmp/sources/stacks-project-book.pdf (its PDF page
    is its printed page) and every statement was read in its tag file. That
    file has 7654 pages, not the 7655 that the preamble said, its last page
    being the bibliography headed 7654.
    (4) The nine tags that had no file, 00HS 00FK 01OJ 01JO 00I3 04KM 07K2
    030W 00EU, now have one apiece in tmp/sources/stacks-tags and are cited
    with it, at the printed pages 525, 495, 534, 532, 535, 536 and 481 for the
    Algebra lemmas; the paragraph announcing that they had none is replaced.
    The tag files are the text versions cited throughout, the site's build
    from stacks-project commit a04446e57ec1fbc252a871afcec7752fb2807b14; the
    compiled book is a different, older build and only its pages are taken
    from it.
    COMPLAINTS.md is corrected in the same pass: the II.3.15 header no longer
    calls the card unsolved, the paragraph recording Cais's argument now gives
    the non-perfect counterexample instead of the false one, and the page and
    attribution in the closing paragraph of that entry are fixed, as is the
    duplicated sentence of the II.2.15(c) entry and the citation of I.7.6(a)
    in the I.7.7(b) correction. Those edits were carried into commit
    493cf6e98d, which is another chat's, because this checkout is shared and
    they were in the tree when it committed; the file's content is as
    described here. Not checked
    in this pass: part (c)'s three examples, which are the card's own and were
    not changed, and the statements of 10.39.19, 10.30.5, 10.43.4, 10.42.4,
    10.43.7, 10.44.2 and 10.25.1, which were read as statements in their tag
    files at the pages given and not transcribed.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, fourth pass. One step is repaired and two
    record defects are corrected; the step repair is stated here so that a
    record of the commit's own day carries it.
    (1) Step purely-inseparable-reducedness-tests gave the implications of
    Algebra, Lemma 10.44.4 (tag 030V) the wrong reason. It said that a reduced
    ring stays reduced after a base change to a larger field containing the
    last one as a subfield, which is false, and the card's own step
    integral-not-geom-reduced refutes it: over k = F_p(u) the field
    S = k[x]/(x^p - u) is reduced, while k^{1/p} tensor_k S is
    k^{1/p}[x]/((x - u^{1/p})^p), which is not. What the four implications
    use is the other direction. For k inside L inside K the map
    L tensor_k S -> K tensor_k S is injective because K is flat over the
    field L, so the smaller field's tensor is a subring of the larger one's
    and is reduced with it; the step now says that, names the larger field
    each implication runs from, and keeps the counterexample to the upward
    direction. The lemma's own "it is clear" is read that way, and nothing
    else in the step, in parts (a) and (b), or in part (c) changed.
    (2) The event above was written and committed on 2026-11-16, in
    4ace5f19b8 (committer date 2026-11-16 07:30:21), and a record carries the
    day of the commit that lands it: its date field said 2026-11-17, a day
    that had not happened, and it says 2026-11-16 now. Its text stands. The
    same correction is made in the four other events of that date on the
    three other cards of the round.
    (3) The event above says that the COMPLAINTS.md edits of that pass "were
    carried into commit 493cf6e98d, which is another chat's". That commit
    carries none of them: `git show 493cf6e98d -- COMPLAINTS.md` is the
    V.3.6, V.3.7, V.4.3, V.4.4(b) and V.5.8(b) paragraphs only. They entered
    through 89d13d01e14 (2026-11-16 07:13:27), whose COMPLAINTS diff carries
    the II.3.15 header, the Cais paragraph, the duplicated sentence of the
    II.2.15(c) entry and the I.7.6(a) sentence of the I.7.7(b) correction.
    The final report of the round repeated 493cf6e98d; the commit is
    89d13d01e14. Not checked in this pass: the mathematics of the rest of the
    card, which the reader accepted, and part (c)'s three examples, which
    were not changed.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, sixth pass: the fourth-pass event above was
    rewritten in place by 104d6c8646, and it is restored here to the text it
    had on its date, as d6dd20ac0c committed it. The rewrite was false as well
    as in place. The restored enumeration is right: `git show 493cf6e98d --
    COMPLAINTS.md` has three hunks, and what they add is the V.3.7 sentence of
    the Chapter V state paragraph and four new paragraphs, V.3.6, V.4.4(b),
    V.4.3 and V.5.8(b). The five the event names are therefore V.3.6, V.3.7,
    V.4.3, V.4.4(b) and V.5.8(b), the V.3.7 change being the sentence appended
    to that paragraph rather than one of the four new ones; the rewrite
    dropped V.3.6 and V.4.3, and both are in that diff. The commit the event
    corrects is unchanged: the II.3.15 edits entered through 89d13d01e14, not
    493cf6e98d. Nothing in the problem, the solution or the pages changes, and
    no page was re-read.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, fifth pass: the in-place rewrite of the
    2026-11-16 solution-written event. Commit 4ace5f19 deleted the words
    "Read against the book:" from that event's sentence "printed page; each
    page was read in that PDF. Read against the book: Hartshorne II Ex. 3.15
    on printed p. 93 asks ...". A dated event is a record of its date and is
    left as it stands; the deleted words are quoted here, and they carried no
    claim beyond introducing the comparison with Hartshorne that the sentence
    still makes. Nothing else on the card changes in this pass, and no page
    was re-read.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121 on in-place edits to dated events. Commit
    d6dd20ac0c (committer date 2026-11-16 09:00:13) changed the third-pass
    event's date from 2026-11-17 to 2026-11-16, in the same diff that added the
    fourth-pass event. A dated event is never edited: its day is part of the
    record, and a correction is a new event of the commit's date. The field is
    therefore restored here to 2026-11-17, the day that event's author wrote;
    the commit that landed it is 4ace5f19b8 (committer date 2026-11-16
    07:30:21), a day earlier than the date it carries, and that is the record.
    Its text is unchanged, and so is the fourth-pass event's text, whose item
    (2) records what d6dd20ac0c did: that item's "it says 2026-11-16 now"
    describes the state this event restores to 2026-11-17. The fourth-pass
    event's corrected attribution is untouched: the II.3.15 COMPLAINTS.md edits
    entered through 89d13d01e14. Nothing in the problem, the solution or the
    pages changes, and no page was re-read.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121 on in-place edits to dated events; two
    records are restored to the text they were committed with, and nothing in
    the problem, the solution or the pages changes. No page was re-read.
    (1) Commit a54c0ddf5b (committer date 2026-11-15 19:08:16) changed the
    2026-11-11 source-checked note's "tag 035U" to "tag 035X", a record dated
    four days before that commit. The note is restored and reads 035U as its
    session wrote it, which is Section 33.6 rather than its Lemma 33.6.4; the
    tag correction it carried is the 2026-11-15 source-corrected event that
    follows it, and the body and the published-solution remark cite 035X
    throughout.
    (2) Commit 4ace5f19b8 (committer date 2026-11-16 07:30:21) deleted the
    words "Read against the book:" from the 2026-11-16 solution-written note.
    That note and that commit carry the same day, and the note is restored
    all the same: a record keeps the text of its day, and the words carried
    no claim beyond introducing the comparison with Hartshorne that the
    sentence still makes. They were also quoted, with the deletion, in the
    event recording the fifth pass, which stands as written.

---

::: {.problem}
Let $X$ be a scheme of finite type over a field $k$, not necessarily algebraically closed.
Here $\fiberprod{X}{k}{K}$ abbreviates $\fiberprod{X}{\Spec k}{\Spec K}$.

(a) Show that the following three conditions are equivalent, in which case we say that $X$ is **geometrically irreducible**:

    - $\fiberprod{X}{k}{\bar{k}}$ is irreducible, where $\bar{k}$ denotes the algebraic closure of $k$;
    - $\fiberprod{X}{k}{k_s}$ is irreducible, where $k_s$ denotes the separable closure of $k$;
    - $\fiberprod{X}{k}{K}$ is irreducible for every extension field $K$ of $k$.

(b) Show that the following three conditions are equivalent, in which case we say $X$ is **geometrically reduced**:

    - $\fiberprod{X}{k}{\bar{k}}$ is reduced;
    - $\fiberprod{X}{k}{k_p}$ is reduced, where $k_p$ denotes the perfect closure of $k$;
    - $\fiberprod{X}{k}{K}$ is reduced for all extension fields $K$ of $k$.

(c) We say that $X$ is **geometrically integral** if $\fiberprod{X}{k}{\bar{k}}$ is integral.
Give examples of integral schemes which are neither geometrically irreducible nor geometrically reduced.
:::

::: {.solution}
The proof is the Stacks Project's, transcribed step by step below. The
statements and proofs were read in the tag files
`tmp/sources/stacks-tags/<TAG>.md`, which are the site's build from
stacks-project commit `a04446e57ec1fbc252a871afcec7752fb2807b14` (28 July
2026). The printed pages are those of the retained compiled book
`tmp/sources/stacks-project-book.pdf` (7654 pages, whose PDF page is its
printed page), which is a different and older build, version `ed88ff78`
compiled 14 July 2026, and only the pages are taken from it. The two lemmas
that carry the two parts are
Lemma 33.8.9 (tag 038I, printed pp. 2832--2833,
`tmp/sources/stacks-tags/038I.md`), whose item (1) is irreducibility after
every field extension, and Lemma 33.6.4 (tag 035X, printed pp. 2821--2822,
`tmp/sources/stacks-tags/035X.md`, in Section 33.6, tag 035U). They rest on
Algebra, Lemma 10.47.3 (tag 037K, printed pp. 544--545,
`tmp/sources/stacks-tags/037K.md`) and Algebra, Lemma 10.44.4 (tag 030V,
printed p. 537, `tmp/sources/stacks-tags/030V.md`) for the affine charts.

The nine further lemmas and sections that the transcription cites are cited
by tag and were read in their tag files as well: Algebra 10.39.19 (tag
00HS, `tmp/sources/stacks-tags/00HS.md`, printed p. 525), 10.30.5 (tag
00FK, `tmp/sources/stacks-tags/00FK.md`, printed p. 495), 10.43.4 (tag
00I3, `tmp/sources/stacks-tags/00I3.md`, printed p. 534), 10.42.4 (tag
04KM, `tmp/sources/stacks-tags/04KM.md`, printed p. 532), 10.43.7 (tag
07K2, `tmp/sources/stacks-tags/07K2.md`, printed p. 535), 10.44.2 (tag
030W, `tmp/sources/stacks-tags/030W.md`, printed p. 536) and 10.25.1 (tag
00EU, `tmp/sources/stacks-tags/00EU.md`, printed p. 481), and the two
sections Properties 28.3 (tag 01OJ, `tmp/sources/stacks-tags/01OJ.md`) and
Schemes 26.17 (tag 01JO, `tmp/sources/stacks-tags/01JO.md`), each cited for
the one point it is used for: that a scheme affine over a field is reduced
exactly when its ring is, and that base change is gotten by gluing the
spectra of the tensor products over an affine cover.

Three facts of the same work are used below in the form in which the source
uses them.

1. A nonzero ring with at most one minimal prime has irreducible spectrum:
   the nilradical is then the unique minimal prime, hence prime, and its
   vanishing locus is the whole spectrum.

2. Algebra, Lemma 10.46.7 (tag 0BRA, printed p. 541,
   `tmp/sources/stacks-tags/0BRA.md`): if $\varphi:R\to S$ is
   a ring map with locally nilpotent kernel, generated as an $R$-algebra by
   elements $x$ with $x^{p^n}\in\varphi(R)$ and $p^nx\in\varphi(R)$ for some
   $n>0$ and some prime $p$, then $\varphi$ induces a homeomorphism of
   spectra, and every base change of $\varphi$ satisfies the same
   hypotheses. In particular $R\to k'\otimes_kR$ induces a homeomorphism of
   spectra for an algebraic purely inseparable field extension $k'/k$.

3. Lemma 33.8.8 (tag 038H, printed p. 2832,
   `tmp/sources/stacks-tags/038H.md`): for a separably algebraically
   closed field $k$, a field extension $k'/k$ and a $k$-scheme $X$, the
   morphism $X_{k'}\to X$ induces a bijection of irreducible components.

::: pf

::: {.pf-step #affine-irreducibility-tfae}
Let $R$ be a $k$-algebra. The following are equivalent:

1. $\Spec(R\otimes_kK)$ is irreducible for every field extension $K/k$;
2. $\Spec(R\otimes_kk')$ is irreducible for every finite separable field extension $k'/k$;
3. $\Spec(R\otimes_kk_s)$ is irreducible;
4. $\Spec(R\otimes_k\bar k)$ is irreducible.

::: pf-proof
This is Algebra, Lemma 10.47.3 (tag 037K), printed pp. 544--545, and the
proof below is its proof.

$(1)\Rightarrow(2)$ is clear.

$(2)\Rightarrow(3)$: let $\mathfrak q_1,\mathfrak q_2\subseteq R\otimes_kk_s$
be minimal prime ideals, and write $k_s=\bigcup k'$ over the finite
subextensions $k'/k$, each of which is separable. For such $k'$ the ring map
$R\otimes_kk'\to R\otimes_kk_s$ is flat, so by going down for flat ring maps
(Algebra, Lemma 10.39.19, tag 00HS, printed p. 525, `tmp/sources/stacks-tags/00HS.md`) the contractions
$\mathfrak p_i=(R\otimes_kk')\cap\mathfrak q_i$ are minimal primes of
$R\otimes_kk'$, and $(2)$ gives $\mathfrak p_1=\mathfrak p_2$. Since $k_s$ is
the union of the $k'$, it follows that $\mathfrak q_1=\mathfrak q_2$, so
$\Spec(R\otimes_kk_s)$ has one minimal prime and is irreducible by fact 1.

$(3)\Rightarrow(4)$: $\bar k/k_s$ is algebraic and purely inseparable, so by
fact 2 the ring map
$R\otimes_kk_s\to R\otimes_k\bar k=R\otimes_{k_s}\bar k$ induces a
homeomorphism of spectra, and irreducibility passes across it.

$(4)\Rightarrow(1)$: let $K/k$ be a field extension and choose a field $F$
containing both $K$ and $\bar k$ over $k$. Then
$$
R\otimes_kF=(R\otimes_k\bar k)\otimes_{\bar k}F,
$$
and $\bar k$ is separably closed, so by Algebra, Lemma 10.47.2 (tag 00I7,
printed p. 544, `tmp/sources/stacks-tags/00I7.md`) the tensor product of two $\bar k$-algebras with a unique
minimal prime has a unique minimal prime; by $(4)$ the ring $R\otimes_kF$ has
one minimal prime, hence irreducible spectrum. Finally
$R\otimes_kK\to R\otimes_kF$ is flat and injective, so every minimal prime of
$R\otimes_kK$ is the image of a minimal prime of $R\otimes_kF$ (Algebra,
Lemma 10.30.5, tag 00FK, printed p. 495, `tmp/sources/stacks-tags/00FK.md`, with
going down), and $R\otimes_kK$ has one minimal prime too.
:::

:::

::: {.pf-step #xbark-irred-implies-xk-irred}
If $X_{\bar k}$ is irreducible, then $X_K$ is irreducible for every field
extension $K/k$.

::: pf-proof
This is the proof of $(3)\Rightarrow(1)$ in Lemma 33.8.9 (tag 038I), printed
p. 2832.

Let $K/k$ be a field extension. Choose a field $\bar k'$ containing $\bar k$
such that $K$ embeds in $\bar k'$ over $k$. The field $\bar k$ is separably
algebraically closed, so by fact 3 the morphism
$X_{\bar k'}\to X_{\bar k}$ induces a bijection of irreducible components, and
$X_{\bar k'}$ is irreducible.

The projection $X_{\bar k'}\to X_K$ is surjective, being the base change of
the surjective morphism $\Spec\bar k'\to\Spec K$, and the image of an
irreducible space is irreducible. Hence $X_K$ is irreducible.
:::

:::

::: {.pf-step #xks-irred-implies-xbark-irred}
If $X_{k_s}$ is irreducible, then $X_{\bar k}$ is irreducible.

::: pf-proof
This is item $(3)\Rightarrow(4)$ of Algebra, Lemma 10.47.3 (tag 037K, printed
p. 544), recorded as step [](#affine-irreducibility-tfae){.pf-ref}, applied on
an affine cover and glued; it is not the proof of Lemma 33.8.9, whose second
paragraph proves the parallel statement for finite separable extensions.

The extension $\bar k/k_s$ is algebraic and purely inseparable. On an affine
open $U=\Spec R\subseteq X$ the ring map $R\otimes_kk_s\to R\otimes_k\bar k$
is of the form covered by fact 2, so
$\Spec(R\otimes_k\bar k)\to\Spec(R\otimes_kk_s)$ is a homeomorphism; these
homeomorphisms glue over an affine cover, so $X_{\bar k}\to X_{k_s}$ is a
homeomorphism.

A homeomorphism induces a bijection on irreducible closed subsets, so
$X_{k_s}$ irreducible forces $X_{\bar k}$ irreducible.
:::

:::

::: {.pf-step #irreducibility-tfae}
The three conditions of part (a) are equivalent.

::: pf-proof
If $X_{\bar k}$ is irreducible, then $X_K$ is irreducible for every $K$ by
step [](#xbark-irred-implies-xk-irred){.pf-ref}, and $X_{k_s}$ is irreducible
because $X_{\bar k}\to X_{k_s}$ is surjective, being a base change of the
surjective morphism $\Spec\bar k\to\Spec k_s$.

Conversely, $X_{k_s}$ irreducible gives $X_{\bar k}$ irreducible by step
[](#xks-irred-implies-xbark-irred){.pf-ref}, and irreducibility of $X_K$ for
every $K$ gives it for $K=\bar k$. This proves part (a).

The affine input is item $(3)\Rightarrow(4)$ of step
[](#affine-irreducibility-tfae){.pf-ref}, the purely inseparable base change
$k_s\to\bar k$; its other item, the finite separable extensions, is what
Lemma 33.8.9 uses in its own second paragraph, where it goes from the finite
separable subextensions of $k_s$ to $X_{k_s}$ itself. The two steps above
reach $X_{\bar k}$ from $X_{k_s}$ without that detour, because the
extension $\bar k/k_s$ is purely inseparable.
:::

:::

::: {.pf-step #affine-reducedness-tfae}
Let $X$ be a scheme over $k$. Then $X_K$ is reduced for every field extension
$K/k$ if and only if for every affine open $U\subseteq X$ the ring $\OO_X(U)$
is geometrically reduced over $k$.

::: pf-proof
This is the second and third paragraphs of the proof of Lemma 33.6.4
(tag 035X, `tmp/sources/stacks-tags/035X.md`), printed p. 2822.

Assume $X_K$ is reduced for every $K$; the source states this as its
condition (1), that $X$ is geometrically reduced, which for it means that
for every $K$ and every point $x'\in X_K$ the local ring of $X_K$ at $x'$ is
reduced, an equivalent form since reducedness of a scheme is reducedness of
all its local rings.

Now let $U\subseteq X$ be affine open. Since $X_K$ is reduced, its open
subscheme $U_K=\Spec(\OO_X(U)\otimes_kK)$ is reduced, hence the ring
$\OO_X(U)\otimes_kK$ is reduced, a scheme affine over a field being reduced
exactly when its ring is (Properties, Section 28.3, tag 01OJ,
`tmp/sources/stacks-tags/01OJ.md`). So
$\OO_X(U)$ is geometrically reduced.

Conversely, if every $\OO_X(U)$ is geometrically reduced, then for any $K$
the scheme $X_K$ is obtained by gluing the spectra of the rings
$\OO_X(U)\otimes_kK$ over an affine cover (Schemes, Section 26.17, tag 01JO,
`tmp/sources/stacks-tags/01JO.md`), each of
them reduced, so $X_K$ is reduced.
:::

:::

::: {.pf-step #purely-inseparable-reducedness-tests}
Let $S$ be a $k$-algebra, and let $k_p=k^{perf}$ be the perfect closure of
$k$. The following are equivalent:

1. $k'\otimes_kS$ is reduced for every finite purely inseparable extension $k'/k$;
2. $k^{1/p}\otimes_kS$ is reduced;
3. $k_p\otimes_kS$ is reduced;
4. $\bar k\otimes_kS$ is reduced;
5. $S$ is geometrically reduced over $k$, that is $K\otimes_kS$ is reduced for every field extension $K/k$.

::: pf-proof
This is Algebra, Lemma 10.44.4 (tag 030V), printed p. 537,
`tmp/sources/stacks-tags/030V.md`, and the
proof below is its proof. When $k$ has characteristic zero every field
extension of $k$ is separable and the assertion is Algebra, Lemma 10.43.6
(tag 030U, printed p. 534, `tmp/sources/stacks-tags/030U.md`).

Every finite purely inseparable extension $k'/k$ embeds in $k_p$, and
$k^{1/p}\subseteq k_p\subseteq\bar k$. For $k\subseteq L\subseteq K$ among
these fields the map
$L\otimes_kS\to K\otimes_kS=K\otimes_L(L\otimes_kS)$ is injective, $K$ being
flat over the field $L$, so $L\otimes_kS$ is a subring of $K\otimes_kS$, and a
subring of a reduced ring is reduced. That is what makes
$(5)\Rightarrow(4)\Rightarrow(3)\Rightarrow(2)$ and $(3)\Rightarrow(1)$
immediate, the larger field being the one whose tensor is assumed reduced; it
is not that reducedness survives a base change to a larger field, which is
false: over $k=\FF_p(u)$ the field $S=k[x]/(x^p-u)$ is reduced, while
$k^{1/p}\otimes_kS\cong k^{1/p}[x]/((x-u^{1/p})^p)$ is not.

$(1)\Rightarrow(5)$: let $K/k$ be a field extension; $K\otimes_kS$ is to be
reduced. By Algebra, Lemma 10.43.4 (tag 00I3, printed p. 534,
`tmp/sources/stacks-tags/00I3.md`) it suffices to treat
finitely generated $K$, and then Algebra, Lemma 10.42.4 (tag 04KM, printed
p. 532, `tmp/sources/stacks-tags/04KM.md`)
provides a diagram $k\subseteq k'\subseteq K'$, $K\subseteq K'$ with $k'/k$
and $K'/K$ finite purely inseparable and $K'/k'$ separably generated. By
$(1)$ the ring $k'\otimes_kS$ is reduced, so by Algebra, Lemma 10.43.6 the
ring
$$
K'\otimes_kS=K'\otimes_{k'}(k'\otimes_kS)
$$
is reduced, being a separably generated base extension of a reduced algebra
over $k'$. The ring $K\otimes_kS$ is a subring of it, so it is reduced.

$(2)\Rightarrow(5)$: assume $k^{1/p}\otimes_kS$ is reduced. Then $S$ is
reduced, since $S$ embeds in $k^{1/p}\otimes_kS$. For a minimal prime
$\mathfrak p$ of $S$ the ring $k^{1/p}\otimes_kS_{\mathfrak p}$ is a
localization of $k^{1/p}\otimes_kS$, hence reduced, and
$S_{\mathfrak p}$ is a field (Algebra, Lemma 10.25.1, tag 00EU, printed p. 481,
`tmp/sources/stacks-tags/00EU.md`), hence geometrically
reduced by Algebra, Lemma 10.44.2 (tag 030W, printed p. 536,
`tmp/sources/stacks-tags/030W.md`), which identifies
geometric reducedness of a field extension with separability. Then $S$ is
geometrically reduced by Algebra, Lemma 10.43.7 (tag 07K2, printed p. 535,
`tmp/sources/stacks-tags/07K2.md`), since a
reduced algebra all of whose localizations at minimal primes are
geometrically reduced is geometrically reduced.
:::

:::

::: {.pf-step #reducedness-tfae}
The three conditions of part (b) are equivalent.

::: pf-proof
Step [](#affine-reducedness-tfae){.pf-ref} identifies reducedness of $X_K$ for
all $K$ with geometric reducedness of the rings $\OO_X(U)$ on affine opens,
and step [](#purely-inseparable-reducedness-tests){.pf-ref} gives, for each
such ring $S$, the equivalence of the four base-change tests with geometric
reducedness of $S$.

It remains to pass from the rings to the scheme. If $X_{\bar k}$ is reduced
then each $\OO_X(U)\otimes_k\bar k$ is reduced, so each $\OO_X(U)$ is
geometrically reduced by the equivalence of the previous step, and then
$X_K$ is reduced for every $K$ by step
[](#affine-reducedness-tfae){.pf-ref}. Conversely if $X_{k_p}$ is reduced then
each $\OO_X(U)\otimes_kk_p$ is reduced, so each $\OO_X(U)$ is geometrically
reduced, and again every $X_K$ is reduced, in particular $X_{\bar k}$. This
proves part (b).
:::

:::

::: {.pf-step #integral-not-geom-irreducible}
An integral scheme need not be geometrically irreducible.

::: pf-proof
Take
$$
k=\RR,
\qquad
X=\Spec\CC
$$
with its natural structure as an $\RR$-scheme.  Since $\CC$ is a field, $X$ is integral.

After base change to $\CC$,
$$
\CC\otimes_{\RR}\CC
\cong
\CC\times\CC.
$$
Thus
$$
X_\CC
\cong
\Spec\CC\amalg\Spec\CC
$$
is reducible.  Hence $X$ is not geometrically irreducible.
:::

:::

::: {.pf-step #integral-not-geom-reduced}
An integral scheme need not be geometrically reduced.

::: pf-proof
Let
$$
k=\FF_p(u)
$$
and set
$$
X=\Spec k[x]/(x^p-u).
$$
The element $u$ is not a $p$th power in $k$: its valuation at the prime $u$ is $1$, whereas a $p$th power has valuation divisible by $p$.  Hence
$$
x^p-u
$$
is irreducible over $k$, so the quotient is a field and $X$ is integral.

After adjoining $u^{1/p}$,
$$
x^p-u=(x-u^{1/p})^p.
$$
Therefore
$$
X_{k(u^{1/p})}
\cong
\Spec k(u^{1/p})[x]/(x-u^{1/p})^p
$$
is nonreduced.  Thus $X$ is not geometrically reduced.
:::

:::

::: {.pf-step #integral-neither-example}
There are integral schemes which are simultaneously neither geometrically irreducible nor geometrically reduced.

::: pf-proof
Let
$$
k=\FF_p(u,v),
$$
and let $w$ satisfy the Artin--Schreier equation
$$
w^p-w=v.
$$
This polynomial is separable because its derivative is $-1$.  It has no root in $k$: using the valuation at infinity in the variable $v$, normalized by
$$
\operatorname{ord}_\infty(v)=-1,
$$
one has
$$
\operatorname{ord}_\infty(r^p-r)
$$
either nonnegative, or a negative integer divisible by $p$, and therefore never $-1$.  An Artin--Schreier polynomial $T^p-T-v$ with no root is irreducible.  Thus
$$
L=k(w)
$$
is a finite separable extension of degree $p$.

Now put
$$
E=L(u^{1/p}),
\qquad
X=\Spec E.
$$
The element $u^{1/p}$ cannot lie in $L$: otherwise the nontrivial purely inseparable extension
$$
k(u^{1/p})/k
$$
would be a subextension of the separable extension $L/k$.  Hence
$$
[E:L]=p.
$$
Hence $E$ is a field and $X$ is integral.

Over an algebraic closure $\bar k$, the separable extension $L/k$ splits into $p$ distinct embeddings, while the purely inseparable equation becomes a $p$th power.  Consequently
$$
E\otimes_k\bar k
\cong
\prod_{j=1}^{p}
\bar k[\epsilon]/(\epsilon^p).
$$
This ring has more than one minimal prime and has nonzero nilpotents.  Therefore $X_{\bar k}$ is both reducible and nonreduced, so $X$ is neither geometrically irreducible nor geometrically reduced.
:::

:::

::: pf-qed
Step [](#irreducibility-tfae){.pf-ref} proves part (a), step [](#reducedness-tfae){.pf-ref} proves part (b), and steps [](#integral-not-geom-irreducible){.pf-ref}, [](#integral-not-geom-reduced){.pf-ref} and [](#integral-neither-example){.pf-ref} give the examples requested in part (c).
:::

:::

:::

::: {.remark}
Irreducibility of $X_K$ is weaker than reducedness, or domain-ness, of the corresponding ring, but over an algebraically closed base field the failure cannot come from a domain. Let $A$ be a domain of finite type over $k$ and let $K=\Frac(A)$. If $k$ is algebraically closed then $\bar k=k$, so $\Spec(A\otimes_kK)$ is irreducible by step [](#irreducibility-tfae){.pf-ref}, and $A\otimes_kK$ is reduced because $K/k$ is separable, $k$ being perfect, by Algebra, Lemma 10.43.6 (tag 030U, printed p. 534, `tmp/sources/stacks-tags/030U.md`); a reduced ring whose spectrum is irreducible is a domain. So a domain of finite type over an algebraically closed field stays a domain after extending scalars to its fraction field. A perfect base field is not enough: over $k=\RR$ the field $A=\CC$ is a domain, while $A\otimes_k\Frac(A)=\CC\otimes_\RR\CC\cong\CC\times\CC$ has two minimal primes, which is step [](#integral-not-geom-irreducible){.pf-ref}.

The phenomenon needs a non-perfect base: over $k=\FF_p(u)$ the ring $A=k[x]/(x^p-u)$ is a field, so it is reduced and its spectrum is irreducible, while for $K=A$ and $\alpha$ the image of $x$ in $K$,
$$
A\otimes_kK\cong K[x]/((x-\alpha)^p)
$$
has a nonzero nilpotent; that is step [](#integral-not-geom-reduced){.pf-ref}. So when $k$ is not perfect, a domain $A$ can acquire nilpotents after extending scalars to $K=\Frac(A)$, and irreducibility of $X_K$ is a statement about the minimal primes of $A\otimes_kK$ rather than about whether that ring is a domain.
:::

::: {.remark title="Published solution"}
Both parts are proved in full in the Stacks Project, with the same closures that Hartshorne's list uses, and the two parts of the solution above are that proof transcribed. Part (a) is Lemma 33.8.9 (tag 038I, printed pp. 2832--2833, `tmp/sources/stacks-tags/038I.md`), whose three items are "$X$ is geometrically irreducible over $k$", where geometric irreducibility is irreducibility after every field extension by definition, "$X_{k'}$ is irreducible for every finite separable field extension $k'/k$" and "$X_{\bar k}$ is irreducible, where $k\subset\bar k$ is a separable algebraic closure of $k$"; these are Hartshorne's three conditions. Step `xbark-irred-implies-xk-irred` is that proof's first paragraph; step `xks-irred-implies-xbark-irred` is not the second, which runs the other way, from finite separable subextensions to the separable closure, and rests on Algebra, Lemma 10.47.3 (tag 037K) applied on affine opens. What the card's second step uses is item $(3)\Rightarrow(4)$ of the same lemma, the purely inseparable passage from $k_s$ to $\bar k$, and that is the item carried out, with the lemma's other items, in step `affine-irreducibility-tfae` (tag 037K, printed pp. 544--545, `tmp/sources/stacks-tags/037K.md`). Part (b) is Lemma 33.6.4 (tag 035X, in Section 33.6, which is tag 035U, printed pp. 2821--2822, `tmp/sources/stacks-tags/035X.md`), which lists as equivalent: $X$ geometrically reduced; $X_{k'}$ reduced for every field extension $k'/k$; $X_{k'}$ reduced for every finite purely inseparable $k'/k$; $X_{k^{1/p}}$ reduced; $X_{k^{perf}}$ reduced; $X_{\bar k}$ reduced; and, as its item (7), geometric reducedness of the rings $\OO_X(U)$ on the affine opens $U$. The $k_p$ of the exercise is $k^{perf}$, so items (2), (5) and (6) are exactly the three conditions of part (b). The equivalence of those conditions is Algebra, Lemma 10.44.4 (tag 030V, printed p. 537, `tmp/sources/stacks-tags/030V.md`), transcribed in step `purely-inseparable-reducedness-tests`, and the passage from the rings on affine opens to the scheme is step `affine-reducedness-tfae`, whose two paragraphs are the second and third of the proof of 035X, printed p. 2822.

What the two steps do not get from the source is part (c). The three examples are the card's own: $\Spec\CC$ over $\RR$, $\Spec\FF_p(u)[x]/(x^p-u)$ over $\FF_p(u)$, and $\Spec E$ with $E=L(u^{1/p})$ over $\FF_p(u,v)$ for an Artin--Schreier extension $L=k(w)$, none of which the Stacks Project states.

Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter II §3, Exercise 3.15, PDF pp. 26--27, text version `tmp/sources/hartshorne-solutions-kim.md`, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: for (a) Kim reduces a reducible $X_K$ to an affine chart with $A\otimes_kK$ reducible, extracts non-nilpotent $f_1,f_2$ with $f_1f_2=0$, and then asserts that the resulting finitely many polynomial conditions, which have a solution over the algebraically closed field $K$, have one over a finite extension of $k$; a finite purely inseparable base change of a separably closed $k$ is a homeomorphism, which would finish the argument.
That descent is asserted rather than proved, and it fails on the natural reading: a purely inseparable extension of a separably closed but non-perfect $k$ need not have a $k$-point, so a solution over $K$ does not specialize to one over $k$.
The proof above replaces it by the cited Lemma 10.47.3 and keeps Kim's two reductions, that purely inseparable base change is a homeomorphism and that extension of scalars over an algebraically closed field preserves the set of minimal primes.
Agree on the reduction, not on the descent step.  For (b) Kim uses the trace form of a Galois extension; the proof above uses the cited Lemma 10.43.6 over the perfect closure.
:::
