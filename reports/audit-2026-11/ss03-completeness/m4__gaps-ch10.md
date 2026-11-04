# SRC-TEXT-SS03 — Chapter 10 (Applications of Theta Functions)

**No missing cards.** Printed: 12 exercises (§4, PDF pages 328–333) and 6 problems (§5,
PDF pages 333–336); cards present: 12 and 6 (`E-SS10.EX-1..12`, `E-SS10.PR-1..6`).
PDF page 337 opens Appendix A. PDF page = printed folio + 19 (PDF 328 = printed 309,
PDF 336 = printed 317). Numbering verified contiguous in the print.

**"How many problems does chapter 10 print?" — six.** PR-1 … PR-6, PR-6 (starred, `r_8(n)`)
ending on PDF p. 336 with its parts (a)–(f) and the closing sentence "…which must be 1. This
gives the desired result." The collection's 6 cards are complete.

Scope of the fidelity claim: **all 18 cards**, statement blocks read against the printed
items, plus `remark` blocks and audit notes. No proof audited. One structural note: three
cards here carry a `source-corrected`/`source-checked` audit event and a `remark` that names
the printed wording they depart from, so the chapter's deviations are mostly on the record.

## Differences from the print, documented on the card

### `E-SS10.EX-1` (PDF p. 328) — "first two derivatives" → "first three"
Print: "where cτ can be expressed in terms of the **first two** derivatives of Θ(z|τ), with
respect to z, at z = 1/2 + τ/2."
Card: "… in terms of the **first three** derivatives of $\Theta(z \thetaseparator \tau)$ …"
The audit note reads "Repaired the published erratum: 'first two derivatives' should read
'first three derivatives'", and a remark explains that the constant term of the Laurent
expansion at `z₀ = 1/2 + τ/2` involves `Θ'''(z₀|τ)`. Documented.

### `E-SS10.PR-1` (PDF p. 333, starred) — "positive integers" → "nonnegative integers"
Print: "Suppose n is of the form n = 4a (8k + 7), where a and k are **positive integers**."
Card: "Suppose $n=4^a(8k+7)$, where $a$ and $k$ are **nonnegative integers**."
Audit event `source-corrected`: "Stein and Shakarchi Ch. 10, Problem 1 prints a,k positive.
Its converse then fails for n=7. The card uses nonnegative a,k so the stated three-square
theorem is true." Documented.
Second, smaller change in the same card: the print's closing sentence "The converse, that
every n that is not of that form can be written as the sum of three-squares, is a difficult
theorem of Legendre and Gauss" becomes "The converse for positive integers is the
three-square theorem of Legendre and Gauss." (the word "difficult" and the explicit
statement of the converse are gone; the substance survives).

### `E-SS10.PR-2` (PDF p. 333) — the fundamental domain is corrected, and "distinct" is added
Print: "F1 = {τ ∈ C : |τ | ≥ 1, |Re(τ )| ≤ 1/2 and **|Im(τ )| ≥ 0**}".
Card: "$\mathcal{F}_1 = \{\tau \in \CC : \abs{\tau} \geq 1,\ \abs{\Re(\tau)} \leq 1/2
\text{ and } \Im(\tau) > 0\}$".
The printed condition `|Im(τ)| ≥ 0` is vacuous; the card's `Im τ > 0` is the intended one.
A remark records it: "The source prints the condition |Im(τ)| ≥ 0 in F1; the domain lies in
H. Part (b) in the source omits 'distinct', although every τ is congruent to itself; it also
writes the congruent point as w in one place and τ′ in another." So the card also adds
"distinct" in part (b), also recorded.

## The one undocumented difference

`E-SS10.EX-4` (PDF p. 330). Print: "p(n) = p(n − 1) + p(n − 2) − p(n − 5) − p(n − 7) **− · · ·**";
card: `p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) \mathbf{+ \cdots}`. The trailing sign differs
(the Euler recurrence continues `+p(n−12)+p(n−15)−…`, so the card is right and the printed
`−` is a typo or an OCR slip). The card has only a `solution-written` audit event and no
remark, so the change is not recorded. Trivial, but it is the only unrecorded statement
difference in the chapter.

## Checked and faithful (no action)

EX-2 (Fibonacci generating function, parts (a)–(d), `A = 1/√5`, `B = −1/√5`), EX-3
(two-term recurrence), EX-5 (`log F(x) ∼ π²/(6(1−x))` and its long hint), EX-6
(`e^{c₁n^{1/2}} ≤ p(n) ≤ e^{c₂n^{1/2}}` with the two-sided hint), EX-7 (the triangular- and
septagonal-number identities, brackets and all), EX-8 (Pythagorean triples with the
`b² = (c−a)(c+a)` hint), EX-9, EX-10 (`r₂`/`r₄` irregularities with hint), EX-11 (divisor
sums), EX-12 (`θ⁴` identity, hint `x/(1−x)² = Σnxⁿ`), PR-3 (the group `G`, `S`, `T₂`), PR-4
(the `Σy_k = ∞` condition, read correctly from an OCR that drops the Σ), PR-5
(`Δ(τ) = (2π)^{12}η^{24}(τ)`, hint present as a `hint` block), PR-6 (all six parts plus the
combined hint; the print's "Theorem: r8(n) = 16σ3∗(n)" framing is folded into the statement,
which is a presentation change, not a change of content).
The starredness of PR-1, PR-5, PR-6 is not recorded on the cards (no card in the collection
records it — see `gaps-summary.md`).
