# Appendix A (Asymptotics) — completeness

Source: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, OCR text layer
(`pdftotext -layout`); printed page = PDF page − 19.

## Scope

* Appendix A prints one section of problems and no exercises: heading "5. Problems" on p. 341,
  problems 1–5, last on p. 343 (1 p341; 2–4 p342; 5 p343).
* Cards on disk at 16:12 UTC: **none.** There was no appendix directory under
  `corpus/collections/SRC-TEXT-SS03/`, no `E-SSA.*` / `E-SSApp.*` card anywhere in `corpus/`, and no
  mention of Appendix A in `index.md`. At 16:18 UTC `appendix-a-problems/` with `E-SSA.PR-1` …
  `E-SSA.PR-5` appeared (see "Missing items").
* Appendix B (Simple Connectivity and Jordan Curve Theorem) prints **no** exercises and no problems
  (its table-of-contents entry ends at "2.1 Proof of a general form of Cauchy's theorem", p. 361).

## Missing items

**Status of this finding.** At the inventory pass (16:12 UTC) there was no `appendix-a-problems/`
directory and no appendix card anywhere. At 16:18 UTC, while this audit was still running, the
directory `appendix-a-problems/` with `E-SSA.PR-1.md` … `E-SSA.PR-5.md` appeared on disk (concurrent
work by another worker — this audit did not create them; the id prefix is the one this file proposed).
Their statements were then compared with the printed text: see "Late-arriving cards" at the end.
`index.md` had not been updated at that point and still has no Appendix A section.

At the time of the inventory pass all five printed problems were missing.

**Caution on the quotes:** the OCR layer mangles the displays in Problems 1, 2, 3 and 5 badly
(superscripts, roots and fraction bars are dropped or displaced). Problems 3 and 5 below are
reconstructions of those displays from context, not literal transcriptions; every symbol must be read
off the page image before a card is written. Problem 4's text is nearly clean.

| item | book page | printed statement (OCR text layer, symbols may be mangled) | card that should exist |
|---|---|---|---|
| Problem 1 | p. 341 | "1. Let η be an indefinitely differentiable function supported in a finite interval, so that η(x) = 1 for x near 0. Then, if m > −1 and N > 0, ∫_0^∞ e^{−sx} x^m η(x) dx = s^{−m−1} Γ(m + 1) + O(s^{−N}) for Re(s) ≥ 0, \|s\| → ∞. (a) Consider first the case −1 < m ≤ 0. It suffices to see that ∫_0^∞ e^{−sx} x^m (1 − η(x)) dx = O(s^{−N}), and this can be done by repeated integration by parts since e^{−sx} = (−1)^N s^{−N} (d/dx)^N (e^{−sx}). (b) To extend this to all m, find an integer k so that k − 1 < m ≤ k, write ∫ (d/dx)^k (x^m) e^{−sx} η(x) dx = c_{k,m} s^{−m+k−1} + O(s^{−N}), and integrate by parts k times." | `corpus/collections/SRC-TEXT-SS03/appA-problems/E-SSA.PR-1.md` (directory and id prefix are a proposal — see note) |
| Problem 2 | p. 342 | "2. The following is a more precise version of Stirling's formula. There are real constant a1 = 1/12, a2 , . . ., an , . . ., so that for every N > 0 Γ(s) = e^{s log s −s} √(2π)/s^{1/2} (1 + Σ_{j=1}^{N} a_j s^{−j} + O(s^{−N})) when s ∈ S_δ . This can be proved by using the results of Problem 1 in place of Proposition 1.3." | `…/appA-problems/E-SSA.PR-2.md` |
| Problem 3 | p. 342 | "3. The Bessel functions and Airy function have the following power series expansions: Jν (x) = (x/2)^ν Σ_{m=0}^{∞} (−1)^m (x²/4)^m / (m! Γ(ν + m + 1)), Ai(−x) = (1/π) Σ_{n=0}^{∞} (x^n/n!) sin(2π(n + 1)/3) 3^{n/3−2/3} Γ(n/3 + 1/3). (a) From this, verify that when x > 0, Ai(−x) = (x^{1/2}/3)(J_{1/3}((2/3)x^{3/2}) + J_{−1/3}((2/3)x^{3/2})). (b) The function Ai(x) extends to an entire function of order 3/2. [Hint: For (b), use (a), or alternatively, apply Problem 4 in Chapter 5 to the power series for Ai. Compare also with Problem 1, Chapter 4.]" | `…/appA-problems/E-SSA.PR-3.md` |
| Problem 4 | p. 342 | "4. Suppose F (z) = Σ_{n=0}^{∞} F_n w^n is meromorphic in a region containing the closed unit disc, and the only poles of F are on the unit circle at the points α1 , . . . , αk , and their orders are r1 , . . . , rk respectively. Then for some ǫ > 0 F_n = Σ_{j=1}^{k} P_j (n) + O(e^{−ǫn}) as n → ∞. Here P_j (n) = (1/(r_j − 1)!) (d/dw)^{r_j −1} ((w − α_j)^{r_j} w^{−n−1} F (w))|_{w=α_j}. Note that each P_j is of the form P_j (n) = A_j (α_j^{−1} n)^{r_j −1} + O(n^{r_j −2}). To prove this, use the residue formula (Theorem 1.4, Chapter 3)." | `…/appA-problems/E-SSA.PR-4.md` |
| Problem 5∗ | p. 343 | "5.∗ The one shortcoming in our derivation of the asymptotic formula for p(n) arose from the fact that while f1 (z) = √(z/i) e^{iπ/(12z)} e^{iπz/12} is a good approximation to the generating function f (z) near z = 0, this fails near other points on the real axis, since f1 is regular there, but f is not. However, using the transformation law (24) and the identity f (z + 1) = f (z), one can derive the following generalization of (24): whenever p/q is a rational number in lowest form (so p and q are relatively prime) then f (z − p/q) = ω_{p/q} (zq/i)^{1/2} e^{iπ/(12zq)} e^{−iπzq/12} f (−1/z − p′/q), where pp′ ≡ 1 mod q. Here ω_{p/q} is an appropriate 24th root of unity. This formula leads to an analogous f_{p/q} , approximating f at z = p/q. From this one can obtain for each p/q a contribution of the form c_{p/q} √(2π) (1/2) d/dn (n − 1/24)^{1/2} e^{(K/q)(n − 1/24)^{1/2}} to the asymptotic formula for p(n). When suitably modified, the resulting series, summed over all proper fractions p/q in [0, 1), actually converges and gives an exact formula for p(n)." | `…/appA-problems/E-SSA.PR-5.md` |

