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

### Duplicate Burnside lemma cards C-CM7ZS and C-HE5SL

- **Object and need:** `C-CM7ZS` and `C-HE5SL` in
  `corpus/theory/Algebra`. The copy-policy pass must preserve one canonical
  statement rather than two intrinsic cards for the same mathematics
  (`CARD-04`, `SOURCE-02`).
- **Observed evidence:** both complete cards have the title `Burnside's
  lemma`, the same hypotheses (a finite group acting on a finite set), the
  same fixed-point notation, and the same orbit-count formula. Before repair,
  `C-CM7ZS` also declared itself `variant-of: C-HE5SL`. The wiki references
  `C-HE5SL`; the only other reader-facing reference to `C-CM7ZS` was the
  algebra-guide publication list.
- **Impact and owner:** retaining both cards gives two addresses for one
  theorem and lets guide surfaces disagree about which one is canonical.
  `C-HE5SL` is the existing wiki-facing owner; the algebra guide must point to
  it and the duplicate card must be removed.
- **Uncertainty:** none after reading both complete cards; there is no
  mathematical or source-appearance distinction between them.
- **Repair:** the same repair commit redirects `publications/algebra-guide.yaml`
  to `C-HE5SL` and removes `C-CM7ZS`.

### Second duplicate Burnside card FF-OL75S

- **Object and need:** `C-HE5SL` and `FF-OL75S` in
  `corpus/theory/Algebra`. Both state Burnside's orbit-counting formula for a
  finite group acting on a finite set.
- **Observed evidence:** the displayed formulas are identical after the
  notational substitution `$X^g=\Fix(g)$`; `FF-OL75S` adds only the review
  prompt and the standard double-counting proof. The wiki and algebra guide
  displayed both cards.
- **Impact and owner:** a second flashcard-derived address remained for the
  same theorem after the earlier `C-CM7ZS` duplicate was removed.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the review prompt and double-counting
  proof to `C-HE5SL`, removes duplicate reader-facing references, and deletes
  `FF-OL75S`.

### Duplicate class-equation cards C-A6UAR, C-O7CP3, and FD-L2TEC

- **Object and need:** `C-A6UAR`, `C-O7CP3`, and `FD-L2TEC` in
  `corpus/theory/Algebra`. They are intrinsic cards for the same class
  equation (`CARD-04`, `SOURCE-02`).
- **Observed evidence:** after reading all three complete cards, they have the same
  title, hypotheses, centralizer notation, choice of noncentral conjugacy-class
  representatives, and class-equation formula. Their only substantive source
  difference is presentation syntax (`\#` versus the repository's `\size`
  macro). `FD-L2TEC` later restated the same theorem and added its standard
  conjugation-action proof. The wiki and algebra guide exposed the duplicate
  theorem beside `C-O7CP3`.
- **Impact and owner:** retaining the duplicates gives multiple canonical-looking
  addresses for one theorem and splits guide references. `C-O7CP3` is already the
  wiki-facing statement and uses the current notation convention.
- **Uncertainty:** none after reading all three complete cards; no distinct source
  appearance or mathematical variant was found.
- **Repair:** the first repair redirected the algebra guide to `C-O7CP3` and
  removed `C-A6UAR`; the later repair moves the review prompt and proof from
  `FD-L2TEC` onto `C-O7CP3`, removes duplicate reader-facing references, and
  deletes `FD-L2TEC`.

### Duplicate coset-counting cards C-HWX2P and C-XRC67

- **Object and need:** `C-HWX2P` and `C-XRC67` in
  `corpus/theory/Algebra`. They state the same coset-counting formula and
  therefore violate the single-owner expectation for standard statements
  (`CARD-04`, `SOURCE-02`).
- **Observed evidence:** both complete cards have the same title, hypotheses,
  definition of the index, and equations
  `$\size G=[G:H]\,\size H$` and `$[G:H]=\size G/\size H$`, differing only
  by `\size` versus `\#` presentation syntax. `C-XRC67` also declares itself
  `variant-of: C-HWX2P`. The wiki and algebra guide both reference
  `C-HWX2P`; no reader-facing surface references `C-XRC67`.
- **Impact and owner:** retaining `C-XRC67` creates a second intrinsic address
  for the same theorem without a source or mathematical distinction.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit removes `C-XRC67` and retains
  `C-HWX2P` as the canonical statement.

### Zero-divisor definition was wrong for noncommutative rings and duplicated

- **Object and need:** `D-4I3SL` and `FD-S62UB` in
  `corpus/theory/Algebra`. `D-GURUB` defines rings without commutativity, but
  `D-4I3SL` defined a zero divisor by requiring one nonzero element to
  annihilate the given element on both the left and the right. `FD-S62UB`
  separately gave the standard commutative definition.
- **Observed evidence:** `D-4I3SL` quantified over an arbitrary ring and
  required `$ar=ra=0$`; `FD-S62UB` quantified over a commutative ring and
  required a nonzero `$x$` with `$rx=0$`. Current uses of the zero-divisor
  card in the domain, primary-ideal, and Noetherian-ring material are in the
  commutative setting. The wiki and algebra guide exposed both definitions
  side by side.
- **Impact and owner:** the canonical card misstated the noncommutative notion
  and duplicated a second card for the commutative notion. In a
  noncommutative ring, left and right zero divisors need not coincide; the
  simultaneous two-sided condition is not the standard generic definition.
- **Uncertainty:** none about the defect. The corpus currently needs the
  commutative notion; noncommutative left/right variants can be introduced
  separately if needed later.
- **Repair:** the same repair commit restricts `D-4I3SL` to commutative rings,
  uses the standard annihilator definition, preserves the review prompt there,
  removes duplicate reader-facing references to `FD-S62UB`, and deletes the
  duplicate card.

### D-5JYEI delegated the separable-degree statement to an opaque screenshot

- **Object and need:** `D-5JYEI`, Galois extension and Galois group. The
  closing remark states that separable degree counts embeddings but then shows
  only a legacy image with filename alt text instead of the formula.
- **Observed evidence:** the card ended with
  `![figures/2021-08-09_22-29-40.png](../../assets/figures/...)`; no surrounding
  prose stated the embedding set or explained how the Galois automorphism
  count follows.
- **Impact and owner:** the card's last mathematical claim was inaccessible to
  text readers and dependent on an unexplained asset. The relevant formula is
  intrinsic to the theorem and should be authored as mathematics on the card.
- **Uncertainty:** none; for a finite extension, the separable degree is the
  number of `$k$`-embeddings into a fixed algebraic closure.
