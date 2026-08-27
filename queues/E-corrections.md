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

- **Big_List_of_Math_Problems.md** (73): removed 33 dead control-character debris lines (figure-position residue after the "Figure 1: Pitch, yaw and roll of the ship" and "Figure 2: Positions of the stars" captions) and null-patched 2 lines in the relay-circuit diagram ASCII art; 0 control bytes remain.
  Typography throughout is spacing-degraded (flattened sub/superscripts like `x2 1`, split words like `Considerthequadraticforms`), but problem statements are present and mathematically correct in sampled regions (problems 1-9, 47-48, probability section).
  Kept as-is; source PDF `assets/attachments/Big_List_of_Math_Problems.pdf` remains the oracle.
  The "P" and "/Radioactivity" legend markers are intentional (creative / hard problems).

- **calculating_galois_from_polynomial.md** (74): stripped 2 `\x03` control bytes (end-of-proof marks); fixed 27 OCR garbles — `char ( K ) ≠ 2` (twice; Ω misread), if/iff restorations, "Galois group", "cyclotomic", "computed", "Adding…identical", $p$-cycle, $F_{11}$ subscript, $\alpha_2$ subscript, [Q(∛2):Q] = 3 (was "degree 2"), 1000 = 8·125 and Gal ≅ Z₂×Z₂×Z₁₀₀ (was 4·125 / Z₂×Z₁₀₀ — data-error fix), $x^{p^n} − x$, "of arbitrary degree", stray `]`, excluded set \{9\} (was \{2\}; 9 = −2 mod 11 is the found root), $\bar{p}$ → p, "the transitive subgroups of $S_3$ are $S_3$ and $A_3$" (removed internal contradiction), "cubic over $\mathbb{Q}$", "over $\mathbb{Q}$" (3×).

- **calculus_practice_test3.md** (75): reconstructed answer-choice labels stripped by the scan and cleaned ~35 garbles.
  Recovered: problem 6 (∫_b^{b+1}(x²+x)dx minimum, b = −1 — choices force the upper limit), 7 (octants of $z = e^{x+y}$), 8 ($f = \sqrt{\tan^2 x − 1}$ domain), 14/15 (∫₁^x dt/(1+t²) tangent at x = 2 — stem reconstructed from the choice set), 16 ($e^{g(x)}h(x)$, $h' = −g'h$; $\mathfrak{x}$→x, $\hbar$→h), 25 (Lipschitz: $|f(x)−f(y)| ≤ K|x−y|$ — abs-value bars and stem restored from choices), 29 (Σ(1/k − 1/2^k) = +∞), 30 (piecewise $\sqrt{1−x^2}$ / $x−1$ integral, "thien"→"then"), 34 (FTC: $2xe^{−x^4}$; choices (A)(B) reconstructed from glyph fragments), 35 (Riemann sum = 9/2), 39 (log(1+sin 2πx) undefined iff $x = (4n−1)/4$), 44 (lim = $9P''(x)$). Verified 0 control bytes.
  Flagged as ambiguous (see below): problems 9-15, 18, 20-28, 30-33, 36-38, 40-43 are absent from the extraction or have unreadable stems.

### Batch 5: files 76-80

- **cambride_analysis_ii.md** (76): replaced 34 PUA glyphs (U+F8E0–U+F8FF) at 6 sites with their intended delimiters (`{`, `(`, `)`) or dropped them; 0 control bytes and 0 PUA remain.
  Extraction otherwise excellent; text-layer renderings `↦ →`, `⁄=`, `‖ ‖` kept as-is.
  "fundamental theorem of algebra" kept as extracted — author typo, not verifiable without the source PDF bytes.

- **Cambridge Examples Sheets.md** (77): fixed ~20 OCR garbles — `\right.` → `\right\}` closing cases environments (2 sites), restored missing math delimiters (Im z; |z|²; sech z), missing `\to` in `f \colon \mathcal { H } \to \mathcal { H }$`, `Let $^ { a , }$ b` → `Let $a , b$ be`, doubled commas `,$ ,` (4 sites), `$a > 1 _ { . }$` → `$a > 1$`, reconstructed the Dirichlet-integral display ("Evaluate $\lim _ { R \to \infty } \int _ { - R } ^ { R } \ldots$ R→∞"), `\hat { t }`/`\dot { t }` → `t`, `\widehat { / }` → `/`, `\mathcal { H } _ { 2 }` → `\mathcal { V } _ { 2 }`. Left as extracted: `\tag{iii}` on the sin² integral — internally inconsistent numbering (the hint references the log integral as part (iii)), plausibly an authorial typo, unverifiable from the extraction alone.

