# #189: `wiki/algebraic-geometry/` — the reading record, third version

**Status: bounded adjudication, not a claim that #189's first acceptance clause is met.** Reviewer gzg9 returned NOT MET
at `078db711f834`; reviewer Kimi max returned NOT MET on the second version and named seven failures. This version makes
the repairs those two lists require — four of them are corrections to mathematics *I* wrote — and states in §9 what is
still undecided. Two cards are repaired in the commits beside this file, not only relabelled.

## 0. What changed in this version, item by item against the Kimi list

| Item the review required | Where it is done |
|---|---|
| 1. `T-FFDESCENT:71` identifications reversed; commit `1287f30106` moved the wrong way | §4.1 and the card commit `96ef469b62`: `p_1(b)=b⊗1` gives `C⊗_{B,p_1}N ≅ B⊗_AN`, `p_2(b)=1⊗b` gives `C⊗_{B,p_2}N ≅ N⊗_AB`, and the recovered module is `{n : θ(1⊗n)=n⊗1}` |
| 2. Four false general witnesses | §2 rows 1, 2, 7, 12 — each replaced, with the reason the earlier one failed |
| 3. Row 5 adjudicated; every dependency the second version listed as unread decided | §2 row 5; §5 lists each source now read (twenty-two numbered statements, the four cards, both Stacks tags) and the one that is not on the machine |
| 4. Rows 6 and 15 recovered as independent findings | §2 rows 6 and 15, each with its own mathematical content |
| 5. `curves-in-projective-space.md:87` dual class | §3.5 |
| 6. Toric semigroup terminology | §3.3 |
| 7. `PR-RJ3P7:51` qualification | §4.2 and the card commit `13f9c3a8eb` |

## 1. Baseline

- **Pinned blob: `078db711f834`**, the commit the first reviewer read. The 82 Markdown files under
  `wiki/algebraic-geometry/` there total **3908 lines** (measured per blob). The second version's 3908 figure was right;
  the *first* version's 3767 belonged to `698a059f47` and was misprinted.
- The tree has moved twice since (`29a103fab4`, then `067cd0a3f3`), and #188 keeps rewriting pages. Every finding below
  gives the baseline line **and**, where the text has moved or been repaired, the current state, naming the commit.
  **No later commit counts as evidence that this reading read it.**
- Policies: `CONTRIBUTING.md` (read in full) and the shared writing policy's `section-structure.md`, `citations.md`,
  `prose.md`, `prose-tells.md`, `definitions.md`, `resource-descriptions.md`.

## 2. The fifteen flags

Row numbering is #175's bullet order. Rows 1, 2, 8, 9, 10, 11, 12, 14 are the ones the first reviewer found decided by
example or not at all; rows 3, 4, 6, 7, 13, 15 carry a cross-reference or nearby finding; row 5 is decided here for the
first time.

| # | Flag | Verdict | § |
|---|---|---|---|
| 1 | cokernel "not the naive one" in both categories | false for $A$-modules, true for $\OO_X$-modules | 2.1 |
| 2 | $(-2)$-curve; Gorenstein canonical dim 3; terminal | false / false / true-but-vacuous, and the triple was inconsistent | 2.2 |
| 3 | Riemann–Hurwitz $d_p$ | page now gives IV.2.2; over-cites IV.2.4 | 2.3 |
| 4 | class group on an integral scheme | true for Cartier, false for Weil; Remark II.6.11.2 missing | 2.4 |
| 5 | ampleness "stable under pullback" | false in general; each surviving clause true, with its hypothesis named | 2.5 |
| 6 | fibre dimension upper semicontinuous on $Y$ | true only for closed $f$; row carries a finding | 2.6 |
| 7 | the product of stalks | injectivity is not gluing | 2.7 |
| 8 | "the only ones available" | false: $j_!$, $Rf_!$, $f^!$ | 2.8 |
| 9 | CM/Gorenstein/lci order; `\inverseof{i}` | order regular ⇒ lci ⇒ Gorenstein ⇒ CM; adjunction restricts | 2.9 |
| 10 | det-7 cone; "every toric surface from $\PP^2$"; "every toric variety is a fan" | false / true in general / false until normal | 2.10 |
| 11 | cone $\pi_1$; torus bundle; faces generate $H^*$ | page's $\pi_1=0$ right; two repaired | 2.11 |
| 12 | "lattice distance two"; "the table above" | both false; facets at distance one *by definition* | 2.12 |
| 13 | "isomorphism in codimension one" | false; codim $\ge2$ for normal source; notation slip at `:21` | 2.13 |
| 14 | the Segre claim | true in general, and the page states the general case | 2.14 |
| 15 | dominance hypothesis on maps to $\PP^n$ | unnecessary; row carries its own finding | 2.15 |

### 2.1 Row 1 — the two cokernels
**Decision.** For any ring and any $f\colon M\to N$, the cokernel in $A\text{-}\mathbf{Mod}$ is $N/\im f$: a quotient of a
module by a submodule is a module. For any ringed space, the cokernel in $\OO_X\text{-}\Mod$ is the sheafification of
$U\mapsto\coker(f(U))$ (Har77 **II.1.2**, now read: "Given a presheaf $\mathcal F$, there is a sheaf $\mathcal F^+$ and a
morphism $\theta\colon\mathcal F\to\mathcal F^+$, with the property that for any sheaf $\mathcal G$ …"; this is what the
page cites).
**Witness, corrected.** My second version used multiplication by $x$ on $\AA^1\sm\{0\}$ and claimed a cokernel class there;
that is wrong, because $x$ is a *unit* on $\AA^1\sm\{0\}$, so the map is an automorphism and the cokernel vanishes. The
correct witness is the same map on $\AA^1$: for $P(U)=\OO(U)/x\,\OO(U)$, one has $P(\AA^1)=k[x]/(x)=k$ while
$P(D(x))=P(D(x-1))=0$, and $D(x)\cup D(x-1)=\AA^1$; the map $P(\AA^1)\to P(D(x))\times P(D(x-1))=0$ therefore has the
nonzero class of $1$ in its kernel, so $P$ is not a sheaf. (Its sheafification is the structure sheaf of the origin.)
**Page now (`cohomology/homological-algebra.md:21-22`): true.** No repair.