- **Repair:** the same repair commit replaces the screenshot with the formula
  `$[L:k]_s=\size\Hom_{k\text{-alg}}(L,\bar k)$` and explains why normality
  identifies these embeddings with `\Gal(L/k)` in the Galois case.

### Duplicate lower-central-series cards D-BGNME and D-D7L4X

- **Object and need:** `D-BGNME` and `D-D7L4X` in
  `corpus/theory/Algebra`. The two cards gave the same definition of the lower
  central series (`CARD-04`, `SOURCE-02`).
- **Observed evidence:** both complete cards define `$G^0=G$` and
  `$G^{i+1}=[G,G^i]$` using the same commutator convention. `D-D7L4X`
  declares itself `variant-of: D-BGNME`; `D-BGNME` additionally records the
  nilpotence characterization. The wiki and algebra guide exposed both.
- **Impact and owner:** two intrinsic addresses for the same definition split
  links and duplicate the recall unit. `D-BGNME` is already used by
  `T-4INET` and contains the strictly richer local exposition.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit redirects the wiki to `D-BGNME`, removes
  the duplicate guide entry, and deletes `D-D7L4X`.

### D-KRKV7 printed an incorrect presentation of the quaternion group

- **Object and need:** `D-KRKV7`, Quaternion group `$Q_8$`. The second
  displayed presentation must actually force the generators to have the
  quaternion orders.
- **Observed evidence:** the card printed
  `$\gens{x,y\mid x^4=y^4,\ x^2=y^2,\ yxy^{-1}=x^{-1}}$`. The relation
  `$x^4=y^4$` follows already from `$x^2=y^2$` and does not impose
  `$x^4=1$`.
- **Impact and owner:** the displayed group need not be finite and is not the
  standard presentation of `$Q_8$`. The canonical presentation requires
  `$x^4=1$`, `$x^2=y^2$`, and `$yxy^{-1}=x^{-1}$`.
- **Uncertainty:** none; the standard two-generator presentation is explicit.
- **Repair:** the same repair commit replaces `$x^4=y^4$` by `$x^4=1$` and
  states the eight quaternion elements directly rather than treating `-1` as
  a presentation generator.

### D-LIEMF marked the free-module universal map as injective without hypothesis

- **Object and need:** `D-LIEMF`, Free module. The universal property of the
  free module uses a set map `$\iota:\mathcal B\to M$`; injectivity is not
  part of the universal property's statement.
- **Observed evidence:** the commutative diagram rendered the arrow labelled
  `$\iota$` with `hook`, although item (2) only assumes a map of sets. Over
  the zero ring, the free module on a nonempty set is the zero module and the
  universal structure map is not injective as a set map.
- **Impact and owner:** the diagram asserted a stronger property than the
  proposition and one that fails in an allowed ring case.
- **Uncertainty:** none; the free-module adjunction requires a map, not an
  injection.
- **Repair:** the same repair commit removes the hook decoration from the
  `$\iota$` arrow and leaves the universal property unchanged.

### Gram matrix had two defining cards

- **Object and need:** `D-H4TDM` and `D-RG5FO` in
  `corpus/theory/Algebra`. Both cards defined the Gram matrix of a bilinear
  form, contrary to the single canonical defining-occurrence policy.
- **Observed evidence:** `D-H4TDM` defines the matrix
  `$(b(e_i,e_j))$` and records change of basis and nondegeneracy;
  `D-RG5FO` independently defined the same matrix and then proved the distinct
  proposition that Gram matrices classify bilinear forms in a fixed basis.
  The wiki linked the term “Gram matrix” to `D-RG5FO` while other theory cards
  linked it to `D-H4TDM`.
- **Impact and owner:** the duplicated definition split the canonical link,
  while the useful classification proposition on `D-RG5FO` should be retained
  as separate mathematics.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit keeps `D-H4TDM` as the definition owner,
  converts `D-RG5FO` to the proposition “Bilinear forms and Gram matrices,”
  and redirects the wiki's definitional link to `D-H4TDM`.

### D-SSGKC duplicated the quadratic-form definition

- **Object and need:** `D-NRRIT` and `D-SSGKC` in
  `corpus/theory/Algebra`. `D-NRRIT` is the basis-free definition of a
  quadratic form, while `D-SSGKC` independently redefined a quadratic form as
  a degree-two polynomial before discussing its coordinate matrix and real
  signature.
- **Observed evidence:** the two complete cards define the same object in
  equivalent forms when the characteristic is not `2`; `D-SSGKC` already had
  a relation to `D-NRRIT` and a final concept block restating the basis-free
  definition.
- **Impact and owner:** the coordinate card duplicated the canonical
  definiendum rather than using it, while its matrix/signature material is
  distinct and useful.
- **Uncertainty:** none; in characteristic different from `2`, a basis-free
  quadratic form on `$k^n$` has a unique symmetric coordinate matrix.
- **Repair:** the same repair commit makes `D-SSGKC` use `D-NRRIT`, defines
  only the coordinate matrix and signature locally, and moves the Artin
  citation onto Sylvester's law of inertia.

### D-TZXBO used commutative Noetherian terminology on arbitrary rings

- **Object and need:** `D-TZXBO`, Noetherian ring. `D-GURUB` allows
  noncommutative rings and `D-GOFWL` defines an unqualified ideal there to
  mean a two-sided ideal.
- **Observed evidence:** `D-TZXBO` quantified over an arbitrary ring and
  called ACC on those two-sided ideals “Noetherian.” In noncommutative ring
  theory the standard notions are left-Noetherian and right-Noetherian; ACC
  only on two-sided ideals is a different condition. Every current use of
  `D-TZXBO` in the corpus and wiki is in commutative algebra.
- **Impact and owner:** the canonical definition silently changed meaning
  outside the commutative setting and could be read as the standard
  noncommutative notion when it is not.
- **Uncertainty:** none about current scope; all observed consumers are
  commutative.
- **Repair:** the same repair commit restricts `D-TZXBO` to commutative rings
  and leaves left/right Noetherian notions for separate definitions if they
  are ever needed.

### Group action had two defining cards

- **Object and need:** `D-WYC7C` and `D-3T6O2` in
  `corpus/theory/Algebra`. Both cards independently defined a group action,
  while `D-3T6O2` also contained the distinct action/homomorphism
  correspondence.
- **Observed evidence:** both complete cards used the same axioms
  `$e\cdot x=x$` and `$g\cdot(h\cdot x)=(gh)\cdot x$`. `D-WYC7C` additionally
  owns orbit, stabilizer, and fixed-point definitions and is already the main
  dependency of the action theorems. Reader-facing links were split between
  the two cards.
