# #189: `wiki/algebraic-geometry/` — the reading record, second version

**Supersedes** `results/189-ag-inventory.md` as it stood at `078db711f834`. Reviewer gzg9 returned NOT MET on that
version at that commit and named the failures; this version re-decides from the general statement, adds the omitted
defects and the omitted policy findings, adjudicates four cards from their sources, and states its baseline correctly.
Nothing in it was carried over on the earlier version's authority: every line number below was re-derived by reading
the blob at the pinned commit.

## 0. Acceptance clause by clause, as this file stands

| #189 acceptance clause | State here |
|---|---|
| Every page of `wiki/algebraic-geometry/` read against the full parent policy set | All 82 enumerated files read (§8); the tree is listed so the claim is checkable. Pages rewritten by the concurrent #188/#187 lanes after the first pass were re-read at the pinned blob. |
| Every statement flagged in #175 decided from its source | All fifteen flags decided, each from the **general** statement, not a special case (§2). Eight of them needed a new argument; six carry a cross-reference or nearby finding recorded beside them. |
| Every violation has an actionable page/card location | §3 (five new mathematical defects), §4 (cards), §5 (policy: two undefined macros, four positional sentences, and the carried items). |
| The two named card defects recorded, not duplicated | `PR-RJ3P7` and `T-FFDESCENT` recorded as already repaired at `2734e61c70` and `1287f30106`, with what I checked (§4.1). |
| Baseline complaint on `PR-VGA2L` | Recorded and adjudicated as **not** closable: no retained numbered statement of Chevalley–Warning (§4.2). |

This file does not repair anything and runs no gate. It does not claim the corpus is clean: §9 says where it did not
look.

## 1. Baseline, and the correction to the earlier version

- **Pinned blob: `078db711f834`** — the commit the reviewer read. The 82 Markdown files under `wiki/algebraic-geometry/`
  at that commit total **3908 lines** (measured per blob with `git show`, not from the working tree). The earlier
  version printed "3767 lines": that is the same tree at `698a059f47`, the tip when the first pass began, and it was
  wrong to print it beside line numbers pinned later. Both numbers belong to different commits; this version uses
  `078db711f834` throughout.
- The working tree has moved: the current tip at the time of writing is `29a103fab4`, and #188/#187 keep rewriting
  pages. Where a finding's location has changed since the baseline, §3/§5 give **both** the baseline line and the
  current one, and say which. A later commit is never counted as evidence that this reading read it.
- Policies used: `CONTRIBUTING.md` (read in full) and the shared writing policy's `section-structure.md`,
  `citations.md`, `prose.md`, `prose-tells.md`, `definitions.md`, `resource-descriptions.md`.
- Sources opened for this version, each read at the statement: `tmp/sources/hartshorne-1977-algebraic-geometry.md`,
  `tmp/sources/vakil-rising-sea-2025-10-21.md`, `tmp/sources/cox-little-schenck-2011-toric-varieties.md`,
  Stacks tags **021M** and **00VH** (fetched live), `vocabularies/macros.json`, `vocabularies/references.yaml`,
  `sources/attachment-extraction-ledger.jsonl`, and the four cards of §4.

## 2. The fifteen flags, each decided from its general statement

The "page now" column is the text at `078db711f834`. Where I say a claim is true I give the general argument; where it
is false I give the general witness, not an example of a special case.

All fifteen flags from #175's list, with the verdict and where it is argued.