### 2.2 Row 2 — the three crepant assertions
**Decision, three verdicts, and a withdrawal.**
1. "A $(-2)$-curve cannot be contracted": **false.** The case the page needs is a single smooth rational curve $E$ with
   $E^2=-2$ on a smooth surface — the $A_1$ du Val configuration — and its contraction exists; the page's own crepancy
   computation ($E\cdot K_X=0$ by adjunction, $E\cdot f^*K_{X_0}=f_*E\cdot K_{X_0}=0$, hence the discrepancy coefficient
   satisfies $aE^2=0$, so $a=0$) is the proof, and it is a proof about this curve, not about a class of curves.
2. "Crepant resolutions exist for Gorenstein **canonical** singularities in dimension three": **false as stated.** The
   existence theorem in dimension three is for **terminal** Gorenstein threefolds; terminal is strictly stronger than
   canonical, so it cannot be restated with the weaker hypothesis.
3. "Terminal singularities admit none": **true, vacuously.** Terminal means every discrepancy is $>0$; a crepant morphism
   has discrepancy $0$ on each exceptional divisor; so a crepant resolution has no exceptional divisor and is an
   isomorphism. With 2 and 3 together the original triple asserted existence for a class containing the ones it denied,
   which is the inconsistency the repair had to remove by deleting 2.
**Withdrawal.** My second version wrote "a curve with negative-definite intersection matrix on a smooth surface is
contractible (Artin; Grauert)" as support for 1. That general statement is not what the page needs and is not safe as
stated: negative definiteness is Grauert's criterion in the analytic category, and a negative-definite curve of positive
genus need not be algebraically contractible. Nothing in the verdict above rests on it.
**Page now (`curves-and-surfaces/crepant-resolutions.md:18,32-34`): the three sentences are gone and what remains is true.**

### 2.3 Row 3 — Riemann–Hurwitz
As before, and confirmed: Har77 **Prop IV.2.2** (items (a)–(c) read) gives $\length=e_P-1$ tame and $\length\ge e_P$ wild;
there is no "$e_P-1$ plus a $p$-multiple" in the source. The page prints this correctly at
`curves-and-surfaces/riemann-hurwitz.md:18`.
**Cross-reference finding (kept):** `:18` cites "Proposition IV.2.2 **and Corollary IV.2.4**"; Cor IV.2.4 (read) is the
Hurwitz degree formula already printed at `:15-17` and says nothing about tameness, so the second number is an
over-citation (CITE-4).

### 2.4 Row 4 — class group and Picard group
**Decision.** $\CaCl(X)\to\Pic(X)$ is an isomorphism for every integral scheme (Har77 **Prop II.6.15**, read);
$\CaCl(X)\into\Cl(X)$ is injective for normal $X$ (**Remark II.6.11.2**, read: the Cartier divisors are the locally
principal Weil divisors) and an isomorphism when every local ring is a UFD (**Prop II.6.11**, read), in particular for
regular $X$ (**Remark II.6.11.1A**, read); not an isomorphism in general: the affine quadric cone has $\CaCl=0$ and
$\Cl=\ZZ/2$ (**Example II.6.11.3**, read).
**Cross-reference findings (kept, two):** `divisors/class-group-and-picard-group.md:17` omits **Remark II.6.11.2**, which
is the number behind its normal-case clause; and a *new* one on the page that transcludes the same material —
`divisors/weil-and-cartier.md:34` cites **Exercise IV.1.8** for the exact sequence
$0\to\oplus_p\tilde\OO_p^\times/\OO_{X,p}^\times\to\Pic(X)\to\Pic(\tilde X)\to0$. Exercise IV.1.8, now read, is
"$p_a$ of a Singular Curve": its exact sequence is $0\to\OO_X\to f_*\OO_{\tilde X}\to\sum_P\tilde\OO_P/\OO_P\to0$ and its
content is $p_a(X)=p_a(\tilde X)+\sum\delta_P$. It does **not** state the Picard sequence; that citation is wrong
(CITE-8) and I did not locate the right number in the retained text, so it is recorded as owed, not replaced.

### 2.5 Row 5 — ampleness and pullback (decided here)
The page (`morphisms/projective-morphisms.md:46-48`) makes four assertions. Each is true, with the hypothesis its source
carries, and none is the flagged "stable under pullback":
1. **Very ample ⇒ ample; ample ⟺ some power very ample** for $X$ of finite type over a noetherian ring. Har77 **Theorem
   II.7.6** read: "Let $X$ be a scheme of finite type over a noetherian ring $A$, and let $\mathcal L$ be an invertible
   sheaf on $X$. Then $\mathcal L$ is ample if and only if $\mathcal L^m$ is very ample over $\Spec A$ for some $m>0$."
2. **Restriction to a closed subscheme.** Har77 **Ex III.5.7(a)** read: "If $\mathcal L$ is ample on $X$, and $Y$ is any
   closed subscheme of $X$, then $i^*\mathcal L$ is ample on $Y$." The exercise's standing hypothesis, printed at its
   head, is that $X$ and $Y$ are proper over a noetherian ring $A$ — the page omits it.
3. **Pullback along a finite morphism.** Vakil **Ex 16.2.G** read: "Suppose $\pi\colon X\to Y$ is a finite morphism of
   proper $A$-schemes, and $\mathcal L$ is an ample line bundle on $Y$. Show that $\pi^*\mathcal L$ is ample on $X$."
   (Vakil's own remark extends it past "proper $A$-schemes"; the page states the unrestricted version, which is fine but
   is not what the citation says.) The **iff** in the page's next clause is Har77 **Ex III.5.7(d)** read: "Let
   $f\colon X\to Y$ be a finite surjective morphism, and let $\mathcal L$ be an invertible sheaf on $Y$. Then $\mathcal L$
   is ample on $Y$ if and only if $f^*\mathcal L$ is ample on $X$."
4. **Not preserved by arbitrary pullback.** For $\pi\colon\tilde X\to X$ the blowup at a point of a surface,
   $\pi^*\mathcal L\cdot E=\mathcal L\cdot\pi_*E=0$, and an ample divisor meets every irreducible curve positively —
   Har77 **Theorem V.1.10** (Nakai–Moishezon, read): "$D$ on the surface $X$ is ample if and only if $D^2>0$ and
   $D\cdot C>0$ for all irreducible curves $C$."
**Verdict: the flag is answered — ampleness is not stable under arbitrary pullback, and the three cases in which it is
preserved are each a theorem with its own hypothesis.** The only page-side defect is the dropped standing hypothesis in
clause 2 (CITE-6: the hypothesis belongs in the sentence, not in the exercise).

