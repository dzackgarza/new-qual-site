# Findings — `SRC-TEXT-HAT02` (Hatcher, *Algebraic Topology*), §4.3

Auditor: member `m6` of swarm `smvy0zsoh` (direction `d2`). Slice: **§4.3 only**, all 24 cards.
Source of truth: `tmp/hat/AT.txt` (PDF `tmp/hat/AT.pdf`). Every statement about the book below is a verbatim quotation of `tmp/hat/AT.txt` with its line numbers, in the form `NNNNN: <text>`; the extraction's own line breaks, spacing and symbol renderings are preserved, because that file is the only witness in the repository.
`corpus/` was not modified.

---

## 0. Scope and card count

Cards per section of the unread slice, from `ls corpus/collections/SRC-TEXT-HAT02/`:

| section dir | cards | audited here |
| --- | --- | --- |
| `3-d` | 3 | no — member `m3` (`d1`) |
| `3-f` | 9 | no — `m4` (`d3`) |
| `3-h` | 6 | no — `m7` (`d4`) |
| `4-1` | 23 cards (exercises 1–23; 10–23 = 14 are in the unread part) | no — `m7` (`d4`) |
| `4-2` | 39 | no — `m8` (`d5`) |
| **`4-3`** | **24** | **yes — all 24, in full** |
| `4-a` 5, `4-b` 2, `4-d` 10, `4-f` 3, `4-g` 4, `4-h` 4, `4-i` 3, `4-k` 6, `4-l` 5 | 42 (nine additional-topic sections) | no — `m1` (`d6`) |
| **total unread** | **137** | **24 audited here** |

So the unread slice is 137 cards; this report covers 24 of them (§4.3), no sampling, and **no card of §4.3 is left unread**. The remaining 113 cards belong to the seven other members' slices and are not audited here; nothing in this file should be read as a verdict on them.

The printed §4.3 exercise block is `tmp/hat/AT.txt` lines **20754–20830**: heading `Exercises` on 20754, exercise 1 starting on 20755, exercise 24 ending on 20830; the §4.A page begins at 20831.

### Extraction caveat used throughout

`AT.txt` renders two-line displayed formulas of the exercise list on the *math* line and leaves the prose line broken, and for exercise 1 the two pieces come out in the wrong vertical order (20755–20758). I quote the file exactly and, where the order is perturbed, say what the printed page must read. No verdict below depends on a reordering: each card is compared with the file's words, and the one place where the card's reading could be contested (exercise 1) is discussed explicitly. As a check on the extraction only (never as a citation), I also ran `pdftotext` on `tmp/hat/AT.pdf` for the printed pages 419–420 and compared the whole exercise block: it agrees with `AT.txt` word for word, including the five bracketed hints, the `iff` of exercise 22 and the reading of exercise 1 used below. Every reference in this report is nevertheless a line number of `tmp/hat/AT.txt`.

### Method

For each of the 24 cards I read the whole `.md` file (frontmatter, statement, solution), then:

1. **Statement** — compared word by word with the printed exercise, including quantifiers, hypotheses, exponents vs. subscripts, both halves of every "iff", and every bracketed hint. A token-level multiset diff of the book block against the card's `{.problem}` block was run as a check for dropped words; every hit was then verified by hand. Differences appear below with both quotations.
2. **Proof** — read line by line. Every cited result was checked against its printed hypotheses, in this file:
   - Theorem 4.57 and the fundamental class — `AT.txt:19541–19543`, `19549–19555`, and the non-basepointed form at `19556–19561`;
   - definition of fibration and of relative HLP — `18713–18714`, `18728–18740`;
   - `E_f`, Proposition 4.64, deformation retraction onto `A`, homotopy fibre — `20167–20175`, `20193–20200`, `20274–20276`;
   - Postnikov condition (3) `fibre K(π_n X, n)` — `20331`;
   - definition of principal fibration, k-invariants — `20431–20437`;
   - obstructions of the relative lifting problem — `20732–20734`;
   - Corollary 4.73 — `20688–20690`; Proposition 4.74 — `20703–20704`;
   - Proposition 4.18 (functoriality of `n`-connected CW models) — `17684–17690`;
   - H-space definition — `13964–13968`; Corollary 0.21 — `997–999`.

Verdict vocabulary: **statement matches** / **statement differs** (with book vs. card quotes) / **proof correct** / **proof has a gap** (with the exact step and why). Where a proof is right but one step is compressed, I say so and do not call it a gap unless the step is missing rather than merely short.

---

## 1. Verdicts at a glance

| card | statement | proof |
| --- | --- | --- |
| E-HAT-4.3-1 | matches | correct |
| E-HAT-4.3-2 | matches | correct |
| E-HAT-4.3-3 | matches | correct |
| E-HAT-4.3-4 | matches | correct (one terse step) |
| E-HAT-4.3-5 | **differs — hint dropped** | correct, central step a black box |
| E-HAT-4.3-6 | matches | correct, one compressed step |
| E-HAT-4.3-7 | matches | correct (symbol slip `ν`/`u`) |
| E-HAT-4.3-8 | matches | correct |
| E-HAT-4.3-9 | **differs — hint dropped** | correct |
| E-HAT-4.3-10 | matches | correct, one unargued step |
| E-HAT-4.3-11 | matches | correct |
| E-HAT-4.3-12 | matches | correct |
| E-HAT-4.3-13 | **differs — hint dropped** | correct |
| E-HAT-4.3-14 | **differs — hint dropped** | correct |
| E-HAT-4.3-15 | matches | correct |
| E-HAT-4.3-16 | matches | correct |
| E-HAT-4.3-17 | matches | correct |
| E-HAT-4.3-18 | matches | correct |
| E-HAT-4.3-19 | matches | correct (transport `F→F_p` left implicit) |
| E-HAT-4.3-20 | matches | **gap — one false sentence**, conclusion survives |
| E-HAT-4.3-21 | matches | correct (cites an unnumbered standard fact) |
| E-HAT-4.3-22 | **differs — "iff" weakened to "if"** | **gap — only one direction proved** |
| E-HAT-4.3-23 | **differs — hint dropped** | correct modulo one unstated hypothesis check |
| E-HAT-4.3-24 | matches | **gap — no proof; seven placeholder proofs** |

Six cards have statement defects (5, 9, 13, 14, 22, 23); three proofs have defects that matter (24, 22, 20); seven proofs are correct but leave one step terse, uncited or unstated (4, 5, 6, 10, 19, 21, 23); the remaining fourteen proofs are complete.

---

## 2. Card-by-card

Notation: "⟨X,Y⟩" in the cards is the corpus's rendering of Hatcher's `hX, Y i` (basepointed homotopy classes); I treat that as a house convention and not a statement difference. Exercise numbers are carried by the card id, not by the statement text, so their absence from the statement is not a difference.

### E-HAT-4.3-1 — Exercise 1

**Book (`AT.txt:20755–20758`).**
```
20755: 1. Show there is a map RP∞ →CP∞ = K(Z, 2) which induces the trivial map on
20756: H                                  e ∗ (−; Z) . How is this consistent with the universal
20757: e ∗ (−; Z) but a nontrivial map on H
20758: coefficient theorem?
```

**Card statement.**
```
Show there is a map $\RP^\infty \to \CP^\infty = K(\ZZ, 2)$ which induces the trivial map on $\tilde{H}_*(-; \ZZ)$ but a nontrivial map on $\tilde{H}^*(-; \ZZ)$.
How is this consistent with the universal coefficient theorem?
```

**STATEMENT: matches.** The content is identical: the trivial map on `H̃_*(-;Z)`, a nontrivial map on `H̃^*(-;Z)`, and the question "How is this consistent with the universal coefficient theorem?" Note only that in the file the two halves of the two-line formula are out of vertical order — line 20756 ends "How is this consistent with the universal" and line 20757 carries "e ∗ (−; Z) but a nontrivial map on H" — so the block reads jumbled; the card has the printed reading (PDF p. 419).

