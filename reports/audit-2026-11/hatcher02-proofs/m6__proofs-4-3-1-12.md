# §4.3 exercises 1–12 — proof audit (slice 6)

Slice 6 of the swarm's disjoint slices: the 12 cards `4-3` exercises 1 to 12.
Book text quoted by line number from `tmp/hat/AT.txt` (Hatcher, *Algebraic Topology*).

**Question asked of every card.** Is the conclusion the card states actually proved, from the book's
hypotheses, by the proof the card carries? Statements were excluded by the task; only proofs are
judged. Verdicts: `correct`, `gap` (a step is missing or an unproved nontrivial fact is asserted),
`wrong` (a step is false).

**Standard applied.** A step is a defect if it asserts a nontrivial theorem or construction without
giving the construction/argument and without citing a numbered result whose hypotheses I checked in
AT.txt. A step is *not* a defect if it names a construction whose verification is one standard line
from results already proved, if it cites a numbered result whose hypotheses hold, or if it is a
standard homology/homotopy computation for a named space. Terse, correct proofs are recorded as
`correct` with no patch.

**Verdicts at a glance:** 10 `correct` · 1 `gap` (`E-HAT-4.3-5`) · 1 `wrong` (`E-HAT-4.3-9`).
Patch specifications for the two defective cards follow their verdicts.

## Book locations used in checking