### 2.6 Row 6 — fibre dimension, and the finding on this page
**Decision.** Vakil **Theorem 12.4.3** read verbatim: (a) the dimension of the largest component of $\pi^{-1}(\pi(x))$
through $x$ is upper semicontinuous **on $X$**; (b) the dimension of the fibre over $y$ is upper semicontinuous **on $Y$**
when $\pi$ is closed, e.g. proper. The third function $\krulldim\OO_{X_{f(x)},x}$ is not upper semicontinuous
($\AA^1_k\to\Spec k$: $1$ at closed points, $0$ at $\eta$). The page separates all three (`schemes/dimension.md:43-52`).
**Independent finding on this page (not "none"):** `:53` says "for $X$ Cohen–Macaulay and $Y$ regular the pointwise
equality … forces $f$ to be flat ([[T-MORMIRACLE]])", and the card's own numbered source for that is Vakil **26.2.11**,
which is the **pure-fibre** statement ("the fibers of $\pi$ have dimension $\dim X-\dim Y$"); the pointwise form is the
card's corollary from **26.2.10** (the local theorem), applied at each $x$. A reader who follows the page's pointer to
26.2.11 gets a hypothesis that the page's sentence does not carry (purity of every fibre, not a pointwise equality). The
repair is to cite the local statement (26.2.10) for the pointwise form, as the card does. Both numbers read; see §5.
Second, smaller: `:48` attaches `[[T-MORFIBDIM]]` to the elementary computation $\{x:\dim_x\ge1\}=$ closed points, which is
not that card's statement — the link is to the wrong owner for the example, though harmless.

### 2.7 Row 7 — the product of the stalks
**Decision.** $s\mapsto(s_p)$ is injective (axiom 3) and is not the gluing axiom; the product carries no compatibility.
**Witness, corrected.** My second version used $\Spec k[\varepsilon]/(\varepsilon^2)$ and said the product of stalks over
its one point is $k$: that is wrong, because localising a local ring at its maximal ideal leaves it unchanged, so the
product of stalks over the single point is the whole ring and injectivity is an isomorphism there — no witness at all.
The correct witness is $\AA^1$: the family $g_p=1/x$ for $p\ne0$ and $g_0=0$ is a point of $\prod_p\OO_{\AA^1,p}$ (each
entry is a germ of a regular function near its point) but is not the family of germs of any section of $\OO_{\AA^1}$,
since a section regular at $0$ cannot equal $1/x$ on $\AA^1\sm\{0\}$.
**Page now (`schemes/ringed-spaces.md:26-28`): true.** The finding on this row is §5.3's definition-shaped prose at `:16`.

### 2.8 Row 8 — the functors on sheaves
**Decision.** For a morphism of ringed spaces, $f^{-1}\dashv f_*$ and $f^*=\OO_X\otimes_{f^{-1}\OO_Y}f^{-1}(-)$ are three
functors, and for sheaves of abelian groups there are $j_!$ (left adjoint to $j^{-1}$, for an open immersion), $Rf_!$
(proper supports) with right adjoint $f^!$, plus $\otimes^L$ and $R\sheafhom$ — the six operations. All of this is the
content of the card `D-SHFSIX`, now read, which states $j_!$, the three adjunctions, base change and $f^!$ with the
hypothesis that $f_!$ has finite cohomological dimension. The general reason $f_*$ cannot be replaced: a right adjoint
preserves limits and not colimits, with the coproduct witness $\left(f_*(\oplus_i\mcf_i)\right)(\mathrm{pt})=\prod_i\ZZ$
against $\oplus_i\ZZ$ for $X=\coprod_{i\in I}\{i\}$, $I$ infinite.
**Page now (`sheaves/pushforward-and-pullback.md:13,27-29`): true.** No repair.

### 2.9 Row 9 — the order and the adjunction
**Decision.** regular ⇒ local complete intersection ⇒ Gorenstein ⇒ Cohen–Macaulay, one-directionally: an lci ideal is
generated by a regular sequence of the right length, so the Koszul complex is a finite free resolution and the dualizing
sheaf is invertible, which is Gorenstein; CM is what makes "dualizing sheaf invertible" the right criterion. The card
`D-SCHCMGOR`, now read, defines all three (CM by $\operatorname{depth}R=\dim R$, Gorenstein by finite injective
dimension, complete intersection by the completed presentation $S/(f_1,\dots,f_c)$) and defines lci for a closed
subscheme of a smooth variety as "ideal locally generated by a regular sequence; at a point of codimension $c$ the
sequence has length $c$" — which is exactly what `tangent-normal-and-canonical-sheaves.md:46` uses for a divisor.
Adjunction is about sheaves on $Y$: Har77 **Prop II.8.20** read: "$\omega_Y\cong\omega_X\otimes\wedge^r\mathcal N_{Y/X}$.
In case $r=1$ … $\omega_Y\cong\omega_X\otimes\mathcal L\otimes\OO_Y$."
**Page now (`:45-46,52-60`): true**, every adjunction written with `\restrictionof{·}{Y}`; no `\inverseof` remains in it
or in `riemann-hurwitz.md`. No repair.

### 2.10 Row 10 — the three toric claims
As before, with the sources read this time: the quadric cone is $\Spec k[x,y,z]/(xy-z^2)$ with $\Cl=\ZZ/2$ and a ruling
that is Weil but not Cartier (Har77 **Example II.6.11.3**, read; the card `FE-TORCD`, read, carries the same cone as
$\Cone(e_2,\,de_1-e_2)$, $d\ge2$, with $\Cl=\ZZ/d$); the classification of smooth complete toric surfaces is
`T-TORSURF`, read (rays $v_i$ in cyclic order with each $\{v_i,v_{i+1}\}$ a basis and $v_{i-1}+v_{i+1}=a_iv_i$), and the
page's "$\PP^2$, $\FF_a$, or a blowup" is its consequence; "every toric variety is a fan" is a category error, and the
true statements are that a fan gives a normal toric variety and that $\Sigma\mapsto X_\Sigma$ loses nothing for normal
toric varieties — the cuspidal cubic, being non-normal, is not $X_\Sigma$ (`D-FULSAT`, read: saturation and
$\Spec k[S]$ normal, with the $(4,0),(3,1),(1,3),(0,4)$ example).
**Page now (`toric/examples.md:36,40,45,61`): true.** No repair.

