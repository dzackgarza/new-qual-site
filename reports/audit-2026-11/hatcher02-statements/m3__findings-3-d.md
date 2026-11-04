# Audit findings — SRC-TEXT-HAT02, section §3.D ("The Cohomology of SO(n)")

Auditor: member `m3` (swarm `smvy0zsoh`). Source of truth: `tmp/hat/AT.txt`; every
book quotation below is one line of that file, quoted verbatim, with its line number.
Nothing under `corpus/` was modified.

## Card census for this slice

| section | cards on disk | statements read | proofs read | unread |
|---|---|---|---|---|
| §3.D (`corpus/collections/SRC-TEXT-HAT02/3-d/`) | 3 | 3 | 3 | 0 |

Cards: `E-HAT-3.D-1`, `E-HAT-3.D-2`, `E-HAT-3.D-3`.
The section is complete: the book prints exactly three exercises in §3.D —
AT.txt:15093 `Exercises`, AT.txt:15094–15096 (ex. 1), 15097–15098 (ex. 2), 15099 (ex. 3),
and §3.E begins at AT.txt:15100. §3.D contains no other exercises, so no exercise is
missing from the corpus. (The corpus convention is exercise-only cards; the four
propositions of §3.D, 3D.1–3D.4, have no cards, which is consistent.)

All three proofs were read line by line, in full. Nothing in this slice is unread.

---

## E-HAT-3.D-1

### 1. STATEMENT — **statement matches**

Book (AT.txt:15094–15096):
```
1. Show that a topological group with a finite-dimensional CW structure is an ori-
entable manifold. [Consider the homeomorphisms x ֏ gx or x ֏ xg for fixed g
and varying x in the group.]
```
Card: `Show that a topological group with a finite-dimensional CW structure is an orientable manifold. [Consider the homeomorphisms $x \mapsto gx$ or $x \mapsto xg$ for fixed $g$ and varying $x$ in the group.]`