**PROOF: correct.** Checked step by step. (i) `[RP^∞, K(Z,2)] ≅ H^2(RP^∞;Z)` is Theorem 4.57 with `X = RP^∞`, a CW complex, `T([f]) = f^*(α)` (`AT.txt:19541–19543`). (ii) The nonzero `u ∈ H^2(RP^∞;Z) ≅ Z/2` is realised by `f` with `f^*(c) = u ≠ 0`, so `f^*` is nontrivial on reduced cohomology. (iii) `H̃_i(RP^∞;Z) = Z/2` for `i` odd and `0` for `i` even, while `H_i(CP^∞;Z) = 0` for `i` odd; hence every `f_*: H̃_i(RP^∞) → H̃_i(CP^∞)` is zero. (iv) The universal-coefficient sequence in degree 2 for `RP^∞` is `0 → Ext(H_1(RP^∞),Z) → H^2(RP^∞;Z) → Hom(H_2(RP^∞),Z) → 0`, i.e. `0 → Z/2 → Z/2 → 0 → 0`, while for `CP^∞` the same sequence is `0 → Ext(0,Z) → H^2(CP^∞;Z) → Hom(Z,Z) → 0`, so `H^2(CP^∞;Z) ≅ Hom(Z,Z) = Z` and its generator is a Hom-class; the class `f^*(c)` is carried by the `Ext` term of `RP^∞`. The card's remark that the sequence is natural but its splitting is not is exactly the reason `f_* = 0` and `f^* ≠ 0` coexist. No step of the card goes outside its hypotheses.

### E-HAT-4.3-2 — Exercise 2

**Book (`AT.txt:20759–20761`).**
```
20759: 2. Show that the group structure on S 1 coming from multiplication in C induces a
20760: group structure on hX, S 1 i such that the bijection hX, S 1 i→H 1 (X; Z) of Theorem 4.57
20761: is an isomorphism.
```

**Card statement.**
```
Show that the group structure on $S^1$ coming from multiplication in $\CC$ induces a group structure on $\langle X, S^1 \rangle$ such that the bijection $\langle X, S^1 \rangle \to H^1(X; \ZZ)$ of Theorem 4.57 is an isomorphism.
```

**STATEMENT: matches.**