- §4.3 exercise block, AT 20754–20794: ex.1 20755–20758, ex.2 20759–20761, ex.3 20762–20764,
  ex.4 20765–20767, ex.5 20768–20769 (with the hint "Build a K(Z, n) from S^n by attaching cells of
  dimension ≥ n + 2"), ex.6 20770–20773, ex.7 20774–20776, ex.8 20777–20778, ex.9 20779–20780,
  ex.10 20781–20786, ex.11 20790–20792, ex.12 20793–20794.
- Theorem 4.57 (`⟨X,K(G,n)⟩ ≅ H^n(X;G)`, all CW `X`, all `n>0`; `T([f]) = f^*(α)`): AT 19541–19543.
  Fundamental class = inverse Hurewicz element of `H^n(K;G) ≈ Hom(H_n(K),G)`: AT 19549–19555.
  Same for unbased `[X,K(G,n)]`: AT 19556–19561.
- Theorem 3.2 (UCT for cohomology, split exact, `C` free): AT 9744–9748.
- Theorem 4.32 (Hurewicz, `(n−1)`-connected, `n ≥ 2`): AT 18260–18262. `H_1 ≅ π_1^{ab}`: Theorem 2A.1,
  AT 8312. Theorem 4.37 (relative Hurewicz): AT 18453.
- Theorem 4.8 (cellular approximation): AT 17393–17395. Example 4.11 (cellular approximation for pairs,
  homotopy stationary on subcomplexes where the map is already cellular): AT 17505–17510.
  Proposition 0.16 (CW pairs have the HEP): AT 926.
- Fibration = HLP with respect to all spaces: AT 18713–18714. Fiber bundle = local triviality with fibre
  `F`: AT 18771–18786. "In a fiber bundle all the fibers are homeomorphic by definition": AT 20067–20068.
- H-space: multiplication with a two-sided homotopy identity `e`, homotopies through maps `(X,e)→(X,e)`:
  AT 13964–13968. The usual action of `π_1` on `π_n` by basepoint change, `β_γ([f]) = [γf]`, with `β_γ`
  a homomorphism and `β_{γη} = β_γ β_η`: AT 17055–17068.
- Fiber-preserving map / fiber homotopy equivalence: AT 20117–20121. Pullback fibration: AT 20128–20135.
  Proposition 4.62 (pullbacks along homotopic maps are fiber homotopy equivalent): AT 20137–20138.
  `E_f` and Proposition 4.64: AT 20169–20175.

---

## E-HAT-4.3-1 — `corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-1.md`

Book: AT 20755–20758. **Verdict: correct.**

- `RP^∞` and `CP^∞` are CW complexes, so Theorem 4.57 (AT 19541) applies to `X = RP^∞`, `G = Z`, `n = 2`,
  and the nonzero class `u` of `H^2(RP^∞;Z) ≅ Z/2` is `f^*(c)` for some `f`. The card names that class `ν`
  in the preceding display and then writes `u`; a notation slip with one possible reading, not a gap.
- Trivial on reduced homology: for odd `i` the source `H̃_i(RP^∞;Z) = Z/2` maps to `H_i(CP^∞;Z) = 0`
  (cells of `CP^∞` only in even degrees), for even `i` the source vanishes. This covers all `i`, not just
  some degrees, so "every reduced homology homomorphism induced by `f` is zero" is established.
- The UCT half is the right explanation, not a hand-wave: in the natural UCT sequence (AT 9744–9748) for
  `RP^∞` the degree-2 map on `Hom` parts is `Hom(H_2(CP^∞),Z) → Hom(H_2(RP^∞),Z) = Hom(0,Z) = 0`, since
  `H_2(RP^∞;Z) = 0`; so the generator of `H^2(CP^∞;Z) = Z` is carried into the `Ext(H_1(RP^∞),Z) = Z/2`
  summand, which is exactly why a trivial map on homology does not force a trivial map on cohomology.

## E-HAT-4.3-2 — `corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-2.md`

Book: AT 20759–20761. **Verdict: correct.**

- Pointwise multiplication of based maps into the topological abelian group `S^1` is based
  (`f(x_0)g(x_0) = 1`) and respects based homotopies, so it descends to `⟨X,S^1⟩`; associativity and
  inverses are inherited pointwise. So a group structure is produced (AT 20759).
- The Künneth step is correct: `H^1(S^1×S^1;Z)` is free on `pr_1^*u, pr_2^*u`, so `μ^*u = a·pr_1^*u + b·pr_2^*u`,
  and restricting to `S^1×{pt}` resp. `{pt}×S^1` gives `a = deg μ|_{S^1×{pt}} = 1`, `b = 1`. So
  `μ^*u = pr_1^*u + pr_2^*u`.
- `(fg)^*u = (f,g)^*(pr_1^*u + pr_2^*u) = f^*u + g^*u`, and Theorem 4.57 (AT 19541–19543, with
  `T([f]) = f^*(u)`) identifies `[f]` with `f^*u`; additivity is precisely the statement that this
  bijection is an isomorphism of groups. Both halves of the exercise are proved.

## E-HAT-4.3-3 — `corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-3.md`

Book: AT 20762–20764. **Verdict: correct.**

- "Image a direct summand isomorphic to `Z`" gives the splitting `H_1(X;Z) = i_*H_1(S^1;Z) ⊕ A` and hence
  the homomorphism `λ` with `λ i_* = id`; that is the definition of a direct summand, so nothing is missing.
- UCT `H^1(X;Z) ≅ Hom(H_1(X),Z)` needs only `H_0` free for the `Ext` term to vanish (AT 9744–9748);
  `X` is a CW complex (AT 20762), so Theorem 4.57 (AT 19541) produces `r:X→S^1` with `r^*ι = u`.
- `(ri)^*ι = i^*u` corresponds to `λ i_* = id`, hence equals `ι`; a self-map of `S^1` of degree 1 is
  homotopic to the identity. Correct.
- The HEP step is exact, and this is the step most easily faked: `r|_{S^1} = r i` on the nose, so the
  homotopy `ri ≃ id_{S^1}` *starts* at `r|_{S^1}` and Proposition 0.16 for the CW pair `(X,S^1)` (AT 926)
  extends it to `X×I` starting at `r`; its endpoint `r'` satisfies `r'i = id_{S^1}`, a genuine retraction.

## E-HAT-4.3-4 — `corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-4.md`

Book: AT 20765–20767. **Verdict: correct.**

- `K(G,n)` is a CW complex, so Theorem 4.57 (AT 19541) gives `⟨K(G,n),K(H,n)⟩ ≅ H^n(K(G,n);H)`.
- `H_n(K(G,n);Z) ≅ π_n ≈ G`: Hurewicz Theorem 4.32 (AT 18260) for `n ≥ 2`, since `K(G,n)` is
  `(n−1)`-connected; for `n = 1` Hurewicz gives `H_1 ≅ π_1^{ab}` (Theorem 2A.1, AT 8312), which is `G`
  precisely because `G` is abelian — the reason the phrase "Since `G` is abelian" is there.
- `Ext` vanishes as claimed: `H_{n-1}(K(G,n);Z) = 0` for `n > 1`, and `H_0 = Z` is free for `n = 1`
  (AT 9744–9748). So `H^n(K(G,n);H) ≅ Hom(G,H)`.
- The final step, that `[f] ↦ f^*(α)` corresponds to `f_*` on `π_n`, is the naturality of Hurewicz plus
  the description of the fundamental class as the inverse Hurewicz element (AT 19549–19555). Compressed,
  but it is the right argument, and it is uniform in `n ≥ 1`.

## E-HAT-4.3-5 — `corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-5.md`

Book: AT 20768–20769 (the exercise, including the hint "Build a K(Z, n) from S^n by attaching cells of
dimension ≥ n + 2"). **Verdict: gap.**

The failing step is the whole comparison `[X,S^n] ≈ [X,K(Z,n)]`:

> "If $X$ is $n$-dimensional, obstruction theory or cellular induction says that an $n$-equivalence of
> targets induces a bijection ... Indeed, maps and homotopies from an $n$-dimensional CW complex depend
> only on the homotopy groups of the target through degree $n$."

What is missing: the bijection `j_*:[X,S^n] → [X,K(Z,n)]` is the substance of the exercise. It is
asserted as what "obstruction theory or cellular induction says"; no numbered result of the book is
cited, and the one-sentence "Indeed" restates the assertion rather than proving it. The remaining steps
(`π_i` of `S^n` and `K(Z,n)` agree for `i ≤ n`; representability) are fine and are proved. The
conclusion is true — only the justification is absent — hence a gap rather than an error. The book's own
hint supplies the elementary argument, which is what the patch inserts.

CARD: corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-5.md
BOOK: Hatcher, Algebraic Topology, §4.3 ex.5 and its hint, AT.txt 20768–20769; cellular approximation Thm 4.8, AT.txt 17393–17395; cellular approximation for pairs, Example 4.11, AT.txt 17505–17510
OLD:
```
If $X$ is $n$-dimensional, obstruction theory or cellular induction says that an $n$-equivalence of targets induces a bijection
$$
j_*:[X,S^n]\xrightarrow{\cong}[X,K(\ZZ,n)].
$$
Indeed, maps and homotopies from an $n$-dimensional CW complex depend only on the homotopy groups of the target through degree $n$.
```
NEW:
```
Take $K(\ZZ,n)$ as in the hint, built from $S^n$ by attaching only cells of dimension $\ge n+2$, and give $S^n$ its usual cellular structure with one $0$ cell and one $n$ cell; then $K(\ZZ,n)^k=(S^n)^k$ for $k\le n+1$, so $K(\ZZ,n)^n=K(\ZZ,n)^{n+1}=S^n$. By cellular approximation (Theorem 4.8) every map $X\to K(\ZZ,n)$ is homotopic to a cellular map, whose image lies in $K(\ZZ,n)^n=S^n$, and every class in $[X,S^n]$ has a cellular representative; so $j_*$ is surjective, and it is enough to show that cellular maps $c_0,c_1:X\to S^n$ that are homotopic in $K(\ZZ,n)$ are homotopic in $S^n$. Let $G:X\times I\to K(\ZZ,n)$ be such a homotopy. For $k\le n$ the $k$ skeleton of the subcomplex $X\times\partial I$ is $X^k\times\partial I$, and $G$ carries it into $K(\ZZ,n)^k$ because $c_0$ and $c_1$ are cellular and $K(\ZZ,n)^k=(S^n)^k$; so the relative form of cellular approximation (Example 4.11) deforms $G$ relative to $X\times\partial I$ to a cellular map, which lands in $K(\ZZ,n)^{n+1}=S^n$. Thus $c_0\simeq c_1$ in $S^n$ and $j_*$ is injective. Hence
$$
j_*:[X,S^n]\xrightarrow{\cong}[X,K(\ZZ,n)].
$$
```
WHY: The comparison of `[X,S^n]` with `[X,K(Z,n)]` was asserted, not proved. The replacement derives it from cellular approximation for the `K(Z,n)` built as the hint prescribes, whose skeleta up to dimension `n+1` are those of `S^n`; surjectivity and injectivity are each obtained by pushing a map of an at most `(n+1)`-dimensional CW complex off the cells of dimension `≥ n+2`. Nothing else in the proof changes.

## E-HAT-4.3-6 — `corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-6.md`

Book: AT 20770–20773; Exercise 4 is AT 20765–20767. **Verdict: correct.**

- `K(G,n)×K(G,n)` is a CW complex and a `K(G⊕G,n)`; Exercise 4 classifies maps out of it by
  `Hom(G⊕G,G)`, so `μ` corresponding to `(a,b) ↦ a+b` exists.
- Unit: with the H-space axioms as at AT 13964–13968, the two restrictions `x ↦ μ(x,e)`, `x ↦ μ(e,x)`
  must be homotopic to `id_{K(G,n)}` through based maps; they induce `id_G` on `π_n`, so by the
  injectivity part of Exercise 4 they are so homotopic.
- Associativity: `μ(μ×1)` and `μ(1×μ)` both induce `(a,b,c) ↦ a+b+c` on `π_n = G³`, so Exercise 4
  (with source `K(G³,n) = K^3`) makes them homotopic. Commutativity: `μ` and `μτ` both induce `a+b`.
- Homotopy inverse: `ν` with `ν_* = -id` exists by Exercise 4 (`a ↦ -a` is a homomorphism because `G` is
  abelian); `μ(id,ν)` induces `a + (−a) = 0`, hence is homotopic to the constant map at the basepoint,
  which is the unit. So `ν` is a two-sided homotopy inverse.
- Uniqueness: an H-space multiplication `μ'` satisfies `μ'∘i_1 ≃ id ≃ μ'∘i_2`, so
  `μ'_*(a,0) = a` and `μ'_*(0,b) = b`; since `μ'_*` is a group homomorphism, `μ'_* = +`, and Exercise 4
  gives `μ' ≃ μ`. Each inference is one standard step; nothing is asserted without support.

## E-HAT-4.3-7 — `corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-7.md`

Book: AT 20774–20776. **Verdict: correct.**

- `H^n(K(G,n)×K(G,n);G) ≅ Hom(H_n(K×K),G)` with vanishing `Ext` (`H_{n-1}(K×K) = 0` for `n ≥ 2` by
  Künneth from `H_i(K) = 0` for `0 < i < n`; `H_0` free for `n = 1`, AT 9744–9748), and
  `H_n(K×K;Z) ≅ π_n(K×K) = G⊕G` by Hurewicz (AT 18260). A class is therefore determined by its effect
  on `π_n`, so `μ_* = +` (Exercise 6) gives `μ^*u = pr_1^*u + pr_2^*u`; the two sides have the same
  image in `Hom(G⊕G,G)`. Correct, and the card signposts it ("under the Künneth/representability
  identification").
- `(μ(f,g))^*u = (f,g)^*μ^*u = f^*u + g^*u`, and Theorem 4.57 (AT 19541) sends `[f]` to `f^*u`, so the
  induced addition is ordinary addition in `H^n(X;G)`. Both directions of the correspondence claimed by
  the exercise are established.

## E-HAT-4.3-8 — `corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-8.md`

Book: AT 20777–20778; fibration defined as HLP with respect to all spaces, AT 18713–18714.
**Verdict: correct.**

- (⟸) Given `s` with `πs = id`: `x ↦ (f(x),H_x)` lands in `E_p` because `p f(x) = H(x,0)`, and
  `H̃(x,t) = s(f(x),H_x)(t)` has `H̃(x,0) = f(x)` (first coordinate of `π s = id`) and
  `p H̃(x,t) = H_x(t) = H(x,t)` (second coordinate). This is HLP for an arbitrary space `X`, which is
  the book's definition (AT 18713).
- (⟹) With `q:E_p → E`, `q(e,α) = e` and `K((e,α),t) = α(t)`, one has `K(-,0) = pq`, so HLP (applied to
  the space `E_p ⊂ E×B^I`, which is legitimate because HLP is required for all spaces) gives `K̃` with
  `K̃(-,0) = q`, `pK̃ = K`; then `s(e,α)(t) = K̃((e,α),t)` satisfies `s(e,α)(0) = e` and `p s(e,α) = α`,
  i.e. `πs = id_{E_p}`.
- No hypothesis beyond HLP is used, and no topology of `E_p` is needed beyond it being the displayed
  subspace. Both directions are complete.

## E-HAT-4.3-9 — `corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-9.md`

Book: AT 20779–20780; "In a fiber bundle all the fibers are homeomorphic by definition", with this very
projection given as the example of a fibration that is not a bundle: AT 20067–20069; fibre bundle =
local triviality: AT 18771–18786. **Verdict: wrong.**

The fibration half is correct and general: for `Δ = {(x,y) : 0 ≤ x ≤ 1, 0 ≤ y ≤ λ(x)}` with `λ ≥ 0`
continuous — which is what any linear projection onto an edge becomes in suitable affine coordinates,
`p(x,y) = x` — the map `r(x,y) = (x, min{y,λ(x)})` is a continuous fibre-preserving retraction of the
trivial bundle `I×[0,M] → I` onto `Δ`, so a lift of any homotopy is obtained by lifting in the product
and composing with `r`, and `r` fixes `Δ`.

The false step is the reason given for "not a fiber bundle":

> "For a linear projection onto an edge, the fibers over the endpoints of the edge are points, while
> fibers over interior points are nondegenerate closed intervals."

This is false for the maps the card treats, and the card's own coordinate model exhibits it: take
`λ(x) = 1 − x`, i.e. `Δ = conv{(0,0),(1,0),(0,1)}` with `p(x,y) = x`, a linear projection of the
2-simplex onto the edge `[(0,0),(1,0)]` that is the identity on that edge. The fibre over the endpoint
`0` is `{(0,y) : 0 ≤ y ≤ 1}`, a whole edge of the simplex, not a point. (The fibre over `1` is a single
point.) The conclusion survives: over the endpoint that is not the image of the third vertex the fibre
is a single vertex, and over interior points it is a nondegenerate interval, so not all fibres are
homeomorphic, which is what the bundle argument needs (AT 20067–20068). Both the exercise (AT 20779) and
Hatcher's remark (AT 20068) quantify over all such linear projections, so the false general claim is a
defect even though the conclusion is true.

CARD: corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-9.md
BOOK: Hatcher, Algebraic Topology, §4.3 ex.9, AT.txt 20779–20780; fibres of a bundle are homeomorphic, AT.txt 20067–20068; fibre bundle definition, AT.txt 18771–18786
OLD:
```
It is not a fiber bundle. For a linear projection onto an edge, the fibers over the endpoints of the edge are points, while fibers over interior points are nondegenerate closed intervals. These fibers are not homeomorphic, whereas all fibers of a bundle over the connected edge would be homeomorphic. Hence $p$ is not a fiber bundle.
```
NEW:
```
It is not a fiber bundle. For a linear projection onto an edge, let $s\in[0,1]$ be the point of the edge under the third vertex, where $\lambda$ attains its maximum. The fiber over an endpoint $x\neq s$ of the edge consists of the single vertex of $\Delta$ lying over $x$: it is the face of $\Delta$ on which the linear function $p$ attains its maximum (for $x=1$) or its minimum (for $x=0$), and the only vertex of $\Delta$ mapping to $x$ is that one. The fiber over an interior point of the edge is a nondegenerate closed interval, since $p$ takes the values $0$ and $1$ at the two endpoints of the edge and therefore takes values on both sides of any interior value. These fibers are not homeomorphic, whereas all fibers of a bundle over the connected edge would be homeomorphic. Hence $p$ is not a fiber bundle.
```
WHY: The claim that both endpoint fibres are points fails when the third vertex projects to an endpoint of the edge (e.g. `p(x,y) = x` on `conv{(0,0),(1,0),(0,1)}`, where the fibre over `0` is the edge `{(0,y)}`). The replacement states the correct general fact — one endpoint fibre is a single vertex, interior fibres are nondegenerate intervals — which still yields non-homeomorphic fibres, and hence "not a fibre bundle", for every linear projection.

## E-HAT-4.3-10 — `corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-10.md`

Book: AT 20781–20786. **Verdict: correct.**

- The construction is the standard one and every constraint is checked: on `S^n×{0} ∪ {*}×I` the data
  `α` and `β` agree at `(*,0) = e_0`; the composed map `(x,t) ↦ pβ(t)` extends their projections to
  `B`; a fibration has HLP with respect to every space (AT 18713), so the lift relative to that subspace
  exists; the end map `α_1` lands in `F` because `pα_1(x) = pβ(1) = b_0` and is based because
  `α̃(*,1) = β(1) = e_0`.
- Well-definedness up to homotopy of `α` and of `β` (singular cubes vary continuously, so homotopies
  transport, using the lift-extension property for the pairs `S^n×I×I` and `I×I`), the composition law
  `(βγ)·α = β·(γ·α)` by concatenating transport homotopies, and invertibility by reversing `β` are all
  stated with their mechanism. Terse, not missing.
- The composite `π_1(F) → π_1(E) → Aut(π_n(F))` is the usual action — the basepoint-change action
  `β_γ([f]) = [γf]` of AT 17055–17068 — because for `β` a loop in `F` the projection `pβ` is the constant
  path, so the lift is a homotopy within `F` moving the basepoint along `β`. `π_1(E) = 0` therefore gives
  the trivial action.
- Not spelled out, and standard enough not to be a defect: for `n ≥ 2` any continuous self-map of `F`
  induces a group homomorphism on `π_n`, and for `n = 1` the transport is likewise induced by a
  continuous self-map of `F`; that is what makes the target `Aut(π_n(F))` rather than the symmetric group.

## E-HAT-4.3-11 — `corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-11.md`

Book: AT 20790–20792; fiber homotopy equivalence, AT 20117–20121; pullback fibration, AT 20128–20135;
Proposition 4.62, AT 20137–20138. **Verdict: correct.**

- `f^*(E) = {(b,e) : f(b) = p(e)} → B_1` is a fibration (the pullback inherits HLP, AT 20131–20135), and
  pullback carries fiber-preserving maps and fiber homotopies to fiber-preserving maps and fiber homotopies
  (definitions AT 20117–20121), so `f^*` is well defined on `F(B_2)`.
- Homotopy invariance: pulling back along `H:B_1×I → B_2` and transporting along the interval is exactly
  the proof of Proposition 4.62 (AT 20137–20138), which states the two endpoint restrictions are fiber
  homotopy equivalent; the card names the mechanism (homotopy lifting property along the interval), so this
  is a legitimately compressed citation rather than an assertion.
- `(fg)^* = g^*f^*`; with `g` a homotopy inverse of `f:B_1→B_2`, `f^*g^* = (gf)^* = id_{F(B_1)}` and
  `g^*f^* = (fg)^* = id_{F(B_2)}` by homotopy invariance. Note the card's order is consistent with
  `f^*:F(B_2)→F(B_1)`. Hence `f^*` is a bijection when `f` is a homotopy equivalence.

## E-HAT-4.3-12 — `corpus/collections/SRC-TEXT-HAT02/4-3/E-HAT-4.3-12.md`

Book: AT 20793–20794; `E_f`, `p(a,γ) = γ(1)`, Proposition 4.64, AT 20169–20175. **Verdict: correct.**

- `Φ(a,γ) = (a, \overline{H_a}*γ)` is a point of `E_g` (the concatenated path starts at `g(a)`) and is
  fibre-preserving over `B` because both concatenations end at `γ(1)`; `Ψ` is the same construction with
  `H_a` in place of `\overline{H_a}`.
- `ΨΦ` prepends the loop `H_a*\overline{H_a}` at `f(a)` and `ΦΨ` prepends `\overline{H_a}*H_a` at `g(a)`;
  contracting a loop at a point by the standard reparametrisation is jointly continuous in `(a,γ)`, and
  the endpoint of the resulting path is unchanged throughout, so the homotopies are fibre-preserving and
  cover the identity of `B`. That is precisely a fiber homotopy equivalence in the sense of AT 20117–20121.

---

## Closing

**Cards read: 12 of 12** — `E-HAT-4.3-1` … `E-HAT-4.3-12` (slice 6, §4.3 exercises 1–12, AT 20755–20794).
**Cards not read: none** of the slice. Every card in the slice carries a proof; none is empty.
**Unverified: none.** Every step I had to check was settled against `tmp/hat/AT.txt`; both defective
verdicts rest on the book's own hypotheses (`4.3-5`) or on an explicit counterexample inside the card's
own coordinate model (`4.3-9`), not on the absence of sources.

Not reported as defects, and why: `E-HAT-4.3-1` writes `u` for the class it has just called `ν` (single
possible reading); `E-HAT-4.3-10` does not spell out that the transport is induced by a continuous
self-map of `F` (standard, and not needed for any step that is used); the remaining cards are terse but
each step either is proved, is a standard computation for a named space, or cites a numbered result whose
hypotheses hold here. No card in this slice is circular. Nothing under `corpus/` was modified.
