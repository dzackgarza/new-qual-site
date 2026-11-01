# findings-4-L — SRC-TEXT-HAT02 §4.L (Steenrod Squares and Powers)

Cards in section: **5** (E-HAT-4.L-1 … 5). Book exercise block: AT.txt **line 25802**
("Exercises"), statements at **25803–25820**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.L-1 | **statement matches** (AT 25803–25804). | unread |
| E-HAT-4.L-2 | **statement matches** (AT 25805–25806). | unread |
| E-HAT-4.L-3 | **statement differs** — bracketed hint dropped (defect 1). | unread |
| E-HAT-4.L-4 | **statement differs** — bracketed hint dropped (defect 2). | unread |
| E-HAT-4.L-5 | **statement matches** (AT 25817–25820); the diagram the exercise refers to is a figure not in AT.txt, so "encoded in the following diagram" has no witness either way in the extraction. | unread |

## Defects (most serious first)

1. **E-HAT-4.L-3: bracketed hint dropped.** Book, AT **25809–25810**: "[The Gysin sequence can be used
   to determine the map on cohomology induced by the bundle projection HP5 →OP2 .]"
2. **E-HAT-4.L-4: bracketed hint dropped.** AT **25811–25813**: "[Compute the cohomology ring of the
   mapping cone of the projection S 23 →OP2 via Poincaré duality or the Thom isomorphism.]"

## Census
5 cards; 2 differ. All 5 carry `source-checked` / `solution-written` / `solution-reviewed`
(`gpt-5.6-sol`).

## PROOF AUDIT
All 5 proofs in this section are **unread** — only the statement layer was audited here.

## PROOF AUDIT

- **E-HAT-4.L-1 — proof correct.** Cohomology operations H^m(−;G) → H^n(−;H) are the classes in
  H^n(K(G,m);H). H^1(−;Z) ↔ H^n(S^1;Z), which vanishes for n > 1, so only u ↦ a·u survives;
  H^2(−;Z) ↔ H^n(CP^∞;Z) = Z for n = 2j, 0 for n odd, so the operations are u ↦ a·u^j;
  H^1(−;Z_p) ↔ H^n(K(Z_p,1);Z_p), which is Z_2[x] for p = 2 (giving u ↦ u^n in every degree) and
  Λ(x) ⊗ Z_p[y], y = βx, for odd p (giving (βu)^j in degree 2j and u(βu)^j in degree 2j+1). All
  three classifications are right, including the odd-prime Bockstein-generated basis.
- **E-HAT-4.L-2 — proof correct.** H̃^*(X;Z_2) ≅ H^*(S^1;Z_2) ⊗ H̃^*(CP^∞;Z_2), so H^3(X;Z_2) is
  spanned by u = a×x; the Cartan formula gives Sq^2(u) = a×Sq^2x = a×x^2 ≠ 0 because Sq^1a = a^2 = 0
  and Sq^2a = 0 by instability. In Y = S^3 × CP^∞ the degree-3 class is pr_1^*(ι_3) and
  Sq^2 of it vanishes because H^5(S^3;Z_2) = 0. Since the degree-3 group is one-dimensional on both
  sides, a homotopy equivalence would have to match these classes and their Sq^2's. Correct.
- **E-HAT-4.L-3 — proof correct.** The Gysin sequence for an S^4-bundle gives
  H^3(B) → H^8(B) → H^8(E) → H^4(B), and H^3(OP^2;Z_3) = H^4(OP^2;Z_3) = 0, so p^*y = x^2.
  P^1y = 0 because H^{12}(OP^2;Z_3) = 0, while P^1x = x^2 (restrict to CP^∞, where x = −u^2 and
  P^1(−u^2) = −2u^4 = u^4 = x^2 in Z_3) and hence P^1(x^2) = 2x^3 ≠ 0 by Cartan. Naturality gives
  0 = p^*(P^1y) = P^1(p^*y) = 2x^3, contradiction. The mod-3 arithmetic is right throughout
  (2 ≢ 0, −2 ≡ 1).
- **E-HAT-4.L-4 — proof unread** (only the opening Thom-isomorphism setup was read).
- **E-HAT-4.L-5 — proof unread.**
