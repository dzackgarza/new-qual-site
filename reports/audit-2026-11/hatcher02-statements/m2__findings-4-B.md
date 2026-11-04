# findings-4-B — SRC-TEXT-HAT02 §4.B (The Hopf Invariant)

Cards in section: **2** (E-HAT-4.B-1, 4.B-2). Book exercise block: AT.txt **line 21215**
("Exercises"), statements at **21217–21223**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.B-1 | **statement matches** (AT 21217–21220), both H(gf) = (deg f)H(g) and H(gf) = (deg g)²H(f). | unread |
| E-HAT-4.B-2 | **statement differs** — the bracketed hint is dropped (defect 1). | unread |

## Defects

1. **E-HAT-4.B-2: bracketed hint dropped.** Book, AT **21223**: "… when n > 1 , H(p) = ±1 . [Show
   that Cp is a manifold and apply Poincaré duality.]" The card ends at "H(p) = ±1." The hint is the
   only indication of how the degree is to be computed; §4.D exercise 5 (AT 22161–22164) asks for the
   same result by a different route.

## Census
2 cards; 1 differs. Both carry `source-checked` / `solution-written` / `solution-reviewed`
(`gpt-5.6-sol`).

## PROOF AUDIT (read in full)

- **E-HAT-4.B-1 — proof correct.** With x_h ∈ H^n(C_h) the generator and x_h² = H(h)y_h: for
  g∘f the map C_{gf} → C_g is the identity on the bottom cell and has degree d on the top, so pulling
  back gives x_{gf}² = dH(g)y_{gf}, i.e. H(gf) = (deg f)H(g); in the other order the map
  C_f → C_{gf} is g on the bottom cell and degree 1 on the top, so x_{gf} pulls back to d x_f and
  d²H(f) = H(gf). Both computations are right, including the direction of pullback.
- **E-HAT-4.B-2 — proof correct.** m = n + k from local triviality; for n > 1 the base is simply
  connected, the fiber is not S^0, and π_n(S^m) → π_n(S^n) → π_{n−1}(S^k) with π_n(S^m) = 0 forces
  k ≤ n − 1, while k < n − 1 makes π_{k+1}(S^n) → π_k(S^k) → π_k(S^m) read 0 → Z → 0; so k = n−1,
  m = 2n−1 (and n = 1 forces k = 0, the double cover). Then C_p is a closed 2n-manifold (as the
  book's hint at AT 21223 prescribes), its middle cohomology is Z, and unimodularity of the
  intersection form forces H(p) = ±1. Only the orientability of C_p is stated rather than argued (it
  follows from simple connectivity of S^n, n > 1, which is available) — not a gap in substance.
