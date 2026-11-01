# repairs-4-i — slice 4 (4-a, 4-b, 4-i), section 4.I

Hatcher, *Algebraic Topology*, §4.I exercises 1–3, AT.txt:23272-23288. Patch specification only; nothing under `corpus/` was modified.

Quotes of AT.txt are verbatim in wording; its lossy glyph linearisation is normalised (`hX, Y i` → `⟨X, Y⟩`, a raised `W` → `∨`, `֏` → `↦`), and superscripts and subscripts are written spaced as AT.txt prints them. Line ranges are exact.

CARD: corpus/collections/SRC-TEXT-HAT02/4-i/E-HAT-4.I-1.md
BOOK: AT.txt:23273-23276  "1. If a connected CW complex X retracts onto a subcomplex A , show that ΣX ≃ ΣA ∨ Σ(X/A) . [One approach: Show the map Σr + Σq : ΣX →ΣA ∨ Σ(X/A) induces an isomorphism on homology, where r : X →A is the retraction and q : X →X/A is the quotient map.]"
OLD: |
If a connected CW complex $X$ retracts onto a subcomplex $A$, show that $\Sigma X \simeq \Sigma A \lor \Sigma(X/A)$.
|
NEW: |
If a connected CW complex $X$ retracts onto a subcomplex $A$, show that $\Sigma X \simeq \Sigma A \lor \Sigma(X/A)$.
[One approach: Show the map $\Sigma r + \Sigma q: \Sigma X \to \Sigma A \lor \Sigma(X/A)$ induces an isomorphism on homology, where $r: X \to A$ is the retraction and $q: X \to X/A$ is the quotient map.]
|
WHY: The printed bracketed hint "[One approach: ...]", which supplies the whole suggested proof, was missing.

CARD: corpus/collections/SRC-TEXT-HAT02/4-i/E-HAT-4.I-2.md
BOOK: AT.txt:23280-23282  "2. Using the Künneth formula, show that ΣK(Zm × Zn , 1) ≃ ΣK(Zm , 1) ∨ ΣK(Zn , 1) if m and n are relatively prime. Thus to determine stable splittings of K(Zn , 1) it suffices to do the case that n is a prime power, as in Proposition 4I.3."
OLD: |
Using the Künneth formula, show that $\Sigma K(\ZZ_m \times \ZZ_n, 1) \simeq \Sigma K(\ZZ_m, 1) \vee \Sigma K(\ZZ_n, 1)$ if $m$ and $n$ are relatively prime.
|
NEW: |
Using the Künneth formula, show that $\Sigma K(\ZZ_m \times \ZZ_n, 1) \simeq \Sigma K(\ZZ_m, 1) \vee \Sigma K(\ZZ_n, 1)$ if $m$ and $n$ are relatively prime.
Thus to determine stable splittings of $K(\ZZ_n, 1)$ it suffices to do the case that $n$ is a prime power, as in Proposition 4I.3.
|
WHY: The printed exercise continues with a second sentence, "Thus to determine stable splittings of K(Zn , 1) it suffices to do the case that n is a prime power, as in Proposition 4I.3", which the card dropped.

CARD: corpus/collections/SRC-TEXT-HAT02/4-i/E-HAT-4.I-3.md
BOOK: AT.txt:23284-23288  "3. Extending Proposition 4I.3, show that the (2k + 1) skeleton of the suspension of a high-dimensional lens space with fundamental group of order p n is homotopy equivalent to the wedge sum of the (2k + 1) skeleta of the spaces Xi , if these Xi ’s are chosen to have the minimum number of cells in each dimension, as described in the remarks following the proof."
OLD: |
Extending Proposition 4I.3, show that the $(2k+1)$-skeleton of the suspension of a high-dimensional lens space with fundamental group of order $p^n$ is homotopy equivalent to the wedge sum of the $(2k+1)$-skeleta of the spaces $X_i$, if these $X_i$'s are chosen to have the minimum number of cells in each dimension.
|
NEW: |
Extending Proposition 4I.3, show that the $(2k+1)$-skeleton of the suspension of a high-dimensional lens space with fundamental group of order $p^n$ is homotopy equivalent to the wedge sum of the $(2k+1)$-skeleta of the spaces $X_i$, if these $X_i$'s are chosen to have the minimum number of cells in each dimension, as described in the remarks following the proof.
|
WHY: The printed pointer ", as described in the remarks following the proof", which locates where the cell-minimal choices are described, was dropped.


## comparison summary

Compared card by card against the printed §4.I exercises, AT.txt:23272-23288: `E-HAT-4.I-1`, `E-HAT-4.I-2`, `E-HAT-4.I-3` — all three cards that exist in `4-i`. All three are defective: 4.I-1 dropped the bracketed `[One approach: ...]` hint, 4.I-2 dropped the printed second sentence, and 4.I-3 dropped the printed pointer `, as described in the remarks following the proof` (that third one loses a cross-reference rather than any mathematics; it is reported because it is printed matter, and a reviewer may downgrade it).

Not compared: every other card of SRC-TEXT-HAT02. The other two sections of this slice are reported in `repairs-4-a.md` and `repairs-4-b.md`; all remaining sections belong to other members' slices. The printed §4.I exercises carry no asterisks and no sub-part stars.

Note for the applier: the audit notes in the front matter of `E-HAT-4.I-1` and `E-HAT-4.I-3` claim "the stored statement matches the corrected current source". Both statements were in fact missing printed matter, so those notes are false as they stand; this specification changes statement blocks only and leaves front matter untouched.
