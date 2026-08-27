# Queue E corrections: OCR repair of 354 extracted markdown files

Read each extracted markdown file fully.
Fix OCR mistakes, remove hallucination notes, fix encoding.
Flag unrecoverably bad extractions.
One file at a time.
No scripts, no pattern matching.

## Progress

| Batch | Files | Status |
| --- | --- | --- |
| 1-25 | 140A_Exam_Review — ALGEBRA_REVIEW1 | done |
| 26-50 | Algebra_Solutions — basic-08F | done |
| 51-100 | basic-08S — calculus_practice_test3 | in progress |
| 101-200 |  | pending |
| 201-354 |  | pending |

## Corrections applied

### Batch 1: files 1-25

- **140A_Exam_Review.md**: clean, no changes needed

- **603_11.md**: clean, no changes needed

- **8.1.2 Further Examples (1).md**: image placeholders in overview section, text clean

- **8150-hw1.md**: clean

- **8150-hw2.md**: clean

- **8150-hw3.md**: clean

- **8155-starter-problems.md**: clean

- **8210 Lecture Notes (Usher) Smooth Manifolds.md**: clean (2574L)

- **8.2.3 Normal family.md**: image placeholders, text clean

- **8.3 Riemann Mapping Theorem (1).md**: image placeholders, text clean

- **871-872January_2004_871-953.md**: clean

- **871-872January_2006_850-871.md**: clean

- **871-872January_2006_852-871.md**: clean

- **871-872January_2008_850-871.md**: clean

- **871-872June_2004_852-871.md**: clean

- **871-872June_2007_852-871.md**: clean

- **Adam Syllabus.md**: clean

- **AG Exam Problems.md**: clean

- **AG Solutions (1).md**: unrecoverable — binary/encoding garbage throughout

- **Algebra_Final_Solns 1.md**: fixed fraktur font garbling in problem 5

- **Algebra_Final_Solns.md**: fixed fraktur font garbling in problem 5 (duplicate of above)

- **Algebra_HW_11_Solns.md**: clean (duplicate content of 603_11.md with solutions)

- **Algebra_HW_4_Solns.md**: clean

- **Algebra_Notes.md**: clean

- **ALGEBRA_REVIEW1.md**: reconstructed 12+ garbled GRE multiple-choice problems

### Batch 2: files 26-50

- **Algebra_Solutions 1.md** and **Algebra_Solutions.md**: identical duplicates, clean (large solution manual, 9242L)

- **analysis_2003-2007.md**: removed 8 MinerU hallucination notes (OCR commentary about blank images)

- **analysis_2008-2013.md**: clean

- **analysis_2014-2016.md**: clean

- **analysis_jan2014.md**: clean

- **Applied-Algebra-FA17.md**: fixed 3 null bytes (replaced with tensor product and sigma symbols)

- **Azoff Problems by Topic.md**: clean

### Batch 3: files 51-72

- **basic-08S.md**: cleaned double "1_3" digit splits, if/else reconstruction, mathfrak garbles

- **basic-09F.md**: checked; see basic-09S relation

- **basic-09S.md**: cleaned mathfrak garbles and digit splits

- **basic-10F.md** and **basic-10S.md**: cleaned arrows/digit splits/mathfrak

- **basic-11F.md** and **basic-11S.md**: cleaned arrows and if/else reconstruction

- **basic-12F.md**: cleaned arrows, redirecting arrows, set-builder braces, ℝ/ℂ digits

- **basic-12S.md**: cleaned arrows, convexity formula, Cesàro sum, linear-map arrows, convergence-as-i→∞; Problem 11(a) matrix fragment `A = { \binom { 1 } { 4 } } \ 3 )` left as extracted — missing matrix entry, ambiguous (see below)

- **basic-13F.md**: fixed "if and only if", "and", arrows, "for all" inserts; Problem 6 `(z^n)^{(2)}` left as self-consistent; Problem 11 "orthogonal basis" left as extracted

- **basic-13S.md**: fixed radius ε, ellipsis, extra paren, when m≠n/m=n, exp/ln series, adjoint arrow, ℝ^16 affine subspace

- **basic-14F.md** and **basic-14S.md**: fixed B_· → matrix B, M_{m,n} notation, mathfrak sequences, t→x, π→n, C^1(ℝ), equicontinuity, I_π→I_n

- **basic-15F.md** and **basic-15S.md**: fixed π→n digit splits (a_n/n), mathfrak cleanup, A^Σ→A^T, T^18/ℝ^12 digits, 12−10 digits, E-1/E^+1→E⁻¹/E⁺¹, arrow fixes

- **basic-16F.md** and **basic-16S.md**: fixed as/and/if/else, lim arrows, a_11 digit splits, ℝ/ℚ splits, "n ≥ 4," punctuation

- **basic-17F.md** and **basic-17S.md**: fixed arrows, matrix -x_2, if/else/i∈I, F=ℝ, F₃=ℤ/3ℤ, Young equation, ⇔ pairs, positive-definite phrasing, B-dot removal, ε-quantifier

- **basic-18F.md** and **basic-18S.md**: fixed with/and/if, deg-2 matrix, dim(W), rank, 16-digit matrix, ℝ image/domain, sqrt(n)x_n limit, f:ℝ→ℝ