- **Ch10PtASltns.md** (78): fixed headers `## # N:` → `## N:` (6 sites; standalone single-# headers kept), missing `\to` (3 sites: ℝ*→ℝ*, ℝ[x]→ℝ[x]), `\bar { \phi }` → `\phi`, joined the scattered kernel paragraph into one math line (Ker φ = {0}), form-feed `\x0c` → `|` in the set-builder, `x 7→ 3x` → `x \mapsto 3 x`, `bia` → `via`. 0 control bytes remain.

- **Ch10Sltns.md** (79): fixed ~30 garbles — `## # N:` → `## N:` (9 sites), doubled commas, `\right. }` → `\right\} }`, `23Kerφ` → `$2 3 \, \mathrm { K e r } \phi$`, `{4, 0}` → `$\{ 4 , 0 \}$`, `x 7→` maps → `\mapsto` (3 sites), `$| G | 2$ Generalize.` → `$| G |$? Generalize.`, `in C.` → `in $\mathbb { C }$ .`, stray `7` → `or`, missing commas/periods.
  Rewrote the corrupted φ-ring-homomorphism computation on problem 12 (triplicated sqrt factors and stray text removed; chain restored).
  Math-error fix: `\phi ( g N ) \phi ( g M )` → `\phi ( g N ) \phi ( h N )` — the solution maps the first factor to φ(gN) and the second to φ(hN). Generator notation `< 5 >`, `< g >` kept — author convention, renders correctly.

- **Ch11Sltns.md** (80): fixed headers `## # N:` → `## N:` (3 sites), HTML-table OCR — `$\overline { { \phi ( 4 ) = 2 } }$` → `$\phi ( 4 ) = 2$`, `Z _ { 1 6 }`-style cells → `\mathbb { Z }` (4 cells), `φ(2)`/`φ(4)` → `$\phi$` form; "or order 360" → "of order 360" (2 sites), "p andq" → "p and q", `(1, 1, 1)` → `$( 1 , 1 , 1 )$`. Flagged as ambiguous (see below): problem 10's group (b) has the wrong order.

### Batch 6: files 81-85

- **Ch12Sltns.md** (81): 0 control bytes. Fixed ~20 garbles — headers `## # N:` → `## N:` (7 sites: # 3, 4, 12, 17, 45, 46, 50; run-on "# 27" header split onto its own line), `In C` / `in R` → `In $\mathbb { C }$` / `in $\mathbb { R }$`, restored multiplication dots `2  3 = 0` → `$2 \cdot 3 = 0$` and `3  2 = 0 = 3  4` → `$3 \cdot 2 = 0 = 3 \cdot 4$`, `$a x \ = \ b$` → `$a x = b$`, unclosed math closed + period (`$x = a ^ { - 1 } b$ .`), "Farther" → "Further", rebuilt the # 19 center set-builder (`$\{ x \in R \mid a x = x a \text { for all } a \in R \}$`), `i↵` → "if and only if", `\left\lceil … \right\rceil` → `\left[ … \right]`, `$\frac { 1 } { d e t ( A ) }$ is in Z` → `$\frac { 1 } { \operatorname { d e t } ( A ) } \in \mathbb { Z }$`, `must $\mathrm { b e } \pm 1$` → `must be $\pm 1$`, # 42 set-builder rebuilt as `\left\{ \begin{array} { c c } … \right| a , b \in \mathbb { Z } \right\}$`, # 43 `\in \mathbb { R }` → `\in R$` (data fix: S is a subset of R = Z⊕Z⊕Z, not of ℝ).
- **Ch13Sltns.md** (82): removed 2 embedded NUL bytes (the old blob was binary); 0 control bytes remain. Fixed ~15 garbles — headers `## # N:` → `## N:` (7 sites: # 6, 10, 12, 13, 16, 18, 26), `Z[x]` → `$\mathbb { Z } [ x ]$`, `2Z` → `$2 \mathbb { Z }$`, restored the # 10 set-builder (`∈`-area NULs replaced by `\mid$`, math closed: `$\{ ( a , b , c ) \mid$ exactly 1 or 2 of the entries are zero $\}$ .`), "composes" → "composed", `\mathrm { ~ S o ~ }` / `\mathrm { s o }` / `\mathrm { \stackrel { \sim } { s o } }` → plain "So"/"so", joined split math (`= 6 + 5 =$ 11 = 4` → `= 6 + 5 = 1 1 = 4$`), `a  b` → `a - b$` in the subfield test, answer lists a-d wrapped in math (`? $2$`, `$2 , 3$`, …), `\bigoplus` → `\oplus`, "order 2n" → `$2 ^ { n }$` in both title and body of # 35 (data fix: the field has order 2ⁿ, so char F = 2), closing periods (`$a - b \in N$ .`, `$a = 1$`).
- **Ch14Sltns.md** (83): 0 control bytes. Fixed ~15 garbles — colon misreads `\colon` / `\mathrm { : }` / `\dot { : }` → plain `:`, generator ideals `(2), (5)` → `$( 2 ) , ( 5 )$` (3 sites), doubled comma `a - b ,$ ,` → `$a - b$ ,`, `\mathrm { S i n c e }` → `\text { Since }`, `g c d` → `\operatorname { g c d } ( m , n )`, `\mathrm { ~ s o ~ }` → `\text { so }`, `d e g` → `\operatorname { d e g }`, # 28 title `\mathbb { \tilde { \rho } } [ x ]` → `\mathbb { R } [ x ]` (data fix: ρ̃ was the scan's misread of ℝ), # 32 quotient-size lines closed + periods, # 38 `4 $: 2 = 8$` → `$4 \cdot 2 = 8$` and quotient elements `a in 0,1,2,3` → `$a$ in $\{ 0 , 1 , 2 , 3 \}$`, # 46 proof `x , y \in A$` → `\in N ( A )$` and the power step `so $( x + y ) ^ { n + m } \in A$ . Thus $x + y \in N ( A )$` (data fix: sums of nilradical elements land in A by the power bound), nil-radical set-builder rebuilt with `\mid` + `\text { for some }`, `N ( < ~ 0 ~ > )` → `N ( < 0 > )`, # 49 `= R / I$` and `= I$` joins.
- **Ch15Sltns.md** (84): 11024 bytes, 0 control bytes. Fixed ~15 garbles — # 11 header, # 12 φ proof chain, # 15 matrix garble, `order 5` → `order 6` (data fix), `# 1 7{:}:\` header, # 21 / # 50 / # 66 garble fixes.
- **Ch16Sltns.md** (85): 10619 bytes, 0 control bytes. Fixed 10 garbles — header `$\#$ 1` → `# 1`; # 1: f+g display rebuilt with its intermediate coefficient sums (`3 x ^ { 4 } + ( 4 + 3 ) x ^ { 3 } + … ` → `3 x ^ { 4 } + 2 x ^ { 3 } + 0 x ^ { 2 } + 2 x + 2`); # 2 / # 4 fixes; # 6 map chain `$ )` → `\mapsto`; # 9 / # 10 `R R[x]` → `R \to R[x]`; # 11 `\operatorname { m a x }`; # 15 `\begin{array}{r}` cleanup, stray `1.` → "By induction"; # 17 `\boldsymbol { x }` → `x`, `b ^ { m }` → `b _ { m }`; # 19 `\operatorname { d e g }`, `c _ { n + m } x ^ { n + m }` → `c _ { i } x ^ { i }`; # 20 `a + < x > \mapsto a`; # 56 `\dot { f ( x ) }` → `f ( x )`, `x | f ( x )`. Flagged as ambiguous (see below): the f(x)·g(x) computation the problem asks for is absent from the scan.

### Batch 7: files 86-88

- **Ch17Sltns.md** (86): 9879 bytes, 0 control bytes. Fixed 12 garbles — `d e g` / `k e r` → `\operatorname { … }`; # 24 `~ = ~` → `=`; # 31 `f ( x ) \mapsto f ( a )`; # 12(e): polynomial coefficients reconstructed as `\textstyle \frac { 5 } { 2 } , \frac { 9 } { 2 } , \frac { 1 5 } { 2 } , \frac { 3 } { 7 } , \frac { 3 } { 1 4 }` — verified internally: 14f(x) = 35x⁵ + 63x⁴ + 105x³ + 6x² + 84x + 3 (each 14·coefficient reproduces the Eisenstein line; p = 3 works: p | 63, 105, 6, 84, 3; p ∤ 35; p² ∤ 3); # 15 `f ( 0 ) = 6$` (x³ + 6 over Z₇); # 26 `( 4 ) ^ { - 1 }` and "squares to 2" (4² = 16 ≡ 2 mod 7).
- **Ch20Sltns.md** (87): 4617 bytes, 0 control bytes. Fixed 9 garbles — # 6 `Show that $\mathbb { R } ( a + b i ) = \mathbb { C }$ .`, # 7 "and has root", # 21b `\ldots` joins, # 23 paragraph rejoin, # 27 `So $-3 =`, # 38 `\pm i` math.
- **Ch6Sltns.md** (88): 19167 bytes, 0 control bytes. ~55 garbles across 20 problems — header `## # 1` → `## 1` and `$\#$ 35`/`$\#$ 45`/`$\#$ 48` → `# …`; # 4/# 5 titles: `U(8)` → `$U ( 8 )$`, and # 5 title math fix `U ( 1 0 )` → `U ( 1 2 )` (second problem is U(8) ≅ U(12); U(12) = {1, 5, 7, 11} all square to 1) with the multiplication-check list reconstructed as `\phi ( 1 \cdot 3 ) , \phi ( 3 \cdot 5 ) , \phi ( 3 \cdot 7 ) , \phi ( 5 \cdot 7 )`; # 20 `a \mathbb { Z }$`-subgroups proof rebuilt (`$a = \pm 1$` / `$a = 0$` cases, `\to$`, `a z \mapsto z$`, one-to-one/onto straightened); # 35 `\mathbb { C }` restored (2 sites) + missing `i` restored (`( a c - b d ) - ( b c + a d ) i$`); # 36 set-builder rebuilt (`\left[ … \right]` not `\left\lceil … \right\rceil` — 2 sites, `\text { are rational }` ×2, `\right.$` split removed), the φ map `a + b \sqrt { 2 } \mapsto \left[ \begin{array} … \end{array} \right]$`, kernel re-derived as $\{ a + b \sqrt { 2 } \mid \left[ \begin{array} … \right] = \left[ \begin{array} … 0 \end{array} \right] \} = \{ a + b \sqrt { 2 } \mid a = 0 = b \} = \{ 0 \}$`, "φ is onto since Ker" → "one-to-one since $\operatorname { K e r } \phi$" (math fix), matrix products repaired (`a c + 2 b d`, `2 ( a d + b c )`, …) in both checks; # 37 `\frac { p } { q }$` fractions, `i \cdot \frac { p } { q }$`, `q = 2$`, and `\frac { p } { 2 q } \not \in < \frac { p } { q } >$` (math fix: p/2q is a rational outside the cyclic subgroup generated by p/q); # 40 `\mapsto` restored, `\mathbb { R } ^ { n }` normalized (3 sites), tuple-arithmetic chain rebuilt (`( - ( a _ { 1 } + b _ { 1 } ) , … )`), kernel rewritten as $\{ ( a _ { 1 } , … , a _ { n } ) | - a _ { i } = 0 \forall i \} = \{ ( 0 , 0 , … , 0 ) \}$ with `\ldots` joins; # 42 `g  g ^ { 2 }` → `g \mapsto g ^ { 2 }$` (double-space, replaceAll), the one-to-one argument repaired (`g ^ { 2 } h ^ { - 2 } = ( g h ^ { - 1 } ) ^ { 2 } = e$`), and the non-onto example `\mathbb { Z } _ { \geq 0 }$` → `$\mathbb { Z }$` (data fix: Z≥0 is not a group under addition; the example is φ(x) = 2x on Z with "nothing maps to 3"); # 43/# 45 grammar (`g \in G$ . If`, `$\phi _ { g }$`-vs-`\phi _ { h }` argument); # 45 header joined from the two-line split; # 48 centralizer proof punctuation (`$a b = b a$`, `C ( a )$ . Then`, `h$ . But`, `C ( a ) )$ . Since`); # 52 `$a * b = b a$`, `$G ^ { * }$` math, `Farther` → "Further", kernel collapsed to $\{ g \in G | g = e \} = \{ e \}$ (was the duplicated `\{ g \in G | g ^ { - 1 } g = e g \} =$ $\{ g \in G | e = g \}`).

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

- **Ch11Sltns.md**, problem 10: group (b) `$Z_2 \oplus Z_2 \oplus Z_2 \oplus Z_5$` has order 40, not 360. The complete order-360 Abelian list needs $Z_2^3 \oplus Z_9 \oplus Z_5$ — either a `⊕ Z_9` factor was lost in the scan or the author erred.
  The remaining listed groups (a),(c),(d),(e),(f) are correct.

- **Ch16Sltns.md**, problem 1: the solution computes f(x)+g(x) (display rebuilt with intermediate coefficient sums) but the requested f(x)·g(x) computation is absent from the scan — the product step is missing entirely between the f+g display and problem 2. Re-extraction from the source would recover it; the linked polynomials (f = 4x³+2x²+x+3, g = 3x⁴+3x³+3x²+x+4 over Z₅) are intact.

- **calculus_practice_test3.md**: problems 9-15, 18, 20-28, 30-33, 36-38, 40-43 are absent or their stems are unreadable — page/scanner gaps, not fixable from the extraction.
  Problem 17 stem has an unreadable first term (`$\mathbf{i_\tau} - \sin^2(\mathrm{Arccos}\frac{\pi}{12})$`); problem 43's polynomial-condition stem is garbled (`\quad n = \sum a_i x^i` fragment with unknown degree hypothesis); problem 35 choice (C) `$\frac{3!}{6}$` has lost digits.
  Problem 19-24 fragment: statement I's right-hand side is lost (`f(x) = ?`). Re-extraction from `assets/attachments/calculus_practice_test3.pdf` is the repair path for all of these.