Word for word identical: hypothesis "finite-dimensional CW structure", conclusion
"orientable manifold", and the bracketed hint kept with **both** alternatives
`gx` **or** `xg`. (`֏` in the extraction is Hatcher's ↦ glyph.) The book's own
back-reference to this exercise uses the same words, AT.txt:14620–14622:
`An exercise at the end of the section is to / show that a topological group with a finite-dimensional CW structure is an orientable / manifold, so SO(n) is a closed orientable manifold.`

### 2. PROOF — **proof has a gap**: the orientability half rests on one unproved lemma
(the conclusion and the statement are true; the gap is repairable, not an error of fact).

Steps checked, with what each needs:

* "let $d$ be the largest dimension of a cell" — fine: finite-dimensional means the set
  of cell dimensions is bounded, and a group is nonempty, so a maximum exists.
* "the union of all cells other than $e^d$ is a subcomplex, hence closed. Therefore the
  open cell $e^d$ is an open subset of $G$" — **correct**, and this is exactly CW axiom
  (ii), AT.txt:25939–25940: `(ii) For each cell eαn , Φαn (∂Dαn ) is contained in the union of a finite number of cells of / dimension less than n .`
  (a $d$-cell's closure contains no other $d$-cell), plus axiom (iii) AT.txt:25941
  `(iii) A subset of X is closed iff it meets the closure of each cell of X in a closed set.`
* "$L_g$ … carrying $x$ to $y$ … Hence $L_g(e^d)$ is an open neighborhood of $y$
  homeomorphic to $\RR^d$" — correct ($g=yx^{-1}$ gives $gx=y$).
* "so $G$ is a $d$-manifold" — **minor omission**: Hatcher's manifold must also be
  Hausdorff. AT.txt:11491–11493: `A manifold of dimension n , or more concisely / an n manifold, is a Hausdorff space M in which each point has an open neighborhood / homeomorphic to Rn .`
  The card checks only the local-Euclidean half. Harmless, because the CW hypothesis
  supplies Hausdorffness (Prop. A.2, AT.txt:25933 `Given a Hausdorff space X and a family of maps Φα : Dαn →X ,`),
  but the proof never says so.
* "Since a CW complex is locally path-connected, each connected component of $G$ is
  path-connected." — true; the book has it at AT.txt:3198–3199 `For / example, CW complexes have the much stronger property of being locally contractible,`
  but the card cites nothing (**minor**).
* "$L_hL_g^{-1}=L_{hg^{-1}}$" — **correct** as an identity of maps
  ($L_h(L_g^{-1}z)=hg^{-1}z$), and $hg^{-1}\in G_0$ because $G_0$ is a subgroup (used
  without proof; standard for topological groups, **minor**).
* **The gap.** Card: "The family $L_{\gamma(t)}$ is an isotopy from the identity
  homeomorphism to $L_{hg^{-1}}$. *An isotopy cannot reverse the local orientation
  class*, so all transition maps preserve the transported orientations. Hence $G_0$ is
  orientable." The italicised sentence is the entire content of orientability here, and
  it is asserted with no proof and no citation. It is a true lemma (a homeomorphism of a
  manifold that is isotopic to the identity preserves orientation: lift the isotopy to
  the 2-sheeted orientation covering by the homotopy lifting property), but **nothing in
  §3.D states or proves it** — the book's orientation machinery is §3.3, beginning at
  AT.txt:11491 — and the card supplies neither. Strictly, the card also owes the reader
  the statement that $g\mapsto (L_g)_*\mu_e$ is continuous as a family of local orientation
  classes over $G_0$; that continuity is precisely what the "transition maps" computation
  is meant to establish, so as written the passage is a sketch of the right proof rather
  than a proof.
* Cosmetic, harmless: the seed orientation is placed "at the identity $e$", whereas the
  only chart in hand is the one on the open top cell; and $L_g$ is called a "local
  homeomorphism" although it is a global one. Both are harmless — any class at $e$ gives
  a coherent family by the computation above, and every class at $e$ is the class of some
  chart at $e$ — but the text as printed does not say this.

---

## E-HAT-3.D-2

### 1. STATEMENT — **statement matches**

Book (AT.txt:15097–15098):
```
2. Using the CW structure on SO(n) , show that π1 SO(n) ≈ Z2 for n ≥ 3 . Find a
loop representing a generator, and describe how twice this loop is nullhomotopic.
```
Card: `Using the CW structure on $SO(n)$, show that $\pi_1 SO(n) \approx \ZZ_2$ for $n \geq 3$. Find a loop representing a generator, and describe how twice this loop is nullhomotopic.`

Identical, including the `≈`, the hypothesis $n\ge 3$, and both tasks of the second
sentence. The book prints `π1 SO(n)` (no parentheses); the card matches it.

### 2. PROOF — **proof correct**

* Cells = admissible sequences. AT.txt:14700–14702 `Proposition 3D.1. The maps ρϕI : DI →SO(n) , for I ranging over all admissible / sequences, are the characteristic maps of a CW structure on SO(n) …`;
  the admissibility condition is AT.txt:14697 `n > i1 > ··· > im > 0 . These sequences will be called admissible, as will the sequence`;
  the cells are AT.txt:14704–14707 `In particular, there is a single 0 cell e0 = {11} … The / other cells eI = ei1 ··· eim are products, via the group operation in SO(n) , of the cells / ei ⊂ P n−1 ⊂ SO(n) .`
  "In dimensions at most 2 exactly three cells $e^0,e^1,e^2$": the admissible sequences
  of weight $\le 2$ are $()$, $(1)$, $(2)$ (and $(1,1)$ is not admissible) — correct for
  $n\ge 3$, where $2<n$.
* "$e^1$ and $e^2$ are the images of the standard cells of $RP^{n-1}$ under
  $\rho(v)=r(v)r(e_1)$" — correct; $\rho(v)=r(v)r(e_1)$ is AT.txt:14682 and the cells
  $e_i\subset P^{n-1}\subset SO(n)$ are AT.txt:14706–14707.
* "The characteristic map of the 2-cell of $RP^{n-1}$ restricts on its boundary circle to
  the double covering $S^1\to RP^1\cong S^1$" — correct, AT.txt:14690–14691
  `If ϕi : D i →P i is the standard characteristic map for the i cell of / P i , restricting to the 2 sheeted covering projection ∂D i →P i−1`.
* "Consequently the 2-cell of $SO(n)$ is attached to the 1-cell by a map of degree 2" —
  correct, and the one hidden hypothesis is satisfied: $\rho$ restricted to $P^1$ is
  injective onto the 1-skeleton (injectivity of $\rho$: AT.txt:14683–14686 `This map is injective … we may think of ρ as embedding P n−1 as a subspace of SO(n) .`,
  and the 1-skeleton is $\rho(P^1)$ by AT.txt:14704–14707). The composite
  $S^1\to P^1\to e^1\cup e^0$ is then the double cover, of degree 2. Cross-check: the
  same degree is what Hatcher's cellular boundary formula gives, $\partial e_2=2e_1$
  (appendix (2) below, computed independently), so the 2-cell's attaching degree really
  is 2.
* "$\pi_1(SO(n)^{(2)})=\langle a\mid a^2\rangle\cong\ZZ_2$" — correct (one 0-cell, one
  1-cell, one 2-cell attached by a degree-2 map; van Kampen).
* "Attaching cells of dimension at least 3 does not change the fundamental group" —
  correct, and its hypotheses hold: Prop. 1.26(b),(c), AT.txt:2534–2537
  `(b) If Y is obtained from X by attaching n cells for a fixed n > 2 , then the inclusion / X ֓ Y induces an isomorphism π1 (X, x0 ) ≈ π1 (Y , x0 ) . / (c) For a path-connected cell complex X the inclusion of the 2 skeleton X 2 ֓ X in- / duces an isomorphism π1 (X 2 , x0 ) ≈ π1 (X, x0 ) .`
  $SO(n)$ is path-connected with a single 0-cell (AT.txt:14704), so (c) applies.
* The geometric generator: "a fixed oriented 2-plane … rotate through angle
  $0\le\theta\le2\pi$ … it is precisely the loop represented by the 1-cell $e^1$" —
  correct. With $\rho(v)=r(v)r(e_1)$, $v$ a unit vector at angle $\theta$ from $e_1$,
  $\rho(v)$ is rotation by $2\theta$, and the 1-cell of $P^1=RP^1$ runs over all lines
  $\theta\in[0,\pi]$, i.e. a full $2\pi$ turn — the loop the card describes.
* "the attaching map of $e^2$ traverses the 1-cell twice, so the characteristic disk of
  $e^2$ is an explicit nullhomotopy of this doubled loop. Thus the generator has order
  exactly 2." — correct; the characteristic map $\rho\phi_{(2)}:D^2\to SO(n)$ has that
  doubled loop as boundary, and $\pi_1=\ZZ_2$ makes the order exactly 2.
* Harmless imprecision only: the double of $\theta\mapsto R(2\theta)$ is a $4\pi$ turn
  traversed in a non-uniform parametrisation, not literally the constant-speed $4\pi$
  rotation; it is homotopic rel. endpoints, so the claim stands unchanged.

---

## E-HAT-3.D-3

### 1. STATEMENT — **statement matches**

Book (AT.txt:15099):
```
3. Compute the Pontryagin ring structure in H∗ (SO(5); Z) .
```
Card: `Compute the Pontryagin ring structure in $H_*(SO(5); \ZZ)$.` — identical.

### 2. PROOF — **proof correct** (three one-line justifications are left unwritten; all
are true and are flagged M3–M5 below). I recomputed the entire computation
independently; the script and its output are `verify_3d3.py` in this directory, and the
results are quoted in the appendix.

* "The subcomplexes $C^2$ and $C^4$ have generators $e^{2i-1}$, $e^{2i}$, and
  $E_i=e^{2i}e^{2i-1}$, with $\partial e^{2i}=2e^{2i-1}$, $\partial e^{2i-1}=\partial E_i=0$"
  — correct, verbatim from AT.txt:14928–14932 `let C 2i be the subcomplex of C∗ SO(n) with basis the cells e0 , / e2i , e2i−1 , and e2i e2i−1 . This is a subcomplex since de2i−1 = 0 , de2i = 2e2i−1 , / and, in P 2i × P 2i−1 , d(e2i × e2i−1 ) = de2i × e2i−1 + e2i × de2i−1 = 2e2i−1 × e2i−1 , hence / d(e2i e2i−1 ) = 0`
  (also AT.txt:14917–14918 `For a cell ei ⊂ P n−1 ⊂ SO(n) the cellular bound- / ary dei is 2ei−1 for even i > 0 and 0 for odd i`).
* "The cellular complex of $SO(5)$ is $C^2\otimes C^4$" — correct, AT.txt:14934
  `C∗ SO(2k + 1) ≈ C 2 ⊗C 4 ⊗ ··· ⊗C 2k` with $k=2$.
* "The integral Künneth theorem therefore gives free groups in degrees $0,3,7,10$ and one
  $\ZZ_2$ in each of degrees $1,3,4,5,6,8$; all other groups vanish." — **correct**, and
  the theorem's hypotheses are satisfied: Thm 3B.5, AT.txt:13588–13589
  `Theorem 3B.5. If R is a principal ideal domain and the R modules Ci are free, then / for each n there is a natural short exact sequence … and this sequence splits.`
  with $R=\ZZ$ a PID and the chain modules free (cellular chains are free on cells,
  AT.txt:5086 `has chain groups Cn (X) which are free abelian groups with basis the n cells of X ,`).
  Recompute: $H_*(C^2)=\ZZ,\ZZ_2,0,\ZZ$ in degrees $0,1,2,3$ and $H_*(C^4)=\ZZ,\ZZ_2,0,\ZZ$ in
  degrees $0,3,4,7$ (AT.txt:14945–14946 `Since H∗ (C 2i ) consists of Z ’s in dimensions 0 and 4i − 1 and a Z2 in dimension / 2i − 1`);
  Künneth gives $H_0=\ZZ$, $H_1=\ZZ_2$, $H_2=0$, $H_3=\ZZ\oplus\ZZ_2$, $H_4=\ZZ_2$,
  $H_5=\ZZ_2$, $H_6=\ZZ_2$, $H_7=\ZZ$, $H_8=\ZZ_2$, $H_9=0$, $H_{10}=\ZZ$ — exactly the
  card's list. (Script, appendix (3).) The wording "free groups in degrees 0,3,7,10" is
  loose — degree 3 is $\ZZ\oplus\ZZ_2$ — but the card also lists the $\ZZ_2$ in degree 3, so
  the total statement is right.
* "$a=[e^1]$ and $c=[e^3]$, both of order 2, $b=[E_1]\in H_3$ and $d=[E_2]\in H_7$ free
  generators" — correct; $E^i=e^{2i}e^{2i-1}$ is Hatcher's own generator, AT.txt:14983
  `Let E i be the cycle e2i e2i−1 generating a Z summand of H∗ (SO(n); Z) .` Verified as
  non-boundary cycles by the script, appendix (4).
* The class $t$: "represented by $e^4e^1+e^3e^2$ … its boundary is $2e^3e^1-2e^3e^1=0$ …
  $\partial(e^4e^2)=2(e^4e^1+e^3e^2)$" — **all three equations are right** (checked with
  Hatcher's boundary formula AT.txt:14921–14924; script, appendix (2)):
  $d(e^4e^1)=2e^3e^1$, $d(e^3e^2)=-2e^3e^1$, $d(e^4e^2)=2e^3e^2+2e^4e^1=2t$. So $2t=0$ and
  $t\ne0$, i.e. $t$ has order exactly 2 — appendix (4) shows $t\notin\operatorname{im}\partial$.
* "Hatcher's mod-two Pontryagin ring is the exterior algebra on $e^1,e^2,e^3,e^4$" —
  correct: Thm 3D.2(b), AT.txt:14803 `(b) The Pontryagin ring H∗ (SO(n); Z2 ) is the exterior algebra ΛZ2 [e1 , ··· , en−1 ] .`
  with the degree convention at AT.txt:14805 `Here ei denotes the cellular homology class of the cell ei ⊂ P n−1 ⊂ SO(n) ,`
  and $n=5$.
* "Since the integral homology has only 2-torsion, reduction modulo 2 is injective on each
  torsion subgroup." — true (the kernel of $H_n(X;\ZZ)\to H_n(X;\ZZ_2)$ is $2H_n(X;\ZZ)$,
  which vanishes on 2-torsion). Terse but justified.
