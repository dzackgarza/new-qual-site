# Statement fidelity — what was actually compared

The task asks for fidelity "only where cheap". Two things were cheap here and are reported in
full; everything else is explicitly not audited.

## 1. The ∗ (difficulty) markers are printed and are almost entirely dropped

Stein–Shakarchi marks the harder problems with a dagger-like asterisk set after the number
(`2.∗`). In the OCR it comes through as `∗` (U+2217). A census over every exercise/problem page
(PDF 43–50, 83–89, 122–129, 146–152, 172–177, 193–199, 218–223, 267–279, 297–301, 328–336,
360–362) finds **27 markers**: 26 whole problems and one sub-part. **One card records it.**

Printed markers, with page (PDF = printed + 19):

| item | PDF page | card on disk | card records the ∗? |
|---|---|---|---|
| ch2 PR-1 **(b) ∗** (a starred *part*, not the whole item) | 87 | E-SS2.PR-1 | **no** — card's part (b) reads "Fix $0 < \alpha < \infty$" |
| ch2 PR-2 | 87 | E-SS2.PR-2 | no |
| ch2 PR-5 | 88 | E-SS2.PR-5 | **yes** — a `{.remark}` says "The book marks this problem with an asterisk." |
| ch3 PR-1 | 127 | E-SS3.PR-1 | no |
| ch3 PR-4 | 129 | **no card** | — (see gaps-3.md) |
| ch3 PR-5 | 129 | **no card** | — (see gaps-3.md) |
| ch4 PR-3 | 152 | E-SS4.PR-3 | no |
| ch4 PR-4 | 152 | E-SS4.PR-4 | no |
| ch5 PR-2 | 176 | E-SS5.PR-2 | no |
| ch5 PR-3 | 176 | E-SS5.PR-3 | no |
| ch5 PR-4 | 176 | E-SS5.PR-4 | no |
| ch6 PR-2 | 199 | E-SS6.PR-2 | no |
| ch6 PR-3 | 199 | E-SS6.PR-3 | no |
| ch6 PR-4 | 199 | E-SS6.PR-4 | no |
| ch7 PR-2 | 223 | E-SS7.PR-2 | no |
| ch7 PR-3 | 223 | E-SS7.PR-3 | no |
| ch7 PR-4 | 223 | E-SS7.PR-4 | no |
| ch8 PR-3 | 275 | E-SS8.PR-3 | no |
| ch8 PR-4 | 276 | E-SS8.PR-4 | no |
| ch8 PR-6 | 277 | E-SS8.PR-6 | no |
| ch8 PR-7 | 277 | E-SS8.PR-7 | no |
| ch8 PR-8 | 278 | E-SS8.PR-8 | no |
| ch8 PR-9 | 278 | E-SS8.PR-9 | no |
| ch9 PR-3 | 300 | E-SS9.PR-3 | no |
| ch9 PR-4 | 301 | **no card** | — (see gaps-9.md) |
| ch10 PR-1 | 333 | E-SS10.PR-1 | no |
| ch10 PR-5 | 335 | E-SS10.PR-5 | no |
| ch10 PR-6 | 335 | E-SS10.PR-6 | no |
| App A PR-5 | 362 | **no card** | — (see gaps-appendix-a.md) |

(The same `∗` character also occurs inside mathematics — `Λ∗`, `E2∗`, `σ1∗`, `r8∗` — and is not a
marker; those were excluded.)

**No exercise anywhere carries the marker**; all 27 are in problems.

Whether this is a defect or an editorial decision (the schema has no field for it) is a judgement
call for the collection owner, but as a *fidelity* matter the printed information is lost on 22
extant cards, and the two ch3 cards still to be written would lose it as well unless a convention
is fixed first. If a convention is wanted, the cheapest is a `{.remark}` line like the one already
in E-SS2.PR-5, or a front-matter key such as `difficulty: starred`.

## 2. Card-by-card spot checks (9 cards read in full against the print)

| card | printed page | result |
|---|---|---|
| E-SS2.PR-1 | PDF 87–88 / printed 68 | statement, both parts and both hints match. **Exception:** part (b) is printed `(b) ∗` and the star is gone (row 1 above). |
| E-SS3.PR-1 | PDF 128 / printed 108 | matches, including "(a) … Compute fn′ (0), and discuss." and the closing Koebe–Bieberbach paragraph with the best constant r = 1/4. |
| E-SS3.PR-2 | PDF 128–129 / printed 108–109 | matches, including the `T (z) = (z0 − z)/(1 − z0 z)` hint (print: `T (z) = (z0 − z)/(1 − z0 z)` with an overline the OCR drops). |
| E-SS5.EX-17 | PDF 175–176 / printed 156 | matches. The card's remark is right that the print has `E ′ (z)` in the first denominator of the Pringsheim formula (raw OCR: `E ′ (z) z`), and that the `b_j` summand needs `E ′ (0)`. |
| E-SS5.PR-1 | PDF 175–176 / printed 156–157 | matches. The printed `[Hint: Use Jensen's formula.]` sits at the top of printed p. 157, split from the statement by a page break; the card keeps it. |
| E-SS5.PR-2 | PDF 176 / printed 157 | matches in content. The print's part (a) reads `(1 − αz)α` in the OCR; the ᾱ overline is lost by the OCR, not by the card (the card has `\overline{\alpha}`). |
| E-SS8.PR-9 | PDF 278–279 / printed 259–260 | matches; the hint of part (a) (`a0 ≥ … ≥ b0`, `an − bn ≤ (a − b)/2^n`) is retained, and (b) keeps the reference to Exercise 24(b). |
| E-SS9.PR-1 | PDF 300–301 / printed 281 | matches: S1 , S2 , S3 , the forbidden Eisenstein series F and its reverse F̃, and the comparison-integral hint. |
| E-SS9.PR-3 | PDF 300–301 / printed 281 | matches. The print has the integral over `4z3 − g2 z − g3` under a square root (OCR loses the radical); the card supplies `\sqrt{4z^3-g_2z-g_3}`. |

## 3. What this is not

Nine cards out of 206 were compared. **The other 197 statements were not diffed.** A dropped
hypothesis, a lost hint or a wrong sign in any of them would not be visible in this report. The
counting evidence in `gaps-summary.md` says nothing about whether a card's text is right.