**PROOF: correct.** Pointwise multiplication `(fg)(x) = f(x)g(x)` and `f̄(x) = \overline{f(x)}` make `⟨X,S^1⟩` a group because `S^1 ⊂ C` is a topological group, so the axioms hold on the nose before passing to homotopy classes. The key identity `μ^*(u) = pr_1^*u + pr_2^*u` is right: `H^1(S^1×S^1;Z)` is free on `pr_1^*u, pr_2^*u` (Künneth, both factors have free finitely generated cohomology) and the two restrictions of `μ` are the identity, hence of degree 1. Naturality of `f ↦ f^*` gives `(fg)^*u = f^*u + g^*u`. Theorem 4.57 (`AT.txt:19541–19543`) says `T([f]) = f^*(α)` is a bijection, so this identity says precisely that `T` is an isomorphism of groups. (Theorem 4.57 is stated for CW `X`; the exercise, like the card, leaves that to the section's standing hypothesis, so there is no card-vs-book difference — but a reader needs `X` a CW complex.)

### E-HAT-4.3-3 — Exercise 3

**Book (`AT.txt:20762–20764`).**
```
20762: 3. Suppose that a CW complex X contains a subcomplex S 1 such that the inclusion
20763: S 1 ֓ X induces an injection H1 (S 1 ; Z)→H1 (X; Z) with image a direct summand of
20764: H1 (X; Z) . Show that S 1 is a retract of X .
```

**Card statement.**
```
Suppose that a CW complex $X$ contains a subcomplex $S^1$ such that the inclusion $S^1 \hookrightarrow X$ induces an injection $H_1(S^1; \ZZ) \to H_1(X; \ZZ)$ with image a direct summand of $H_1(X; \ZZ)$.
Show that $S^1$ is a retract of $X$.
```

**STATEMENT: matches.**

**PROOF: correct.** (i) `λ: H_1(X;Z) → Z` with `λ i_* = id` exists because `i_*(H_1(S^1;Z)) ≅ Z` is a direct summand: split `H_1(X) = i_*(H_1(S^1)) ⊕ K` and invert `i_*` on the first summand. (ii) `H^1(X;Z) ≅ Hom(H_1(X),Z)` by UCT, `Ext(H_0(X),Z) = 0`. (iii) Theorem 4.57 applies to the CW complex `X` and gives `r: X → S^1` with `r^*(ι) = u`; then `(ri)^*ι = i^*u = ι`, so `ri` has degree 1. (iv) A map `S^1 → S^1` of degree 1 is homotopic to the identity (unbased homotopy suffices, and is what is available here), and the homotopy extension property of the CW pair `(X, S^1)` extends that homotopy of `r|_{S^1} = ri` to a homotopy of `r` ending at `r'` with `r'i = id`. Nothing in the argument needs a basepoint, which matters: degree 1 alone does not give a based homotopy. Sound.

### E-HAT-4.3-4 — Exercise 4

**Book (`AT.txt:20765–20767`).**
```
20765: 4. Given abelian groups G and H and CW complexes K(G, n) and K(H, n) , show
20766: that the map hK(G, n), K(H, n)i→ Hom(G, H) sending a homotopy class [f ] to the
20767: induced homomorphism f∗ : πn (K(G, n))→πn (K(H, n)) is a bijection.
```

**Card statement.**
```
Given abelian groups $G$ and $H$ and CW complexes $K(G, n)$ and $K(H, n)$, show that the map $\langle K(G, n), K(H, n) \rangle \to \operatorname{Hom}(G, H)$ sending a homotopy class $[f]$ to the induced homomorphism $f_*: \pi_n(K(G, n)) \to \pi_n(K(H, n))$ is a bijection.
```

**STATEMENT: matches.**

**PROOF: correct.** (i) `⟨K(G,n),K(H,n)⟩ ≅ H^n(K(G,n);H)`: Theorem 4.57 with `X = K(G,n)`, a CW complex. (ii) Hurewicz: `K(G,n)` is `(n−1)`-connected, so `H_n(K(G,n);Z) ≅ π_n ≅ G` (for `n = 1`, `H_1 ≅ π_1^{ab} = G`, which is abelian by hypothesis). (iii) UCT: `0 → Ext(H_{n−1},H) → H^n → Hom(H_n,H) → 0` has `Ext = 0` because `H_{n−1}(K(G,n)) = 0` for `n > 1` and `H_0(K(G,1)) = Z` is free — the card checks both cases. (iv) The final step, that the class corresponds to `f_*` on `π_n`, is Hatcher's own description of the fundamental class: `α ∈ H^n(K(G,n);G) ≈ Hom(H_n(K;Z),G)` is "given by the inverse of the Hurewicz isomorphism `G = π_n(K(G,n))→H_n(K;Z)`" (`AT.txt:19549–19555`), so pairing `f^*(α)` with `H_n(K(G,n))` recovers exactly `f_*` after Hurewicz on both ends. The card's one sentence "by naturality of Hurewicz and of the representing cohomology class" names the right two facts; the step is true and traceable to the book. Not a gap, but it is the one place in this proof a reader must supply.

### E-HAT-4.3-5 — Exercise 5

**Book (`AT.txt:20768–20769`).**
```
20768: 5. Show that [X, S n ] ≈ H n (X; Z) if X is an n dimensional CW complex. [Build a
20769: K(Z, n) from S n by attaching cells of dimension ≥ n + 2 .]
```

**Card statement.**
```
Show that $[X, S^n] \approx H^n(X; \ZZ)$ if $X$ is an $n$-dimensional CW complex.
```

**STATEMENT: differs — the printed bracketed hint is dropped.** Book: "`[Build a K(Z, n) from S n by attaching cells of dimension ≥ n + 2 .]`" (lines 20768–20769). Card: no bracketed hint at all; the statement stops after "if $X$ is an $n$-dimensional CW complex."

**PROOF: correct, with one black-box step.** (i) `j: S^n → K(Z,n)` representing the generator is an `n`-equivalence: both spaces have `π_i = 0` for `i < n` and `j_*: π_n(S^n) → π_n(K(Z,n)) = Z` is an isomorphism. (ii) The card's central step — "obstruction theory or cellular induction says that an `n`-equivalence of targets induces a bijection `j_*: [X,S^n] ≅ [X,K(Z,n)]`" — is a true standard theorem for `dim X ≤ n`, so the proof is not wrong. But it is invoked without proof, and the dropped hint is exactly the elementary substitute: build `K(Z,n)` from `S^n` by cells of dimension `≥ n+2`, making the inclusion an `(n+1)`-equivalence, and push a map from the `n`-dimensional `X` off the higher cells by cellular approximation. (iii) `[X,K(Z,n)] ≅ H^n(X;Z)` is Theorem 4.57 in its non-basepointed form, which Hatcher states explicitly: "The theorem also holds with `hX, K(G, n)i` replaced by `[X, K(G, n)]`" (`AT.txt:19556–19561`). So the last step is properly supported.

### E-HAT-4.3-6 — Exercise 6

**Book (`AT.txt:20770–20773`).**
```
20770: 6. Use Exercise 4 to construct a multiplication map µ : K(G, n)× K(G, n)→K(G, n) for
20771: any abelian group G , making a CW complex K(G, n) into an H–space whose multipli-
20772: cation is commutative and associative up to homotopy and has a homotopy inverse.
20773: Show also that the H–space multiplication µ is unique up to homotopy.
```

**Card statement.**
```
Use Exercise 4 to construct a multiplication map $\mu: K(G, n) \times K(G, n) \to K(G, n)$ for any abelian group $G$, making a CW complex $K(G, n)$ into an H-space whose multiplication is commutative and associative up to homotopy and has a homotopy inverse.
Show also that the H-space multiplication $\mu$ is unique up to homotopy.
```

**STATEMENT: matches.**

**PROOF: correct, with one compressed step.** `K(G,n)×K(G,n)` is a `K(G⊕G,n)` and a CW complex, so Exercise 4 classifies maps `K×K → K` by `Hom(G⊕G,G)`; the map `μ` for `(a,b) ↦ a+b` restricts on each factor to a map inducing the identity on `π_n`, hence homotopic to the identity (again Exercise 4), so `μ` is an H-space multiplication with identity `e`; `μ(μ×1)` and `μ(1×μ)` both induce `(a,b,c) ↦ a+b+c`, so they are homotopic; `μ` and `μτ` both induce `a+b`, so the multiplication is homotopy-commutative. For uniqueness the card uses Hatcher's definition: an H-space multiplication comes with `e` such that `x ↦ µ(x,e)` and `x ↦ µ(e,x)` are homotopic to the identity through maps `(X,e)→(X,e)` (`AT.txt:13964–13968`), so the restriction to each factor induces the identity on `G` and hence `G⊕G → G` is addition; Exercise 4 then makes any such `μ` homotopic to the constructed one.

*Compressed step:* "The map corresponding to `a ↦ −a` is a homotopy inverse." That map has type `K → K`; a homotopy inverse for `μ` must be tested through the diagonal, i.e. one must observe that `µ∘(id×ν)∘Δ: K → K×K → K` and `µ∘(ν×id)∘Δ` induce `a ↦ a + (−a) = 0`, hence are homotopic to the constant map at `e` because Exercise 4 gives `[K,K] ≅ Hom(G,G)`. The card never writes the composite. True, and a one-line repair, but as printed the step does not by itself show what it claims.

### E-HAT-4.3-7 — Exercise 7

**Book (`AT.txt:20774–20776`).**
```
20774: 7. Using an H–space multiplication µ on K(G, n) , define an addition in hX, K(G, n)i
20775: by [f ] + [g] = [µ(f , g)] and show that under the bijection H n (X; G) ≈ hX, K(G, n)i
20776: this addition corresponds to the usual addition in cohomology.
```

**Card statement.**
```
Using an H-space multiplication $\mu$ on $K(G, n)$, define an addition in $\langle X, K(G, n) \rangle$ by $[f] + [g] = [\mu(f, g)]$ and show that under the bijection $H^n(X; G) \approx \langle X, K(G, n) \rangle$ this addition corresponds to the usual addition in cohomology.
```

**STATEMENT: matches.**

**PROOF: correct.** With `u` the fundamental class, the identification `H^n(K×K;G) ≅ Hom(H_n(K×K),G) = Hom(G⊕G,G)` of Exercise 4's proof sends `μ^*u` to the homomorphism induced by `μ` on `π_n = G⊕G`, which is addition (Exercise 6); `pr_1^*u` and `pr_2^*u` correspond to the two projections, so `μ^*u = pr_1^*u + pr_2^*u`; then `(μ(f,g))^*u = (f,g)^*μ^*u = f^*u + g^*u`, and `T([f]) = f^*u` (`AT.txt:19541–19543`) turns this into the statement that the defined addition is cohomology addition. `⟨X,K(G,n)⟩` thereby becomes a group and `T` a group isomorphism — which also takes care of well-definedness of `[f]+[g]`.

*Symbol slip (cosmetic):* the fundamental class is introduced as `\nu` in the displayed formula `\nu\in H^n(K(G,n);G)` and then called `u` in every subsequent formula (`\mu^*u`, `f^*u`). One symbol, two names.

### E-HAT-4.3-8 — Exercise 8

**Book (`AT.txt:20777–20778`).**
```
20777: 8. Show that a map p : E →B is a fibration iff the map π : E I →Ep , π (γ) = (γ(0), pγ) ,
20778: has a section, that is, a map s : Ep →E I such that π s = 11.
```

**Card statement.**
```
Show that a map $p: E \to B$ is a fibration if and only if the map $\pi: E^I \to E_p$, $\pi(\gamma) = (\gamma(0), p\gamma)$ has a section, that is, a map $s: E_p \to E^I$ such that $\pi s = \id$.
```

**STATEMENT: matches.** "iff" is written out as "if and only if"; "π s = 11" (Hatcher's identity map) is written `\pi s = \id`. Both are faithful.

**PROOF: correct.** (⇒, a section gives the HLP): for a lifting problem `f: X→E`, `H: X×I→B` with `H(-,0) = pf`, the map `x ↦ (f(x), H_x)` lands in `E_p` because `H_x(0) = H(x,0) = pf(x)`, and it is continuous by the exponential law (`AT.txt:20169–20173`, Proposition A.14, which the book uses for exactly this); `H̃(x,t) = s(f(x),H_x)(t)` then satisfies `H̃(-,0) = f` and `p H̃ = H`. Since Hatcher defines a fibration as having the HLP with respect to **all** spaces (`AT.txt:18713–18714`), `p` is a fibration. (⇐, a fibration gives a section): with `q(e,α) = e` and `K((e,α),t) = α(t)` one has `K(-,0) = pq`, so the HLP applies — to the space `E_p`, which is legitimate for the same reason — and `s(e,α)(t) = K̃((e,α),t)` satisfies `s(e,α)(0) = e` and `p s(e,α) = α`, i.e. `π s = id`. Continuity of `s` is continuity of the adjoint. Correct in both directions.

### E-HAT-4.3-9 — Exercise 9

**Book (`AT.txt:20779–20780`).**
```
20779: 9. Show that a linear projection of a 2 simplex onto one of its edges is a fibration but
20780: not a fiber bundle. [Use the preceding problem.]
```

**Card statement.**
```
Show that a linear projection of a 2-simplex onto one of its edges is a fibration but not a fiber bundle.
```

**STATEMENT: differs — the printed bracketed hint is dropped.** Book: "`[Use the preceding problem.]`" (line 20780). The card's statement ends after "not a fiber bundle."

**PROOF: correct.** After an affine change of coordinates the projection is `p(x,y) = x` on `Δ = {(x,y) : 0 ≤ x ≤ 1, 0 ≤ y ≤ λ(x)}` with `λ ≥ 0` continuous (for a linear projection onto the edge, `λ` is the piecewise-linear width function, vanishing at both ends) — that is the correct normal form. `r(x,y) = (x, min{y,λ(x)})` is continuous, fiber-preserving over `I`, and the identity on `Δ`. The trivial bundle `I×[0,M] → I` is a fibration (`AT.txt:18714–18717`: "a projection `B × F →B` is a fibration"), and a fiberwise retract of a fibration is a fibration: lift the base homotopy in `I×[0,M]` keeping the second coordinate of the given lift (legitimate, by the same formula), then apply `r`. Hence `p` is a fibration. Not a bundle: the fibre over an endpoint of the edge is a single point (a point of the triangle whose image is a vertex, with the third vertex mapping to an interior point, must be that vertex), the fibre over an interior point is a nondegenerate closed interval, and a fibre bundle over the connected base `I` has homeomorphic fibres. Correct. (The card does not need the dropped hint, nor Exercise 8, which the hint points to.)

### E-HAT-4.3-10 — Exercise 10

**Book (`AT.txt:20781–20786`).**
```
20781: 10. Given a fibration F →E →B , use the homotopy lifting property to define an action
20782:                                                            
20783: of π1 (E) on πn (F ) , a homomorphism π1 (E)→Aut πn (F ) , such that the composi-
20784:                                  
20785: tion π1 (F )→π1 (E)→Aut πn (F ) is the usual action of π1 (F ) on πn (F ) . Deduce
20786: that if π1 (E) = 0 , then the action of π1 (F ) on πn (F ) is trivial.
```

**Card statement.**
```
Given a fibration $F \to E \to B$, use the homotopy lifting property to define an action of $\pi_1(E)$ on $\pi_n(F)$, a homomorphism $\pi_1(E) \to \operatorname{Aut}\bigl(\pi_n(F)\bigr)$, such that the composition $\pi_1(F) \to \pi_1(E) \to \operatorname{Aut}\bigl(\pi_n(F)\bigr)$ is the usual action of $\pi_1(F)$ on $\pi_n(F)$.
Deduce that if $\pi_1(E) = 0$, then the action of $\pi_1(F)$ on $\pi_n(F)$ is trivial.
```

**STATEMENT: matches.** (`\u0001` on 20782 and 20784 is a glyph the extraction lost; it is the parenthesis around `π_n (F )`, as the card renders it.)

**PROOF: correct in substance, with one unargued step.** The relative HLP is available for the CW pair `(S^n×I, S^n×{0} ∪ {*}×I)` (`AT.txt:18728–18740`), and the prescription (α on `S^n×{0}`, β on `{*}×I`) projects consistently to `(x,t) ↦ pβ(t)` because `pα ≡ b_0 = pβ(0)`; the end of the lift lies in `F` and is based at `β(1) = e_0`, so `[β]·[α]` is well defined; homotopies of `α` and `β` give homotopies of `α_1`; `(βγ)·α = β·(γ·α)`; reversal of `β` inverts; for `β` a loop in `F` the lift stays in `F`, so `α_1` is `β·α` under the usual action and the composite `π_1(F)→π_1(E)→Aut π_n(F)` is the usual action; when `π_1(E) = 0` that composite is trivial.

*Unargued step:* "reversing `β` gives the inverse automorphism. Thus `π_1(E,e_0)→Aut(π_n(F,e_0))` is a homomorphism." Invertibility of `[α] ↦ [β]·[α]` does not by itself make it a homomorphism of `π_n(F,e_0)`; for that one needs the (true) fact that the assignment is induced by the transport map `F → F`, `x ↦` endpoint of the lift starting at `x`, which is a homotopy equivalence of `F` and therefore a group homomorphism on `π_n`. The card asserts the conclusion and omits this one sentence.

### E-HAT-4.3-11 — Exercise 11

**Book (`AT.txt:20790–20792`).**
```
20790: 11. For a space B , let F(B) be the set of fiber homotopy equivalence classes of fibra-
20791: tions E →B . Show that a map f : B1 →B2 induces f ∗ : F(B2 )→F(B1 ) depending only
20792: on the homotopy class of f , with f ∗ a bijection if f is a homotopy equivalence.
```

**Card statement.**
```
For a space $B$, let $\mathcal{F}(B)$ be the set of fiber homotopy equivalence classes of fibrations $E \to B$.
Show that a map $f: B_1 \to B_2$ induces $f^*: \mathcal{F}(B_2) \to \mathcal{F}(B_1)$ depending only on the homotopy class of $f$, with $f^*$ a bijection if $f$ is a homotopy equivalence.
```

**STATEMENT: matches.**

**PROOF: correct.** Pullback of a fibration is a fibration; pullback sends fiber-preserving maps and fiber homotopies to such, hence sends fiber homotopy equivalences to fiber homotopy equivalences, so `f^*` is well defined on `F(B_2)`. If `f_0 ≃ f_1` through `H: B_1×I → B_2`, then `H^*E → B_1×I` restricts to `f_0^*E` and `f_1^*E` at the two ends, and the HLP for the fibration over `B_1×I` produces fiberwise homotopy equivalences between the two restrictions, mutually inverse (run the argument with the reversed interval). Functoriality `(fg)^* = g^*f^*` holds for pullbacks. For `f` a homotopy equivalence with inverse `g`, `f^*g^* = (gf)^* = 1` and `g^*f^* = (fg)^* = 1` by homotopy invariance, so `f^*` is a bijection. All steps check out.

### E-HAT-4.3-12 — Exercise 12

**Book (`AT.txt:20793–20794`).**
```
20793: 12. Show that for homotopic maps f , g : A→B the fibrations Ef →B and Eg →B are
20794: fiber homotopy equivalent.
```

**Card statement.**
```
Show that for homotopic maps $f, g: A \to B$ the fibrations $E_f \to B$ and $E_g \to B$ are fiber homotopy equivalent.
```

**STATEMENT: matches.**

**PROOF: correct.** The card's recollection of `E_f` matches Hatcher exactly: "let `Ef` be the space of pairs `(a, γ)` where `a ∈ A` and `γ : I →B` is a path in `B` with `γ(0) = f (a)`", `p(a,γ) = γ(1)` (`AT.txt:20167–20175`, Proposition 4.64). For `(a,γ) ∈ E_f`, `H̄_a * γ` runs from `g(a)` to `γ(1)`, so `Φ` is well defined and fiber-preserving; `Ψ` is `(a,γ) ↦ (a, H_a * γ)`. The composites prepend `H_a * H̄_a` resp. `H̄_a * H_a` — the card states the two in the right order — which contract to constant paths by the standard reparametrization, continuously in `a`, and the homotopy keeps the first coordinate `a` and the endpoint fixed, so it is a fiber homotopy over `B`. Correct.

### E-HAT-4.3-13 — Exercise 13

**Book (`AT.txt:20795–20797`).**
```
20795: 13. Given a map f : A→B and a homotopy equivalence g : C →A , show that the fi-
20796: brations Ef →B and Ef g →B are fiber homotopy equivalent. [One approach is to use
20797: Corollary 0.21 to reduce to the case of deformation retractions.]
```

**Card statement.**
```
Given a map $f: A \to B$ and a homotopy equivalence $g: C \to A$, show that the fibrations $E_f \to B$ and $E_{fg} \to B$ are fiber homotopy equivalent.
```

**STATEMENT: differs — the printed bracketed hint is dropped.** Book: "`[One approach is to use Corollary 0.21 to reduce to the case of deformation retractions.]`" (lines 20796–20797). The card's statement ends after "are fiber homotopy equivalent."

**PROOF: correct.** `Φ(c,γ) = (g(c),γ)` is well defined because `γ(0) = fg(c)`, and fiber-preserving. `Ψ(a,γ) = (h(a), fK_a * γ)` is well defined because `fK_a` runs from `fgh(a) = fg(h(a))` to `f(a)` and `γ` continues from `f(a)` to `γ(1)`; the endpoint is preserved. `ΦΨ(a,γ) = (gh(a), fK_a * γ)`, and `(a,γ) ↦ (K(a,t), fK_a|_{[t,1]} * γ)` is a homotopy in `E_f` from `ΦΨ` to the identity (the first coordinate is allowed to move; the second coordinate starts at `f(K(a,t))`, as required); `ΨΦ` is treated the same way with `hg ≃ 1_C`. So the two fibrations are fiber homotopy equivalent. The card's sketch asserts exactly these homotopies. Correct.

### E-HAT-4.3-14 — Exercise 14

**Book (`AT.txt:20798–20801`).**
```
20798: 14. For a space B , let M(B) denote the set of equivalence classes of maps f : A→B
20799: where f1 : A1 →B is equivalent to f2 : A2 →B if there exists a homotopy equivalence
20800: g : A1 →A2 such that f1 ≃ f2 g . Show the natural map F(B)→M(B) is a bijection.
20801: [See Exercises 11 and 13.]
```

**Card statement.**
```
For a space $B$, let $\mathcal{M}(B)$ denote the set of equivalence classes of maps $f: A \to B$ where $f_1: A_1 \to B$ is equivalent to $f_2: A_2 \to B$ if there exists a homotopy equivalence $g: A_1 \to A_2$ such that $f_1 \simeq f_2 g$.
Show the natural map $\mathcal{F}(B) \to \mathcal{M}(B)$ is a bijection.
```

**STATEMENT: differs — the printed bracketed hint is dropped.** Book: "`[See Exercises 11 and 13.]`" (line 20801). The card's statement ends after "is a bijection."

**PROOF: correct.** Well definedness: a fiber homotopy equivalence is a homotopy equivalence of total spaces with `p_1 ≃ p_2 g`, so it identifies the classes in `M(B)`; conversely the construction below is the inverse. Surjectivity: for `f: A → B`, `E_f → B` is a fibration (Proposition 4.64, `AT.txt:20175`) and `A ⊂ E_f` is a deformation retract ("`Ef` deformation retracts onto this subspace by restricting all the paths `γ` to shorter and shorter initial segments", `AT.txt:20193–20198`), so `A → E_f` is a homotopy equivalence and `p_f i = f`; hence `f` and `p_f` define the same element of `M(B)`. Injectivity: `p_1 ≃ p_2 g` with `g: E_1→E_2` a homotopy equivalence gives `E_{p_1} ≃_f E_{p_2 g}` (Exercise 12, i.e. card E-HAT-4.3-12) and `E_{p_2 g} ≃_f E_{p_2}` (Exercise 13, card E-HAT-4.3-13), and each `p_i` is fiber homotopy equivalent to its mapping-path replacement. Correct.

*Note on the citation:* the card's proof cites Exercises 12 and 13, while the printed hint says 11 and 13. Exercise 12 is exactly the homotopy-invariance case that is used here, so the card's citation is mathematically sound; the defect is only that the printed hint is absent from the statement (see the summary).

### E-HAT-4.3-15 — Exercise 15

**Book (`AT.txt:20802–20803`).**
```
20802: 15. If the fibration p : E →B is a homotopy equivalence, show that p is a fiber homo-
20803: topy equivalence of E with the trivial fibration 11 : B →B .
```

**Card statement.**
```
If the fibration $p: E \to B$ is a homotopy equivalence, show that $p$ is a fiber homotopy equivalence of $E$ with the trivial fibration $\id: B \to B$.
```

**STATEMENT: matches.** (`\id` for Hatcher's `11`.)

**PROOF: correct, given Exercise 14 (card E-HAT-4.3-14).** In `M(B)` the map `p: E → B` and the identity `1_B: B → B` are equivalent with `g = p`: it is a homotopy equivalence by hypothesis and `p = 1_B ∘ p` holds strictly. The bijection `F(B) → M(B)` of Exercise 14 then says `p` and `1_B` lie in the same class of `F(B)`, i.e. `p` is fiber homotopy equivalent to the trivial fibration `1_B: B→B`. Correct — its only dependency is Exercise 14, whose card (E-HAT-4.3-14) I verified above.

### E-HAT-4.3-16 — Exercise 16

**Book (`AT.txt:20804–20806`).**
```
20804: 16. Show that a map f : X →Y of connected CW complexes is a homotopy equivalence
20805:                                                                  e ∗ (Ff ; Z) = 0 .
20806: if it induces an isomorphism on π1 and its homotopy fiber Ff has H
```

**Card statement.**
```
Show that a map $f: X \to Y$ of connected CW complexes is a homotopy equivalence if it induces an isomorphism on $\pi_1$ and its homotopy fiber $F_f$ has $\tilde{H}_*(F_f; \ZZ) = 0$.
```

**STATEMENT: matches.**

**PROOF: correct.** Replace `f` by the fibration `F_f → E_f → Y`, `E_f ≃ X` (`AT.txt:20193–20200`). `π_1(E_f) ≅ π_1(Y)` and the exact sequence give that `π_1(F_f) → π_1(E_f)` has trivial image. Exercise 10 (card E-HAT-4.3-10) says the usual action of `π_1(F_f)` on `π_n(F_f)` is the composite through `π_1(E_f)`, hence trivial; for `n = 1` that action is conjugation, so `π_1(F_f)` is abelian. `H̃_1(F_f;Z) = 0` is `H_1(F_f;Z) = 0` (the homotopy fibre is nonempty, and `H̃_0 = 0` is what makes it path connected), and `H_1 = π_1^{ab}`, so `π_1(F_f) = 0`. Then `F_f` is simply connected and acyclic; if `π_n(F_f) ≠ 0` for the least `n ≥ 2`, Hurewicz gives `π_n(F_f) ≅ H_n(F_f) = 0`, a contradiction, so all homotopy groups vanish and Whitehead gives `F_f ≃ *` (this needs `F_f` to have CW homotopy type, which the card states). The exact sequence then gives `π_n(E_f) ≅ π_n(Y)` in every degree, i.e. `f_*` iso on all homotopy groups, and Whitehead for connected CW complexes gives `f` a homotopy equivalence. The one lemma used without proof — that an acyclic simply connected space of CW homotopy type is contractible — is Whitehead's theorem itself. Correct.

### E-HAT-4.3-17 — Exercise 17

**Book (`AT.txt:20807`).**
```
20807: 17. Show that ΩX is an H–space with multiplication the composition of loops.
```

**Card statement.**
```
Show that $\Omega X$ is an H-space with multiplication the composition of loops.
```

**STATEMENT: matches.**

**PROOF: correct.** The concatenation formula is Hatcher's; the constant loop is a two-sided homotopy identity **through based maps** (reparametrizations fix the endpoints), which is exactly what Hatcher's definition of an H-space demands: `µ(x,e)` and `µ(e,x)` homotopic to the identity "through maps `(X, e)→(X, e)`" (`AT.txt:13964–13968`). Associativity up to homotopy through based loops by reparametrization, and loop reversal as a two-sided homotopy inverse, are both proved. The card proves more than the exercise asks (Hatcher's definition needs only the identity) and nothing false.

### E-HAT-4.3-18 — Exercise 18

**Book (`AT.txt:20808–20810`).**
```
20808: 18. Show that a fibration sequence ··· →ΩB →F →E →B induces a long exact se-
20809: quence ··· →hX, ΩBi→hX, F i→hX, Ei→hX, Bi , with groups and group homomor-
20810: phisms except for the last three terms, abelian groups except for the last six terms.
```

**Card statement.**
```
Show that a fibration sequence $\cdots \to \Omega B \to F \to E \to B$ induces a long exact sequence $\cdots \to \langle X, \Omega B \rangle \to \langle X, F \rangle \to \langle X, E \rangle \to \langle X, B \rangle$, with groups and group homomorphisms except for the last three terms, abelian groups except for the last six terms.
```

**STATEMENT: matches.**

**PROOF: correct.** Exactness of `⟨X,F⟩ → ⟨X,E⟩ → ⟨X,B⟩` as pointed sets: if `pf` is nullhomotopic, the HLP lifts a chosen nullhomotopy starting at `f`, and its end maps into `F`, so `[f]` is in the image from `⟨X,F⟩`; the composite is trivial since `p` is constant on `F`. Applying this to each looped fibration of `⋯ → ΩB → F → E → B` (Ω of a fibration is a fibration) gives the sequence. Groups: `⟨X,ΩK⟩` is a group under pointwise concatenation and maps induced by loop maps are homomorphisms, so every term except `⟨X,F⟩, ⟨X,E⟩, ⟨X,B⟩` is a group and the maps between the group terms are homomorphisms. Abelian: `⟨X,Ω^rK⟩` is abelian for `r ≥ 2` by Eckmann–Hilton; in `⋯ → ⟨X,Ω²B⟩ → ⟨X,ΩF⟩ → ⟨X,ΩE⟩ → ⟨X,ΩB⟩ → ⟨X,F⟩ → ⟨X,E⟩ → ⟨X,B⟩` the abelian terms are exactly all but the last six. The card's count coincides with the book's "abelian groups except for the last six terms". Correct.

### E-HAT-4.3-19 — Exercise 19

**Book (`AT.txt:20811–20816`).**
```
20811:                                 p
20812: 19. Given a fibration F -→ E --→ B , define a natural action of ΩB on the homotopy
20813: fiber Fp and use this to show that exactness at hX, F i in the long exact sequence in
20814: the preceding problem can be improved to the statement that two elements of hX, F i
20815: have the same image in hX, Ei iff they are in the same orbit of the induced action of
20816: hX, ΩBi on hX, F i .
```

**Card statement.**
```
Given a fibration $F \to E \xrightarrow{p} B$, define a natural action of $\Omega B$ on the homotopy fiber $F_p$ and use this to show that exactness at $\langle X, F \rangle$ in the long exact sequence in the preceding problem can be improved to the statement that two elements of $\langle X, F \rangle$ have the same image in $\langle X, E \rangle$ iff they are in the same orbit of the induced action of $\langle X, \Omega B \rangle$ on $\langle X, F \rangle$.
```

**STATEMENT: matches.** The lone `p` on line 20811 is the label printed above the pair of arrows of `F → E --p--> B`, i.e. the structure map `E → B`, which is how the card renders it; the PDF (printed p. 420) prints the same exercise with the same label placement.

**PROOF: correct.** The homotopy fibre is Hatcher's: "`Fp` consists of pairs `(e, γ)` with `e ∈ E` and `γ` a path in `B` from `p(e)` to `b0`" (`AT.txt:20274–20276`). `(e,γ)·λ = (e,γ·λ)` is well defined (γ·λ still ends at `b_0`) and is a right action on the nose, hence on homotopy classes; `(f·u)(x) = f(x)·u(x)` makes `⟨X,ΩB⟩` act on `⟨X,F_p⟩`, and at the basepoint the result is a reparametrized constant path, so the action is defined on based homotopy classes. Same orbit ⇒ same image: the action does not move the `E`-coordinate, so `i∘(f·u) = i∘f`. Same image ⇒ same orbit: given a based homotopy `H` from `f_E` to `g_E`, the path `η_{x,s}(t) = pH(x,(1−t)s)` runs from `pH(x,s)` to `pf_E(x)`, so `K(x,s) = (H(x,s), η_{x,s}·α_x)` is a based homotopy in `F_p` from `f` to `x ↦ (g_E(x), η_{x,1}·α_x)`; then `λ(x) = β̄_x·η_{x,1}·α_x` is a loop at `b_0` — `β̄_x` from `b_0` to `pg_E(x)`, `η_{x,1}` from `pg_E(x)` to `pf_E(x)`, `α_x` from `pf_E(x)` to `b_0` — and is based, and `g·λ = (g_E, β_x·β̄_x·η_{x,1}·α_x) ≃ (g_E, η_{x,1}·α_x) ≃ f` because `β_x·β̄_x` contracts to a constant path naturally in `x`. Both directions are correct.

*Minor, not a gap:* the action is built on `F_p` while the exercise speaks of `⟨X,F⟩`; the card transports along the inclusion `F → F_p`, `e ↦ (e,const)`, which the book says is a homotopy equivalence (`AT.txt:20274–20275`) and which satisfies `i∘j = id_F`, so the transport is legitimate and compatible with the maps to `⟨X,E⟩`. The transported action itself is never written down.

### E-HAT-4.3-20 — Exercise 20

**Book (`AT.txt:20817–20818`).**
```
20817: 20. Show that by applying the loopspace functor to a Postnikov tower for X one
20818: obtains a Postnikov tower of principal fibrations for ΩX .
```

**Card statement.**
```
Show that by applying the loop space functor to a Postnikov tower for $X$ one obtains a Postnikov tower of principal fibrations for $\Omega X$.
```

**STATEMENT: matches.** ("loop space" for the book's "loopspace".)

**PROOF: has a gap — one sentence is false.** Exact step, quoted from the card: "Equivalently, the three-term sequence $\Omega X_{n+1}\longrightarrow\Omega X_n\longrightarrow\Omega X_{n-1}$ is a principal fibration, with fiber an Eilenberg--MacLane loop space."

Why it is false. In a Postnikov tower the fibration `X_n → X_{n−1}` has fibre `K(π_n X, n)` — "`(3)` The map `Xn →Xn−1` is a fibration with fiber a `K(πn X, n)`" (`AT.txt:20331`) — so `ΩX_n → ΩX_{n−1}` has fibre `ΩK(π_n X, n) = K(π_n X, n−1)`. But `π_n(ΩX_{n+1}) = π_{n+1}(X_{n+1}) = π_{n+1}(X)`. These groups differ in general: `K(π_nX,n−1)` has a single nonzero homotopy group, whereas `π_i(ΩX_{n+1}) = π_{i+1}(X)` for every `i ≤ n`. Concretely, for `X = S^2` and `n = 3`: `π_1(ΩX_4) = π_2(X) = Z`, whereas the fibre `K(π_3X,2) = K(Z,2)` has `π_1 = 0`. So `ΩX_{n+1} → ΩX_n → ΩX_{n−1}` is not a fibration sequence at all, and in particular not a principal one. What is true, and is what the card's *preceding* sentence correctly says, is that `ΩX_{n+1} → ΩX_n` is principal: it is the pullback of the path fibration over `K(π_{n+1}X, n+2)` along `Ωk_n`, and Hatcher's definition of "principal" needs a base `B` together with a fibration sequence `ΩB′ → PB′ → B′` and weak equivalences in a commutative square (`AT.txt:20431–20437`); the base here is `K(π_{n+1}X,n+2)`, not `ΩX_{n−1}`. The final conclusion is unaffected, because it follows from the correct preceding sentence.

Second, minor: the index shift is left implicit. `π_i(ΩX_n) = π_{i+1}(X_n)` vanishes for `i ≥ n`, so in the looped tower `⋯ → ΩX_n → ΩX_{n−1} → ⋯` the space `ΩX_n` is the `(n−1)`-st stage of `ΩX`, not the `n`-th. The card says only "the space `ΩX_n` has the correct truncated homotopy groups to be the corresponding Postnikov stage of `ΩX`", which is true only with that shift understood.

### E-HAT-4.3-21 — Exercise 21

**Book (`AT.txt:20819–20820`).**
```
20819: 21. Show that in the Postnikov tower of an H–space, all the spaces are H–spaces and
20820: the maps are H–maps, commuting with the multiplication, up to homotopy.
```

**Card statement.**
```
Show that in the Postnikov tower of an H-space, all the spaces are H-spaces and the maps are H-maps, commuting with the multiplication, up to homotopy.
```

**STATEMENT: matches.**

**PROOF: correct**, on two standard facts that it names but does not prove. `P_n(X×X)` and `P_nX×P_nX` are CW complexes with isomorphic homotopy groups in every degree, since `π_i(X×X) = π_i(X)⊕π_i(X)` for `i ≤ n` and both have no homotopy above `n`; hence they are homotopy equivalent, and `P_nμ` transported across that equivalence gives `μ_n: P_nX×P_nX → P_nX`. The homotopy identity `x ↦ μ(x,e) ≃ x` passes through `P_n` (apply `P_n` to the homotopy), giving a homotopy identity `e_n = P_n(e)`, so each stage is an H-space in Hatcher's sense (`AT.txt:13964–13968`); associativity and inverses pass the same way. Naturality of truncation gives `T_n ∘ μ_n ≃ μ_{n−1} ∘ (T_n×T_n)` for `T_n: P_nX → P_{n−1}X`, i.e. the tower maps are H-maps.

The two named facts are true and traceable: Hatcher's Proposition 4.18 gives, for `n = n′` and a map `g: (X,A)→(X′,A′)`, a map `h: Z→Z′` with `f′h ≃ gf` **and uniqueness of `h` up to homotopy** (`AT.txt:17684–17690`), which is precisely "the Postnikov construction is functorial up to homotopy" plus the naturality used above. The card does not cite it; under the house rule allowing standard course facts by citation this is not a defect, but it is the only proof in the slice whose central step is neither argued nor attributed.

### E-HAT-4.3-22 — Exercise 22

**Book (`AT.txt:20821–20823`).**
```
20821:                                                p
20822: 22. Show that a principal fibration ΩC -→ E --→ B is fiber homotopy equivalent to the
20823: product ΩC × B iff it has a section, a map s : B →E with ps = 11.
```

**Card statement.**
```
Show that a principal fibration $\Omega C \to E \xrightarrow{p} B$ is fiber homotopy equivalent to the product $\Omega C \times B$ if it has a section, a map $s: B \to E$ with $ps = \id$.
```

**STATEMENT: differs — the "iff" is weakened to "if".** Book: "is fiber homotopy equivalent to the / product `ΩC × B` **iff** it has a section, a map `s : B →E` with `ps = 11`" (lines 20822–20823). Card: "is fiber homotopy equivalent to the product $\Omega C \times B$ **if** it has a section, a map $s: B \to E$ with $ps = \id$." The half "trivial ⇒ has a section" is missing, so the card states strictly less than the exercise.

**PROOF: has a gap — only the "if" direction is proved.** The step as printed: "Consequently $E\to B$ is fiber homotopy equivalent to the stated product fibration", reached from a section. That direction is correct: for a principal fibration realised as `f^*(PC → C)`, a section is `s(b) = (b, γ_b)`; `H(b,t) = γ_b(t)` is a homotopy from the constant map at `c_0` to `f`; Exercise 11 (card E-HAT-4.3-11) gives that `f^*` and `const^*` are fiber homotopy equivalent as fibrations over `B`; and `const^*(PC→C) = {(b,γ) : γ(0) = c_0 = γ(1)} = B×ΩC`. What is missing is the converse required by the printed exercise: a fibration fiber homotopy equivalent to `ΩC×B → B` has a section (the product carries the evident section `b ↦ (const_{c_0}, b)`, and sections transport along a fiber homotopy equivalence). It is one line, but as it stands the card discharges only half of the book's statement.

### E-HAT-4.3-23 — Exercise 23

**Book (`AT.txt:20824–20827`).**
```
20824: 23. Prove the following uniqueness result for the Quillen plus construction: Given
20825: a connected CW complex X , if there is an abelian CW complex Y and a map X →Y
20826: inducing an isomorphism H∗ (X; Z) ≈ H∗ (Y ; Z) , then such a Y is unique up to homo-
20827: topy equivalence. [Use Corollary 4.73 with W the mapping cylinder of X →Y .]
```

**Card statement.**
```
Prove the following uniqueness result for the Quillen plus construction: Given a connected CW complex $X$, if there is an abelian CW complex $Y$ and a map $X \to Y$ inducing an isomorphism $H_*(X; \ZZ) \approx H_*(Y; \ZZ)$, then such a $Y$ is unique up to homotopy equivalence.
```

**STATEMENT: differs — the printed bracketed hint is dropped.** Book: "`[Use Corollary 4.73 with W the mapping cylinder of X →Y .]`" (line 20827). The card's statement ends after "unique up to homotopy equivalence."

**PROOF: correct, modulo one unstated hypothesis check.** (i) With `W = M_i ⊃ X` and `W ≃ Y`, `i` a homology isomorphism gives `H_*(W,X;Z) = 0`: the exact sequence `H_n(X)→H_n(W)→H_n(W,X)→H_{n−1}(X)` has the first map an isomorphism in every degree. (ii) The UCT for the pair then gives `H^{n+1}(W,X;A) = 0` for every abelian `A` and every `n`, in particular `A = π_n(Y′)`. (iii) Corollary 4.73 — "If `X` is a connected abelian CW complex and `(W , A)` is a CW pair such that `H n+1 (W , A; πn X) = 0` for all `n` , then every map `A→X` can be extended to a map `W →X`" (`AT.txt:20688–20690`) — with `X ↦ Y′`, `A ↦ X`, `W ↦ W` extends `i′: X → Y′` to `F: W → Y′`. (iv) Restricting to the deformation retract `Y ⊂ W` gives `f: Y → Y′` with `fi ≃ i′`. (v) `f_* = i′_* i_*^{-1}` is an isomorphism on homology. (vi) Proposition 4.74 — "If `X` and `Y` are connected abelian CW complexes, then a map `f : X →Y` inducing isomorphisms on all homology groups is a homotopy equivalence" (`AT.txt:20703–20704`) — gives `f` a homotopy equivalence. (Connectedness of `Y, Y′` follows from `H_0(X) ≅ H_0(Y)` with `X` connected, so the card's use of "connected" in the proof matches the book's statement.)

*Unstated check:* Corollary 4.73 requires `(W, A)` to be a **CW pair**. `(M_i, X)` is a CW pair only if `i: X → Y` is cellular; the mapping cylinder of an arbitrary map of CW complexes is not a CW complex containing `X` as a subcomplex. The repair is one sentence (replace `i` by a homotopic cellular map — cellular approximation — which is still a homology isomorphism), but as written the cited theorem is applied without its hypothesis verified. This is the only respect in which the proof falls short.

### E-HAT-4.3-24 — Exercise 24

**Book (`AT.txt:20828–20830`).**
```
20828: 24. In the situation of the relative lifting problem, suppose one has two different lifts
20829: W →X that agree on the subspace A ⊂ W . Show that the obstructions to finding a
20830: homotopy rel A between these two lifts lie in the groups H n (W , A; πn F ) .
```

**Card statement.**
```
In the situation of the relative lifting problem, suppose one has two different lifts $W \to X$ that agree on the subspace $A \subset W$.
Show that the obstructions to finding a homotopy rel $A$ between these two lifts lie in the groups $H^n(W, A; \pi_n F)$.
```

**STATEMENT: matches.**

**PROOF: has a gap — there is no proof.** The five top-level steps state true things, but every `pf-proof` is a placeholder phrase in place of an argument. Verbatim, at card lines: 40 "`setup.`"; 56 "`definition of relative homotopy between lifts.`"; 80 "`product cellular decomposition with $I = [0, 1]$.`"; 95 "`boundary formula for cylinder cells.`"; 119 "`standard obstruction theory for extending sections of fibrations.`"; 134 "`assignment of boundary homotopy classes to $(n+1)$-cells.`"; 153 "`excision and suspension isomorphism in relative cohomology.`" The concluding step then says "The obstruction to finding a homotopy rel `A` between the two lifts at stage `n` lies in `H^n(W, A; \pi_n F)`. Q.E.D." and its proof is "Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}." So the conclusion the book asks the reader to prove is asserted, not derived.

What is genuinely missing, step by step: (a) that a boundary lift defines a well-defined element of `π_n(F)` — this needs the fibration to be trivial over the contractible cell `e^n×I` up to fiber homotopy (the card gestures at it with "Since `g∘pr_W` is nullhomotopic on `e^n×I`, lift a contraction of this base map to identify the restricted fibration with the constant fiber up to fiber homotopy", which is the entire content and is not carried out), and it needs the coefficient group fixed: Hatcher's own §4.3 writes the obstructions of the relative lifting problem as `ω_n ∈ H^{n+1}(W,A; π_n F)` (`AT.txt:20732–20734`), so `π_n F` is the right group, but the card never addresses the action of `π_1(B)` on it; (b) that the assembled cochain is a cocycle; (c) that the suspension identification is compatible with coboundaries, so that the obstruction is a cohomology class rather than a cochain.

Secondary structural defect: five `pf-step`s are nested *inside* a `pf-proof` (card lines 34, 72, 111, 125, 140). Running the corpus's own filter (`pandoc --lua-filter ~/.pandoc/filters/lamport_proof.lua`) renders them as sub-steps `1.1, 1.2, 2.1, 2.2, 3.1, 3.2, 3.3` of the proof blocks at card lines 32, 70, 109, while the real top-level steps are at card lines 28, 46, 66, 105, 163. The argument therefore does not read as a chain of top-level steps.

What the card gets right: the reformulation on `W×I` is correct — a homotopy rel `A` from `f_0` to `f_1` lifting the constant homotopy of `g` is the same as a lift on `W×I` extending the partially defined one on `Y = W×{0} ∪ A×I ∪ W×{1}`, and the three prescriptions agree on overlaps because `f_0|_A = f_1|_A`; the cell correspondence (an `n`-cell `e^n` of `W∖A` gives the `(n+1)`-cell `e^n×(0,1)`) and `∂(e^n×I) ≅ S^n` are correct; and the identifications `C^{n+1}(W×I,Y;π_nF) ≅ C^n(W,A;π_nF)` and `H^{n+1}(W×I,Y;π_nF) ≅ H^n(W,A;π_nF)` are correct, since `(W×I)/Y = Σ(W/A)` and suspension shifts degree by one.

---

## 3. Defects, most serious first

1. **`E-HAT-4.3-24` — the card has no proof.** All seven `pf-proof` blocks are placeholder phrases (card lines 40, 56, 80, 95, 119, 134, 153); the conclusion is the exercise itself. Additionally five `pf-step`s sit inside `pf-proof`s (card lines 34, 72, 111, 125, 140) and render as sub-steps. The reformulation, the cell count and the suspension isomorphism are right; the obstruction construction, the cocycle property and the coefficient system are not treated.
2. **`E-HAT-4.3-20` — one sentence of the proof is false.** "the three-term sequence `ΩX_{n+1}→ΩX_n→ΩX_{n−1}` is a principal fibration, with fiber an Eilenberg–MacLane loop space." The fibre of `ΩX_n→ΩX_{n−1}` is `K(π_nX,n−1)`, not `ΩX_{n+1}`; the principal fibration is `ΩX_{n+1}→ΩX_n` over `K(π_{n+1}X,n+2)`. The conclusion survives (the preceding sentence is right), but the false statement must go. The stage index (`ΩX_n` is the `(n−1)`-st stage of `ΩX`) is also left implicit.
3. **`E-HAT-4.3-22` — statement weakened from "iff" to "if", and only one direction proved.** Book `AT.txt:20823`: "iff it has a section"; card: "if it has a section". The missing direction (product ⇒ section) is not proved.
4. **`E-HAT-4.3-5`, `-9`, `-13`, `-14`, `-23` — the printed bracketed hints are dropped.** Exact text dropped: `-5` "`[Build a K(Z, n) from S n by attaching cells of dimension ≥ n + 2 .]`" (`20768–20769`); `-9` "`[Use the preceding problem.]`" (`20780`); `-13` "`[One approach is to use Corollary 0.21 to reduce to the case of deformation retractions.]`" (`20796–20797`); `-14` "`[See Exercises 11 and 13.]`" (`20801`); `-23` "`[Use Corollary 4.73 with W the mapping cylinder of X →Y .]`" (`20827`). Each is printed as part of the exercise and is a hint a reader of the book gets and a reader of the card does not. For `-5` the hint is also the elementary proof of the step the card leaves as a black box.
5. **`E-HAT-4.3-10` — the action is not shown to be by group automorphisms.** The step "reversing `β` gives the inverse automorphism. Thus `π_1(E,e_0)→Aut(π_n(F,e_0))` is a homomorphism" gives invertibility of `[α]↦[β]·[α]` but never additivity in `α`; one sentence (the transport map `F→F` is a homotopy equivalence, hence a homomorphism on `π_n`) is missing.
6. **`E-HAT-4.3-23` — a hypothesis of the cited theorem is not checked.** Corollary 4.73 needs `(W,A)` to be a CW pair; `(M_i,X)` is one only if `i` is cellular. The fix is to homotope `i` to a cellular map first.
7. **`E-HAT-4.3-6` — the homotopy-inverse step skips its composite.** "The map corresponding to `a ↦ −a` is a homotopy inverse" must be checked through `µ∘(id×ν)∘Δ` (and `µ∘(ν×id)∘Δ`), which induces `a ↦ 0`; as written the step names `ν` but never forms the composite whose class must be that of the constant map.
8. **`E-HAT-4.3-7` — symbol slip.** The fundamental class is introduced as `\nu` and then used as `u` in every subsequent formula.
9. **Prose-level terse steps that are nevertheless correct** (not defects under a citation standard, listed so a reviewer need not re-derive them): `-4` the compatibility of the representing class with Hurewicz (supported by `AT.txt:19549–19555`); `-5` the `n`-equivalence step; `-19` the transport of the `ΩB`-action from `F_p` to `F`; `-21` functoriality of Postnikov truncation (supported by Proposition 4.18, `AT.txt:17684–17690`).
10. **Audit metadata contradicts this audit.** The `source-checked` notes on `E-HAT-4.3-5`, `-9`, `-13`, `-14` and `-23` all read "Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise N; the stored statement matches." Those five notes are wrong — each of those statements is missing its printed hint. `E-HAT-4.3-22` has no `source-checked` note at all (only `solution-written` by `gemini-3.7-flash`), and it is the one statement that drops half of an "iff". Likewise `24` has only `solution-written` (by `muse-spark-1.2`), and it is the card with no proof at all. (`19`, also only `solution-written` by `gemini-3.7-flash`, is in fact correct.) The twenty-one `solution-reviewed` events by `gpt-5.6-sol` in this section did not catch defects 2, 5, 6, 7 or 8, so `solution-reviewed` in this section is not evidence of correctness.

---

## 4. Limits of this audit

* Read in full: statements and solutions of all 24 cards of §4.3. Nothing in §4.3 is sampled or left unread.
* Not audited (other members' slices, 113 cards): §3.D (3), §3.F (9), §3.H (6), §4.1 exercises 10–23 (14), §4.2 (39), and the nine Chapter-4 additional-topic sections (42). No verdict here applies to them.
* Proofs were checked as mathematics, by reading, against the printed statements of the theorems they cite; no machine formalisation was attempted, and no card was edited.