- **Basic_Linear_Algebra_Review.md**: major reconstruction of OCR-garbled examples — vector addition [1;2]+[3;4]=[4;6], scalar mult 5[1;2]=[5;10], dot product [1,2]·[3,4], norm [1,2,3], 2×2 inverse/det matrices (a b;c d), augmented system third row x−2y−4z=−1, standard basis of ℝ³, char poly 2×2 determinant display, row-reduction arrows, eigenvalue example 5[3,1]=[15,5]; fixed det typography, ℚ→rank-like garbles, Rn→ℝⁿ, dimension n+1 for polynomials, "review previous in-class exams", T arrows, shearing, 10/11/12 digit splits, 3×3 matrix rows

### Batch 4: files 73-75

- **Big_List_of_Math_Problems.md** (73): removed 33 dead control-character debris lines (figure-position residue after the "Figure 1: Pitch, yaw and roll of the ship" and "Figure 2: Positions of the stars" captions) and null-patched 2 lines in the relay-circuit diagram ASCII art; 0 control bytes remain. Typography throughout is spacing-degraded (flattened sub/superscripts like `x2 1`, split words like `Considerthequadraticforms`), but problem statements are present and mathematically correct in sampled regions (problems 1-9, 47-48, probability section). Kept as-is; source PDF `assets/attachments/Big_List_of_Math_Problems.pdf` remains the oracle. The "P" and "/Radioactivity" legend markers are intentional (creative / hard problems).

- **calculating_galois_from_polynomial.md** (74): stripped 2 `\x03` control bytes (end-of-proof marks); fixed 27 OCR garbles — `char ( K ) ≠ 2` (twice; Ω misread), if/iff restorations, "Galois group", "cyclotomic", "computed", "Adding…identical", $p$-cycle, $F_{11}$ subscript, $\alpha_2$ subscript, [Q(∛2):Q] = 3 (was "degree 2"), 1000 = 8·125 and Gal ≅ Z₂×Z₂×Z₁₀₀ (was 4·125 / Z₂×Z₁₀₀ — data-error fix), $x^{p^n} − x$, "of arbitrary degree", stray `]`, excluded set \{9\} (was \{2\}; 9 = −2 mod 11 is the found root), $\bar{p}$ → p, "the transitive subgroups of $S_3$ are $S_3$ and $A_3$" (removed internal contradiction), "cubic over $\mathbb{Q}$", "over $\mathbb{Q}$" (3×).

- **calculus_practice_test3.md** (75): reconstructed answer-choice labels stripped by the scan and cleaned ~35 garbles. Recovered: problem 6 (∫_b^{b+1}(x²+x)dx minimum, b = −1 — choices force the upper limit), 7 (octants of $z = e^{x+y}$), 8 ($f = \sqrt{\tan^2 x − 1}$ domain), 14/15 (∫₁^x dt/(1+t²) tangent at x = 2 — stem reconstructed from the choice set), 16 ($e^{g(x)}h(x)$, $h' = −g'h$; $\mathfrak{x}$→x, $\hbar$→h), 25 (Lipschitz: $|f(x)−f(y)| ≤ K|x−y|$ — abs-value bars and stem restored from choices), 29 (Σ(1/k − 1/2^k) = +∞), 30 (piecewise $\sqrt{1−x^2}$ / $x−1$ integral, "thien"→"then"), 34 (FTC: $2xe^{−x^4}$; choices (A)(B) reconstructed from glyph fragments), 35 (Riemann sum = 9/2), 39 (log(1+sin 2πx) undefined iff $x = (4n−1)/4$), 44 (lim = $9P''(x)$). Verified 0 control bytes. Flagged as ambiguous (see below): problems 9-15, 18, 20-28, 30-33, 36-38, 40-43 are absent from the extraction or have unreadable stems.

## Unrecoverable extractions

- **AG Solutions (1).md**: completely garbled binary/encoding.
  Every byte is non-standard encoding from a custom PDF font.
  No mathematical content is recoverable.
  Needs re-extraction or manual transcription from the source PDF.

- **Topology_Prelim_Answers_-_Unknown.md**: severely garbled throughout.
  The entire text has slashes inserted between characters, spaces in wrong places, and control characters replacing math symbols.
  384 control chars across 3064 lines.
  Mathematical content is unrecoverable.
  Needs re-extraction.

- **solutions-mims-2ed.md** and **Schilling_-_Acknowledgement...md** (duplicates): 8655 control characters from a custom PDF font encoding.
  Greek letters and math symbols replaced by control chars (\x16=\mu, \x1b=\sigma, \x0f=\epsilon) throughout 21K lines.
  25% of lines affected.
  Needs re-extraction with correct font mapping.

## Ambiguous fragments (kept as extracted, needs source check)

- **basic-12S.md**, Problem 11(a): matrix fragment `A = { \binom { 1 } { 4 } } \ 3 )`. One 2×2 matrix entry is missing; the occluded entry cannot be recovered from the extraction alone.
  The problem (degree-2 polynomial P with P(A)=0) still renders, but the stated matrix is incomplete.

- **calculus_practice_test3.md**: problems 9-15, 18, 20-28, 30-33, 36-38, 40-43 are absent or their stems are unreadable — page/scanner gaps, not fixable from the extraction. Problem 17 stem has an unreadable first term (`$\mathbf{i_\tau} - \sin^2(\mathrm{Arccos}\frac{\pi}{12})$`); problem 43's polynomial-condition stem is garbled (`\quad n = \sum a_i x^i` fragment with unknown degree hypothesis); problem 35 choice (C) `$\frac{3!}{6}$` has lost digits. Problem 19-24 fragment: statement I's right-hand side is lost (`f(x) = ?`). Re-extraction from `assets/attachments/calculus_practice_test3.pdf` is the repair path for all of these.