### Note on the directory and id

The collection's id scheme is `E-SS<chapter>.EX-<n>` / `E-SS<chapter>.PR-<n>` with chapter a single
number. The book's Appendix A is not a numbered chapter, so the id needs a human decision. Two
workable choices: `E-SSA.PR-<n>` in `appA-problems/`, or treat the appendix as chapter 11
(`E-SS11.PR-<n>` in `ch11-problems/`) — but note the book has **no** Chapter 11, so the first option
does not collide with anything. Whichever is chosen must also be added to `index.md` as a new
section ("Appendix A Problems") and to any id regexes the tooling uses.

## Late-arriving cards (16:18 UTC) — statement check

* `E-SSA.PR-1` — matches (η supported in a finite interval with η = 1 near 0; the m > −1, N > 0
  asymptotic; parts (a) and (b) including the integration-by-parts identity and `c_{k,m}s^{−m+k−1}`).
* `E-SSA.PR-2` — matches (a1 = 1/12, the expansion inside `Γ(s) = e^{s log s − s}(√(2π)/s^{1/2})(…)`,
  `s ∈ S_δ`, and the remark about Problem 1 vs Proposition 1.3). "real constant" in print vs "real
  constants" on the card is a typo-level difference.
* `E-SSA.PR-3` — matches (both series, the J_{±1/3} identity, order 3/2, and the hint).
* `E-SSA.PR-4` — **statement loss.** The printed problem gives the explicit form of the polynomials:
  `P_j (n) = (1/(r_j − 1)!) (d/dw)^{r_j −1} ((w − α_j)^{r_j} w^{−n−1} F (w))|_{w=α_j}`, adds
  "Note that each P_j is of the form `P_j (n) = A_j (α_j^{−1} n)^{r_j −1} + O(n^{r_j −2})`", and ends
  with the instruction "To prove this, use the residue formula (Theorem 1.4, Chapter 3)." The card
  replaces all three by "where each $P_j$ is a polynomial of degree $r_j-1$". The formula for P_j is
  the substance of the problem; the card should carry it, plus the residue-formula instruction.
* `E-SSA.PR-5` — present in full, including the `ω_{p/q}` clause, the `pp′ ≡ 1 mod q` condition and
  the closing paragraph; two symbols deserve an image check: the card writes `f_1(z) = (z/i)e^{…}`
  where the OCR shows `z/i` preceded by a possible radical (the standard normalisation is
  `√(z/i)`), and the exponents of the transformation law (`e^{πi/(12zq²)}`, `e^{−πiz/12}`,
  `f(−1/(zq²) − p′/q)`) cannot be verified against the mangled OCR display. The contribution formula
  `c_{p/q} (1/(2π√2)) d/dn[(n − 1/24)^{−1/2} e^{(K/q)(n − 1/24)^{1/2}}]` also cannot be checked
  against the OCR, which scrambles that display.

## Also needed

`corpus/collections/SRC-TEXT-SS03/index.md` has no "Appendix A Problems" section and does not list
`E-SSA.PR-1` … `E-SSA.PR-5`; it still says `completion: complete`.

## Not checked

* Appendix B (no exercises/problems are printed there — only two sections of text).
* Proofs and solutions of the five appendix problems.
