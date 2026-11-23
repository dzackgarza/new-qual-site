# #189: `wiki/algebraic-geometry/` — the reading record, fourth version

**Status: bounded adjudication, not a claim that #189's first acceptance clause is met.** Reviewer gzg9 returned NOT MET
at `078db711f834`; reviewer Kimi max returned NOT MET on the second version; reviewer Kimi **ra84** returned NOT MET on the
third and named seven adjudications of that version as false. This version corrects all seven, repairs the page and card
defects they and this session's page read expose, and states in §9 exactly what is still unread.

The seven corrections are not relabellings: each is a different mathematical statement from the one the third version
made, and four of them are corrections to arguments the third version itself wrote.

**This is the fifth version.** It carries four corrections the fourth version left open — the Picard-sequence locator at
`divisors/weil-and-cartier.md:34`, now **Exercise II.6.9(a)**, read at the statement; the canonical-descent locator at
`stacks-and-moduli/functors-and-topologies.md:64`, which attaches the canonical-instance formula to **Section 35.3, tag
023F**, not to Definition 35.3.1; the facet conclusion of §0 item 4, which was false in the fourth version too; and the
miracle-flatness gloss of §0 item 6, which misdescribed Vakil **26.2.11** and made purity necessary — together with one
batch of named transcluded cards actually read, §9.1.

## 0. The seven ra84 items, corrected

