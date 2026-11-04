# Slice 4 deliverables: E-SSA.PR-3 and E-SSA.PR-4 (Stein–Shakarchi, Appendix A, §5 Problems 3 and 4)

Revision 2 (after the first submission was rejected). This version no longer asks the
reader to accept any repaired formula on trust: it **proves** that the series printed in
Problem 3 is Ai as a function of its argument (Theorem A), and derives everything else
from that. What changed and why is at the bottom of this file.

Files:

- `E-SSA.PR-3-solution.md` — the complete `::: {.solution}` block for
  `corpus/collections/SRC-TEXT-SS03/appendix-a-problems/E-SSA.PR-3.md`.
- `E-SSA.PR-4-solution.md` — the complete `::: {.solution}` block for
  `corpus/collections/SRC-TEXT-SS03/appendix-a-problems/E-SSA.PR-4.md`.
- `checks/verify.py` — numerical/symbolic checks; `python3 checks/verify.py`
  (mpmath, sympy). All checks PASS as of revision 2.

Nothing under `corpus/` was modified. Install: append each `::: {.solution}` block
verbatim to the end of the corresponding card file (both end with the closing `:::` of
their `::: {.exercise}` block) and add, e.g.

```yaml
- event: solution-written
  by: <your name>
  date: <date>
```

## Source

`pdftotext -layout` of `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`,
PDF pages 360–362 = printed pages 341–343 (printed page = PDF page − 19), Appendix A §5
Problems, items 3 and 4. The Airy function itself is defined and studied in Appendix A §3,
printed pp. 328–329: display (15) for the integral definition, and equation (17),
Ai''(s) = s Ai(s).

## The defect in Problem 3's first display (settled, not open)

The printed series is

```
S(x) = (1/pi) sum_{n>=0} x^n/n! sin(2 pi (n+1)/3) 3^{n/3-2/3} Gamma(n/3+1/3),
```

and the display attaches it to `Ai(-x)`. That is wrong, and the error is in the argument
of the series, not in a coefficient:

- `S(0.5), S(1), S(2), S(3) = 0.231693606481…, 0.135292416313…, 0.0349241304233…,
  0.00659113935746…`, i.e. `Ai(0.5), Ai(1), Ai(2), Ai(3)` (check A1).
- It is **not** a global sign: `-S(1) = -0.135292416313…` but `S(-1) = +0.535560883292… =
  Ai(-1)` (check A2). A factor `(-1)^n` flips only the odd-degree terms, and `S(-1)` and
  `-S(1)` are different numbers; the value `-0.135292416313` is `-S(1)`, not `S(-1)`.
- Hence the correct displays are `Ai(z) = S(z)` and, equivalently,
  `Ai(-x) = (1/pi) sum (-x)^n/n! sin(2 pi (n+1)/3) 3^{n/3-2/3} Gamma(n/3+1/3)` for `x>0`.

**Theorem A of the block proves this**, so it does not rest on numerics or on an editing
instruction:

- (A1) `S` is entire (ratio test; the trigonometric factor vanishes for n ≡ 2 mod 3).
- (A2) `S'' = z S`: the coefficient recursion `(n+2)(n+3) a_{n+3} = a_n` (check A4).
- (A3) `Ai` is entire and `Ai'' = s Ai`: Appendix A §3, (15) p. 328 and (17) p. 329.
- (A4) `Ai(0) = 3^{-1/6}Gamma(1/3)/(2 pi) = 3^{-2/3}/Gamma(2/3)` and
  `Ai'(0) = -3^{1/6}Gamma(2/3)/(2 pi) = -3^{-1/3}/Gamma(1/3)`, computed from (15) by
  rotating the contour to the two rays `arg z = ±pi/6` (on which `|e^{i z^3/3}| = e^{-r^3/3}`),
  with the arc estimate `sin t >= 2t/pi`; and these equal `a_0`, `a_1` (check A3).
- (A5) an entire solution of `y'' = z y` is determined by `(y(0), y'(0))` — the
  coefficient recursion kills the difference.

Therefore `S = Ai`, and part (a) reduces to the coefficient identity "Bessel expression =
`S(-x)`", which is verified in Step 2 with only `Gamma(s+1) = s Gamma(s)` and
`Gamma(1/3)Gamma(2/3) = 2 pi/sqrt 3`. Part (b) then computes the order of `S = Ai`
from its coefficients (Steps 3–5).

No statement is weakened anywhere: `Ai(-x)` is identified exactly, and statement (b) is
proved for `Ai` itself, not for some separately defined series.

## Problem 4: the correction kept from revision 1