- **Impact and owner:** duplicate defining occurrences split the canonical
  concept link, while deleting `D-3T6O2` would discard its useful proposition
  identifying actions with homomorphisms into `\Aut(X)`.
- **Uncertainty:** none after reading both live cards; the older candidate
  `D-BVOUL` is absent from the current tree.
- **Repair:** the same repair commit keeps `D-WYC7C` as the definition owner,
  converts `D-3T6O2` to the action/homomorphism proposition, and redirects
  definitional links to `D-WYC7C`.

### Duplicate UFD cards D-INULL and FD-25SUQ

- **Object and need:** `D-INULL` and `FD-25SUQ` in
  `corpus/theory/Algebra`. Both cards gave the full definition of a unique
  factorization domain, including existence and uniqueness up to order and
  associates.
- **Observed evidence:** the complete statements are mathematically identical;
  `D-INULL` is the dependency used by the UFD theorems and polynomial-ring
  material, while `FD-25SUQ` came from the flashcard migration. The wiki and
  algebra guide displayed both adjacent to one another.
- **Impact and owner:** the duplicate flashcard creates a second defining
  occurrence and splits review/navigation without adding mathematics.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the flashcard review prompt to
  `D-INULL`, removes duplicate reader-facing references, and deletes
  `FD-25SUQ`.

### Duplicate integral-domain cards D-QJ3QL and FD-2A5XH

- **Object and need:** `D-QJ3QL` and `FD-2A5XH` in
  `corpus/theory/Algebra`. Both cards define a nonzero commutative ring with no
  nonzero zero divisors.
- **Observed evidence:** the complete statements are mathematically identical.
  `D-QJ3QL` is the dependency used throughout the ring and factorization
  theory; `FD-2A5XH` is a migrated flashcard and the wiki displayed it
  immediately beside `D-QJ3QL`.
- **Impact and owner:** the flashcard duplicate creates a second canonical
  definition without additional mathematics.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the review prompt to `D-QJ3QL`,
  removes the duplicate wiki entry, and deletes `FD-2A5XH`.

### Duplicate indecomposable-module cards D-4HEUB and FD-2EUYX

- **Object and need:** `D-4HEUB` and `FD-2EUYX` in
  `corpus/theory/Algebra`. `D-4HEUB` already defines decomposable and
  indecomposable modules; `FD-2EUYX` repeats the indecomposable definition.
- **Observed evidence:** both complete statements say that a nonzero module is
  indecomposable exactly when it cannot be written as a direct sum of two
  nonzero submodules. The wiki and algebra guide displayed both adjacent to
  one another.
- **Impact and owner:** the flashcard duplicate adds no mathematics and creates
  a second defining occurrence.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the review prompt to `D-4HEUB`,
  removes duplicate reader-facing references, and deletes `FD-2EUYX`.

### Simple ring had a second defining occurrence on the simple-module card

- **Object and need:** `FD-SNOTW` and `D-4KM4P` in
  `corpus/theory/Algebra`. `FD-SNOTW` defines simple rings for arbitrary
  rings, while `D-4KM4P` independently defined the commutative special case
  alongside simple modules.
- **Observed evidence:** `D-4KM4P` called a commutative ring simple when it is
  simple as a module over itself, equivalently when its only ideals are `0`
  and `R`; `FD-SNOTW` gives the same two-sided-ideal definition without the
  unnecessary commutativity restriction.
- **Impact and owner:** the term “simple” had two defining occurrences for
  rings, while `D-4KM4P` is otherwise the canonical simple-module card.
- **Uncertainty:** none; the general ring definition specializes to the
  commutative statement.
- **Repair:** the same repair commit leaves `FD-SNOTW` as the sole simple-ring
  owner, removes the ring definition from `D-4KM4P`, and records the relation
  between the two cards.

### Duplicate cyclic-module cards D-HY7UU and FD-S2W5E

- **Object and need:** `D-HY7UU` and `FD-S2W5E` in
  `corpus/theory/Algebra`. Both define a cyclic module as a module generated by
  one element.
- **Observed evidence:** the definition blocks are identical. `FD-S2W5E`
  additionally proves the standard characterization `$M\cong R/I$` for a
  left ideal `$I$`. The wiki and algebra guide displayed both cards.
- **Impact and owner:** the duplicate definition splits the recall unit, while
  the quotient characterization is useful and should be retained on the
  canonical card.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the prompt and quotient
  characterization/proof to `D-HY7UU`, removes duplicate reader-facing
  references, and deletes `FD-S2W5E`.

### Duplicate torsion-free-module card FD-U6KUJ

- **Object and need:** `D-ZJJ7G` and `FD-U6KUJ` in
  `corpus/theory/Algebra`. `D-ZJJ7G` already defines torsion-free modules;
  `FD-U6KUJ` restates the integral-domain special case as vanishing of the
  torsion submodule.
- **Observed evidence:** over an integral domain the torsion set on `D-ZJJ7G`
  is exactly the torsion submodule of `FD-BPUNZ`, so `$M_t=\{0\}$` and
  `$\tor(M)=0$` are the same condition. The wiki and algebra guide exposed
  both definitions.
- **Impact and owner:** the flashcard adds no distinct mathematics and splits
  the definition of torsion-free modules.
- **Uncertainty:** none after reading the canonical torsion card, the
  domain-specific torsion-submodule card, and `FD-U6KUJ`.
- **Repair:** the same repair commit moves the review prompt to `D-ZJJ7G`,
  removes duplicate reader-facing references, and deletes `FD-U6KUJ`.

### Duplicate simple-group cards D-T2NZ4 and FD-2UWAQ

- **Object and need:** `D-T2NZ4` and `FD-2UWAQ` in
  `corpus/theory/Algebra`. Both cards define a nontrivial group whose only
  normal subgroups are the identity subgroup and the whole group.
- **Observed evidence:** the complete definitions are mathematically
  identical. `D-T2NZ4` is used by the alternating-group and finite-index
  arguments; `FD-2UWAQ` is a migrated flashcard. The wiki and algebra guide
  exposed both, and one flashcard-derived series card still linked to the
  duplicate.
- **Impact and owner:** the flashcard duplicate creates a second defining
  occurrence and splits dependencies.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the prompt and citation to
  `D-T2NZ4`, redirects the remaining dependency, removes duplicate
  reader-facing references, and deletes `FD-2UWAQ`.

### Duplicate composition-series cards D-FYX4I and FD-PLAEO

- **Object and need:** `D-FYX4I` and `FD-PLAEO` in
  `corpus/theory/Algebra`. They define the same finite normal series, with
  `D-FYX4I` descending by maximal proper normal subgroups and `FD-PLAEO`
  ascending with simple successive quotients.