| ra84 item | The third version said | What is true | Repaired in |
|---|---|---|---|
| 1. Terminal singularities and crepant small resolutions | "Terminal singularities admit none: true, vacuously … a crepant resolution has no exceptional divisor and **is an isomorphism**" (§2.2 item 3) | A crepant resolution of a terminal singularity has no exceptional **divisor**, hence is **small**; it need not be an isomorphism, and it need not be unique. The ordinary double point $\{xy-zw=0\}\subseteq\CC^4$ is terminal and has **two non-isomorphic** crepant small resolutions, related by the Atiyah flop | card `D-VARCREPANT` at `5c8e30e20c` |
| 2. Injectivity and finite surjectivity | "it **needs** $\phi$ injective" (`PR-RJ3P7:47`), i.e. injectivity necessary for $f$ surjective | Injectivity is **sufficient and not necessary**. $k[t]/(t^2)\to k$, $t\mapsto0$, is non-injective and $\Spec k\to\Spec k[t]/(t^2)$ is a homeomorphism of one-point spaces; what injectivity excludes is the primes outside the kernel, which is why $\ZZ\to\ZZ/2$ misses the generic point | card `PR-RJ3P7` at `afe86c9d92` |
| 3. The canonical descent $\theta$ | "for $N=M\tensor_AB$ the canonical $\theta$ **is the flip**", with the recovery condition $\theta(1\tensor n)=n\tensor1$ between two differently identified modules (§4.1) | Written in Stacks' own convention the datum is $\theta\colon N\tensor_AB\to B\tensor_AN$ with $\theta(n\tensor1)$ and $1\tensor n$ **both** in $B\tensor_AN$; the canonical instance is $(m\tensor b)\tensor b'\mapsto b\tensor(m\tensor b')$. The third version's pairing made the condition an identity, so it recovered $N$, not $M$ | card `T-FFDESCENT` at `d9477e605a`, page `stacks-and-moduli/functors-and-topologies.md` at `0204ce05f4` |
| 4. The "distance-two facet" counterexample | "the triangle $\operatorname{Conv}((2,-2),(2,2),(-1,0))$ … has facets at distances $1,1,2$" (§2.12) | That triangle has **all three** facet distances $2/\gcd(2,3)=2$: the edges are $x=2$, $-2x+3y=2$ and $-2x-3y=2$, each at lattice distance $2$. It therefore does not exhibit a mix of distances, so the third version's $1,1,2$ is false; but the triangle remains a witness, because $(2,0)$ lies in the relative interior of the edge $x=2$, $-2<y<2$, so a facet at lattice distance two **can** carry a relative-interior lattice point, and this triangle refutes the universal claim that none does. Reflexivity is argued definitionally, from $\inner{m}{u_\rho}=-1$ with $u_\rho$ primitive | §2.12 here; no page carried the claim |
| 5. The toric translation and saturation | "$\Cone(P_D-m_\sigma)=\sigma^\vee$, **whose lattice semigroup is $S_\sigma$**" — the second clause a self-equality, since $S_\sigma$ *is* $\sigma^\vee\cap M$ | The translation is $\Cone(P_D\cap M-m_\sigma)=\sigma^\vee$, which is CLS (6.1.6) together with **Exercise 6.1.10** (the proper faces of $\Cone((u_\rho,-a_\rho))$ project to the cones of $\Sigma$); very ampleness is the **saturation** of $\NN(P_D\cap M-m_\sigma)$ inside $S_\sigma$, which is **Proposition 6.1.10(c)** and its proof | card `PR-TORPOS` at `9837cb2c28`, page `toric/polytopes-and-divisors.md` at `0204ce05f4` |
| 6. Miracle flatness and its citations | the pointwise equality "forces $f$ to be flat", the card's hypothesis being the **numerical** equality (§2.6, §4.3) | Vakil **26.2.10** assumes the fibre ring has **pure** dimension $\dim B-\dim A$; the numerical equality alone is what a flat local map satisfies. **26.2.11** does not restate that purity: its printed hypotheses are pure-dimensional $X$ and $Y$, $X$ Cohen--Macaulay, $Y$ regular, and fibres of dimension $\dim X-\dim Y$. Purity is not necessary either: Stacks **Lemma 10.128.1, tag 00R4** derives flatness from $\dim S=\dim R+\dim(S/\mfm_RS)$ alone, with $R$ regular and $S$ Cohen--Macaulay. The pointwise form now carries equidimensionality of $\OO_{X_y,x}$ | card `T-MORMIRACLE` at `1da5ab5aa3`, page `schemes/dimension.md` at `0204ce05f4` |
| 7. The alleged properness defect in Vakil 16.2.G | the page "states the unrestricted version, which is fine but **is not what the citation says**" (§2.5 item 3) | Vakil's own remark inside 16.2.G says the result "applies in that situation, i.e. with 'proper $A$-schemes' changed to 'schemes', without change". There is no defect to record: the unrestricted statement is the exercise's stated extension | §2.5 here; page unchanged |

## 1. Baseline and scope

- **Read in full this session**: all **82** files under `wiki/algebraic-geometry/`, **4273 lines** measured per blob at
  `c9e3611a3d`, the tip this session started from. Every path is enumerated in §10 and adjudicated in §8.
- Policies: `CONTRIBUTING.md` and the writing policy it links (`section-structure.md`, `citations.md`, `prose.md`,
  `prose-tells.md`, `definitions.md`, `resource-descriptions.md`). The policy findings of §6 are the ones this reading
  re-checked on the current blobs.
- **Transcluded cards**: the 82 pages transclude **327** distinct card ids. **Read in full this session**: `T-FFDESCENT`,
  `D-VARCREPANT`, `FE-207WC`, `PR-RJ3P7`, `T-MORMIRACLE`, `PR-MIRACLEFLAT`, `PR-TORPOS`, `D-TORQD`, `D-FULSAT`,
  `D-TORREFL`. **Read in part**: `T-COHBC` (statement headers, for the semicontinuity link at
  `cohomology/projective-schemes.md:28`), `PR-VGA2L` (the anticanonical and Chevalley–Warning passage, §4.4),
  `D-MODAMPLE`, `D-MORPROJ`, `D-MORFIN`, `FE-MORNOTPROPER`, `D-SRFADE` (the sentences about properness, projectivity and
  Du Val points that the pages lean on). **Not read, supporting nothing here**: the remaining ~310 cards. That is the
  largest single gap in this record and it is stated as a gap, not as a coverage.

## 2. The fifteen #175 flags

Row numbering is #175's bullet order. Rows 2, 3, 4, 5, 6, 10, 11, 12, 13, 15 changed verdict or witness since the third
version; rows 1, 7, 8, 9, 14 stand as they were, re-checked on the current blobs.

| # | Flag | Verdict | § |
|---|---|---|---|
| 1 | cokernel "not the naive one" in both categories | false for $A$-modules, true for $\OO_X$-modules | 2.1 |
| 2 | $(-2)$-curve; Gorenstein canonical dim 3; terminal | first false, second false as stated, third **false as the third version wrote it** — terminal excludes exceptional divisors, not crepant small resolutions | 2.2 |
| 3 | Riemann–Hurwitz $d_p$ | page gives IV.2.2 correctly; over-cites IV.2.4 | 2.3 |
| 4 | class group on an integral scheme | true for Cartier, false for Weil; the normal-case injection is Remark II.6.11.2, now cited | 2.4 |
| 5 | ampleness "stable under pullback" | false in general; each surviving clause true with its hypothesis; **no properness defect in the finite clause** | 2.5 |
| 6 | fibre dimension upper semicontinuous on $Y$ | true only for closed $f$; the miracle-flatness sentence now carries the purity hypothesis | 2.6 |
| 7 | the product of stalks | injectivity is not gluing | 2.7 |
| 8 | "the only ones available" | false: $j_!$, $Rf_!$, $f^!$ | 2.8 |
| 9 | CM/Gorenstein/lci order; `\inverseof{i}` | regular ⇒ lci ⇒ Gorenstein ⇒ CM; adjunction restricts | 2.9 |
| 10 | det-7 cone; "every toric surface from $\PP^2$"; "every toric variety is a fan" | false / true in general / false until normal | 2.10 |
| 11 | cone $\pi_1$; torus bundle; faces generate $H^*$ | page's $\pi_1=0$ right; two repaired | 2.11 |
| 12 | "lattice distance two"; "the table above" | both false; facets at distance one by definition | 2.12 |
| 13 | "isomorphism in codimension one" | false; codim $\ge2$ for normal source; the $\OO_{X,\eta}$ slip at `:21` now reads $\OO_{X,\eta}$ for the *generic* point and $\OO_{X,x}$ for the codimension-one point | 2.13 |
| 14 | the Segre claim | true in general, and the page states the general case | 2.14 |
| 15 | dominance hypothesis on maps to $\PP^n$ | unnecessary; the pullback is $\varphi^*$, now so written | 2.15 |

### 2.1 Row 1 — the two cokernels
For any ring and any $f\colon M\to N$, the cokernel in $A\text{-}\mathbf{Mod}$ is $N/\im f$. In $\OO_X\text{-}\Mod$ it is
the sheafification of $U\mapsto\coker(f(U))$ (Har77 **II.1.2**, read: "Given a presheaf $\mathcal F$, there is a sheaf
$\mathcal F^+$ and a morphism $\theta\colon\mathcal F\to\mathcal F^+$ …"). The page's witness at
`cohomology/homological-algebra.md:21-22` is the multiplication-by-$x$ presheaf quotient on $\AA^1$, whose value on
$\AA^1$ is $k$ and on $D(x),D(x-1)$ is $0$.
**Page now: true.** No repair.

### 2.2 Row 2 — the three crepant assertions, and the correction of the third
1. "A $(-2)$-curve cannot be contracted": **false.** The $A_1$ du Val configuration — one smooth rational curve $E$ with
   $E^2=-2$ on a smooth surface — contracts; the page's crepancy computation ($E\cdot K_X=0$ by adjunction, so the
   discrepancy coefficient satisfies $aE^2=0$) is a proof about this curve.
2. "Crepant resolutions exist for Gorenstein **canonical** singularities in dimension three": **false as stated.** The
   threefold existence theorem is for **terminal** Gorenstein threefolds.
3. "Terminal singularities admit none": **false, and this is ra84's first correction.** Terminal means every discrepancy
   is $>0$, so a crepant morphism out of a smooth $Y$ has no exceptional divisor over a terminal $X$ — it is **small**,
   which is not the same as being an isomorphism. The ordinary double point is terminal and has two crepant small
   resolutions, $\pi\colon X\to C$ and $\pi'\colon X'\to C$, with no morphism between them over $C$ (CLS **Example
   11.4.13** gives the cone as terminal in the lattice $\{(a,b,c):a+b+c\equiv0 \bmod 2\}$, **Exercise 11.4.13(a)** is
   the request for a crepant resolution of it, and **Proposition 11.4.12** is the terminal/canonical criterion; the two
   resolutions are `FE-207WC`, read, with Vakil **Exercise 22.4.N** and **Remark 22.4.11**).
**Page now (`curves-and-surfaces/crepant-resolutions.md:30-34`): the three sentences are gone and what remains is true.**
**Card `D-VARCREPANT:34-42` now states smallness, existence and non-uniqueness**, at `5c8e30e20c`.

### 2.3 Row 3 — Riemann–Hurwitz
Har77 **Prop IV.2.2** gives $\length=e_P-1$ tame and $\length\ge e_P$ wild; there is no "$e_P-1$ plus a $p$-multiple" in
the source. The page prints this correctly at `curves-and-surfaces/riemann-hurwitz.md:18`, and **Corollary IV.2.4** there
is the degree formula already printed at `:15-17`, so the second number is an over-citation, not an error of substance.

### 2.4 Row 4 — class group and Picard group
$\CaCl(X)\to\Pic(X)$ is an isomorphism for every integral scheme (Har77 **Prop II.6.15**); $\CaCl(X)\into\Cl(X)$ is
injective for normal $X$ (**Remark II.6.11.2**) and an isomorphism when every local ring is a UFD (**Prop II.6.11**), in
particular for regular $X$ (**Remark II.6.11.1A**); not an isomorphism in general: the affine quadric cone has
$\CaCl=0$, $\Cl=\ZZ/2$ (**Example II.6.11.3**).
**Repaired here**: `divisors/class-group-and-picard-group.md:17` now cites **Remark II.6.11.2** for the normal-case
injection (commit `0204ce05f4`).
**Still owed**: `divisors/weil-and-cartier.md:34` cites **Exercise IV.1.8** for the Picard sequence
$0\to\oplus_p\tilde\OO_p^\times/\OO_{X,p}^\times\to\Pic(X)\to\Pic(\tilde X)\to0$. Exercise IV.1.8 (read) is "$p_a$ of a
Singular Curve" and states $0\to\OO_X\to f_*\OO_{\tilde X}\to\sum_P\tilde\OO_P/\OO_P\to0$. The right number is not located
in the retained text, so it is recorded as owed rather than replaced.

### 2.5 Row 5 — ampleness and pullback, and the correction of the properness item
Four assertions at `morphisms/projective-morphisms.md:44-48`, each with its hypothesis:
1. Very ample ⇒ ample; ample ⟺ some power very ample for $X$ of finite type over a noetherian ring (Har77 **Theorem
   II.7.6**, read).
2. Restriction to a closed subscheme (Har77 **Ex III.5.7(a)**, read, under the exercise's standing hypothesis that $X$
   and $Y$ are proper over a noetherian ring — now stated on the page).
3. Pullback along a finite morphism (Vakil **Ex 16.2.G**, read: "Suppose $\pi\colon X\to Y$ is a finite morphism of
   proper $A$-schemes, and $\mathcal L$ is an ample line bundle on $Y$. Show that $\pi^*\mathcal L$ is ample on $X$").
   **ra84's seventh correction**: the third version recorded the page's unrestricted version as "not what the citation
   says". The exercise's own remark says "the result applies in that situation, i.e. with 'proper $A$-schemes' changed to
   'schemes', without change". The page states the extension the exercise states; there is no defect.
   The iff is Har77 **Ex III.5.7(d)** (read: "$f\colon X\to Y$ finite surjective, $\mathcal L$ invertible on $Y$; then
   $\mathcal L$ is ample on $Y$ if and only if $f^*\mathcal L$ is ample on $X$").
4. Not preserved by arbitrary pullback: $\pi^*\mathcal L\cdot E=\mathcal L\cdot\pi_*E=0$ for the blowup at a point of a
   surface, against Nakai–Moishezon, Har77 **Theorem V.1.10** (read).
**Verdict: the flag is answered; the page's clauses are true with their hypotheses and the third carries no defect.**

### 2.6 Row 6 — fibre dimension, and miracle flatness (correction 6)
Vakil **Theorem 12.4.3** read verbatim: (a) the dimension of the largest component of $\pi^{-1}(\pi(x))$ through $x$ is
upper semicontinuous **on $X$**; (b) the dimension of the fibre over $y$ is upper semicontinuous **on $Y$** when $\pi$
is closed. The third function $\krulldim\OO_{X_{f(x)},x}$ is not upper semicontinuous ($\AA^1_k\to\Spec k$: $1$ at closed
points, $0$ at $\eta$). The page separates all three (`schemes/dimension.md:43-52`).
**Corrected here**: `:53` now says that the pointwise equality, **with the local ring of each fibre equidimensional**,
forces flatness. Vakil **26.2.10** (read) is the local statement and
requires the fibre ring of **pure** dimension $\dim B-\dim A$; **26.2.11** (read) is a global statement whose printed
hypotheses are that $X$ and $Y$ are pure dimensional, $X$ is Cohen--Macaulay, $Y$ is regular, and the fibres of $\pi$ have
dimension $\dim X-\dim Y$ — it does not assume pure fibre rings. **Neither theorem makes purity necessary**: Stacks
**Lemma 10.128.1, tag 00R4** (fetched live this session) proves $R\to S$ flat from $R$ regular, $S$ Cohen--Macaulay and
$\dim S=\dim R+\dim(S/\mfm_RS)$, the numerical equality alone, and `dimension.md:53` now cites that lemma for the
pointwise form. What the third version got wrong was the **attribution** — it offered the numerical form as the card's
corollary from 26.2.10, whose hypothesis is purity — not the numerical statement.
Card `T-MORMIRACLE` at `1da5ab5aa3`, page `schemes/dimension.md` at `0204ce05f4`.
Second, smaller: `:48` attaches `[[T-MORFIBDIM]]` to the elementary computation $\{x:\dim_x\ge1\}=$ closed points, which
is not that card's statement. Not repaired; the link is harmless and the owner is the fibre-dimension material.

### 2.7 Row 7 — the product of the stalks
$s\mapsto(s_p)$ is injective (axiom 3) and is not the gluing axiom. Witness at `schemes/ringed-spaces.md:26-28`: on
$\AA^1$ the family $g_p=1/x$ for $p\ne0$ and $g_0=0$ is a point of $\prod_p\OO_{\AA^1,p}$ that is not the family of germs
of a section. **Page now: true.**

### 2.8 Row 8 — the functors on sheaves
$f^{-1}\dashv f_*$ and $f^*=\OO_X\tensor_{f^{-1}\OO_Y}f^{-1}(-)$; for abelian sheaves there are $j_!$, $Rf_!$ with
right adjoint $f^!$, $\tensor^L$ and $R\sheafhom$ (`D-SHFSIX`). The coproduct witness: $\bigl(f_*(\oplus_i\mcf_i)\bigr)(\mathrm{pt})=\prod_i\ZZ$ against $\oplus_i\ZZ$.
**Page now (`sheaves/pushforward-and-pullback.md:13,27-29`): true.**

### 2.9 Row 9 — the order and the adjunction
regular ⇒ lci ⇒ Gorenstein ⇒ CM, one-directionally; adjunction is about sheaves on $Y$: Har77 **Prop II.8.20**.
**Page now (`:45-46,52-60`): true**, every adjunction written with `\restrictionof{·}{Y}`; no `\inverseof` remains in it
or in `riemann-hurwitz.md`.

### 2.10 Row 10 — the three toric claims
The quadric cone is $\Spec k[x,y,z]/(xy-z^2)$ with $\Cl=\ZZ/2$ and a ruling that is Weil but not Cartier (Har77
**Example II.6.11.3**; `FE-TORCD` carries $\Cone(e_2,de_1-e_2)$, $\Cl=\ZZ/d$); the classification of smooth complete
toric surfaces is `T-TORSURF`; "every toric variety is a fan" is a category error, and the cuspidal cubic, being
non-normal, is not $X_\Sigma$ (`D-FULSAT`, read: saturation and $\Spec k[S]$ normal).
**Page now (`toric/examples.md:36,40,45,61`): true.**

### 2.11 Row 11 — the three toric-topology claims
1. $\pi_1(X_\Sigma(\CC))\cong N/N_\Sigma$ with $N_\Sigma$ generated by **all** lattice points of $|\Sigma|$; the affine
   quadric cone is $\Cone((0,1),(2,-1))$ and contains $(1,0)=\tfrac12(0,1)+\tfrac12(2,-1)$, so $\pi_1=0$. The page is
   right and the first reader's $\ZZ/2$ is wrong (the owner's ruling on this page stands).
2. The moment map is not a torus bundle: over the relative interior of a $k$-face the preimage is the orbit of complex
   dimension $k$ and the fibre is $(S^1)^k$ (`D-TORMOMENT`).
3. $H^*$ is the Stanley–Reisner ring (`T-TORCOHOM`).
**Page now (`toric/topology.md:31,55,47`): all three right.** The `[@Ful93, §3.2]` and `§4.2]` locators remain
unverified (§9).

### 2.12 Row 12 — the del Pezzo page, and the correction of the counterexample
Both flagged sentences were false and the corrected reason is definitional: for a smooth complete toric surface with
$-K$ Cartier and ample, $P_{-K}=\{m:\inner{m}{u_\rho}\ge-1\ \forall\rho\}$ has its facets on the hyperplanes
$\inner{m}{u_\rho}=-1$ with $u_\rho$ **primitive**, so each facet is at lattice distance one; "distance two" contradicts
the displayed inequalities and no facet passes through the origin because $-K$ is not trivial. Reflexivity is a condition
on the polar (`D-TORREFL`, read: $P^\circ=\{u:\inner{m}{u}\ge-1\ \forall m\in P\}$ and the facet description with $a_F>0$).
**ra84's fourth correction, and the third version's second false witness here.** It wrote that the review's triangle
$\operatorname{Conv}((2,-2),(2,2),(-1,0))$ "has facets at distances $1,1,2$". It has **all three at distance $2$**: the
three edges are $AB:\ x=2$, $BC:\ -2x+3y=2$ and $CA:\ -2x-3y=2$, at lattice distances $2$, $2/\gcd(2,3)=2$ and
$2/\gcd(2,3)=2$. So the triangle exhibits no mixed distances — but it **is** a witness against the universal claim, which
is what the fourth version missed here: the edge $AB$ is $x=2$ with $-2<y<2$, and $(2,0)$ is a lattice point in its
relative interior. A facet at lattice distance two can therefore carry a relative-interior lattice point, and this
triangle proves it. The page's own display is right, and the del Pezzo facets are at distance one for the separate
reason above: $u_\rho$ is primitive and the constant is $-1$.
**Page now (`toric/toric-del-pezzo-surfaces.md:55-59,66`): true**, with $K^2=12-d$ (`PR-FULKSQ`) and the five degrees
$9,8,8,7,6$ recomputed from $3,4,4,5,6$ rays.

### 2.13 Row 13 — rational maps
A birational map from a **normal** variety to a projective variety is undefined only in codimension $\ge2$ (Har77
**Lemma V.5.1**, read), and Vakil **Ex 15.3.B** (read) gives the mechanism at a regular codimension-one point. A blowup is
birational with normal source and target and changes a divisor, so "isomorphism in codimension one" is false. For maps to
$\PP^n$ there is no dominance hypothesis (Har77 **Theorem II.7.1**).
**Repaired here**: `varieties/rational-maps.md:22` now says that dominance is exactly what makes $\varphi^*\colon k(Y)\to
k(X)$ exist, and that it is injective — the object is the induced map, not an inclusion (commit `0204ce05f4`). The
`:48` citation was moved to Proposition II.6.3A by `60a0596190`.

### 2.14 Row 14 — the Segre claim, generally
For all $r,s$: $\psi\colon\PP^r\times\PP^s\to\PP^N$, $N=rs+r+s$, is injective with image $Z(\mathfrak a)$ (Har77
**Exercise I.2.14**, read verbatim). Projectivity of the product follows for every $r,s$.
**Page now (`varieties/projective-varieties.md:41-44`): the general statement.**

### 2.15 Row 15 — dominance, with the finding this row owns
A dominant rational map induces $k(Y)\to k(X)$ contravariantly and the card `D-VARBIRAT` states the correspondence with
finitely generated field extensions (Har77 **Theorem I.4.4**, **Corollary I.4.5**). The page's former "along the
inclusion $k(Y)\into k(X)$" is corrected at `:22` as in §2.13.

## 3. Mathematical defects found and repaired in this session's page read

### 3.1 Projection formula with no hypothesis — `sheaves/pushforward-and-pullback.md:42`
Har77 **Exercise II.5.1(d)** (read: "(Projection Formula). If $f\colon(X,\OO_X)\to(Y,\OO_Y)$ is a morphism of ringed
spaces, if $\mathcal F$ is an $\OO_X$-module, and if $\mathcal E$ is a locally free $\OO_Y$-module **of finite rank**,
then there is a natural isomorphism $f_*(\mathcal F\tensor f^*\mathcal E)\cong f_*(\mathcal F)\tensor\mathcal E$").
Repaired with the hypothesis and the number.

### 3.2 Generating sections ≠ embedding — `sheaves-of-modules/line-bundles.md:21`
Har77 **Proposition II.7.3** (read in full) is about the **span**: $\varphi$ is a closed immersion iff the elements of
$V$ separate points and tangent vectors. Counterexample kept on the page: $\OO(2)$ on $\PP^1$ with $s_0=x^2$, $s_1=y^2$
has no common zero and gives $[x:y]\mapsto[x^2:y^2]$, of degree two, not injective. Repaired.

### 3.3 Toric very ampleness: the shift and the saturation — `toric/polytopes-and-divisors.md:52`
Repaired as §0 item 5: the translated semigroup $\NN(P_D\cap M-m_\sigma)$ inside $S_\sigma=\sigma^\vee\cap M$, with
CLS **Proposition 6.1.10(c)** for the saturation and CLS **(6.1.6)** with **Exercise 6.1.10** for the translation. The
card `PR-TORPOS` carries the same repair in its remark (`9837cb2c28`).

### 3.4 The sheaf condition stated with one axiom — `sheaves/the-sheaf-condition.md:12`
The opening defined a sheaf by locality alone, while `:18-19` separates the two axioms. Repaired to state both, with the
witness for gluing already on the page (the constant presheaf on a two-point discrete space).

### 3.5 The descent convention — `T-FFDESCENT` and `stacks-and-moduli/functors-and-topologies.md:64-65`
Both now use Stacks' convention and Stacks' recovery formula (§0 item 3), fetched live at **Definition 35.3.1, tag
023G**, **Section 35.3, tag 023F** (canonical map $(m\tensor a)\tensor a'\mapsto a\tensor(m\tensor a')$), **Lemma 35.3.7,
tag 039W** and **Proposition 35.3.9, tag 023N**.

### 3.6 Dominance and $\varphi^*$ — `varieties/rational-maps.md:22`
Repaired (§2.13, §2.15).

### 3.7 The normal Cartier-to-Weil injection — `divisors/class-group-and-picard-group.md:17`
Repaired with Har77 **Remark II.6.11.2** (§2.4).

### 3.8 Miracle flatness — `T-MORMIRACLE`, `schemes/dimension.md:53`
Repaired (§0 item 6). `PR-MIRACLEFLAT` (read) states the finite case, whose hypothesis $\dim\OO_{X,x}=\dim\OO_{Y,y}$ is
automatic for a finite morphism because the fibres are finite, and which follows from Har77 **Exercise III.10.9** (read:
"every fibre of $f$ has dimension equal to $\dim X-\dim Y$"). Its citation is therefore correct as the special case, and
its own example (the cusp normalization) is the right witness for the regularity of the target.

### 3.9 Crepant resolutions of terminal singularities — `D-VARCREPANT`
Repaired (§0 item 1), and `FE-207WC` (read) already carries the two resolutions with their two rational maps
$[w:x]$ and $[w:y]$.

### 3.10 Injectivity and finite surjectivity — `PR-RJ3P7:47`
Repaired (§0 item 2).

### 3.11 The triangle — no page carried it
§0 item 4. No page edit: the claim lived only in the third and fourth versions of this record, and the fourth version's
own conclusion ("supports nothing") was false; $(2,0)$ is a relative-interior lattice point of the distance-two edge.

## 4. The cards on which this version's verdicts rest

### 4.1 `T-FFDESCENT` — rewritten in Stacks' convention
Read: **023G** (descent datum and cocycle), **023F** (the canonical map, displayed), **023N**, **039W** (the descended
submodule is $\{n:1\tensor n=\varphi(n\tensor1)\}$). The card now names the canonical map on $(M\tensor_AB)\tensor_AB$ and
puts both sides of the recovery formula in $B\tensor_AN$. The third version's pairing
($C\tensor_{B,p_1}N\cong B\tensor_AN$, $C\tensor_{B,p_2}N\cong N\tensor_AB$, condition $\theta(1\tensor n)=n\tensor1$)
compared elements of two different modules and was satisfied by the canonical datum for every $n$, so it did not recover
$M$. Withdrawn and replaced at `d9477e605a`; `qualc.authoring check T-FFDESCENT` passes.

### 4.2 `PR-RJ3P7` — injectivity qualified
Read: the two theorems against Atiyah–Macdonald **5.10, 5.11, 5.16** — still not on the machine, so those citations remain
unverified at citation level (§9), and the mathematical claims decided here are decided by counterexample. `:51`'s height
statement is the integral case (going down with going up and incomparability), and flat going-down alone is refuted by
$\ZZ[x]\to\ZZ[x,y]$ at $(y)$, repaired at `13f9c3a8eb`. `:47` now separates sufficiency from necessity at `afe86c9d92`.
`qualc.authoring check PR-RJ3P7` passes.

### 4.3 `T-MORMIRACLE` and `PR-MIRACLEFLAT`
Both read; Vakil **26.2.10** and **26.2.11** and Har77 **Ex III.10.9** and Stacks **00R4** read. 26.2.10's hypothesis is
purity of the fibre ring, so the card's theorem is a valid specialization of it; the card's remark that "with regular base
and Cohen--Macaulay source this necessary dimension condition is also sufficient" is the sharp statement, and it is
Stacks **00R4**, which the card's remark now names. Purity is not necessary, and the fourth version's wording to that effect
was wrong. `PR-MIRACLEFLAT`
is the finite case and is correct as stated, with its citation to the exercise that states the fibre-dimension version.
`qualc.authoring check T-MORMIRACLE` passes.

### 4.4 `PR-VGA2L` and Chevalley–Warning — closed
`corpus/theory/Algebraic_Geometry/PR-VGA2L.md:64` now instantiates the theorem (one quadratic form in three variables,
sum of degrees $2<3$, no constant term, the origin a zero) and cites Serre, *A Course in Arithmetic*, Chapter I §2.2,
Theorem 3 (key `Ser73`), at `b9d281ac21`. The previous version's open item is closed; the transclusions at
`curves-and-surfaces/genus.md:24` and `riemann-roch-for-curves.md` now lean on a numbered statement.

### 4.5 `D-TORQD`, `D-FULSAT`, `D-TORREFL`, `PR-TORPOS`
All read. `D-TORQD`'s sections theorem is the standard one; `D-FULSAT`'s saturation criterion ($\Spec k[S]$ normal iff
$S$ saturated in $\ZZ S$) and its $(4,0),(3,1),(1,3),(0,4)$ witness are correct, and its remark that
$S_\sigma=\sigma^\vee\cap M$ is saturated because the defining inequalities are homogeneous is a *statement about the
cone semigroup*, not about a translated polytope semigroup — the two are distinguished on `PR-TORPOS`, which is the
point of §0 item 5. `D-TORREFL`'s polar dual, facet description and 16/5 count are correct.

## 5. Sources read for this version

`tmp/sources/hartshorne-1977-algebraic-geometry.md`: **Ex II.5.1(d)**, **Prop II.7.3**, **Ex II.6.9(a)** (`:4237`),
**Ex III.6.2**, **Ex III.10.9**, **Ex IV.1.8** (`:9290`), **Remark II.6.11.2**, plus the statements re-read for the rows
above (II.1.2, II.6.11,
II.6.11.1A, II.6.15, II.6.16, II.7.6, II.8.20, II.8.22A, III.2.1, III.3.7, III.5.1, Ex III.5.7, V.1.10, V.5.1, IV.2.2,
IV.2.4, IV.3.1, IV.5.1, IV.5.2, IV.5.4, I.2.14, I.3.4, I.4.4, I.4.5, I.6.8, I.7.2, I.7.7).

`tmp/sources/vakil-rising-sea-2025-10-21.md`: **Thm 26.2.10**, **Thm 26.2.11**, **Ex 26.2.G**, **Ex 16.2.G with its
remark**, **Ex 8.3.I**, **Thm 12.4.3**, **Def 7.3.10**, **Lemma 5.3.2**, **Ex 15.3.B**, **Ex 22.4.N**, **Remark 22.4.11**.

`tmp/sources/cox-little-schenck-2011-toric-varieties.md`: **Prop 6.1.10** (with equation (6.1.6) and the proof),
**Ex 6.1.10**, **Thm 6.1.14** and its proof, **Prop 11.4.12**, **Ex 11.4.13**, **Exercise 11.4.13**, **Ex 11.2.7**,
**Prop 2.2.18**, **Def 2.2.17**.

Stacks, fetched live this session: **Definition 35.3.1 (023G)**, **Section 35.3 (023F)** — whose running text carries the
canonical datum $(m\otimes a)\otimes a'\mapsto a\otimes(m\otimes a')$ and Definition 35.3.1 does not —,
**Proposition 35.3.9 (023N)**, **Lemma 35.3.7 (039W)**, **Lemma 10.128.1 (00R4)**; in earlier versions **021M, 021N,
00VH, 00Z4, 0G12**.

**Not on the machine and therefore not read**: Atiyah–Macdonald (**5.10, 5.11, 5.16**), Fulton, Mori's existence theorem,
Godement, Serre's *Local Fields*, and the Godement and Fulton locators named in §9.

## 6. Policy findings on the current blobs

- **Undefined control word**: `schemes/properties-from-the-ring.md:18` wrote `\sp`; the corpus macro is
  `\underlyingspace{…}` and the page now uses it (`17b0fe5161`). Re-checked: no `\sp` remains in the chapter.
- **Surviving positional prose** (PROSE-03): `schemes/what-is-a-scheme.md:80` "the criterion above";
  `curves-and-surfaces/special-divisors-and-the-canonical-map.md:22` "Two consequences organise everything below";
  `morphisms/projective-morphisms.md:50` heading "Consequences used later";
  `stacks-and-moduli/functors-and-topologies.md:20` "in both directions below".
- **Definition-shaped prose with no "Recall"** (DEF-1, DEF-29): `schemes/ringed-spaces.md:16`.
- **CITE-1 unkeyed inline reference**: `toric/affine-computations.md:14`, "[Cox–Little–Schenck, *Toric Varieties*,
  Proposition 1.1.9]" — the number is right (read), the form needs a bibliography key. (`divisors/weil-and-cartier.md:34`
  was named here in the fourth version; on the current blob and at the fourth version's own blob its citation is the keyed
  `[@Har77, …]`, and its defect was the CITE-8 number below.)
