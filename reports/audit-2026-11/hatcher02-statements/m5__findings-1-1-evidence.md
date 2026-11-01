# §1.1 — all 20 cards audited; the section fails the brief's completion test

The brief says of the already-read sections: "every card in those sections carries a
`solution-reviewed` audit event by `claude` stating what was checked". That is false for §1.1 in
two ways, so §1.1 is not established as read:

* **No** card of §1.1 carries a `solution-reviewed` event by `claude`. 16 of the 20 carry one by
  `gpt-5.6-sol`, 4 carry none at all.
* The four cards with **no** `solution-reviewed` event of any kind are
  `E-HAT-1.1-1`, `E-HAT-1.1-11`, `E-HAT-1.1-12`, `E-HAT-1.1-17`. Nothing in the repository
  records that anyone read their proofs.

I audited **all 20 cards of §1.1** in full (statement against `tmp/hat/AT.txt` with line
quotes, proof line by line): the four below in Part 1, the other sixteen in Part 2. The 16 carry a
`solution-reviewed` event by `gpt-5.6-sol`, so the brief would treat them as read, but since the
brief's stated criterion (a `claude` review) fails for every card of the section, the section as a
whole is not established as read and I verified it rather than assume it.

Book witness: `tmp/hat/AT.txt`; §1.1's exercise list begins at 1989 (`Exercises`).

## E-HAT-1.1-1 — cancellation property for composition of paths
**Statement: matches.** Book 1990–1991:
```
 1990|1. Show that composition of paths satisfies the following cancellation property: If
 1991|f0 g0 ≃ f1 g1 and g0 ≃ g1 then f0 ≃ f1 .
```
Card: "Show that composition of paths satisfies the following cancellation property: If $f_0 \cdot g_0 \simeq f_1 \cdot g_1$ and $g_0 \simeq g_1$ then $f_0 \simeq f_1$." The extraction prints composition dots as spaces (compare 1469, where `h̄·f·h` appears as "h f h"), so the card's `\cdot` is the correct reading of the printed text; no difference.

**Proof: correct.** From f_0·g_0 ≃ f_1·g_1 and g_0 ≃ g_1 (path homotopies, i.e. relative to endpoints) one gets f_0·g_0·ḡ_0 ≃ f_1·g_1·ḡ_1, and f_i·g_i·ḡ_i ≃ f_i·c_{g_i(0)} ≃ f_i, hence f_0 ≃ f_1. The only implicit requirement is that all concatenations are defined (f_0(1) = g_0(0), f_1(1) = g_1(0)), which is what "composition of paths" presupposes. No gap.

## E-HAT-1.1-11 — inclusion of the path component induces an isomorphism on π_1
**Statement: matches.** Book 2034–2035:
```
 2034|11. If X0 is the path-component of a space X containing the basepoint x0 , show that
 2035|the inclusion X0 ֓ X induces an isomorphism π1 (X0 , x0 )→π1 (X, x0 ) .
```
Card: "If $X_0$ is the path-component of a space $X$ containing the basepoint $x_0$, show that the inclusion $i: X_0 \hookrightarrow X$ induces an isomorphism $i_*: \pi_1(X_0, x_0) \to \pi_1(X, x_0)$." Same statement; naming the map `i` adds nothing. (Structure: frontmatter `kind: problem` but the statement sits in `::: {.exercise}` — the same mismatch as E-HAT-2.C-2.)

**Proof: correct.** Surjective: every point of a loop at x_0 is joined to x_0 by an initial segment of the loop, so the loop factors through X_0. Injective: a homotopy rel basepoint H: I² → X has H(s,t) joined to x_0 = H(0,0) by a path in I², so H(I²) ⊆ X_0 and H is a homotopy in X_0. No gap.

