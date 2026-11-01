---
member: m8
swarm: smvy31u3e
slice: 8
cards:
  - corpus/collections/SRC-TEXT-HAT02/3-h/E-HAT-3.H-2.md
  - corpus/collections/SRC-TEXT-HAT02/3-h/E-HAT-3.H-4.md
  - corpus/collections/SRC-TEXT-HAT02/3-h/E-HAT-3.H-5.md
book: "Hatcher, Algebraic Topology (tmp/hat/AT.txt; line numbers cited per claim)"
status: complete (3 of 3 gaps closed with OLD:/NEW: replacements)
---

# Slice 8 — the §3.H proof gaps: three repairs

Files, one per card, each containing the byte-exact `OLD:` text (verified to occur exactly once in the
card) and the `NEW:` text that replaces it, plus a note on what was wrong:

| card | flagged gap | what the repair does |
|---|---|---|
| `E-HAT-3.H-2` | Poincaré duality quoted for an arbitrary local system | restricts duality to what the book proves — Example 3H.3 for the fundamental class in $H_n(M;\widetilde{\ZZ})$, Theorem 3H.6 for the cap-product isomorphism — and exhibits the general statement's failure on $M=N_g$ with trivial coefficients |
| `E-HAT-3.H-4` | lift compatibility unproved | proves that a lifted homotopy ends at a deck transformation $\gamma$, absorbs it by replacing $\widetilde g$ with $\widetilde G=\gamma^{-1}\widetilde g$, and derives *both* composites $\widetilde G\widetilde f\simeq_p\operatorname{id}$, $\widetilde f\widetilde G\simeq_p\operatorname{id}$; also replaces the unproved "finite fundamental domain" properness step by a proved lemma (Prop. A.1 + freeness of the deck action, using $\pi_1$-injectivity) |
| `E-HAT-3.H-5` | "split injection" is not a map of $\widetilde H_0$ | specifies an exhaustion for which every complementary component is infinite (so the component map is surjective), defines the section and the splitting in the *reduced* model, identifies the limit as the direct sum $\bigoplus_i\ker s_i$, and proves the rank is infinite by counting spheres in the universal cover of the leafless core of $X$ |

None of the three statements is weakened: the answers
$(\ZZ,\ZZ^{g-1},\ZZ_2)$, $\widetilde X\simeq_{\text{proper}}\widetilde Y$, and
$H^1(X;\ZZ[\pi])\cong\bigoplus_{\NN}\ZZ$ ($g>1$) are exactly the cards'.

## Hatcher line numbers used (tmp/hat/AT.txt)

- Example 3H.3 and the fundamental class: 16471–16509 (the class: 16499–16509)
- Ring-bundle duality paragraph before Theorem 3H.6: 16797–16822; **Theorem 3H.6**: 16825–16831
- **Proposition 3H.5**: 16732–16736; finite cellular cochains for $H_c^*$: 16756–16766
- $H_c^*$: singular definition 12085–12095; direct limit description 12160–12175; Example 3.32 ($H_c^*(\RR)$) 12071–12080
- Exercises: 2 at 16836–16837, 4 at 16840–16842, 5 at 16843–16849
- **Proposition A.1** (compact $\Rightarrow$ finite subcomplex) and its proof: 25888–25914
- Prop. 1.30 (homotopy lifting) 2979; Prop. 1.34 (uniqueness of lifts) 3129; deck transformations
  determined by one value 3632–3635; Prop. 1.39 (deck group $=\pi_1$) 3653

## Verification performed

- Each `OLD:` block was extracted from the repair files and checked to occur **exactly once**,
  byte-for-byte, in its card (script check, no manual transcription).
- The final groups of `E-HAT-3.H-2` were re-derived twice: from the twisted cellular chain complex
  ($d_1=-2$, $d_2=0$, giving $H_2=\ZZ$, $H_1=\ZZ^{g-1}$, $H_0=\ZZ_2$) and from
  $H^{2-j}(N_g;\ZZ)$; they agree.
- The properness lemma of `E-HAT-3.H-4` was checked against the counterexample that shows injectivity is
  needed (pinch $S^1\vee S^1\to S^1$, $F_2\twoheadrightarrow\ZZ$, infinite fibres).
- The exhaustion of `E-HAT-3.H-5` was checked to satisfy, for every $i$: $T_i$ finite, $T_i\subset
  T_{i+1}$, $\bigcup_iT_i=\widetilde X$, all complementary components infinite, and every
  complementary component containing a component of the next complement.

## Not done / honest limits

- These are repairs of existing cards, so no new card was created and nothing under `corpus/` was
  modified; a human installs the `NEW:` text over the `OLD:` text.
- `E-HAT-3.H-2`: the card's *combinatorial verification* step (the twisted cellular chain complex for
  $N_g$) is correct but was not rewritten; it is consistent with the repaired duality step.
- `E-HAT-3.H-4`: the repair uses Hatcher's Proposition A.1 and Propositions 1.30/1.34/1.39; Hatcher
  states the "deck transformation determined by one point" fact in words on p. 62 rather than as a
  numbered result, and the repair cites it where it is used.