- **CITE-8, citations that do not state the claim**: none survives. `divisors/weil-and-cartier.md:34` carried Har77
  **Ex IV.1.8** — the arithmetic-genus formula $p_a$ of a singular curve (`:9290`) — for the Picard sequence that is
  **Ex II.6.9(a)**, "Singular Curves" (`:4237`), whose displayed sequence matches the page's term for term. Repaired in
  this version. `varieties/rational-maps.md:48` was moved to II.6.3A at `60a0596190`; `varieties/projective-varieties.md:18`
  was moved to Ex I.2.2 at `77ed72a62b`.
- **PROVENANCE-01**: `syllabus.md:191` and `:205` open "The numbered items group the topics by subject." and name no
  document; the sections at `:53-105`, `:107-143`, `:145-187` do name theirs. `:207`'s eight Reid locators are unkeyed.
- **PROSE-11 / RESOURCE-11:** `resources.md:58, :87, :148, :194`.
- **SEC-2:** `sheaves/the-sheaf-condition.md:19` (three counterexamples in one sentence) and
  `sheaves/examples-of-sheaves.md:33`.
- **PROSE-05:** `schemes/what-is-a-scheme.md:53` ("the two one expects").

## 7. Carried defects, re-checked

- `cohomology/derived-functors-and-vanishing.md:47,49` — the soft/c-soft acyclicity is cited to Godement, *Topologie
  algébrique et théorie des faisceaux*, Chapitre II, Théorème 4.4.3 and 4.6.2. On a family of supports this is the right
  shape of statement, but **no Godement text is on the machine**, so the two numbers are unverified (§9).