## E-HAT-1.1-12 — every endomorphism of π_1(S^1) is induced by a map S^1 → S^1
**Statement: matches.** Book 2036–2037:
```
 2036|12. Show that every homomorphism π1 (S 1 )→π1 (S 1 ) can be realized as the induced
 2037|homomorphism ϕ∗ of a map ϕ : S 1 →S 1 .
```
Card: "Show that every homomorphism $\pi_1(S^1) \to \pi_1(S^1)$ can be realized as the induced homomorphism $\varphi_*$ of a map $\varphi: S^1 \to S^1$." (`ϕ` vs `\varphi` is not a mathematical difference.)

**Proof: correct.** π_1(S^1,1) = ℤ = ⟨[ω]⟩ so a homomorphism is multiplication by a unique n; φ_n(z) = z^n is continuous and basepoint-preserving for every n ∈ ℤ, and φ_n∘ω = e^{2πint} represents n[ω]. Nothing missing.

## E-HAT-1.1-17 — infinitely many nonhomotopic retractions S^1∨S^1 → S^1
**Statement: matches.** Book 2055:
```
 2055|17. Construct infinitely many nonhomotopic retractions S 1 ∨ S 1 →S 1 .
```
Card: "Construct infinitely many nonhomotopic retractions $S^1 \lor S^1 \longrightarrow S^1$."

**Proof: correct, with one incorrectly attributed citation.**
* The construction r_n = identity on the first circle, z ↦ z^n on the second is a retraction with (r_n)_*(α) = ζ, (r_n)_*(β) = ζ^n. Correct.
* Nonhomotopy: for a homotopy H from r_m to r_n the track γ(t) = H(x_0,t) is a loop at x_0 (both r_m and r_n are retractions, so both fix x_0), and π_1(S^1) abelian makes the basepoint-change isomorphism β_γ the identity, so ζ^n = ζ^m. Correct.
* **Citation defect:** the card writes "by Hatcher, §1.1, Proposition 1.5, the induced homomorphisms satisfy (r_n)_* = β_γ ∘ (r_m)_*". Proposition 1.5 as printed states only — 1479:
```
 1479| Proposition 1.5. The map βh : π1 (X, x1 )→π1 (X, x0 ) is an isomorphism.
```
  and its proof (1480–1482) only shows β_h is a homomorphism with inverse β_h̄. The formula g_* = β_γ∘f_* for the track of an unbased homotopy is a different (true, standard) fact; Hatcher does not state it as Proposition 1.5, and §1.1 contains it nowhere. The step is true but the named reference does not support it.
* The card's other citation is accurate: Example 1.21, 2238–2240 — "Thus for a wedge sum ∨α Sα1 of circles, π1 (∨α Sα1 ) is a free group, the free product of copies of Z , one for each circle Sα1 . In particular, π1 (S 1 ∨S 1 ) is the free group Z∗Z". The card is also honest that this is §1.2 material used inside a §1.1 exercise.

## Defects

1. **Evidence defect (affects all four cards and 16 more):** §1.1 contains no `solution-reviewed`
   event by `claude`, contrary to the brief; four of its cards (`1.1-1`, `1.1-11`, `1.1-12`,
   `1.1-17`) have no `solution-reviewed` event at all.
2. **E-HAT-1.1-17 — Proposition 1.5 is cited for a statement it does not make** (1479 gives only
   that β_h is an isomorphism; the track formula is not in §1.1). Minor: the mathematics is right.
3. **E-HAT-1.1-11 — `kind: problem` with a `::: {.exercise}` block** (structural mismatch).

All four statements match the printed text; all four proofs are correct.

# Part 2 — the other sixteen §1.1 cards

Statements were compared with a word-sequence diff against the printed exercises (LaTeX stripped,
extraction hyphenation ignored): **no difference in any of the sixteen except 1.1-16(c)**, which is
recorded as a defect below. Every proof was read line by line. Line numbers are lines of
`tmp/hat/AT.txt`.