| Flag (as #175 states it) | Verdict | § |
|---|---|---|
| 1. `homological-algebra`: "in both a cokernel is not the naive one" | false for $A$-modules, true for $\OO_X$-modules; page now states both | 2 |
| 2. `crepant-resolutions`: $(-2)$-curve; Gorenstein canonical in dim 3; terminal | false / false / true-but-vacuous, and the triple was inconsistent | 2 |
| 3. `riemann-hurwitz`: $d_p=e_p-1+(	ext{correction divisible by }p)$ | not the book's statement; page now gives IV.2.2 | 2 (over-citation) |
| 4. `class-group-and-picard-group`: isomorphism on an integral scheme | true for Cartier, false for Weil; page now separates them | 2 (Remark II.6.11.2 missing) |
| 5. `projective-morphisms`: ampleness "stable under pullback" | false in general; page now gives the finite/pullback cases and the blowup counterexample | 2 |
| 6. `schemes/dimension`: fibre dimension upper semicontinuous on $Y$ | true only for closed $f$; page now separates three functions | 2 (no finding) |
| 7. `schemes/ringed-spaces`: the product of stalks | injectivity is not gluing; page now says so | 2 (§5.3 nearby) |
| 8. `sheaves/pushforward-and-pullback`: "the only ones available" | false; $j_!$, $Rf_!$, $f^!$ | 2 |
| 9. `tangent-normal-and-canonical-sheaves`: CM/Gorenstein/lci order; `\inverseof{i}` | order regular $\Rightarrow$ lci $\Rightarrow$ Gorenstein $\Rightarrow$ CM; adjunction needs the restriction | 2 |
| 10. `toric/examples`: det-7 cone; "every toric surface from $\PP^2$"; "every toric variety is a fan" | false / true in general / false until normal | 2 |
| 11. `toric/topology`: quadric cone $\pi_1$; torus bundle; faces generate $H^*$ | page's $\pi_1=0$ is right; the other two were false and are repaired | 2 |
| 12. `toric/toric-del-pezzo-surfaces`: "lattice distance two"; "the table above" | both false; reflexive means distance one | 2 |
| 13. `varieties/rational-maps`: "isomorphism in codimension one" | false; undefined only in codim $\ge2$ for normal source | 2; notation at `:21`, citation at §5.4 |
| 14. `varieties/projective-varieties`: the Segre claim | true in general; page now states the general case | 2 |
| 15. `varieties/rational-maps`: the dominance hypothesis on maps to $\PP^n$ | unnecessary; page now attaches dominance only to pullback | 2 |

### Row 1 — the cokernel in `A-Mod` and in `O_X-Mod`
- **Flag:** "in both a cokernel is not the naive one."
- **Decision: false in one of the two categories, true in the other.** General statement: for *any* ring $A$ and *any*
  $A$-linear $f\colon M\to N$, the cokernel in $A\text{-}\mathbf{Mod}$ is the quotient $N/\im f$ — the naive one; the
  quotient of a module by a submodule is already a module, so no completion is needed. For *any* ringed space and any
  $\OO_X$-linear $f\colon\mcf\to\mcg$, the cokernel in $\OO_X\text{-}\Mod$ is the **sheafification** of
  $U\mapsto\coker(f(U))$. General witness that the presheaf is not already a sheaf: on $X=\AA^1$ take
  $f=\cdot x\colon\OO_X\to\OO_X$; then $(U\mapsto\coker)$ has a section over $\AA^1\sm\{0\}$ (the class of $1/x$)
  that restricts to $0$ on every affine open and does not come from a section over $\AA^1$, so the presheaf cokernel
  fails the gluing axiom. Source for the sheaf side: Har77 II.1.2 (the associated sheaf), which the page cites.
- **Page now (`cohomology/homological-algebra.md:21-22`): true.** It states the $\OO_X$ cokernel as the cokernel sheaf
  and the $A$-module cokernel as the quotient $N/\im f$, and cites II.1.2 for the first. **No repair.**

### Row 2 — the three crepant assertions
- **Flag:** "a $(-2)$-curve cannot be contracted"; "crepant resolutions exist for Gorenstein canonical singularities
  (dimension 3)"; "terminal singularities admit none".
- **Decision, general, three separate verdicts:**
  1. **False.** A curve with negative-definite intersection matrix on a smooth surface is contractible (Artin; the
     surface case of Grauert), and a single $(-2)$-curve $E\cong\PP^1$ is that case: adjunction
     $2g-2=E\cdot(E+K_X)$ gives $E\cdot K_X=0$, and the contraction to the du Val $A_1$ point is crepant because
     $E\cdot K_X=0=E\cdot f^*K_{X_0}$ forces the discrepancy $a$ to satisfy $aE^2=0$, so $a=0$ (the general argument the
     page now gives).
  2. **False as stated, and by the wrong hypothesis.** The existence theorem in dimension three is for **terminal**
     Gorenstein threefolds (Mori), not for canonical ones; terminal is strictly stronger than canonical, so a theorem
     about terminal singularities cannot be restated for canonical ones. No retained text of Mori is on this machine;
     the falsity I rely on is the incompatibility of 2 with 3 below, which uses only definitions.
  3. **True, and vacuous.** A *terminal* singularity has every discrepancy $>0$ by definition, and a crepant morphism
     has discrepancy $0$ on every exceptional divisor, so a crepant resolution with an exceptional divisor cannot exist;
     the only crepant "resolution" is the identity. So 3 holds while 2 cannot, and the original triple was
     self-contradictory: it asserted existence for canonical singularities and non-existence for the terminal ones
     inside them.
- **Page now (`curves-and-surfaces/crepant-resolutions.md:18,32-34`): the three sentences are gone; what remains is
  true.** `:18` gives $K_{\tilde X}=\pi^*K_X+(n-1)E$ and "a blowup of a smooth point is never crepant"; `:32-34` give
  Castelnuovo's criterion, contractibility of $(-1)$- and $(-2)$-curves, and the crepancy computation. **No repair on
  this row.** The residual is §9.2: I did not read Mori.

### Row 3 — Riemann–Hurwitz and the tame/wild correction
- **Flag:** "$d_p=e_p-1+(\text{a correction divisible by }p)$".
- **Decision: the printed form is not the book's.** General statement (Har77 Prop IV.2.2, items read): for a finite
  separable morphism of curves, $\length(\Omega_{X/Y})_P=e_P-1$ when $P$ is tame, and $\length\ge e_P$ when $P$ is wild;
  the general formula for the degree of the ramification divisor is therefore
  $\deg R=\sum_P\length(\Omega_{X/Y})_P\ge\sum_P(e_P-1)$, with equality exactly in the tame case. A "correction
  divisible by $p$" is not what the proposition says: the wild case gives at least $e_P$, not $e_P-1$ plus a
  $p$-multiple.
- **Page now (`curves-and-surfaces/riemann-hurwitz.md:12-18`): true and general** — it defines $R$ by the lengths, gives
  $K_X\sim f^*K_Y+R$ (IV.2.3), the degree formula (Cor IV.2.4), and the tame/wild split with "so
  $\deg R=\sum(e_P-1)$ holds exactly when no point is wildly ramified".
- **Cross-reference finding (this row): the last sentence over-cites.** The implication "$\deg R=\sum(e_P-1)$ exactly
  when tame" uses **only** Proposition IV.2.2; Corollary IV.2.4 (Hurwitz) is the degree formula already printed at
  `:15-17` and states nothing about tameness. CITE-4 asks for the citation at the claim it supports; drop IV.2.4 at
  `:18`.
- **Nearby defect: none found** in `:12-18` or `:32` (the genus computations at `:32` check out:
  $2g_X-2=-2n+\deg R$ gives $g_X=0$ for $2n-2$ simple branch points and $g_X=g$ for a degree-two cover of $\PP^1$ with
  $2g+2$ branch points).

### Row 4 — class group and Picard group on an integral scheme
- **Flag:** "on an integral scheme the map between them is an isomorphism" (needs local factoriality).
- **Decision: true for Cartier divisors, false for Weil divisors.** General statement: for *every* integral scheme,
  $\CaCl(X)\to\Pic(X)$, $[D]\mapsto[\OO_X(D)]$, is an isomorphism (Har77 Prop II.6.15, read) — no factoriality.
  $\CaCl(X)\into\Cl(X)$ is injective for normal $X$ (Remark II.6.11.2, read) and an isomorphism when every local ring
  is a UFD (Prop II.6.11, read), in particular for regular $X$ (Remark II.6.11.1A, read); it is **not** an isomorphism
  in general: on the affine quadric cone $\CaCl=0$ while $\Cl=\ZZ/2$ (Example II.6.11.3, read).
- **Page now (`divisors/class-group-and-picard-group.md:12-18`): true, with the hypotheses exactly where they belong.**
- **Cross-reference finding (this row): `:17` cites Proposition II.6.11 and Corollary II.6.16 and Remark II.6.11.1A,
  but its normal-case clause — "a Cartier divisor is a locally principal Weil divisor, so $\CaCl\into\Cl$" — is
  Remark II.6.11.2's statement, and that number is absent.** Add it. Second, `:36` locates the global-sections formula
  only as "[@Har77, §II.6]"; the statements are the ones on $\OO_X(D)$ and effective divisors, and a section locator is
  the weakest the policy allows (CITE-1 wants the statement reached).

### Row 6 — fibre dimension "upper semicontinuous in the point of $Y$"
- **Flag:** fibre dimension "upper semicontinuous as a function of the point of $Y$".
- **Decision: two different functions, and the flag conflated them.** General statement (Vakil Theorem 12.4.3, read
  verbatim): (a) on the **source**, $x\mapsto\dim$ of the largest component of $\pi^{-1}(\pi(x))$ through $x$ is upper
  semicontinuous; (b) on the **target**, $y\mapsto\dim X_y$ is upper semicontinuous *when $\pi$ is closed*, e.g. proper.
  Without closedness it fails in general: the open immersion $\AA^1\sm\{0\}\into\AA^1$ has $\{y:\dim X_y\ge0\}$ open
  and non-closed. The local function $\krulldim\OO_{X_{f(x)},x}$ is a third function and is not upper semicontinuous:
  $\AA^1_k\to\Spec k$ has value $1$ at closed points and $0$ at $\eta$.
- **Page now (`schemes/dimension.md:43-52`): true, all three functions separated, each with its hypothesis.**
- **Cross-reference finding (this row): none.** `:43` and `:51` cite 12.4.3(a) and (b) correctly, `:48` links the card,
  `:53` rests on `T-MORMIRACLE`, which §4.3 now verifies against Vakil 26.2.10/26.2.11. Nearby: `:52`'s witness for
  the necessity of closedness is correct as printed.

### Row 7 — gluing and "the product of the stalks"
- **Flag:** gluing as "the structure sheaf is a subsheaf of the product of its stalks".
- **Decision: the injectivity is true and is not the sheaf axiom.** General statement: for any sheaf $\mcf$ on a space
  and any open $U$, $s\mapsto(s_p)_{p\in U}$ is injective (axiom 3); the gluing axiom is the *existence* of a section
  over $U$ from a compatible family, and the product of stalks carries no compatibility, so a section of the product
  need not be a section of $\mcf$. Witness for the gap in the structure sheaf: on $\Spec k[\varepsilon]/(\varepsilon^2)$
  every element of the product of stalks over the single point is a value $k$-element, while the ring is
  two-dimensional.
- **Page now (`schemes/ringed-spaces.md:26-28`): true** — injectivity, then "injectivity is not the gluing axiom …
  the product of the stalks imposes no compatibility between its coordinates".
- **Cross-reference finding (this row): `:16` locates the definition of a morphism of locally ringed spaces as
  "[@Har77, Section II.2]".** The definition there is not a numbered statement, so the page cannot carry a number; that
  is a source-side gap, not a page defect, and it should be recorded rather than "fixed" by inventing a number.
  **Nearby defect: the sentence is definition-shaped prose** (DEF-29/DEF-1) — a local homomorphism is defined by a card
  (`D-AN662`), and `:16` restates the condition without "Recall that". See §5.3.

### Row 8 — "the two functors are the only ones available"
- **Flag:** the claim that $f_*$ and $f^*$ exhaust the functors.
- **Decision: false in general, and false as an implication, not merely in an example.** General statement: for a
  morphism of ringed spaces the adjunction $f^{-1}\dashv f_*$ gives two functors; $f^*=-\otimes_{f^{-1}\OO_Y}\OO_X$ is a
  third; for sheaves of abelian groups there are $j_!$ (left adjoint to restriction, for an open immersion $j$),
  $Rf_!$ (proper supports, for $f$ a map of locally compact spaces), and $f^!$ (right adjoint of $Rf_!$, Verdier
  duality) — the six operations with $\otimes$ and $\sheafhom$. General reason $f_*$ cannot be replaced by $f^{-1}$: a
  right adjoint preserves limits and not colimits; the witness is unchanged: for $X=\coprod_{i\in I}\{i\}$, $I$
  infinite, $f\colon X\to\{\mathrm{pt}\}$ and $\mcf_i=\ZZ$ on the $i$th point,
  $\left(f_*(\oplus_i\mcf_i)\right)(\mathrm{pt})=\prod_i\ZZ$ while $\left(\oplus_if_*\mcf_i\right)(\mathrm{pt})=\oplus_i\ZZ$.
- **Page now (`sheaves/pushforward-and-pullback.md:13,27-29`): true** — `:13` names $j_!$, $Rf_!$ and $f^!$ with the
  hypotheses under which they exist; `:28` says which limits each side preserves; `:29` gives the counterexample.
- **No repair on this row.**

### Row 9 — the CM / Gorenstein / lci order, and the adjunction restriction
- **Flag:** the order reversed; $\inverseof{i}\Omega_X$ for $i^*\Omega_X$ (also in `riemann-hurwitz.md`).
- **Decision: the order is regular $\Rightarrow$ local complete intersection $\Rightarrow$ Gorenstein $\Rightarrow$
  Cohen–Macaulay, and it is one-directional.** General reason: the ideal sheaf of an lci is generated by a regular
  sequence of the right length, so the Koszul complex is a finite free resolution and the dualizing sheaf is invertible
  (Gorenstein); Cohen–Macaulayness is what makes "dualizing sheaf invertible" the right criterion at all. The converse
  direction fails in general, which is why the order is not a convention. Separately, adjunction for
  $i\colon Y\into X$ is a statement about sheaves **on $Y$**: $\omega_Y\cong\restrictionof{\omega_X}{Y}\otimes\wedge^r\mcn_{Y/X}$,
  and for $r=1$ $\omega_Y\cong\restrictionof{(\omega_X\otimes\mcl)}{Y}$ (Har77 Prop II.8.20 read: "$\omega_Y\cong
  \omega_X\otimes\mathcal L\otimes\OO_Y$"); writing $i^*$ or the restriction is required, and `\inverseof{i}` is not
  the pullback.
- **Page now (`sheaves-of-modules/tangent-normal-and-canonical-sheaves.md:45-46,52-60`): true.** lci $\Rightarrow$
  Gorenstein $\Rightarrow$ invertible dualizing sheaf, and every adjunction written with `\restrictionof{·}{Y}`. No
  `\inverseof` remains in it or in `riemann-hurwitz.md` (search at the pinned blob). **No repair.**
- Residual: I did not read a source for "lci $\Rightarrow$ Gorenstein" outside the corpus card `D-SCHCMGOR` (§9.3).

### Row 10 — the three toric claims on `toric/examples.md`
- **Flag:** a determinant-7 cone called the quadric cone; "every toric surface from $\PP^2$ by blowing up fixed
  points"; "every toric variety is a fan".
- **Decision, three general verdicts:**
  1. The quadric cone is $V(xy-z^2)$, the toric variety of $\Cone((0,1),(2,-1))$, with $\Cl=\ZZ/2\ZZ$ and a ruling that
     is a Weil divisor not locally principal (Har77 Example II.6.11.3 read). A cone of determinant $7$ is a different
     surface, with $\Cl=\ZZ/7$.
  2. **True in general:** every smooth complete toric surface is $\PP^2$, a Hirzebruch surface $\FF_a$ ($a\ge0$), or a
     blowup of one of these at torus-fixed points; equivalently a fan with at least four rays and no "unnecessary"
     subdivision. This is the general classification, not an example, and the page states it in that form.
  3. **False as a category claim, true after normality.** A variety is not a fan; the correct general statements are
     that a fan determines a **normal** toric variety $X_\Sigma$, that $\Sigma\mapsto X_\Sigma$ is injective on fans, and
     that a normal toric variety is $X_\Sigma$ for a fan determined by its orbit stratification. The cuspidal cubic is not
     normal, hence not of the form $X_\Sigma$ — the page's own remark.
- **Page now (`toric/examples.md:36,40,45,61`): true.** Determinant seven computed at `:40`; the classification at
  `:61`; `:45` says the cuspidal cubic is not of the form $X_\Sigma$. **No repair.**

### Row 11 — the three toric-topology claims
- **Flag:** the affine quadric cone not simply connected; "torus bundle over a polytope"; "$H^*$ has the faces of the
  fan as generators".
- **Decision, three general verdicts:**
  1. **The page's trivial-$\pi_1$ claim is true and the reader's $\ZZ/2$ is false.** General statement:
     $\pi_1(X_\Sigma(\CC))\cong N/N_\Sigma$ where $N_\Sigma$ is generated by **all lattice points in $|\Sigma|$**, not by
     the ray generators. For a complete fan $N_\Sigma=N$, so every complete toric variety over $\CC$ is simply
     connected — including the affine quadric cone, whose fan is not complete but whose cone contains the lattice points
     $(1,0)=u_1/2+\ldots$: the cone $\Cone((0,1),(2,-1))$ contains $(1,0)$, so $N_\Sigma=N$ and $\pi_1=0$. This is the
     owner's ruling at #175 and it is correct.
  2. **False: the moment map is not a torus bundle over $P$.** General statement: over the relative interior of a
     $k$-dimensional face $F$, $\mu^{-1}$ is the orbit of $F$, of complex dimension $k$, and the fibre of $\mu$ there is
     the compact torus $(S^1)^k$ of real dimension $k$ — not the algebraic orbit, which is a torus bundle over that
     compact torus.
  3. **False as stated; the correct general statement is Stanley–Reisner.** $H^*(X_\Sigma)$ for a smooth complete fan is
     the quotient of the polynomial ring on the rays by the Stanley–Reisner ideal of monomials spanning no cone, modulo
     the linear relations — not generated by faces.
- **Page now (`toric/topology.md:31,55,47`): all three are right at the pinned blob.** `:31` gives the trivial
  $\pi_1$ with the lattice-point reason; `:55` gives the $(S^1)^k$ fibre and denies the bundle claim; `:47` gives the
  Stanley–Reisner presentation. **No repair.**
- Residual: the page's locators `[@Ful93, §3.2]`, `[@Ful93, §4.2]` are not checkable here (§9.1).

### Row 12 — the toric del Pezzo page
- **Flag:** "lattice distance two"; a reference to "the table above" the page lacks.
- **Decision: both were wrong, and the general statement is distance one.** General statement: for a smooth complete
  toric surface, $-K$ is Cartier and ample exactly when
  $P_{-K}=\{m\in M_\RR:\langle m,u_\rho\rangle\ge-1\text{ for every ray }\rho\}$ is a reflexive lattice polytope with
  normal fan $\Sigma$ — its facets are at lattice distance **one** from the origin (that is what "reflexive" means for a
  polytope containing $0$ in its interior), and a facet at distance two would not contain a lattice point in its
  relative interior. The page's displayed inequalities $\langle m,u_\rho\rangle\ge-1$ are therefore right and the
  "distance $0$/$2$" sentence was inconsistent with them. "The table above" referred to nothing on the page.
- **Page now (`toric/toric-del-pezzo-surfaces.md:55-59,66`): true.** $P_{-K}$ as displayed; $K^2=12-d$ with the five
  degrees $9,8,8,7,6$ (checked: $3,4,4,5,6$ rays); the fourth-blowup obstruction $-K\cdot C=2+C^2=0$ on a $(-2)$-curve.
  **No repair.**

### Row 13 — rational maps: codimension one and the dominance hypothesis
- **Flag:** "a birational map is an isomorphism in codimension one"; the dominance hypothesis on maps to $\PP^n$.
- **Decision: the first is false and the second is unnecessary.** General statement: a birational map from a
  **normal** variety to a projective variety is undefined only in codimension $\ge2$ (Har77 V.5.1, read: "if $T\colon
  X\to Y$ is a birational transformation of projective varieties, and if $X$ is normal, then the fundamental points of
  $T$ form a closed subset of codimension $\ge2$") — an isomorphism in codimension one is a strictly stronger and
  generally false claim (a single blowup is birational, normal source and target, and changes a divisor). For maps to
  $\PP^n$: general statement, an $(n+1)$-tuple of rational functions not all zero, modulo $k(X)^\times$, is a rational
  map with no dominance condition (Har77 Theorem II.7.1, read: the morphism is built from $\mathcal L$ and sections, and
  no dominance appears); dominance is needed only to pull back functions along a map to a general $Y$.
- **Page now (`varieties/rational-maps.md:21,22,26`): true on both counts.**
- **Cross-reference finding (this row): `:21` writes "at a point of codimension one the local ring $\OO_{X,\eta}$ is a
  discrete valuation ring" — $\eta$ is the generic point by this corpus's convention, and the local ring meant is
  $\OO_{X,x}$ at the codimension-one point.** Notation defect (SYM-1/NOT-3) at the same sentence. Nearby: `:48`'s
  citation is the D-item of §3.6 (II.8.19 and Ex II.8.8 do not state the extension).

### Row 14 — the Segre claim
- **Flag:** the Segre/product claim on `varieties/projective-varieties.md`.
- **Decision: the general statements are true, and the page now states them generally.** $m=n=1$ is only the printed
  instance, not the argument. General statement: $\sigma\colon\PP^m\times\PP^n\to\PP^{(m+1)(n+1)-1}$,
  $(x,y)\mapsto(x_iy_j)$, is a closed immersion onto the locus of rank-one matrices, cut out by all $2\times2$ minors;
  for closed $X\subseteq\PP^m$, $Y\subseteq\PP^n$ the product $X\times Y$ is closed in $\PP^m\times\PP^n$, so
  $\sigma(X\times Y)$ is closed in $\sigma(\PP^m\times\PP^n)$, hence in $\PP^N$ — projectivity of the product follows
  for every $m,n$. (`m=n=1`: the single minor $z_{00}z_{11}-z_{01}z_{10}$ is the smooth quadric in $\PP^3$.)
- **Page now (`varieties/projective-varieties.md:41-44`): the general statement, with `m=n=1` as the illustration.**
  **No repair.**
- Residual: Har77 Exercise I.2.14 (Segre) was not opened (§9.3); the general mechanism is decided, the citation is not.

### Row 15 — dominance, carried from row 13
- **Decision: as row 13.** `varieties/rational-maps.md:22` attaches dominance only to pullback of functions on a general
  target, and `:26` has none for $\PP^n$. **No repair.** Nearby: `:28`'s "the morphisms are the base-point-free linear
  systems" is the correct general statement for a base-point-free linear system on a variety (the pullback of
  $\OO(1)$ and the assigned sections).

## 3. New mathematical defects, with location, source and witness

These are the five the reviewer identified and this reading now confirms at the pinned blob.

### 3.1 Projection formula stated with no hypothesis — `sheaves/pushforward-and-pullback.md:42`
    The projection formula is the compatibility of the two functors with tensor: $f_*(\mcf\tensor f^*\mcg)\cong f_*\mcf\tensor\mcg$.

Hartshorne's statement carries a hypothesis: **II.5.1(d)**, read — "if $\mathcal F$ is an $\OO_X$-module, **and if
$\mathcal E$ is a locally free $\OO_Y$-module of finite rank**, then there is a natural isomorphism
$f_*(\mathcal F\otimes f^*\mathcal E)\cong f_*(\mathcal F)\otimes\mathcal E$", and III. Ex 8.3 repeats it in the same
form. Without finite local freeness the displayed isomorphism is not a theorem: the two sides are not even both defined
as the same kind of object of a finite-rank construction, and the natural map $f_*\mcf\otimes\mcg\to f_*(\mcf\otimes
f^*\mcg)$ is not invertible in general. Repair: carry "for $\mcg$ locally free of finite rank" (and cite II.5.1(d)),
which is what the corpus's own `PR-SCHPROJFORM` card is for.

### 3.2 Generating sections do not make the map an embedding — `sheaves-of-modules/line-bundles.md:21`
    For $X$ proper over a field, a line bundle $\mcl$ generated by sections $s_0,\ldots,s_n$ defines a morphism
    $X\to\PP^n$, and this morphism is a closed embedding exactly when $\mcl$ is very ample.

**False, and not the criterion's statement.** Hartshorne **II.7.3** (read in full) is about the **chosen span**:
"Let $V\subseteq\Gamma(X,\mathcal L)$ be the subspace spanned by the $s_i$. Then $\varphi$ is a closed immersion if and
only if (1) elements of $V$ separate points … and (2) elements of $V$ separate tangent vectors". Very ampleness of
$\mcl$ says that *some* choice of sections of some power separates; it does not certify the given $s_0,\ldots,s_n$.
Counterexample: $X=\PP^1$, $\mcl=\OO(2)$ (very ample), $s_0=x^2$, $s_1=y^2$. These generate $\OO(2)$ — they have no
common zero on $\PP^1$ — and the resulting map is $[x:y]\mapsto[x^2:y^2]$, of degree $2$, hence not injective and not a
closed immersion. Repair: replace "exactly when $\mcl$ is very ample" by II.7.3's criterion on $V$. Note that
`morphisms/projective-morphisms.md:45` already states it correctly with $V$, so the two pages contradict each other at
the pinned blob.

### 3.3 Very ampleness of a toric divisor: the semigroup must be shifted — `toric/polytopes-and-divisors.md:52`
    $D$ is very ample exactly when it is ample and the lattice points of $P_D$ generate the local semigroup
    $S_\sigma$ at every vertex

The lattice points of $P_D$ lie in $P_D$; what generates the local semigroup at a vertex is their translate by the
vertex. Cox–Little–Schenck **Definition 2.2.17** (read): "a lattice polytope $P\subseteq M_\RR$ is very ample if for
every vertex $m\in P$, the semigroup $\mathsf S_{P,m}=\mathbb N(P\cap M-m)$ generated by the set
$P\cap M-m=\{m'-m\mid m'\in P\cap M\}$ is saturated in $M$." Repair: "the lattice points $m-m_\sigma$, for
$m\in P_D\cap M$, generate $S_\sigma$ at every maximal cone $\sigma$, with $m_\sigma$ the Cartier datum" — and the
saturation clause, since CLS Proposition 2.2.18 (read) is the statement that a *normal* polytope is very ample, i.e.
saturation is part of the criterion.

### 3.4 The sheaf condition stated without the gluing axiom — `sheaves/the-sheaf-condition.md:12`
    A presheaf is a contravariant functor … and a sheaf is a presheaf whose sections are determined by their
    restrictions to the members of any open cover.

That is the identity (locality) axiom only. The general definition has two parts: two sections agreeing on a cover are
equal, **and** a compatible family of sections over a cover glues to a section. The page's own `:18-19` says "neither
axiom follows from the other" — so the opening sentence defines a sheaf by one of the two axioms it then separates.
Witness that the second is not automatic: the constant presheaf on a two-point discrete space has no section
restricting to a prescribed pair of different values, though the family is compatible (its overlaps are empty).
Repair: state both axioms at first use, leaving the card `D-RCCFY` as the defining occurrence and the page's sentence as
the "Recall that …" reminder.

### 3.5 The Gauss map's degree — `curves-and-surfaces/curves-in-projective-space.md:86`
    For a smooth curve of degree $d\ge2$ the Gauss map $C\to C^\vee$ has degree $d(d-1)$, so a smooth conic is
    self-dual …

$d(d-1)$ is the degree of the **dual curve**, not of the Gauss map. For a smooth plane curve $C$ of degree $d$ the class
of $C$ — the degree of $C^\vee$ — is $d(d-1)$ (the page itself says so two lines later, in Plücker's formula
$\deg C^\vee=d(d-1)-2\delta-3\kappa$ with $\delta=\kappa=0$), while the Gauss map is **birational** onto $C^\vee$, of
degree $1$; the corpus's own card `D-CRVDUAL:41` says "the Gauss map $C\to C^\vee$ is birational", so the page
contradicts its own card. The attached conclusions survive when read correctly ("a smooth conic is self-dual" because
$2\cdot1=2$ and the map is an isomorphism; "a smooth cubic has dual of degree $6$"). Repair: "the dual curve $C^\vee$ has
degree $d(d-1)$, and the Gauss map is birational onto it".
**Location note:** this sentence is on the current tree (`29a103fab4`), added by #188 after the pinned blob; at
`078db711f834` the page is 43 lines and the "Dual curves" section contains only the transclusion. It is a live defect,
not one the review could have read at the pinned commit, and it is recorded here as such.

## 4. The cards

### 4.1 The two named in #189
- `corpus/theory/Algebraic_Geometry/PR-RJ3P7.md` — repaired at `2734e61c70`, before both versions of this record.
  Read at `078db711f834`: `:47` "surjectivity is not part of that: it is lying over, and it needs $\phi$ injective …
  $\ZZ\to\ZZ/2$"; `:49` "a finite morphism need not preserve the dimension of its target"; `:51` "going down is what
  makes heights match, $\operatorname{ht}\mfq=\operatorname{ht}(\mfq\cap A)$, under its hypotheses". Correct, and the
  height statement follows from going up + going down + incomparability. **MET; nothing for #187.**
- `corpus/theory/Algebraic_Geometry/T-FFDESCENT.md` — repaired at `1287f30106`. Read: the datum
  $\theta\colon C\otimes_{B,p_1}N\to C\otimes_{B,p_2}N$ with cocycle, and the quasi-inverse
  $\{n\in N:\theta(n\otimes1)=1\otimes n\}$ under $C\otimes_{B,p_1}N\cong N\otimes_AB$ and
  $C\otimes_{B,p_2}N\cong B\otimes_AN$ — the standard Amitsur equalizer, citing Stacks 023N and 03OE. **MET; the only
  residual is that the $\otimes_{B,p_i}$ convention is implicit.**

### 4.2 Baseline complaint: `PR-VGA2L` and Chevalley–Warning — **still open, not closable here**
`corpus/theory/Algebraic_Geometry/PR-VGA2L.md:64` (read): "If $k=\FF_q$, the anticanonical conic is defined by one
homogeneous quadratic equation in three variables. **Chevalley–Warning** gives a nonzero solution over $\FF_q$, hence a
$k$-rational point on $C$." The theorem is used, not stated: no numbered statement, no hypothesis transcribed, and no
retained text of Chevalley–Warning exists on this machine (`tmp/sources` has none; `vocabularies/references.yaml` has no
key). The card is transcluded by `curves-and-surfaces/genus.md:24` and by
`curves-and-surfaces/riemann-roch-for-curves.md` in the edition of that page that carries `PR-VGA2L` (both were
checked), so the gap is visible on two pages.
Under CITE-8 this is a defect and under QUAL-01 it is not repairable here: the honest record is **waiting on a
numbered statement of Chevalley–Warning** (its statement and proof are in every text on finite fields, but none is
retained and I do not invent a number). The complaint entry is the sibling commit `b27109aeb5`.

### 4.3 The four cards the review asked to adjudicate
- **`D-CRVHYP`** (hyperelliptic; read at `078db711f834`). Definition cites **Har77 Exercise IV.1.7**, read: "A curve $X$
  is called hyperelliptic if $g\ge2$ and there exists a finite morphism $f\colon X\to\PP^1$ of degree 2" — matches, and
  "equivalently a $g^1_2$" is the standard equivalence for $g\ge2$. The proposition cites **Prop IV.5.3**, read
  (unique $g^1_2$; the canonical morphism is $f_0$ followed by the $(g-1)$-uple embedding). The remark's
  base-point-freeness argument uses $\ell(p)=1$ and Riemann–Roch, which reproduces the proof of **Lemma IV.5.1**, read.
  **MET.** One thing the card leaves implicit: $|K|=(g-1)g^1_2$ is the last clause of Prop IV.5.3, so the citation
  covers it.
- **`T-MORMIRACLE`** (miracle flatness; read). Cites **Vakil 26.2.10** and **26.2.11**, both read verbatim:
  26.2.10 — "Suppose $\Phi\colon(B,\mathfrak n)\to(A,\mathfrak m)$ is a (local) homomorphism of Noetherian local rings,
  such that $A$ is Cohen–Macaulay, and $B$ is regular, and $A\otimes_B(B/\mathfrak n)$ has pure dimension $\dim A-\dim B$.
  Then $\phi$ is flat"; 26.2.11 — "Suppose $\pi\colon X\to Y$ is a morphism of pure dimensional finite type $k$-schemes,
  where $X$ is Cohen–Macaulay, $Y$ is regular, and the fibers of $\pi$ have dimension $\dim X-\dim Y$. Then $\pi$ is
  flat." The card's theorem has the letters of the map in the opposite order from Vakil's — it writes
  $(A,\mathfrak m)\to(B,\mathfrak n)$ and hypothesises "$A$ regular, $B$ Cohen–Macaulay" — which is the same statement,
  and the card's corollary and its "in particular" sentence match 26.2.11. **MET, with the convention to state: the
  card's source is Vakil, whose letters are reversed; a reader checking 26.2.10 against the card as printed will think
  the hypotheses are swapped unless the card says so.**
- **`D-ETFPPF`** (read). Cites **Stacks 021M** and **021N**. 021M was fetched and read: "Definition 34.7.1. Let $T$ be
  a scheme. An *fppf covering of $T$* is a family of morphisms $\{f_i\colon T_i\to T\}_{i\in I}$ of schemes such that each
  $f_i$ is flat, locally of finite presentation and such that $T=\bigcup f_i(T_i)$" — exactly the card's fppf clause.
  021N was not opened; it is the "next lemma" of 021M's page (same section 34.7), and the card's use of it (étale
  coverings are fppf) is the standard Lemma 34.7.2. **MET for 021M; the 021N number is consistent with the site's own
  navigation and unread.**
- **`D-GROTHTOP`** (read). Its definition of a site ends "(Stacks Project, Chapter 7, *Sites and Sheaves*)" — a chapter,
  not a tag, which the house convention for Stacks does not allow. I fetched the chapter: Chapter 7 is tag **00UZ**
  ("Sites and Sheaves") and the site definition is **Definition 7.6.2, tag 00VH** (read: "a site is given by a category
  $\mathcal C$ and a set $\mathrm{Cov}(\mathcal C)$ of families of morphisms with fixed target $\{U_i\to U\}_{i\in I}$,
  called coverings … satisfying the following axioms"). Two points for the repair: the number exists and is 00VH; and
  00VH presents a site by **covering families**, while the card defines a Grothendieck topology by **covering sieves**, so
  citing 00VH needs either the sieve formulation's own tag (not located here) or a sentence that the two presentations
  agree. **NOT MET on citation form.** The wiki sentence at `stacks-and-moduli/functors-and-topologies.md:12` copies the
  card's phrase, so it is repaired with the card.

## 5. Policy findings

### 5.1 Two undefined control words (no gate catches either)
Screening every `\word` token in the 82 blobs against the 346 macros of `vocabularies/macros.json` plus the standard
LaTeX/AMS command set returns exactly two tokens that are neither:
- **`\sp`** — `schemes/properties-from-the-ring.md:18`: "$\sp(\Spec A)$ is a noetherian topological space when $A$ is
  noetherian". Hartshorne writes `sp(X)` in Exercise II.2.13 (read) for the underlying space; the corpus macro for it is
  `\underlyingspace{…}`. Repair: `\underlyingspace{\Spec A}`.
- **`\tensorn`** — `stacks-and-moduli/functors-and-topologies.md:65`: "the equalizer $n\mapsto\{n\in N:\theta(n\tensor1)=
  1\tensorn\}$". A missing space in `1\tensor n`; `\tensorn` is undefined and renders as an error. Repair: `1\tensor n`.
Both are visible to a reader and invisible to `qualc check`.

### 5.2 Surviving positional prose (PROSE-03, and SEC-10 for the heading)
- `schemes/what-is-a-scheme.md:80` — "For noetherian $X$ **the criterion above** has a cohomological form". "Above" is
  document layout; the criterion is Serre's, and the sentence should name it and link the card (`T-5IOUR`).
- `curves-and-surfaces/special-divisors-and-the-canonical-map.md:22` — "Two consequences organise everything **below**."
  A sentence about the page; delete it or state the two consequences as one sentence each.
- `morphisms/projective-morphisms.md:50` — the heading "**## Consequences used later**". A title that names position
  rather than mathematics (SEC-10): name the results (coherence of higher direct images, formal functions, the Hilbert
  polynomial).
- `stacks-and-moduli/functors-and-topologies.md:20` — "it is used in both directions **below**". Name the two uses.
The earlier version reported no positional prose surviving; that was wrong for these four locations, which I had
screened but not read.

### 5.3 Definition-shaped prose with no "Recall"
- `schemes/ringed-spaces.md:16` — "A morphism $(f,f^\sharp)$ of ringed spaces is a morphism of locally ringed spaces
  when … is a local homomorphism". The defining occurrence is `D-AN662`; the house form for a reminder is "Recall that
  …" with a link (DEF-1, DEF-17, DEF-29).
- `schemes/subschemes-and-points.md:12` — "A subscheme of $X$ is a locally closed subscheme, a closed subscheme of an
  open subscheme …". Same form; `D-SCHSUB` owns it.

### 5.4 Carried from the first version, still present at the baseline
- **CITE-1 unkeyed inline reference** — `toric/affine-computations.md:14` `[Cox--Little--Schenck, *Toric Varieties*,
  Proposition 1.1.9]`. The number is right (CLS Prop 1.1.9 read); the form is the one #175 rejected. Needs a Zotero key.
- **CITE-8** — `varieties/rational-maps.md:48` cites Theorem II.8.19 (read: birational invariance of $p_g$) and
  Exercise II.8.8 (read: plurigenera and Hodge numbers) for the codimension-two extension of differential forms. The
  number for that step is **II.6.3A**, read, used inside 8.19's proof on an affine trivialising chart.
- **CITE-8** — `curves-and-surfaces/curves-in-projective-space.md:19`: "Every irreducible curve of degree $d$ spanning
  $\PP^d$ is rational normal" with no argument, link or number (true: Castelnuovo's bound with $r=d$ gives $g\le0$).
- **CITE-8** — `varieties/projective-varieties.md:18`: the empty-set criterion is Exercise **I.2.2** (read); Exercise
  I.2.4 (read) is the bijection clause.
- **PROVENANCE-01** — `syllabus.md:10` claims every section names its document; `:149, :163, :183, :197` name none
  (each opens "The numbered items group the topics by subject." at `:151, :165, :185, :199`). `:167` gives eight
  section locators of Reid, *Chapters on Algebraic Surfaces*, unkeyed.
- **PROSE-11 / RESOURCE-11** — `resources.md:58` ("the course page notes that there is no grader"), `:87` (a term's
  assignment sequence), `:148` ("lectures [1] through [18]"), `:194` ("homework and solution sheets `hwk1`–`hwk7`").
  Adjudicated as **not** defects: the nine vendored solution PDFs at `:94-110`, each with a ledger disposition
  ("inventoried") in `sources/attachment-extraction-ledger.jsonl`; and `:192`, checked against the live tag page
  (Section 111.63, tag 0G12, exercises 111.63.1–111.63.7).
- **SEC-2** — `sheaves/the-sheaf-condition.md:19` carries three counterexamples in one unfenced sentence above the card
  that states them; `sheaves/examples-of-sheaves.md:33` states a remark about four examples in prose (`FE-SHFFUNCS`).
- **PR-18 / PROSE-05** — `schemes/what-is-a-scheme.md:53`: "the standard non-examples are the two one expects".

## 6. Carried mathematical defects, re-verified at the baseline

Both were reported in the first version and are present at `078db711f834` at the same lines.
- **`cohomology/derived-functors-and-vanishing.md:46`** — "so affine vanishing fails for a **quasicoherent** sheaf that
  is not coherent". The example is Har77 **Exercise III.2.1(a)** (read): $X=\AA^1_k$ over an infinite field,
  $U=X-\{P,Q\}$, "show that $H^1(X,\ZZ_U)\ne0$". The sheaf is the extension by zero of the constant sheaf, which is not
  quasicoherent; the block's own title is "Quasicoherence cannot be dropped", and
  `sheaves/pushforward-and-pullback.md:49` says of the same construction "it is not quasicoherent". Repair: "so vanishing
  for quasicoherent sheaves does not extend to arbitrary sheaves of abelian groups".
- **`curves-and-surfaces/special-divisors-and-the-canonical-map.md:49`** — "one needs $\ell(K-p-q)=g-3$ … and
  Riemann--Roch converts this into $\ell(p+q)=1$". Hartshorne's criterion (**Prop IV.3.1(b)**, read) is
  $\dim|K-P-Q|=\dim|K|-2=g-3$, i.e. $\ell(K-p-q)=g-2$; with $g-3$ Riemann–Roch would give $\ell(p+q)=0$. The page's own
  conclusion fixes the intended value. `divisors/line-bundles-and-linear-systems.md:30` states the same criterion
  correctly in $\ell$-form, so this is a one-page slip.

## 7. What the earlier version got wrong, recorded so the next reader does not repeat it

1. It printed 3767 lines beside line numbers pinned to a later blob; the pinned tree is **3908**. (§1)
2. Rows 1, 2, 8, 9, 10, 11, 12 and 14 were decided by an instance or not at all. Rows 2 and 14 decided a special case
   (a surface contraction; $m=n=1$). (§2)
3. It reported "no positional prose surviving" and "one undefined control word"; there are four positional sentences
   and two undefined macros. (§5.1, §5.2)
4. It omitted five mathematical defects that are at the baseline: §3.1–§3.4, and §3.5 on the current tree.
5. It left the four cards' status implicit instead of reading them. (§4.3)
6. It did not record the `PR-VGA2L`/Chevalley–Warning gap at all. (§4.2)

## 8. The 82 enumerated files (the coverage claim, made checkable)

The list is `git ls-tree -r --name-only 078db711f834 -- wiki/algebraic-geometry` filtered to `.md`; the per-page
verdict is in §8b. Total 3908 lines.

```
wiki/algebraic-geometry/cohomology/computing-cohomology.md
wiki/algebraic-geometry/cohomology/derived-functors-and-vanishing.md
wiki/algebraic-geometry/cohomology/families.md
wiki/algebraic-geometry/cohomology/homological-algebra.md
wiki/algebraic-geometry/cohomology/index.md
wiki/algebraic-geometry/cohomology/projective-schemes.md
wiki/algebraic-geometry/cohomology/vanishing-and-duality.md
wiki/algebraic-geometry/curves-and-surfaces/blowups-and-the-classification-of-surfaces.md
wiki/algebraic-geometry/curves-and-surfaces/crepant-resolutions.md
wiki/algebraic-geometry/curves-and-surfaces/curves-in-projective-space.md
wiki/algebraic-geometry/curves-and-surfaces/elliptic-curves-over-c.md
wiki/algebraic-geometry/curves-and-surfaces/elliptic-curves.md
wiki/algebraic-geometry/curves-and-surfaces/embeddings-and-jacobians.md
wiki/algebraic-geometry/curves-and-surfaces/genus.md
wiki/algebraic-geometry/curves-and-surfaces/index.md
wiki/algebraic-geometry/curves-and-surfaces/intersection-theory-on-surfaces.md
wiki/algebraic-geometry/curves-and-surfaces/moduli-of-curves.md
wiki/algebraic-geometry/curves-and-surfaces/riemann-hurwitz.md
wiki/algebraic-geometry/curves-and-surfaces/riemann-roch-for-curves.md
wiki/algebraic-geometry/curves-and-surfaces/special-divisors-and-the-canonical-map.md
wiki/algebraic-geometry/divisors/class-group-and-picard-group.md
wiki/algebraic-geometry/divisors/index.md
wiki/algebraic-geometry/divisors/line-bundles-and-linear-systems.md
wiki/algebraic-geometry/divisors/positivity.md
wiki/algebraic-geometry/divisors/weil-and-cartier.md
wiki/algebraic-geometry/index.md
wiki/algebraic-geometry/morphisms/classes-of-morphism.md
wiki/algebraic-geometry/morphisms/fibres-and-images.md
wiki/algebraic-geometry/morphisms/finite-and-flat.md
wiki/algebraic-geometry/morphisms/index.md
wiki/algebraic-geometry/morphisms/inseparable-morphisms-and-luroth.md
wiki/algebraic-geometry/morphisms/projective-morphisms.md
wiki/algebraic-geometry/morphisms/separated-and-proper.md
wiki/algebraic-geometry/morphisms/smooth-unramified-etale.md
wiki/algebraic-geometry/resources.md
wiki/algebraic-geometry/schemes/dimension.md
wiki/algebraic-geometry/schemes/fibre-products-and-base-change.md
wiki/algebraic-geometry/schemes/index.md
wiki/algebraic-geometry/schemes/normalization.md
wiki/algebraic-geometry/schemes/proj-and-gluing.md
wiki/algebraic-geometry/schemes/properties-from-the-ring.md
wiki/algebraic-geometry/schemes/ringed-spaces.md
wiki/algebraic-geometry/schemes/subschemes-and-points.md
wiki/algebraic-geometry/schemes/what-is-a-scheme.md
wiki/algebraic-geometry/sheaves-of-modules/differentials.md
wiki/algebraic-geometry/sheaves-of-modules/index.md
wiki/algebraic-geometry/sheaves-of-modules/line-bundles.md
wiki/algebraic-geometry/sheaves-of-modules/operations.md
wiki/algebraic-geometry/sheaves-of-modules/projective-sheaves.md
wiki/algebraic-geometry/sheaves-of-modules/quasicoherence.md
wiki/algebraic-geometry/sheaves-of-modules/tangent-normal-and-canonical-sheaves.md
wiki/algebraic-geometry/sheaves/examples-of-sheaves.md
wiki/algebraic-geometry/sheaves/index.md
wiki/algebraic-geometry/sheaves/morphisms-of-sheaves.md
wiki/algebraic-geometry/sheaves/pushforward-and-pullback.md
wiki/algebraic-geometry/sheaves/stalks-and-exactness.md
wiki/algebraic-geometry/sheaves/the-sheaf-condition.md
wiki/algebraic-geometry/stacks-and-moduli/functors-and-topologies.md
wiki/algebraic-geometry/stacks-and-moduli/index.md
wiki/algebraic-geometry/stacks-and-moduli/spaces-and-stacks.md
wiki/algebraic-geometry/syllabus.md
wiki/algebraic-geometry/toric/affine-computations.md
wiki/algebraic-geometry/toric/criteria.md
wiki/algebraic-geometry/toric/examples.md
wiki/algebraic-geometry/toric/index.md
wiki/algebraic-geometry/toric/polytopes-and-divisors.md
wiki/algebraic-geometry/toric/surfaces-and-morphisms.md
wiki/algebraic-geometry/toric/the-dictionary.md
wiki/algebraic-geometry/toric/topology.md
wiki/algebraic-geometry/toric/toric-del-pezzo-surfaces.md
wiki/algebraic-geometry/varieties/affine-or-projective.md
wiki/algebraic-geometry/varieties/blowups.md
wiki/algebraic-geometry/varieties/canonical-class.md
wiki/algebraic-geometry/varieties/dimension-and-degree.md
wiki/algebraic-geometry/varieties/index.md
wiki/algebraic-geometry/varieties/morphisms-of-varieties.md
wiki/algebraic-geometry/varieties/nonsingular-curves.md
wiki/algebraic-geometry/varieties/projective-varieties.md
wiki/algebraic-geometry/varieties/rational-maps.md
wiki/algebraic-geometry/varieties/regular-functions.md
wiki/algebraic-geometry/varieties/smooth-and-singular.md
wiki/algebraic-geometry/varieties/the-dictionary.md
```

## 8b. Per-page ledger

Compact form: after a path, `read` means read in full at the pinned blob; a bracketed item is what was checked, and a
§ reference is a defect above. A page not named as defective is a page on which this reading found nothing at the
baseline — not a page certified clean.

- `cohomology/`: `computing-cohomology.md` read [duality shift and $\omega_{\PP^n}=\OO(-n-1)$ by hand];
  `derived-functors-and-vanishing.md` read [§6, and the vanishing bound sharpness];
  `families.md` read [flatness example by hand: $\chi$ $1\to2$, $X\subset\PP^1_{\AA^1}$ closed so $f$ projective];
  `homological-algebra.md` read [§2 row 1; III.6.x not opened]; `index.md` read; `projective-schemes.md` read
  [`T-COHBC` not opened, §9.3]; `vanishing-and-duality.md` read [III.3.7; `T-5IOUR`'s quasicoherent-ideal variant not
  opened].
- `curves-and-surfaces/`: `blowups-and-the-classification-of-surfaces.md` read [**Thm V.4.9 read**];
  `crepant-resolutions.md` read [§2 row 2; V.5.7, Cor V.5.4 read]; `curves-in-projective-space.md` read
  [§3.5 on the current tree, Ex IV.3.4 read, the $(a,b)$-genus by adjunction];
  `elliptic-curves-over-c.md` read [Thm IV.4.15B, Thm IV.4.19 read; IV.4.12B, IV.4.16 not opened];
  `elliptic-curves.md` read [the $ty^2=x^3-x$ twist by hand]; `embeddings-and-jacobians.md` read [$T_0\Jac=H^1(\OO_C)$;
  cards not re-read]; `genus.md` read [Ex I.7.2 read; `PR-VGA2L` transcluded, §4.2]; `index.md` read;
  `intersection-theory-on-surfaces.md` read; `moduli-of-curves.md` read; `riemann-hurwitz.md` read [§2 row 3; IV.2.2,
  IV.2.3, Cor IV.2.4, **Prop IV.2.5**, Ex IV.2.5.1–2.5.5 read]; `riemann-roch-for-curves.md` read [`PR-VGA2L`
  transcluded, §4.2]; `special-divisors-and-the-canonical-map.md` read [§6; IV.1.3, Ex IV.1.3.3, IV.5.1, IV.5.2,
  IV.5.3, Thm IV.5.4, Cor IV.3.2, Ex IV.5.2.1/2.2 read].
- `divisors/`: `class-group-and-picard-group.md` read [§2 row 4; II.6.4, II.6.5, II.6.11, Remarks II.6.11.1A and
  II.6.11.2, Ex II.6.11.3, Prop II.6.15, Cor II.6.16, Cor II.6.17 read]; `index.md` read;
  `line-bundles-and-linear-systems.md` read [**IV.3.1 read**]; `positivity.md` read [II.7.6 read];
  `weil-and-cartier.md` read [Ex IV.1.8 not opened].
- `morphisms/`: `classes-of-morphism.md` read [Vakil Ex 8.3.I not opened]; `fibres-and-images.md` read;
  `finite-and-flat.md` read [A–M 5.10/5.11/5.16 **not** opened]; `index.md` read;
  `inseparable-morphisms-and-luroth.md` read [Prop IV.2.5 read verbatim — its "isomorphic as abstract schemes" is
  Hartshorne's, not the page's overstatement]; `projective-morphisms.md` read [§2 row 5, §5.2; II.4.9, II.7.3, II.7.6,
  V.1.10 read]; `separated-and-proper.md` read [I.3.4 read]; `smooth-unramified-etale.md` read [substance on cards].
- `schemes/`: `dimension.md` read [§2 row 6; Vakil 12.4.3 read verbatim]; `fibre-products-and-base-change.md` read
  [$\FF_9$ fibre by hand]; `index.md` read; `normalization.md` read [II.8.22A, II.6.3A, **I.3.9A** read];
  `proj-and-gluing.md` read [II.2.5, Ex II.3.12, Ex II.2.12, II.4.9, Cor II.4.8 read];
  `properties-from-the-ring.md` read [§5.1; II.3.1, Ex II.2.9, Ex II.2.13, Ex II.5.7 read];
  `ringed-spaces.md` read [§2 row 7, §5.3; Ex II.2.3.2 not opened]; `subschemes-and-points.md` read [§5.3];
  `what-is-a-scheme.md` read [§5.2, §5.4; **Thm III.3.7 read**; II.2.3, Ex II.2.4, Prop II.2.6, Ex II.3.2 not opened].
- `sheaves-of-modules/`: `differentials.md` read [II.8.17 read]; `index.md` read;
  `line-bundles.md` read [§3.2; II.7.3 read]; `operations.md` read [the $\FF_p$ pullback by hand];
  `projective-sheaves.md` read [II.5.11, II.5.15 read]; `quasicoherence.md` read;
  `tangent-normal-and-canonical-sheaves.md` read [§2 row 9; Prop II.8.20 read].
- `sheaves/`: `examples-of-sheaves.md` read [§5.4]; `index.md` read; `morphisms-of-sheaves.md` read;
  `pushforward-and-pullback.md` read [§2 row 8, §3.1]; `stalks-and-exactness.md` read;
  `the-sheaf-condition.md` read [§3.4, §5.4].
- `stacks-and-moduli/`: `functors-and-topologies.md` read [§4.3 `D-ETFPPF`, §5.1, §5.2; Stacks 021M read];
  `index.md` read; `spaces-and-stacks.md` read.
- `toric/`: `affine-computations.md` read [§5.4; CLS Prop 1.1.9 read]; `criteria.md` read; `examples.md` read
  [§2 row 10; determinant and continued-fraction computations by hand]; `index.md` read;
  `polytopes-and-divisors.md` read [§3.3; CLS Def 2.2.17, Prop 2.2.18 read]; `surfaces-and-morphisms.md` read
  [`FE-207WC` not opened]; `the-dictionary.md` read; `topology.md` read [§2 row 11; Ful93 locators not checkable];
  `toric-del-pezzo-surfaces.md` read [§2 row 12; $K^2=12-d$ recomputed].
- `varieties/`: `affine-or-projective.md` read; `blowups.md` read [**Prop V.3.4 read**]; `canonical-class.md` read
  [II.8.20-based trichotomy by hand]; `dimension-and-degree.md` read [I.7.7, Cor I.7.8, Ex I.7.1, Ex I.7.2 read];
  `index.md` read; `morphisms-of-varieties.md` read; `nonsingular-curves.md` read [**Prop I.6.8**, II.6.3A read];
  `projective-varieties.md` read [§2 row 14, §5.4]; `rational-maps.md` read [§2 rows 13 and 15, §5.4; V.5.1 read];
  `regular-functions.md` read [**Thm I.3.4** read; Ex I.3.6 not opened]; `smooth-and-singular.md` read [Euler relation];
  `the-dictionary.md` read.
- root: `index.md` read; `resources.md` read [§5.4; tag 0G12 fetched]; `syllabus.md` read [§5.4].

## 9. Unresolved, exactly

1. **Fulton's *Introduction to Toric Varieties*** — `toric/topology.md:29` (`[@Ful93, §3.2]`), `:55` (`§4.2`),
   `toric/index.md:16` and `syllabus.md:187` (ranges). No text on the machine; the statements are decided from CLS's
   chapters where CLS states the same theorem, and the locators are not verified.
2. **Mori's existence theorem for crepant resolutions of terminal Gorenstein threefolds** (§2 row 2) — no retained text.
   The verdict on the page does not depend on it; the verdict on claim 2 does, through the definitional incompatibility
   with claim 3.
3. **Statements carried on cards not opened here** — `T-5IOUR` (qcqs form of Serre's criterion),
   `T-COHBC` (semicontinuity), `D-SCHCMGOR` (lci $\Rightarrow$ Gorenstein, dualising sheaves), `D-SHFSIX` (six
   operations), `FE-207WC`, `T-SRFZMT`, `T-SRFCAST`, `T-BIRINV`, `D-8XX95`, `FE-SRFFERMATQUARTIC`,
   `D-TORQD`/`T-TORDIV`, `PR-TORPOS`, `D-CRVBRILLNOETHER`.
4. **Numbers cited but not opened**: Har77 II.1.2, II.2.3, Ex II.2.4, Prop II.2.6, Ex II.2.3.2, Ex I.2.14, Ex I.3.6,
   IV.4.12B, IV.4.16, Ex IV.1.8, Prop III.9.7, Caution III.6.5.2, Ex III.6.2, III.4.5, III.5.1, Ex III.5.3;
   Atiyah–Macdonald 5.10/5.11/5.16; Vakil Ex 8.3.I, 15.3.B, 16.2.G, Def 7.3.10, Lemma 5.3.2; Stacks 021N.
5. **`syllabus.md:37`'s Berkeley document** (`https://math.berkeley.edu/~ritvik/…`) — not fetched; a document is named,
   so `PROVENANCE-01` is met in form and its existence is unverified.
6. **The reviewer's own cross-reference list for rows 3, 4, 6, 7, 13, 15** — I was not given that text. What §2 records
   for those rows is what I could substantiate at the same locations; where I write "none found" it means my reading of
   that page's links and neighbours found nothing, not that the reviewer's finding is answered.

## 10. What this file does not do

It edits no page and no card; every repair above names the owning file for #187 (a false sentence, a missing
hypothesis, a citation) or for the orchestrator (bibliography keys for CLS and Reid, and the Chevalley–Warning
statement). It runs no gate. It does not claim #189's first acceptance clause is met: §8 lists the 82 files read and
§9 lists what this reading did not decide.

## 11. Repair state at the current tip (`29a103fab4`), so #187 knows what is left

Each row was re-checked against the tip blob for the exact string; "repaired after the baseline" names the commit and
is not counted as anything this reading established.

| Item | At `078db711f834` | At `29a103fab4` |
|---|---|---|
| §3.1 projection formula, `sheaves/pushforward-and-pullback.md:42` | present | **open**, same line |
| §3.2 generating sections ≠ embedding, `sheaves-of-modules/line-bundles.md:21` | present | **open**, same line |
| §3.3 very ampleness needs $m_\sigma$, `toric/polytopes-and-divisors.md:52` | present | **open**, same line |
| §3.4 gluing axiom missing, `sheaves/the-sheaf-condition.md:12` | present | **open**, same line |
| §3.5 Gauss map degree, `curves-and-surfaces/curves-in-projective-space.md` | not yet written | **open**, at `:86` |
| §5.1 `\sp`, `schemes/properties-from-the-ring.md:18` | present | **open**, same line |
| §5.1 `\tensorn`, `stacks-and-moduli/functors-and-topologies.md:65` | present | repaired at `c910f0e80f` |
| §5.2 positional, `schemes/what-is-a-scheme.md:80` | present | **open** |
| §5.2 positional, `curves-and-surfaces/special-divisors…:22` | present | **open** |
| §5.2 positional heading, `morphisms/projective-morphisms.md:50` | present | **open** |
| §5.2 positional, `stacks-and-moduli/functors-and-topologies.md:20` | present | **open** |
| §5.3 `schemes/ringed-spaces.md:16` | present | **open** |
| §5.3 `schemes/subschemes-and-points.md:12` | present | repaired (page rewritten) |
| §5.4 `toric/affine-computations.md:14` unkeyed CLS | present | **open** (needs a key) |
| §5.4 `varieties/rational-maps.md:48` citation | present | **open** |
| §5.4 `varieties/rational-maps.md:21` `\OO_{X,\eta}` | present | **open** |
| §5.4 `varieties/projective-varieties.md:18` I.2.2/I.2.4 | present | **open** |
| §5.4 `curves-in-projective-space.md:19` unsupported assertion | present | repaired (sentence gone) |
| §5.4 `syllabus.md` four sourceless sections, `:167` Reid | present | **open** |
| §5.4 `resources.md:58,87,148,194` | present | **open** |
| §5.4 `sheaves/the-sheaf-condition.md:19`, `examples-of-sheaves.md:33` SEC-2 | present | **open** |
| §5.4 `what-is-a-scheme.md:53` "the two one expects" | present | **open** |
| §6 `derived-functors-and-vanishing.md:46` quasicoherence | present | repaired at `34d031aac8` (the same reading: the exercise is the sharpness of the dimension bound) |
| §6 `special-divisors-and-the-canonical-map.md:49` $g-3$ | present | **open**, same line |
| §4.2 `PR-VGA2L.md:64` Chevalley–Warning | present | **open**, same line |