### 2.11 Row 11 — the three toric-topology claims
1. $\pi_1(X_\Sigma(\CC))\cong N/N_\Sigma$ with $N_\Sigma$ generated by **all** lattice points of $|\Sigma|$; for the
   affine quadric cone the cone contains $(1,0)$ (it is $\Cone((0,1),(2,-1))$, whose lattice points include
   $\tfrac12(0,1)+\tfrac12(2,-1)=(1,0)$), so $N_\Sigma=N$ and $\pi_1=0$. The page's claim is right and the reader's
   $\ZZ/2$ is wrong. The route to the formula is the card `PR-TORMOR` (read: compatibility, completeness iff
   $|\Sigma|=N_\RR$) together with `D-FULSTAR` (read: $N_\tau=\ZZ\langle\tau\cap N\rangle$ — the sublattice generated by
   the lattice points, which is precisely the distinction at issue).
2. The moment map is not a torus bundle: over the relative interior of a $k$-face the fibre is $(S^1)^k$, the preimage is
   the orbit of complex dimension $k$ (`D-TORMOMENT`, read: the compact torus $T_c\cong(S^1)^n$ and $\mu\colon X_P\to M_\RR$).
3. $H^*$ is the Stanley–Reisner ring (`T-TORCOHOM`, read: the ideal $I_\Sigma$ and the presentation for a smooth complete
   toric variety).
**Page now (`toric/topology.md:31,55,47`): all three right.** No repair. The `[@Ful93, §3.2]` and `§4.2` locators remain
unverified (§9).

### 2.12 Row 12 — the del Pezzo page, and a withdrawal
**Decision.** Both flagged sentences were false, and the corrected reason is *definitional*, not a lattice-point count:
for a smooth complete toric surface with $-K$ Cartier and ample, $P_{-K}=\{m:\langle m,u_\rho\rangle\ge-1\ \forall\rho\}$
has its facets on the hyperplanes $\langle m,u_\rho\rangle=-1$ with $u_\rho$ a **primitive** lattice vector, so each facet
is at lattice distance exactly one from the origin; "distance two" contradicts the displayed inequalities, and no facet can
pass through the origin because $-K$ is not trivial. Reflexivity is a condition on the *polar*, stated in the card
`D-TORREFL` (read: $P^\circ=\{u:\langle m,u\rangle\ge-1\ \forall m\in P\}$ and the facet description with $a_F>0$).
**Withdrawal.** My second version argued "a facet at distance two would contain no lattice point in its relative
interior". That reasoning is invalid, and the review supplies the counterexample: the triangle
$\operatorname{Conv}((2,-2),(2,2),(-1,0))$ contains the origin in its interior and has facets at distances $1,1,2$, the
distance-two facet being the segment from $(2,2)$ to $(-1,0)$, whose only lattice points are its endpoints. So a
distance-two facet can exist and the correct ground is the definition, as stated above. The page's own display is right.
**Page now (`toric/toric-del-pezzo-surfaces.md:55-59,66`): true**, with $K^2=12-d$ (`PR-FULKSQ`, read) and the five
degrees $9,8,8,7,6$ recomputed from $3,4,4,5,6$ rays.