| card | book lines | statement | proof |
|---|---|---|---|
| E-HAT-1.1-2 | 1992–1993 | matches | correct: the three-piece loop F_t = H(·,t)·f·H(1−·,t) is continuous by the pasting lemma, F_0 = h·f·h̄, F_1 = k·f·k̄, basepoint fixed, so β_h = β_k |
| E-HAT-1.1-3 | 1994–1995 | matches ("iff"; both directions proved) | correct: abelian ⇒ a b a⁻¹ = b with a = [h·k̄], b = β_k[f], and a b a⁻¹ = β_h[f]; conversely β_h = β_c for a loop h forces [h][f] = [f][h] |
| E-HAT-1.1-4 | 1996–2002 | matches, including "traversed at constant speed" and the "in particular … open … union of finitely many closed convex sets" clause | correct: Lebesgue number subdivision; a star-shaped V is contractible to its centre so any path in V is homotopic rel endpoints to the broken line via the centre; the pieces paste; open sets are locally star-shaped; a finite union of closed convex sets is locally star-shaped with centre x (J = {j : x ∈ C_j} finite, balls avoiding the other C_j) |
| E-HAT-1.1-5 | 2003–2008 | matches, including the bracket "[In this problem, 'homotopic' means 'homotopic without regard to basepoints'.]" | correct: (a)⇔(b) via the cone (S^1×I)/(S^1×{1}) ≅ D^2 and via contracting D^2; (a)⇒(c) because a freely homotopic loop has conjugate based class, and the identity is central; (c)⇒(a) trivially; "simply-connected iff all maps S^1 → X are homotopic" proved in both directions (constant maps at different points are homotopic exactly when X is path connected) |
| E-HAT-1.1-6 | 2009–2015 | matches | correct: Φ is onto for path connected X (slide the basepoint along a path); Φ[f] = Φ[g] iff [f],[g] conjugate, by cutting the free homotopy cylinder along {s_0}×I to get the boundary word f·h·ḡ·h̄ |
| E-HAT-1.1-7 | 2016–2020 | matches, hint included | correct: f_t(θ,s) = (θ+2πts,s) is stationary on s = 0; α(s) = (θ_0,s) and f∘α are not homotopic rel endpoints, since projecting to S^1 turns them into loops of degree 0 and 1; a homotopy stationary on both circles would give such a homotopy; the companion homotopy g_t(θ,s) = (θ+2πt(s−1),s) is stationary on s = 1 |
| E-HAT-1.1-8 | 2021–2022 | matches | correct: f(x,y) = x has f(−x,−y) = −x ≠ x, so the Borsuk–Ulam analogue fails for the torus (answer: no) |
| E-HAT-1.1-9 | 2026–2028 | matches | correct: F(v,d) = (∫_{A_i} sgn(v·x−d))_{i≤3} on S^3 ⊂ R^3×R is continuous (dominated convergence; {v·x = d} is null when v ≠ 0, and v = 0 forces the integrand constant), odd, so Borsuk–Ulam (Corollary 2B.7 with n = 3) gives F(q) = 0; v = 0 only if all μ(A_i) = 0, and then any plane works; for v ≠ 0 the plane {v·x = d} has null measure and splits each A_i into equal halves |
| E-HAT-1.1-10 | 2029–2033 | matches | correct: G(u,v) = (a(u),b(v)) on the convex square, with p_0 (bottom then right) ↦ α·β and p_1 (left then top) ↦ β·α, straight-line homotopy p_t = (1−t)p_0 + t p_1 fixes both endpoints, so [α][β] = [β][α] |
| E-HAT-1.1-13 | 2038–2040 | matches (iff, both directions) | correct: from surjectivity of i_*, ℓ = a·γ·b is homotopic to a loop c in A, so γ ≃ ā·c·b̄ lies in A; conversely a loop at x_0 is homotopic rel endpoints to a path in A, which is a loop in A |
| E-HAT-1.1-14 | 2041–2043 | matches (the formula [f] ↦ (p_{1*}([f]), p_{2*}([f])) is stated) | correct: Ψ[f] = ([p_1f],[p_2f]) is a homomorphism, Θ[a],[b] = [t ↦ (a(t),b(t))] is well defined, ΨΘ = id and ΘΨ = id |
| E-HAT-1.1-15 | 2044–2046 | matches, and the card reproduces the commutative diagram of the printed exercise | correct: (f_*β_h)[γ] = [f h·fγ·f h‾] = β_{fh}[fγ] = (β_{fh}f_*)[γ], using f∘h̄ = \overline{f∘h} |
| E-HAT-1.1-16 | 2048–2054 | **differs in (c)** — see below | (a),(b),(d),(e),(f) correct; (c) correct only relative to the card's own description |
| E-HAT-1.1-18 | 2056–2062 | matches, including n ≥ 2, "path-connected", part (b) and the bracket "[For the case that X has infinitely many cells, see Proposition A.1 in the Appendix.]" | correct: U = X∖{c} and V = int(e^n) with U ≃ A, V contractible, U∩V path connected for n ≥ 2, then Lemma 1.15's subdivision gives a loop in U homotopic to γ; (a) S^1∨S^2 = S^1 ∪ 2-cell with a retraction back by collapsing S^2; (b) attach cells one at a time, and for infinitely many use Proposition A.1 as the book directs |
| E-HAT-1.1-19 | 2063–2071 | matches, including the whole bracketed remark about π_1(S^1) | correct: compact image in a finite connected subcomplex K; finite cover by contractible "monotone" sets; Lebesgue-number subdivision; replace each piece inside a contractible U_i; cancel backtracking across interior points of edges (finitely many breakpoints); conclude with a finite sequence of whole edges, monotonically |
| E-HAT-1.1-20 | 2072–2075 | matches, bracket included | correct: Lemma 1.19 as printed (1957–1960: "If ϕt : X →Y is a homotopy and h is the path ϕt (x0 ) … then … ϕ0∗ = βh ϕ1∗") applied to f_t gives id = β_h, i.e. [h][γ][h]⁻¹ = [γ] for all [γ], so [h] is central |