- `curves-and-surfaces/special-divisors-and-the-canonical-map.md:48` — **correct at this tip**: $\ell(K-p-q)=g-2$ and
  $\dim\linearsystem{K-p-q}=g-3$, which is what very ampleness of $K$ requires; the third version's entry claiming
  $g-2$ was misprinted there is withdrawn.
- `cohomology/projective-schemes.md:28` — the semicontinuity theorem is `T-COHBC` (read at its statement headers:
  "Semicontinuity", "Grauert and base change"), so the link is to the right owner.

## 8. Per-page ledger (all 82 pages, at the blobs repaired in this session)

After each path, what was checked on it and the verdict. "Nothing found" means this reading found nothing, not that the
page is certified clean. Every page was read in full this session. A numbered statement named in §5 is one this session
read; a number appearing here and not there is one the page cites, taken from the page and not re-read, and the verdict
on such a page is a verdict on its prose and its internal consistency.

- `cohomology/computing-cohomology.md` — Čech comparison III.4.5, the $\PP^n$ computation III.5.1, the sign and value
  $+1$ of $\delta(z)$ recomputed on the two branch cuts. Nothing found.
- `cohomology/derived-functors-and-vanishing.md` — injectives, flasque acyclicity (Ex II.1.16, Prop III.2.5), affine
  vanishing III.3.5 with the $j_!\ZZ_U$ sharpness example (Ex III.2.1), Grothendieck III.2.7. Godement numbers
  unverified (§7).