### 2.13 Row 13 — rational maps
**Decision.** A birational map from a **normal** variety to a projective variety is undefined only in codimension $\ge2$
(Har77 **Lemma V.5.1**, read: "if $T\colon X\to Y$ is a birational transformation of projective varieties, and if $X$ is
normal, then the fundamental points of $T$ form a closed subset of codimension $\ge2$"), and Vakil **Ex 15.3.B** read
gives the mechanism: for a Noetherian $X$ and an irreducible codim-one $Z$ whose generic point is regular,
$\OO_{X,Z}$ is a DVR and the domain of definition contains a dense open of $Z$. A blowup is birational with normal
source and target and changes a divisor, so "isomorphism in codimension one" is false. For maps to $\PP^n$: an
$(n+1)$-tuple of rational functions modulo $k(X)^\times$ is a rational map with no dominance hypothesis (Har77
**Theorem II.7.1**, read).
**Cross-reference finding (kept):** `varieties/rational-maps.md:21` writes "at a point of codimension one the local ring
$\OO_{X,\eta}$ is a discrete valuation ring". $\eta$ is this corpus's generic point; the ring meant is $\OO_{X,x}$ at the
codimension-one point. The same slip is in the card `D-VARBIRAT`'s proof of its codimension-two proposition, so this is
one defect with two locations, and the card's proof has a second problem: it cites "[@Har77, §I.4]" for a statement
Hartshorne states in V.5.1.
The citation defect at `:48` is §3.4 (II.8.19/Ex II.8.8 support the *other* claim; the extension step is II.6.3A).

### 2.14 Row 14 — the Segre claim, generally
**Decision.** For all $r,s$: $\psi\colon\PP^r\times\PP^s\to\PP^N$ with $N=rs+r+s$, $(a,b)\mapsto(a_ib_j)$, is injective
with image $Z(\mathfrak a)$ where $\mathfrak a=\ker(k[z_{ij}]\to k[x,y]$, $z_{ij}\mapsto x_iy_j)$ — Har77 **Exercise
I.2.14**, read verbatim, which states exactly this. Since $\psi$ is a closed immersion, for closed $X\subseteq\PP^r$,
$Y\subseteq\PP^s$ the product $X\times Y$ is closed in $\PP^r\times\PP^s$ and $\psi(X\times Y)$ is closed in
$\PP^N$; projectivity of the product follows for every $r,s$. $m=n=1$ is the illustration (the single minor
$z_{00}z_{11}-z_{01}z_{10}$), not the argument.
**Page now (`varieties/projective-varieties.md:41-44`): the general statement.** No repair.

### 2.15 Row 15 — dominance, with the finding this row owns
**Decision.** Dominance is needed exactly to pull functions back: a dominant rational map $\varphi\colon X\dashrightarrow Y$
of varieties induces a $k$-algebra map $k(Y)\to k(X)$, $g\mapsto g\circ\varphi$, and the card `D-VARBIRAT` (read) states
the contravariant correspondence with finitely generated field extensions, citing Har77 **Theorem I.4.4** and **Corollary
I.4.5** (both read: Cor I.4.5 is the equivalence "birational ⟺ $k(X)\cong k(Y)$"). Maps to $\PP^n$ need no dominance, so
the page is right to attach it only to the general target.
**Finding on this row:** `varieties/rational-maps.md:22` says dominant maps "pull functions back **along the inclusion**
$k(Y)\into k(X)$ of function fields". What exists is an induced map $\varphi^*\colon k(Y)\to k(X)$, which is injective
because $\varphi$ is dominant; writing it as an inclusion presupposes the identification of $k(Y)$ with its image, and
for a non-dominant map there is no such map at all. That is a precise-statement defect (PR-15): the object is
$\varphi^*$, and its injectivity is the content of dominance.

## 3. Mathematical defects, with location, hypothesis and witness

### 3.1 Projection formula with no hypothesis — `sheaves/pushforward-and-pullback.md:42`
"The projection formula is … $f_*(\mcf\tensor f^*\mcg)\cong f_*\mcf\tensor\mcg$." Har77 **II.5.1(d)** (read) requires
"**$\mathcal E$ a locally free $\OO_Y$-module of finite rank**"; **Ex III.8.3** restates it with the same hypothesis.
Without finite local freeness the two sides are not related by a theorem. Repair: carry the hypothesis and cite II.5.1(d)
(the card `PR-SCHPROJFORM` owns it).

### 3.2 Generating sections ≠ embedding — `sheaves-of-modules/line-bundles.md:21`
"For $X$ proper over a field, a line bundle $\mcl$ generated by sections $s_0,\dots,s_n$ defines a morphism $X\to\PP^n$, and
this morphism is a closed embedding exactly when $\mcl$ is very ample." **False.** Har77 **II.7.3** (read in full) is
about the **span**: "Let $V\subseteq\Gamma(X,\mathcal L)$ be the subspace spanned by the $s_i$. Then $\varphi$ is a closed
immersion if and only if (1) elements of $V$ separate points … and (2) elements of $V$ separate tangent vectors".
Counterexample: $X=\PP^1$, $\mcl=\OO(2)$ (very ample), $s_0=x^2$, $s_1=y^2$; these generate $\OO(2)$ (no common zero) and
give $[x:y]\mapsto[x^2:y^2]$, of degree $2$, which is not injective. `morphisms/projective-morphisms.md:45` states the
criterion correctly with $V$, so the two pages contradict each other at the baseline.

### 3.3 Toric very ampleness: shift by the Cartier datum, and the right semigroup — `toric/polytopes-and-divisors.md:52`
"$D$ is very ample exactly when it is ample and the lattice points of $P_D$ generate the local semigroup $S_\sigma$ at
every vertex". **Two errors, and my second version repeated the second one.**
- The lattice points of $P_D$ need the **shift by the vertex**: the vertices of $P_D$ are the Cartier data $m_\sigma$, and
  on $U_\sigma$ the map is $p\mapsto(\chi^{m_1-m_\sigma}(p),\dots)$ (CLS, proof of **Theorem 6.1.14**, read: "$m_\sigma\in
  P_D$ … on $U_\sigma$, $\phi_D$ is given by $(\chi^{m_1-m_\sigma},\dots,\chi^{m_s-m_\sigma})$").
- **The two semigroups are different objects.** $S_\sigma=\sigma^\vee\cap M$ is the *cone* semigroup of the affine chart;
  $\mathsf S_{P_D,m_\sigma}=\mathbb N(P_D\cap M-m_\sigma)$ is the *translated polytope* semigroup (CLS **Definition
  2.2.17**, read). Very ampleness says the second is **saturated** — i.e. it *equals* $\mathsf S_{P_D,m_\sigma}$, not that
  the raw lattice points "generate $S_\sigma$"; CLS **Proposition 2.2.18** (read) is "a normal lattice polytope is very
  ample", which is where saturation enters.
Repair: "for every maximal cone $\sigma$ with Cartier datum $m_\sigma$, the semigroup $\mathbb N(P_D\cap M-m_\sigma)$ is
saturated", citing CLS Definition 2.2.17 and Theorem 6.1.14.

### 3.4 Gluing axiom missing — `sheaves/the-sheaf-condition.md:12`
"A sheaf is a presheaf whose sections are determined by their restrictions to the members of any open cover" — the
locality axiom alone. The page's own `:18-19` says the two axioms are independent, so the opening defines a sheaf by one
of them and then separates them. Witness that existence is not automatic: the constant presheaf on a two-point discrete
space has no section restricting to a prescribed pair of different values over the two points, although the family is
compatible. (`D-RCCFY` owns both axioms.)

### 3.5 The dual class on the plane-curve page — `curves-and-surfaces/curves-in-projective-space.md:87`
The page (rewritten by #188 at `edd7f51680`) now reads at `:87`: "the Gauss map $C\to C^\vee$ is birational onto the dual
curve, and its composite with the projection of $(\PP^2)^\vee$ from the point corresponding to a general line $L$ has
degree $d(d-1)$; **that number is the class of $C^\vee$**, the number of tangent lines through a general point of the
plane". Two mislabels, both live:
- $d(d-1)$ is the class of $C$, i.e. $\deg C^\vee$ — which the same section says correctly two lines earlier at `:86`
  ("the degree of $C^\vee$ is the class of $C$"). The class of $C^\vee$ is $\deg (C^\vee)^\vee=\deg C=d$ by biduality,
  which the page itself invokes at `:89` ("biduality says $(C^\vee)^\vee=C$").
- "the number of tangent lines through a general point of the plane" is the definition of the class of $C$, so the
  appositive names the wrong curve's class.
Repair: "that number is the class of $C$, that is, $\deg C^\vee$".
**Correction to my second version:** it recorded this page's defect as "the Gauss map has degree $d(d-1)$". That sentence
was the *pre-rewrite* text and #188 has since fixed it; the surviving defect is the one above, at `:87`, which my second
version missed. Neither reading may be carried forward as current without re-checking the blob.

## 4. The cards

### 4.1 `T-FFDESCENT` — corrected here, against my earlier verdict
`corpus/theory/Algebraic_Geometry/T-FFDESCENT.md:71` said the quasi-inverse sends $(N,\theta)$ to
$\{n:\theta(n\otimes1)=1\otimes n\}$ "under the identifications $C\otimes_{B,p_1}N\cong N\otimes_AB$ and
$C\otimes_{B,p_2}N\cong B\otimes_AN$". With $p_1(b)=b\otimes1$ and $p_2(b)=1\otimes b$ those two identifications belong the
other way round: tensoring over $B$ through $p_1$ leaves the second factor of $C=B\otimes_AB$, giving
$C\otimes_{B,p_1}N\cong B\otimes_AN$, and through $p_2$ leaves the first, giving $C\otimes_{B,p_2}N\cong N\otimes_AB$.
With that pairing the condition that is well typed and recovers $M$ is $\theta(1\otimes n)=n\otimes1$: for $N=M\otimes_AB$
the canonical $\theta$ is the flip, $1\otimes n=1\otimes m\otimes b\mapsto b\otimes m\otimes 1=n\otimes 1$, and the
invariant elements are exactly $m\otimes1\cong M$.
**Repaired** at `96ef469b62` (identification order and condition together), cited to Stacks 023N and 03OE as before.
**My earlier verdict was wrong**: I recorded the card as "repaired, MET", relying on commit `1287f30106`, which had
changed the condition in the wrong direction. The card gate passes: `qualc.authoring check T-FFDESCENT` →
"schema and Markdown parsing OK".

### 4.2 `PR-RJ3P7` — qualified here
`:51` said "Going down is what makes heights match, $\operatorname{ht}\mfq=\operatorname{ht}(\mfq\cap A)$, **under its
hypotheses**". The remark has just given two going-down statements, one for integral extensions with integrally closed
base and one for **every flat** ring map, and height equality is a consequence only of the first together with going up and
incomparability. Flat going down alone refutes it: $\ZZ[x]\to\ZZ[x,y]$ is flat (free), the prime $(y)$ has height $1$, and
its contraction $(0)$ has height $0$.
**Repaired** at `13f9c3a8eb`: the sentence now restricts the height statement to the integral case, states the
counterexample, and keeps the geometric sentence on generizations, which is true for both going-down statements.
Card gate passes.

### 4.3 The four cards the earlier review asked to adjudicate
- **`D-CRVHYP`** — definition cites Har77 **Ex IV.1.7** (read: "A curve $X$ is called hyperelliptic if $g\ge2$ and there
  exists a finite morphism $f\colon X\to\PP^1$ of degree 2"); proposition cites **Prop IV.5.3** (read) and the
  base-point-freeness reproduces **Lemma IV.5.1** (read). **MET.**
- **`T-MORMIRACLE`** — Vakil **26.2.10** and **26.2.11** both read; the card is the same theorem with the letters of the
  local map written in the opposite order from Vakil's ($B\to A$ there, $A\to B$ here), which a reader needs to be told.
  **MET, with that convention to state.**
- **`D-ETFPPF`** — Stacks **021M** read ("any fppf covering is a family of flat, locally of finite presentation morphisms
  with $T=\bigcup f_i(T_i)$") and **021N** read ("Any syntomic covering is an fppf covering, and a fortiori, any smooth,
  étale, or Zariski covering is an fppf covering"). **MET** — the second number, which my second version left unread, now
  checks.
- **`D-GROTHTOP`** — the site definition ends "(Stacks Project, Chapter 7, *Sites and Sheaves*)", a chapter, not a tag.
  I fetched the chapter: Chapter 7 is tag **00UZ**, and the site definition is **Definition 7.6.2, tag 00VH** (read: "a
  site is given by a category $\mathcal C$ and a set $\mathrm{Cov}(\mathcal C)$ of families of morphisms with fixed target
  $\{U_i\to U\}_{i\in I}$, called coverings … satisfying the following axioms"). Note the mismatch of presentation:
  00VH defines a site by **covering families**, the card by **covering sieves**, so citing 00VH needs either the sieve
  formulation's own tag or a sentence that the two presentations agree. **NOT MET on citation form**; the wiki sentence at
  `stacks-and-moduli/functors-and-topologies.md:12` copies the card, so it is fixed with the card.

### 4.4 `PR-VGA2L` and Chevalley–Warning — open, and not closable here
`corpus/theory/Algebraic_Geometry/PR-VGA2L.md:64` (unchanged at the current tip): "Chevalley–Warning gives a nonzero
solution over $\FF_q$, hence a $k$-rational point on $C$." No numbered statement, no hypothesis transcribed, and no
retained text of the theorem on the machine (`tmp/sources` has none; no bibliography key). Transcluded by
`curves-and-surfaces/genus.md:24` and by `curves-and-surfaces/riemann-roch-for-curves.md`, so the gap shows on two pages.
Verdict: **waiting on a numbered statement**; the complaint is the sibling commit `b27109aeb5`. I do not invent a number.

## 5. Sources read for this version, and the one that could not be

Read at the statement for this version, in `tmp/sources/hartshorne-1977-algebraic-geometry.md` unless noted:
II.1.2, II.2.3, Ex II.2.4, Prop II.2.6, **Ex II.2.3.2**, II.5.1(d), II.5.11, II.5.15, II.6.4, II.6.5, II.6.11,
Remarks II.6.11.1A and II.6.11.2, Example II.6.11.3, Prop II.6.15, Cor II.6.16, Cor II.6.17, II.7.1, II.7.3, II.7.6,
II.7.7, II.8.15, II.8.17, II.8.19, II.8.20, II.8.22A, II.4.9, Cor II.4.8, II.2.5, Ex II.2.9, Ex II.2.13, Ex II.5.7,
Thm III.3.7, Ex III.2.1, **III.4.5**, **III.5.1**, **Ex III.5.3**, Ex III.5.7, Caution III.6.5.2, **Ex III.6.2**,
Ex III.8.3, Prop III.9.7, Prop IV.1.3, Ex IV.1.3.3, Ex IV.1.3.5, **Ex IV.1.7**, **Ex IV.1.8**, Prop IV.2.2, Prop IV.2.3,
Cor IV.2.4, Prop IV.2.5, Ex IV.2.5.1–2.5.5, Ex IV.3.4, Cor IV.3.2, Prop IV.3.1, Prop IV.4.12B, Thm IV.4.15B, Thm IV.4.16,
Thm IV.4.19, Lemma IV.5.1, Prop IV.5.2, Prop IV.5.3, Thm IV.5.4, Ex IV.5.2.1, Ex IV.5.2.2, Thm I.1.8A, Prop I.1.12A,
Thm I.3.4, Thm I.3.9A, Cor I.4.5, **Ex I.2.14**, Ex I.2.1, Ex I.2.2, Ex I.2.4, **Ex I.3.6**, Ex I.7.1, Ex I.7.2, Thm I.7.7,
Cor I.7.8, Prop I.3.1, Prop II.3.1, Prop I.6.8, Thm V.1.10, Prop V.3.4, Thm V.4.9, Cor V.5.4, Lemma V.5.1, Thm V.5.7,
Remark V.5.7.2.

**Vakil**, `tmp/sources/vakil-rising-sea-2025-10-21.md`: **Ex 8.3.I** (finite morphisms to $\Spec A$ are projective),
**Def 7.3.10** (functor of points), **Lemma 5.3.2** (affine communication), **Ex 15.3.B** (extension over regular
codimension-one sets), **Ex 16.2.G** (finite pullback of an ample bundle), **Thm 12.4.3**, **Thm 26.2.10**,
**Thm 26.2.11**.

**Stacks**, fetched live: **021M**, **021N**, **00VH**, **0G12**.

**CLS**, `tmp/sources/cox-little-schenck-2011-toric-varieties.md`: **Def 2.2.17**, **Prop 2.2.18**, **Lemma 6.1.13**,
**Thm 6.1.14**, **Prop 1.1.9**.

**Cards read**: `D-SHFSIX` (six operations, $j_!$, $Rf_!\dashv f^!$, base change), `D-SCHCMGOR` (CM, Gorenstein, lci,
dualizing sheaf), `D-VARBIRAT` (rational/birational maps, function fields, the codimension-two proposition and its proof),
`T-CRVMINMOD`, `T-BIRINV`, `FE-TORCD`, `T-TORSURF`, `D-FULSAT`, `PR-TORMOR`, `T-FULBETTI`, `D-TORMOMENT`, `T-TORCOHOM`,
`D-FULSTAR`, `PR-O8V3I`, `D-TORREFL`, `PR-FULCRIT`, `PR-FULKSQ`, plus the four of §4.3 and the two of §4.1–4.2.

**Not read, and therefore supporting nothing here:** Atiyah–Macdonald, which is not on the machine — so the numbers
5.10, 5.11 and 5.16 quoted by `morphisms/finite-and-flat.md:20-24` and by `PR-RJ3P7` are **unverified citations**, and
the only mathematical claim in that material that this record decides is the height statement, decided by the
$\ZZ[x]\to\ZZ[x,y]$ counterexample rather than by the book.

## 6. Policy findings

- **Two undefined control words**, both live at the baseline and one still live: **`\sp`**
  (`schemes/properties-from-the-ring.md:18`, still live: the corpus macro is `\underlyingspace{…}`; Hartshorne writes
  `sp(X)` in Ex II.2.13, which is presumably where it came from); **`\tensorn`**
  (`stacks-and-moduli/functors-and-topologies.md:65` at the baseline, repaired by #188 at `c910f0e80f` — a missing space
  in `1\tensor n`). Neither is a TeX command and neither is caught by `qualc check`.
- **Surviving positional prose** (PROSE-03; the last is SEC-10): `schemes/what-is-a-scheme.md:80` "the criterion above";
  `curves-and-surfaces/special-divisors-and-the-canonical-map.md:22` "Two consequences organise everything below";
  `morphisms/projective-morphisms.md:50` heading "Consequences used later";
  `stacks-and-moduli/functors-and-topologies.md:20` "in both directions below".
- **Definition-shaped prose with no "Recall"** (DEF-1, DEF-17, DEF-29): `schemes/ringed-spaces.md:16`; and at the
  baseline `schemes/subschemes-and-points.md:12`, repaired when that page was rewritten.
- **CITE-1 unkeyed inline reference:** `toric/affine-computations.md:14`, `[Cox--Little--Schenck, *Toric Varieties*,
  Proposition 1.1.9]` — the number is right (read), the form needs a Zotero key.
- **CITE-8, citations that do not state the claim:**
  `varieties/rational-maps.md:48` (II.8.19 and Ex II.8.8 are birational invariance of $p_g$ and of plurigenera/Hodge
  numbers; the codimension-two extension is **II.6.3A**, which is how 8.19's own proof gets it — and the card `T-BIRINV`
  uses those two numbers correctly, which is the contrast that settles it);
  `divisors/weil-and-cartier.md:34` (**Ex IV.1.8** is $p_a$ of a singular curve, not the Picard sequence) — new here;
  `varieties/projective-varieties.md:18` (the empty-set criterion is **Ex I.2.2**; I.2.4 is the bijection);
  `curves-and-surfaces/curves-in-projective-space.md:19` at the baseline (an unsupported assertion, since removed by
  #188's rewrite).
- **PROVENANCE-01:** `syllabus.md:10` claims every section names its document, and `:149, :163, :183, :197` name none
  (each opens "The numbered items group the topics by subject." at `:151, :165, :185, :199`); `:167`'s eight Reid
  locators are unkeyed.
- **PROSE-11 / RESOURCE-11:** `resources.md:58, :87, :148, :194`. Not defects: the nine vendored solution PDFs at
  `:94-110` each carry a ledger disposition; `:192`'s Stacks entry was checked against tag 0G12 (Section 111.63,
  exercises 111.63.1–111.63.7).
- **SEC-2:** `sheaves/the-sheaf-condition.md:19` (three counterexamples in one unfenced sentence above the card that
  states them); `sheaves/examples-of-sheaves.md:33`. **PR-18/PROSE-05:** `schemes/what-is-a-scheme.md:53` ("the two one
  expects").

## 7. Carried mathematical defects, re-verified at the baseline

- `cohomology/derived-functors-and-vanishing.md:46` — "affine vanishing fails for a **quasicoherent** sheaf that is not
  coherent". Har77 **Ex III.2.1** (read) is about $j_!\ZZ_U$, which is not quasicoherent; the block's own title is
  "Quasicoherence cannot be dropped". **Repaired by #188 at `34d031aac8`**, with the same reading.
- `curves-and-surfaces/special-divisors-and-the-canonical-map.md:49` — "$\ell(K-p-q)=g-3$" should be $g-2$ (Hartshorne's
  criterion is $\dim|K-P-Q|=g-3$, **Prop IV.3.1(b)** read, and the page's own $\ell(p+q)=1$ forces $g-2$).
  `divisors/line-bundles-and-linear-systems.md:30` states it correctly. **Still open** at the current tip.

## 8. Per-page ledger (baseline `078db711f834`)

After each path, what was checked on it. A page not named as defective is one on which this reading found nothing — not a
page certified clean. The 82 paths themselves are enumerated in §10.

- `cohomology/`: `computing-cohomology.md` [III.4.5, III.5.1 read]; `derived-functors-and-vanishing.md` [§7; Grothendieck
  bound sharp]; `families.md` [flatness example by hand]; `homological-algebra.md` [§2.1, Caution III.6.5.2 and Ex
  III.6.2 read]; `index.md`; `projective-schemes.md` [`T-COHBC` not opened, §9]; `vanishing-and-duality.md` [III.3.7,
  `T-5IOUR`'s qcqs variant not opened].
- `curves-and-surfaces/`: `blowups-and-the-classification-of-surfaces.md` [Thm V.4.9 read]; `crepant-resolutions.md`
  [§2.2]; `curves-in-projective-space.md` [§3.5, Ex IV.3.4 read]; `elliptic-curves-over-c.md` [Thm IV.4.12B, 4.15B,
  4.16, 4.19 read]; `elliptic-curves.md` [twist by hand]; `embeddings-and-jacobians.md` [cards not re-read];
  `genus.md` [`PR-VGA2L` transcluded, §4.4]; `index.md`; `intersection-theory-on-surfaces.md`; `moduli-of-curves.md`;
  `riemann-hurwitz.md` [§2.3]; `riemann-roch-for-curves.md` [`PR-VGA2L` transcluded]; 
  `special-divisors-and-the-canonical-map.md` [§7].
- `divisors/`: `class-group-and-picard-group.md` [§2.4, all six numbers read]; `index.md`;
  `line-bundles-and-linear-systems.md` [IV.3.1 read]; `positivity.md` [II.7.6 read]; `weil-and-cartier.md` [§2.4, Ex
  IV.1.8 read and found not to state the sequence].
- `morphisms/`: `classes-of-morphism.md` [Vakil Ex 8.3.I read]; `fibres-and-images.md`; `finite-and-flat.md` [AM not on
  the machine, §5]; `index.md`; `inseparable-morphisms-and-luroth.md` [Prop IV.2.5 read verbatim];
  `projective-morphisms.md` [§2.5, §6]; `separated-and-proper.md` [I.3.4 read]; `smooth-unramified-etale.md` [cards].
- `schemes/`: `dimension.md` [§2.6]; `fibre-products-and-base-change.md` [$\FF_9$ fibre by hand]; `index.md`;
  `normalization.md` [II.8.22A, II.6.3A, I.3.9A read]; `proj-and-gluing.md` [II.2.5, Ex II.3.12, Ex II.2.12, II.4.9,
  Cor II.4.8 read]; `properties-from-the-ring.md` [§6, all four numbers read]; `ringed-spaces.md` [§2.7, §6, Ex II.2.3.2
  read]; `subschemes-and-points.md`; `what-is-a-scheme.md` [Prop II.2.3, Ex II.2.4, Prop II.2.6, Thm III.3.7, Vakil
  Lemma 5.3.2 read; §6].
- `sheaves-of-modules/`: `differentials.md` [II.8.17 read]; `index.md`; `line-bundles.md` [§3.2, II.7.3 read];
  `operations.md` [$\FF_p$ pullback by hand]; `projective-sheaves.md` [II.5.11, II.5.15 read]; `quasicoherence.md`;
  `tangent-normal-and-canonical-sheaves.md` [§2.9, Prop II.8.20 read].
- `sheaves/`: `examples-of-sheaves.md` [§6]; `index.md`; `morphisms-of-sheaves.md`; `pushforward-and-pullback.md`
  [§2.8, §3.1]; `stalks-and-exactness.md`; `the-sheaf-condition.md` [§3.4, §6].
- `stacks-and-moduli/`: `functors-and-topologies.md` [§4.3, §6; Stacks 021M/021N read]; `index.md`;
  `spaces-and-stacks.md`.
- `toric/`: `affine-computations.md` [§6, CLS Prop 1.1.9 read]; `criteria.md`; `examples.md` [§2.10, computations by
  hand]; `index.md`; `polytopes-and-divisors.md` [§3.3, CLS Def 2.2.17/Prop 2.2.18/Thm 6.1.14 read];
  `surfaces-and-morphisms.md` [`FE-207WC` not opened]; `the-dictionary.md`; `topology.md` [§2.11, Ful93 locators
  unverified]; `toric-del-pezzo-surfaces.md` [§2.12, `PR-FULKSQ` read].
- `varieties/`: `affine-or-projective.md`; `blowups.md` [Prop V.3.4 read]; `canonical-class.md` [II.8.20];
  `dimension-and-degree.md` [I.7.7, Cor I.7.8, Ex I.7.1, Ex I.7.2, Ex III.5.3 read]; `index.md`;
  `morphisms-of-varieties.md`; `nonsingular-curves.md` [Prop I.6.8, II.6.3A read]; `projective-varieties.md` [§2.14,
  §6]; `rational-maps.md` [§2.13, §2.15, V.5.1 and Vakil 15.3.B read]; `regular-functions.md` [I.3.4, Ex I.3.6 read];
  `smooth-and-singular.md`; `the-dictionary.md`.
- root: `index.md`; `resources.md` [§6]; `syllabus.md` [§6].

## 9. What is undecided, exactly

1. **Atiyah–Macdonald 5.10, 5.11, 5.16** — no text on the machine. The pages that quote them
   (`morphisms/finite-and-flat.md:20,22`, `schemes/normalization.md:28`, `PR-RJ3P7`'s two theorems) are therefore
   **undecided at citation level**; the one mathematical claim in them that this record decides, the height equality, is
   decided by counterexample (§4.2), not by the book.
2. **Fulton's locators** — `toric/topology.md:29` (`§3.2`), `:55` (`§4.2`), `toric/index.md:16`, `syllabus.md:187`. No
   text; the statements are decided from the corpus cards and CLS where CLS states the same theorem.
3. **Mori's existence theorem** for crepant resolutions of terminal Gorenstein threefolds — no retained text. The verdict
   on the page does not depend on it; the verdict on claim 2 of row 2 rests instead on claim 3 plus the definitions.
4. **Cards not opened**: `T-5IOUR` (qcqs form of Serre's criterion — the noetherian/coherent form, Thm III.3.7, is read),
   `T-COHBC` (semicontinuity), `FE-207WC`, `T-SRFZMT`, `T-SRFCAST`, `FE-SRFFERMATQUARTIC`, `D-TORQD`/`T-TORDIV`,
   `PR-TORPOS`, `D-CRVBRILLNOETHER`, `D-8XX95`, `D-L6ERW`. Pages leaning on them are marked in §8.
5. **`syllabus.md:37`'s Berkeley document** — not fetched.
6. **The reviewers' own cross-reference lists** — neither report text was supplied. Rows 3, 4, 6, 7, 13, 15 now carry the
   findings I can substantiate at their locations; where a reviewer's item is not among them it is unanswered, not denied.

## 10. The 82 files at `078db711f834` (3908 lines), enumerated

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

## 11. What this file does not do

It repairs two cards (§4.1, §4.2) and nothing else: the page-level defects of §3 and §6 name their owning file for #187
(a false sentence, a missing hypothesis, a citation) or the orchestrator (a key for CLS and for Reid, and the
Chevalley–Warning statement). It runs no gate beyond the two per-card checks it reports. **It does not claim #189's
first acceptance clause is met**: §9 lists what is undecided, and §8 records where this reading found nothing rather than
certifying it.