- **Observed evidence:** those conditions are equivalent, since
  `$N_i\normal N_{i+1}$` is maximal proper exactly when
  `$N_{i+1}/N_i$` is simple. `FD-PLAEO` additionally names the successive
  simple quotients as composition factors. The wiki and algebra guide exposed
  both cards, and `FD-T7IQV` linked to the flashcard duplicate.
- **Impact and owner:** two cards owned one definition, while the composition
  factor terminology belongs naturally on the canonical series card.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the prompt and composition-factor
  terminology to `D-FYX4I`, redirects `FD-T7IQV`, removes duplicate
  reader-facing references, and deletes `FD-PLAEO`.

### FD-T7IQV restated solvability as a definition instead of a finite-group criterion

- **Object and need:** `D-DFIDP` and `FD-T7IQV` in
  `corpus/theory/Algebra`. `D-DFIDP` canonically defines solvable groups by a
  finite normal series with abelian quotients; `FD-T7IQV` independently
  defined finite-group solvability via abelian composition factors.
- **Observed evidence:** the latter condition is an equivalent theorem for
  finite groups, not a second definition owner. No other card states this
  composition-factor criterion.
- **Impact and owner:** keeping the card as a definition duplicated the term,
  while deleting it would lose a useful finite-group characterization.
- **Uncertainty:** none; the equivalence follows because subgroups and
  quotients of solvable groups are solvable and a simple solvable group is
  abelian.
- **Repair:** the same repair commit converts `FD-T7IQV` to the proposition
  “Solvability via composition factors,” links it to the canonical solvability
  and composition-series cards, and adds the proof of the equivalence.

### Duplicate finite-Galois card FD-4GFTY

- **Object and need:** `D-5JYEI` and `FD-4GFTY` in
  `corpus/theory/Algebra`. The canonical Galois card defines finite Galois
  extensions by normality and separability and proves the automorphism-count
  condition as an equivalent characterization; the flashcard restates that
  characterization as a second definition.
- **Observed evidence:** `D-5JYEI` item (5) states
  `$\size\Aut_F(K)=[K:F]_s=[K:F]$`; `FD-4GFTY` defines Galois by
  `$\abs{\Aut(K/F)}=[K:F]$`. The wiki and algebra guide displayed both.
- **Impact and owner:** the flashcard duplicates an equivalent condition
  already owned by the canonical card and creates a second defining surface.
- **Uncertainty:** none after reading both cards.
- **Repair:** the same repair commit moves the automorphism-count review
  prompt to `D-5JYEI`, removes duplicate reader-facing references, and deletes
  `FD-4GFTY`.

### Duplicate finite-Galois characterization theorem FT-3WWKN

- **Object and need:** `D-5JYEI` and `FT-3WWKN` in
  `corpus/theory/Algebra`. Both list equivalent characterizations of a finite
  Galois extension.
- **Observed evidence:** `FT-3WWKN` lists separable splitting field, fixed
  field, full automorphism count, and normal-plus-separable. `D-5JYEI` already
  contains all four and additionally the irreducible separable splitting-field
  characterization and the separable-degree equality.
- **Impact and owner:** the flashcard theorem duplicates a strictly richer
  canonical card; one downstream example still linked to the duplicate.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit adds a characterization review prompt to
  `D-5JYEI`, redirects the downstream link, removes duplicate reader-facing
  references, and deletes `FT-3WWKN`.

### Duplicate fundamental-theorem-of-Galois-theory cards

- **Object and need:** `FT-GJ6NR` and `T-NLPZY` in
  `corpus/theory/Algebra`. Both state the subgroup/intermediate-field
  anti-isomorphism and its standard consequences.
- **Observed evidence:** the field/subgroup bijection, inclusion reversal,
  degree formulas, normal-subgroup criterion, and compositum/intersection
  formulas agree exactly. `T-NLPZY` additionally records the normalizer of an
  intermediate field and distinguishes `$\langle H_1,H_2\rangle$` from the
  product set `$H_1H_2$`; `FT-GJ6NR` contributes only the review prompt.
- **Impact and owner:** the same major theorem had two intrinsic addresses in
  the Galois wiki and algebra guide.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the review prompt to `T-NLPZY`,
  removes duplicate reader-facing references, and deletes `FT-GJ6NR`.

### Duplicate irreducible-element cards D-TO3IY and FD-6LLJF

- **Object and need:** `D-TO3IY` and `FD-6LLJF` in
  `corpus/theory/Algebra`. Both define a nonzero nonunit `$r$` to be
  irreducible when every factorization `$r=ab$` has a unit factor.
- **Observed evidence:** the complete definitions are mathematically
  identical. `D-TO3IY` is used by the UFD and prime-element material;
  `FD-6LLJF` is a migrated flashcard and the wiki displayed it beside the
  canonical card.
- **Impact and owner:** the flashcard duplicate creates a second defining
  occurrence without additional mathematics.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the review prompt to `D-TO3IY`,
  removes the duplicate wiki link, and deletes `FD-6LLJF`.

### Duplicate prime-element cards D-AWSKI and FD-S52W7

- **Object and need:** `D-AWSKI` and `FD-S52W7` in
  `corpus/theory/Algebra`. Both define a nonzero nonunit `$p$` to be prime
  when `$p\divides ab$` implies `$p\divides a$` or `$p\divides b$`.
- **Observed evidence:** the definition bodies are mathematically identical.
  `D-AWSKI` is the dependency used by the prime-versus-irreducible theorem and
  factorization wiki; the wiki displayed `FD-S52W7` beside it.
- **Impact and owner:** the flashcard adds no distinct mathematics and creates
  a second defining occurrence.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the review prompt to `D-AWSKI`,
  removes the duplicate wiki link, and deletes `FD-S52W7`.

### FD-R4K7Z was a second irreducible-element duplicate with a false variant edge

- **Object and need:** `FD-R4K7Z` in `corpus/theory/Algebra`. The card defines
  irreducible elements of a commutative ring, which is already owned by
  `D-TO3IY`, but declared itself `variant-of: FD-GHY34`, a polynomial
  irreducibility card.
- **Observed evidence:** its body is the same ring-element condition as
  `D-TO3IY`: a nonzero nonunit `$p$` with every factorization `$p=ab$` having
  a unit factor. `FD-GHY34` instead quantifies over polynomials in `$K[x]$`.
- **Impact and owner:** the card both duplicated the canonical definition and
  asserted a variant relation between different levels of generality/objects.
- **Uncertainty:** none after reading all three cards.
- **Repair:** the same repair commit removes the duplicate wiki link and
  deletes `FD-R4K7Z`; `D-TO3IY` already carries the equivalent review prompt.

