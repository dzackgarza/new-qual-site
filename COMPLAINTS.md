# Mathematical issues and papercuts

Record issues encountered during source reading, solving, review, authoring or site use under [QUAL-05](CONTRIBUTING.md#named-policies).
Include findings outside the selected card.
This file owns observations; [TODO.md](TODO.md) owns selected repair tasks and dependencies.
Keep existing GitHub issue links rather than copying their live status.
The [corpus review patterns](CONTRIBUTING.md#corpus-review-patterns) supply named candidate patterns, not proof that a candidate is a defect.

## Recording an issue

Add a descriptive heading in the appropriate section below, with:

- **Object and need:** card/collection ID or affected workflow; the exact mathematical statement and hypotheses, or user action and expected behavior.

- **Observed evidence:** source page and passage, counterexample or proof gap, or actual action and result with the relevant path/revision.

- **Impact and owner:** affected parts or consumers, existing partial result, and the mathematical or tool boundary that must change.

- **Uncertainty:** distinguish a verified error from a source ambiguity or review candidate.
  State inspected scope and remaining questions.
  For absence claims supply Searched, Found, Conclusion, Confidence and Gaps.

- **Repair:** link the existing TODO task or issue when available and state the result that would resolve the observation.

A missing hypothesis with a concrete counterexample is a mathematical issue.
An unreadable source is an unresolved source question.
An unsolved problem is ordinary authoring work, not by itself a defect.
A command that prevents reading the intended card is a papercut even when it has a simple workaround.

Extend an existing entry when the same cause affects another card.
Preserve concurrent entries.
If the selected proof requires a repair, link that dependency and resolve it before relying on the statement; recording it does not make the proof valid.
Continue independent assigned mathematics.

After verifying the full repair, remove the resolved entry with evidence in the fixing commit; retain any unresolved portion.
Put durable mathematical errata on the owning card and durable policy in CONTRIBUTING. Keep process notes out of public mathematical remarks.

## Mathematical issues and source questions

### Berkeley Spring 2000 Problem 14 permits degenerate intervals

- **Object and need:** `P-BKS00-14` /
  `SRC-BERKELEY-PRELIM-SPRING-2000`, Problem 14. The printed statement
  assumes only that the intervals $I_1,\ldots,I_n$ are disjoint, closed,
  and nonempty, then asserts that vanishing of all $n$ integrals forces every
  polynomial of degree below $n$ to vanish.
- **Observed evidence:** pages 2--3 of `assets/attachments/Spring00.pdf`
  print exactly “disjoint closed nonempty subintervals of R” and supply no
  positive-length condition. If degenerate intervals are allowed, take
  $n=1$, $I_1=\{0\}$ and $p=1$. Then $\deg p=0<1$ and
  $\int_{I_1}p(x)\,dx=0$, but $p\ne0$.
- **Impact and owner:** part 1 is false literally under the convention that
  singleton sets are intervals. The standard zero-counting proof of part 1
  requires every $I_j$ to have positive length. Part 2 remains true under the
  literal source hypotheses: the owning card separates the nondegenerate
  intervals, proves their lower-degree moment map is an isomorphism, and
  adjusts $x^n$ by a lower-degree polynomial. The card records the part-1
  counterexample as mathematical errata.
- **Uncertainty:** the defect is exact under the usual inclusive definition
  of a closed interval. The Berkeley exam may have intended “subinterval” to
  mean a nondegenerate interval, but the retained paper does not state that
  convention.
- **Repair:** retain the printed statement for source fidelity, together with
  the owning card's erratum, corrected positive-length formulation of part 1,
  and literal proof of part 2, unless an authoritative Berkeley correction or
  explicit convention establishes that singleton intervals were excluded.

### Berkeley Fall 1983 Problem 15 omits connectedness of the ambient open set

- **Object and need:** `P-BKF83-15` /
  `SRC-BERKELEY-PRELIM-FALL-1983`, Problem 15(1). The source assumes only
  that $f$ is analytic on an open set containing the closed unit disk and
  asks to prove that $f$ is constant.
- **Observed evidence:** line 117 of
  `assets/attachments/extracted/Fall83.md` gives exactly that hypothesis.
  If
  $U=\{\lvert z\rvert<2\}\cup\{\lvert z-4\rvert<1/2\}$, the function
  equal to $0$ on the first component and $1$ on the second is holomorphic
  on $U$, real-valued on the unit circle, and not constant on $U$.
- **Impact and owner:** the usual harmonic-maximum/open-mapping argument proves
  that $f$ is constant on the unit disk, and the identity theorem extends
  that constant only across the connected component containing the disk.
  The owning solution must not silently apply the identity theorem to
  disconnected components.
- **Uncertainty:** the mathematical gap is exact. The source may be using
  "open set" informally for a connected region, but the retained source does
  not state connectedness.
- **Repair:** `P-BKF83-15` now proves constancy on the connected component
  containing the closed unit disk and records the literal disconnected-domain
  counterexample as mathematical errata. Retain this source-intent note unless
  an authoritative Berkeley correction establishes that "open set" was
  intended to mean a connected domain.

### UCSD Spring 2019 square-root solution argues circularly off the zero set

- **Object and need:** P-CASP19B claims to prove that a continuous function f
  is analytic when its square is analytic. The proof must establish
  analyticity of f on the nonzero set before removable singularities can be
  used at the zeros.
- **Observed evidence:** lines 32--34 of
  corpus/collections/SRC-UCSD-CA-SPRING-2019/P-CASP19B.md say that f=f^2/f is
  a quotient of analytic functions and justify this by 1/f=f/f^2. Both
  statements already require analyticity of f, which is the conclusion being
  proved. At a point z_0 with f(z_0) nonzero, the noncircular argument instead
  factors the difference of squares in the difference quotient, so its limit
  is (f^2)'(z_0)/(2f(z_0)).
- **Impact and owner:** the current solution does not prove analyticity away
  from the zero set, so its later removable-singularity step has no established
  punctured-neighborhood analyticity to extend. The owning card P-CASP19B
  needs a proof repair; no statement change is required.
- **Uncertainty:** the circularity is exact in the current authored solution.
  The statement itself is true. The sibling Berkeley card P-BKF84-19 is being
  solved independently and does not rely on this proof.
- **Repair:** replace the circular quotient step on P-CASP19B with the
  difference-quotient argument, then use isolated zeros of the analytic
  function f^2 and continuity of f to apply the removable singularity theorem.

### Berkeley Spring 1997 Problem 18 does not specify whether the direct product is finite

- **Object and need:** `P-BERK97S-18` / `SRC-BERKELEY-PRELIM-SPRING-1997`,
  Problem 18(2). The source asks whether an extension splits when the quotient
  is "a direct product of infinite cyclic groups" but does not say whether the
  product has finitely many factors.
- **Observed evidence:** the retained Spring 1997 extraction prints exactly
  that wording. For a finite product, the quotient is `\ZZ^r` and a basis can
  be lifted to split the quotient map. For an arbitrary infinite product the
  claim is false in general: the Baer--Specker group
  `\prod_{n\geq1}\ZZ` is not free, so a free presentation of it cannot split
  as the quotient times its kernel.
- **Impact and owner:** a proof that lifts the coordinate generators silently
  assumes the finite-product (equivalently here, finite-rank free-abelian)
  reading. The owning card must distinguish that case from a literal arbitrary
  infinite product.
- **Uncertainty:** the source's intended convention is unknown.
  **Searched:** current `assets/`, `sources/`, and Git history for
  `Spring97`, Spring 1997 solution variants, and the exact statement.
  **Found:** the exam PDF and its extraction, but no solution packet or prior
  authoritative solution. **Conclusion:** no authoritative retained solution
  resolving the convention was found. **Confidence:** high for the current
  repository. **Gaps:** external Berkeley archives were not searched.
- **Repair:** `P-BERK97S-18` now proves the finite-product reading and records
  the arbitrary-infinite-product counterexample. Keep this source-intent note
  until an authoritative Berkeley solution or convention resolves the wording.

### Azoff Möbius symmetry problem has a false fourth equivalent condition

- **Object and need:** \`P-AZOFF-C12\` / \`SRC-AZOFF-PROBLEMS-BY-TOPIC\`,
  Conformal mapping Problem 12. The source asks to prove four conditions on a
  Möbius transformation equivalent; condition (d) requires a real fixed point
  \(\alpha\) in addition to one nonreal conjugation-compatible point.
- **Observed evidence:** page 3 of the retained PDF prints
  \(T(\alpha)=\alpha\) with no overbar on either occurrence of \(\alpha\).
  The PDF vector data separately shows the overbars in
  \(T(\overline\beta)=\overline{T\beta}\), so the fixed-point clause is not an
  extraction loss. The Möbius transformation
  \(T(z)=-1/z\) has real coefficients and therefore satisfies (a)--(c), but
  its fixed-point equation is \(z^2=-1\), so it has no real fixed point and
  fails (d).
- **Impact and owner:** the printed four-way equivalence cannot be proved.
  The owning problem card must state the true implication pattern before its
  solution is authored.
- **Uncertainty:** verified against the rendered PDF, its text layer, and the
  vector rules carrying the overbars. The mathematical counterexample is
  exact; whether the source author intended a different condition (d) is
  unknown.
- **Repair:** correct \`P-AZOFF-C12\` to ask for the equivalence of (a)--(c),
  prove that printed (d) implies them, and record that the converse fails via
  \(T(z)=-1/z\). Preserve the printed source error as a durable erratum on
  the card.

### Zaidenberg Definition 4.3 makes the following finite-morphism exercises inconsistent

- **Object and need:** \`SRC-AGX-VARIETIES-PROBLEMS\`, Definition 4.3 and
  Exercises 4.4. The standard definition of a finite morphism does not require
  the comorphism to be injective.
- **Observed evidence:** page 6 of the recorded PDF says that a finite morphism
  has an "embedding" $f^*:O(Y)\to O(X)$, while the same exercise immediately
  asks for a non-surjective finite morphism. An injective module-finite
  comorphism is integral, so lying over makes the corresponding affine map
  surjective.
- **Impact and owner:** the source wording cannot govern cards about finite
  morphisms. \`P-AGXVARFINCLOSED\` records and uses the repository definition
  \`D-MORFIN\`, under which the exercise is coherent.
- **Uncertainty:** verified in the PDF with two independent text extractors;
  this may be a typo in the source rather than an intended nonstandard
  convention.
- **Repair:** retain the standard repository definition and treat the printed
  word "embedding" as source errata unless a corrected source edition is found.

### Berkeley Fall 2006 Problem 6A solution packet uses irreducibility circularly

- **Object and need:** `P-BKF06-6A` / `SRC-BERKELEY-PRELIM-FALL-2006`,
  Problem 6A. The retained solution packet proves that
  $x^p-x+1$ is irreducible over $\FF_p$ by analyzing subsets of its translated
  roots.
- **Observed evidence:** `assets/attachments/extracted/f06solution.md` says
  that $(\#I)\alpha\in\FF_p$ and then states “Since f is irreducible,
  $\alpha\notin\FF_p$,” using the desired conclusion to justify the key
  contradiction. The needed independent fact is immediate instead:
  $f(a)=a^p-a+1=1$ for every $a\in\FF_p$, so no root of $f$ lies in
  $\FF_p$.
- **Impact and owner:** the source solution has a circular proof at the
  decisive factor-exclusion step. The owning authored card must not inherit
  that circularity.
- **Uncertainty:** the circular sentence is present in the retained solution
  extraction, and the replacement argument is exact. No claim is made that a
  different edition of the source packet contains the same sentence.
- **Repair:** `P-BKF06-6A` now proves $\alpha\notin\FF_p$ directly from
  $f(a)=1$ before applying the root-sum argument. Retain this entry as source
  errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2006 Problem 8A solution packet gives the wrong cokernel torsion

- **Object and need:** `P-BKF06-8A` / `SRC-BERKELEY-PRELIM-FALL-2006`,
  Problem 8A. The source asks for the kernel, image, and cokernel of the
  displayed integer matrix.
- **Observed evidence:** `assets/attachments/extracted/f06solution.md`
  displays an integral equivalence reducing the matrix to
  `diag(3,0,0)`, but then states
  `cokernel(A) ≅ Z^2 ⊕ Z/2Z`. The displayed diagonal form instead gives
  `Z^2 ⊕ Z/3Z`. Directly, the image is generated by
  $(3,3,6)=3(1,1,2)$, with $(1,1,2)$ primitive, so the quotient has a
  torsion class of exact order $3$.
- **Impact and owner:** importing the source conclusion verbatim would give
  the wrong abelian-group structure on the authored card.
- **Uncertainty:** the contradiction is internal to the retained solution
  packet and independently verified from the matrix. It is consistent with a
  typographical `2` for `3` in the packet's prose.
- **Repair:** `P-BKF06-8A` now computes the image directly and records
  `coker(A) ≅ Z^2 ⊕ Z/3Z`. Retain this entry as source errata; the
  provenance packet itself is not rewritten.

### Berkeley Fall 2006 Problem 1B solution packet omits the factorial in Cauchy's estimate

- **Object and need:** `P-BKF06-1B` / `SRC-BERKELEY-PRELIM-FALL-2006`,
  Problem 1B. The retained proof uses Cauchy's estimates to force all positive
  derivatives of an entire function to vanish.
- **Observed evidence:** `assets/attachments/extracted/f06solution.md`
  states
  `|f^(m)(0)| <= (2^n M)/(R_n)^m`. For ordinary derivatives, Cauchy's
  estimate is
  `|f^(m)(0)| <= m! M(R_n)/(R_n)^m`; the factor `m!` is missing.
- **Impact and owner:** the printed inequality is not the standard derivative
  estimate, although the omitted constant is independent of `n` and the
  argument still tends to zero after it is restored.
- **Uncertainty:** verified against the retained extraction and the standard
  Cauchy integral formula. No normalized-derivative convention is stated in
  the packet.
- **Repair:** `P-BKF06-1B` includes the factor `m!` and retains the same
  limiting argument. Retain this entry as source errata; the provenance
  packet itself is not rewritten.

### Berkeley Fall 2012 Problem 7B solution packet uses a non-invariant quotient

- **Object and need:** P-BKF12-7B / SRC-BERKELEY-PRELIM-FALL-2012,
  Problem 7B. The retained solution packet must prove that a linear map
  satisfying $AB-BA=A$ is nilpotent.
- **Observed evidence:** assets/attachments/extracted/F12_Solutions.md
  first correctly computes
  $BAv=(\lambda-1)Av$ for a $B$-eigenvector $v$, but its final induction
  then says that $A$ is nilpotent on $V/\CC v$. The displayed relation only
  shows that $Av$ is zero or belongs to the $(\lambda-1)$-eigenspace; it does
  not show $Av\in\CC v$. Thus $\CC v$ need not be $A$-invariant, so $A$
  need not induce an operator on that quotient and the induction step is not
  defined.
- **Impact and owner:** the source solution does not establish the requested
  nilpotence. The owning authored card must supply an independent argument
  rather than inherit the quotient induction.
- **Uncertainty:** the invalid quotient step is present in the retained
  solution extraction. The preceding eigenvector calculation is correct, and
  no claim is made that another edition of the solution packet has the same
  final paragraph.
- **Repair:** P-BKF12-7B now uses the generalized eigenspace decomposition
  of $B$ and the identity
  $(B-(\lambda-1)I)A=A(B-\lambda I)$ to show that $A$ shifts generalized
  eigenspaces from $\lambda$ to $\lambda-1$ and hence satisfies
  $A^{\dim V}=0$. Retain this entry as source errata; the provenance packet
  itself is not rewritten.

### Berkeley Fall 2012 Problem 9B solution packet confuses nullity with algebraic multiplicity

- **Object and need:** P-BKF12-9B / SRC-BERKELEY-PRELIM-FALL-2012,
  Problem 9B. The retained solution packet factors the characteristic
  polynomial in order to identify the product of the nonzero eigenvalues.
- **Observed evidence:** assets/attachments/extracted/F12_Solutions.md states
  that the characteristic polynomial is
  $x^m\prod_i(x-\lambda_i)$ "where m is the nullity of M." The exponent of
  the factor $x$ is instead the algebraic multiplicity of the eigenvalue
  $0$. For example, the nonzero nilpotent Jordan block
  $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ has nullity $1$ but characteristic
  polynomial $x^2$.
- **Impact and owner:** the packet can identify the wrong coefficient of the
  characteristic polynomial when the geometric and algebraic multiplicities
  of $0$ differ. The coefficient argument is correct only after replacing
  nullity by algebraic multiplicity.
- **Uncertainty:** the word "nullity" is present in the retained solution
  extraction. The counterexample is exact; this may be terminological
  shorthand or a typo in the packet rather than the intended invariant.
- **Repair:** P-BKF12-9B now defines $m$ as the multiplicity of $0$ as a root
  of the characteristic polynomial and proves that its $t^m$ coefficient is
  $(-1)^{n-m}$ times the product of the nonzero eigenvalues. Retain this entry
  as source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2013 Problem 7B solution packet proves the converse singularity implication

- **Object and need:** P-BKF13-7B / SRC-BERKELEY-PRELIM-FALL-2013,
  Problem 7B. The source asks to prove that invertibility of $I_m-AB$
  implies invertibility of $I_n-BA$.
- **Observed evidence:** page 18 of assets/attachments/F13_Solutions.pdf
  argues that if $I_m-AB$ is singular, then a nonzero vector fixed by $AB$
  yields, after applying $B$, a vector fixed by $BA$, so $I_n-BA$ is
  singular. This is the converse of the singularity implication needed as
  the contrapositive of the requested statement. The same paragraph also
  writes the eigenvectors in $\mathbb R^m$ and $\mathbb R^n$ although the
  matrices are complex.
- **Impact and owner:** as written, the retained solution does not establish
  the requested implication. The owning card must supply the missing
  direction independently.
- **Uncertainty:** swapping $A$ and $B$ in the same idea immediately gives
  the needed implication, so the packet may have intended that symmetric
  argument without stating it. No claim is made about another edition.
- **Repair:** P-BKF13-7B now starts with a vector fixed by $BA$, applies
  $A$, and uses invertibility of $I_m-AB$ to force that vector to vanish.
  Retain this entry as source errata; the provenance packet itself is not
  rewritten.

### Berkeley Fall 2014 Problem 8A solution packet ends with the wrong ambient order

- **Object and need:** P-BKF14-8A / SRC-BERKELEY-PRELIM-FALL-2014,
  Problem 8A. Part (b) asks for a countably infinite total order whose
  collection of down-sets has the largest possible cardinality.
- **Observed evidence:** page 9 of assets/attachments/Fall_2014_Solutions.pdf
  correctly constructs X=Q, injects R into L(Q), and bounds L(Q) by the
  power set of Q. Its final sentence then says this proves the result "in
  the case X=R."
- **Impact and owner:** R is uncountable and does not satisfy the hypothesis
  of the problem. The preceding argument proves the intended statement for
  Q, so importing the final sentence literally would state the wrong
  example.
- **Uncertainty:** the preceding construction and both cardinality bounds
  unambiguously use Q, so the final X=R is a typographical error rather than
  a competing mathematical interpretation.
- **Repair:** P-BKF14-8A retains X=Q throughout and proves
  |L(Q)|=2^{aleph_0}. Retain this entry as source errata; the provenance
  packet itself is not rewritten.

### Berkeley Fall 2015 Problem 5A solution packet reverses a half-plane and skips repeated critical roots

- **Object and need:** P-BKF15-5A / SRC-BERKELEY-PRELIM-FALL-2015,
  Problem 5A. Part (a) proves the reciprocal-sum convex-hull lemma and part
  (b) applies it to the zeros of a polynomial derivative.
- **Observed evidence:** assets/attachments/F15_Solutions.pdf normalizes
  part (a) to z=0 with every c_i in the half-plane Re(w)>0, then says the
  numbers 1/(z-c_i) also lie in that half-plane. In fact
  1/(z-c_i)=-1/c_i has negative real part. The conclusion that their sum
  cannot vanish remains valid, but the stated orientation is reversed.
  In part (b), the packet writes p'/p as the reciprocal sum and applies
  part (a) whenever p'(z)=0 without separating the case p(z)=0; at a
  repeated root the quotient p'/p is not defined, although that critical
  point is already a root and hence is trivially in the convex hull.
- **Impact and owner:** importing the packet literally gives a false
  half-plane assertion and leaves a gap at repeated roots. The owning card
  must correct both points while preserving the Gauss--Lucas argument.
- **Uncertainty:** both issues are visible in the retained PDF text and are
  mathematically exact. They do not affect the truth of either requested
  conclusion.
- **Repair:** P-BKF15-5A uses the correct negative half-plane for the
  normalized reciprocal terms and treats p(zeta)=0 separately before using
  the logarithmic derivative when p(zeta) is nonzero. Retain this entry as
  source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2015 Problem 4B is explicitly retracted by its source solution packet

- **Object and need:** P-BKF15-4B / SRC-BERKELEY-PRELIM-FALL-2015,
  Problem 4B. The printed problem defines a Schur function to be
  nonconstant and asks to prove that the displayed Schur-algorithm transform
  is again a Schur function.
- **Observed evidence:** assets/attachments/F15_Solutions.pdf explicitly
  states "the problem as stated is incorrect" and gives f(z)=z, for which
  the transform is the constant function -1. The packet then supplies a
  corrected formulation: allow Schur functions themselves to be constant,
  retain the hypothesis that the input f is nonconstant, and prove only
  holomorphy and the bound |g|<=1 for the transform.
- **Impact and owner:** the source-faithful printed statement is false. A
  solution cannot prove the requested nonconstancy of the output; the
  owning card must expose the counterexample and distinguish it from the
  corrected theorem supplied by the same source packet.
- **Uncertainty:** none about the source's intent: the retained official
  solution packet contains the correction and explains the grading rule.
- **Repair:** P-BKF15-4B preserves the printed problem, gives f(z)=z as the
  counterexample, and then proves the source-corrected formulation using the
  disk automorphism and Schwarz's lemma. Retain this entry as source errata;
  the provenance packet itself is not rewritten.

### Berkeley Fall 2015 Problem 9B solution packet misadds the diagonal-reflection fixed points

- **Object and need:** P-BKF15-9B / SRC-BERKELEY-PRELIM-FALL-2015,
  Problem 9B. The Burnside computation requires the number of nonattacking
  rook placements fixed by each diagonal reflection.
- **Observed evidence:** assets/attachments/F15_Solutions.pdf prints the
  standard involution-counting expression
  $1+28+210+420+105$ for a diagonal reflection, but states that its value is
  774. The displayed summands instead total 764. The packet's final answer
  5282 is consistent with 764, not 774: using 764 gives
  $(40320+2(764)+2(12)+384)/8=5282$.
- **Impact and owner:** the intermediate fixed-point total in the official
  solution is arithmetically false and is incompatible with its own final
  Burnside average. The owning card must use the correct fixed count.
- **Uncertainty:** none. The printed summands, their sum, and the final
  average determine the intended value uniquely.
- **Repair:** P-BKF15-9B counts diagonal-fixed placements as involutions in
  $S_8$, obtaining 764, and independently derives all other fixed-point
  counts before recovering the source's final answer 5282. Retain this
  entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2016 Problem 4A solution packet omits the actual leading term at the indentation

- **Object and need:** P-BKF16-4A / SRC-BERKELEY-PRELIM-FALL-2016,
  Problem 4A. The retained contour solution analyzes
  $(e^{3iz}-3e^{iz})/z^3$ on a small upper semicircle around zero.
- **Observed evidence:** assets/attachments/F16_Solutions.pdf states that
  the "leading term" of $e^{3iz}-3e^{iz}$ is
  $-9z^2/2+3z^2/2=-3z^2$. In fact the expansion begins
  $-2-3z^2-4iz^3+\cdots$. Thus the integrand also contains the more singular
  term $-2/z^3$. The packet also prints the first real-axis segment as
  $[-R,r]$ rather than the intended $[-R,-r]$.
- **Impact and owner:** the stated local expansion is false and, without a
  separate calculation, does not justify replacing the small-arc integral
  by that of $-3/z$. The final value survives because the integral of
  $-2/z^3$ over the symmetric clockwise semicircle is exactly zero.
- **Uncertainty:** none. The Taylor expansion and the two semicircle
  integrals are explicit, and the final source value $3\pi/4$ is consistent
  with the corrected calculation.
- **Repair:** P-BKF16-4A uses the correct half-annular contour, expands the
  numerator through the omitted constant term, proves its $-2/z^3$
  contribution vanishes, and then obtains the same $3\pi/4$ value. Retain
  this entry as source errata; the provenance packet itself is not
  rewritten.

### Berkeley Fall 2016 Problem 1B prints the unit-ball volume as the sphere surface area

- **Object and need:** P-BKF16-1B / SRC-BERKELEY-PRELIM-FALL-2016,
  Problem 1B. The problem defines $S_n$ as the $(n-1)$-dimensional surface
  area of the unit sphere in $\mathbb R^n$ and supplies example values.
- **Observed evidence:** assets/attachments/F16_Exam.pdf prints
  $S_2=2\pi$ and $S_3=4\pi/3$. The latter is the volume of the unit ball in
  $\mathbb R^3$; the surface area of its unit sphere is $4\pi$. The formula
  requested in part (a), together with $C=\sqrt\pi$ and the gamma
  recurrence, likewise yields $S_3=4\pi$.
- **Impact and owner:** the parenthetical example contradicts the stated
  meaning of $S_n$. The posed parts (a)--(d) remain solvable because none
  requires using the incorrect $S_3$ value.
- **Uncertainty:** none. The two standard geometric quantities are distinct,
  and the problem's own formula recovers the correct surface area.
- **Repair:** P-BKF16-1B preserves the source-faithful statement, carries a
  mathematical erratum remark identifying the corrected value $S_3=4\pi$,
  and its solution derives the requested formulas without using the false
  parenthetical value. Retain this entry as source errata; the provenance
  document itself is not rewritten.

### Berkeley Spring 1981 Problem 4 falsely claims two-sided global existence

- **Object and need:** P-BKS81-4 / SRC-BERKELEY-PRELIM-SPRING-1981,
  Problem 4. Part (1) asks for a solution defined for every
  $t\in\mathbb R$ from every initial condition.
- **Observed evidence:** along every solution,
  $s(t)=x(t)^2+y(t)^2$ satisfies $s'=2s(1-s)$. For the initial condition
  $(x_0,y_0)=(2,0)$, hence $s(0)=4$, the forced solution is
  $s(t)=4/(4-3e^{-2t})$. Its denominator vanishes at
  $t_*=\frac12\log(3/4)<0$, and $s(t)\to+\infty$ as $t\downarrow t_*$.
- **Impact and owner:** Part (1) is false as printed. The forward-time
  statement is true for every initial condition, and Part (2) remains true:
  every nonzero initial condition has $s(t)\to1$ as $t\to\infty$.
- **Uncertainty:** none. The scalar radial equation follows by direct
  differentiation and has the displayed explicit solution.
- **Repair:** P-BKS81-4 preserves the printed question, gives the finite
  backward-time blow-up counterexample, proves the corrected forward-time
  existence statement, proves Part (2), and records the exact erratum on the
  card. Retain this entry as source errata; the provenance packet itself is
  not rewritten.

### Berkeley Spring 1981 Problem 11 source PDF is missing the contour figure

- **Object and need:** P-BKS81-11 / SRC-BERKELEY-PRELIM-SPRING-1981,
  Problem 11. The requested contour integral depends on the closed curve
  $C$ shown in the source.
- **Observed evidence:** page 2 of assets/attachments/Spring81.pdf contains
  the problem text followed, in place of the contour, by the literal
  typesetting error `../Fig/Pr/Sp81-11.ps not found`. Thus the retained PDF
  itself does not specify which of the poles $0$ and $1$ are enclosed or
  with what winding numbers.
- **Impact and owner:** no unique numerical value can be recovered from the
  retained source. The owning card must not invent the missing curve; it can
  determine the integral exactly in terms of the winding numbers of $C$.
- **Uncertainty:** none about the retained PDF. An external PostScript figure
  may have accompanied the original exam, but it is absent from the retained
  source packet.
- **Repair:** P-BKS81-11 records the missing-source obstruction and computes
  the residue formula
  $2\pi i[-\operatorname{Ind}_C(0)+(e-1)\operatorname{Ind}_C(1)]$.
  Retain this entry as source errata; the provenance packet itself is not
  rewritten.

### Berkeley Fall 1993 Problem 12 source PDF is missing the contour figure

- **Object and need:** P-BKF93-12 / SRC-BERKELEY-PRELIM-FALL-1993,
  Problem 12. The requested normalized contour integral depends on the curve
  $\gamma$ that the source says should be depicted.
- **Observed evidence:** page 2 of assets/attachments/Fall93.pdf prints the
  literal typesetting error "../Fig/Pr/Fa93-12.ps not found" where the curve
  should occur. The integrand survives, but the path itself does not.
- **Impact and owner:** the retained source does not determine the path,
  orientation, endpoints, or winding numbers, so it does not determine a
  unique numerical integral. The owning card must not infer a curve from the
  three poles.
- **Uncertainty:** none about the retained repository packet.
  **Searched:** assets/, sources/, corpus/, and Git history for Fa93-12,
  Fall 1993 duplicates, and the problem card.
  **Found:** the Fall 1993 PDF, its extractions, and P-BKF93-12, but no
  figure asset or duplicate statement containing the curve.
  **Conclusion:** the contour data are absent from the retained repository
  source.
  **Confidence:** high.
  **Gaps:** external Berkeley archives were not searched; an original
  PostScript figure may still exist outside the repository.
- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue
  #2. P-BKF93-12 records the missing-source obstruction, computes
  all three residues, and gives the exact residue-theorem formula in terms of
  winding numbers when the missing curve is closed. Retain this entry as
  source errata unless an authoritative copy of the missing figure is
  recovered.

### Berkeley Fall 1996 Problem 8 extraction drops the numerator fraction

- **Object and need:** P-BKF96-8 / SRC-BERKELEY-PRELIM-FALL-1996,
  Problem 8. The generalized binomial coefficient must be known before its
  denominator can be analyzed.
- **Observed evidence:** page 2 of assets/attachments/Fall96.pdf, read with
  layout preservation, places `1/2` directly above `n` inside the displayed
  binomial coefficient. Both retained Markdown extractions instead reduce
  the numerator to `1`.
- **Impact and owner:** the problem card had treated the coefficient as
  unrecoverable, preventing the Author-solutions selector from completing
  the card. The authoritative retained PDF determines the statement as
  $\binom{1/2}{n}$.
- **Uncertainty:** none about the retained PDF layout; the stacked `1/2`
  and `n` are explicit on the page.
- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue
  #2. P-BKF96-8 restores the coefficient from the PDF and supplies the
  complete proof.

### Berkeley Fall 1996 Problem 15 leaves epsilon unquantified

- **Object and need:** P-BKF96-15 / SRC-BERKELEY-PRELIM-FALL-1996,
  Problem 15. The existence of a real twentieth root depends on the printed
  parameter epsilon.
- **Observed evidence:** page 3 of assets/attachments/Fall96.pdf visibly
  asks for a real A with twentieth power diag(-1,-1-epsilon), then asks to
  exhibit A or prove none exists. No definition or quantifier for epsilon
  appears in the problem or surrounding page.
- **Impact and owner:** assuming epsilon>0 would add a hypothesis not in the
  source. The owning solution instead classifies all real epsilon.
- **Uncertainty:** none about the retained PDF; the missing quantifier is in
  the source itself, not only in the extraction.
- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue
  #2. P-BKF96-15 proves existence exactly for epsilon=0 and records the
  source omission in a mathematical remark.

### Berkeley Spring 1983 Problem 4 source PDF is missing the network diagram

- **Object and need:** P-BKS83-4 / SRC-BERKELEY-PRELIM-SPRING-1983,
  Problem 4. The requested Euclidean symmetry group depends on the triangular
  network drawn in the source.
- **Observed evidence:** page 1 of assets/attachments/Spring83.pdf prints
  \`../Fig/Pr/Sp83-4.ps not found\` where the defining diagram should occur.
  No retained \`Sp83-4\` asset, duplicate statement with the figure, or embedded
  PDF image is present in the repository.
- **Impact and owner:** the four surviving labeled points do not determine the
  network or its symmetry group. The owning card must not reconstruct the
  missing edges by guesswork.
- **Uncertainty:** none about the retained packet. The original exam may have
  had an external PostScript figure, but that file is absent here.
- **Repair:** P-BKS83-4 records the source obstruction and proves that the
  surviving data are underdetermined by exhibiting two triangular networks
  through the named points with different Euclidean symmetry groups. Retain
  this entry as source errata; the missing source asset is not reconstructed.

### Berkeley Spring 2009 Problem 7A source solution doubles the requested integral

- **Object and need:** P-BKS09-7A / SRC-BERKELEY-PRELIM-SPRING-2009,
  Problem 7A. The exam asks for
  $\int_0^\pi (a+\cos\theta)^{-1}\,d\theta$ for $a>1$ by residues.
- **Observed evidence:** assets/attachments/extracted/s09solutions.md states
  the interval $[0,\pi]$, but its solution substitutes $z=e^{i\theta}$ and
  replaces the requested integral by
  $-2i\int_{|z|=1}(z^2+2az+1)^{-1}\,dz$. That contour parametrization
  corresponds to $0\leq\theta\leq2\pi$, not $0\leq\theta\leq\pi$,
  and the packet consequently reports $2\pi/\sqrt{a^2-1}$.
- **Impact and owner:** the source solution is too large by a factor of two.
  Since the integrand is invariant under $\theta\mapsto2\pi-\theta$, the
  full-circle integral is twice the requested half-circle integral. The
  owning solution must therefore divide the residue computation by $2$.
- **Uncertainty:** none about the retained statement and solution extraction;
  the factor mismatch is determined by the displayed integration interval
  and the contour parametrization.
- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue
  #2. P-BKS09-7A supplies the corrected residue computation and obtains
  $\pi/\sqrt{a^2-1}$. Retain this entry as source errata; the provenance
  packet itself is not rewritten.

### Berkeley Spring 2009 Problem 9A source solution switches to the wrong least common multiple

- **Object and need:** P-BKS09-9A / SRC-BERKELEY-PRELIM-SPRING-2009,
  Problem 9A. The requested argument must use the integrality of
  $d_{2m+1}I_m$ to prove $d_{2m+1}\geq2^{2m}$.
- **Observed evidence:** page 4 of assets/attachments/s09solutions.pdf
  first establishes $d_{2m+1}I_m\in\mathbb Z$, then after bounding
  $0<I_m\leq(1/4)^m$ states instead that $d_mI_m\geq1$. The same index
  change is present in the retained Markdown extraction.
- **Impact and owner:** positivity and integrality justify
  $d_{2m+1}I_m\geq1$, not $d_mI_m\geq1$. The printed step therefore does
  not follow as written, although replacing $d_m$ by $d_{2m+1}$ immediately
  completes the intended proof.
- **Uncertainty:** none; the incorrect subscript is present in the retained
  PDF itself and is not merely an extraction artifact.
- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue
  #2. P-BKS09-9A keeps the established integer $d_{2m+1}I_m$ throughout
  and derives $d_{2m+1}\geq4^m=2^{2m}$. Retain this entry as source errata.

### Berkeley Spring 2009 Problem 1B source solution omits the case n=1

- **Object and need:** P-BKS09-1B / SRC-BERKELEY-PRELIM-SPRING-2009,
  Problem 1B. The statement does not impose $n\geq2$, so its odd case
  includes $n=1$.
- **Observed evidence:** page 4 of assets/attachments/s09solutions.pdf begins
  its proof with “Since $f^{[n-1]}(a)=0$” and then applies a Taylor formula
  with an $(n-1)$st-derivative remainder. For $n=1$, the displayed vanishing
  would assert $f(a)=0$, which is not a hypothesis, and that remainder formula
  does not give the claimed argument.
- **Impact and owner:** the retained source proof establishes the intended
  parity conclusion for $n\geq2$ but leaves the permitted case $n=1$
  untreated. In that case $f'(a)>0$ directly implies values below $f(a)$ on
  the left of $a$ and above $f(a)$ on the right.
- **Uncertainty:** low. The retained statement has no $n\geq2$ qualifier.
  If an unstated convention was intended to impose it, the extra case is
  redundant rather than harmful.
- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue
  #2. P-BKS09-1B treats $n=1$ separately and then gives the Taylor argument
  for $n\geq2$.

### Berkeley Spring 2009 Problem 7B source omits f and its solution inverts the square root

- **Object and need:** P-BKS09-7B / SRC-BERKELEY-PRELIM-SPRING-2009,
  Problem 7B. The problem is intended to start with a normalized univalent
  function $f$ and to prove that $g(z)=\sqrt{f(z^2)}$ has the stated
  analytic, odd, and univalent properties.
- **Observed evidence:** page 6 of assets/attachments/s09solutions.pdf
  prints “If is a univalent ... function” before immediately defining
  $f(z)=z+\sum_{n\geq2}a_nz^n$, so the function name is missing in the
  opening clause. In the solution, after correctly writing
  $f(z^2)=z^2\phi(z)$ and constructing $\sqrt{\phi}$, the PDF then prints
  $g(z)=1/\sqrt{f(z^2)}=1/(z\sqrt{\phi(z)})$, contradicting the displayed
  definition of $g$ immediately above.
- **Impact and owner:** the omitted name is recoverable from the defining
  formula for $f$. The reciprocal formula in the solution cannot be the
  intended $g$: it has a pole at $0$, whereas the problem asks for a function
  analytic on the unit disk. The correct analytic branch is
  $g(z)=z\sqrt{\phi(z)}$ with the square root chosen to equal $1$ at $0$.
- **Uncertainty:** none about these two retained-PDF defects; both are visible
  on page 6 and are not extraction artifacts.
- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue
  #2. P-BKS09-7B retains a mathematical remark about the omitted name and
  supplies the corrected analytic-square-root proof using
  $g(z)=z\sqrt{\phi(z)}$. Retain this entry as source errata.

### Berkeley Spring 2011 Problem 7B card corrupts the Laplace equation

- **Object and need:** P-BKS11-7B / SRC-BERKELEY-PRELIM-SPRING-2011,
  Problem 7B. The statement must reproduce the Laplace equation printed in
  the retained source.
- **Observed evidence:** page 5 of assets/attachments/s11solutions.pdf prints
  $\partial^2 f/\partial x^2+\partial^2 f/\partial y^2=0$. The authored
  card instead has $\partial^2\widetilde f/\partial x^2$ in the first term
  and $\partial^2 f/\partial y^2$ in the second.
- **Impact and owner:** the mixed function symbols make the displayed
  definition of harmonicity incorrect as written. The retained PDF is
  unambiguous, so the card should use $f$ in both second derivatives.
- **Uncertainty:** none; the retained PDF was inspected directly and the
  discrepancy is an extraction/transcription defect.
- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue
  #2. P-BKS11-7B restores $f$ in the first Laplacian term before attaching
  the complete solution.

### Berkeley Spring 2012 Problem 7A card drops the n=0 term and source solution uses the wrong functional equation

- **Object and need:** P-BKS12-7A / SRC-BERKELEY-PRELIM-SPRING-2012,
  Problem 7A. The authored statement must match the retained series, and the
  natural-boundary proof must use the functional equation that this series
  actually satisfies.
- **Observed evidence:** page 2 of assets/attachments/s12solutions.pdf prints
  $f(z)=\sum_{n\geq0}z^{2^n}$, while the authored card has
  $\sum_{n>0}z^{2^n}$. The source solution on the same page then states
  $f(z)=1+f(z^2)$.
- **Impact and owner:** the card omits the initial term $z$. For the source
  series, direct reindexing gives
  $f(z)=z+f(z^2)$, not $1+f(z^2)$. The source solution's propagation idea
  is repairable, but its displayed functional equation is false.
- **Uncertainty:** none; both formulas are legible in the retained PDF and
  were checked visually.
- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue
  #2. P-BKS12-7A restores the source index $n\geq0$ and proves the natural
  boundary using $f(z)=z+f(z^2)$ and the dense dyadic roots of unity.

### Berkeley Spring 2013 Problem 3B source solution omits the permitted case k=0

- **Object and need:** P-BKS13-3B / SRC-BERKELEY-PRELIM-SPRING-2013,
  Problem 3B. The exam assumes only that $k\neq n^2$ for
  $n=1,2,3,\ldots$, so $k=0$ remains allowed.
- **Observed evidence:** the retained Spring 2013 exam states exactly that
  restriction. The retained solution writes the constant Fourier term as
  $a_0/(2k)$, which is undefined when $k=0$.
- **Impact and owner:** the printed solution handles only $k\neq0$. When
  $k=0$, periodic solvability forces $a_0=0$, all nonconstant Fourier
  coefficients are still determined by division by $-n^2$, and the constant
  Fourier coefficient of $f$ is arbitrary.
- **Uncertainty:** none; the exam statement and solution packet were checked
  directly and disagree on this permitted case.
- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue
  #2. P-BKS13-3B treats $k\neq0$ and $k=0$ separately and proves convergence
  of the resulting Fourier series in both cases.

### Candidates reported by the 2026-09-28 copy-review readers

- **Object and need:** the cards below. Each line is a reader's report made
  while repairing copy; the reader did not change the mathematics named here.
- **Observed evidence:** the report text, one line per card.
  - Statements: E-SS2.EX-9 is false without connectedness; a remark carries
    the component statement.
  - Statements that lost source text: P-WHHDI lost its commutative diagram.
    E-SS1.EX-25 names three calculations and carries two; Stein--Shakarchi
    1.25 has a part (c). E-SS10.EX-2 ends mid-sentence, and its figure
    caption is in E-SS10.EX-3. P-CI7E2 cites a definition of normality that
    its statement does not contain. P-AGXVARPROJIRR and P-ALGFINAL11-02
    carry extraction or agent wording inside the statement.
  - Card structure: E-AXBZQ holds two problems. E-SS2.PR-1 holds
    Stein--Shakarchi Chapter 2 Problems 1 and 2. SRC-TEXT-SS03 lists section
    problems in identifier order, not source order.
  - Proof gaps: E-SS1.EX-13 proves part (3) only. E-SS10.PR-2 (b) asserts the
    $\abs c=1$ corner cases. P-AGXHWDISTINGOPEN mixes the directions of the
    sheaf map on $D(f)$. P-AGXHWREDUCED solves part (a) only.
    P-AGXVARSMOOTHMFLD step <1>4 proves one inclusion of
    $T_pX=\ker dF_p$. P-B2P3P (b)(i) does not exclude the other partitions
    of 5. P-C6SRA (d) calls $0\subset M_2(\QQ)$ maximal and not prime, which
    holds only for completely prime ideals.
  - `STYLE-08` layout (fragment proofs, *Goal*, *Proof:*): P-JHUFA07ANE,
    P-4KTFN, P-PGDJ2, P-YBT6I, P-JHUMAY06ANH, P-JHUMAY06ANI, P-JHUMAY06ANK,
    P-JHUMAY11ANF, P-JHUFA05ANC, P-JHUFA06ANB, P-JHUSP05AND, P-JHUSP05ANE,
    P-XYYHG, P-JHUFA01CAD, P-JHUFA02CAH, P-JHUSP01CAC, P-JHUFA08ANE,
    P-JHUFA08ANF, P-JHUSP07ANA, P-JHUSP08ANE, P-8XT04, P-8XT06, P-8XT09,
    P-WVJBX, P-8XT17, P-8XT32, P-MSHRB, P-7QJS2, P-8XT20, P-PAQ4K,
    P-JHUFA02CAC, P-JHUFA02CAD, P-JHUU51RA5, P-JHU4547C5.
  - Duplicate candidates under `CARD-04`: E-BXDQY / E-EUGUZ, E-ENWYG /
    E-EOMTI, E-22P3T / E-2HIKG, E-AKNDW / E-CFHC4, E-2DPQC / E-5AKU5.
- **Impact and owner:** statement and structure lines are data defects of
  urgency 1 in `AGENTS.md`; proof gaps and layout are authoring work.
- **Uncertainty:** every line is an unverified reader report. None is a
  finding until someone reads the card and its source.
- **Repair:** read each card, confirm or reject the line, repair confirmed
  defects on the card, and delete the line in the repairing commit.

## Workflow and rendering papercuts

### Overlapping workstream owners edited the same Author-solutions card

- **Object and need:** the `new-qual-site` Core2 workstream must have one
  active author on its selected card, under `QUAL-03` and `QUAL-07`.
- **Observed evidence:** on 2026-09-22, repeated successful `workstream`
  continuation calls were followed by `WORKSTREAM_SETUP_REQUIRED` on calls
  carrying the returned ID. One response explicitly reported a superseded
  owner's already-admitted call still settling. During the same session,
  `1b56ef019` committed `P-BERK90S-07` with this session's partial solution
  followed by another complete solution; subsequent edits completed the
  first block, producing two proofs of the same integral by the same method.
- **Impact and owner:** the workstream handoff/dispatch boundary permits
  overlapping authorship and rejected calls. This is not a corpus parser,
  mathematical, or publication-gate defect.
- **Uncertainty:** the rejected calls and overlapping card contents were
  observed directly; the mechanism initiating the competing continuations
  has not been established.
- **Repair:** the card is reconciled by removing this session's duplicate
  and retaining the other complete proof unchanged. The external handoff
  remains unresolved: a successor must not race a still-writing predecessor,
  and must reread the final settled card before editing it.