* The product list "$\;ac=[e^3e^1],\; at=bc=[e^3e^2e^1],\; ct=ad=[e^4e^3e^1],\; bd$ generates
  $H_{10}$" — **correct in every entry**. Recomputed in the mod-2 exterior algebra
  ($\mathrm{red}(a)=e^1$, $\mathrm{red}(b)=e^1e^2$, $\mathrm{red}(c)=e^3$,
  $\mathrm{red}(d)=e^3e^4$, $\mathrm{red}(t)=e^1e^4+e^2e^3$): the six named products all
  reduce to the reductions of the named cycles $[e^3e^1]$ ($H_4$), $[e^3e^2e^1]$ ($H_6$),
  $[e^4e^3e^1]$ ($H_8$), $[e^4e^3e^2e^1]$ ($H_{10}$) — script, appendix (5),(6) — and each
  of those cycles is a non-boundary, so it generates its $\ZZ_2$ or $\ZZ$ (appendix (4)).
* "All squares of positive-degree generators vanish." — $b^2=d^2=0$ is Hatcher's own
  computation, AT.txt:14995–14998 `When i = j we have (E i )2 = 0 since e2i e2i−1 e2i e2i−1 = / e2i e2i e2i−1 e2i−1 , which lies in a lower-dimensional skeleton`; $a^2=c^2=0$ by
  the mod-2 computation; but **$t^2=0$ is asserted with no reason** (it needs: $2t=0$, so
  $\mathrm{ord}(t^2)\le2$, while $t^2\in H_{10}\cong\ZZ$ is torsion-free). True as claimed. **M3**