- `cohomology/families.md` — the non-flat $\chi$-jump example computed by hand ($\chi=1$ against $\chi=2$). Nothing
  found; the page is a transclusion cluster whose cards were not read (except `T-COHBC`'s headers).
- `cohomology/homological-algebra.md` — the two cokernels (§2.1), enough injectives (Prop III.2.2), no projectives on
  $\PP^1$ (Caution III.6.5.2, Ex III.6.2 read). Nothing found.
- `cohomology/index.md` — the three opening claims follow from `D-DEFEXT`, `D-MODPIC`, `T-D8DMU`, `T-5IOUR`; only
  `T-5IOUR`'s noetherian form was read. Nothing found on the page; the qcqs variant is unread (§9).
- `cohomology/projective-schemes.md` — finiteness/Serre vanishing, the Hilbert-polynomial flatness criterion
  (`T-COHFLATCHI` cited; card not read), the semicontinuity attribution (§7). Nothing found.
- `cohomology/vanishing-and-duality.md` — III.3.7, the dualizing sheaf (III.7.2, III.7.5, III.7.6, III.7.11, III.7.12),
  Kleiman's $\Ext$ form, the trace at $\Spec K$. Nothing found.
- `curves-and-surfaces/blowups-and-the-classification-of-surfaces.md` — Thm V.4.9 (27 lines, only $(-1)$-curves),
  Prop V.3.4. Nothing found.
- `curves-and-surfaces/crepant-resolutions.md` — §2.2; the Du Val contraction and the discrepancy computation
  ($E\cdot K_X=0$, $aE^2=0$) check; the terminal sentence is gone and now lives correctly on `D-VARCREPANT`.
- `curves-and-surfaces/curves-in-projective-space.md` — the degree bounds (Prop IV.3.1/Cor IV.3.2), **the class and the
  degree of $C^\vee$ separated at `:88-91`** ($d(d-1)$ is the class of $C$; the class of $C^\vee$ is $d$ by biduality),
  Castelnuovo IV.6.4, the quadric bidegrees (Ex III.5.6), the genus-5 open case referred to Brill–Noether. Nothing found.
- `curves-and-surfaces/elliptic-curves-over-c.md` — IV.4.15B (the fundamental region as printed), IV.4.16, the
  $j$-invariant normalization, the three standard lattices. Nothing found.
- `curves-and-surfaces/elliptic-curves.md` — the isotrivial twist $ty^2=x^3-x$ and why it is not constant. Nothing found.
- `curves-and-surfaces/embeddings-and-jacobians.md` — II.7.1, the canonical embedding (IV.5.1/IV.5.2), the tangent
  space of $\Jac$ and Serre duality (Remark III.7.12.2), Dolgachev (5.19)/(5.20) with the theta characteristic. Nothing
  found; the Dolgachev numbers are cited from the card and were not re-read this session.
- `curves-and-surfaces/genus.md` — Ex I.7.2 for the Hilbert-polynomial constant term. `PR-VGA2L` transcluded and now
  sourced (§4.4).
- `curves-and-surfaces/index.md` — the syllabus list; each entry names a page. Nothing found.
- `curves-and-surfaces/intersection-theory-on-surfaces.md` — $E^2=-1$, $K_{\tilde X}=\pi^*K_X+E$. Nothing found.
- `curves-and-surfaces/moduli-of-curves.md` — the coarse space and the $j$-line. Nothing found.
- `curves-and-surfaces/riemann-hurwitz.md` — §2.3, Prop IV.2.2 tame/wild and the inseparable case (Ex IV.2.5.1–4).
  The IV.2.4 over-citation remains (§2.3).
- `curves-and-surfaces/riemann-roch-for-curves.md` — IV.1.3, $\deg K=2g-2$, Clifford (IV.5.4), the canonical map.
  Nothing found.
- `curves-and-surfaces/special-divisors-and-the-canonical-map.md` — §7's re-check: the separation count at `:48` is
  correct; Clifford's equality cases; the Brill–Noether gonality bound. Nothing found.
- `divisors/class-group-and-picard-group.md` — §2.4; **repaired** with Remark II.6.11.2.
- `divisors/index.md` — the syllabus list and the nodal/cuspidal $\Pic^0$. Nothing found.
- `divisors/line-bundles-and-linear-systems.md` — IV.3.1 separation criteria, the base-locus description. Nothing found.
- `divisors/positivity.md` — Theorem II.7.6 with its noetherian hypothesis, the cohomological criterion under
  properness, Nakai–Moishezon, Kleiman. Nothing found.
- `divisors/weil-and-cartier.md` — the excision sequence II.6.5 and $\Cl(\PP^n\sm V(f))=\ZZ/d$. **Ex IV.1.8 for the
  Picard sequence is wrong** and the right number is not located (§2.4, §9).
- `varieties/affine-or-projective.md` — projective ⇒ complete, complete affine ⇒ point, Serre's criterion. Nothing found.
- `varieties/blowups.md` — V.3.4, $K^2$ drop by one, $p_g$ birational invariance. Nothing found.
- `varieties/canonical-class.md` — the determinant, II.8.20, the Euler sequence, the trichotomy and its failure under
  blowup, Reid C.3.1/C.3.2 with "minimal" against "$K$ nef". Nothing found.
- `varieties/dimension-and-degree.md` — I.1.7, I.1.8A, Bézout I.7.7/I.7.8, the Segre degree (Ex I.7.1), $p_a$ from
  $P_X(0)$ (Ex I.7.2, Ex III.5.3). Nothing found.
- `varieties/index.md` — the syllabus list. Nothing found.
- `varieties/morphisms-of-varieties.md` — the anti-equivalence, the Segre and Veronese images. Nothing found.
- `varieties/nonsingular-curves.md` — DVRs, Prop I.6.8, II.6.3A. Nothing found.
- `varieties/projective-varieties.md` — Ex I.2.2/I.2.4 for the empty zero set and the correspondence, I.2.10 for the
  cone, Ex I.2.14 for Segre. Nothing found.
- `varieties/rational-maps.md` — §2.13, §2.15; **repaired** to $\varphi^*$.
- `varieties/regular-functions.md` — I.3.4, Ex I.3.6. Nothing found.
- `varieties/smooth-and-singular.md` — the Jacobian criterion and the Euler relation, and its failure when $\deg f$ is
  not invertible. Nothing found.
- `varieties/the-dictionary.md` — the radical-ideal bijection and the $(x)$/$(x^2)$ example. Nothing found.
- `index.md` — the topic list. Nothing found.
- `morphisms/classes-of-morphism.md` — Vakil 8.3.I (finite to affine is projective), the implication chain, the
  non-closed-immersion homeomorphism example. Nothing found.
- `morphisms/fibres-and-images.md` — fibre dimension, Zariski's main theorem, Stein factorization; the node
  normalization example computed. Nothing found.
- `morphisms/finite-and-flat.md` — going up and going down; the $\ZZ\to\ZZ/2$ example for surjectivity; III.9.7 for
  flatness over a regular curve. **Atiyah–Macdonald unverified** (§9).
- `morphisms/index.md` — the syllabus list and `P-AGH242AGREEDENSE` with its two witnesses. Nothing found.
- `morphisms/inseparable-morphisms-and-luroth.md` — Prop IV.2.5 and Ex IV.2.5.1's zero map $F^*\Omega\to\Omega$. Nothing
  found.
- `morphisms/projective-morphisms.md` — **§2.5**: the four ampleness clauses with their hypotheses, Ex III.5.7(a) and
  (d), Vakil 16.2.G with the remark that removes the properness allegation, II.4.9 and the non-projective threefold.
  Nothing to repair.
- `morphisms/separated-and-proper.md` — the diagonal, II.4.9, I.3.4. Nothing found; `D-8XX95` not read.
- `morphisms/smooth-unramified-etale.md` — the étale/smooth/unramified dictionary. Transclusion-only for the
  substantive content; cards not read.
- `schemes/dimension.md` — §2.6; **repaired** at `:53`.
- `schemes/fibre-products-and-base-change.md` — the $\FF_9$ fibre and $\CC\tensor_\RR\CC$ computed by hand. Nothing
  found.
- `schemes/index.md` — the syllabus list. Nothing found.
- `schemes/normalization.md` — II.8.22A, I.3.9A, AM 5.10/5.11 (unverified), II.6.3A. Nothing found beyond §9.
- `schemes/proj-and-gluing.md` — II.2.5 charts, Ex II.3.12, II.4.9 with Cor II.4.8(c). Nothing found.
- `schemes/properties-from-the-ring.md` — Ex II.2.13, Ex II.2.9, Ex II.5.7(a). **`\sp` remains** (§6).
- `schemes/ringed-spaces.md` — §2.7; Ex II.2.3.2 for the non-local morphism; the injectivity-not-gluing distinction.
  Nothing found but the DEF-1 prose (§6).
- `schemes/subschemes-and-points.md` — open against closed subschemes, the reduced induced structure (Ex II.3.2.6), the
  scheme-theoretic image (Ex II.3.11, Vakil §9.4), Chevalley (Ex II.3.19), the double point. Nothing found.
- `schemes/what-is-a-scheme.md` — Prop II.2.3, Ex II.2.4, Prop II.2.6, III.3.7, Vakil Lemma 5.3.2, the
  $k[\eps]/\eps^2$ and $\Spec\ZZ$ examples. Nothing found but the prose items of §6.
- `sheaves-of-modules/differentials.md` — II.8.17, the conormal and relative sequences, the Euler sequence. Nothing
  found.
- `sheaves-of-modules/index.md` — the syllabus list. Nothing found.
- `sheaves-of-modules/line-bundles.md` — §3.2; **repaired** with Prop II.7.3 and the $\OO(2)$ counterexample.
- `sheaves-of-modules/operations.md` — $f^*$ right exact, the $\ZZ\xrightarrow{p}\ZZ$ pullback to $\FF_p$, ideal sheaves.
  Nothing found.
- `sheaves-of-modules/projective-sheaves.md` — II.5.11, Ex II.5.9, II.5.15, Ex II.7.5. Nothing found.
- `sheaves-of-modules/quasicoherence.md` — $\widetilde M$, the twists, resolutions by twists. Nothing found.
- `sheaves-of-modules/tangent-normal-and-canonical-sheaves.md` — II.8.15, II.8.12, the CM/Gorenstein/lci order, II.8.20
  with `\restrictionof{·}{Y}` throughout. Nothing found.
- `sheaves/examples-of-sheaves.md` — constant/locally constant, the skyscraper's support $\closure{\{p\}}$, the
  exponential. Nothing found; the SEC-2 item at `:33` stands (§6).
- `sheaves/index.md` — the syllabus list and the exponential example. Nothing found.
- `sheaves/morphisms-of-sheaves.md` — kernel/image/cokernel, the stalk criterion, $\sheafhom$, the étale space, the
  non-splitting of $\exp$. Nothing found.
- `sheaves/pushforward-and-pullback.md` — §2.8; **repaired** at `:42` with Ex II.5.1(d).
- `sheaves/stalks-and-exactness.md` — support not closed for $j_!$, closed for coherent on noetherian. Nothing found.
- `sheaves/the-sheaf-condition.md` — §3.4; **repaired** at `:12`.
- `stacks-and-moduli/functors-and-topologies.md` — the site and topology (Stacks 00VH/00Z4), the fppf comparison
  (021M/021N), representability and the open-subfunctor gluing, torsors; **the descent passage rewritten** (§3.5).
- `stacks-and-moduli/index.md` — two entries, each naming a page. Nothing found.
- `stacks-and-moduli/spaces-and-stacks.md` — the Hilbert functor (Stacks 99.9.4/0D01, III.9.9), coarse against fine
  moduli with the twist, algebraic spaces (Stacks 65.10.5/02WW), stacks and automorphisms. Nothing found.
- `syllabus.md` — six sections; the source lines and reading pointers are present for three, absent for two (§6); `:37`'s
  Berkeley document not fetched.
- `toric/affine-computations.md` — CLS Prop 1.1.9 read, the determinant-7 cone, the minimal resolution of the quadric
  cone; the CLS reference is unkeyed (§6).
- `toric/criteria.md` — the smooth/complete criteria, $K_{U_\sigma}$ Cartier. Nothing found.
- `toric/examples.md` — §2.10; the four curve examples and the determinant-7 resolution recomputed. Nothing found.
- `toric/index.md` — the syllabus list; Fulton §1–4 locator unverified (§9).
- `toric/polytopes-and-divisors.md` — §3.3; **repaired** at `:52`.
- `toric/surfaces-and-morphisms.md` — the limit criterion for completeness, the classification of smooth complete
  toric surfaces, star subdivision's four effects; `FE-207WC` read and correct. Nothing found.
- `toric/the-dictionary.md` — the face/dual reversal, orbit closures as toric varieties, the five-row table. Nothing
  found.
- `toric/topology.md` — §2.11; $\pi_1=N/N_\Sigma$, the Euler characteristic as a cone count, Stanley–Reisner, the
  moment map with the $(S^1)^k$ fibre. Fulton §3.2 and §4.2 unverified (§9).
- `toric/toric-del-pezzo-surfaces.md` — §2.12; the five surfaces, $K^2=12-d$, degrees $9,8,8,7,6$, the fourth-blowup
  obstruction. Nothing found.

## 9. What is undecided, exactly

1. **Atiyah–Macdonald 5.10, 5.11, 5.16** — no text on the machine. The pages that quote them
   (`morphisms/finite-and-flat.md:23,25,32`, `schemes/normalization.md:28`, `PR-RJ3P7`'s two theorems) are **undecided at
   citation level**; the height claim this record decides is decided by the $\ZZ[x]\to\ZZ[x,y]$ counterexample, not by
   the book.
2. **Fulton's locators** — `toric/topology.md:29` (§3.2), `:55` (§4.2), `toric/index.md:16`, `syllabus.md:187`. No text.
3. **Godement, Chapitre II, Théorème 4.4.3 and 4.6.2** — `cohomology/derived-functors-and-vanishing.md:47,49`. No text.
4. **`divisors/weil-and-cartier.md:34` — closed.** The Picard sequence is right; its cited number (Ex IV.1.8) was wrong and
   is now **Ex II.6.9(a)**, read at `:4237` in the retained text and quoted in §5. Nothing is owed on this item.
5. **The transcluded cards this session did not open.** The fourth version's list stands except for the five cards of §9.1,
   which are now read; a count is still not a list, so the remainder is named again here: `T-SRFZMT`, `T-SRFCAST`,
   `FE-SRFFERMATQUARTIC`, `T-TORDIV`, `PR-TORMOR`, `T-FULBETTI`, `T-TORCOHOM`, `D-TORMOMENT`, `D-FULSTAR`, `PR-O8V3I`,
   `PR-FULCRIT`, `PR-FULKSQ`, `D-CRVBRILLNOETHER`, `D-8XX95`, `D-VARBIRAT`'s siblings in the toric and surface chapters,
   `T-CRVMINMOD`, `D-SCHCMGOR`, `T-EFRAPL`/`T-DEFRAPL`, `D-MODAMPLE`, `D-2049GP`, and the remaining ~285. The third
   version's §5 records sixteen of these as read in *that* session (`D-SHFSIX`, `D-SCHCMGOR`, `D-VARBIRAT`, `T-CRVMINMOD`,
   `T-BIRINV`, `FE-TORCD`, `T-TORSURF`, `D-FULSAT`, `PR-TORMOR`, `T-FULBETTI`, `D-TORMOMENT`, `T-TORCOHOM`,
   `D-FULSTAR`, `PR-O8V3I`, `D-TORREFL`, `PR-FULCRIT`, `PR-FULKSQ`); those readings are **carried here, not re-verified**,
   and the verdicts in §2 that rest on them inherit that status. What this session re-read in full is the ten cards of
   §1 and the five of §9.1.
6. **`syllabus.md:37`'s Berkeley document** — not fetched.
7. **Mori's existence theorem** for crepant resolutions of terminal Gorenstein threefolds — no retained text, and the
   verdicts here do not use it: §0 item 1 rests on CLS Proposition 11.4.12 and Examples 11.4.13 with `FE-207WC`.

### 9.1 The fifth version's read batch: five transclusions, decided

Each card was opened whole and its numbered citations checked against the retained text or the fetched tag. "MET" here
means the mathematics of the card was checked and corrects nothing; it is not a certification of every sentence, and the
four cards not repaired carry no claim that they are free of defects this reading did not look for.

- **`D-VARBIRAT` — corrected.** The rational-map and birational definitions were cited as `[@Har77, Definition I.4]`
  twice. Hartshorne's I.4 has **two unnumbered definitions** (`:1025`, `:1029` of the retained text: "Definition. Let X,Y
  be varieties. A rational map …" and "Definition. A birational map …"), so the number does not exist; both now read
  `[@Har77, §I.4]`, the section form the card already used elsewhere. Theorem **I.4.4** (`:1046`) is exactly the displayed
  bijection between dominant rational maps $X\dashrightarrow Y$ and $k$-algebra homomorphisms $k(Y)\to k(X)$, with the
  arrow-reversing equivalence to finitely generated field extensions, and Corollary **I.4.5** (`:1059`) is
  (i) birational $\Leftrightarrow$ (ii) isomorphic open subsets $\Leftrightarrow$ (iii) $K(X)\cong K(Y)$; the card's
  theorem states (i)$\Leftrightarrow$(iii). **Second correction:** the codimension-two indeterminacy proposition's proof
  cited §I.4, which contains no such statement; it now cites Vakil **Exercise 15.3.B** (`:10678`: "rational maps from
  Noetherian $k$-schemes to projective $k$-schemes can be extended over regular codimension 1 sets"), the iteration over
  codimension-one points being what gives codimension $\ge2$, and the same exercise is what `varieties/rational-maps.md:21`
  already uses.
- **`T-BIRINV` — MET.** The theorem's statement, $\mathrm H^0(X,(\Omega^p_{X/k})^{\otimes m})\cong
  \mathrm H^0(X',(\Omega^p_{X'/k})^{\otimes m})$ for birational smooth projective $X,X'$ in any characteristic, is true:
  $(\Omega^p)^{\otimes m}$ is locally free, hence reflexive, so sections extend over a complement of codimension $\ge2$
  (algebraic Hartogs on the smooth, hence normal, variety). The citations are to the **method**, and the card says so:
  Har77 **Theorem II.8.19** (`:5031`) is $p_g(X)=p_g(X')$ and its proof is that extension argument, and Har77 **Exercise
  II.8.8** (`:5281`) is "Using the method of (8.19), show that $P_n$ and $h^{q,0}$ are birational invariants". Neither
  numbered statement covers the mixed case $p<n$, $m>1$; the card's own sentence "following the method of" is therefore
  the correct description and is not a false attribution. `P-AGH288PLURIGENUS` is named as where the inverse pullbacks are
  constructed.
- **`D-L6ERW` — MET.** Har77 **Proposition II.5.13** (`:3438`) is
  $\Gamma_*(\OO_X)\cong S$ for $X=\PP^r_A$; since $S$ is concentrated in non-negative degrees, that is simultaneously
  $h^0(\PP^1,\OO(m))=m+1$ for $m\ge0$ and $0$ for $m<0$, which is what the card's example uses it for. The
  $\deg(X)/d!$ reading of the leading coefficient is [@Har77, §I.7], a section locator, correctly so, and the twisted
  cubic's $P(r)=3r+1$ follows from $h^0(\PP^1,\OO(3r))=3r+1$.
- **`T-5IOUR` — MET for the theorem; the remark's qcqs form is unverified.** Har77 **Theorem III.3.7** (`:6039`,
  "Serre [5]") is the three-way equivalence for a **noetherian** scheme, verbatim as the card states it; **Theorem
  III.3.5** (`:6029`) is $H^i(\Spec A,\mcf)=0$ for quasi-coherent $\mcf$ and $i>0$ over a noetherian $A$, which is
  (i)$\Rightarrow$(ii); and **II.2.17** (`:2532`, "A Criterion for Affineness") is the affineness criterion the proof
  invokes. The remark's quasicompact quasi-separated form was checked against **no** retained numbered statement this
  session and is recorded as unverified, not as false.