### Duplicate irreducible-polynomial cards D-BVMTZ, FD-GHY34, and FD-KPW3H

- **Object and need:** `D-BVMTZ`, `FD-GHY34`, and `FD-KPW3H` in
  `corpus/theory/Algebra`. All three define irreducibility of a polynomial over
  a field by absence of a factorization into two positive-degree factors.
- **Observed evidence:** the definitions are equivalent; `FD-GHY34` added the
  observation that degree-one polynomials are irreducible, while `FD-KPW3H`
  restates the same condition as “no factorization into two strictly
  lower-degree factors.” `D-BVMTZ` is the dependency used throughout Galois
  and factorization theory. The wiki exposed the flashcard definitions beside
  the canonical card.
- **Impact and owner:** the flashcard duplicates the defining occurrence while
  its small useful remark can live on the canonical card.
- **Uncertainty:** none after reading all three complete cards.
- **Repair:** the first repair moved the prompt and linear-polynomial remark to
  `D-BVMTZ` and deleted `FD-GHY34`; the later repair moves the factor-degree
  review prompt to the same canonical card and deletes `FD-KPW3H`.

### FD-6WSIA duplicated the separable-extension definition

- **Object and need:** `D-JGYLA` and `FD-6WSIA` in
  `corpus/theory/Algebra`. Both cards defined separability of an algebraic
  field extension through separability of every element's minimal polynomial.
- **Observed evidence:** the definition blocks are equivalent; `FD-6WSIA`
  additionally proves the distinct criterion that an irreducible polynomial
  is separable exactly when its formal derivative is nonzero.
- **Impact and owner:** deleting the flashcard would discard useful
  mathematics, but retaining its definition would leave two owners for
  separable extension.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the two review prompts to
  `D-JGYLA` and converts `FD-6WSIA` to the proposition-only card
  “Irreducible separability criterion.”

### Duplicate projective-module cards D-RHJMK and FD-6XJ7D

- **Object and need:** `D-RHJMK` and `FD-6XJ7D` in
  `corpus/theory/Algebra`. Both define projective modules by the lifting
  property and prove that projective modules are exactly direct summands of
  free modules.
- **Observed evidence:** `D-RHJMK` contains the same lifting diagram and
  direct-summand proof and additionally records splitting of short exact
  sequences and exactness of `\Hom_R(P,-)`. The wiki and algebra guide
  displayed both cards.
- **Impact and owner:** the flashcard duplicates a strictly richer canonical
  card without preserving distinct mathematics.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the review prompt to `D-RHJMK`,
  removes duplicate reader-facing references, and deletes `FD-6XJ7D`.

### Duplicate maximal-ideal cards D-7XH2R and FD-CD2FE

- **Object and need:** `D-7XH2R` and `FD-CD2FE` in
  `corpus/theory/Algebra`. Both define a proper ideal to be maximal when no
  proper strictly larger ideal exists.
- **Observed evidence:** the complete definitions are mathematically
  identical. `D-7XH2R` is the dependency used throughout the ideal and local
  ring theory; `FD-CD2FE` is a migrated flashcard and the wiki displayed it
  beside the canonical card.
- **Impact and owner:** the duplicate flashcard adds no mathematics and creates
  a second defining occurrence.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the review prompt to `D-7XH2R`,
  removes the duplicate wiki link, and deletes `FD-CD2FE`.

### Duplicate prime-ideal cards D-5BM46 and FD-OSSYR

- **Object and need:** `D-5BM46` and `FD-OSSYR` in
  `corpus/theory/Algebra`. Both define a proper ideal `$\mathfrak p$` of a
  commutative ring to be prime when `$ab\in\mathfrak p$` implies
  `$a\in\mathfrak p$` or `$b\in\mathfrak p$`.
- **Observed evidence:** the definitions are identical. `D-5BM46` is the
  dependency used by the prime spectrum, quotient criterion, and height
  theorems; the wiki displayed `FD-OSSYR` immediately beside it.
- **Impact and owner:** the flashcard adds no distinct mathematics and creates
  a second defining occurrence.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the review prompt to `D-5BM46`,
  removes the duplicate wiki link, and deletes `FD-OSSYR`.

### Sign homomorphism used incompatible codomains under one symbol

- **Object and need:** `D-BZ3KD`, `D-TMME3`, and the permutation/determinant
  cards using `\sgn`. The canonical sign map must have one type.
- **Observed evidence:** `D-BZ3KD` defined
  `$\sgn:S_n\to\ZZ/2$` by transposition parity, and `D-TMME3` therefore used
  `$\sgn(\sigma)=0$` for even permutations. `FD-GHDF2`, `FD-X4DBP`, and the
  determinant formulas use the conventional multiplicative sign
  `$\sgn:S_n\to\{\pm1\}$`.
- **Impact and owner:** the same notation had two incompatible codomains, so
  links to the canonical sign definition did not type-check against formulas
  using it multiplicatively.
- **Uncertainty:** none. The parity map and multiplicative sign are equivalent
  via `$k\bmod2\mapsto(-1)^k$`, but they are not the same typed map.
- **Repair:** the same repair commit makes `D-BZ3KD` own the conventional
  multiplicative sign, updates `D-TMME3` to use sign `1` for even
  permutations, and links `FD-GHDF2` to the canonical definition.

### Duplicate alternating-group card FD-X4DBP

- **Object and need:** `D-TMME3` and `FD-X4DBP` in
  `corpus/theory/Algebra`. `D-TMME3` already defines even/odd permutations and
  the alternating group as the kernel of the sign homomorphism; `FD-X4DBP`
  repeats only the latter definition.
- **Observed evidence:** both complete cards state
  `$A_n=\ker(\sgn)=\{\sigma\in S_n:\sgn(\sigma)=1\}$`. The wiki and algebra
  guide displayed both cards adjacent to one another.
- **Impact and owner:** the flashcard adds no distinct mathematics and creates
  a second defining occurrence.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the kernel review prompt to
  `D-TMME3`, removes duplicate reader-facing references, and deletes
  `FD-X4DBP`.

### Duplicate even/odd-permutation card FD-PIVQZ

- **Object and need:** `D-TMME3` and `FD-PIVQZ` in
  `corpus/theory/Algebra`. `D-TMME3` already owns the definition of even
  permutations and the alternating group; `FD-PIVQZ` repeats evenness and
  adds oddness plus the parity characterization.
- **Observed evidence:** after the sign convention repair, both use the same
  multiplicative sign `$S_n\to\{\pm1\}$`. The wiki and algebra guide exposed
  both recall units, and `FD-X4DBP` linked to the flashcard for “even.”