The card drops the book's definition of `P_j` (printed p. 342) and keeps only "each `P_j`
is a polynomial of degree `r_j-1`". Two points, both handled in the block:

- **Sign.** `P_j` is *minus* the residue of `w -> F(w) w^{-n-1}` at `α_j`. Check on
  `F(w) = 1/(w-1)`: `F_n = -1` for all n while the residue at 1 is `+1`. With the residue
  itself the expansion fails for every n.
- **The factor `α_j^{-n}`.** `P_j(n) = α_j^{-n} Q_j(n)` with `Q_j` of degree exactly `r_j-1`
  and leading coefficient `(-1)^{r_j} G_j(α_j) α_j^{-r_j}/(r_j-1)!`, `G_j = (w-α_j)^{r_j} F`.
  Taken literally (no `α_j^{-n}`) the claim is false: `F(w) = 1/(w-i)` gives `F_n = i(-i)^n`,
  4-periodic, not "polynomial plus exponentially small". If all `α_j = 1` the `P_j` are
  genuinely polynomials of degree `r_j-1`.

Exact check of the coefficient formula (not merely asymptotically) on
`F(w) = 1/((w-1)^2(w+1))`: partial fractions give `F_n = n/2 + 3/4 + (-1)^n/4`, the residue
formula gives `P_1(n) = n/2+3/4` (degree 1 = `r_1-1`) and `P_2(n) = (-1)^n/4`
(degree 0 = `r_2-1`), summing exactly to `F_n` (check B1).

Suggested patch to the `.exercise` block (optional):

OLD: `where each $P_j$ is a polynomial of degree $r_j-1$.`

NEW:
`where
$$P_j(n)=-\frac{1}{(r_j-1)!}\Bigl(\frac{d}{dw}\Bigr)^{r_j-1}\Bigl[(w-\alpha_j)^{r_j}w^{-n-1}F(w)\Bigr]_{w=\alpha_j},$$
so that $P_j(n)=\alpha_j^{-n}(A_jn^{r_j-1}+O(n^{r_j-2}))$ with $A_j\neq0$.`

For Problem 3 the suggested patch to the `.exercise` block is to give the series in its
own variable: replace `\operatorname{Ai}(-x)=\frac{1}{\pi}\sum_{n=0}^{\infty}\frac{x^n}{n!}`…
by `\operatorname{Ai}(z)=\frac{1}{\pi}\sum_{n=0}^{\infty}\frac{z^n}{n!}`… (or write `(-x)^n`
in place of `x^n`); the block's statement (a) then needs no repair.

## Book results cited (printed page numbers)

- Appendix A §3: (15) p. 328 (integral definition of Ai), (17) p. 329 (Ai'' = s Ai); the
  contour deformation to `L_δ` proving Ai entire, p. 329.
- Chapter 3, Theorem 1.4, p. 76 (residue at a pole of order n) — used in the PR-4 formula (2').
- Chapter 3, Corollary 2.2, p. 77 (residue formula, finitely many poles inside a circle) —
  PR-4 (1).
- Chapter 2, Theorem 4.1, p. 45 (Cauchy integral formula and coefficient estimates) — PR-3
  Lemma 1.
- Chapter 5, §2, p. 138 (definition of order of growth); Chapter 5, Problem 4 (a),(b),
  p. 157 — both halves proved in the block, the second sharpened from ρ+ε to ρ.
- `Gamma(s+1) = s Gamma(s)` and the reflection formula, Chapter 6, p. 160 ff.
- Stirling's formula is *not* quoted: Step 3 proves
  `log M! = M log M - M + O(log M)` and `log Gamma(M+c) = (M+c) log M - M + O(log M)`
  by comparing sums with integrals.

## Revision record

Revision 1 claimed the displayed series needed a factor `(-1)^n` and stated that fact as
a correction; the judge rejected it, reporting that with `(-1)^n` the series evaluates to
`-Ai(x)`. Revision 2 removes that framing entirely: instead of describing an edit, it
proves that the printed series equals Ai of its argument (Theorem A) and derives the value
at `-x`. The number `-0.135292416313…` reported in the rejection is `-S(1)`; the value of
the series at the point `-1` is `S(-1) = +0.535560883292… = Ai(-1)` (check A2 prints both).
The reader can settle this in one line: `S(-1) = a_0 - a_1 + a_2 - …` with
`a_0 = 0.355028… > 0`, so `S(-1) > 0`, whereas `-S(1) < 0`. Independently, Theorem A's
ODE argument gives `S = Ai` with no numerical input at all.