- **`D-SHFSIX` — statements MET, and it cites nothing.** The six operations, $Rf_!=Rf_*$ for proper $f$, $j^!=j^{-1}$
  for an open inclusion, proper base change, the projection formula, $\omega_X=a^!\ZZ$ with $\omega_X\cong\mathrm{or}_X[n]$
  on a topological $n$-manifold, and $i^!=i^{-1}R\Gamma_Z$ for a closed inclusion are all standard and correctly stated,
  as is the Poincaré-duality consequence in the remark. The card carries **no citation at all**, which `QUAL-10` asks for
  on a theory card; there is no Iversen or Kashiwara–Schapira text on this machine, so the gap is recorded and no number
  is invented for it.

**The remaining unread set, measured at `2136132338`.** The 82 pages of `wiki/algebraic-geometry/` transclude **327**
distinct card ids (`rg -o '\[\[[A-Z][A-Z0-9-]{2,}(\|[^\]]*)?\]\]'` over the 82 files, the pipe target stripped, `sort -u`);
the page count is still 82 files. All fifteen cards this record has read in full — the ten of §1 and the five of §9.1 — are
among those 327, so **312 transclusions were unread at that commit** — §9.3 reads four more and states the file's current
figure, which is the one to use. That is a count of cards, not of filesystem paths, and the
reading still owed is one card at a time; the list of what is left is §9 item 5 plus the archive of card ids on disk, not
a number that stands in for it.

### 9.2 The `T-JLB44J` / Exercise III.1.6-to-III.1.8 item does not exist on `main`

The fifth version's brief asked for a repair "in the owning `T-JLB44J` material", correcting a Hartshorne locator from
Exercise III.1.6 to Exercise III.1.8. Neither the card nor either number exists here, and the check below is exhaustive
rather than a failed filename guess.

- **No card id `T-JLB44J`.** `rg -n "JLB44J"` over `corpus/`, `wiki/`, `results/`, `sources/` and `tools/` returns
  nothing, no file under `corpus/theory/Algebraic_Geometry/` carries the name, `git log --all -S"JLB44J"` returns no
  commit on any ref, and the issue #189 body and its (empty) comment list name it nowhere.
- **No locator `III.1.6` or `III.1.8` anywhere in the repository.** `rg -n "III\.1\.[0-9]+"` over the whole tree returns
  only III.1.1A, III.1.2A, III.1.3A, III.1.17 and III.1.4, every one of them a real numbered result of Hartshorne §III.1
  which the cards cite for what it says.
- **Hartshorne Chapter III §1 prints no exercises.** `tmp/sources/hartshorne-1977-algebraic-geometry.md` runs §III.1 from
  `:5632` to `:5776` ("## 2 Cohomology of Sheaves") with no exercise block; the chapter's exercises begin at `:5930` with
  **2.1**. So "Exercise III.1.6" and "Exercise III.1.8" are not Hartshorne exercise numbers, and a swap between them
  cannot be made. Two nearby numbers were checked and stand: **II.1.8** is the left exactness of $\Gamma(U,-)$, cited at
  `corpus/theory/Algebraic_Geometry/PR-C9ZEK.md:40`, and **III.10.9** is the fibre-dimension criterion `PR-MIRACLEFLAT`
  uses.

### 9.3 The batch after the fifth version: four transclusions read, three closed items re-read at the statement

The three findings the fifth version closed were re-read here at the statement and stand. `divisors/weil-and-cartier.md:34`
now names **Exercise II.6.9(a)**, whose display at `:4237` is
$0\to\bigoplus_{P\in X}\widetilde{\mathcal O}_P^*/\mathcal O_P^*\to\Pic X\to\Pic\widetilde X\to0$ — and Exercise
**IV.1.8** (`:9290`) is "$p_a$ of a Singular Curve", so the earlier number was wrong and not merely unlocatable.
`stacks-and-moduli/functors-and-topologies.md:64` attaches the canonical instance to **Section 35.3, tag 023F**, whose
running text is where $(m\otimes a)\otimes a'\mapsto a\otimes(m\otimes a')$ is displayed, immediately before Lemma
35.3.3; Definition 35.3.1 is **tag 023G**, and the tags of the 023F page run 023G, 023H, …, 023N, 039W in document
order, so the two numbers are not interchangeable. The facet triangle of §0 item 4 is a witness: $(2,0)$ is a lattice
point in the relative interior of the edge $x=2$, $-2<y<2$, which is at lattice distance two.

Of the cards §9 names as unread, four were opened whole. "Repaired" means the defect was in the locator and the
mathematics stands; it is not a certification that the rest of the card is free of defects.