* "Every other product of generators vanishes." — true, but no case check is given. The
  cases are: $ab=0$, $bt=0$ (mod 2), $cd=0$ ($2\cdot cd=(2c)d=0$ and $H_{10}$ torsion-free),
  $dt=0$ ($H_{12}=0$), the five squares, and then every product of three or more
  generators (smallest possible degree $1+3+3=7$; the ones that land in a torsion group
  die by associativity from $ab=b^2=c^2=0$ or by $H_9=H_{11}=0$). All checked. **M4**
* "The product $db=-bd$, while reversing the order of a product with torsion value leaves
  that value unchanged." — true, and it is literally in the book, in the proof of
  Prop. 3D.4, AT.txt:14993–14995 `Applying / this four times to commute E i E j = e2i e2i−1 e2j e2j−1 to E j E i = e2j e2j−1 e2i e2i−1 , three / of the four applications give a sign of −1 and the fourth gives a +1 , so we conclude / that E i E j = −E j E i if i < j`
  — with $b=E^1$, $d=E^2$ this is exactly $db=-bd$. The card cites nothing, and the
  half-sentence about reversing the order is only true because the torsion values are
  2-torsion ($x=-x$). **M5**
* The closing sentence ("These generators, additive groups, and products give the
  integral Pontryagin ring") is true: $\{1,a,b,c,ac,t,at,d,ad,bd\}$ in degrees
  $0,1,3,3,4,5,6,7,8,10$ is an additive basis in every degree, so the listed products
  determine all products by associativity. The card does say this; it just does not show
  the span, which is immediate from the degree list it has already given.

---

## Summary of defects, most serious first

1. **E-HAT-3.D-1, gap in the proof (the orientability half).** "An isotopy cannot
   reverse the local orientation class, so all transition maps preserve the transported
   orientations. Hence $G_0$ is orientable" is the load-bearing step and is stated with no
   proof and no citation; the book does not contain it in §3.D (its orientation theory is
   §3.3, AT.txt:11491 ff.). The lemma is true and the exercise's conclusion is right, so
   this is a missing justification, not a false step.
2. **E-HAT-3.D-1, minor omission.** "so $G$ is a $d$-manifold" checks only the
   local-Euclidean condition; Hatcher's definition also requires Hausdorff
   (AT.txt:11491–11493). Supplied by the CW hypothesis (AT.txt:25933) but never mentioned.
3. **E-HAT-3.D-3, minor omission (M3).** "$t^2=0$" is included in "all squares of
   positive-degree generators vanish" without the one-line argument ($2t=0$ plus
   $H_{10}\cong\ZZ$ torsion-free).
