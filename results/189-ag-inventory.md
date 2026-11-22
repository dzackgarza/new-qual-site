# #189: `wiki/algebraic-geometry/` — reading and adjudication inventory

Scope: every page of `wiki/algebraic-geometry/` (82 files, 3767 lines), read against the policy set named in
#175 and against the numbered statements of the sources each page cites.
This is a read-only adjudication: no page prose (that is #188) and no card (that is #187) is edited by this file.

## 1. Snapshot, method, coverage

- **Snapshot.** First pass: `698a059f47` (the tip when the reading began). Every line number below is the state at
  `5e96c6f622`. Ten commits by the #175/#187/#188 lanes landed in this subtree during the reading; the nine pages
  they touched were re-read at the final snapshot:
  `schemes/what-is-a-scheme`, `schemes/ringed-spaces`, `schemes/proj-and-gluing`, `schemes/subschemes-and-points`,
  `schemes/properties-from-the-ring`, `schemes/normalization`, `schemes/fibre-products-and-base-change`,
  `stacks-and-moduli/functors-and-topologies`, `curves-and-surfaces/special-divisors-and-the-canonical-map`.
  The other 73 pages were unchanged between the two snapshots
  (`git diff --name-only 698a059f47..5e96c6f622 -- wiki/algebraic-geometry`). The lanes are still writing: re-check a
  line before repairing it.
- **Sources actually opened.** `tmp/sources/hartshorne-1977-algebraic-geometry.md` (every Hartshorne number below was
  read in this text version, not from memory), `tmp/sources/vakil-rising-sea-2025-10-21.md` (Theorem 12.4.3 read
  verbatim), `tmp/sources/cox-little-schenck-2011-toric-varieties.md` (Proposition 1.1.9),
  `https://stacks.math.columbia.edu/tag/0G12` (fetched live), `vocabularies/macros.json`,
  `vocabularies/references.yaml`, `sources/attachment-extraction-ledger.jsonl`.
  Policies: `CONTRIBUTING.md` (read in full) and the shared writing policy's `section-structure.md`,
  `citations.md`, `prose.md`, `prose-tells.md`, `definitions.md`, `resource-descriptions.md`.
- **Coverage claim, deliberately bounded.** All 82 pages were read in full. The numbered statements checked against
  a source are listed per page in §6; a page marked clean there is a page on which *this* reading found no defect —
  not a page certified free of them, which no reading of this kind establishes. §7 lists what stayed undecided and
  why: statements carried on transcluded cards I did not open, and two locators whose book is not on the machine.
- **No gate was run** for this file. It touches no `corpus/`, `wiki/` or `vocabularies/` path.
- One sibling commit, `b27109aeb5` (a `COMPLAINTS.md` entry for `PR-VGA2L`), was already on local `main` and
  unpushed when this file was committed; it travels with this push and is not mine.

## 2. Every statement flagged in #175, decided

Each row gives the location in its **current** state (the flagged text is frequently gone; where it is, the decision
records what the page now says), the decision, and the numbered statement that decides it.

| # | Location | Current state and decision | Source statement read |
|---|---|---|---|
| 1 | `cohomology/homological-algebra.md:21-22` | **Repaired, true.** "In $\mods{\OO_X}$ the cokernel is the cokernel sheaf, the sheafification of $U\mapsto\coker(f(U))$ … In $\mods{A}$ nothing needs sheafifying and the cokernel is the quotient $N/\im f$." The flagged claim that a cokernel is naive in neither category is gone; the cokernel of $A$-modules **is** the naive quotient. | Har77 II.1.2 (sheafification) — **not opened in this pass**; the cokernel-sheaf definition is `D-A7LCT`'s, and the claim is the standard separation of presheaf from sheaf cokernel |
| 2 | `curves-and-surfaces/crepant-resolutions.md:18,32-34` | **Repaired, true.** The three flagged sentences (a $(-2)$-curve cannot be contracted; crepant resolutions exist for Gorenstein canonical singularities in dimension three; terminal singularities admit none) are no longer on the page. What replaces them is right: a blowup of a smooth point has $K_{\tilde X}=\pi^*K_X+(n-1)E$; a $(-2)$-curve **is** contractible (Artin), to a du Val point, and that contraction is crepant. Crepancy checked by hand: $E\cdot K_X=0$ (adjunction, $E^2=-2$) and $E\cdot f^*K_{X_0}=f_*E\cdot K_{X_0}=0$, so the discrepancy coefficient is $0\cdot E^2=0$. | Har77 V.5.7 (Castelnuovo), Cor V.5.4, `D-SRFADE` |
| 3 | `curves-and-surfaces/riemann-hurwitz.md:18` | **Repaired, true.** "At a tamely ramified point $\length(\Omega_{X/Y})_p=e_p-1$, and at a wildly ramified point $\length\ge e_p$; so $\deg R=\sum_p(e_p-1)$ holds exactly when no point is wildly ramified." No "$d_p=e_p-1+(\text{correction divisible by }p)$" remains. | Har77 Proposition IV.2.2 (items (a)–(c) read) and Corollary IV.2.4 (Hurwitz, read) |
| 4 | `divisors/class-group-and-picard-group.md:12-18` | **Repaired, true.** $\CaCl(X)\iso\Pic(X)$ is asserted for an *integral* scheme (correct, no factoriality needed); the Weil/Cartier inclusion is asserted to be an isomorphism only under "every local ring is a UFD", and the strictness sentence keeps the quadric cone as its example. Confirmed against the book: $\CaCl=0$ while $\Cl\iso\ZZ/2\ZZ$ on the quadric cone, so the inclusion is strict there. | Har77 Proposition II.6.15, Proposition II.6.11, Corollary II.6.16, Remark II.6.11.1A, Example II.6.11.3 (all read) |
| 5 | `morphisms/projective-morphisms.md:46-48` | **Repaired, true.** Ampleness is preserved by restriction to a closed subscheme and by pullback along a *finite* morphism, is invariant under a finite surjective pullback when both are proper, and "is not preserved by pullback along an arbitrary morphism", with the blowup at a point and $\pi^*\cL\cdot E=L\cdot\pi_*E=0$. The claimed unconditional stability under pullback is gone. | Har77 Theorem II.7.6, Exercise III.5.7(d), Theorem V.1.10 (Nakai–Moishezon) |
| 6 | `schemes/dimension.md:43-52` | **Decided, true — and the page now states the distinction the flag collapsed.** Two functions are separated: the dimension of the *largest component* of $X_{f(x)}$ through $x$ is upper semicontinuous on $X$ (Vakil 12.4.3(a), read verbatim), while the local dimension $\krulldim\OO_{X_{f(x)},x}$ is not, with $\AA^1_k\to\Spec k$ as the witness (dimension $1$ at closed points, $0$ at $\eta$). The target-side statement is quoted with its closedness/properness hypothesis (12.4.3(b)) and refuted without it by $\AA^1\sm\{0\}\into\AA^1$. | Vakil, *Rising Sea*, Theorem 12.4.3(a),(b) |
| 7 | `schemes/ringed-spaces.md:26-27` | **Repaired, true.** The gluing claim is now the injectivity of $\mcf(U)\to\prod_{p\in U}\mcf_p$ (axiom 3), followed by "injectivity is not the gluing axiom … the product of the stalks imposes no compatibility". Nothing calls the structure sheaf a subsheaf of the product of its stalks any more. | Har77 §II.1 (sheaf axiom 3) |
| 8 | `sheaves/pushforward-and-pullback.md:13,27-29` | **Repaired, true.** `:13` names $j_!$, $Rf_!$ and $f^!$ with where they exist, so "the two functors are the only ones available" is gone; `:28` says $f^{-1}$ preserves direct sums and $f_*$ preserves products, kernels and fibre products; `:29` gives the counterexample, $\left(f_*(\oplus_i\mcf_i)\right)(\mathrm{pt})=\prod_i\ZZ$ against $\oplus_i\ZZ$. Verified. | adjunction left/right exactness; own computation |
| 9 | `sheaves-of-modules/tangent-normal-and-canonical-sheaves.md:45-46,52-60` | **Repaired, true.** The order is now local complete intersection $\Rightarrow$ Gorenstein $\Rightarrow$ invertible dualizing sheaf ($D$ a divisor in a smooth $X$ is lci because its ideal is generated by a regular sequence of length $1$; hence Gorenstein). Adjunction is stated with restrictions: $\omega_Y\iso\restrictionof{\omega_X}{Y}\otimes\bigwedge^r\mcn_{Y/X}$ and $\omega_Y\iso\restrictionof{(\omega_X\otimes\mcl)}{Y}$. No `\inverseof{i}\Omega_X` remains in this page or in `riemann-hurwitz.md` (checked by search). | Har77 Proposition II.8.20, §II.8 (lci) |
| 10 | `toric/examples.md:40,61,45` | **Repaired, true.** The determinant-seven cone is $\Cone((2,1),(1,4))$ with determinant $2\cdot4-1\cdot1=7$ — not the quadric cone (which is $(0,1),(2,-1)$, `:36`, `affine-computations.md:36`). "Every smooth complete toric surface is $\PP^2$, a Hirzebruch surface $\FF_a$, or a blowup of one of these at torus-fixed points" replaces "every toric surface from $\PP^2$". "Every toric variety is a fan" is replaced by "a fan $\Sigma$ gives a normal toric variety $X_\Sigma$", and `:45` says the cuspidal cubic is *not* of the form $X_\Sigma$. Minimal-resolution self-intersections checked by hand: $u_0+u_2=3u_1$, $u_1+u_3=2u_2$, $u_2+u_4=2u_3$, giving $(-3,-2,-2)$ as printed. | own computation; CLS Proposition 1.1.9 read for D4 below, the fan criteria not re-read |
| 11 | `toric/topology.md:31,55,47` | **Decided — two of the three were never defects.** `:31` the affine quadric cone has trivial $\pi_1$ (the owner's `c4a`-ruling at #175 is correct: the cone's lattice points generate $N$, and the cone retracts to its vertex). `:55` the moment-map fibre over the relative interior of a $k$-face is the compact torus $(S^1)^k$, and the preimage is the orbit of complex dimension $k$; the page states exactly this and explicitly denies being a torus bundle over $P$. `:47` the cohomology ring is the Stanley–Reisner ring, not "the faces of the fan as generators". | the owner's #175 ruling plus the page's own computation; `D-TORMOMENT` was not opened and the Fulton §4.2 locator was not verified (§7) |
| 12 | `toric/toric-del-pezzo-surfaces.md:55-59,66` | **Repaired, true.** The anticanonical polytope is $P_{-K}=\{m:\inner{m}{u_\rho}\ge-1\ \forall\rho\}$; there is no "lattice distance two" and no reference to a table the page lacks. `K^2=12-d` checked: $3,4,4,5,6$ rays give $9,8,8,7,6$. The obstruction to the fourth blowup is right: adjunction gives $-K\cdot C=2+C^2=0$ on a $(-2)$-curve. | Har77 Theorem V.1.10; own computation |
| 13 | `varieties/rational-maps.md:48` | **Repaired mathematically, citation still wrong — see D6.** "The indeterminacy locus of a birational map from a normal variety to a projective variety has codimension at least two" is the correct statement (a birational map is *not* an isomorphism in codimension one). The supporting numbers do not state it. | Har77 V.5.1 (fundamental points of a birational map codim $\ge2$), II.6.3A |
| 14 | `varieties/projective-varieties.md:41-44` | **Repaired, true.** The Segre image is the closed subscheme cut out by the $2\times2$ minors; for $m=n=1$ the single minor $z_{00}z_{11}-z_{01}z_{10}$ is the smooth quadric in $\PP^3$; the product of projective varieties is projective because $\sigma(X\times Y)$ is closed in $\sigma(\PP^m\times\PP^n)$. | own check of the two-by-two minors; Har77 Exercise I.2.14 (Segre) not opened |
| 15 | the dominance hypothesis on maps to $\PP^n$ (`rational-maps.md:22,26`) | **Repaired.** Dominance is now attached only to the pullback of functions on a general target ("the [[D-VARBIRAT\|dominant]] rational maps $X\dashrightarrow Y$ pull functions back"), and the tuple description of $X\dashrightarrow\PP^n$ carries no dominance hypothesis, which is correct. | Har77 Theorem II.7.1 |

Two flagged items from #175 need no repair and should be closed in the parent rather than in #187:

- `toric/topology.md:31` (affine cone $\pi_1$) — the reader's $\ZZ/2$ claim is wrong, as #175's second verdict established.
- the eleven "chapters not yet written" — all eleven now carry authored prose; their *mathematics* is adjudicated in §6.

## 3. The two locations #189 names explicitly

Both were repaired on `main` **before** this reading, by the #187 lane; recording them, not duplicating them.

- **`corpus/theory/Algebraic_Geometry/PR-RJ3P7.md`** — repaired at `2734e61c70`. `:51` is now the height statement
  ("Going down is what makes heights match, $\operatorname{ht}\mfq=\operatorname{ht}(\mfq\cap A)$, under its
  hypotheses"), and the hypotheses the flagged version dropped are on the page: `:47` puts surjectivity where it
  belongs (lying over, which needs $\phi$ injective, with $\ZZ\to\ZZ/2$ missing the generic point) and `:49` makes the
  dimension equality a statement about an integral extension $A\subseteq B$, "a finite morphism need not preserve the
  dimension of its target". Checked against Atiyah–Macdonald 5.10/5.11/5.16 and Stacks 01WM (closedness) and 01WH
  (finiteness). **No surviving defect; nothing for #187.**
- **`corpus/theory/Algebraic_Geometry/T-FFDESCENT.md:71`** — repaired at `1287f30106`. The recovered module is
  $\{n\in N:\theta(n\otimes1)=1\otimes n\}$ under $\CC\otimes_{B,p_1}N\cong N\otimes_AB$ and
  $\CC\otimes_{B,p_2}N\cong B\otimes_AN$, which is the standard Amitsur equalizer and is what makes
  $\theta(n\otimes1)=1\otimes n$ well typed; the reversed factors are gone. The only residual is that the convention
  behind $\otimes_{B,p_i}$ is left implicit (notational, not false). **No surviving defect; nothing for #187.**

## 4. Defects found by this reading and still present at `b27109aeb5`

Ordered by severity. "Repair target" names the file that owns the fix; the page prose is #188's, the cards #187's,
and a page line that states false mathematics is #187's under #175's own split.

### D1 (mathematics, false as written) `cohomology/derived-functors-and-vanishing.md:46`

    hence $H^1(X,j_!\ZZ_U)\cong\ZZ^2/\ZZ\neq0$, so affine vanishing fails for a quasicoherent
    sheaf that is not coherent [@Har77, Exercise III.2.1].

The example is Hartshorne's Exercise III.2.1(a), read: $X=\AA^1_k$ over an infinite field, $P\ne Q$ closed points,
$U=X-\{P,Q\}$, and it shows $H^1(X,\ZZ_U)\ne0$ for the extension by zero — a sheaf of abelian groups that is
**not quasicoherent**. The clause says the opposite of what the example shows and of what the block's own title says
("Quasicoherence cannot be dropped"); `sheaves/pushforward-and-pullback.md:49` says of the same construction "it is
not quasicoherent", so the two pages contradict each other. Repair: "so affine vanishing of *quasicoherent* sheaves
cannot be extended to sheaves of abelian groups" (or delete the clause; the title already carries the point).
Source: Har77 Exercise III.2.1(a).

### D2 (mathematics, off by one) `curves-and-surfaces/special-divisors-and-the-canonical-map.md:49`

    For $K$ to be very ample one needs $\ell(K-p-q)=g-3$ for every pair of points, including
    $p=q$, and Riemann--Roch converts this into $\ell(p+q)=1$

Hartshorne's criterion (Proposition IV.3.1(b), read) is $\dim|D-P-Q|=\dim|D|-2$; with $D=K$ and $\dim|K|=g-1$
that is $\dim|K-p-q|=g-3$, i.e. **$\ell(K-p-q)=g-2$**, not $g-3$, since $\ell=\dim+1$. The page's own next clause
proves the intended value: Riemann–Roch on $p+q$ gives $\ell(p+q)-\ell(K-p-q)=3-g$, which is $1$ exactly when
$\ell(K-p-q)=g-2$ (the printed $g-3$ would force $\ell(p+q)=0$, impossible for a divisor of degree $2$ on a curve).
`divisors/line-bundles-and-linear-systems.md:30` states the same criterion correctly in $\ell$-form
($\ell(D-p-q)=\ell(D)-2$), so this is a one-page slip, not a corpus convention.
Repair: $\ell(K-p-q)=g-2$ (or write $\dim\linearsystem{K-p-q}=g-3$). Source: Har77 Proposition IV.3.1(b).

### D3 (rendering, no gate catches it) `schemes/properties-from-the-ring.md:18`

    ... the topological noetherian condition: $\sp(\Spec A)$ is a noetherian topological space ...

`\sp` is not among the 346 macros in `vocabularies/macros.json` and is not a LaTeX or AMS command; it occurs exactly
once in the 82 pages (a check of every `\word` token against `macros.json` plus the standard command set returns this
one entry and no other). It is Hartshorne's own notation — his Exercise II.2.13 writes `sp(X)` — which is presumably
how it arrived. Repair: `\underlyingspace{\Spec A}` (the corpus macro for the underlying space) or plain prose.
Source: Har77 Exercise II.2.13 (read: parts (c) and (d) are exactly the two assertions the sentence makes).

### D4 (CITE-1, and the precedent is #175's) `toric/affine-computations.md:14`

    ... generated by the binomials $x^a-x^b$ for the relations $\sum a_im_i=\sum b_im_i$
    [Cox--Little--Schenck, *Toric Varieties*, Proposition 1.1.9].

The number is right — CLS Proposition 1.1.9 is "the ideal of the affine toric variety $Y_{\mathcal A}\subseteq\CC^s$"
generated by those binomials — but the citation is unkeyed inline author–title, the form #175's third verdict rejected
for `D-VARSEVBRAUER`'s Serre references. It is the only unkeyed inline reference left in the 82 pages (every
`[@Key]` used here — 21 keys — exists in `vocabularies/references.yaml`). Repair target belongs to the orchestrator:
a Zotero item and key for CLS, then `[@CLS11, Proposition 1.1.9]`; the page cannot be repaired by hand-editing
`references.yaml`.

### D5 (CITE-8) `varieties/rational-maps.md:48`

    ... a rational differential form on a nonsingular variety whose domain of definition misses a
    closed subset of codimension two extends across it [@Har77, Theorem II.8.19 and Exercise II.8.8].

The statement is true. Neither cited number states it: Theorem II.8.19 is "let $X,X'$ be birationally equivalent
nonsingular projective varieties over $k$; then $p_g(X)=p_g(X')$", and Exercise II.8.8 asks for the birational
invariance of the plurigenera and Hodge numbers. The extension step is Hartshorne's own use of **Proposition II.6.3A**
(inside the proof of 8.19: on an affine $U$ with $\omega_X|_U\cong\OO_U$, $\Gamma(U,\OO_U)\to\Gamma(U\cap V,\OO_U)$ is
bijective because $U-(U\cap V)$ has codimension $\ge2$), applied after trivialising $\omega_X$ locally. Repair:
cite II.6.3A and say the form is an $\OO_U$-multiple of a local generator.

### D6 (CITE-8) `curves-and-surfaces/curves-in-projective-space.md:19`

    Every irreducible curve of degree $d$ spanning $\PP^d$ is rational normal, so degree $d$ and
    span $\PP^d$ determine the curve up to projective equivalence.

True (Castelnuovo's bound with $r=d$ gives $g\le0$, and a rational curve of degree $d$ spanning $\PP^d$ is the
$d$-uple embedding), but it is asserted with no argument, no link and no citation, and the page transcludes the bound
`T-CRVCAST` twenty lines below. Repair: cite Castelnuovo's bound (the page's own `T-CRVCAST`, or Har77 IV.6.4) at the
sentence, or drop the sentence — the previous line already carries the cited naming (`Exercise IV.3.4`, read:
"let $X$ be the $d$-uple embedding … we call $X$ the rational normal curve of degree $d$").

### D7 (CITE-8, small) `varieties/projective-varieties.md:18`

    A homogeneous ideal need not cut out anything: $V(J)$ is empty exactly when $\sqrt J$ contains
    the irrelevant ideal $S_+$ ... [@Har77, Exercise I.2.4].

Two statements, one number. Exercise I.2.4(a) (read) is the inclusion-reversing bijection with homogeneous radical
ideals **other than** $S_+$ — the second clause. The empty-set criterion is Exercise **I.2.2** (read: $Z(\mathfrak a)=\emptyset$
iff $\sqrt{\mathfrak a}=S$ or $S_+$). Repair: cite I.2.2 for the criterion and I.2.4 for the correspondence.

### D8 (PROVENANCE-01, with the page's own claim falsified) `syllabus.md`

- `:10` says "A section names the document whose list it transcribes, and where the list is a topic outline it names
  the reading that covers the topics instead." Four of the eight sections name no document: `:149` ("Varieties,
  schemes, cohomology and curves"), `:163` ("Complex algebraic surfaces"), `:183` ("Toric varieties"), `:197`
  ("Complex algebraic geometry (minor topic)"). Each opens with "The numbered items group the topics by subject."
  (`:151`, `:165`, `:185`, `:199`) and then gives reading pointers. The two sections that are syllabi name theirs (`:15` Harvard syllabus, `:37` Berkeley
  syllabus) and two name Hartshorne's contents (`:69`, `:107`). So the page's first sentence is false as written and
  the provenance of four lists is unrecorded.
- `:167` gives Miles Reid, *Chapters on Algebraic Surfaces* (Park City, 1993) with eight specific section locators
  ("Chapter B, §B.9 (item ix)", "§C.5.6 (item 3)", …) as an unkeyed inline reference. This is #175's rejected form
  again; the work is not in `references.yaml`. Repair target: an orchestrator Zotero item and key, then
  `[@Reid97, …]`; the locators cannot be checked against a text that is not on the machine (see §7).
- `:37` is a qualifying-exam "syllabus and transcript" hosted at `https://math.berkeley.edu/~ritvik/…`, a personal
  page. It does name a document, so `PROVENANCE-01` is met in form; I did not fetch it (§7).

### D9 (PROSE/RESOURCE residue) `resources.md`

Adjudicated as **not** defects: the nine vendored Hartshorne solution PDFs (`:94-110`) each have a ledger line in
`sources/attachment-extraction-ledger.jsonl` with a disposition ("inventoried") and an inventory note, which is the
intake model `RES-02` asks for; the resolver links are `RESOURCE-40`'s "author, title, citation, access link" form, not
citations in mathematical prose; and `:192`'s Stacks entry was checked against the live tag page — Section 111.63,
tag 0G12, "Algebraic Geometry, Final Exam, Spring 2020", exercises 111.63.1–111.63.7 — so the earlier reader's
"wrong exercise" finding is answered by the current line.

Surviving, all small: `:58` "(the course page notes that there is no grader)" is curation about a course page, not a
description of the mathematics (`PROSE-11`); `:87` transcribes a term's exercise assignment sequence ("assigned, in
order: I.1.1–1.6; …") which is a reading schedule rather than a resource description (`RESOURCE-11`); `:148`
("lectures [1] … through [18]") and `:194` ("solution sheets `hwk1`–`hwk7`") are URL- and filename-pattern bookkeeping
(`PROSE-11`); `:120` attaches a bibliography-keyed claim to the Hartshorne appendix ("which Hartshorne states as
Theorem 2.1 of Appendix B [@Har77, Appendix B, Theorem 2.1]") while the work itself enters unkeyed — consistent with
CITE-1's split (the mathematical claim *is* keyed; the work is navigation), so this line is **not** a defect.

### D10 (SEC-2) `sheaves/the-sheaf-condition.md:19`

    On a disconnected space the constant presheaf fails gluing, the quotient of the continuous functions by
    the bounded ones has a nonzero class that restricts to zero on every bounded interval, and the tensor
    presheaf has chartwise sections that agree on the overlap and do not glue ([[FE-AM5Z8]]).

Three examples in one unfenced running sentence in a mathematical section, immediately above the transclusion of the
card that states them (`FE-AM5Z8` at `:21`). `SEC-2` asks for a fenced example unit or deletion; the sentence also
compresses three distinct counterexamples into one clause ("the quotient … restricts to zero on every bounded
interval" is not the failure of an axiom by itself). Same class, lower grade:
`sheaves/examples-of-sheaves.md:33-35` ("Each of these is a sheaf for the same reason …") states a remark about four
examples in prose rather than linking `FE-SHFFUNCS`.

### D11 (PR-18 / PROSE-05) `schemes/what-is-a-scheme.md:53`

    ... the standard non-examples are the two one expects: ...

"the two one expects" manufactures a reader expectation and then satisfies it; the two computations themselves
($\Gamma(\PP^1)=k$; $\Gamma(\AA^2\sm\{0\})=k[x,y]$) are the content. Delete the four words.

### D12 (superseded during this reading; one new item) `stacks-and-moduli/functors-and-topologies.md:12`

The PRECISION-1 sentence this reading first flagged ("descent … is the statement that a quasicoherent sheaf on a
scheme is the same data on an fppf cover") is **gone**: #188 rewrote the page at `5e96c6f622`, and the replacement
states the Amitsur exactness, the descent datum $\theta\colon C\otimes_{B,p_1}N\to C\otimes_{B,p_2}N$ with its
cocycle, and the equalizer quasi-inverse $\{n:\theta(n\otimes1)=1\otimes n\}$, citing Stacks 023N and 03OE. Read at
the new state the page is sound: the Yoneda and two-test-scheme paragraphs, the $\PP^n$ functor up to isomorphism of
$\mcl$, the open-subfunctor gluing, the Kummer/Hilbert-90 computations and the torsor statements all check out.

What is left is a citation form: `:12` ends "(Stacks Project, Chapter 7, *Sites and Sheaves*)" — a Stacks chapter with
no tag, where CITE-3 and the house convention cite Stacks by tag. The same page does it correctly at `:53` and `:54`
(tags 021M, 021N). Repair: carry the tag of the specific section or definition the sentence uses — I did not open one, and I do not
invent one here — or drop the parenthetical in favour of the tag'd citations that follow. This is the one place in
the 82 pages where a Stacks reference carries a chapter rather than a tag.

### D13 (DEF-29, two candidates needing a reader decision) `schemes/ringed-spaces.md:16`, `schemes/subschemes-and-points.md:12`

`:16` "A morphism $(f,f^\sharp)$ of ringed spaces is a morphism of locally ringed spaces when for each $p$ … is a
local homomorphism" and `:12` "A subscheme of $X$ is a locally closed subscheme, a closed subscheme of an open
subscheme: …" are both definition-shaped prose with no `\dfn`, no definition block, and no "Recall that …" opening
(the house's sanctioned reminder form, `CONTRIBUTING.md` §Defining occurrences). Both pages link the owning card
(`D-AN662`, `D-SCHSUB`) a few lines away, so the fix is one word each ("Recall that …") or a pointed link; a reader
has to decide which, because `:16` also carries a condition ($f^\sharp_p$ local) that the card states.

Nothing else in the four classes #175 named as "examples" survives: across the 82 pages there is **no** `\dfn`, no
`{.proof}` or `::: pf` block, no "For example"/"For instance", no "is called"/"we say"/"is defined to be", and the
PROSE-01/03/04/07/08 vocabulary ("crucial", "key fact", "worth noting", "This page states", "the whole reason",
"matters", "keep in mind") returns one hit in total, D11 above.

## 5. Claims I checked by computation rather than by citation

Recorded so they can be re-checked: the $(-2)$-curve discrepancy (§2#2); the $\det 7$ cone's resolution
self-intersections $u_0+u_2=3u_1$, $u_1+u_3=2u_2$, $u_2+u_4=2u_3$ giving $(-3,-2,-2)$; the Hirzebruch
self-intersections $D_2^2=-a$, $D_4^2=a$ from $u_1+u_3=a\,u_2$ and $u_3+u_1=-a\,u_4$; $K^2=12-d$ and the del Pezzo
degrees $9,8,8,7,6$; Clifford equality on a hyperelliptic curve, $\ell(m g^1_2)=2m+1-g+(g-m)=m+1=\tfrac12\deg+1$;
the genus-4 canonical complete-intersection degrees $(4),(2,3),(2,2,2)$ from $\sum d_i=g+1$ with $d_i\ge2$;
$\FF_3[x]/(x^2+1)=\FF_9$; the isotrivial family $ty^2=x^3-x$ having every geometric fibre isomorphic to
$y^2=x^3-x$ (scale $x\mapsto\alpha x$, $y\mapsto\beta y$ with $\alpha=\pm1$, $\beta^2=\pm1/a$); the twisted family's
non-constancy; the pullback of $\ZZ\xrightarrow{p}\ZZ$ along $\Spec\FF_p\to\Spec\ZZ$ being zero; the fibre-dimension
counterexample at $\eta\in\AA^1$.

## 6. Per-page ledger

"Read" = read in full at the snapshots of §1. "Checked" names the numbered statements I opened for that page.
Pages carrying a defect above are marked with its label.

**`cohomology/`**
1. `computing-cohomology.md` — read; the $\PP^n$ duality shift and $\omega_{\PP^n}=\OO(-n-1)$ checked by hand; III.4.5/III.5.1 not re-opened (standard, and cited as a section pair).
2. `derived-functors-and-vanishing.md` — read; **D1**; Grothendieck-vanishing sharpness $H^n(\PP^n,\OO(-n-1))\ne0$ correct.
3. `families.md` — read; the flatness example checked by hand ($\chi$ jumps $1\to2$; $f$ is projective since $X\subset\PP^1_{\AA^1}$ closed).
4. `homological-algebra.md` — read; §2#1 decided; III.6.5.2 / Exercise III.6.2 (no enough projectives) not re-opened.
5. `index.md` — read; the $H^1(\OO^\times)=\Pic$ and Serre-criterion summaries match the pages they summarize.
6. `projective-schemes.md` — read; lower semicontinuity/constancy attribution rests on `T-COHBC` (card not read, §7).
7. `vanishing-and-duality.md` — read; III.3.7, III.7 duality, Kodaira vanishing restated correctly; the qcqs/quasicoherent-ideal variant rests on `T-5IOUR` (Stacks, not opened, §7).

**`curves-and-surfaces/`**
8. `blowups-and-the-classification-of-surfaces.md` — read; V.4.9 read verbatim (27 lines, each $-1$, the only curves of negative self-intersection).
9. `crepant-resolutions.md` — read; §2#2 decided; V.5.7, Cor V.5.4 read.
10. `curves-in-projective-space.md` — read; **D6**; Exercise IV.3.4 read; the $(a,b)$-type genus $ab-a-b+1$ checked against adjunction.
11. `elliptic-curves-over-c.md` — read; **Theorem IV.4.15B read** ($J(\tau)=J(\tau')$ iff $\tau'=(a\tau+b)/(c\tau+d)$ with $ad-bc=\pm1$) and **Theorem IV.4.19 read** (CM $\iff\tau$ imaginary quadratic); IV.4.12B and IV.4.16 not opened (§7).
12. `elliptic-curves.md` — read; the $ty^2=x^3-x$ twist checked by hand.
13. `embeddings-and-jacobians.md` — read; $T_0\Jac=H^1(\OO_C)$ and the Abel–Jacobi embedding for $g\ge1$ correct; card-level statements not re-read.
14. `genus.md` — read; Exercise I.7.2 read ($P_C(m)=dm+1-p_a$).
15. `index.md` — read; adjunction summary consistent with `T-SRFADJ`.
16. `intersection-theory-on-surfaces.md` — read; $K_{\tilde X}=\pi^*K_X+E$, $E^2=-1$ correct.
17. `moduli-of-curves.md` — read; the coarse-moduli example is the same twist, correct.
18. `riemann-hurwitz.md` — read; §2#3 decided; IV.2.2, IV.2.3, Cor IV.2.4, **Prop IV.2.5 and Example IV.2.5.1 read**.
19. `riemann-roch-for-curves.md` — read; $\deg K=2g-2$ from $D=K$, Clifford's bound, gonality all correct.
20. `special-divisors-and-the-canonical-map.md` — read (rewritten by #188 mid-pass, re-read); **D2**; IV.1.3, Ex IV.1.3.3, IV.5.1, IV.5.2, IV.5.3, Thm IV.5.4, Cor IV.3.2, Ex IV.5.2.1/2.2 read.

**`divisors/`**
21. `class-group-and-picard-group.md` — read; §2#4 decided; II.6.4, II.6.5, II.6.11, Remark II.6.11.1A, Example II.6.11.3, Prop II.6.15, Cor II.6.16, Cor II.6.17 read.
22. `index.md` — read; consistent with the pages.
23. `line-bundles-and-linear-systems.md` — read; **IV.3.1 read** — this page states the very-ampleness criterion in $\ell$-form correctly, which is the corroboration for D2; II.7.3, II.7.7.
24. `positivity.md` — read; Theorem II.7.6 read; Nakai–Moishezon and Kleiman restated correctly.
25. `weil-and-cartier.md` — read; II.6.4, II.6.5 read; Exercise IV.1.8 (normalisation/Pic sequence) not re-opened (§7).

**`morphisms/`**
26. `classes-of-morphism.md` — read; the implication chain is correct (closed immersion $\Rightarrow$ finite $\Rightarrow$ proper; projective $\Rightarrow$ proper; proper $\Rightarrow$ universally closed); Vakil Exercise 8.3.I not checked (§7).
27. `fibres-and-images.md` — read; the node's normalisation is not flat, correct.
28. `finite-and-flat.md` — read; the page's A–M 5.10/5.11/5.16 and Stacks 00HS citations were **not opened here** (the third #175 verdict read them); Proposition III.9.7 not re-opened.
29. `index.md` — read; the going-down item of #175 is satisfied by `finite-and-flat.md:20-24`.
30. `inseparable-morphisms-and-luroth.md` — read; **Prop IV.2.5 read verbatim**, including "X and Y are isomorphic as abstract schemes" — the page transcribes it, so my own first suspicion (that $C\not\cong C^{(p)}$ refutes it) is wrong: $K\subseteq L$ purely inseparable of curves has $K\cong L$ as abstract fields via $x\mapsto x^{p^n}$. Ex IV.2.5.1, 2.5.4, 2.5.5 read.
31. `projective-morphisms.md` — read; §2#5 decided; II.4.9, II.7.3, II.7.6, V.1.10 read; Vakil 16.2.G and Exercise III.5.7(d) not re-opened.
32. `separated-and-proper.md` — read; II.4.9 and I.3.4 read.
33. `smooth-unramified-etale.md` — read; the page's own sentences are correct; the substance is on `D-MORETALE`, `D-MORSM`, `T-MORGEN` (not re-read).

**`schemes/`**
34. `dimension.md` — read; §2#6 decided against Vakil 12.4.3 read verbatim.
35. `fibre-products-and-base-change.md` — read (rewritten mid-pass, re-read); $\FF_9$ fibre checked; both examples now fenced.
36. `index.md` — read; consistent.
37. `normalization.md` — read (rewritten mid-pass, re-read); II.8.22A (Serre's criterion), II.6.3A, **I.3.9A read**; a sibling has since removed the uncited "need not be finite in general".
38. `proj-and-gluing.md` — read (rewritten, re-read); II.2.5, Exercise II.3.12, Exercise II.2.12 (glueing), II.4.9, Cor II.4.8(c) read.
39. `properties-from-the-ring.md` — read (rewritten, re-read); **D3**; II.3.1, Exercise II.2.9, Exercise II.2.13, Exercise II.5.7(a) read.
40. `ringed-spaces.md` — read (rewritten, re-read); §2#7 decided; **D13a**; the DVR non-example was checked by hand (the empty preimage forces the zero map, so the only non-local datum is the stalk inclusion), and its citation, Hartshorne Example II.2.3.2, was not opened (§7).
41. `subschemes-and-points.md` — read (rewritten, re-read); the closed-vs-locally-closed defect of #175 is repaired; **D13b**.
42. `what-is-a-scheme.md` — read (rewritten by #188 mid-pass, re-read); **Theorem III.3.7 read verbatim** (the page's three-clause form is Hartshorne's own); the page's II.2.3, Exercise II.2.4, Proposition II.2.6 and Example II.3.2 were not opened (§7); **D11**.

**`sheaves-of-modules/`**
43. `differentials.md` — read; II.8.17 and the tame/wild length statement correct.
44. `index.md` — read; consistent.
45. `line-bundles.md` — read; the non-abelian example (cokernel of $\OO\xrightarrow{x}\OO$ is a skyscraper) correct.
46. `operations.md` — read; the $\FF_p$ pullback computation checked by hand; $f_*$ exact for a closed immersion correct.
47. `projective-sheaves.md` — read; Proposition II.5.15 read (the page's statement is that proposition), II.5.11.
48. `quasicoherence.md` — read; correct.
49. `tangent-normal-and-canonical-sheaves.md` — read; §2#9 decided; Prop II.8.20 read.

**`sheaves/`**
50. `examples-of-sheaves.md` — read; flabby/acyclic on an irreducible space, and skyscraper support, both correct; **D10 (second item)**.
51. `index.md` — read; the exponential example is right.
52. `morphisms-of-sheaves.md` — read; the two positional references of #175 are now named and linked; the stalk criterion and $\sheafhom$ statements correct.
53. `pushforward-and-pullback.md` — read; §2#8 decided; the $\prod$ vs $\oplus$ counterexample checked.
54. `stalks-and-exactness.md` — read; correct.
55. `the-sheaf-condition.md` — read; **D10**; the noetherian filtered-colimit statement and the $\oplus\to\prod$ witness correct.

**`stacks-and-moduli/`**
56. `functors-and-topologies.md` — read, then re-read after #188's rewrite at `5e96c6f622`; **D12** (superseded, one citation-form item left); the site/pretopology sheaf condition, the étale-inside-fppf implication and the Kummer exactness are correct; Vakil's Definition 7.3.10 at `:19` was not opened (§7).
57. `index.md` — read; consistent.
58. `spaces-and-stacks.md` — read; the prose redefinitions #175 flagged are now "Recall that …" sentences over card links; the hyperelliptic-automorphism obstruction is right.

**`toric/`**
59. `affine-computations.md` — read; **D4**; CLS Prop 1.1.9 read; $\Cl=\ZZ/|\det|$, smoothness $\iff|\det|=1$, checked.
60. `criteria.md` — read; the Gorenstein/Cartier condition $(\exists m:\inner{m}{u_\rho}=1\ \forall\rho)$ correct.
61. `examples.md` — read; §2#10 decided; the determinantal computations redone by hand.
62. `index.md` — read; consistent with the pages.
63. `polytopes-and-divisors.md` — read; $P_D$/$H^0$ equality, $\Pic\subseteq\Cl$ of finite index on simplicial fans, and the cone-over-a-square example ($\Cl=\ZZ$, $\Pic=0$) correct; the CLS chapter-6 statements rest on `D-TORQD`/`T-TORDIV` (not re-read).
64. `surfaces-and-morphisms.md` — read; blowup invariants ($\rank\Pic+1$, $\chi+1$, $-1$-curve, neighbours $-1$) correct; the $V(xy-zw)$ cone and its two small resolutions rest on `FE-207WC`.
65. `the-dictionary.md` — read; the table's $\Cl=\ZZ/d$ row matches `FE-TORCD`; "every smooth complete surface is projective" correct.
66. `topology.md` — read; §2#11 decided; **§7** for the two Fulton locators.
67. `toric-del-pezzo-surfaces.md` — read; §2#12 decided; $K^2=12-d$ and the five degrees redone.

**`varieties/`**
68. `affine-or-projective.md` — read; projective $\Rightarrow$ complete, complete affine is a point, Serre's criterion all correct.
69. `blowups.md` — read; **Prop V.3.4 read** ($\pi_*\OO_{\tilde X}=\OO_X$, $R^i\pi_*=0$); $K^2$ drop and $p_g,q$ invariance correct.
70. `canonical-class.md` — read; the hypersurface trichotomy $d\lessgtr n+1$ and $\binom{d-1}{2}$ correct.
71. `dimension-and-degree.md` — read; **Theorem I.7.7, Corollary I.7.8 (Bézout), Exercise I.7.1 and Exercise I.7.2 read** — I.7.2 defines $p_a$ and itself points at (III, Ex. 5.3) for embedding-independence, which is the citation at `:49`.
72. `index.md` — read; consistent.
73. `morphisms-of-varieties.md` — read; the anti-equivalence, the Segre and Veronese descriptions correct; the definition is now a "Recall that …" link.
74. `nonsingular-curves.md` — read; **Proposition I.6.8 read**; Proposition II.6.3A read as its statement.
75. `projective-varieties.md` — read; §2#14 decided; **D7**.
76. `rational-maps.md` — read; §2#13, §2#15 decided; **D5**; Vakil 15.3.B not checked (§7).
77. `regular-functions.md` — read; **Theorem I.3.4 read**; Exercise I.3.6 not opened (§7).
78. `smooth-and-singular.md` — read; the Euler relation argument correct.
79. `the-dictionary.md` — read; the $(x)$/$(x^2)$ example is now fenced and correct.

**root**
80. `index.md` — read; the dependency paragraph is correct.
81. `resources.md` — read; **D9**.
82. `syllabus.md` — read; **D8**.

## 7. What stayed undecided, at exact locations

These are the places where I did not reach a decision, stated so that the inventory is not read as a clean sheet.

1. **Statements carried on cards I did not open.** Every wiki sentence that restates a card is only as good as the
   card, and #187 owns the cards. The load-bearing ones whose source statement I did not read:
   `vanishing-and-duality.md:19` (`T-5IOUR`: the qcqs form of Serre's criterion with quasicoherent ideals, and
   "quasicompactness cannot be omitted"); `projective-schemes.md:28` (`T-COHBC`, semicontinuity);
   `tangent-normal-and-canonical-sheaves.md:45` (`D-SCHCMGOR`, dualising sheaf on a CM projective scheme);
   `sheaves-of-modules/operations.md:32-35` and `pushforward-and-pullback.md:50` (`D-SHFSIX`, the six operations,
   $f_!$/$f^!$ and their hypotheses); `toric/surfaces-and-morphisms.md:44-45` (`FE-207WC`, two small resolutions);
   `curves-and-surfaces/blowups-and-the-classification-of-surfaces.md:12` (`T-SRFZMT`, weak factorisation);
   `morphisms/finite-and-flat.md:14` (`III.9.7` cited through a card).
2. **Two Fulton locators, book not on the machine.** `toric/topology.md:29` cites `[@Ful93, §3.2]` for
   $\pi_1=N/N_\Sigma$ and `:55` cites `[@Ful93, §4.2]` for the moment-map fibres; `toric/index.md:16` and
   `syllabus.md:187` cite chapter/section ranges of the same book. There is no text of Fulton's *Introduction to
   Toric Varieties* under `tmp/sources`; the statements are standard and the page's own version is consistent, but I
   did not read the numbered statements and do not certify the locators.
3. **Vakil exercises cited by number.** `morphisms/classes-of-morphism.md:44` (Exercise 8.3.I),
   `morphisms/projective-morphisms.md:47` (Exercise 16.2.G), `varieties/rational-maps.md:21` (Exercise 15.3.B),
   `schemes/what-is-a-scheme.md:72` (Lemma 5.3.2). The Vakil *Rising Sea* text on disk was used only for Theorem
   12.4.3; these four numbers were not opened.
4. **Hartshorne numbers cited for a statement I verified independently but did not match to the number.**
   `cohomology/homological-algebra.md:44` (Caution III.6.5.2, Exercise III.6.2); `divisors/weil-and-cartier.md:34`
   (Exercise IV.1.8); `morphisms/finite-and-flat.md:14` (Proposition III.9.7);
   `cohomology/computing-cohomology.md:13-14` (III.4.5, III.5.1). The mathematics is right; the numbers are unchecked.
5. **`syllabus.md:37`'s Berkeley document** (`https://math.berkeley.edu/~ritvik/…`). Not fetched; `PROVENANCE-01` is
   satisfied in form (a document is named) and the document's existence and contents are unverified.
6. **`toric/polytopes-and-divisors.md:44-52`** (ampleness as strict upper convexity, very ampleness from local
   semigroup generation). Adjudicated as consistent with `PR-TORPOS` and with the del Pezzo page's use of it; the
   chapter-6 statement of CLS is not on disk, so this rests on the card.
7. **Vakil's Definition 7.3.10 and §1.2** at `stacks-and-moduli/functors-and-topologies.md:19` (Yoneda and the
   functor of points). Not opened.
8. **Hartshorne numbers cited on the pages that this pass did not open**, distinct from item 4 (where the mathematics
   was verified another way): `schemes/what-is-a-scheme.md:37,49,53` (Proposition II.2.3, Exercise II.2.4, Proposition
   II.2.6); `schemes/ringed-spaces.md:18` (Example II.2.3.2); `varieties/regular-functions.md:22` (Exercise I.3.6);
   `curves-and-surfaces/elliptic-curves-over-c.md:18,26` (Theorem IV.4.12B, Theorem IV.4.16);
   `cohomology/homological-algebra.md:21` (Proposition-Definition II.1.2); `varieties/projective-varieties.md:43`
   (Exercise I.2.14, the Segre embedding). `morphisms/finite-and-flat.md:20-24` rests on Atiyah–Macdonald Theorems
   5.10, 5.11 and 5.16, which I did not open; the third #175 verdict reports having read them, and that report is a
   claim I did not check.

## 8. What this file does not do

It edits no page and no card. It does not repair D1–D13; each names the owning file so #187 (pages whose sentence is
false, cards) and the orchestrator (bibliography keys for D4 and D8's Reid entry) can act. It runs no gate. It does not
claim the 82 pages are clean: §6 records where this reading found nothing, §7 records where it did not look.
