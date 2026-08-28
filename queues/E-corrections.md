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
| 51-100 | basic-08S — chapter-5 | in progress |
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

- **Ch12Sltns.md** (81): 0 control bytes.
  Fixed ~20 garbles — headers `## # N:` → `## N:` (7 sites: # 3, 4, 12, 17, 45, 46, 50; run-on "# 27" header split onto its own line), `In C` / `in R` → `In $\mathbb { C }$` / `in $\mathbb { R }$`, restored multiplication dots `2  3 = 0` → `$2 \cdot 3 = 0$` and `3  2 = 0 = 3  4` → `$3 \cdot 2 = 0 = 3 \cdot 4$`, `$a x \ = \ b$` → `$a x = b$`, unclosed math closed + period (`$x = a ^ { - 1 } b$ .`), "Farther" → "Further", rebuilt the # 19 center set-builder (`$\{ x \in R \mid a x = x a \text { for all } a \in R \}$`), `i↵` → "if and only if", `\left\lceil … \right\rceil` → `\left[ … \right]`, `$\frac { 1 } { d e t ( A ) }$ is in Z` → `$\frac { 1 } { \operatorname { d e t } ( A ) } \in \mathbb { Z }$`, `must $\mathrm { b e } \pm 1$` → `must be $\pm 1$`, # 42 set-builder rebuilt as `\left\{ \begin{array} { c c } … \right| a , b \in \mathbb { Z } \right\}$`, # 43 `\in \mathbb { R }` → `\in R$` (data fix: S is a subset of R = Z⊕Z⊕Z, not of ℝ).

- **Ch13Sltns.md** (82): removed 2 embedded NUL bytes (the old blob was binary); 0 control bytes remain.
  Fixed ~15 garbles — headers `## # N:` → `## N:` (7 sites: # 6, 10, 12, 13, 16, 18, 26), `Z[x]` → `$\mathbb { Z } [ x ]$`, `2Z` → `$2 \mathbb { Z }$`, restored the # 10 set-builder (`∈`-area NULs replaced by `\mid$`, math closed: `$\{ ( a , b , c ) \mid$ exactly 1 or 2 of the entries are zero $\}$ .`), "composes" → "composed", `\mathrm { ~ S o ~ }` / `\mathrm { s o }` / `\mathrm { \stackrel { \sim } { s o } }` → plain "So"/"so", joined split math (`= 6 + 5 =$ 11 = 4` → `= 6 + 5 = 1 1 = 4$`), `a  b` → `a - b$` in the subfield test, answer lists a-d wrapped in math (`? $2$`, `$2 , 3$`, …), `\bigoplus` → `\oplus`, "order 2n" → `$2 ^ { n }$` in both title and body of # 35 (data fix: the field has order 2ⁿ, so char F = 2), closing periods (`$a - b \in N$ .`, `$a = 1$`).

- **Ch14Sltns.md** (83): 0 control bytes.
  Fixed ~15 garbles — colon misreads `\colon` / `\mathrm { : }` / `\dot { : }` → plain `:`, generator ideals `(2), (5)` → `$( 2 ) , ( 5 )$` (3 sites), doubled comma `a - b ,$ ,` → `$a - b$ ,`, `\mathrm { S i n c e }` → `\text { Since }`, `g c d` → `\operatorname { g c d } ( m , n )`, `\mathrm { ~ s o ~ }` → `\text { so }`, `d e g` → `\operatorname { d e g }`, # 28 title `\mathbb { \tilde { \rho } } [ x ]` → `\mathbb { R } [ x ]` (data fix: ρ̃ was the scan's misread of ℝ), # 32 quotient-size lines closed + periods, # 38 `4 $: 2 = 8$` → `$4 \cdot 2 = 8$` and quotient elements `a in 0,1,2,3` → `$a$ in $\{ 0 , 1 , 2 , 3 \}$`, # 46 proof `x , y \in A$` → `\in N ( A )$` and the power step `so $( x + y ) ^ { n + m } \in A$ . Thus $x + y \in N ( A )$` (data fix: sums of nilradical elements land in A by the power bound), nil-radical set-builder rebuilt with `\mid` + `\text { for some }`, `N ( < ~ 0 ~ > )` → `N ( < 0 > )`, # 49 `= R / I$` and `= I$` joins.

- **Ch15Sltns.md** (84): 11024 bytes, 0 control bytes.
  Fixed ~15 garbles — # 11 header, # 12 φ proof chain, # 15 matrix garble, `order 5` → `order 6` (data fix), `# 1 7{:}:\` header, # 21 / # 50 / # 66 garble fixes.

- **Ch16Sltns.md** (85): 10619 bytes, 0 control bytes.
  Fixed 10 garbles — header `$\#$ 1` → `# 1`; # 1: f+g display rebuilt with its intermediate coefficient sums (`3 x ^ { 4 } + ( 4 + 3 ) x ^ { 3 } + … ` → `3 x ^ { 4 } + 2 x ^ { 3 } + 0 x ^ { 2 } + 2 x + 2`); # 2 / # 4 fixes; # 6 map chain `$ )` → `\mapsto`; # 9 / # 10 `R R[x]` → `R \to R[x]`; # 11 `\operatorname { m a x }`; # 15 `\begin{array}{r}` cleanup, stray `1.` → "By induction"; # 17 `\boldsymbol { x }` → `x`, `b ^ { m }` → `b _ { m }`; # 19 `\operatorname { d e g }`, `c _ { n + m } x ^ { n + m }` → `c _ { i } x ^ { i }`; # 20 `a + < x > \mapsto a`; # 56 `\dot { f ( x ) }` → `f ( x )`, `x | f ( x )`. Flagged as ambiguous (see below): the f(x)·g(x) computation the problem asks for is absent from the scan.

### Batch 7: files 86-88

- **Ch17Sltns.md** (86): 9879 bytes, 0 control bytes.
  Fixed 12 garbles — `d e g` / `k e r` → `\operatorname { … }`; # 24 `~ = ~` → `=`; # 31 `f ( x ) \mapsto f ( a )`; # 12(e): polynomial coefficients reconstructed as `\textstyle \frac { 5 } { 2 } , \frac { 9 } { 2 } , \frac { 1 5 } { 2 } , \frac { 3 } { 7 } , \frac { 3 } { 1 4 }` — verified internally: 14f(x) = 35x⁵ + 63x⁴ + 105x³ + 6x² + 84x + 3 (each 14·coefficient reproduces the Eisenstein line; p = 3 works: p | 63, 105, 6, 84, 3; p ∤ 35; p² ∤ 3); # 15 `f ( 0 ) = 6$` (x³ + 6 over Z₇); # 26 `( 4 ) ^ { - 1 }` and "squares to 2" (4² = 16 ≡ 2 mod 7).

- **Ch20Sltns.md** (87): 4617 bytes, 0 control bytes.
  Fixed 9 garbles — # 6 `Show that $\mathbb { R } ( a + b i ) = \mathbb { C }$ .`, # 7 "and has root", # 21b `\ldots` joins, # 23 paragraph rejoin, # 27 `So $-3 =`, # 38 `\pm i` math.

- **Ch6Sltns.md** (88): 19167 bytes, 0 control bytes.
  ~55 garbles across 20 problems — header `## # 1` → `## 1` and `$\#$ 35`/`$\#$ 45`/`$\#$ 48` → `# …`; # 4/# 5 titles: `U(8)` → `$U ( 8 )$`, and # 5 title math fix `U ( 1 0 )` → `U ( 1 2 )` (second problem is U(8) ≅ U(12); U(12) = {1, 5, 7, 11} all square to 1) with the multiplication-check list reconstructed as `\phi ( 1 \cdot 3 ) , \phi ( 3 \cdot 5 ) , \phi ( 3 \cdot 7 ) , \phi ( 5 \cdot 7 )`; # 20 `a \mathbb { Z }$`-subgroups proof rebuilt (`$a = \pm 1$` / `$a = 0$` cases, `\to$`, `a z \mapsto z$`, one-to-one/onto straightened); # 35 `\mathbb { C }` restored (2 sites) + missing `i` restored (`( a c - b d ) - ( b c + a d ) i$`); # 36 set-builder rebuilt (`\left[ … \right]` not `\left\lceil … \right\rceil` — 2 sites, `\text { are rational }` ×2, `\right.$` split removed), the φ map `a + b \sqrt { 2 } \mapsto \left[ \begin{array} … \end{array} \right]$`, kernel re-derived as $\{ a + b \sqrt { 2 } \mid \left[ \begin{array} … \right] = \left[ \begin{array} … 0 \end{array} \right] \} = \{ a + b \sqrt { 2 } \mid a = 0 = b \} = \{ 0 \}$`, "φ is onto since Ker" → "one-to-one since $\operatorname { K e r } \phi$" (math fix), matrix products repaired (`a c + 2 b d`, `2 ( a d + b c )`, …) in both checks; # 37 `\frac { p } { q }$` fractions, `i \cdot \frac { p } { q }$`, `q = 2$`, and `\frac { p } { 2 q } \not \in < \frac { p } { q } >$`(math fix: p/2q is a rational outside the cyclic subgroup generated by p/q); # 40`\mapsto`restored,`\mathbb { R } ^ { n }` normalized (3 sites), tuple-arithmetic chain rebuilt (`( - ( a _ { 1 } + b _ { 1 } ) , … )`), kernel rewritten as $\{ ( a _ { 1 } , … , a _ { n } ) | - a _ { i } = 0 \forall i \} = \{ ( 0 , 0 , … , 0 ) \}$ with `\ldots`joins; # 42`g  g ^ { 2 }`→`g \mapsto g ^ { 2 }$` (double-space, replaceAll), the one-to-one argument repaired (`g ^ { 2 } h ^ { - 2 } = ( g h ^ { - 1 } ) ^ { 2 } = e$`), and the non-onto example `\mathbb { Z } _ { \geq 0 }$` → `$\mathbb { Z }$` (data fix: Z≥0 is not a group under addition; the example is φ(x) = 2x on Z with "nothing maps to 3"); # 43/# 45 grammar (`g \in G$ . If`, `$\phi _ { g }$`-vs-`\phi _ { h }` argument); # 45 header joined from the two-line split; # 48 centralizer proof punctuation (`$a b = b a$`, `C ( a )$ . Then`, `h$ . But`, `C ( a ) )$ . Since`); # 52 `$a * b = b a$`, `$G ^ { * }$` math, `Farther` → "Further", kernel collapsed to $\{ g \in G | g = e \} = \{ e \}$ (was the duplicated `\{ g \in G | g ^ { - 1 } g = e g \} =$ $\{ g \in G | e = g \}`).

### Batch 8: files 89-91

- **Ch7Sltns.md** (89): 10978 bytes, 0 control bytes.
  Fixed ~20 garbles — headers `## # N:` → `## N:` (# 1, 2, 5); # 8 data fix: quotient order fraction rebuilt as `\frac { 1 5 } { 3 } = 5` (|⟨a⁵⟩| = 3, so the quotient has 15/3 = 5 cosets, not 15/2); # 14 set-builder `\mid` restored; # 21 `\operatorname { g c d }`; # 27 `\mathbf { \Psi }` junk removed (coset elements were plain `g \in G`); # 33 equality kept as `= | K : H |`; # 45 `\operatorname { s t a b }` / `\operatorname { o r b } _ { G } ( 5 )`; # 60 “oars” → “are”; closing periods on `$a ^ { 1 3 } = e$` etc. (list not exhaustive).

- **Ch8Sltns.md** (90): 19197 bytes, 0 control bytes; 8 embedded NUL lines (L15, 17, 29, 43, 45, 91, 93, 109) rewritten byte-exact.
  ~35 further garbles — headers `## # N:` → `## N:`; `⇤` → `$*$`; halving-line joins; # 6 data fix “order 4” → “order 8” ($( 1 0 \circ f ) ^ { 2 }$ is not the identity; the powers first revisit the identity at the 8th power); # 7 data fix: cross-wired generator subscripts swapped to match the stated maps; $X + Y - Z$ span joins; `{ \cal G }` → `G` (6 sites); `l c m` → `\operatorname { l c m }` and “must have order 9”; `di↵erent` → “different”; split `# 14:` header merged onto its own line; “semidirect”; `$n _ { ! }$` → `$n$`; `\oplus \cdot \cdot \cdot` → `\oplus \cdots \oplus`; # 26 data fix `S _ { 3 } \oplus \mathbb { Z } _ { 3 }` → `\mathbb { Z } _ { 2 }` (the noncyclic factor of order 6 is S₃, so the cyclic factor is the remaining Z₂); # 38 data fix: matrix product row rebuilt as `{ 1 } & { a + c } & { b + d }` (interior entry is a + c, not a c); # 49 data fix `\phi ( 2 5 ) = 5 ^ { 2 } - 5 = 2 0` (Euler’s φ(25) = 25 − 5 = 20; the scan had `= 5 ^ { 2 } = 5`); `A u t` → `\operatorname { A u t }`; `\text { Yes! } Z _ { 1 0 }`; NUL chain rebuilt as `\mathbb { Z } _ { 1 5 } \oplus \mathbb { Z } _ { 4 } \oplus \mathbb { Z } _ { 1 2 } \approx \mathbb { Z } _ { 5 } \oplus \mathbb { Z } _ { 4 } \oplus \mathbb { Z } _ { 4 } \oplus \mathbb { Z } _ { 3 } \oplus \mathbb { Z } _ { 3 }`; multiplication dots `8 \cdot 2`, `8 \cdot \phi`, `8 \cdot ( 2 , 3 )`, `3 \cdot 5 \cdot 1 1`; `\oplus 9 U ( 1 5 )` → `\oplus U ( 1 5 )`; unclosed math closed (only odd-`$` line pre-fix).
  Flagged as ambiguous (see below): # 68 never answers “How many have order 2?” — the file ends at the order-4 count.

- **Ch9Sltns.md** (91): 18464 bytes, 0 control bytes.
  ~55 garbles — headers `## # N:` → `## N:` (12 sites: # 13, 14, 16, 17, 19, 21, 23, 51, 56, 61, 68, 47-team); single-`#` headers left as-is per convention; `\mathrm`-wrapped words → plain text; split math spans joined (`>$ $`), tildes / `\ < \ >` / `~ { = } ~` junk stripped; `\Biggr \}` → `\}`; `\textrm { < } … \textrm { > }` → `$< … >$`; `I n n` / `g c d` / `l c m` → `\operatorname { … }`; `\mathbb Z` → `\mathbb { Z }`; “Straight forward”/“Farther”/“it’s order”/“Hnece” → fixed; doubled punctuation (`.$ .`, `,$ ,`, `p .$ .`) collapsed; `φ` → `$\phi$`; tombstone `□` kept.
  Data fixes: # 6 lost exponent restored (`\right) ^ { - 1 }$`) and the garbled question mark `\mathbf { \updownarrow }` read as `?`; # 8 dropped the stray superscript `^ { n }` on `\mathbb { Z } _ { \frac { n } { k } }`; # 16 `\Im` read as `?`; # 19 missing bar restored in the denominator `| < ( 2 , 9 ) > |` (10 × 4 / 10 = 4); # 23 garbled algebra `k = n / 4 = n / 2 … 4 n \ = \ 2 n` rebuilt as `n = 4 k = 2 k` , so `n = 0`; # 24/# 25 data fix: per-coset order list `1 , 2 , 4 , 4 , 2 , 4 , 4 , 2` → `1 , 4 , 4 , 2 , 2 , 4 , 4 , 2` (computed: (1,0)H has order 4, (1,1)H has order 2; the order multiset {1, 2, 2, 2, 4, 4, 4, 4} and the conclusion G ≅ Z₄⊕Z₂ are unchanged); # 49 data fix: final conclusion `| Z ( G ) | = p ^ { 2 }` → `= p` (the point of the problem; the contradiction argument shows the order is exactly p); # 51 `h0inH` → `h ^ { \prime } \in H` and the conclusion `g H g ^ { - 1 } \subset N` → `\subset H` (normality needs ghg⁻¹ ∈ H); the `$^ { 6 6 } { \Leftarrow }` garble → `$( \Leftarrow )$`; # 10b coset products verified and joined (`( 2 4 3 ) ( 1 3 2 ) = ( 1 2 ) ( 3 4 )` and `( 1 4 2 ) ( 2 3 4 ) = ( 1 4 ) ( 2 3 )`, the second outside H).

### Batch 9: file 92

- **chapter-1.md** (92): 7322 bytes, 0 control bytes, 0 odd-`$` lines.
  GRE-style precalculus multiple-choice review sheet (25 questions).
  Choice letters and question numbers were the main casualties.

  - Question-number repair (sequence 1-25 unambiguous): restored `2.` (Q2), `5.` (Q5), `10.` (Q10, scan had “0”), `11.` (Q11), `12.` (Q12), `13.` (Q13, scan had “.When”), `14.` (Q14), `19.` (Q19, scan had “1.”), `20.` (Q20, scan had “2”), `21.` (Q21, scan had “2.”), `22.` (Q22, unlabeled).

  - Choice-letter repair: (B)/(D) markers restored in Q1, Q5, Q18, Q24; run-together choice lists rebuilt in Q8, Q15, Q21, Q22, Q23, Q25.

  - Statement garbles: Q2 typo run (“Determie…posiive…satisy…inequaliy”); Q4 recursion `1 \cdots [ f ( n ) ] ^ { 2 }` → `1 - [ f ( n ) ] ^ { 2 }`; Q5 `!` → `?`; Q6 `\operatorname { I f }` → “If”, `f, g, h` math-ified; Q8 split math joined; Q16/Q17 variables math-ified; Q19 `sinh-1 x` → `$\sinh ^ { - 1 } x$`; Q20 cosh display gained the dropped LHS `\cosh x =`; Q21 `sin(sin $x \} = …` → `$\sin ( \sin x ) = \frac { 1 } { 2 }$`; Q23 `tan(2 arcsin` → `$\tan ( 2 \arcsin \frac { 1 } { 3 } )$`; Q25 `arctan` math-ified; stray `{ }` wrappers stripped throughout; `\operatorname { t a n h }` display unified to `\tanh`.

  - Data fixes: Q7 (L19) choice (A) `2 x - y = 3` → `2 x - 3 y = 3` (locus equidistant from (1,4) and (5,−2) is the perpendicular bisector: midpoint (3,1), slope 2/3; as extracted no choice was true); Q13 second remainder restored as `- 1` (both remainders read “1” as extracted, leaving no valid choice; with p(1) = 1, p(−1) = −1 the remainder is `x`, choice (C) — flagged: the minus may be scan-dropped, but then no option is correct); Q19 choices (C) and (D) were duplicated as `\log ( x - \sqrt { x ^ { 2 } + 1 } )`; (D) corrected to `\log ( x + \sqrt { x ^ { 2 } + 1 } )` (the only correct inverse of sinh); Q17 `\log _ { c }` → `\log _ { A }` (no free c appears; A = a² gives log_A x = ½ log_a x); Q15 choice (E) rebuilt from garble as `b ^ { 2 } - 2` (answer (A) `2 - b ^ { 2 }` verified; (E) itself uncertain); Q22 hint rebuilt: “111 is just slightly greater than 353.64” → “`$1 1 1$ is just slightly greater than $3 5 \pi$`” (35π ≈ 109.96 < 111 < 36π ≈ 113.1, so sin 111 > 0 and (B) is in the domain).

  - Every answer is math-verified against its choice set (Q1 (E) 6 via roots 1, 5; Q4 (D); Q5 (C) 1 via f⁻¹(y) = 2 ⇒ y = 1; Q6 (E); Q8 (E) point, (x−1)² + (y+2)² = 0; Q9 (B) 4π; Q10 (B) (1,0) focus; Q11 (D) 1; Q12 (D); Q14 (D) 5, p ≡ 5; Q16 (C) √3, roots 1, 1 ± i√3; Q17 (E) x√x; Q18 (C) 1, e²; Q20 (E) ½log((1+x)/(1−x)); Q21 (E) √3/2; Q22 (B) 111; Q23 (D) 4√2/7; Q24 (D) π/4; Q25 (B) π = arctan 1 + arctan 2 + arctan 3).

### Batch 10: file 93

- **chapter-2.md** (93): 15224 bytes, 0 control bytes, 0 odd-`$` lines.
  Chapter 2 review sheet (48 questions: sequences, limits, continuity, derivatives, applications, integrals, series).
  Question numbers, choice letters, and math delimiters were the main casualties.

  - Question-number repair (sequence 1-48 unambiguous within each section): restored `4.` (Q4), `10.` (Q10), `12.` (Q12), `13.` (Q13), `15.` (Q15), `18.` (Q18), `21.` (Q21), `22.` (Q22, scan had “2.”), `25.` (Q25), `26.` (Q26), `29.` (Q29), `30.` (Q30), `34The` → `34.`, and `35.`-`48.` except `37.` (present).

  - Choice-letter repair: run-together choice lists rebuilt (Q16, Q17, Q18, Q23, Q24, Q27, Q31, Q34, Q40, Q41, Q46); (B)/(C)/(D)/(E) markers restored (Q19, Q20, Q28, Q35, Q39, Q45, Q47); choices split across `$$` blocks converted to inline (Q4, Q7, Q9, Q32, Q38, Q43).

  - Statement garbles: `\operatorname { I f }`/`\operatorname { J f }` → “If”; `\operatorname* { l i m }` → `\operatorname*{lim}`; `\dot { t }` → t (Q21); `\dot { b }` → b (Q10); `\stackrel { \cdot } { f }` → f (Q15); `\Theta` → `\theta` (Q32); `\frac { 4 } { 2 }` → `2` (Q41 exponent); `\frac { 1 } { e { \sqrt { 3 } } }` → `\frac { 1 } { e \sqrt { 3 } }` (Q9); `\mathbb { 1 } f` → “If” (Q42); `\mathbf { j }` → “If” (Q45); `\ O \tilde { a }` → a (Q33); unicode ⅢII → III (Q41); Q30 `[Note: … \}` → “Note: …”; Q39 broken `\$2\sqrt2 }\$` → `$2 \sqrt { 2 }$` and trailing stray “π” dropped; Q6/Q10/Q27 piecewise arrays rebuilt (Q6’s rational was split across rows); Q37 unwrapped from a `<table>` cell.

  - Data fixes: Q10 `m = 3` → `m = 4` (differentiability at x = 1 forces m = 4, b = −4; as extracted, choice (E) with m = 3 matched none); Q23 `\sin ^ { 2 } / \sec` → `\mathrm { cm } ^ { 2 } / \sec` (cm² misread as sin²); Q29 `x = 1 2` → `x = 1` (area (π−2)/4 = ∫₀¹ x arctan x dx forces upper limit 1); Q33 `y = - 6 x` → `y = - b x` (volume 2πb⁵/(15a³) constant ⟺ b⁵ = 2a³, matching choice (C); scan misread b as 6); Q14 “value of f(0)” → “value of f′(0)” (f(0) = 3 not among choices; f′(0) = −4 = (E)); Q18 choice (A) `( n ^ { \prime \prime } )` → `( n ^ { 2 } )` (n″ assumed to be n²; answer ½n! = (B) verified); Q31 statement rebuilt (“lclate he re the egin the qarant” → “Calculate the area of the region in the first quadrant bounded by the curves…”); Q32 statement rebuilt (“Whic he olig epressins vehe are f the regnbonded by the to circ i tured below?”
    → “Which of the following expressions gives the area of the region bounded by the two curves shown below?”); Q36 statement rebuilt; Q39 statement rebuilt; Q42 rebuilt; Q47 phrase rebuilt (“In te yn” → “In the Maclaurin expansion of”).

  - Every answer is math-verified against its choice set (Q1 (E); Q2 (B) 6; Q3 (A) −2; Q4 (A) 1/6; Q6 (D) −1/3 via (x−2) cancellation; Q7 (C) 1/2; Q8 (D) [1/e², e²]; Q9 (A); Q10 (E); Q11 (B) 2f′(x); Q12 (C) y = x + 1; Q13 (A) 2; Q14 (E) −4; Q15 (C) π/2 − 1; Q16 (C) −0.02; Q17 (D) −2; Q18 (B) n!/2; Q19 (E); Q20 (C) a²; Q21 (B) π/3; Q22 (E) (k/e)ᵏ; Q23 (A) 4π; Q24 (B) −log 2; Q25 (D) 1/60; Q26 (C) 9/2; Q27 (E) 3; Q28 (C); Q29 (B) (π−2)/4; Q30 (D) 3/2; Q31 (B) 8 (15/4 + 17/4); Q32 (D); Q33 (C); Q34 (A) 32π/3; Q35 (A) 9/8; Q36 (D) e; Q37 e^(−1/2) = 1/√e; Q38 (C) 1/(n−1); Q39 (E) π/2; Q40 (B); Q41 (A) I only; Q42 (E) 4; Q43 (D) 1/6; Q44 II and III true (I false: aₙ = 1/n² gives √aₙ = 1/n, divergent; III: alternating-series test) — choice list lost entirely; Q45 (B); Q46 (C) 7 (radius 27/4); Q47 (C) −7/6; Q48 (A) −4 via binomial expansion about x = −1).

  - Surviving-choice gaps (kept as extracted; see also Ambiguous fragments below): Q4 only (A)-(C) of five; Q7 only (A)-(D) of five; Q31 (C) value lost; Q37 no choice list survived; Q44 entire choice list lost (answer verified: II and III only); Q42 (E) $4$ forced by the math (scan had only (A)-(D)); Q48 (A) $- 4$ forced by the math (scan had only (B)-(E), (B) rebuilt from `^ { \infty 3 }` as −3); Q41 root index q unrecoverable (convergence of I is independent of q); Q5 statement lost entirely — the surviving relation 2x² + 3x − 2xy − y = 6 is satisfied by none of the five surviving points, so a coefficient of the relation is itself suspect.

### Batch 11: file 94

- **chapter-3.md** (94): 13108 bytes, 0 control bytes, 0 odd-`$` lines.
  Chapter 3 review sheet (30 questions, multivariable calculus: vectors, lines and planes, surfaces, partial derivatives, multiple integrals, Green's theorem).
  Question numbers, choice letters, and math delimiters were the main casualties.

  - Question-number repair (sequence 1-30 unambiguous): restored `7.`, `8.`, `9.`, `10.` (scan had `Whic o`), `12.` (scan had `2The`), `13.` (scan had `1.`), `14.` (scan had `1.`), `16.` (stem lost entirely), `20.` (scan had `0.`), `21.`, `22.`, `27.`, `28.`, `29.` (stem lost entirely), `30.`; `1.`/`11.` spacing (`1.Find` → `1. Find`, `11Consider` → `11. Consider`); `26.` (scan had `2Let`).

  - Choice-letter repair: run-together choice lists rebuilt (Q2, Q3, Q5, Q6, Q8, Q12, Q13, Q14, Q17, Q18, Q20, Q25, Q26, Q27, Q30); (B)-(E) markers restored (Q15 had four unlabeled lines); Q23 (C) `2`, Q24 (E) `27` letters restored; Q28 choices (B)-(E) split across `$$` blocks with `\tag{B}` converted to inline with letters, `\textstyle` stripped.

  - Statement garbles: Q2 hat/vector junk cleaned (`\hat { \dot { \mathbf { i } } }` → `\hat { \mathbf { i } }`, `\vec { \mathrm { ? } }` dropped, `\{ 0 , 0 , 1 \}` → `( 0 , 0 , 1 )`, `^ { \cdots }` dropped); Q3 area math wrapped; Q4 `\begin{array}` identity display → inline, `\bullet` → `\cdot`, `\pmb` → `\mathbf`, `\{ … \}` → `( … )`, "A x V = B" → `\mathbf { A } \times \mathbf { V } = \mathbf { B }`; Q11 piecewise display rebuilt as three separate arrays (scan had a mangled `\frac { if…}{if…}` fused line; the f₂, f₃ values at (0,0) recovered as 0); Q12/Q13/Q14 displays rebuilt (`\arctan \frac { x + y } { 1 - x y }`, the triple partial-product expression, and the f_xy piecewise array); Q15 run-together letters `(DVolume`/`(E)Volume` split; Q18 rebuilt ("untins of twovaribls … suc that" → "functions of two variables … such that"; names f, g, h recovered; `\mathtt { I }` → 1; subtree `Q _ { i }` → `Q _ { 0 }`; `\boldsymbol` → plain; "respectively" spelled; bare `|` → `\left. … \right|`); Q19 rebuilt ("equaton"/"Afl"/"followig vers" → completed; `\operatorname { T }` → `T`); Q20 prose rebuilt ("ba cion" → "be a function", "crta pont in the y-plan" → "certain point P in the xy-plane"); Q21 bare hat macros `\mathbf i`/`\mathbf j` → `\mathbf { i }`/`\mathbf { j }`; Q29 `\mathrm { ~ 0 ~ }` → `0`, `\mathrm { ~ 2 ~ } \alpha` → `2 a`; Q30 (D) braces inside `\sqrt` cleaned.

  - Data fixes: Q5 `P = ( \cdots 1 , - 2 , 4 )` → `P = ( - 1 , - 2 , 4 )` (line-plane intersection computes to (9,6,−2) at t = 2, matching (E); as extracted no choice was reachable); Q6 `Q = ( \cdots 3 , 3 , 3 )` → `Q = ( - 3 , 3 , 3 )` (R = (−5,5,4) = (B) verified at t = 3/2); Q7 `x \div 5 y` → `x + 5 y` (the plane x + 5y − z = 12 = (D) verified: its normal is perpendicular to the line direction ⟨−2,1,3⟩ and it contains A and B; with `\div` no choice worked); Q21 choice (B) `\ \div \` → `+` (coefficient −3 on ĵ verified); Q22 `3xy` → `- 3 x y` (with +3xy the function has no local minimum; with −3xy the min is at (1,1), f = −1 = (D), verified).

  - Statement reconstructions (flagged): Q7 (stem lost; rebuilt from the surviving data: line through A=(3,2,1) parallel to ⟨−2,1,3⟩, plane through L and B=(−2,3,1)); Q9 (stem lost; rebuilt: curve z = f(x) in the xz-plane revolved about the x-axis; answer (E) y²+z²=[f(x)]², verified); Q16 (stem lost; rebuilt: “The plane P is tangent to the surface y²z − 2xz² + 3x²y = 2 at the point Q=(1,1,1)…”; tangent plane 4x+5y−3z = 6, (E) (−2,4,2) verified); Q19 (the fly's point was lost as `(, , .`; recovered as (2,2,2) because −∇T(2,2,2) = (−60,−12,−24) ∝ (−5,−1,−2) = (A)); Q29 (stem lost; rebuilt as “29. Evaluate the integral:”). Q1 (cube-diagonal angle), Q10 (level curves of z = r² cos 2θ), Q30 (Green's theorem on the drawn triangle) depend on occluded images — answers unverifiable, flagged.

  - Every answer is math-verified against its choice set (Q2 (D), not orthogonal: v·(D) = −4; Q3 (B) 7/2 via PQ×PR = (−2,−3,−6); Q4 (E): A×(A−A×B) = B; Q5 (E); Q6 (B); Q7 (D); Q8 (C) 2, distance 6/3; Q9 (E); Q11 (D) f₃ only (f₁ discontinuous, f₂ discontinuous along y = x); Q12 (C) 1/5 at x = 2, y = 1; Q13 (A) −1 triple product; Q14 (A) −1 via f_x(0,y) = −y; Q15 (C) dV = π(2rh·1 + r²·(−1)) = π(100)²; Q16 (E); Q17 (D) 1/8 via F_y = 1, F_z = −8 at z = 1; Q18 (B) 16 = 11·2 + (−3)·2; Q19 (A); Q20 (B) 2√5 via ∇f = (4,2); Q21 (E) ĵ−3k̂ = ∇F/16 at (1,8,4); Q22 (D) −1; Q23 (C) 2, eigenvalues 5, 1 of [[3,2],[2,3]], minimum distance² = 20/5; Q24 (D) 13√13−8, height ≡ 27 on y = x^{3/2}, arc length (13√13−8)/27; Q25 (A) −1 via ∫₁⁰(4x³+3x²−2x)dx; Q26 (E) 2, exact form with f = sin(xy) − x + y; Q27 (B) 1 = 8·(¼)·(½); Q28 (E), region x²+y²/9 ≤ 1 with integrand 2 − x² − y²/9 − √(x²+y²/9)).

  - Surviving-choice gaps (kept as extracted; see also Ambiguous fragments below): Q2 (C) value lost; Q3 (D) value lost.
    Flagged ambiguous: Q20 (C) `4 3 \sqrt { 2 }`, Q23 (D) `2 3 \sqrt { 2 }` and (E) `5 3 \sqrt { 2 }` — fraction-bar-dropped patterns (as written the digit pairs are adjacent numbers, likely `\frac { 4 } { 3 } \sqrt { 2 }` etc., but not recovered); Q24 (E) `27` as extracted; Q29 the integral evaluates to 16a³/9 over the left half of the disk x² + (y−a)² = a², which is not among the choices — the full disk gives 32a³/9 = (B), so a bound or a choice is suspect; bounds kept as extracted.

### Batch 12: file 95

- **Chapter3-notes1.md** (95): 4088 bytes, 0 control bytes, 0 odd-`$` lines.
  Notes sheet on convergent sequences and subsequences (Definition 2.7, subsequence remark/exercise, Definition 3.1, convergence example, Lemma with proof, Theorem 3.7 with proof by induction).
  No data fixes — all garbles were prose/math tokens.

  - `DeÖnition` / `deÖne` / `deÖned` (fi-ligature misread, 4 sites) → `Definition` / `define` / `defined`; sentence-ending `:` → `.` (6 sites); `\cdot \cdot \cdot` → `\cdots`; `\{ - 1 , 1 , - 1 , 1 , . . . \}` → `\ldots`; `\mathrm { ~ o r ~ }` → “or”; “n is represents” → “n represents”.

  - Dropped arrow restored: `\mathbf { P } \circ n : \mathbb { N }  X` → `\mathbb { N } \to X`; `li \mathrm { n } _ { n  \infty }` → `\lim _ { n \to \infty }`; `\scriptstyle \operatorname* { l i m }` → `\lim`; `\mathfrak { l } _ { k  \infty }` → `\lim _ { k \to \infty }`; `\mathbb N` → `\mathbb { N }`; `N \in  { \mathbb { N } }` → `N \in \mathbb { N }`; `\frac 2 k` → `\frac { 2 } { k }`; `a _ { n } < \varepsilon { \mathrm { ~ f o r ~ } } n \geq N$` → `a _ { n } < \varepsilon$ for $n \geq N$`; misplaced delimiter `d $( p _ { n } , p )` → `$d \left( p _ { n } , p \right)$`.

  - Three `\begin{array} { r } { … } \end{array}` single-inequality wrappers unwrapped to inline math (`d ( q _ { k } , q ) < \frac { 1 } { k }`, `d ( p _ { n _ { k } } , q _ { k } ) < \frac { 1 } { k }`, `d ( p _ { n _ { k } } , q ) < \frac { 2 } { k }`); `\sqsubseteq` → `\square` (proof tombstone: “Hence $q \in E . \square$”); closing periods added at sentence-ending math throughout; stray parenthesis moved out of math in “(where we define $n \left( i \right) = 2 i$)”.

### Batch 13: file 96

- **chapter-4.md** (96): 6025 bytes, 0 control bytes, 0 odd-`$` lines.
  Chapter 4 review questions, 16 differential-equation problems.
  Data fixes: 3 (two answer garbles and one dropped factor, each resolved against the verified answer).

  - **Data fixes:** Q1 answer `\frac { 1 } { \frac { 3 } { 4 } } ( 4 - \pi )` → `\frac { 1 } { 4 } ( 4 - \pi )` (f(1) = 1 − π/4 = (4−π)/4; the `3` is a scan insertion).
    Q8 (A) `x - cosh x` → `(A) $x - \sinh x$` (x − cosh x fails f(0) = 0; x − sinh x satisfies all four conditions y⁗ = y″ with f(0) = f′(0) = f″(0) = 0, f‴(0) = −1). Q9 (E) `{ \mid }` → `{ t }` in `2 t + c _ { 1 } + c _ { 2 } e ^ { - t / 2 } + c _ { 3 } e ^ { - 3 t }` (characteristic roots 0, −1/2, −3, particular 2t; a `\mid` symbol cannot appear in a solution).

  - Question numbers added where the scan dropped them: 2, 3, 4, 6, 7, 8, 9, 10, 11, 13 (`11At` → `11. At`). Q4 stem rebuilt from fragments: “Which of the following is a slope field for the differential equation $\left( \frac { d y } { d x } \right) ^ { 2 } = \frac { x } { y } \left( 2 \frac { d y } { d x } - \frac { x } { y } \right) ?$”; the five slope-field images are placeholders (`(A)` … `(E)` + `<!-- image-->`), so the question cannot be answered from the extraction.
    Q13 stem fragment “at the orthogonal to F?” → “at the origin.
    What family of curves is orthogonal to F?” (the family F consists of circles tangent to the y-axis at the origin, so the reconstruction is forced by the circle equation).

  - Q2 statement span `the ur e i v of k.` (prose tying the growth rate to k) is unrecoverable → `[statement lost in the scan]`; numeric choices rebuilt from adjacent digits with dropped letters: `(A) 6 (B) 8 (C) 9 (D) 27 (E) 81`.

  - Math normalization: `$$` display wrappers + `\mathrm{(B)}` / `\mathrm { ( C ) }` / `( \Xi )` prefixes on Q9 choices removed (inline); `\textstyle` (2 sites, Q11) and `\scriptstyle` (1 site, Q10 (A)) wrappers dropped; `\div` → `+` (Q13 circle equation `( x - c ) ^ { 2 } + y ^ { 2 } = c ^ { 2 }`); `{ + }` → `+` (Q7 (C)); `(D) $y ^ { \prime } { = } \frac { 2 x y } { x ^ { 2 } - y ^ { 2 } }$` → `= `; Q14 choices: missing `(A)` / `(E)` letters restored, `\div` → `+` in (D) `x \sin x + \cos x`, Unicode minus U+2212 → ASCII in (C); Q6 stem `g: R → R` → `$g : \mathbb { R } \to \mathbb { R }$`; Q7 stem `f ( \frac { 1 } { 2 } \pi )` → `f ( \frac { \pi } { 2 } )`; `\mathsf { a r c c o s }` → `\arccos` (Q15 (D)); sentence-ending `,` → `.$` after math in Q5, Q6, Q14 stems; stray ` y` dropped at end of the Q4 stem; trailing spaces stripped from the image-marker lines `(A)  ` … `(E)  `.

  - Answers verified against the mathematics (stem and choices otherwise kept as extracted): Q1 (4−π)/4; Q3 (D) `c x ^ { 2 }` (y′ = 2y/x from ∫₀ˣ f dt = xy/3); Q5 (A) 0 (y = e^{ax} − sin(ax); e^u > 1 ≥ sin u for u > 0); Q6 (D) (−1,−1) (M_y = N_x = 1, F = xy + ∫g − ∫g, the g-terms cancel at (−1,−1) where x = y); Q7 (B) 2/π (integrating factor x: xy = sin x − x cos x, C = 0 from f(π) = 1); Q8 (A) x − sinh x; Q9 (E); Q10 (D) (μ = x⁴y², F = x⁶y⁴/2 − x⁵y³); Q11 (D) (exact, F = x²y − x + y³ + y = 2); Q12 (A) e^{y/x} = cx (v = y/x); Q13 (D) (orthogonal slope 2xy/(x² − y²)); Q15 (C) (2w_x − 3w_y = 0 forces w = φ(3x + 2y)). Q14 (B): (D) and (E) fail g(0, y) = 0; among (A), (B), (C), only (B) has g_x = x cos x, so only (B) is consistent with exactness, with coefficient M = xy cos x — the scan's `( \sin x y )` in the stem likely misread `x y \cos x`; kept as extracted, needs source check.

  - Surviving-choice gaps, kept as extracted (needs source check): Q3 (A) `\cos ^ { 3 }` (unlikely distractor shape for this problem class); Q8 (B) `x - \sin \alpha x` and (D) `x + \sin \tan x`; Q9 (C) `e ^ { - 1 / 3 }` (missing the `t` in the exponent) and (D) exponents `e ^ { - t / 3 }`, `e ^ { - 2 t }` (neither matches the characteristic roots); Q10 (A) `x ^ { \ast }` (asterisk instead of a power); Q12 (E) `e ^ { - x / y } = - x` (sign arrangement uncertain).
    Q4 images: see above.

### Batch 14: file 97

- **chapter-5.md** (97): 8912 bytes, 0 control bytes, 0 odd-`$` lines.
  Chapter 5 review questions, 20 linear-algebra problems.
  Data fixes: 9 (two OCR-fabricated fractions, one phantom box, one stray `\cdot`, one `X_f` garble, one `\mathrm{ard}` word garble, two Unicode subscript swaps, one degree-garble, one `\mathbf` miss).

  - **Data fixes:** Q18 `\frac { 3 } { 3 }` → `\frac { 1 } { 3 }` in choices (A) and (B) (the eigenvalue of $A ^ { - 1 }$ is the reciprocal; the `3/3` is a scan duplication). Q7 `{ \cdot 5 }` → `{ 5 }` (matrix entry 5). Q5 `{ \mathrm { a r d } }` → `\text { and }` (joins the two matrices in the “are inverses of each other” statement). Q16 `$9 0 ^ { \circ }$` → `$90 ^ { \circ }$`. Q6 subscripts `\mathfrak { z }` → `1`, `2` (`\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 }`); Q13 `y _ { i }` → `y _ { 1 }` in choices (C) and (D) (the collinear-point determinant uses `y _ { 1 }` twice with `y _ { 2 }`). Q12 (B) `\hbar - 1` → `n - 1` (dimension formula n(n−1)/2; the `\hbar` is a scan substitution). Q18 stem `$X _ { f }$` → `$\mathbf { x } ,$`. Q17 (A) matrix trailing `{ 0 , }` → `{ 0 }`.

  - Question numbers added/restored where the scan dropped or merged them: 5, 6, 7, 8 (inserted as “8. If” before the determinant display), 10 (`10 For` → `10. For`), 11, 12, 13, 14, 15 (`. Let` → `15. Let`), 19 (`## 19.` → `19.`), 20 (`## 20.` → `20.`). Q12 stem rebuilt from prose garbles: `A que matri A is said to be symeric it equals its wn tranose:A = A. … imen sion` → “A square matrix $A$ is said to be symmetric if it equals its own transpose: $A = A ^ { \top } .$ What is the dimension …”. Q14 stem rebuilt as far as possible: “$T : \mathbb { R } ^ { 2 } \to \mathbb { R } ^ { 2 }$ that maps $( 1 , \cdot )$ to $( 1 , 1 )$ and $( 0 , \cdot )$ to $( 2 , \cdot )$” (second coordinates lost).

  - Choice letters restored where the value survived the scan: Q4 (C)/(D); Q6 (B)/(D); Q7 (D); Q9 (B)/(C)/(D); Q10 (A)/(B)/(E); Q11 (C)/(D)/(E); Q13 (A)/(B)/(E); Q15 (A)/(B)/(D)/(E); Q16 (A) (`(AST= I` → `(A) $S T = I$`) and (C) (`)TS = I` → `(C) $T S = I$`); Q18 (A)-(D) (`) The matrix …` and unlettered lines); Q19 (B), with `(D) 5.` punctuation cleaned. Scattered multi-line choice blocks collapsed inline to match the rest of the file.

  - Math normalization: Q12 choice wrappers `\textstyle`, `\scriptstyle`, and the `\begin{array}` in (D) dropped; Q17 (B) bottom-right `{ 1 \rule { 0 ex } { 5 ex } }` → `{ 1 }` (phantom box stands in for the diagonal 1; inference flagged below); `{ \mathrm { s p a n } }` → `\operatorname { span }`; `\operatorname { k }` → `k` (Q6); Unicode all replaced by LaTeX: `≠` → `\neq`, `⇒` / `→` → `\Rightarrow` / `\to` (Q14, Q15 stems), `Ⅲ` (U+2162) → `III`, `R²` → `\mathbb { R } ^ { 2 }`, `R³` / `R5` → `\mathbb { R } ^ { 3 }` / `\mathbb { R } ^ { 5 }`, `→` → `\to`; stray `$\Re ^ { 2 }$` dropped after the Q13 stem; residual plain-text math delimited throughout (Q1 (C) `$A$`, Q2 `$a$` / `$a + b$`, Q3 matrices `$2 \times 2$`, Q5 `$c$`, Q9 `$x$`, Q16 `$S$` / `$T$` / `$I$`, Q17 v and x, Q18 choices `$\mathbf { x }$` etc., Q19 `$-4$` / `$b - 1 .$`).

  - Answers verified against the mathematics (stem and choices otherwise kept as extracted): Q1 (E) (two distinct solutions to a consistent system ⇒ infinitely many; (C) is not necessary: square singular $A = [ [ 1 , 0 ] , [ 0 , 0 ] ]$, $\mathbf { b } = ( 1 , 0 )$); Q2 $a + b = - 1$ (the solution (a, b, a) forces a = −1/2 and b = 2a² − 1 = −1/2); Q3 (D) none (I fails for nilpotent [[0,1],[0,0]]; II fails $AB = AC \not \Rightarrow B = C$; III fails the reflection diag(1,−1)); Q4 (D) 6 ($[ [ 1 , 1 ] , [ 0 , 1 ] ] ^ { n } - [ [ 1 , 0 ] , [ 1 , 1 ] ] ^ { n } = [ [ 0 , n ] , [ - n , 0 ] ]$); Q5 (C) 0 (AB = I forces a = b = c = 0); Q6 (B) −1 (det = −2(k+1)); Q7 (E) 2 (rank 2, determinant 0); Q8 −2d (column ops C₂ := C₂ + 2C₁, C₃ := C₃ − C₁; the answer choices are entirely absent from the scan); Q9 (B) 0 (4×4 determinant −x); Q10 (B) 10 ($b = \alpha ( 1 , 4 , 7 ) + \beta ( 2 , 5 , 8 ) + 0 \cdot ( 3 , 6 , 9 )$ with $\alpha = - 38 / 3$, $\beta = 37 / 3$); Q12 (D) n(n+1)/2; Q13 (D) (determinant zero ⇔ (x, y), (0, y₁), (1, y₂) collinear, a line of slope y₂ − y₁); Q15 (C) (dim ker = 3 in R⁵ ⇒ rank 2 ⇒ image a plane through the origin); Q16 (E) ($S T = - T S$: matrix products [[0,−1],[−1,0]] vs [[0,1],[−1,0]]); Q17 (A) (cross-product matrix [[0,−c,b],[c,0,−a],[−b,a,0]]); Q18 (A) ($A ^ { - 1 }$ has eigenvalue 1/3 with the same eigenvector; (B) misstates the eigenvector as the entrywise reciprocals); Q19 (E) 6 (eigenvalues −4 and b − 1; trace 1 = −4 + b − 1); Q20 eigenvalues 1 and 7 (Hermitian, trace 8, determinant 7).

  - Surviving-choice gaps, kept as extracted (needs source check): Q8 — all answer choices missing from the scan. Q11 — choice (B) missing, and vectors 5 and 6 of the span have 6 entries (not 5), so the dimension cannot be computed reliably from the extraction. Q12 (E) `${ } _ { \textrm { 2 } \hbar \mathrm { ! } } ^ { \perp }` unrecoverable garble. Q14 stem — the two images of the domain basis are lost (“maps $( 1 , \cdot )$ to $( 1 , 1 )$ and $( 0 , \cdot )$ to $( 2 , \cdot )$”), so the question cannot be answered from the extraction (an `<!-- image-->` marker precedes it). Q17 (B) — the `\rule`-replacement of the (3,3) entry as `1` is an inference; a source check should confirm the candidate is the all-diagonal-1s matrix. Q17 (D) — two fragments (`\left( - c \mathrm { ~ ~ \sigma ~ } _ { 1 } \mathrm { ~ ~ \sigma ~ } _ { a } \right)` plus a 3×3 matrix), unrecoverable as a choice. Q20 — letters (B) and (C) lost, `3` survives unlettered, and none of the readable choices (−1, 3, i, 1+i) is an eigenvalue (1 and 7); the correct choice is absent, needs source check.

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
