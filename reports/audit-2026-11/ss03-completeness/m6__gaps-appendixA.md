# Appendix A (Asymptotics) — gaps: the whole section is uncarded

> **Status note (added after the audit).** When this audit was run there was no appendix
> directory at all. A later applying pass has since created `appendix-a-problems/` with
> `E-SSA.PR-1.md` … `E-SSA.PR-5.md` — the id scheme proposed below, under the directory name
> `appendix-a-problems` rather than `appA-problems`. All five statements match the printed
> items quoted below. The gap is closed; the quotes remain the reference.

Printed section: `5 Problems`, PDF 360–362 (printed pp. 341–343), items 1–5, contiguous
(5∗ starred). Appendix A prints **no** Exercises section — the heading scan of PDF 337–362
finds only `5 Problems` / `5. Problems`.

Cards on disk: **none.** `corpus/collections/SRC-TEXT-SS03/` has the directories
`ch1-exercises` … `ch10-problems` and nothing for either appendix, so Appendix A's five
problems have no card and no home directory.

Proposed target directory and ids (a naming decision the human has to make, since `E-SS<chapter>`
has no appendix case): `corpus/collections/SRC-TEXT-SS03/appA-problems/E-SSA.PR-1.md` …
`E-SSA.PR-5.md`. (Alternative: `appendixA-problems/E-SS11.PR-n.md`.)

---

### Problem 1 — PDF p. 360–361 (printed p. 341–342)

Printed statement (OCR, verbatim, displays collapsed; the OCR for part (b) is badly
scrambled — `∫ $ d/dx ^k % m (x ) e−sx η(x) dx` — and only the page image can settle it):

> 1. Let η be an indefinitely differentiable function supported in a finite interval, so
> that η(x) = 1 for x near 0. Then, if m > −1 and N > 0,
> ∫_0^∞ e^{−sx} x^m η(x) dx = s^{−m−1} Γ(m + 1) + O(s^{−N})
> for Re(s) ≥ 0, |s| → ∞.
> (a) Consider first the case −1 < m ≤ 0. It suffices to see that
> ∫_0^∞ e^{−sx} x^m (1 − η(x)) dx = O(s^{−N}),
> and this can be done by repeated integration by parts since
> e^{−sx} = (−1)^N s^{−N} (d/dx)^N (e^{−sx}).
> (b) To extend this to all m, find an integer k so that k − 1 < m ≤ k, write
> (∫ (x^m) e^{−sx} η(x) dx = c_{k,m} s^{−m+k−1} + O(s^{−N}),)
> and integrate by parts k times.

Suggested title: “Watson's lemma with a cutoff: ∫ e^{−sx} x^m η(x) dx”.

### Problem 2 — PDF p. 361 (printed p. 342)

> 2. The following is a more precise version of Stirling's formula. There are real
> constant a1 = 1/12, a2 , . . ., an , . . ., so that for every N > 0
> Γ(s) = e^{s log s −s} √(2π) s^{1/2} (1 + Σ_{j=1}^{N} aj s^{−j} + O(s^{−N}))
> when s ∈ Sδ .
> This can be proved by using the results of Problem 1 in place of Proposition 1.3.

Suggested title: “Stirling's formula with the asymptotic series in powers of 1/s”.

### Problem 3 — PDF p. 361 (printed p. 342)

> 3. The Bessel functions and Airy function have the following power series expansions:
> Jν (x) = … (−1)^m / (m! Γ(ν + m + 1)) … ,  Ai(−x) = (1/π) Σ xn/n! sin(2π(n + 1)/3) 3^{n/3−2/3} Γ(n/3 + 1/3).
> (a) From this, verify that when x > 0,
> Ai(−x) = x^{1/2} ( J_{1/3}(2x^{3/2}/3) + J_{−1/3}(2x^{3/2}/3) ).
> (b) The function Ai(x) extends to an entire function of order 3/2.
> [Hint: For (b), use (a), or alternatively, apply Problem 4 in Chapter 5 to the power
> series for Ai. Compare also with Problem 1, Chapter 4.]

(The two series displays are scrambled in the OCR — `x2` and `x` fragments appear out of
order. The bracketed hint is verbatim.)

Suggested title: “Airy function as a Bessel function of order ±1/3; order 3/2”.

### Problem 4 — PDF p. 361–362 (printed p. 342–343)

> 4. Suppose F (z) = Σ_{n=0}^{∞} Fn w n is meromorphic in a region containing the closed
> unit disc, and the only poles of F are on the unit circle at the points α1 , . . . , αk ,
> and their orders are r1 , . . . , rk respectively. Then for some ǫ > 0
> Fn = Σ_{j=1}^{k} Pj (n) + O(e^{−ǫn}) as n → ∞.
> Here Pj (n) = 1/(rj − 1)! (d/dw)^{rj −1} ( (w − αj )^{rj} w^{−n−1} F (w) ) |_{w=αj} .
> Note that each Pj is of the form Pj (n) = Aj (αj^{−1} n)^{rj −1} + O(n^{rj −2}).
> To prove this, use the residue formula (Theorem 1.4, Chapter 3).

(The OCR prints `F (z) = Σ Fn w n`, i.e. it loses the distinction between the variable of the
series and the variable of meromorphy; transcribe from the page image.)

Suggested title: “Polynomial-plus-exponential asymptotics of Taylor coefficients from poles”.

### Problem 5 — PDF p. 362 (printed p. 343). Starred in print.

> 5.∗ The one shortcoming in our derivation of the asymptotic formula for p(n) arose
> from the fact that while f1 (z) = z/i e^{πiz/12} e^{πi/12z} is a good approximation to the
> generating function f (z) near z = 0, this fails near other points on the real axis,
> since f1 is regular there, but f is not.
> However, using the transformation law (24) and the identity f (z + 1) = f (z),
> one can derive the following generalization of (24): whenever p/q is a rational
> number in lowest form (so p and q are relatively prime) then
> f (z − p/q) = ωp/q (zq/i)^{1/2} e^{πizq/12} f ( − p′/(zq 2) − 1/(zq 2) q ) ,
> where pp′ = 1 mod q. Here ωp/q is an appropriate 24th root of unity. This formula
> leads to an analogous fp/q , approximating f at z = p/q.
> From this one can obtain for each p/q a contribution of the form
> c_{p/q} (d/(2π 2 dn)) ( K e^{q(n−1/24)^{1/2}} / (n − 1/24)^{1/2} )
> to the asymptotic formula for p(n). When suitably modified, the resulting series,
> summed over all proper fractions p/q in [0, 1), actually converges and gives an
> exact formula for p(n).

The displayed transformation law is **unreadable in the OCR** (fragments
`iπz iπzq 2 − 12 p′ − zq 2 q` out of order); the page image must be transcribed, not the
text layer. The prose around it is legible and quoted verbatim.

Suggested title: “Transformation law for the partition generating function at rational points
and Rademacher's exact formula for p(n)”.

---

Note for whoever adds these: problems 2, 3, 4 and 5 are internal cross-references of the book
(they refer back to Appendix A Problem 1, Chapter 5 Problem 4, Chapter 4 Problem 1,
Chapter 3 Theorem 1.4 and Chapter 10 Problem 6), so the card ids used here will be cited from
other cards.