4. **E-HAT-3.D-3, minor omission (M4).** "Every other product of generators vanishes" is
   asserted without the case check ($ab$, $bt$, $cd$, $dt$, squares, and triple products).
   The statement is true.
5. **E-HAT-3.D-3, minor omission (M5).** $db=-bd$ and the order-reversal sentence are
   asserted without their source; the sign is computed in the book at AT.txt:14990–14995.
6. **E-HAT-3.D-1, minor omissions.** "CW complexes are locally path-connected" and
   "$G_0$ is a subgroup, so the other components are cosets" are used without citation
   (both are standard; the first is at AT.txt:3198–3199).
7. **E-HAT-3.D-1, cosmetic.** The seed orientation is placed at the identity $e$ rather
   than on the open top cell, and $L_g$ is called a "local homeomorphism". Both are
   harmless as argued above, but the text does not say why.
8. **E-HAT-3.D-1, cosmetic (frontmatter).** `title: "Topological groups with finite CW
   structure are manifolds"` drops two words of the exercise — "finite-**dimensional**"
   and "**orientable**". The statement block itself is correct.
9. **E-HAT-3.D-2, cosmetic.** "Traversing this loop twice gives a $4\pi$ rotation" is
   right up to reparametrisation (the double of $\theta\mapsto R(2\theta)$ is not the
   constant-speed $4\pi$ turn). No effect on the conclusion.