- **`T-SRFZMT` — repaired; the card carried no numbered locator at all**, which is the `QUAL-10` defect for a theory
  card. Its three theorems have Hartshorne numbers: connected fibres is **Corollary III.11.4** (`:8572`, "Zariski's Main
  Theorem", printed for a birational **projective** morphism of noetherian integral schemes to a normal base, so the
  card's "proper" is the Stein-factorization form its own remark argues, and the card now says which is which); the
  single-blowup step and the count of factors are **Proposition V.5.3** and **Corollary V.5.4**; and the factorization of
  a birational transformation of surfaces into monoidal transformations and their inverses is **Theorem V.5.5**. The
  higher-dimensional characteristic-zero case of elimination of indeterminacy is Hironaka's and has **no retained
  numbered statement**; the card now records that rather than borrowing a number for it.
- **`T-SRFCAST` — repaired at the citation.** Its only locator, `[@Har77, Theorem V.5.7]`, was attached to the final
  clause about projectivity, while the criterion itself — the card's actual content — carried none. V.5.7 prints the
  criterion for a nonsingular projective surface and one direction only (a curve with $E\cong\PP^1$, $E^2=-1$ is the
  exceptional curve of a monoidal transformation); the converse is Hartshorne's own `(V, 3.1)`. The card's wider
  hypotheses, $X$ not assumed projective and $E$ only an integral curve proper over $k$, are now labelled as the card's
  form of the statement, not as V.5.7's.
- **`T-TORDIV` — repaired at the locator.** The card's only citation had been `[@Ful93]`, a section of a text that is
  not on this machine (§9 item 2). The class-group sequence with $m\mapsto\operatorname{div}(\chi^m)$ is
  Cox–Little–Schenck, *Toric Varieties*, **Theorem 4.1.3**, and the Cartier condition that cuts the second
  sequence out of the first is **Theorem 4.2.8** — both read in the retained text, and now cited beside the Fulton
  section rather than replacing it.
- **`PR-TORMOR` — repaired at the locator, same reason.** The two section locators into Fulton are backed by numbered
  statements of a retained text: $\pi_1(X_\Sigma(\CC))\cong N/N_\Sigma$ with $N_\Sigma$ generated by $|\Sigma|\cap N$ is
  **Theorem 12.1.10**, and $e(X_\Sigma)=|\Sigma(n)|$ is **Theorem 12.3.9**, which carries no completeness hypothesis —
  a fact the card's own hypothesis did not need but did not state.

**`D-VARCREPANT`, the card-level citation defect the review names — repaired.** Example **11.4.13** (`:22503`) is the
parity-lattice cone of Example 11.2.7, not $\{xy-zw=0\}$, so the card's chain did not reach the conifold at all. The
conifold identification is Example **11.2.12** (`:21780`, $U_\sigma$ for
$\sigma=\operatorname{Cone}(e_1,e_2,e_1+e_3,e_2+e_3)$), its crepant resolution Example **11.2.6** (`:21672`), and the two
small resolutions with $\PP^1$ exceptional loci, related by Atiyah's flop, Example **11.1.12** (`:21552`). The
positive-discrepancy claim was attributed to Proposition 11.4.12, which is instead the lattice-point criterion; it is
Definition **11.4.9(a)** together with the paragraph after it, and terminality of the conifold now comes from
**Proposition 11.4.12(b)(i)** with the polytope computation shown.

With these four, nineteen of the 327 transclusions are read and **308 remain**; §9 item 5's list is otherwise unchanged,
and the reading owed is still one card at a time.

### 9.4 The batch after the sixth version: ten transclusions, nine repaired and one MET

The ten cards below were opened whole at `a6d7a2e75b` and each one read against the numbered statements it cites.
"Repaired" means the defect was a citation or a hypothesis and the mathematics stands; it is not a certification that the
rest of the card is free of defects this reading did not look for. `D-CRVBRILLNOETHER` is **MET** and unchanged.
This is a reading batch of the record and **not** a completion claim for the 82 pages: their reading is the sixth
version's (§1, §8), the page count and the transclusion count are re-measured below, and #189's 82-page condition stands
as it did.

| Card | Source statement read | What was read or repaired | SHA |
|---|---|---|---|
| `FE-SRFFERMATQUARTIC` | Har77 **Prop. II.8.20**, **Thm III.5.1(b)**, **Cor. III.7.7**, **Ex. A.4.1.2**, **Prop. V.1.5** | No numbered citation anywhere on the card; all five now cited. The count of 48 lines was asserted, now proved on the card. Rank-20 span verified by exact arithmetic | `ce0c91629c` |
| `T-FULBETTI` | CLS **Thm 12.3.12**, **Thm 12.3.11**, **Thm 12.3.2**, **Thm 4.1.3** | Coefficients: the two source theorems are over $\QQ$, the card's $\beta_j$ are $\ZZ$-ranks; the integer degeneration at $E_2$ (Franz, recorded in the same section) is now named. The uncited special-cases theorem now cites 12.3.2 and 4.1.3 | `d06fa75ff6` |
| `T-TORCOHOM` | CLS **Thm 12.4.4** (Jurkiewicz--Danilov), **Thm 12.5.3**, (12.4.2)--(12.4.3) | The theorem carried no number; it is 12.4.4, and the Chow comparison is 12.5.3 over $\QQ$. The $\FF_a$ non-cones are the diagonal pairs, not "the opposite pairs" when $a\neq0$ | `23146a24cb` |
| `D-TORMOMENT` | CLS **Thm 12.2.5**, **Prop. 12.2.3**, **Ex. 12.2.8**, **Thm 5.1.11** | Fulton §4.2 unverifiable (no copy on the machine); the numbered backing is CLS §12.2, with 12.2.8 carrying Theorem 12.2.5 to the symplectic $\mu$ the card writes. The Kähler identification is recorded as uncited, not given a number | `ca351c6711` |
| `D-FULSTAR` | CLS **Prop. 3.2.7**, **Ex. 3.2.7**, **Thm 3.2.6(b),(d)**, **Def. 3.3.13**, **Prop. 3.3.15**, §8.0 | The proposition and the remark carried no citation; the orbit closure is 3.2.7, the star a fan by Exercise 3.2.7, the subdivision 3.3.15, the intersections 3.2.6(d) | `15c00208d5` |
| `PR-O8V3I` | CLS **Thm 3.2.6**, **Prop. 3.2.2**, **Thm 4.1.3** | No citation on either block; all three statements cited. The $\ZZ/d$ cokernel is now computed on the ray matrix $[\,0\ d;\ 1\ -1\,]$ | `f531736586` |
| `PR-FULCRIT` | CLS **Thm 3.1.5**, **Def. 1.2.16**, **Thm 1.3.12**, **Thm 3.1.19**, **Prop. 4.2.7**, **Thm 3.4.6**, **Prop. 3.1.6**, **Thm 6.1.7**, **Thm 6.1.14**, **Def. 6.1.12**, **Prop. 6.1.10**, **Def. 2.2.17**, **Cor. 2.2.13**, **Prop. 2.2.18**, **Thm 6.1.15**, **Def. 8.3.1**, **Thm 8.3.4**; Har77 **Thm V.1.10** | Every row of both tables now carries its number. "Ample $\Rightarrow$ very ample on a smooth complete toric variety" is **6.1.15** exactly. $\FF_m$ is taken with $m\ge0$, where $D_2$ is the negative section | `7cc59e021f` |
| `PR-FULKSQ` | CLS **Thm 8.2.3**, **Lemma 10.4.1**, **Thm 10.4.4**, **Thm 10.4.3**; Har77 **Ex. A.4.1.2** | The proof is the card's own and correct; it now cites $K_X=-\sum D_\rho$ (8.2.3), the self-intersections and adjacencies (10.4.4 with 10.4.1), and the classification (10.4.3). The `[@Ful93, §2.5]` hung on the sentence saying the sum rule needs no Noether formula is gone; Noether's formula is Har77 A.4.1.2 | `a8c88f3772` |
| `D-CRVBRILLNOETHER` | no retained source states the theorem | **MET**, unchanged: $\rho=g-(r+1)(g-d+r)$, the hypothesis $g-d+r\ge0$, the degeneracy-locus description and the three attributions are correct, and the example's $2d-g-2$ and $\lceil(g+2)/2\rceil=\lfloor(g+3)/2\rfloor$ check. The remark's claim that neither ACGH nor Griffiths--Harris is retained was verified by absence | — |
| `D-8XX95` | Stacks **Lemma 26.22.1** (01KZ), **Lemma 26.22.2** (01L0), **Lemma 29.43.1** (0BX5), **Lemma 32.15.2** (0207), **Lemma 32.15.3** (0208); Har77 **Ex. II.4.6.1**, **Ex. II.4.11**, §II.4 | **Hypothesis repaired**: the DVR criterion constrains the *base*, not the source. "Of finite type with $X$ Noetherian" is replaced by "$Y$ locally Noetherian and $f$ of finite type", the printed hypothesis of tags 0207 and 0208; Har77 II.4.11 is the Noetherian-schemes form | `a6d7a2e75b` |

**The decisions of this batch, item by item.**

1. **`FE-SRFFERMATQUARTIC`.** (i) The card carried no numbered citation at all — the `QUAL-10` defect for an example that
   computes. $\omega_X=\OO_X$ now cites Har77 **Proposition II.8.20** (for a divisor $Y$: $\omega_Y\cong\omega_X\otimes
   \mathcal L\otimes\OO_Y$) with $\omega_{\PP^3}=\OO(-4)$; $H^1(X,\OO_X)=0$ cites **Theorem III.5.1(b)**, which gives both
   $H^1(\OO_{\PP^3})=0$ and $H^2(\OO_{\PP^3}(-4))=0$; $h^2=h^0(\omega_X)$ is **Corollary III.7.7**; Noether's formula is
   **Example A.4.1.2**, $\chi(\OO_X)=\tfrac1{12}(K_X^2+c_2)$; $L^2=-2$ is **Proposition V.1.5**. (ii) "Exactly $48$" was an
   assertion with no source on the machine, so the card now proves it: two of the four restrictions $\ell_i=
   \restrictionof{x_i}{L}$ are independent, and after a permutation of coordinates — $X$ is $S_4$-invariant and a
   permutation permutes the three families — one solves $s^4+t^4+(as+bt)^4+(cs+dt)^4\equiv0$, whose five coefficient
   equations have exactly the solutions $(a,0,0,d)$ and $(0,b,c,0)$ with the two nonzero entries fourth roots of $-1$;
   sixteen each, plus the displayed family, is the $48$. (iii) "The lines span a sublattice of rank $20$" was verified
   here by exact arithmetic in $\QQ(\zeta)$, $\zeta^4=-1$: the $48\times48$ matrix with diagonal $-2$ and $1$ exactly at
   the pairs that meet — fourteen partners per line — has rank $20$ over $\QQ$, and divisor classes lie in $H^{1,1}$ of
   dimension $20$, so $\rho=20$. The check is `.scratch-189/fermat.py`, not committed; the first run of it was wrong
   (the root list silently held two roots twice, and the reported rank was $48$), which is why the card's claim had been
   worth checking rather than quoting.
2. **`T-FULBETTI`.** The formula is CLS **Theorem 12.3.12** verbatim, including $b_{2k}=b_{2n-2k}$, and the odd vanishing
   is **Theorem 12.3.11(a)**; both are stated with $\QQ$-coefficients, while the card's $\beta_j$ are $\ZZ$-ranks. The
   card now says so and names what closes the gap: the spectral sequence (12.3.11) degenerates at $E_2$ with integer
   coefficients for smooth $X_\Sigma$ (Franz, recorded in the same section immediately before Theorem 12.3.11), so
   $H^\bullet(X_\Sigma(\CC),\ZZ)$ is torsion-free, even, and $\beta_{2k}=b_{2k}$. The uncited second theorem gained
   **Theorem 12.3.2** for $\Pic\cong H^2$ — read at its statement, whose hypothesis is that every maximal cone be
   $n$-dimensional — and **Theorem 4.1.3** for $\beta_2=\size\Sigma(1)-n$. The two worked cases were recomputed.
3. **`T-TORCOHOM`.** The card's "Jurkiewicz--Danilov" theorem carried no number: it is CLS **Theorem 12.4.4**, for smooth
   complete $X_\Sigma$ and over $\ZZ$, induced by $x_i\mapsto[D_{\rho_i}]$, with the two ideals displayed in (12.4.2) and
   (12.4.3); the Chow comparison is **Theorem 12.5.3**, $\QQ$-coefficients complete simplicial. One mathematical error:
   for $\FF_a$ the pairs $\{\rho_1,\rho_3\}$ and $\{\rho_2,\rho_4\}$ are **not** opposite when $a\ne0$ — $\rho_3$ is
   $-e_1+ae_2$ — they are the non-adjacent pairs, which is what makes $x_1x_3=x_2x_4=0$. The ring
   $\ZZ[f,s]/(f^2,s^2-asf)$ and $D_4^2=a$, $D_2^2=-a$ were recomputed and stand.
4. **`D-TORMOMENT`.** The only locator was `[@Ful93, §4.2]`, a section of a text that is not on this machine (§9 item 2).
   The numbered backing is CLS §12.2: **Theorem 12.2.5** (the restricted algebraic moment map is a homeomorphism onto $P$,
   carrying each torus orbit bijectively to the relative interior of the corresponding face), **Proposition 12.2.3(a)**
   for $X_\Sigma/S_N\cong(X_\Sigma)_{S^0}$ and **(b)** for the fibre $S_{N(\sigma)}$ of dimension $n-\dim\sigma=k$ over a
   point of the interior of a $k$-face. Both are stated for the algebraic moment map; **Exercise 12.2.8** is what carries
   Theorem 12.2.5 to the symplectic $\mu$ the card writes, and the card now says which is which. The symplectic-reduction
   paragraph of the remark cites the algebraic Cox quotient **Theorem 5.1.11** and records that the Kähler identification
   itself has no numbered statement in the retained texts.
5. **`D-FULSTAR`.** Neither block carried a citation. $V(\tau)=X_{\Star(\tau)}$ is CLS **Proposition 3.2.7**; that
   $\Star(\tau)$ is a fan is **Exercise 3.2.7**; $\dim V(\tau)=n-\dim\tau$ is **Theorem 3.2.6(b)**; the star subdivision is
   **Definition 3.3.13** with **Proposition 3.3.15**; $D_{\rho_1}\cap\cdots\cap D_{\rho_k}=V(\tau)$ or empty is
   **Theorem 3.2.6(d)**; and the simple-normal-crossing statement is CLS **§8.0**, which says in as many words that
   $D=\sum_\rho D_\rho$ is a simple normal crossing divisor on any smooth toric variety.
6. **`PR-O8V3I`.** No citation on either block. **Theorem 3.2.6** (a), (b), (d) for the correspondence,
   **Proposition 3.2.2** for the limit of $\lambda^u$ at a lattice point of $\operatorname{relint}(\sigma)$,
   **Theorem 4.1.3** for $M\to\ZZ^{\Sigma(1)}\to\Cl(X_\Sigma)\to0$. The $\ZZ/d\ZZ$ cokernel is now shown and not asserted:
   the matrix of the map on the bases $e_1^*,e_2^*$ and $u_1,u_2$ is $\begin{pmatrix}0&d\\1&-1\end{pmatrix}$, determinant
   $-d$.
7. **`PR-FULCRIT`.** Both tables now carry a number per row, each read at its statement: normal **3.1.5**; smooth
   **1.2.16** with **1.3.12** and **3.1.19(a)**; simplicial $\Leftrightarrow$ $\QQ$-factorial **4.2.7**; complete
   **3.4.6**; projective **3.1.6** with **6.1.14**; base point free **6.1.7** (a)$\Leftrightarrow$(d); ample **6.1.14**
   with **6.1.12**; very ample **6.1.10(c)** with **2.2.17**; $|\det(v_1,\dots,v_n)|=1$ **1.2.16**. The remark's claims are
   exact as stated: **Theorem 6.1.15** is "on a smooth complete toric variety, a divisor is ample if and only if it is
   very ample", and the surface case is **Corollary 2.2.13** (every lattice polygon is normal) with **Proposition 2.2.18**
   and 6.1.10(c). Reflexivity versus the site's Fano convention is **Definition 8.3.1** with **Theorem 8.3.4**, and
   `D-VARFANO` was re-read to confirm that its block's standing hypothesis is a smooth complete $X$. One precision
   repair: $\FF_m$ is taken with $m\ge0$, which is where $D_2$ is the negative section and $D_4\sim S+mF$; for $m<0$ the
   self-intersections exchange. The ampleness criterion on $\FF_m$ cites Har77 **Theorem V.1.10** with
   $D^2=2ab+mb^2$.
8. **`PR-FULKSQ`.** The proof is the card's own and its arithmetic checks. $K_X=-\sum_iD_i$ is CLS **Theorem 8.2.3**;
   $D_i^2=-a_i$ and the adjacency pattern $1$/$0$ are **Theorem 10.4.4(a),(b)** with the wall relation
   $u_{i-1}+u_{i+1}=b_iu_i$ of **Lemma 10.4.1**; the induction uses the classification, **Theorem 10.4.3**; and the
   alternative argument's Noether formula is Har77 **Example A.4.1.2**. The misattached bracket — `[@Ful93, §2.5]` on the
   sentence asserting that the sum rule does *not* need Noether's formula — is gone: Fulton §2.5 supported nothing here.
   $K^2=12-d$ with $d=3,4$ giving $9,8$ and each blowup subtracting one were recomputed.
9. **`D-CRVBRILLNOETHER`.** Read whole; **MET**, and unchanged, which is the `QUAL-03` outcome and not a commit. The
   Brill--Noether number $\rho=g-(r+1)(g-d+r)$, the hypothesis $g-d+r\ge0$ (equivalently $\rho\le g$, which is what keeps
   the definition away from the range $d\ge2g-1$ where $W^r_d=\Pic^d$ has dimension $g$), the statement that $W^r_d$ is a
   closed subscheme cut out as a degeneracy locus, and the three theorems with their attributions in the statement are
   all correct. So is the example: $\rho(g,1,d)=2d-g-2$, nonnegative exactly for $d\ge\lceil(g+2)/2\rceil=
   \lfloor(g+3)/2\rfloor$. The remark's claim that no edition of Arbarello--Cornalba--Griffiths--Harris or
   Griffiths--Harris is retained was checked against `tmp/sources`: neither is present, and the retained mentions of
   Brill--Noether (Fulton, *Algebraic Curves*, the pp. 55--62 excerpt, Exercise 8.30 the reciprocity theorem; Reid's
   chapters) state no Brill--Noether theorem. **That is a check cleared by absence of evidence, not a checked citation**,
   and it is the reason the card's theorem has no locator.
10. **`D-8XX95`.** The batch's one mathematical defect, and it is a hypothesis. The second theorem read "Let $f\colon X\to
    Y$ be of finite type with $X$ Noetherian", and no printed statement gives the discrete-valuation-ring criterion under
    that hypothesis: Stacks **Lemma 32.15.2** (tag 0207, for separatedness) and **Lemma 32.15.3** (tag 0208, for
    properness) assume $S$ **locally Noetherian** and $f$ of finite type, and the Noetherian-source shape is
    Hartshorne's **Exercise II.4.11**, which sits under §II.4's standing hypothesis that all schemes are noetherian.
    The card now states "$Y$ locally Noetherian and $f$ of finite type" and records both. The first theorem is correct as
    stated — $f$ quasi-separated throughout, finite type for the properness direction — and now cites **Lemma 26.22.1**
    (tag 01KZ) with **Lemma 26.22.2** (tag 01L0, where quasi-separatedness enters) and **Lemma 29.43.1** (tag 0BX5,
    fetched live, whose printed hypotheses are finite type and quasi-separated). The unnumbered definition of proper is
    cited by section, and the closed-not-universally-closed example is Har77 **Example II.4.6.1**.

**Scope of this batch.** `T-TORDIV` was not redone: its second displayed sequence is CLS **Theorem 4.2.1** in `58bdc94cc8`
already on `main`, and the Fulton section stands beside it. `T-JLB44J` was not invented — §9.2's exhaustive check that no
such card and no Exercise III.1.6/III.1.8 exists on `main` stands, and nothing here revisits it. `PR-RJ3P7` at `640a75d6`
and `T-FFDESCENT` at `73e340990c` were not reopened.

**The unread set, measured at `a6d7a2e75b`.** `wiki/algebraic-geometry/` is still **82** files and **4311** lines, and the
pages transclude **327** distinct card ids (`rg -o '\[\[[A-Z][A-Z0-9-]{2,}(\|[^\]]*)?\]\]'` over the 82 files, pipe
target stripped, `sort -u`). The record has now read **28 distinct** card ids in full — the ten of §1, the five of §9.1,
the four of §9.3 and the ten of this batch, where `D-FULSAT` is a second reading of a card §1 already read — so **299
remain**, and **300** if the batch is counted without collapsing that repeat. That is a count of cards and not a list, and
the reading owed is still one card at a time; §9 item 5's list of named remainders stands, with
`FE-SRFFERMATQUARTIC`, `T-FULBETTI`, `T-TORCOHOM`, `D-TORMOMENT`, `D-FULSTAR`, `PR-O8V3I`, `PR-FULCRIT`, `PR-FULKSQ`,
`D-CRVBRILLNOETHER` and `D-8XX95` now struck from it. Nothing in this batch changes the page count, the transclusion
count, or the 82-page condition: no page was edited, the ten cards are transclusions of pages already read in §8, and the
chapter's completion still requires every page and every one of the 327 cards.




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

## 11. What this version does and does not do

It repairs five cards (`T-FFDESCENT`, `D-VARCREPANT`, `PR-RJ3P7`, `T-MORMIRACLE`, `PR-TORPOS`) in their own commits and
eight pages in one commit, all named by SHA in §0 and §3, and it corrects the seven adjudications ra84 named. Each
touched card passes `qualc.authoring check`; the macro mirror check passes and no new control word is introduced.

It does **not** claim #189's first acceptance clause. §9 is the list of what is unread or unlocatable, the largest item
being the ~310 transcluded cards that this session did not open, and `divisors/weil-and-cartier.md:34`'s citation, which
is owed a number. §8 records where the reading found nothing rather than certifying those pages clean.
