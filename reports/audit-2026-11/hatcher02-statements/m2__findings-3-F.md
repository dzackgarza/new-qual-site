# findings-3-F — SRC-TEXT-HAT02 §3.F (Limits and Ext)

Cards in section: **9** (E-HAT-3.F-1 … 9). Book exercise block: AT.txt **line 15973**
("Exercises"), statements at **15974–16015** and **16021–16023**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-3.F-1 | **statement matches** (AT 15974–15979). Only orthography differs: book "glueing", card "gluing"; book prints ‘reverse mapping telescope’ in single quotes. | unread |
| E-HAT-3.F-2 | **statement matches** (AT 15981–15984). The book's lim with a superscript 1 is rendered `\varprojlim^1`. | unread |
| E-HAT-3.F-3 | **statement matches**, bracketed hint kept (AT 15985–15986). | unread |
| E-HAT-3.F-4 | **statement matches** (AT 15988–15991); "iff" expanded to "if and only if", same content. | unread |
| E-HAT-3.F-5 | **statement matches** (AT 15992–15995), including Ext(Z_{p^∞},Z) ≈ Ẑ_p. | unread |
| E-HAT-3.F-6 | **statement matches** (AT 15996). | unread |
| E-HAT-3.F-7 | **statement matches** (AT 15997–16003). | unread |
| E-HAT-3.F-8 | **statement matches** (AT 16005–16009). | unread |
| E-HAT-3.F-9 | **statement differs** — see defects 1 and 2. | unread |

## Defects (most serious first)

1. **E-HAT-3.F-9(a): an "iff" halved to "if".** Book, AT **16022**:
   "(a) Ext(A, Z) is divisible iff A is torsionfree."
   Card: "(a) $\operatorname{Ext}(A, \ZZ)$ is divisible if $A$ is torsionfree."
   The card states only one direction and drops "iff". Part (b) on the same lines keeps its "if …
   and the converse holds if", so the loss is not a house style.
2. **E-HAT-3.F-9: the displayed six-term sequence is not witnessed by AT.txt.** Book, AT **16014–16015**:
   "sequences 0→p A→A→pA→0 and 0→pA→A→Ap →0 can be spliced together to yield the exact sequence
   across the top of the following diagram", and AT **16021**: "where the map labeled ‘ p ’ is
   multiplication by p ." The sequence itself is printed as a *diagram*, which the extraction does
   not carry (AT 16016 is the page break to p.321 and 16017–16020 are blank). The card instead
   prints the formula
   `Hom(pA,Z) → Ext(A_p,Z) → Ext(A,Z) →^p Ext(A,Z) → Ext(_pA,Z) → 0`
   as if it were the book's text. The formula is the correct splicing of the two six-term sequences
   (naturality of the connecting map makes Ext(pA,Z)→Ext(A,Z) multiplication by p), but no line of
   AT.txt supports it verbatim, so this is an unverified reconstruction presented as source text.

## Census
Cards already carrying `source-checked`/`solution-written`/`solution-reviewed` in frontmatter
(9/9, all `gpt-5.6-sol`): the frontmatter claim "the stored statement matches" is false for
E-HAT-3.F-9(a) at minimum.

## PROOF AUDIT (read in full)

- **E-HAT-3.F-1 — proof correct.** Retracts each M_i onto its top copy X_{i+1}, schedules the
  collapses on [0,1/2], [1/2,3/4], [3/4,7/8], … so every t < 1 involves finitely many cylinders and
  every point is in X_0 at t = 1; continuity follows from the coherent (weak) topology of the union.
  The double-telescope case is then the same argument applied to the left-hand half plus the identity
  on T_{≥n}. Correct.
- **E-HAT-3.F-2 — proof correct.** Φ((g_i)) = (g_i − α_{i+1}(g_{i+1})) has kernel lim and cokernel
  lim¹; the Mittag-Leffler hypothesis makes I_i = im(G_j → G_i) stable, the bonding maps I_{i+1} → I_i
  are onto, and the displayed recursion solves Φ(g) = b exactly (each g_i − b_i lies in I_i, and
  α_{i+1}: I_{i+1} → I_i is onto). The quotient tower is pro-zero, a zero-bonding tower has Φ = id,
  and the six-term lim/lim¹ sequence of 0 → I_i → G_i → Q_i → 0 finishes. The passage to a cofinal
  subsequence is legitimate for lim¹ on a countable tower. Correct.
- **E-HAT-3.F-3 — proof correct**, but by a different route from the book's hint: it uses Baer's
  criterion (Q divisible ⇒ injective) and a free resolution, so Ext¹(A,Q) = coker(Hom(F_0,Q) →
  Hom(F_1,Q)) = 0. Valid. The card drops the book's hint, which is the statement defect recorded
  above.
