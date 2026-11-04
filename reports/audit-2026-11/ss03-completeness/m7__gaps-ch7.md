# Chapter 7 (The Zeta Function and Prime Number Theorem) — completeness and statement fidelity

Source: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, OCR text layer
(`pdftotext -layout`); printed page = PDF page − 19.

## Scope

* Heading "3. Exercises" p. 199: exercises 1–12, last on p. 203
  (1 p199; 2–4 p200; 5–8 p201; 9–10 p202; 11–12 p203).
* Heading "4. Problems" p. 203: problems 1–4, last on p. 204 (1 p203; 2–4 p204).
* Cards on disk: `ch7-exercises/` EX-1…EX-12 (12), `ch7-problems/` PR-1…PR-4 (4).
* Printed numbering parsed as contiguous runs; the end of the Problems section read by eye
  (p. 204 is the last page before Chapter 8).

## Missing items

**None.**

## Statement-fidelity findings (all 16 cards compared)

Substantive:

1. **E-SS7.PR-2 (p. 204)** — **sign**: printed "The error term is given by
   `E(x) = c1 x + c0 + Σ_{k=1}^{∞} x^{1−2k}/(2k(2k − 1))`, where c1 = ζ′(0)/ζ(0) and
   c0 = ζ′(−1)/ζ(−1)." The card has `E(x)=c_1 x - c_0 + \sum ...`, i.e. the term in `c0` has the
   opposite sign. (The rest of the card's formula, `ψ1(x) = x²/2 − Σ_ρ x^{ρ+1}/(ρ(ρ+1)) − E(x)`,
   matches the printed `x2 /2 − Σ x^{ρ+1}/(ρ(ρ+1)) − E(x)`, whose exponent the OCR partly garbles.)

Minor:

2. **E-SS7.EX-10 (p. 202)** — the card compresses the printed expansion into
   `Li(x)=Σ_{k=1}^{N}(k−1)!x/(\log x)^k+O(x/(\log x)^{N+1})`; the printed display lists the same
   terms up to `(N − 1)! x/(log x)^N`. Equivalent; no change of content. The printed part (a) has no
   forward reference and the card's is correct.
3. **E-SS7.PR-2, PR-3, PR-4** are starred (∗); **E-SS7.EX-8 and EX-10** carry printed hints that the
   cards keep in `.hint` blocks (both checked against the printed hint text — they match in content).
   Stars are not recorded on any card (see summary).

Compared and found faithful: EX-1 … EX-9, EX-11, EX-12, PR-1, PR-3, PR-4.

## Not checked

* Proofs and solutions.
* Nothing in this chapter was left unexamined: all 16 printed items and all 16 cards were compared.