- **Impact and owner:** the duplicated evenness definition splits a basic
  permutation concept; the odd terminology and parity statement can be
  preserved on the canonical alternating-group card.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the prompt, odd definition, and
  parity remark to `D-TMME3`, redirects `FD-X4DBP`, removes duplicate
  reader-facing references, and deletes `FD-PIVQZ`.

### FD-CI4NB misclassified polynomial rings as a variant of rational-function fields

- **Object and need:** `FD-CI4NB`, Polynomial ring, and its relation to
  `FD-24RNF`, the field of rational functions.
- **Observed evidence:** the polynomial-ring card declared
  `variant-of: FD-24RNF`, although `$R[x]$` and `$K(x)$` are different
  constructions and the latter is the fraction field of `$K[x]$` when `$K$`
  is a field. The card also used `$K$` for an arbitrary commutative ring,
  making the coefficient type look field-specific.
- **Impact and owner:** the relation asserted mathematical equivalence where
  there is only a constructional relation, and the notation obscured the
  stated ring-level scope.
- **Uncertainty:** none after reading both cards.
- **Repair:** the same repair commit renames the coefficient ring `$R$`, uses
  the title `Polynomial ring $R[x]$`, and changes the relation to
  `related-to: FD-24RNF`.

### Duplicate characteristic-polynomial cards had inconsistent coefficient scope

- **Object and need:** `D-QFYAC` and `FD-GOB47` in
  `corpus/theory/Algebra`. Both define `$\det(xI-A)$`, but the canonical card
  unnecessarily restricted to matrices over a field while the flashcard used
  the correct commutative-ring scope.
- **Observed evidence:** the determinant definition makes sense over any
  commutative ring. The only field-specific content on `D-QFYAC` is its later
  Smith-normal-form remark over `$k[x]$`. The wiki and algebra guide displayed
  both definitions.
- **Impact and owner:** retaining both split a standard definition and made
  the canonical card less general than the duplicate.
- **Uncertainty:** none; characteristic polynomials are defined over arbitrary
  commutative coefficient rings, while Smith normal form here requires the
  field hypothesis.
- **Repair:** the same repair commit broadens `D-QFYAC` to a commutative ring,
  scopes its SNF remark to the field case, moves the review prompt there,
  removes duplicate reader-facing references, and deletes `FD-GOB47`.

### Duplicate normal-extension cards D-LZTAK and FD-JJFZ3

- **Object and need:** `D-LZTAK` and `FD-JJFZ3` in
  `corpus/theory/Algebra`. Both define an algebraic extension to be normal
  when every irreducible polynomial with one root in the extension splits
  there.
- **Observed evidence:** the complete definitions are equivalent. `D-LZTAK`
  is the dependency used by Galois and splitting-field theory; `FD-JJFZ3` is
  a migrated flashcard, and one proposition plus the wiki/guide still linked
  to it.
- **Impact and owner:** the flashcard creates a second definition and splits
  dependencies for a basic Galois-theory concept.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves both review prompts to `D-LZTAK`,
  redirects the remaining proposition, removes duplicate reader-facing
  references, and deletes `FD-JJFZ3`.

### Duplicate characteristic cards D-JNCUB and FD-LXZIW

- **Object and need:** `D-JNCUB` and `FD-LXZIW` in
  `corpus/theory/Algebra`. Both define the characteristic of a ring as the
  least positive `$n$` with `$n\cdot1_R=0$`, or `0` when no such integer
  exists.
- **Observed evidence:** the definitions are identical. `FD-LXZIW` adds the
  useful characterization as the nonnegative generator of the kernel of
  `$\ZZ\to R$`; `D-JNCUB` is the canonical dependency used by the field and
  separability theory. One problem card and a wiki page still linked to the
  flashcard duplicate.
- **Impact and owner:** the duplicate splits a basic ring invariant while the
  useful kernel characterization belongs naturally on the canonical card.
- **Uncertainty:** none after reading both complete cards; the older candidate
  `D-O26OY` is absent from the live tree.
- **Repair:** the same repair commit moves the review prompt and kernel
  characterization to `D-JNCUB`, redirects the problem-card reference,
  removes the duplicate wiki entry, and deletes `FD-LXZIW`.

### Duplicate Euclidean-domain cards D-NKRGN and FD-GXXBV

- **Object and need:** `D-NKRGN` and `FD-GXXBV` in
  `corpus/theory/Algebra`. Both define a Euclidean domain by a Euclidean
  function and the division-with-remainder inequality.
- **Observed evidence:** the only difference is that `D-NKRGN` defines the
  function on all of `$R$`, while `FD-GXXBV` defines it on `$R\setminus\{0\}$`;
  the Euclidean condition never requires a value at zero. The wiki and algebra
  guide displayed both cards.
- **Impact and owner:** the flashcard adds no mathematical distinction and
  creates a second defining occurrence.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the review prompt to `D-NKRGN`,
  removes duplicate reader-facing references, and deletes `FD-GXXBV`.

### Duplicate elementary-divisor card FD-H764S

- **Object and need:** `D-JQNJQ` and `FD-H764S` in
  `corpus/theory/Algebra`. `D-JQNJQ` defines the elementary-divisor
  decomposition for all finitely generated abelian groups; `FD-H764S`
  restates the finite special case and names the same prime-power factors.
- **Observed evidence:** `FD-H764S` explicitly invokes `D-JQNJQ` and then
  reproduces the decomposition with free rank zero. The wiki and algebra
  guide displayed both cards.
- **Impact and owner:** the finite flashcard adds no distinct mathematics and
  creates a second definition of elementary divisors.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the finite-group review prompt to
  `D-JQNJQ`, removes duplicate reader-facing references, and deletes
  `FD-H764S`.

### Duplicate perfect-field cards D-KQFIV and FD-YYLYR

- **Object and need:** `D-KQFIV` and `FD-YYLYR` in
  `corpus/theory/Algebra`. Both define perfect fields and prove the Frobenius
  criterion in positive characteristic.
- **Observed evidence:** `D-KQFIV` already gives the equivalence with
  separability of all irreducible polynomials and all finite extensions;
  `FD-YYLYR` repeats the same argument and adds only the review prompt and the
  finite-field consequence. Reader-facing links and three theory cards were
  split between the two owners.
- **Impact and owner:** the duplicate split the canonical perfect-field link
  across the corpus without adding distinct mathematics.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the prompt and finite-field remark
  to `D-KQFIV`, redirects all live theory references, removes duplicate
  reader-facing entries, and deletes `FD-YYLYR`.

### Duplicate matrix-power counterexamples

