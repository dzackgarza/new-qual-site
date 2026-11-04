# Statement fidelity — bracketed hints dropped by the corpus (SRC-TEXT-SS03)

Cheap check, run over all 206 cards: for every printed item that carries a bracketed
`[Hint: …]`, does the card's `::: {.exercise}` block contain a hint at all? Method: split each
printed section's OCR text into items by their number line, collect `[Hint` occurrences; for each
card, read the `.exercise` fenced block and search for hint text. Pages are PDF pages of
`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (printed page = PDF − 19). All 14 hits
below were then confirmed by reading the printed page and the card block by hand; no card was
edited.

## Confirmed: printed item has a `[Hint: …]`, card statement has none (14)

| # | card | hint on (PDF p. / printed p.) | printed hint (OCR) |
|---|---|---|---|
| 1 | `ch1-exercises/E-SS1.EX-15.md` | 47 / 28 | `[Hint: Sum by parts.]` |
| 2 | `ch1-exercises/E-SS1.EX-16.md` | 47 / 28 | `[Hint: Use Stirling's formula, which says that 1/n! ∼ cn^n+1/2 e−n for some c > 0.]` (OCR garbles the exponent) |
| 3 | `ch1-exercises/E-SS1.EX-18.md` | 48 / 29 | `[Hint: Write z = z0 + (z − z0 ) and use the binomial expansion for z n .]` |
| 4 | `ch1-exercises/E-SS1.EX-21.md` | 49 / 30 | `[Hint: Use the dyadic expansion of an integer and the fact that 2^k+1 − 1 = 1 + 2 + 2² + · · · + 2^k .]` |
| 5 | `ch4-problems/E-SS4.PR-3.md` | 152 / 133 | `[Hint: For part (a), apply the maximum modulus principle to Fǫ (z) = F (z)e−ǫz . For part (b), consider M0^z−1 M1^−z F (z).]` |
| 6 | `ch7-exercises/E-SS7.EX-8.md` | 221 / 202 | `[Hint: To prove (a) and (b) use the functional equation for ζ(s). For (c), use a result of Hadamard, which states that an entire function with fractional order has infinitely many zeros.]` |
| 7 | `ch7-exercises/E-SS7.EX-10.md` | 221 / 202 | `[Hint: Integrate by parts in the definition of Li(x) and observe that it suﬃces to prove ∫_2^x dt/(log t)² = O(x/(log x)²). To see this, split the integral from 2 to √x and from √x to x.]` |
| 8 | `ch8-exercises/E-SS8.EX-13.md` | 270 / 251 | `[Hint: Consider the automorphism ψα (z) = (z − α)/(1 − αz) and apply the Schwarz lemma to ψ^{-1}_{f (w)} ◦ f ◦ ψw .]` |
| 9 | `ch8-problems/E-SS8.PR-4.md` | 276 / 257 | `[Hint: Use the following association.]` + a displayed matrix $z\mapsto\frac{az+b}{cz+d}$ association with $e^{2i\theta}\frac{z-\alpha}{1-\bar\alpha z}$. The card also drops the display. |
| 10 | `ch8-problems/E-SS8.PR-7.md` | 277 / 258 (parts a,b) and 278–279 / 258–259 (parts c,d) | `[Hint: Write f (z) = zg(z) and use the maximum principle to prove that |f ′ (0)| = |g(0)| > 1.]`, `[Hint: Prove that the sequence {|Fn′ (0)|} has a limit by showing that it is bounded above and monotone increasing. Use the Schwarz lemma.]`, `[Hint: If rF (K0 ) ≥ 1 then F is surjective.]`, `[Hint: To prove that |f (z)| > |z| on K − {0} apply the Schwarz lemma to the inverse function, namely ψα ◦ g ◦ ψβ where g(z) = z².]` — the card keeps parts (a)–(e) but none of the four hints. |
| 11 | `ch8-problems/E-SS8.PR-9.md` | 279 / 260 | `[Hint: Show that a ≥ a1 ≥ a2 ≥ · · · ≥ an ≥ bn ≥ · · · ≥ b1 ≥ b and an − bn ≤ (a − b)/2^n .]` |
| 12 | `ch9-problems/E-SS9.PR-3.md` | 301 / 282 | `[Hint: Prove that (I(℘(z + α)))′ = ±1, and use the fact that ℘ is even.]` |
| 13 | `ch10-problems/E-SS10.PR-5.md` | 335 / 316 | `[Hint: △ and η^24 satisfy the same transformation laws under τ → τ + 1 and −1/τ . Because of the fundamental domain described in Problem 2, it suﬃces then to investigate the behavior at the only cusp, which is at infinity.]` |
| 14 | `ch10-problems/E-SS10.PR-6.md` | 336 / 317 | `[Hint: Use the fact that E4 (τ ) = 2ζ(4) + (2π)^3 Σ σ3 (k)e^2πikτ and ζ(4) = π^4/90.]` (part (a)) and `[Hint: Verify that E4∗ (1 − 1/τ ) = τ^4 (E4 (τ ) − E4 (2τ )).]` (part (f)) |

Case 1 is worth a note because the layout is unusual: the hint is printed *inside* the statement,
between the display and the sentence "In other words, if a series converges, then it is Abel
summable with the same limit" (PDF 47), so a transcriber reading only the display would miss it.

## Candidate checks that turned out clean

My first automated pass also flagged five cards whose statement mentions a hint although the
printed item appeared to have none (`ch2-exercises/E-SS2.EX-13`, `E-SS2.EX-15`,
`ch6-exercises/E-SS6.EX-17`, `ch7-problems/E-SS7.PR-1`, `ch8-exercises/E-SS8.EX-24`). All five are
artefacts of OCR line ordering — e.g. the hint for EX-13 sits on PDF 85 after the previous item's
display — and the printed items do carry those hints. **No card invents a hint.**

## Scope

Only the *presence* of the bracketed hint was checked, not its wording. Whether a card's hint is a
faithful rendering (e.g. OCR'd symbols repaired correctly) is not covered. Statement wording — dropped
hypotheses, signs, exponents — is not covered here either; my pass read only 14 blocks plus 5
controls. The 14 findings are complete for the corpus as it stands (206 cards) with respect to
"does any hint text appear at all".