## Defect: E-HAT-1.1-16(c) — the printed figure replaced by an invented description

Book 2048–2054:
```
 2048|16. Show that there are no retractions r : X →A in the following cases:
 2049|(a) X = R3 with A any subspace homeomorphic to S 1 .
 2050|(b) X = S 1 × D 2 with A its boundary torus S 1 × S 1 .
 2051| (c) X = S 1 × D 2 and A the circle shown in the figure.
 2052|(d) X = D 2 ∨ D 2 with A its boundary S 1 ∨ S 1 .
 2053|(e) X a disk with two points on its boundary identified and A its boundary S 1 ∨ S 1 .
 2054| (f) X the Möbius band and A its boundary circle.
```
The card prints for (c): "$X = S^1 \times D^2$ and $A$ a circle in $X$ that winds twice around the core circle $S^1 \times \{0\}$, passing between its two turns through a clasp, as in the source figure." The book's (c) contains a figure and no verbal description; the card's fifteen added words ("winds twice around the core circle … through a clasp") are not in the printed text and cannot be checked against `AT.txt`, which contains no figure. The card's proof of (c) — A is homotopic to the core traversed twice, so i_*: ℤ → ℤ is multiplication by 2, which no retraction can split — is the correct argument *for that description*; if the figure shows something else, the argument does not apply. This is the one place in §1.1 where a card states more than the book prints, and it should be resynced against the figure (or marked as figure-dependent) rather than left as if verified.

The other five cases of 1.1-16 are correct: (a) π_1(ℝ^3) = 0 ⇏ ℤ ↪ 0; (b) the meridian {x_0}×S^1 bounds {x_0}×D^2 in the solid torus; (d) D^2∨D^2 is contractible while π_1(S^1∨S^1) = F_2; (e) the loop ab is nontrivial in F(a,b) but bounds the disk; (f) the boundary of the Möbius band wraps twice around the core.

## §1.1 summary

All 20 cards read. 19 statements match the printed text exactly (mechanical word diff plus manual
reading); **1.1-16(c) differs** (figure replaced by an unverifiable verbal description). All 20
proofs are correct except that 1.1-16(c)'s correctness is conditional on that description. One
citation defect: **1.1-17 cites Proposition 1.5 (1479) for a formula it does not state**. Evidence:
no §1.1 card has a `claude` review; 1.1-1, -11, -12, -17 have no review event at all.