- **Object and need:** `FE-ISVDM`, `FE-W56LS`, and later `FF-VKYM3` in
  `corpus/theory/Algebra`. They answer the same prompt about whether
  `$A^n=B^n$` forces `$A=B$`.
- **Observed evidence:** `FE-ISVDM` and `FE-W56LS` both use
  `$M=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$`, `$M^2=I$`, and
  `$M\ne I$`; `FE-W56LS` already declares itself `variant-of: FE-ISVDM`.
  `FF-VKYM3` gives the same claim with another square-root-of-`$-I$` example.
  All three examples only treated `$n=2$`, even though their body copy said
  “for `$n\ge2$`.”
- **Impact and owner:** one intrinsic counterexample question had multiple
  addresses, and the displayed witnesses did not justify the universal
  `$n\ge2$` wording.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the first repair retained `FE-ISVDM` and deleted `FE-W56LS`.
  The later repair replaces its witness by the rotation matrix through
  `$2\pi/n$`, which works for every `$n\ge2$`, redirects the remaining guide
  and wiki references, and deletes `FF-VKYM3`.

### FF-6MNV6 called a disjoint-cycle product a cycle and changed sign notation

- **Object and need:** `FF-6MNV6`, the worked sign computation for a
  permutation in `$S_{18}$`.
- **Observed evidence:** the review prompt called
  `$(123456)(789)(10~11)(12~13~14~15)(16~17~18)$` “the cycle,” although it is
  a product of five disjoint cycles. The body also denoted sign by
  `$\varepsilon$` while the canonical sign homomorphism is `\sgn` on
  `D-BZ3KD`.
- **Impact and owner:** the prompt misstated the object type and the worked
  example drifted from the corpus's canonical sign notation.
- **Uncertainty:** none.
- **Repair:** the same repair commit says “permutation,” links the canonical
  sign card, and uses `\sgn` throughout the computation.

### FF-7U6UY had malformed and underspecified review copy

- **Object and need:** `FF-7U6UY`, the Jacobson-radical fact. Its review
  prompt should name the invariant in ordinary notation and scope the geometric
  interpretation to the hypotheses used by the card.
- **Observed evidence:** the prompt read `What is ${J ({R}) }$? How is it
  interpreted geometrically?`, while the geometric remark specifically uses a
  finitely generated algebra over an algebraically closed field.
- **Impact and owner:** the prompt exposed malformed legacy TeX and asked a
  broader geometric question than the answer on the card supports.
- **Uncertainty:** none.
- **Repair:** the same repair commit writes `$J(R)$` normally and states the
  finite-type/algebraically-closed scope in the prompt.

### Regular rings had two defining cards across Algebra and Algebraic Geometry

- **Object and need:** `D-DEFREGLR` and `FF-CQSNC`. Both cards defined regular
  local rings by the equality `$\dim R=\dim_k\mfm/\mfm^2$`, and both defined
  regular rings by regularity of all prime localizations.
- **Observed evidence:** `D-DEFREGLR` is the existing definition card used by
  the scheme-theory material. `FF-CQSNC` independently introduced the same
  definitions before applying Nakayama to identify the vector-space dimension
  with the minimal number of generators of `\mfm`.
- **Impact and owner:** the duplicate defining occurrences split one standard
  commutative-algebra concept across areas. The Nakayama/embedding-dimension
  observation is distinct and should remain available without redefining the
  term.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit makes `D-DEFREGLR` explicitly own
  `regular ring`, moves the review prompt there, and converts `FF-CQSNC` to the
  proposition “Embedding dimension criterion for regular local rings.”

### FF-ESIOA named only the nonzerodivisor corollary as Hauptidealsatz

- **Object and need:** `FF-ESIOA` and the canonical principal-ideal theorem on
  `PR-VARHT`.
- **Observed evidence:** `FF-ESIOA` was titled “Krull's Hauptidealsatz” but
  assumed the generator was a nonunit nonzerodivisor and concluded height
  exactly `1`. The actual principal ideal theorem says every prime minimal over
  a principal ideal has height at most `1`; exact height `1` is the stated
  corollary under the extra nonzerodivisor hypothesis. `PR-VARHT` already owns
  both statements.
- **Impact and owner:** the Algebra card mislabeled a strengthened corollary as
  the theorem itself, and `FF-CQSNC` linked to it when invoking Krull's height
  theorem.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit retitles `FF-ESIOA` as the
  nonzerodivisor corollary, links it to `PR-VARHT`, and redirects the
  height-theorem reference on `FF-CQSNC` to the canonical theorem card.

### Duplicate lying-over/going-up cards FF-IBDAT and PR-RJ3P7

- **Object and need:** `FF-IBDAT` and `PR-RJ3P7`. Both state lying over for
  integral extensions and the going-up theorem for chains of prime ideals.
- **Observed evidence:** the Algebra card is exactly the two algebraic clauses
  already contained in the first theorem block of `PR-RJ3P7`; the latter also
  proves closedness and states going down. The Algebra wiki and guide pointed
  to `FF-IBDAT`, while the algebraic-geometry wiki pointed to `PR-RJ3P7`.
- **Impact and owner:** one standard theorem had two intrinsic addresses split
  by subject area, with no mathematical or source-appearance distinction.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the plain “What is going up?” prompt
  to `PR-RJ3P7`, redirects the Algebra wiki and guide, and deletes
  `FF-IBDAT`.

### Krull's maximal-ideal theorem had three intrinsic cards

- **Object and need:** `PR-UTFSY`, `T-QSTRJ`, and `FF-QELG7` in
  `corpus/theory/Algebra`. All three state that every proper ideal is contained
  in a maximal ideal.
- **Observed evidence:** `PR-UTFSY` gives the full Zorn proof for arbitrary
  unital rings; `T-QSTRJ` states the same theorem without proof; `FF-QELG7`
  repeats it for commutative rings with the same Zorn proof and contributes
  the review prompt. The wiki and algebra guide displayed all three together.
- **Impact and owner:** one standard theorem had three canonical-looking
  addresses, and a downstream Jacobson-radical proof linked to the flashcard
  duplicate.
- **Uncertainty:** none after reading all three complete cards.
- **Repair:** the same repair commit keeps `PR-UTFSY`, gives it the Krull title
  and review prompt, redirects all live references, and deletes `T-QSTRJ` and
  `FF-QELG7`.

### Duplicate Eisenstein theorem cards FT-2P5VV and T-CF6S3

- **Object and need:** `FT-2P5VV` and `T-CF6S3` in
  `corpus/theory/Algebra`. Both state Eisenstein's criterion for
  `$f\in\ZZ[x]$` and prove it by Gauss's lemma and reduction modulo `$p$`.
