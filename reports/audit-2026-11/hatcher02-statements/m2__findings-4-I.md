# findings-4-I — SRC-TEXT-HAT02 §4.I (Stable Splittings of Spaces)

Cards in section: **3** (E-HAT-4.I-1 … 3). Book exercise block: AT.txt **line 23272**
("Exercises"), statements at **23273–23288**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.I-1 | **statement differs** — bracketed approach dropped (defect 1). | unread |
| E-HAT-4.I-2 | **statement differs** — final sentence dropped (defect 2). | unread |
| E-HAT-4.I-3 | **statement differs** — trailing clause dropped (defect 3). | unread |

## Defects (most serious first)

1. **E-HAT-4.I-1: bracketed approach dropped.** Book, AT **23274–23276**: "[One approach: Show the map
   Σr + Σq : ΣX →ΣA ∨ Σ(X/A) induces an isomorphism on homology, where r : X →A is the retraction and
   q : X →X/A is the quotient map.]"
2. **E-HAT-4.I-2: final sentence dropped.** Book, AT **23281–23282**: "Thus to determine stable
   splittings of K(Zn , 1) it suffices to do the case that n is a prime power, as in Proposition 4I.3."
   That sentence is the point of the exercise; the card keeps only the Künneth computation.
3. **E-HAT-4.I-3: trailing clause dropped.** Book, AT **23287–23288**: "… are chosen to have the
   minimum number of cells in each dimension, **as described in the remarks following the proof**."
   The dropped clause is the only pointer that fixes which cell structures count.

## Census
3 cards; 3 differ. All 3 carry `source-checked` / `solution-written` / `solution-reviewed`
(`gpt-5.6-sol`).

## PROOF AUDIT (read in full)

- **E-HAT-4.I-1 — proof correct.** F = (j_A Σr) + (j_Q Σq): ΣX → ΣA ∨ Σ(X/A). Since r i = id, i_*
  splits, the LES of (X,A) breaks into split short exact sequences and (r_*,q_*) is an isomorphism;
  under the suspension isomorphism F_* is that map, so F is a homology isomorphism. Both sides are
  simply connected (suspensions of a connected complex), so the homology Whitehead theorem applies.
- **E-HAT-4.I-2 — proof correct.** Uses Σ(X×Y) ≃ ΣX ∨ ΣY ∨ Σ(X∧Y), which is Hatcher's Proposition
  4I.1 verbatim (AT 23143), plus K(G×H,1) ≃ K(G,1)×K(H,1). H̃_i(K(Z_m,1)) is Z_m in odd degrees and 0
  in positive even degrees, so every reduced homology group is m-torsion, likewise n-torsion, and for
  coprime m,n both ⊗ and Tor vanish by Bézout; the Künneth formula for X∧Y then gives H̃_*(X∧Y) = 0,
  and Σ(X∧Y), being simply connected with trivial reduced homology, is contractible.
- **E-HAT-4.I-3 — proof correct.** It follows the book's proof (AT 23225–23260): Xi is the telescope
  of the composite mi of the maps h_j = Σf − r^j·1, and the minimal cell model "a 0 cell and a k cell
  for each k congruent to 2i or 2i+1 mod 2p−2" is exactly AT 23258–23260. Cellular approximation gives
  a map of (2k+1)-skeleta, degreewise homology isomorphism plus vanishing above 2k+1 plus simple
  connectivity (no 1-cells) gives the homotopy equivalence. The phrase "dimension at least 2k" is
  safe: at dimension exactly 2k the (2k+1)-skeleton of ΣL is ΣL = Σ(L^{(2k)}).