10. **E-HAT-3.D-3, metadata.** This card has **no `source-checked` audit event** at all
    (cards 3.D-1 and 3.D-2 have one, by `gpt-5.6-sol`). Separately: cards 3.D-1 and 3.D-2
    carry a `solution-reviewed` event by `gpt-5.6-sol`, which is why §3.D was correctly
    listed as unread — the "already read" criterion is an event by `claude`.

**No statement in this slice differs from the printed exercise.** All three are verbatim
matches, hints included. The proofs of 3.D-2 and 3.D-3 are correct; the proof of 3.D-1 is
correct in substance but has defect 1 outstanding.

## Appendix — independent recomputation for E-HAT-3.D-3

`verify_3d3.py` (with the small exact-arithmetic SNF helper `snf.py`) rebuilds the
cellular chain complex of SO(5) from Hatcher's boundary formula and prints:

1. `d^2 = 0` — verified.
2. `d(e_1)=0, d(e_2)=2e_1, d(e_3)=0, d(e_4)=2e_3, d(e_2e_1)=0, d(e_4e_3)=0,
   d(e_4e_1)=2e_3e_1, d(e_3e_2)=-2e_3e_1, d(e_4e_2)=2e_3e_2+2e_4e_1 = 2t`.
3. $H_*=\ZZ,\ZZ_2,0,\ZZ\oplus\ZZ_2,\ZZ_2,\ZZ_2,\ZZ_2,\ZZ,\ZZ_2,0,\ZZ$ in degrees $0..10$
   (exact Smith normal form of $\partial_n$ and of $\operatorname{im}\partial_{n+1}$ inside
   $\ker\partial_n$) — the card's additive list, exactly.
4. Each named cycle is a cycle and not a boundary, hence nonzero: $[e^1]$, $[e^3]$,
   $[e^2e^1]$, $[e^4e^3]$, $[e^4e^1+e^3e^2]$, $[e^3e^1]$, $[e^3e^2e^1]$, $[e^4e^3e^1]$.
5. The mod-2 products of $a,b,c,d,t$ are nonzero exactly for $(a,c)$, $(a,d)$, $(a,t)$,
   $(b,c)$, $(b,d)$, $(c,t)$ and zero for all nine remaining pairs — the card's split
   between nonvanishing and vanishing products.
6. $ac=[e^3e^1]$, $at=bc=[e^3e^2e^1]$, $ct=ad=[e^4e^3e^1]$, $bd=[e^4e^3e^2e^1]$ all hold
   after reduction mod 2, and the target classes are 2-torsion (resp. the $\ZZ$ generator),
   so by injectivity of reduction on torsion the integral equalities follow.

## What was not done here (other members hold these, per the board)

§3.F, §3.H, §4.1 exercises 10–23, §4.2, §4.3 and the chapter-4 additional topics were not
audited by me. No file under `corpus/` was edited. Nothing in this slice was sampled: all
three statements and all three proofs were read in full.