- **Observed evidence:** the hypotheses and proof are the same. `T-CF6S3`
  additionally records the primitive-polynomial consequence giving
  irreducibility in `$\ZZ[x]$`; `FT-2P5VV` contributes only the review prompt.
  The Galois-theory wiki and algebra guide displayed both.
- **Impact and owner:** one standard irreducibility criterion had two theorem
  addresses, while the richer card strictly contains the other.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the review prompt to `T-CF6S3`,
  redirects the remaining theorem link, removes duplicate reader-facing
  references, and deletes `FT-2P5VV`.

### Gauss's lemma was split across two theorem cards

- **Object and need:** `FT-OXN3Y` and `T-JEZZY` in
  `corpus/theory/Algebra`. Both are standard forms of Gauss's lemma rather
  than genuinely separate theorems.
- **Observed evidence:** `FT-OXN3Y` states that a factorization in the fraction
  field descends to `$R[x]$` with the same factor degrees; `T-JEZZY` gives the
  primitive-polynomial irreducibility equivalence and the sharper scalar
  rescaling statement. The wiki and algebra guide displayed both together.
- **Impact and owner:** one theorem was split between two addresses, and a
  Hartshorne collection card linked specifically to the weaker half.
- **Uncertainty:** none after reading both cards; the two forms are standard
  parts of the same Gauss lemma.
- **Repair:** the same repair commit merges both forms and the polynomial-UFD
  consequence onto `T-JEZZY`, moves the review prompt there, redirects all
  live references, and deletes `FT-OXN3Y`.

### Duplicate reduced-ring card FF-U4FHF

- **Object and need:** `D-PQHHJ` and `FF-U4FHF` in
  `corpus/theory/Algebra`. Both say that a ring is reduced exactly when it has
  no nonzero nilpotent elements.
- **Observed evidence:** `D-PQHHJ` is the canonical definition used by the
  radical-ideal quotient criterion; `FF-U4FHF` repeats it for commutative rings
  and adds only the review prompt and the equivalent nilradical formulation.
  The wiki and algebra guide displayed both.
- **Impact and owner:** the flashcard adds no independent mathematics and
  creates a second defining occurrence.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the prompt and commutative
  nilradical equivalence to `D-PQHHJ`, removes duplicate reader-facing
  references, and deletes `FF-U4FHF`.

### Duplicate stabilizer card FD-IGEOR

- **Object and need:** `D-WYC7C` and `FD-IGEOR` in
  `corpus/theory/Algebra`. `D-WYC7C` already defines the stabilizer `$G_x$`;
  `FD-IGEOR` repeats that definition and adds only prompts plus the proof that
  `$G_x$` is a subgroup.
- **Observed evidence:** both complete cards use
  `$G_x=\{g\in G\mid g\cdot x=x\}$`. The canonical action card is the
  dependency used throughout orbit–stabilizer theory, while the wiki and
  algebra guide displayed the flashcard as an additional recall unit.
- **Impact and owner:** the duplicated definition splits a basic group-action
  concept, while the subgroup fact belongs naturally on the canonical card.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the two prompts and subgroup
  proposition/proof to `D-WYC7C`, removes duplicate reader-facing references,
  and deletes `FD-IGEOR`.

### Duplicate subset-centralizer card FD-SSR6N

- **Object and need:** `D-PX64W` and `FD-SSR6N` in
  `corpus/theory/Algebra`. `D-PX64W` already defines the centralizer of an
  arbitrary subset; `FD-SSR6N` repeats the same condition with notation
  `$Z_G(S)$`.
- **Observed evidence:** both cards define the subgroup of `$g\in G$` that
  satisfy `$gsg^{-1}=s$` for every `$s\in S$`. The wiki displayed the
  flashcard beside the canonical centralizer card.
- **Impact and owner:** the flashcard adds no distinct mathematics and creates
  a second defining occurrence for subset centralizers.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the review prompt to `D-PX64W`,
  removes the duplicate wiki link, and deletes `FD-SSR6N`.

### Duplicate transitive-action cards D-KGGWK and FD-KSKDG

- **Object and need:** `D-KGGWK` and `FD-KSKDG` in
  `corpus/theory/Algebra`. Both define transitivity of a group action by the
  condition that for every `$x,y\in X$` some `$g\in G$` satisfies
  `$g\cdot x=y$`.
- **Observed evidence:** the definitions are identical. `D-KGGWK` is the
  dependency used by transitive subgroups, covering-space theory, and the
  canonical group-action card; the wiki displayed `FD-KSKDG` beside it.
- **Impact and owner:** the flashcard adds no distinct mathematics and creates
  a second defining occurrence.
- **Uncertainty:** none after reading both complete cards.
- **Repair:** the same repair commit moves the review prompt to `D-KGGWK`,
  removes the duplicate wiki link, and deletes `FD-KSKDG`.

### FD-J3HIA treated $K(\alpha)$ as a variant of $K[\alpha]$

- **Object and need:** `FD-J3HIA`, generated subfield `$K(\alpha)$`, and
  `FD-3V3ZW`, generated subring `$K[\alpha]$`.
- **Observed evidence:** `FD-J3HIA` declared `variant-of: FD-3V3ZW`, although
  the two constructions differ for transcendental `$\alpha$`.
- **Impact and owner:** the relation asserted equivalence between a subfield
  and a subring construction. Equality requires the additional hypothesis
  that `$\alpha$` is algebraic over `$K$`.
- **Uncertainty:** none.
- **Repair:** the same repair commit changes the edge to `related-to` and
  records `$K[\alpha]\subseteq K(\alpha)$`, equality for algebraic
  `$\alpha$`, and the polynomial/rational-function distinction in the
  transcendental case.

### Duplicate generated-subfield card FD-QPNDA

- **Object and need:** `FD-J3HIA` and `FD-QPNDA` in
  `corpus/theory/Algebra`. Both define `$K(\alpha)$` as the smallest subfield
  of an ambient extension containing `$K$` and `$\alpha$`.
- **Observed evidence:** the definition bodies are identical. `FD-QPNDA`
  declared itself `variant-of: FD-J3HIA` and also repeated the already-false
  `variant-of: FD-3V3ZW` edge to the generated subring `$K[\alpha]$`. The wiki
  and algebra guide exposed both generated-subfield cards.
- **Impact and owner:** the duplicate adds no mathematics and reintroduces the
  subfield/subring conflation repaired on `FD-J3HIA`.
- **Uncertainty:** none after reading both complete generated-subfield cards.
- **Repair:** the same repair commit moves the additional review prompt to
  `FD-J3HIA`, removes duplicate reader-facing references, and deletes
  `FD-QPNDA`.

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
