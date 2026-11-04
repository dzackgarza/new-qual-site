# findings-3-H — SRC-TEXT-HAT02 §3.H (Local Coefficients)

Cards in section: **6** (E-HAT-3.H-1 … 6). Book exercise block: AT.txt **line 16834**
("Exercises"), statements at **16835–16863**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-3.H-1 | **statement matches** (AT 16835). | unread |
| E-HAT-3.H-2 | **statement matches** (AT 16836–16837). | unread |
| E-HAT-3.H-3 | **statement matches** (AT 16838–16842). Book prints ‘identity’ in single quotes; card uses plain quotes. | unread |
| E-HAT-3.H-4 | **statement matches** (AT 16843–16845). | unread |
| E-HAT-3.H-5 | **statement matches**, bracketed hint kept, including "compute H_c^n(X̃) as lim→ H^n(X̃, X̃ − T_i)" (AT 16846–16854). | unread |
| E-HAT-3.H-6 | **statement matches** (AT 16856–16863). | unread |

## Defects
None at the statement level.

## Census
6/6 cards carry `source-checked`/`solution-written`/`solution-reviewed` (`gpt-5.6-sol`,
2026-09-09).

## PROOF AUDIT (read in full)

- **E-HAT-3.H-1 — proof correct.** With monodromy −1 the twisted cellular differential is
  (−1) − 1 = −2 on the 1-cell: H_1 = ker(−2) = 0, H_0 = coker(−2) = Z_2; dually H^0 = 0, H^1 = Z_2.
  Both answers are right (sign conventions give ±2, same kernel and cokernel).
- **E-HAT-3.H-2 — proof correct.** Poincaré duality with local coefficients H_k(M;M_Z) ≅
  H^{n−k}(M;Z) is the right tool; H_1(N_g;Z) = Z^{g−1} ⊕ Z_2 and H_2 = 0 give H^0 = Z, H^1 = Z^{g−1},
  H^2 = Z_2 by the universal coefficient theorem; hence H_2 = Z, H_1 = Z^{g−1}, H_0 = Z_2. The
  independent cellular check (d_1(a_i) = −2e^0, d_2(e²) = Σ(1 + (−1))a_i = 0) agrees, including
  ker(d_1) = Z^{g−1} (coefficients summing to zero).
- **E-HAT-3.H-3 — proof correct.** Bundles of groups with fiber G over X ↔ monodromy
  π1(X) → Aut(G) up to conjugacy, and [X, BAut(G)] ≅ Hom(π1 X, Aut G)/Inn for X a CW complex; the
  pullback construction is the inverse. The disconnected case is handled componentwise.
- **E-HAT-3.H-4 — proof correct.** The lift of a homotopy equivalence between finite complexes is
  equivariant for the identification of deck groups by f_*; a compact subset of a universal cover
  meets only finitely many translates of a fundamental finite subcomplex, so inverse images of
  compacts are compact, and the same finite-fundamental-domain argument works uniformly in the
  homotopy parameter. Proper homotopy inverses follow.
- **E-HAT-3.H-5 — proof has a gap.** The final answer (Z for g = 1, countable free for g > 1) is
  right and matches the book (AT 16847–16848), but the key step is not justified: the card asserts
  "the maps H̃^0(X̃−T_i) → H̃^0(X̃−T_{i+1}) are split injections". Under the identification
  H^1(X̃, X̃−T_i) ≅ H̃^0(X̃−T_i) the transition map sends a function on components of X̃−T_i to the
  function on components of X̃−T_{i+1} that is constant on the descendants of each component — and
  that is *not* sum-zero preserving, so it is not even a map H̃^0 → H̃^0 as claimed. What the argument
  needs is the (true) statement that the colimit has countable rank; asserting split injectivity with
  a "distinguished descendant" does not supply it. Everything before that step is right:
  H^n(X̃,X̃−T_i) = 0 for n ≠ 1, and H^1 ≅ H̃^0(X̃−T_i) of rank c_i − 1.
- **E-HAT-3.H-6 — proof correct.** Local finiteness is preserved by ∂ (a neighbourhood meeting a
  face's image also meets its parent's), so C_*^{lf} is a complex; the relative locally finite
  homology of successive skeleta is ∏G in degree n and 0 elsewhere (product, not sum — correctly
  noted), and finite-dimensionality makes the skeletal comparison converge, giving the infinite
  cellular chain complex.
