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

### UCLA Spring 2016 Problem 11 omits normalization in the logarithmic determinant limit

- **Object and need:** P-UCLAB16S-11 in SRC-UCLA-BASIC-SPRING-2016. The source asks to prove that log det(M_n) has a limit as n tends to infinity and to compute it.

- **Observed evidence:** the retained scan states the unnormalized logarithm.
  For a=b=1, the determinant recurrence is D_n=D_{n-1}+D_{n-2} with positive initial values, so D_n grows exponentially and log D_n tends to positive infinity rather than a finite real limit.

- **Impact and owner:** the literal finite-limit claim is false in general.
  The natural asymptotic statement is for (1/n) log det(M_n), whose limit is log((a+sqrt(a^2+4b^2))/2).

- **Uncertainty:** none about the counterexample or source wording.
  The missing 1/n normalization is inferred from the standard Toeplitz-determinant asymptotic.

- **Repair:** TODO.md section 7 / issue #2. P-UCLAB16S-11 should preserve the literal source, compute det(M_n), classify the literal extended-real behavior, and record the normalized finite limit.

### UCLA Spring 2016 Problem 3 has an extra factor of n and is false as printed

- **Object and need:** P-UCLAB16S-03 in SRC-UCLA-BASIC-SPRING-2016. The source asks for the limit of n times the quantity sum_{k=0}^n f(k/n) minus n times the integral.

- **Observed evidence:** the retained scan was inspected directly and contains the outer factor n. For the constant C^1 function f=1, the inner quantity is (n+1)-n=1, so the displayed expression equals n and diverges.

- **Impact and owner:** the literal problem has no finite answer in general.
  Removing the outer factor n gives the standard first-order Riemann-sum correction, whose limit is (f(0)+f(1))/2.

- **Uncertainty:** none about the literal counterexample or the retained source wording.
  The intended correction is inferred from the standard Euler--Maclaurin/Riemann-sum statement.

- **Repair:** TODO.md section 7 / issue #2. P-UCLAB16S-03 should preserve the source statement, refute it, and may record the natural corrected statement separately.

### UCLA Spring 2014 Problem 1(b) is false over the real numbers

- **Object and need:** P-UCLAB14S-01 in SRC-UCLA-BASIC-SPRING-2014. Part (a) asks for a real matrix with minimal polynomial t^4+1; part (b) then asks to prove that its usual real linear map has no nontrivial invariant subspace.

- **Observed evidence:** the retained scan states part (b) literally.
  Over R, t^4+1 factors as (t^2+sqrt(2)t+1)(t^2-sqrt(2)t+1) into coprime nonconstant factors.
  For any operator with minimal polynomial t^4+1, the image of one quadratic factor evaluated at A is a nonzero proper invariant subspace annihilated by the other factor.

- **Impact and owner:** part (b) cannot receive a correct proof as stated.
  A solution should answer part (a), then refute part (b) and exhibit the invariant subspace forced by the factorization.

- **Uncertainty:** none about the mathematical defect; the retained source image was inspected directly and contains the false assertion.

- **Repair:** TODO.md section 7 / issue #2. P-UCLAB14S-01 should preserve the source statement and give the correct counterargument in its solution.

### UCLA Spring 2011 Problem 4 overstates LU existence and uniqueness

- **Object and need:** P-UCLAB11S-04 in SRC-UCLA-BASIC-SPRING-2011. The source asks for a necessary-and-sufficient condition for an LU factorization of an arbitrary real square matrix and then says that normalizing the diagonal of L to 1 makes every existing factorization unique.

- **Observed evidence:** the retained scan states the problem with no nonsingularity or nonzero-pivot hypothesis.
  Literal uniqueness is false: for the zero 2 by 2 matrix, A=L0 for every unit lower-triangular L. Likewise, nonvanishing leading principal minors is sufficient for the usual no-pivot elimination factorization but is not necessary for a bare triangular factorization, for example diag(0,1)=I diag(0,1).

- **Impact and owner:** a correct solution must distinguish the general existence criterion from the stronger nonzero-pivot criterion under which normalized LU is unique; the source's part 2 cannot be proved literally without an additional hypothesis.

- **Uncertainty:** none about the counterexamples.
  The only ambiguity is which standard convention for “LU decomposition” the exam intended.

- **Repair:** TODO.md section 7 / issue #2. P-UCLAB11S-04 should record the literal defect and give the correct general criterion together with the intended nonzero-pivot uniqueness statement.

### Wesleyan 2006 topology A5 is false for finite compact zero-dimensional spaces

- **Object and need:** `P-WESTOP06-A5` in `SRC-WESLEYAN-TOP-2006`. Part 2 asks to prove that every compact Hausdorff zero-dimensional space satisfies \(wX=|\operatorname{clop}(X)|\).

- **Observed evidence:** the current source-checked card states the claim with no infinitude hypothesis.
  If \(X\) is a discrete \(n\)-point space with \(1\le n<\infty\), then \(X\) is compact, Hausdorff, and zero-dimensional, \(wX=n\), while every subset is clopen, so \(|\operatorname{clop}(X)|=2^n\ne n\). In particular, the one-point space already gives \(1\ne2\).

- **Impact and owner:** the literal statement on the card cannot receive a correct proof.
  For infinite compact Hausdorff zero-dimensional \(X\), the intended equality follows because \(\operatorname{clop}(X)\) is a basis, while every clopen subset is a finite union of members of a basis of size \(wX\).

- **Uncertainty:** the mathematical counterexample is exact.
  The retained scan still needs direct inspection to determine whether the original exam included an omitted word such as “infinite” or whether the source itself stated the false finite case.

- **Repair:** issue #2 / TODO.md section 7. Verify the original source wording, repair `P-WESTOP06-A5` source-faithfully, and then resume its ordinary source-review/prove/attach/commit chain.

### Wesleyan 2006 topology A6 has a corrupted vanishing-ideal definition and a false converse

- **Object and need:** `P-WESTOP06-A6` in `SRC-WESLEYAN-TOP-2006`. The retained source defines `I(S)` using `Z(f) \supseteq X` rather than `Z(f) \supseteq S`, then asks for every ideal of `C(X)` on compact `X` to equal `I(S)` for some closed `S`.

- **Observed evidence:** under the literal definition, `I(S)={0}` for every `S`, so the notation does not depend on `S`. Under the evident corrected definition `I(S)={f:Z(f)\supseteq S}`, the converse is still false: for `X=[0,1]`, the principal ideal `(x)` is not `I(S)` for any closed `S`; since `x\in(x)`, necessarily `S\subseteq\{0\}`, but `I(\varnothing)=C(X)` and `\sqrt{x}\in I(\{0\})\setminus(x)`.

- **Impact and owner:** parts 2 and 3 cannot be proved literally as a single correct theorem.
  The solution must distinguish the retained definition from the intended vanishing ideal and refute the false converse while proving the maximal-ideal classification independently.

- **Uncertainty:** none about either mathematical defect in the retained statement.
  The original scan would be needed to determine whether the first defect is transcription/OCR corruption and whether part 3 omitted a qualifier such as closed ideal.

- **Repair:** issue #2 / TODO.md section 7. `P-WESTOP06-A6` now records the literal and intended readings, gives the counterexample to part 3, and proves that the maximal ideals are the point-evaluation kernels.

### January 2005 Problems 8--10 are truncated or absent in the retained topology packet

- **Object and need:** P-MH07-JAN05-08, P-MH07-JAN05-09, and P-MH07-JAN05-10 in SRC-MALONE-HOUSLEY-TOPOLOGY-PRELIM-ANSWERS-2007. These cards require complete source statements before solution authoring.

- **Observed evidence:** the final lines of assets/attachments/extracted/Topology_Prelim_Answers_-_Unknown.md retain Problem 8 only through “Let f:R^n->R be a smooth function.
  Show that for almost every a in R^n the function”, with the function formula and conclusion missing; Problems 9 and 10 appear only as the bare numbers “9.” and “10.” with no statement text.
  The three cards preserve these gaps explicitly.

- **Impact and owner:** TODO.md section 7 cannot complete source-review/prove for these cards without inventing the missing mathematics.
  The source/card owner must recover the original statements before solutions can be authored.

- **Uncertainty:** Problem 8 resembles several standard Sard/transversality perturbation exercises, but the omitted formula determines the actual theorem; Problems 9 and 10 have no recoverable mathematical content at all.
  Reconstruction from topic proximity would be speculative.

- **Repair:** issue #2 / TODO.md section 7. Recover January 2005 Problems 8--10 from an independent source or source images, update the three cards to verified statements, then resume their ordinary read/source-review/prove/attach/commit chains.

### January 2005 Problem 3 is truncated after the induced-map symbol

- **Object and need:** P-MH07-JAN05-03 in SRC-MALONE-HOUSLEY-TOPOLOGY-PRELIM-ANSWERS-2007. The source begins a degree-one-map problem for closed connected oriented manifolds but does not retain the induced map or requested conclusion.

- **Observed evidence:** the retained extraction at the end of assets/attachments/extracted/Topology_Prelim_Answers_-_Unknown.md stops after the phrase beginning the induced map following the degree-one hypothesis; the card records that neither variance nor target nor conclusion is recoverable.
  No independent transcription is present in the repository.

- **Impact and owner:** TODO.md section 7 cannot complete source-review:P-MH07-JAN05-03 or prove:P-MH07-JAN05-03 without inventing missing mathematics.
  The source/card owner must recover the original statement before solution authoring can proceed.

- **Uncertainty:** several standard degree-one-map consequences exist, including surjectivity on fundamental groups and injectivity/surjectivity statements on homology or cohomology, so reconstructing the intended result from context would be speculative.

- **Repair:** issue #2 / TODO.md section 7. Recover January 2005 Problem 3 from an independent source or source image, update P-MH07-JAN05-03 with the verified statement, then resume the ordinary read/source-review/prove/attach/commit chain.

### January 2006 Problem 9 is truncated before the theorem statement

- **Object and need:** P-MH07-JAN06-09 in SRC-MALONE-HOUSLEY-TOPOLOGY-PRELIM-ANSWERS-2007. The card is supposed to ask for a proof of a specific piece of the covering-space classification theorem.

- **Observed evidence:** lines 2534--2557 of assets/attachments/extracted/Topology_Prelim_Answers_-_Unknown.md define isomorphism of covering spaces, state the ambient local hypotheses, then begin “Prove the following piece of the classification theorem for covering spaces: Let x in X” before the extraction jumps to a distinct August 2005 block.
  The remainder of the mathematical statement is absent.

- **Impact and owner:** TODO.md section 7 cannot soundly complete source-review:P-MH07-JAN06-09 or prove:P-MH07-JAN06-09 because the theorem hypotheses and conclusion are not recoverable from the retained source.
  The source/card owner must recover the missing statement before a solution can be authored.

- **Uncertainty:** the standard covering-space classification theorem has several nearby formulations, so reconstructing the intended one from textbook knowledge would be speculation.
  The retained extraction also says “semilocally path-connected,” which may itself be an OCR corruption of “semilocally simply connected.”

- **Repair:** issue #2 / TODO.md section 7. Recover the missing January 2006 Problem 9 source statement from an independent source or source image, update P-MH07-JAN06-09 to the verified statement, then resume the ordinary read/source-review/prove/attach/commit chain.

### Kent State Ring Theory Problem 140 omits that A is proper

- **Object and need:** P-KSRING17-140 in SRC-KENT-STATE-RING-THEORY-QUAL-2017. The source claims every nonzero ideal A contains a product of prime ideals, each containing A.

- **Observed evidence:** line 537 of assets/attachments/extracted/Ring_Theory_Qual_Problems.md contains the literal statement.
  For A=R this is impossible under the ordinary nonempty-product convention, because no prime ideal contains R.

- **Impact and owner:** the intended statement is for nonzero proper ideals A. Under that correction the standard Noetherian maximal-counterexample proof works.

- **Uncertainty:** if the source intended the empty product to be R, the unit-ideal edge case becomes vacuous, but that convention is not stated.

- **Repair:** Author solutions in TODO.md section 7, issue #2. P-KSRING17-140 records the missing properness hypothesis and proves the corrected theorem.

### Kent State Ring Theory Problem 136 omits the non-field/proper-ideal qualification

- **Object and need:** P-KSRING17-136 in SRC-KENT-STATE-RING-THEORY-QUAL-2017. The source claims every nonzero ideal of a commutative Noetherian domain contains a product of nonzero prime ideals.

- **Observed evidence:** line 529 of assets/attachments/extracted/Ring_Theory_Qual_Problems.md contains the literal statement.
  Under the usual convention that such a product has at least one prime factor, the statement fails when R is a field: the only nonzero ideal is R and there are no nonzero prime ideals.

- **Impact and owner:** the intended statement is correct for a Noetherian domain that is not a field; equivalently, the substantive proper-ideal case is correct, with the ambient ring handled separately when a nonzero prime exists.

- **Uncertainty:** if the source intended the empty product to count as the unit ideal, the literal field case becomes vacuous, but that convention is not stated.

- **Repair:** Author solutions in TODO.md section 7, issue #2. P-KSRING17-136 records the qualification and proves the intended non-field statement.

### Kent State Ring Theory Problem 103 omits the hypothesis p divides a_0

- **Object and need:** P-KSRING17-103 in SRC-KENT-STATE-RING-THEORY-QUAL-2017. The source states a generalized Eisenstein criterion with p dividing a_i only for i=1,...,k-1, together with p^2 not dividing a_0.

- **Observed evidence:** line 431 of assets/attachments/extracted/Ring_Theory_Qual_Problems.md contains the literal statement.
  As written it is false: for k=2, p=2, f(x)=x^2-1 satisfies 2|a_1, 2 does not divide a_2, and 4 does not divide a_0=-1, but f factors into two linear factors.

- **Impact and owner:** the intended criterion needs p|a_0 as well, so that p divides a_0,...,a_{k-1} and p^2 does not divide a_0.

- **Uncertainty:** none about the counterexample; the corrected statement is the standard generalized Eisenstein argument.

- **Repair:** Author solutions in TODO.md section 7, issue #2. P-KSRING17-103 records the missing hypothesis and proves the corrected theorem.

### Kent State Ring Theory Problem 95 uses the stronger Euclidean-function convention

- **Object and need:** P-KSRING17-095 in SRC-KENT-STATE-RING-THEORY-QUAL-2017. The source asks for the classification of Euclidean domains whose Euclidean function satisfies an ultrametric inequality.

- **Observed evidence:** line 409 of assets/attachments/extracted/Ring_Theory_Qual_Problems.md states the problem only by saying that \(\varphi\) is a Euclidean function.
  The repository's current definition card D-NKRGN uses only division with remainder, whereas the standard proof of this classification uses the additional monotonicity axiom \(\varphi(a)\le \varphi(ab)\) for nonzero \(a,b\).

- **Impact and owner:** the problem is correct under the stronger classical Euclidean-function convention used by many algebra texts; with the repository's weaker convention, the supplied data do not justify the needed unit/minimal-value argument.

- **Uncertainty:** the retained problem source does not restate its local definition of Euclidean function, so the intended convention must be inferred from the theorem being asked.

- **Repair:** Author solutions in TODO.md section 7, issue #2. P-KSRING17-095 records the convention explicitly and proves the theorem under that intended convention.

### Kent State Ring Theory Problem 78 omits that the principal product is nonzero

- **Object and need:** P-KSRING17-078 in SRC-KENT-STATE-RING-THEORY-QUAL-2017. The source states that if IJ is principal in a domain, then I and J are finitely generated.

- **Observed evidence:** lines 341--343 of assets/attachments/extracted/Ring_Theory_Qual_Problems.md contain no nonzero hypothesis.
  If J=(0), then IJ=(0) is principal while I may be any non-finitely-generated ideal of a non-Noetherian domain.

- **Impact and owner:** the intended statement requires IJ=(a) with a != 0, equivalently (in a domain) both I and J nonzero.

- **Uncertainty:** none about the literal counterexample; the supplied hint explicitly relies on cancellation by the generator a.

- **Repair:** Author solutions in TODO.md section 7, issue #2. P-KSRING17-078 records the correction and proves the intended nonzero-product statement.

### Kent State Ring Theory Problem 58 says every ideal is prime, including the improper ideal

- **Object and need:** P-KSRING17-058 in SRC-KENT-STATE-RING-THEORY-QUAL-2017. The source states that every ideal of R is prime.

- **Observed evidence:** line 259 of assets/attachments/extracted/Ring_Theory_Qual_Problems.md contains the literal wording.
  Under the standard definition used throughout the repository, a prime ideal is proper, so the whole-ring ideal R cannot be prime.

- **Impact and owner:** the intended statement must be that every proper ideal is prime.

- **Uncertainty:** none about the literal inconsistency; the supplied hint with (a) and (a^2) matches the corrected statement.

- **Repair:** Author solutions in TODO.md section 7, issue #2. P-KSRING17-058 records the correction and proves the intended statement.

### Kent State Ring Theory Problem 21 omits j != i from the intersection

- **Object and need:** P-KSRING17-021 in SRC-KENT-STATE-RING-THEORY-QUAL-2017. The source asks to show $I_i+\bigcap I_j=R$ for pairwise comaximal ideals.

- **Observed evidence:** line 121 of assets/attachments/extracted/Ring_Theory_Qual_Problems.md prints the intersection without excluding $I_i$.
  Taken literally, $\bigcap_j I_j\subseteq I_i$, so the left side equals $I_i$ and need not be all of $R$.

- **Impact and owner:** the intended statement must be $I_i+\bigcap_{j\ne i}I_j=R$.

- **Uncertainty:** none about the literal statement being false; the intended pairwise-comaximal lemma is standard and is the only nearby statement consistent with the exercise.

- **Repair:** Author solutions in TODO.md section 7, issue #2. P-KSRING17-021 records the correction and proves the intended statement.

### Kent State Ring Theory Problem 9 omits that p is odd in Euler's criterion

- **Object and need:** P-KSRING17-009 in SRC-KENT-STATE-RING-THEORY-QUAL-2017. The source states Euler's criterion for a prime p without saying p is odd.

- **Observed evidence:** line 87 of assets/attachments/extracted/Ring_Theory_Qual_Problems.md states the exponent (p-1)/2 and the Legendre symbol (a/p) for an arbitrary prime p. Under the standard definition, the Legendre symbol has odd prime denominator, and for p=2 the displayed exponent is not an integer.

- **Impact and owner:** the intended statement requires p to be an odd prime.

- **Uncertainty:** none under the standard Legendre-symbol convention used by the statement.

- **Repair:** Author solutions in TODO.md section 7, issue #2. P-KSRING17-009 records the intended odd-prime hypothesis and proves Euler's criterion under it.

### Fall 2016 Question 8 omits the parameter domain for xi

- **Object and need:** P-TIE-F16-08 in SRC-UGA-CA-COMPILATION. The source asks to compute the Fourier-type integral with parameter xi but does not state whether xi is real or complex.

- **Observed evidence:** line 749 of assets/attachments/extracted/Questions_from_Tie.md contains the integral with xi but no parameter range.
  For complex xi, absolute convergence holds only in the strip |Im xi|<1/2; outside that strip the integral generally diverges.

- **Impact and owner:** the Fourier-transform reading is xi in R. A mathematically complete statement must either specify xi real or state the larger convergence strip.

- **Uncertainty:** the course context strongly suggests real Fourier frequency, but the local printed source is silent.

- **Repair:** Author solutions in TODO.md section 7, issue #2. P-TIE-F16-08 records the ambiguity and proves the stronger formula for |Im xi|<1/2, including the real case.

### Fall 2016 Question 3(c) does not specify a logarithm determination

- **Object and need:** P-TIE-F16-03 in SRC-UGA-CA-COMPILATION. Part (c) asks for an upper bound on the contour integral of log(z)/z^2 around the full circle |z|=R.

- **Observed evidence:** lines 695--707 of assets/attachments/extracted/Questions_from_Tie.md contain no branch or parametrized determination of log.
  No single-valued holomorphic logarithm exists on a neighborhood of a full circle winding once around 0.

- **Impact and owner:** the printed contour integral is ambiguous as a line integral of a single-valued function on the contour.
  A branch/determination must be specified before applying the ML estimate.

- **Uncertainty:** none about the branch obstruction; the intended classroom convention is not stated in the retained source.

- **Repair:** Author solutions in TODO.md section 7, issue #2. P-TIE-F16-03 records the ambiguity and proves the requested estimate for the standard continuous determination log R + it along z=Re^{it}, 0<=t<=2pi.

### Spring 2015 Question 24(b) is undefined at alpha equals zero

- **Object and need:** P-TIE-S15-24 in SRC-UGA-CA-COMPILATION. The source assumes $|\alpha|<1$ but writes the right-hand side of part (b) with a factor $|\alpha|^{-2}$.

- **Observed evidence:** lines 615--623 of assets/attachments/extracted/Questions_from_Tie.md include $\alpha=0$ in the hypothesis, while the printed expression is undefined there.
  For $\alpha=0$, one has $\psi_0(z)=-z$, so the normalized integral is $1$.

- **Impact and owner:** part (b) needs either the hypothesis $0<|\alpha|<1$ or the instruction to interpret the formula continuously at $\alpha=0$; the limit is $1$.

- **Uncertainty:** none about the source text or the missing edge case.

- **Repair:** Author solutions in TODO.md section 7, issue #2. P-TIE-S15-24 records the erratum and proves both the nonzero formula and its continuous value at zero.

### Fall 2015 Question 16 and Spring 2015 Question 19 omit the disk self-map hypothesis

- **Object and need:** P-TIE-F15-16 and P-TIE-S15-19 in SRC-UGA-CA-COMPILATION. Both source appearances define iterates $f^{n+1}=f\circ f^n$ on the unit disk and ask for compact-uniform convergence of $\sum f^n$, but state only that $f$ is analytic on $\DD$, fixes $0$, and is not a rotation.

- **Observed evidence:** lines 481 and 595 of assets/attachments/extracted/Questions_from_Tie.md contain no hypothesis $f(\DD)\subseteq\DD$.
  Without it the iterates need not be defined on all of $\DD$; for example $f(z)=2z$ is analytic, fixes $0$, is not a rotation, and sends many disk points outside the domain after one iterate.

- **Impact and owner:** the printed statements are incomplete.
  The standard Schwarz-lemma proof requires $f:\DD\to\DD$.

- **Uncertainty:** none about the local source text or the necessity of a composability hypothesis.

- **Repair:** Author solutions in TODO.md section 7, issue #2. The owning cards retain the printed statements and solve the intended self-map version explicitly.

### Spring 2015 Question 16 omits the condition that the curve bounds a region inside the domain

- **Object and need:** `P-TIE-S15-16` / `SRC-UGA-CA-COMPILATION`, Spring 2015, Question 16. The source claims that if a nonconstant analytic function on a region \(\Omega\) maps a simple closed curve \(\gamma\subset\Omega\) into \(\mathbb R\), then the function must be constant.

- **Observed evidence:** lines 587--588 of `assets/attachments/extracted/Questions_from_Tie.md` contain no hypothesis that the Jordan interior of \(\gamma\) lies in \(\Omega\). On \(\Omega=\{1/2<|z|<2\}\), the function \(f(z)=z+z^{-1}\) is holomorphic and nonconstant, while on the unit circle \(\gamma\) one has \(f(e^{i\theta})=2\cos\theta\in\mathbb R\).

- **Impact and owner:** the printed theorem is false.
  The standard maximum principle proof is valid once the closed Jordan interior is contained in \(\Omega\).

- **Uncertainty:** none about the counterexample or the printed local source.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), issue #2. `P-TIE-S15-16` retains the source statement, records the missing hypothesis, gives the annulus counterexample, and proves the corrected theorem.

### Spring 2015 Question 5 claims a strict bound that fails for the zero polynomial

- **Object and need:** `P-TIE-S15-05` / `SRC-UGA-CA-COMPILATION`, Spring 2015, Question 5. Part (1) defines $M_R=\sup_{\abs z=R}\abs{z^mp(z)-1}$ and asks to prove $M_R>1$ for every polynomial $p$.

- **Observed evidence:** lines 515--520 of `assets/attachments/extracted/Questions_from_Tie.md` contain the strict inequality with no hypothesis $p\ne0$.
  Taking $p=0$ gives $M_R=\sup_{\abs z=R}\abs{-1}=1$.
  The correct universal assertion is $M_R\ge1$; by the maximum modulus principle equality can occur only for $p=0$, so $M_R>1$ is correct for nonzero polynomials.

- **Impact and owner:** the literal part (1) is false.
  Part (2) remains valid for every polynomial because the weaker bound $M_R\ge1$ already gives $\sup_K\abs{p(z)-z^{-m}}\ge R^{-m}$.

- **Uncertainty:** none about the printed source or counterexample.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), issue #2. `P-TIE-S15-05` retains the printed problem, records the erratum, proves the corrected part (1), and proves part (2) both using part (1) and independently.

### Tate Algebra 250(a), October 22 Problem 1 omits separability from the abelian Galois-group claim

- **Object and need:** `P-TATE85-1022-01` / `SRC-HARVARD-TATE-ALGEBRA-250A-1985`, October 22, 1985, Problem 1. The printed statement says that if $f$ is irreducible and $G_f$ is abelian, then $|G_f|=\deg f$.
  For the usual splitting-field automorphism group this requires $f$ to be separable, unless separability is built into the course notation $G_f$.

- **Observed evidence:** line 5 of `assets/attachments/extracted/Tate_Galois_Theory_Problems.md` contains the statement with no separability or distinct-root hypothesis.
  Over $F=\mathbb F_p(t)$, let $f(X)=X^p-t$.
  If $t=u^p$, then $[\mathbb F_p(u):\mathbb F_p(u^p)]=p$: after clearing denominators, the monomials $1,u,\ldots,u^{p-1}$ are linearly independent over $\mathbb F_p(u^p)$ because their exponents occupy distinct congruence classes modulo $p$.
  Hence $f$ is irreducible of degree $p$.
  But $X^p-t=(X-u)^p$, so the splitting field has only the one root $u$ and every $F$-automorphism fixes it.
  Thus $G_f$ is trivial and $|G_f|=1\ne p=\deg f$.

- **Impact and owner:** a proof of the printed statement over arbitrary fields would be invalid.
  The authored solution must state the intended separability convention, prove the transitive abelian action is regular, and retain the source wording separately from the correction.

- **Uncertainty:** the course may have treated separability as part of the notation $G_f$.
  **Searched:** the retained extraction `assets/attachments/extracted/Tate_Galois_Theory_Problems.md` for occurrences of $G_f$, `separable`, `inseparable`, and `distinct roots`. **Found:** no explicit global definition of $G_f$ in that artifact; October 22 Problem 2(b) explicitly asks for a polynomial "with distinct roots".
  **Conclusion:** the local printed statement omits separability unless an external course convention supplies it.
  **Confidence:** high for the local source text and counterexample; moderate about the undocumented course convention.
  **Gaps:** lecture notes or prior class definitions not present in the retained provenance.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. `P-TATE85-1022-01` keeps the printed problem unchanged, proves the claim under the separable interpretation, and records the inseparable counterexample in a mathematical remark.
  Retain this entry as external source errata/ambiguity; the provenance PDF is unchanged.

### Tate Algebra 250(a), November 5 Problem 7 has the wrong sign in a radical identity

- **Object and need:** `P-TATE85-1105-07` / `SRC-HARVARD-TATE-ALGEBRA-250A-1985`, November 5, 1985, Problem 7. The printed statement identifies $(2+\sqrt2)(3+\sqrt3)$ with $-\sqrt6(1+\sqrt2)(1+\sqrt3)$.

- **Observed evidence:** line 153 of `assets/attachments/extracted/Tate_Galois_Theory_Problems.md` contains the minus sign.
  Direct factorization gives $2+\sqrt2=\sqrt2(1+\sqrt2)$ and $3+\sqrt3=\sqrt3(1+\sqrt3)$, hence $(2+\sqrt2)(3+\sqrt3)=+\sqrt6(1+\sqrt2)(1+\sqrt3)$.
  The same source then defines $\theta=\sqrt{-\alpha}=i\sqrt\alpha$, which is consistent with the positive first expression for $\alpha$.

- **Impact and owner:** the printed intermediate equality is false.
  The authored proof should use the first definition of $\alpha$ and record the corrected positive-sign factorization rather than relying on the false equality.

- **Uncertainty:** none; the sign follows by multiplying the two displayed factorizations exactly.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. `P-TATE85-1105-07` retains the source-faithful problem text, records the sign correction as mathematical errata, and proves the problem from the first definition of $\alpha$.
  Retain this entry as external source errata; the provenance PDF is unchanged.

### Harvard Math 21b Practice Final 5 Problem 3 omits transpose eigenvectors that are forced by the given orthogonal eigenbasis

- **Object and need:** `P-HM21B18-PF5-03` / `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-5`, Problem 3(a). The problem gives $A$ the eigenpairs $2,(1,1)^T$ and $3,(1,-1)^T$ and asks which statements hold for $A^T$, $A^2-A$, and $A^{-1}$.

- **Observed evidence:** page 8 of `assets/attachments/solution5.pdf` checks that
  $2,3$ remain eigenvalues of $A^T$ but leaves unchecked the box saying that
  the two given vectors remain eigenvectors. However the two given eigenvectors
  are orthogonal and form a basis, so after normalization
  \[
  A=Q\operatorname{diag}(2,3)Q^T,
  \]
  which is symmetric. Hence $A^T=A$, and both given vectors are necessarily
  eigenvectors of $A^T$ as well.

- **Impact and owner:** the source answer table is incomplete for the specific matrix determined by the stated data.
  The authored solution must use the actual orthogonal eigenbasis rather than the generic fact that transpose eigenvectors need not coincide.

- **Uncertainty:** none; the two vectors are visibly orthogonal and determine a symmetric diagonalization exactly.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. `P-HM21B18-PF5-03` checks both boxes for $A^T$ and derives every row of the table independently.
  Retain this entry as external source errata; the provenance PDF is unchanged.

### Harvard Math 21b Practice Final 5 Problem 1 gives false spectral justifications for statements 14 and 19

- **Object and need:** P-HM21B18-PF5-01 / SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-5, statements 14 and 19. The source marks statement 14 false and statement 19 true, but its explanations must justify those truth values.

- **Observed evidence:** for statement 14 the source says an orthogonal Jacobian has purely imaginary eigenvalues.
  This is false: $I_2$ is orthogonal and has eigenvalues $1,1$.
  The statement itself is false because the linear system $z'=I_2z$ has an orthogonal Jacobian at its unstable equilibrium.
  For statement 19 the source says an idempotent matrix can have eigenvalues $0,1,-1$.
  If $A^2=A$ and $Av=\lambda v$, then $\lambda^2=\lambda$, so only $0$ and $1$ are possible.
  The multiplicity conclusion is nevertheless true by the pigeonhole principle for four eigenvalues taking only two possible values.

- **Impact and owner:** both source truth values happen to be correct, but the supplied explanations assert false spectral facts.
  The authored solution must replace both arguments rather than reproduce them.

- **Uncertainty:** none; the counterexample $I_2$ and the identity $\lambda^2=\lambda$ settle the two issues exactly.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-HM21B18-PF5-01 uses $z'=I_2z$ for statement 14 and the idempotent eigenvalue equation for statement 19. Retain this entry as external source errata; the provenance PDF is unchanged.

### Harvard Math 21b Practice Final 5 Problem 10 uses the wrong forcing frequency in its particular-solution ansatz

- **Object and need:** P-HM21B18-PF5-10 /
  SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-5, Problem 10(a). The worked
  solution derives a particular solution of
  \[
  f''+f=3\sin(2t)+1.
  \]

- **Observed evidence:** assets/attachments/solution5_extracted.md states that one should try $A\sin t+B$.
  The term $\sin t$ lies in the kernel of $D^2+1$, so such an ansatz cannot produce a $\sin(2t)$ forcing term.
  The source's immediately following final solution instead contains $-\sin(2t)+1$, which comes from the correct trial $A\sin(2t)+B$.

- **Impact and owner:** the displayed final answer is correct, but the stated particular-solution derivation does not yield it.
  The authored proof must use the forcing frequency $2$.

- **Uncertainty:** none; substitution into $f''+f$ determines the frequency and coefficient directly.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-HM21B18-PF5-10 derives $-\sin(2t)+1$ from the correct ansatz and then imposes the initial conditions.
  Retain this entry as external source errata; the provenance PDF is unchanged.

### Harvard Math 21b Practice Final 5 Problem 9 gives the wrong shifted eigenvalues in a determinant remark

- **Object and need:** P-HM21B18-PF5-09 / SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-5, Problem 9(b). The worked solution correctly proves the displayed $6\times6$ matrix is singular, then gives an optional eigenvalue argument using $B=A-5I$.

- **Observed evidence:** assets/attachments/solution5_extracted.md and the
  retained source solution state that $B$ has four zero eigenvalues together
  with $5$ and $-1$, and then shift them in the wrong direction to obtain
  eigenvalues $0,-6,-5,-5,-5,-5$ for $A$. In fact the four-dimensional
  subspace
  \[
  \{(0,x_2,\ldots,x_6):x_2+\cdots+x_6=0\}
  \]
  is the zero eigenspace of $B$, while on the span of
  $e_1$ and $(0,1,1,1,1,1)^T$ the characteristic polynomial is
  $\lambda^2+4\lambda-5=(\lambda-1)(\lambda+5)$. Thus
  \[
  \operatorname{Spec}(B)=\{1,-5,0,0,0,0\},
  \qquad
  \operatorname{Spec}(A)=\{6,0,5,5,5,5\}.
  \]

- **Impact and owner:** the optional spectral explanation is false as written, although its conclusion $\det A=0$ is already correctly established by a column dependence.
  The authored solution should not inherit the erroneous eigenvalue remark.

- **Uncertainty:** none; the two-dimensional restriction and the shift $A=B+5I$ determine the eigenvalues exactly.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-HM21B18-PF5-09 proves singularity directly from the column relation and derives part (c) independently.
  Retain this entry as external source errata; the provenance PDF is unchanged.

### Harvard Math 21b Practice Final 4 Problem 1 omitted statement 20 and gives a false explanation for statement 14

- **Object and need:** `P-HM21B18-PF4-01` / `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-4`, Problem 1. The authored card must contain all twenty true-or-false statements, and its solution must independently verify the source's answers.

- **Observed evidence:** page 5 of `assets/attachments/solution4.pdf` contains
  statement 20, “A $3\times3$ matrix $A$ is invertible if and only if all its
  eigenvalues are positive,” and marks it false; the retained Markdown
  extraction lost the statement while retaining only its solution sentence,
  “They can also be negative.” The card consequently declared statement 20
  unrecovered. On page 4 the source correctly marks statement 14 false but
  explains that the Jacobian eigenvalues are purely imaginary. Direct
  differentiation gives
  \[
  J(0,0)=\begin{pmatrix}1&0\\1&0\end{pmatrix},
  \]
  whose eigenvalues are $1$ and $0$ and whose determinant is zero.

- **Impact and owner:** the card omitted one requested statement, and copying the supplied explanation for statement 14 would give a mathematically false justification.
  The owning solution must restore statement 20 from the source page and prove statement 14 by computing the Jacobian.

- **Uncertainty:** none; both statements and selected truth values are visible in the retained PDF, and the Jacobian calculation is exact.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. `P-HM21B18-PF4-01` restores statement 20 and proves all twenty truth values independently.
  Retain this entry for the external source's erroneous explanation of statement 14; the provenance PDF itself is unchanged.

### Harvard Math 21b Practice Final 4 Problem 4 writes the wrong coefficient matrix

- **Object and need:** `P-HM21B18-PF4-04` / `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-4`, Problem 4. Part (a) asks for the coefficient matrix of the displayed six-variable system.

- **Observed evidence:** page 8 of `assets/attachments/solution4.pdf` prints
  the second equation as
  \[
  y+2z+2u+v=2,
  \]
  so the second row of the coefficient matrix is
  $(0,1,2,2,1,0)$. Page 9 of the worked solution instead displays
  $(1,1,2,2,1,1)$, inserting nonexistent $x$ and $w$ coefficients. Direct row
  reduction of the correct augmented matrix nevertheless gives the same RREF
  printed later in the source.

- **Impact and owner:** copying the supplied matrix would answer part (a) incorrectly even though the later RREF and general solution are valid for the original system.
  The owning solution must transcribe the displayed equations rather than inherit the worked-solution matrix.

- **Uncertainty:** none; the system and the inconsistent matrix are both legible in the retained PDF, and the correct reduction is an exact row calculation.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. `P-HM21B18-PF4-04` uses the correct second row, derives the RREF from it, and recovers the general solution.
  Retain this entry as external source errata; the provenance PDF itself is unchanged.

### Harvard Math 21b Practice Final 4 Problem 7 gives a false eigenvector decomposition

- **Object and need:** `P-HM21B18-PF4-07` / `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-4`, Problem 7. Part (b) asks for the closed form of the two-state discrete system with initial state $(100,0)^T$.

- **Observed evidence:** page 12 of `assets/attachments/solution4.pdf` correctly
  identifies eigenvectors $(8,9)^T$ for eigenvalue $1$ and $(1,-1)^T$ for
  eigenvalue $-0.7$, but then prints
  \[
  \binom{100}{0}=-100\binom89+900\binom1{-1},
  \]
  whose right-hand side is $(100,-1800)^T$. Solving for the coefficients gives
  $100/17$ and $900/17$ instead. The source's resulting closed form therefore
  fails the initial condition, although its final normalized equilibrium
  $(800/17,900/17)^T$ is correct.

- **Impact and owner:** copying the worked decomposition would make part (b) false at $t=0$.
  The owning solution must derive the coefficients from the initial vector before applying the eigenvalue powers.

- **Uncertainty:** none; the false equality is visible in the retained PDF and the corrected coefficients solve a two-by-two linear system exactly.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. `P-HM21B18-PF4-07` uses coefficients $100/17$ and $900/17$, verifies the initial condition, and derives the same limiting equilibrium independently.
  Retain this entry as external source errata; the provenance PDF is unchanged.

### Harvard Math 21b Practice Final 4 Problem 9(c) is not an eight-queens matrix and has determinant zero

- **Object and need:** `P-HM21B18-PF4-09` / `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-4`, Problem 9(c). The source calls its displayed $8\times8$ matrix a solution of the eight-queens puzzle and asks for its determinant.

- **Observed evidence:** page 13 of `assets/attachments/solution4.pdf` visibly places entries $2$ in column $4$ of both rows $1$ and $6$, and has no nonzero entry in column $5$.
  Thus the displayed matrix has a zero fifth column and repeated first and sixth rows, so its determinant is $0$.
  The worked solution on the following page instead treats the matrix as $2$ times a permutation matrix, counts an even permutation, and reports $2^8=256$.

- **Impact and owner:** the source prose, displayed matrix, and worked answer cannot all be correct.
  Solving the literal displayed problem gives determinant $0$; silently replacing it by an unspecified intended queens permutation would change the authored problem.

- **Uncertainty:** none about the retained display or its determinant.
  The intended corrected eight-queens permutation is not established by the source material inspected here.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. `P-HM21B18-PF4-09` restores the source-displayed matrix and computes its determinant literally as $0$.
  Retain this entry as external source errata; the provenance PDF itself is unchanged.

### Harvard Math 21b Practice Final 4 Problem 11 has no exact correct phase-portrait option

- **Object and need:** `P-HM21B18-PF4-11` / `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-4`, Problem 11(c). The problem asks which of four displayed phase portraits A--D belongs to $x'=x-y^3$, $y'=x^3+y$.

- **Observed evidence:** page 16 of `assets/attachments/solution4.pdf` explicitly
  says “None of the phase portrait matches exactly,” while also stating that B
  was counted as correct because it supplies the intended unstable equilibrium.
  Independently, the nullclines meet only at $(0,0)$, the Jacobian there is
  $I_2$, and for every nonzero point
  \[
  \dot\theta=\frac{x^4+y^4}{x^2+y^2}>0.
  \]
  Moreover, with $V=x^2+y^2$, one has
  $\dot V\ge2V-V^2>0$ sufficiently near the origin. Thus the exact local
  portrait has one counterclockwise repelling spiral equilibrium.

- **Impact and owner:** no displayed candidate represents all required local features, so B is only the source's accepted grading choice rather than a mathematically exact answer.

- **Uncertainty:** none about the mismatch; the worked source itself records it, and the local phase calculations are exact.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. `P-HM21B18-PF4-11` derives the phase behavior and records B as the source's accepted choice while stating that no candidate is exact.
  Retain this entry as external source errata; the provenance PDF is unchanged.

### Harvard Math 21b Practice Final 4 Problem 12 substitutes the wrong cosine argument in the Fourier coefficient integral

- **Object and need:** `P-HM21B18-PF4-12` / `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-4`, Problem 12(a). The worked solution computes the cosine coefficients of $|x|-\pi/2$.

- **Observed evidence:** page 17 of `assets/attachments/solution4.pdf` displays
  an integral with $x\cos(n\pi)$ where the Fourier coefficient requires
  $x\cos(nx)$. The immediately following value
  \[
  \frac{2}{\pi n^2}(\cos(n\pi)-1)
  \]
  is the result of integrating $x\cos(nx)$, not $x\cos(n\pi)$.

- **Impact and owner:** the displayed intermediate formula is false as written, although the final coefficient is correct.
  The authored solution must derive the coefficient from the proper Fourier integrand.

- **Uncertainty:** none; the source display and the integration-by-parts calculation are both explicit.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. `P-HM21B18-PF4-12` uses $\cos(nx)$ and derives the source's final coefficient independently.
  Retain this entry as external source errata; the provenance PDF is unchanged.

### Harvard Math 21b Practice Final 4 Problem 13 uses the wrong wave speed and initial-velocity coefficient

- **Object and need:** `P-HM21B18-PF4-13` / `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-4`, Problem 13. The worked solution constructs the homogeneous sine modes for $u_{tt}=9u_{xx}$ and must reproduce the prescribed initial velocity.

- **Observed evidence:** page 18 of `assets/attachments/solution4.pdf` rewrites the homogeneous equation as $u_{tt}=c^2u_{xx}$ and then states $c=9$, even though $c^2=9$ gives $c=3$ and the source's subsequent frequencies $51$, $30$, $3$, and $9$ all use $c=3$.
  The same page assigns the velocity mode $-2\sin(3x)$ the term $-(2/3)\sin(3x)\sin(9t)$.
  Its derivative at $t=0$ is $-6\sin(3x)$, not $-2\sin(3x)$.
  The required coefficient is $-2/9$.

- **Impact and owner:** the printed final solution fails one of the initial conditions, and the stated wave speed contradicts both the PDE and the frequencies actually used.
  The authored solution must derive each temporal frequency and velocity coefficient directly.

- **Uncertainty:** none; $c^2=9$ and differentiation at $t=0$ determine both corrections exactly.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. `P-HM21B18-PF4-13` uses wave speed $3$ and coefficient $-2/9$, and verifies the initial data before superposing the forcing term.
  Retain this entry as external source errata; the provenance PDF is unchanged.

### Harvard Math 21b Practice Final 4 Problem 14 shifts the cyclic eigenvalues by 2 instead of 3 in one sentence

- **Object and need:** `P-HM21B18-PF4-14` / `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-4`, Problem 14. The source writes the displayed $40\times40$ matrix as $L=Q+Q^T+3I_{40}$ for the cyclic shift $Q$ and computes its determinant from the Fourier eigenvalues.

- **Observed evidence:** page 19 of `assets/attachments/solution4.pdf` first states that the eigenvalues of $L$ are $\lambda_k+\lambda_k^{-1}+2$, although the definition of $L$ requires $3+\lambda_k+\lambda_k^{-1}$.
  The very next sentence uses the correct value $2\cos(2\pi k/40)+3$, and the printed final determinant agrees with the correct shift.

- **Impact and owner:** the intermediate eigenvalue formula is inconsistent with both the matrix and the final calculation.
  The authored solution must derive the eigenvalues directly from $L=Q+Q^T+3I_{40}$.

- **Uncertainty:** none; applying $L$ to a Fourier eigenvector of $Q$ gives the eigenvalue $3+\lambda_k+\lambda_k^{-1}$ exactly.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. `P-HM21B18-PF4-14` derives the correct eigenvalues and evaluates the determinant independently.
  Retain this entry as external source errata; the provenance PDF is unchanged.

### Harvard Math 21b Practice Final 3 Problem 13 reverses the heat-mode sign in its prose

- **Object and need:** P-HM21B18-PF3-13 / SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-3, Problem 13(a). The source reduces the modified heat equation to scalar sine-mode equations.

- **Observed evidence:** in assets/attachments/solution3.pdf, the source defines the spatial eigenvalue by \(\lambda_n=1-n^2\), but then says the heat equation reduces to \(a_n'=-\lambda_n a_n\) with factor \(e^{-\lambda_n t}\). Direct substitution gives \(a_n'=(1-n^2)a_n=\lambda_n a_n\). The source's immediately following displayed solution uses \(e^{(1-n^2)t}\), which has the correct sign.

- **Impact and owner:** the prose derivation has the wrong sign even though the final displayed answer is correct.
  The owning solution must derive the mode equation without inheriting the sign error.

- **Uncertainty:** none; substituting \(a_n(t)\sin(nx)\) into \(u_t=u_{xx}+u\) determines the sign exactly.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-HM21B18-PF3-13 derives \(a_n'=(1-n^2)a_n\) directly and records the source-prose error.
  Retain this entry as mathematical errata.

### Harvard Math 21b Practice Final 3 Problem 11 uses an inconclusive linearization at the origin

- **Object and need:** P-HM21B18-PF3-11 / SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-3, Problem 11(c). The source asks for stability analysis of all three nonlinear equilibria.

- **Observed evidence:** page 16 of assets/attachments/solution3.pdf computes
  \[
  J(0,0)=\begin{pmatrix}0&1\\0&0\end{pmatrix}
  \]
  and then states that $(0,0)$ is not stable. Both eigenvalues of this
  Jacobian are zero, so the hyperbolic linearization theorem is inapplicable
  and the displayed calculation does not establish the stated conclusion.

- **Impact and owner:** the source's conclusion is correct, but its argument does not prove the nonlinear stability claim.
  A nonlinear argument is required in the owning authored solution.

- **Uncertainty:** none about the proof gap.
  The invariant region \(0<x<1,\ x^2<y<x\) contains arbitrarily small initial data and its trajectories converge to $(1,1)$, proving instability of the origin.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-HM21B18-PF3-11 supplies the invariant-region proof and retains the source portrait choice A. Retain this entry as mathematical errata.

### Harvard Math 21b Practice Final 3 Problem 7 repeats the wrong eigenvector in the initial-value decomposition

- **Object and need:** `P-HM21B18-PF3-07` / `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-3`, Problem 7(c). The source solution decomposes $(3,0,0,0)^T$ into eigenvectors before solving the continuous and discrete systems.

- **Observed evidence:** page 13 of `assets/attachments/solution3.pdf` displays `(3,0,0,0)^T=(-3/4)(-3,1,1,1)^T+(3/4)(-3,1,1,1)^T`, whose right-hand side is zero.
  The immediately following formulas instead use $(1,1,1,1)^T$ in the second summand.
  Direct calculation gives `A(1,1,1,1)^T=0` and `(3,0,0,0)^T=(-3/4)(-3,1,1,1)^T+(3/4)(1,1,1,1)^T`.

- **Impact and owner:** the displayed decomposition in the source solution is false, although its subsequent formulas reveal the intended correction.
  The owning authored solution must use the $0$-eigenvector in the second summand.

- **Uncertainty:** none; the typo is visible in the retained PDF itself and the corrected equality is exact.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. `P-HM21B18-PF3-07` uses the correct decomposition and records the source typo as mathematical errata.
  Retain this entry as source errata.

### Harvard Math 21b Practice Final 3 Problem 1 has three defective worked answers and one card transcription reversal

- **Object and need:** `P-HM21B18-PF3-01` / `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-3`, Problem 1. The authored statement must match the retained exam, and the solution must independently adjudicate the source's twenty true-or-false answers.

- **Observed evidence:** `assets/attachments/solution3.pdf`, Problem 1, statement 18 says that the resonant initial-value problem has solutions for which `|x(t)|` becomes arbitrarily large, while the card had reversed this to the assertion that every solution is bounded.
  In `assets/attachments/solution3_extracted.md`, lines 31--35 answer statement 2 by discussing the fact that the zero vector is not an eigenvector rather than proving it lies in every kernel; lines 131--133 mark `e^{-6t}sin(3x)` as a solution of `f_t=2f_{xx}`, although `f_t=-6f` and `2f_{xx}=-18f`; and lines 149--153 declare the nonlinear equilibrium unstable merely because the linearization has zero eigenvalues, which is an inconclusive linearization test.

- **Impact and owner:** the card's statement 18 changed the source truth value, and copying the source worked answers would give a false answer to statement 12 and an invalid justification for statement 14. The owning card must restore the source statement and supply independent arguments.

- **Uncertainty:** none about these four defects.
  Statement 18 was checked directly in the retained PDF text layer, and the derivative and explicit nonlinear-flow calculations are exact.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. `P-HM21B18-PF3-01` restores statement 18, proves all twenty truth values independently, and records the source-solution defects as mathematical errata.
  Retain this entry as source errata; the provenance PDF itself is not rewritten.

### GRE Practice Test Question 41 treats a smooth function as its Taylor series

- **Object and need:** `P-GREPT-41` / `SRC-GRE-MATH-PRACTICE-TEST`, Question 41. The problem assumes only that $f$ has derivatives of every order on $\mathbb R$ and bounds the derivatives at $0$, then asks for a universal upper bound on $f(1)$.

- **Observed evidence:** the retained source solution at lines 17828--17842 immediately writes $f(x)=\sum_{n\ge0}f^{(n)}(0)x^n/n!$.
  Smoothness does not imply equality with the Taylor series.
  Let $h(0)=0$ and $h(x)=e^{-1/x^2}$ for $x\ne0$; $h$ is smooth and all of its derivatives at $0$ vanish.
  Then $f_M(x)=x+x^2+Mh(x)$ satisfies all three printed derivative conditions for every $M>0$, but $f_M(1)=2+M/e$ is unbounded above.

- **Impact and owner:** no finite number $m$ has the stated property, so none of choices (A)--(E) is correct.
  The source's value $4$ would follow from an additional hypothesis ensuring that the Taylor expansion at $0$ represents $f$ at $x=1$ together with the displayed coefficient bounds.

- **Uncertainty:** none about the smooth counterexample.
  The intended analytic or Taylor-representability hypothesis is not present in the retained statement.

- **Repair:** `P-GREPT-41` proves that the literal values of $f(1)$ are unbounded above and records choice (C) only as the source-intended answer under the missing Taylor-representability hypothesis.
  Retain this entry as source errata.

### GRE Practice Test Question 38 has an impossible condition and an ill-typed composite

- **Object and need:** `P-GREPT-38` / `SRC-GRE-MATH-PRACTICE-TEST`, Question 38. The problem asks which listed conditions would ensure that a function $f:[a,b]\to\mathbb R$, with $a<b$, is constant.

- **Observed evidence:** condition I says that the inverse of $f$ is constant.
  If an inverse function exists, then $f^{-1}(f(a))=a$ and $f^{-1}(f(b))=b$, so condition I is impossible.
  Read as a formal sufficient condition, it therefore implies constancy vacuously, whereas the source solution at lines 17806--17808 discards I because it cannot occur.
  Condition II quantifies over every real-valued $g$ on $[a,b]$, but $f\circ g$ is not defined when $g([a,b])\nsubseteq[a,b]$; the source implicitly reads the quantifier as ranging over composable self-maps.
  Condition III is valid and does force constancy.

- **Impact and owner:** the multiple-choice alternatives do not encode a single literal mathematical reading.
  Under formal implication I is vacuously sufficient, while II is not well-typed as quantified.
  The source's answer (D) requires the conventions that impossible I is not counted and that II ranges over composable maps.

- **Uncertainty:** none about the two formal defects.
  The intended answer is unambiguous from the retained source explanation.

- **Repair:** `P-GREPT-38` records the literal defects, proves the substantive sufficiency of II and III, and records (D) as the source-intended answer rather than as a consequence of the statement literally parsed.
  Retain this entry as source errata.

### GRE Practice Test Question 24 does not state independence of the two throws

- **Object and need:** `P-GREPT-24` / `SRC-GRE-MATH-PRACTICE-TEST`, Question 24. The problem specifies the one-throw probabilities of the six faces and asks for the probability of rolling a $5$ followed by a $6$ in two throws.

- **Observed evidence:** the retained source solution at `assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md`, lines 17636--17640, derives $P(5)=1/9$ and $P(6)=2/9$ and multiplies them, without the printed problem having stated that the two throws are independent.
  Independence gives $P(5,6)=2/81$, whereas the coupling in which the second outcome always equals the first has the same prescribed marginal distribution on each throw and gives $P(5,6)=0$.

- **Impact and owner:** the one-throw distribution does not determine the requested joint probability.
  Literally, choice (E) is correct; choice (A) requires the additional independent-throws hypothesis.

- **Uncertainty:** ordinary elementary-probability convention often treats repeated die throws as independent, and the source solution plainly uses that convention.
  The printed statement itself does not include it, despite offering “Cannot be determined” as a choice.

- **Repair:** `P-GREPT-24` proves the literal underdetermination and records that the source's answer (A) follows under the intended independence assumption.
  Retain this entry as source errata.

### GRE Practice Test Question 14 excludes valid nonzero constant solutions

- **Object and need:** `P-GREPT-14` / `SRC-GRE-MATH-PRACTICE-TEST`, Question 14. The printed problem asks for the family of all nonzero solutions of $y''=(y')^2$.

- **Observed evidence:** the retained source solution at `assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md`, lines 17554--17560, sets $u=y'$, solves $u'=u^2$, explicitly says “We ignore the solution $u\equiv0$,” and selects $y=c_2-\log(c_1+x)$.
  But $u\equiv0$ gives every constant solution $y\equiv C$, and every choice $C\ne0$ is a nonzero solution of the printed differential equation.
  None of the five listed families contains these constant solutions.
  Moreover, the full real nonconstant family on an interval is $y=C_2-\log|x+C_1|$, with the interval avoiding the pole.

- **Impact and owner:** literally, no listed choice is the family of all nonzero solutions.
  The owning card must classify the literal solutions and distinguish the source's intended nonconstant branch from the stated problem.

- **Uncertainty:** the source explanation makes the intended reinterpretation clear: “nonzero” is being applied to $u=y'$ rather than to $y$.
  The printed problem itself does not say “nonconstant” or require $y'\ne0$.

- **Repair:** `P-GREPT-14` records the complete literal solution family and notes that choice (E) is obtained only after replacing the printed request by the intended nonconstant-solution request and taking a domain where $x+C_1>0$.
  Retain this entry as source errata.

### GRE Practice Test Question 4 omits conditions on $a$

- **Object and need:** `P-GREPT-04` / `SRC-GRE-MATH-PRACTICE-TEST`, Question 4. The printed statement sets $A=\{\varnothing,a\}$ and $B=\mathcal P(A)$, then asks for the cardinality of $A\cup B$ without specifying what set-theoretic object $a$ is.

- **Observed evidence:** the retained book extraction at `assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md` prints the statement at lines 16485--16495 and gives answer (B) at lines 17470--17474. If $a=\{\varnothing\}$, then $A=\{\varnothing,\{\varnothing\}\}$ and both elements of $A$ already lie in $\mathcal P(A)$, so $|A\cup\mathcal P(A)|=4$.
  If instead $a=\{\{\varnothing\}\}$, then $a\notin\mathcal P(A)$ and the union has cardinality $5$.

- **Impact and owner:** the literal statement does not determine a unique multiple-choice answer.
  The owning solution must record the ambiguity rather than present the source's answer (B) as forced by the printed hypotheses.

- **Uncertainty:** the source solution evidently treats $a$ as an atom or at least assumes $a\notin\mathcal P(A)$, but the retained statement contains no such convention or hypothesis.

- **Repair:** `P-GREPT-04` exhibits the two admissible choices of $a$, concludes that the printed problem is underdetermined, and records that the source's answer (B) follows after adding $a\notin\mathcal P(A)$.
  Retain this entry as source errata; the provenance source itself is not rewritten.

### Berkeley Spring 2000 Problem 14 permits degenerate intervals

- **Object and need:** `P-BKS00-14` / `SRC-BERKELEY-PRELIM-SPRING-2000`, Problem 14. The printed statement assumes only that the intervals $I_1,\ldots,I_n$ are disjoint, closed, and nonempty, then asserts that vanishing of all $n$ integrals forces every polynomial of degree below $n$ to vanish.

- **Observed evidence:** pages 2--3 of `assets/attachments/Spring00.pdf` print exactly “disjoint closed nonempty subintervals of R” and supply no positive-length condition.
  If degenerate intervals are allowed, take $n=1$, $I_1=\{0\}$ and $p=1$.
  Then $\deg p=0<1$ and $\int_{I_1}p(x)\,dx=0$, but $p\ne0$.

- **Impact and owner:** part 1 is false literally under the convention that singleton sets are intervals.
  The standard zero-counting proof of part 1 requires every $I_j$ to have positive length.
  Part 2 remains true under the literal source hypotheses: the owning card separates the nondegenerate intervals, proves their lower-degree moment map is an isomorphism, and adjusts $x^n$ by a lower-degree polynomial.
  The card records the part-1 counterexample as mathematical errata.

- **Uncertainty:** the defect is exact under the usual inclusive definition of a closed interval.
  The Berkeley exam may have intended “subinterval” to mean a nondegenerate interval, but the retained paper does not state that convention.

- **Repair:** retain the printed statement for source fidelity, together with the owning card's erratum, corrected positive-length formulation of part 1, and literal proof of part 2, unless an authoritative Berkeley correction or explicit convention establishes that singleton intervals were excluded.

### Berkeley Fall 1983 Problem 15 omits connectedness of the ambient open set

- **Object and need:** `P-BKF83-15` / `SRC-BERKELEY-PRELIM-FALL-1983`, Problem 15(1). The source assumes only that $f$ is analytic on an open set containing the closed unit disk and asks to prove that $f$ is constant.

- **Observed evidence:** line 117 of `assets/attachments/extracted/Fall83.md` gives exactly that hypothesis.
  If $U=\{\lvert z\rvert<2\}\cup\{\lvert z-4\rvert<1/2\}$, the function equal to $0$ on the first component and $1$ on the second is holomorphic on $U$, real-valued on the unit circle, and not constant on $U$.

- **Impact and owner:** the usual harmonic-maximum/open-mapping argument proves that $f$ is constant on the unit disk, and the identity theorem extends that constant only across the connected component containing the disk.
  The owning solution must not silently apply the identity theorem to disconnected components.

- **Uncertainty:** the mathematical gap is exact.
  The source may be using "open set" informally for a connected region, but the retained source does not state connectedness.

- **Repair:** `P-BKF83-15` now proves constancy on the connected component containing the closed unit disk and records the literal disconnected-domain counterexample as mathematical errata.
  Retain this source-intent note unless an authoritative Berkeley correction establishes that "open set" was intended to mean a connected domain.

### UCSD Spring 2019 square-root solution argues circularly off the zero set

- **Object and need:** P-CASP19B claims to prove that a continuous function f is analytic when its square is analytic.
  The proof must establish analyticity of f on the nonzero set before removable singularities can be used at the zeros.

- **Observed evidence:** lines 32--34 of corpus/collections/SRC-UCSD-CA-SPRING-2019/P-CASP19B.md say that f=f^2/f is a quotient of analytic functions and justify this by 1/f=f/f^2. Both statements already require analyticity of f, which is the conclusion being proved.
  At a point z_0 with f(z_0) nonzero, the noncircular argument instead factors the difference of squares in the difference quotient, so its limit is (f^2)'(z_0)/(2f(z_0)).

- **Impact and owner:** the current solution does not prove analyticity away from the zero set, so its later removable-singularity step has no established punctured-neighborhood analyticity to extend.
  The owning card P-CASP19B needs a proof repair; no statement change is required.

- **Uncertainty:** the circularity is exact in the current authored solution.
  The statement itself is true.
  The sibling Berkeley card P-BKF84-19 is being solved independently and does not rely on this proof.

- **Repair:** replace the circular quotient step on P-CASP19B with the difference-quotient argument, then use isolated zeros of the analytic function f^2 and continuity of f to apply the removable singularity theorem.

### Berkeley Spring 1997 Problem 18 does not specify whether the direct product is finite

- **Object and need:** `P-BERK97S-18` / `SRC-BERKELEY-PRELIM-SPRING-1997`, Problem 18(2). The source asks whether an extension splits when the quotient is "a direct product of infinite cyclic groups" but does not say whether the product has finitely many factors.

- **Observed evidence:** the retained Spring 1997 extraction prints exactly that wording.
  For a finite product, the quotient is `\ZZ^r` and a basis can be lifted to split the quotient map.
  For an arbitrary infinite product the claim is false in general: the Baer--Specker group `\prod_{n\geq1}\ZZ` is not free, so a free presentation of it cannot split as the quotient times its kernel.

- **Impact and owner:** a proof that lifts the coordinate generators silently assumes the finite-product (equivalently here, finite-rank free-abelian) reading.
  The owning card must distinguish that case from a literal arbitrary infinite product.

- **Uncertainty:** the source's intended convention is unknown.
  **Searched:** current `assets/`, `sources/`, and Git history for `Spring97`, Spring 1997 solution variants, and the exact statement.
  **Found:** the exam PDF and its extraction, but no solution packet or prior authoritative solution.
  **Conclusion:** no authoritative retained solution resolving the convention was found.
  **Confidence:** high for the current repository.
  **Gaps:** external Berkeley archives were not searched.

- **Repair:** `P-BERK97S-18` now proves the finite-product reading and records the arbitrary-infinite-product counterexample.
  Keep this source-intent note until an authoritative Berkeley solution or convention resolves the wording.

### Azoff Möbius symmetry problem has a false fourth equivalent condition

- **Object and need:** \`P-AZOFF-C12\` / \`SRC-AZOFF-PROBLEMS-BY-TOPIC\`, Conformal mapping Problem 12. The source asks to prove four conditions on a Möbius transformation equivalent; condition (d) requires a real fixed point \(\alpha\) in addition to one nonreal conjugation-compatible point.

- **Observed evidence:** page 3 of the retained PDF prints \(T(\alpha)=\alpha\) with no overbar on either occurrence of \(\alpha\). The PDF vector data separately shows the overbars in \(T(\overline\beta)=\overline{T\beta}\), so the fixed-point clause is not an extraction loss.
  The Möbius transformation \(T(z)=-1/z\) has real coefficients and therefore satisfies (a)--(c), but its fixed-point equation is \(z^2=-1\), so it has no real fixed point and fails (d).

- **Impact and owner:** the printed four-way equivalence cannot be proved.
  The owning problem card must state the true implication pattern before its solution is authored.

- **Uncertainty:** verified against the rendered PDF, its text layer, and the vector rules carrying the overbars.
  The mathematical counterexample is exact; whether the source author intended a different condition (d) is unknown.

- **Repair:** correct \`P-AZOFF-C12\` to ask for the equivalence of (a)--(c), prove that printed (d) implies them, and record that the converse fails via \(T(z)=-1/z\). Preserve the printed source error as a durable erratum on the card.

### Zaidenberg Definition 4.3 makes the following finite-morphism exercises inconsistent

- **Object and need:** \`SRC-AGX-VARIETIES-PROBLEMS\`, Definition 4.3 and Exercises 4.4. The standard definition of a finite morphism does not require the comorphism to be injective.

- **Observed evidence:** page 6 of the recorded PDF says that a finite morphism has an "embedding" $f^*:O(Y)\to O(X)$, while the same exercise immediately asks for a non-surjective finite morphism.
  An injective module-finite comorphism is integral, so lying over makes the corresponding affine map surjective.

- **Impact and owner:** the source wording cannot govern cards about finite morphisms.
  \`P-AGXVARFINCLOSED\` records and uses the repository definition \`D-MORFIN\`, under which the exercise is coherent.

- **Uncertainty:** verified in the PDF with two independent text extractors; this may be a typo in the source rather than an intended nonstandard convention.

- **Repair:** retain the standard repository definition and treat the printed word "embedding" as source errata unless a corrected source edition is found.

### Berkeley Fall 2006 Problem 6A solution packet uses irreducibility circularly

- **Object and need:** `P-BKF06-6A` / `SRC-BERKELEY-PRELIM-FALL-2006`, Problem 6A. The retained solution packet proves that $x^p-x+1$ is irreducible over $\FF_p$ by analyzing subsets of its translated roots.

- **Observed evidence:** `assets/attachments/extracted/f06solution.md` says that $(\#I)\alpha\in\FF_p$ and then states “Since f is irreducible, $\alpha\notin\FF_p$,” using the desired conclusion to justify the key contradiction.
  The needed independent fact is immediate instead: $f(a)=a^p-a+1=1$ for every $a\in\FF_p$, so no root of $f$ lies in $\FF_p$.

- **Impact and owner:** the source solution has a circular proof at the decisive factor-exclusion step.
  The owning authored card must not inherit that circularity.

- **Uncertainty:** the circular sentence is present in the retained solution extraction, and the replacement argument is exact.
  No claim is made that a different edition of the source packet contains the same sentence.

- **Repair:** `P-BKF06-6A` now proves $\alpha\notin\FF_p$ directly from $f(a)=1$ before applying the root-sum argument.
  Retain this entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2006 Problem 8A solution packet gives the wrong cokernel torsion

- **Object and need:** `P-BKF06-8A` / `SRC-BERKELEY-PRELIM-FALL-2006`, Problem 8A. The source asks for the kernel, image, and cokernel of the displayed integer matrix.

- **Observed evidence:** `assets/attachments/extracted/f06solution.md` displays an integral equivalence reducing the matrix to `diag(3,0,0)`, but then states `cokernel(A) ≅ Z^2 ⊕ Z/2Z`. The displayed diagonal form instead gives `Z^2 ⊕ Z/3Z`. Directly, the image is generated by $(3,3,6)=3(1,1,2)$, with $(1,1,2)$ primitive, so the quotient has a torsion class of exact order $3$.

- **Impact and owner:** importing the source conclusion verbatim would give the wrong abelian-group structure on the authored card.

- **Uncertainty:** the contradiction is internal to the retained solution packet and independently verified from the matrix.
  It is consistent with a typographical `2` for `3` in the packet's prose.

- **Repair:** `P-BKF06-8A` now computes the image directly and records `coker(A) ≅ Z^2 ⊕ Z/3Z`. Retain this entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2006 Problem 1B solution packet omits the factorial in Cauchy's estimate

- **Object and need:** `P-BKF06-1B` / `SRC-BERKELEY-PRELIM-FALL-2006`, Problem 1B. The retained proof uses Cauchy's estimates to force all positive derivatives of an entire function to vanish.

- **Observed evidence:** `assets/attachments/extracted/f06solution.md` states `|f^(m)(0)| <= (2^n M)/(R_n)^m`. For ordinary derivatives, Cauchy's estimate is `|f^(m)(0)| <= m! M(R_n)/(R_n)^m`; the factor `m!` is missing.

- **Impact and owner:** the printed inequality is not the standard derivative estimate, although the omitted constant is independent of `n` and the argument still tends to zero after it is restored.

- **Uncertainty:** verified against the retained extraction and the standard Cauchy integral formula.
  No normalized-derivative convention is stated in the packet.

- **Repair:** `P-BKF06-1B` includes the factor `m!` and retains the same limiting argument.
  Retain this entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2012 Problem 7B solution packet uses a non-invariant quotient

- **Object and need:** P-BKF12-7B / SRC-BERKELEY-PRELIM-FALL-2012, Problem 7B. The retained solution packet must prove that a linear map satisfying $AB-BA=A$ is nilpotent.

- **Observed evidence:** assets/attachments/extracted/F12_Solutions.md first correctly computes $BAv=(\lambda-1)Av$ for a $B$-eigenvector $v$, but its final induction then says that $A$ is nilpotent on $V/\CC v$.
  The displayed relation only shows that $Av$ is zero or belongs to the $(\lambda-1)$-eigenspace; it does not show $Av\in\CC v$.
  Thus $\CC v$ need not be $A$-invariant, so $A$ need not induce an operator on that quotient and the induction step is not defined.

- **Impact and owner:** the source solution does not establish the requested nilpotence.
  The owning authored card must supply an independent argument rather than inherit the quotient induction.

- **Uncertainty:** the invalid quotient step is present in the retained solution extraction.
  The preceding eigenvector calculation is correct, and no claim is made that another edition of the solution packet has the same final paragraph.

- **Repair:** P-BKF12-7B now uses the generalized eigenspace decomposition of $B$ and the identity $(B-(\lambda-1)I)A=A(B-\lambda I)$ to show that $A$ shifts generalized eigenspaces from $\lambda$ to $\lambda-1$ and hence satisfies $A^{\dim V}=0$.
  Retain this entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2012 Problem 9B solution packet confuses nullity with algebraic multiplicity

- **Object and need:** P-BKF12-9B / SRC-BERKELEY-PRELIM-FALL-2012, Problem 9B. The retained solution packet factors the characteristic polynomial in order to identify the product of the nonzero eigenvalues.

- **Observed evidence:** assets/attachments/extracted/F12_Solutions.md states that the characteristic polynomial is $x^m\prod_i(x-\lambda_i)$ "where m is the nullity of M." The exponent of the factor $x$ is instead the algebraic multiplicity of the eigenvalue $0$.
  For example, the nonzero nilpotent Jordan block $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ has nullity $1$ but characteristic polynomial $x^2$.

- **Impact and owner:** the packet can identify the wrong coefficient of the characteristic polynomial when the geometric and algebraic multiplicities of $0$ differ.
  The coefficient argument is correct only after replacing nullity by algebraic multiplicity.

- **Uncertainty:** the word "nullity" is present in the retained solution extraction.
  The counterexample is exact; this may be terminological shorthand or a typo in the packet rather than the intended invariant.

- **Repair:** P-BKF12-9B now defines $m$ as the multiplicity of $0$ as a root of the characteristic polynomial and proves that its $t^m$ coefficient is $(-1)^{n-m}$ times the product of the nonzero eigenvalues.
  Retain this entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2013 Problem 7B solution packet proves the converse singularity implication

- **Object and need:** P-BKF13-7B / SRC-BERKELEY-PRELIM-FALL-2013, Problem 7B. The source asks to prove that invertibility of $I_m-AB$ implies invertibility of $I_n-BA$.

- **Observed evidence:** page 18 of assets/attachments/F13_Solutions.pdf argues that if $I_m-AB$ is singular, then a nonzero vector fixed by $AB$ yields, after applying $B$, a vector fixed by $BA$, so $I_n-BA$ is singular.
  This is the converse of the singularity implication needed as the contrapositive of the requested statement.
  The same paragraph also writes the eigenvectors in $\mathbb R^m$ and $\mathbb R^n$ although the matrices are complex.

- **Impact and owner:** as written, the retained solution does not establish the requested implication.
  The owning card must supply the missing direction independently.

- **Uncertainty:** swapping $A$ and $B$ in the same idea immediately gives the needed implication, so the packet may have intended that symmetric argument without stating it.
  No claim is made about another edition.

- **Repair:** P-BKF13-7B now starts with a vector fixed by $BA$, applies $A$, and uses invertibility of $I_m-AB$ to force that vector to vanish.
  Retain this entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2014 Problem 8A solution packet ends with the wrong ambient order

- **Object and need:** P-BKF14-8A / SRC-BERKELEY-PRELIM-FALL-2014, Problem 8A. Part (b) asks for a countably infinite total order whose collection of down-sets has the largest possible cardinality.

- **Observed evidence:** page 9 of assets/attachments/Fall_2014_Solutions.pdf correctly constructs X=Q, injects R into L(Q), and bounds L(Q) by the power set of Q. Its final sentence then says this proves the result "in the case X=R."

- **Impact and owner:** R is uncountable and does not satisfy the hypothesis of the problem.
  The preceding argument proves the intended statement for Q, so importing the final sentence literally would state the wrong example.

- **Uncertainty:** the preceding construction and both cardinality bounds unambiguously use Q, so the final X=R is a typographical error rather than a competing mathematical interpretation.

- **Repair:** P-BKF14-8A retains X=Q throughout and proves |L(Q)|=2^{aleph_0}. Retain this entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2015 Problem 5A solution packet reverses a half-plane and skips repeated critical roots

- **Object and need:** P-BKF15-5A / SRC-BERKELEY-PRELIM-FALL-2015, Problem 5A. Part (a) proves the reciprocal-sum convex-hull lemma and part
  (b) applies it to the zeros of a polynomial derivative.

- **Observed evidence:** assets/attachments/F15_Solutions.pdf normalizes part (a) to z=0 with every c_i in the half-plane Re(w)>0, then says the numbers 1/(z-c_i) also lie in that half-plane.
  In fact 1/(z-c_i)=-1/c_i has negative real part.
  The conclusion that their sum cannot vanish remains valid, but the stated orientation is reversed.
  In part (b), the packet writes p'/p as the reciprocal sum and applies part (a) whenever p'(z)=0 without separating the case p(z)=0; at a repeated root the quotient p'/p is not defined, although that critical point is already a root and hence is trivially in the convex hull.

- **Impact and owner:** importing the packet literally gives a false half-plane assertion and leaves a gap at repeated roots.
  The owning card must correct both points while preserving the Gauss--Lucas argument.

- **Uncertainty:** both issues are visible in the retained PDF text and are mathematically exact.
  They do not affect the truth of either requested conclusion.

- **Repair:** P-BKF15-5A uses the correct negative half-plane for the normalized reciprocal terms and treats p(zeta)=0 separately before using the logarithmic derivative when p(zeta) is nonzero.
  Retain this entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2015 Problem 4B is explicitly retracted by its source solution packet

- **Object and need:** P-BKF15-4B / SRC-BERKELEY-PRELIM-FALL-2015, Problem 4B. The printed problem defines a Schur function to be nonconstant and asks to prove that the displayed Schur-algorithm transform is again a Schur function.

- **Observed evidence:** assets/attachments/F15_Solutions.pdf explicitly states "the problem as stated is incorrect" and gives f(z)=z, for which the transform is the constant function -1. The packet then supplies a corrected formulation: allow Schur functions themselves to be constant, retain the hypothesis that the input f is nonconstant, and prove only holomorphy and the bound |g|<=1 for the transform.

- **Impact and owner:** the source-faithful printed statement is false.
  A solution cannot prove the requested nonconstancy of the output; the owning card must expose the counterexample and distinguish it from the corrected theorem supplied by the same source packet.

- **Uncertainty:** none about the source's intent: the retained official solution packet contains the correction and explains the grading rule.

- **Repair:** P-BKF15-4B preserves the printed problem, gives f(z)=z as the counterexample, and then proves the source-corrected formulation using the disk automorphism and Schwarz's lemma.
  Retain this entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2015 Problem 9B solution packet misadds the diagonal-reflection fixed points

- **Object and need:** P-BKF15-9B / SRC-BERKELEY-PRELIM-FALL-2015, Problem 9B. The Burnside computation requires the number of nonattacking rook placements fixed by each diagonal reflection.

- **Observed evidence:** assets/attachments/F15_Solutions.pdf prints the standard involution-counting expression $1+28+210+420+105$ for a diagonal reflection, but states that its value is
  774. The displayed summands instead total 764. The packet's final answer 5282 is consistent with 764, not 774: using 764 gives $(40320+2(764)+2(12)+384)/8=5282$.

- **Impact and owner:** the intermediate fixed-point total in the official solution is arithmetically false and is incompatible with its own final Burnside average.
  The owning card must use the correct fixed count.

- **Uncertainty:** none.
  The printed summands, their sum, and the final average determine the intended value uniquely.

- **Repair:** P-BKF15-9B counts diagonal-fixed placements as involutions in $S_8$, obtaining 764, and independently derives all other fixed-point counts before recovering the source's final answer 5282. Retain this entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2016 Problem 4A solution packet omits the actual leading term at the indentation

- **Object and need:** P-BKF16-4A / SRC-BERKELEY-PRELIM-FALL-2016, Problem 4A. The retained contour solution analyzes $(e^{3iz}-3e^{iz})/z^3$ on a small upper semicircle around zero.

- **Observed evidence:** assets/attachments/F16_Solutions.pdf states that the "leading term" of $e^{3iz}-3e^{iz}$ is $-9z^2/2+3z^2/2=-3z^2$.
  In fact the expansion begins $-2-3z^2-4iz^3+\cdots$.
  Thus the integrand also contains the more singular term $-2/z^3$.
  The packet also prints the first real-axis segment as $[-R,r]$ rather than the intended $[-R,-r]$.

- **Impact and owner:** the stated local expansion is false and, without a separate calculation, does not justify replacing the small-arc integral by that of $-3/z$.
  The final value survives because the integral of $-2/z^3$ over the symmetric clockwise semicircle is exactly zero.

- **Uncertainty:** none.
  The Taylor expansion and the two semicircle integrals are explicit, and the final source value $3\pi/4$ is consistent with the corrected calculation.

- **Repair:** P-BKF16-4A uses the correct half-annular contour, expands the numerator through the omitted constant term, proves its $-2/z^3$ contribution vanishes, and then obtains the same $3\pi/4$ value.
  Retain this entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2016 Problem 1B prints the unit-ball volume as the sphere surface area

- **Object and need:** P-BKF16-1B / SRC-BERKELEY-PRELIM-FALL-2016, Problem 1B. The problem defines $S_n$ as the $(n-1)$-dimensional surface area of the unit sphere in $\mathbb R^n$ and supplies example values.

- **Observed evidence:** assets/attachments/F16_Exam.pdf prints $S_2=2\pi$ and $S_3=4\pi/3$.
  The latter is the volume of the unit ball in $\mathbb R^3$; the surface area of its unit sphere is $4\pi$.
  The formula requested in part (a), together with $C=\sqrt\pi$ and the gamma recurrence, likewise yields $S_3=4\pi$.

- **Impact and owner:** the parenthetical example contradicts the stated meaning of $S_n$.
  The posed parts (a)--(d) remain solvable because none requires using the incorrect $S_3$ value.

- **Uncertainty:** none.
  The two standard geometric quantities are distinct, and the problem's own formula recovers the correct surface area.

- **Repair:** P-BKF16-1B preserves the source-faithful statement, carries a mathematical erratum remark identifying the corrected value $S_3=4\pi$, and its solution derives the requested formulas without using the false parenthetical value.
  Retain this entry as source errata; the provenance document itself is not rewritten.

### Berkeley Spring 1981 Problem 4 falsely claims two-sided global existence

- **Object and need:** P-BKS81-4 / SRC-BERKELEY-PRELIM-SPRING-1981, Problem 4. Part (1) asks for a solution defined for every $t\in\mathbb R$ from every initial condition.

- **Observed evidence:** along every solution, $s(t)=x(t)^2+y(t)^2$ satisfies $s'=2s(1-s)$.
  For the initial condition $(x_0,y_0)=(2,0)$, hence $s(0)=4$, the forced solution is $s(t)=4/(4-3e^{-2t})$.
  Its denominator vanishes at $t_*=\frac12\log(3/4)<0$, and $s(t)\to+\infty$ as $t\downarrow t_*$.

- **Impact and owner:** Part (1) is false as printed.
  The forward-time statement is true for every initial condition, and Part (2) remains true: every nonzero initial condition has $s(t)\to1$ as $t\to\infty$.

- **Uncertainty:** none.
  The scalar radial equation follows by direct differentiation and has the displayed explicit solution.

- **Repair:** P-BKS81-4 preserves the printed question, gives the finite backward-time blow-up counterexample, proves the corrected forward-time existence statement, proves Part (2), and records the exact erratum on the card.
  Retain this entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Spring 1981 Problem 11 source PDF is missing the contour figure

- **Object and need:** P-BKS81-11 / SRC-BERKELEY-PRELIM-SPRING-1981, Problem 11. The requested contour integral depends on the closed curve $C$ shown in the source.

- **Observed evidence:** page 2 of assets/attachments/Spring81.pdf contains the problem text followed, in place of the contour, by the literal typesetting error `../Fig/Pr/Sp81-11.ps not found`. Thus the retained PDF itself does not specify which of the poles $0$ and $1$ are enclosed or with what winding numbers.

- **Impact and owner:** no unique numerical value can be recovered from the retained source.
  The owning card must not invent the missing curve; it can determine the integral exactly in terms of the winding numbers of $C$.

- **Uncertainty:** none about the retained PDF. An external PostScript figure may have accompanied the original exam, but it is absent from the retained source packet.

- **Repair:** P-BKS81-11 records the missing-source obstruction and computes the residue formula $2\pi i[-\operatorname{Ind}_C(0)+(e-1)\operatorname{Ind}_C(1)]$.
  Retain this entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Fall 1993 Problem 12 source PDF is missing the contour figure

- **Object and need:** P-BKF93-12 / SRC-BERKELEY-PRELIM-FALL-1993, Problem 12. The requested normalized contour integral depends on the curve $\gamma$ that the source says should be depicted.

- **Observed evidence:** page 2 of assets/attachments/Fall93.pdf prints the literal typesetting error "../Fig/Pr/Fa93-12.ps not found" where the curve should occur.
  The integrand survives, but the path itself does not.

- **Impact and owner:** the retained source does not determine the path, orientation, endpoints, or winding numbers, so it does not determine a unique numerical integral.
  The owning card must not infer a curve from the three poles.

- **Uncertainty:** none about the retained repository packet.
  **Searched:** assets/, sources/, corpus/, and Git history for Fa93-12, Fall 1993 duplicates, and the problem card.
  **Found:** the Fall 1993 PDF, its extractions, and P-BKF93-12, but no figure asset or duplicate statement containing the curve.
  **Conclusion:** the contour data are absent from the retained repository source.
  **Confidence:** high.
  **Gaps:** external Berkeley archives were not searched; an original PostScript figure may still exist outside the repository.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-BKF93-12 records the missing-source obstruction, computes all three residues, and gives the exact residue-theorem formula in terms of winding numbers when the missing curve is closed.
  Retain this entry as source errata unless an authoritative copy of the missing figure is recovered.

### Berkeley Fall 1996 Problem 8 extraction drops the numerator fraction

- **Object and need:** P-BKF96-8 / SRC-BERKELEY-PRELIM-FALL-1996, Problem 8. The generalized binomial coefficient must be known before its denominator can be analyzed.

- **Observed evidence:** page 2 of assets/attachments/Fall96.pdf, read with layout preservation, places `1/2` directly above `n` inside the displayed binomial coefficient.
  Both retained Markdown extractions instead reduce the numerator to `1`.

- **Impact and owner:** the problem card had treated the coefficient as unrecoverable, preventing the Author-solutions selector from completing the card.
  The authoritative retained PDF determines the statement as $\binom{1/2}{n}$.

- **Uncertainty:** none about the retained PDF layout; the stacked `1/2` and `n` are explicit on the page.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-BKF96-8 restores the coefficient from the PDF and supplies the complete proof.

### Berkeley Fall 1996 Problem 15 leaves epsilon unquantified

- **Object and need:** P-BKF96-15 / SRC-BERKELEY-PRELIM-FALL-1996, Problem 15. The existence of a real twentieth root depends on the printed parameter epsilon.

- **Observed evidence:** page 3 of assets/attachments/Fall96.pdf visibly asks for a real A with twentieth power diag(-1,-1-epsilon), then asks to exhibit A or prove none exists.
  No definition or quantifier for epsilon appears in the problem or surrounding page.

- **Impact and owner:** assuming epsilon>0 would add a hypothesis not in the source.
  The owning solution instead classifies all real epsilon.

- **Uncertainty:** none about the retained PDF; the missing quantifier is in the source itself, not only in the extraction.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-BKF96-15 proves existence exactly for epsilon=0 and records the source omission in a mathematical remark.

### Berkeley Spring 1983 Problem 4 source PDF is missing the network diagram

- **Object and need:** P-BKS83-4 / SRC-BERKELEY-PRELIM-SPRING-1983, Problem 4. The requested Euclidean symmetry group depends on the triangular network drawn in the source.

- **Observed evidence:** page 1 of assets/attachments/Spring83.pdf prints \`../Fig/Pr/Sp83-4.ps not found\` where the defining diagram should occur.
  No retained \`Sp83-4\` asset, duplicate statement with the figure, or embedded PDF image is present in the repository.

- **Impact and owner:** the four surviving labeled points do not determine the network or its symmetry group.
  The owning card must not reconstruct the missing edges by guesswork.

- **Uncertainty:** none about the retained packet.
  The original exam may have had an external PostScript figure, but that file is absent here.

- **Repair:** P-BKS83-4 records the source obstruction and proves that the surviving data are underdetermined by exhibiting two triangular networks through the named points with different Euclidean symmetry groups.
  Retain this entry as source errata; the missing source asset is not reconstructed.

### Berkeley Spring 2009 Problem 7A source solution doubles the requested integral

- **Object and need:** P-BKS09-7A / SRC-BERKELEY-PRELIM-SPRING-2009, Problem 7A. The exam asks for $\int_0^\pi (a+\cos\theta)^{-1}\,d\theta$ for $a>1$ by residues.

- **Observed evidence:** assets/attachments/extracted/s09solutions.md states the interval $[0,\pi]$, but its solution substitutes $z=e^{i\theta}$ and replaces the requested integral by $-2i\int_{|z|=1}(z^2+2az+1)^{-1}\,dz$.
  That contour parametrization corresponds to $0\leq\theta\leq2\pi$, not $0\leq\theta\leq\pi$, and the packet consequently reports $2\pi/\sqrt{a^2-1}$.

- **Impact and owner:** the source solution is too large by a factor of two.
  Since the integrand is invariant under $\theta\mapsto2\pi-\theta$, the full-circle integral is twice the requested half-circle integral.
  The owning solution must therefore divide the residue computation by $2$.

- **Uncertainty:** none about the retained statement and solution extraction; the factor mismatch is determined by the displayed integration interval and the contour parametrization.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-BKS09-7A supplies the corrected residue computation and obtains $\pi/\sqrt{a^2-1}$.
  Retain this entry as source errata; the provenance packet itself is not rewritten.

### Berkeley Spring 2009 Problem 9A source solution switches to the wrong least common multiple

- **Object and need:** P-BKS09-9A / SRC-BERKELEY-PRELIM-SPRING-2009, Problem 9A. The requested argument must use the integrality of $d_{2m+1}I_m$ to prove $d_{2m+1}\geq2^{2m}$.

- **Observed evidence:** page 4 of assets/attachments/s09solutions.pdf first establishes $d_{2m+1}I_m\in\mathbb Z$, then after bounding $0<I_m\leq(1/4)^m$ states instead that $d_mI_m\geq1$.
  The same index change is present in the retained Markdown extraction.

- **Impact and owner:** positivity and integrality justify $d_{2m+1}I_m\geq1$, not $d_mI_m\geq1$.
  The printed step therefore does not follow as written, although replacing $d_m$ by $d_{2m+1}$ immediately completes the intended proof.

- **Uncertainty:** none; the incorrect subscript is present in the retained PDF itself and is not merely an extraction artifact.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-BKS09-9A keeps the established integer $d_{2m+1}I_m$ throughout and derives $d_{2m+1}\geq4^m=2^{2m}$.
  Retain this entry as source errata.

### Berkeley Spring 2009 Problem 1B source solution omits the case n=1

- **Object and need:** P-BKS09-1B / SRC-BERKELEY-PRELIM-SPRING-2009, Problem 1B. The statement does not impose $n\geq2$, so its odd case includes $n=1$.

- **Observed evidence:** page 4 of assets/attachments/s09solutions.pdf begins its proof with “Since $f^{[n-1]}(a)=0$” and then applies a Taylor formula with an $(n-1)$st-derivative remainder.
  For $n=1$, the displayed vanishing would assert $f(a)=0$, which is not a hypothesis, and that remainder formula does not give the claimed argument.

- **Impact and owner:** the retained source proof establishes the intended parity conclusion for $n\geq2$ but leaves the permitted case $n=1$ untreated.
  In that case $f'(a)>0$ directly implies values below $f(a)$ on the left of $a$ and above $f(a)$ on the right.

- **Uncertainty:** low.
  The retained statement has no $n\geq2$ qualifier.
  If an unstated convention was intended to impose it, the extra case is redundant rather than harmful.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-BKS09-1B treats $n=1$ separately and then gives the Taylor argument for $n\geq2$.

### Berkeley Spring 2009 Problem 7B source omits f and its solution inverts the square root

- **Object and need:** P-BKS09-7B / SRC-BERKELEY-PRELIM-SPRING-2009, Problem 7B. The problem is intended to start with a normalized univalent function $f$ and to prove that $g(z)=\sqrt{f(z^2)}$ has the stated analytic, odd, and univalent properties.

- **Observed evidence:** page 6 of assets/attachments/s09solutions.pdf prints “If is a univalent ... function” before immediately defining $f(z)=z+\sum_{n\geq2}a_nz^n$, so the function name is missing in the opening clause.
  In the solution, after correctly writing $f(z^2)=z^2\phi(z)$ and constructing $\sqrt{\phi}$, the PDF then prints $g(z)=1/\sqrt{f(z^2)}=1/(z\sqrt{\phi(z)})$, contradicting the displayed definition of $g$ immediately above.

- **Impact and owner:** the omitted name is recoverable from the defining formula for $f$.
  The reciprocal formula in the solution cannot be the intended $g$: it has a pole at $0$, whereas the problem asks for a function analytic on the unit disk.
  The correct analytic branch is $g(z)=z\sqrt{\phi(z)}$ with the square root chosen to equal $1$ at $0$.

- **Uncertainty:** none about these two retained-PDF defects; both are visible on page 6 and are not extraction artifacts.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-BKS09-7B retains a mathematical remark about the omitted name and supplies the corrected analytic-square-root proof using $g(z)=z\sqrt{\phi(z)}$.
  Retain this entry as source errata.

### Berkeley Spring 2011 Problem 7B card corrupts the Laplace equation

- **Object and need:** P-BKS11-7B / SRC-BERKELEY-PRELIM-SPRING-2011, Problem 7B. The statement must reproduce the Laplace equation printed in the retained source.

- **Observed evidence:** page 5 of assets/attachments/s11solutions.pdf prints $\partial^2 f/\partial x^2+\partial^2 f/\partial y^2=0$.
  The authored card instead has $\partial^2\widetilde f/\partial x^2$ in the first term and $\partial^2 f/\partial y^2$ in the second.

- **Impact and owner:** the mixed function symbols make the displayed definition of harmonicity incorrect as written.
  The retained PDF is unambiguous, so the card should use $f$ in both second derivatives.

- **Uncertainty:** none; the retained PDF was inspected directly and the discrepancy is an extraction/transcription defect.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-BKS11-7B restores $f$ in the first Laplacian term before attaching the complete solution.

### Berkeley Spring 2012 Problem 7A card drops the n=0 term and source solution uses the wrong functional equation

- **Object and need:** P-BKS12-7A / SRC-BERKELEY-PRELIM-SPRING-2012, Problem 7A. The authored statement must match the retained series, and the natural-boundary proof must use the functional equation that this series actually satisfies.

- **Observed evidence:** page 2 of assets/attachments/s12solutions.pdf prints $f(z)=\sum_{n\geq0}z^{2^n}$, while the authored card has $\sum_{n>0}z^{2^n}$.
  The source solution on the same page then states $f(z)=1+f(z^2)$.

- **Impact and owner:** the card omits the initial term $z$.
  For the source series, direct reindexing gives $f(z)=z+f(z^2)$, not $1+f(z^2)$.
  The source solution's propagation idea is repairable, but its displayed functional equation is false.

- **Uncertainty:** none; both formulas are legible in the retained PDF and were checked visually.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-BKS12-7A restores the source index $n\geq0$ and proves the natural boundary using $f(z)=z+f(z^2)$ and the dense dyadic roots of unity.

### Berkeley Spring 2013 Problem 3B source solution omits the permitted case k=0

- **Object and need:** P-BKS13-3B / SRC-BERKELEY-PRELIM-SPRING-2013, Problem 3B. The exam assumes only that $k\neq n^2$ for $n=1,2,3,\ldots$, so $k=0$ remains allowed.

- **Observed evidence:** the retained Spring 2013 exam states exactly that restriction.
  The retained solution writes the constant Fourier term as $a_0/(2k)$, which is undefined when $k=0$.

- **Impact and owner:** the printed solution handles only $k\neq0$.
  When $k=0$, periodic solvability forces $a_0=0$, all nonconstant Fourier coefficients are still determined by division by $-n^2$, and the constant Fourier coefficient of $f$ is arbitrary.

- **Uncertainty:** none; the exam statement and solution packet were checked directly and disagree on this permitted case.

- **Repair:** [Author solutions](TODO.md#7-author-solutions), owned by issue #2. P-BKS13-3B treats $k\neq0$ and $k=0$ separately and proves convergence of the resulting Fourier series in both cases.

### Duplicate Burnside lemma cards C-CM7ZS and C-HE5SL

- **Object and need:** `C-CM7ZS` and `C-HE5SL` in `corpus/theory/Algebra`. The copy-policy pass must preserve one canonical statement rather than two intrinsic cards for the same mathematics (`CARD-04`, `SOURCE-02`).

- **Observed evidence:** both complete cards have the title `Burnside's lemma`, the same hypotheses (a finite group acting on a finite set), the same fixed-point notation, and the same orbit-count formula.
  Before repair, `C-CM7ZS` also declared itself `variant-of: C-HE5SL`. The wiki references `C-HE5SL`; the only other reader-facing reference to `C-CM7ZS` was the algebra-guide publication list.

- **Impact and owner:** retaining both cards gives two addresses for one theorem and lets guide surfaces disagree about which one is canonical.
  `C-HE5SL` is the existing wiki-facing owner; the algebra guide must point to it and the duplicate card must be removed.

- **Uncertainty:** none after reading both complete cards; there is no mathematical or source-appearance distinction between them.

- **Repair:** the same repair commit redirects `publications/algebra-guide.yaml` to `C-HE5SL` and removes `C-CM7ZS`.

### Second duplicate Burnside card FF-OL75S

- **Object and need:** `C-HE5SL` and `FF-OL75S` in `corpus/theory/Algebra`. Both state Burnside's orbit-counting formula for a finite group acting on a finite set.

- **Observed evidence:** the displayed formulas are identical after the notational substitution `$X^g=\Fix(g)$`; `FF-OL75S` adds only the review prompt and the standard double-counting proof.
  The wiki and algebra guide displayed both cards.

- **Impact and owner:** a second flashcard-derived address remained for the same theorem after the earlier `C-CM7ZS` duplicate was removed.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the review prompt and double-counting proof to `C-HE5SL`, removes duplicate reader-facing references, and deletes `FF-OL75S`.

### Duplicate class-equation cards C-A6UAR, C-O7CP3, and FD-L2TEC

- **Object and need:** `C-A6UAR`, `C-O7CP3`, and `FD-L2TEC` in `corpus/theory/Algebra`. They are intrinsic cards for the same class equation (`CARD-04`, `SOURCE-02`).

- **Observed evidence:** after reading all three complete cards, they have the same title, hypotheses, centralizer notation, choice of noncentral conjugacy-class representatives, and class-equation formula.
  Their only substantive source difference is presentation syntax (`\#` versus the repository's `\size` macro).
  `FD-L2TEC` later restated the same theorem and added its standard conjugation-action proof.
  The wiki and algebra guide exposed the duplicate theorem beside `C-O7CP3`.

- **Impact and owner:** retaining the duplicates gives multiple canonical-looking addresses for one theorem and splits guide references.
  `C-O7CP3` is already the wiki-facing statement and uses the current notation convention.

- **Uncertainty:** none after reading all three complete cards; no distinct source appearance or mathematical variant was found.

- **Repair:** the first repair redirected the algebra guide to `C-O7CP3` and removed `C-A6UAR`; the later repair moves the review prompt and proof from `FD-L2TEC` onto `C-O7CP3`, removes duplicate reader-facing references, and deletes `FD-L2TEC`.

### Duplicate coset-counting cards C-HWX2P and C-XRC67

- **Object and need:** `C-HWX2P` and `C-XRC67` in `corpus/theory/Algebra`. They state the same coset-counting formula and therefore violate the single-owner expectation for standard statements (`CARD-04`, `SOURCE-02`).

- **Observed evidence:** both complete cards have the same title, hypotheses, definition of the index, and equations `$\size G=[G:H]\,\size H$` and `$[G:H]=\size G/\size H$`, differing only by `\size` versus `\#` presentation syntax.
  `C-XRC67` also declares itself `variant-of: C-HWX2P`. The wiki and algebra guide both reference `C-HWX2P`; no reader-facing surface references `C-XRC67`.

- **Impact and owner:** retaining `C-XRC67` creates a second intrinsic address for the same theorem without a source or mathematical distinction.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit removes `C-XRC67` and retains `C-HWX2P` as the canonical statement.

### Zero-divisor definition was wrong for noncommutative rings and duplicated

- **Object and need:** `D-4I3SL` and `FD-S62UB` in `corpus/theory/Algebra`. `D-GURUB` defines rings without commutativity, but `D-4I3SL` defined a zero divisor by requiring one nonzero element to annihilate the given element on both the left and the right.
  `FD-S62UB` separately gave the standard commutative definition.

- **Observed evidence:** `D-4I3SL` quantified over an arbitrary ring and required `$ar=ra=0$`; `FD-S62UB` quantified over a commutative ring and required a nonzero `$x$` with `$rx=0$`. Current uses of the zero-divisor card in the domain, primary-ideal, and Noetherian-ring material are in the commutative setting.
  The wiki and algebra guide exposed both definitions side by side.

- **Impact and owner:** the canonical card misstated the noncommutative notion and duplicated a second card for the commutative notion.
  In a noncommutative ring, left and right zero divisors need not coincide; the simultaneous two-sided condition is not the standard generic definition.

- **Uncertainty:** none about the defect.
  The corpus currently needs the commutative notion; noncommutative left/right variants can be introduced separately if needed later.

- **Repair:** the same repair commit restricts `D-4I3SL` to commutative rings, uses the standard annihilator definition, preserves the review prompt there, removes duplicate reader-facing references to `FD-S62UB`, and deletes the duplicate card.

### D-5JYEI delegated the separable-degree statement to an opaque screenshot

- **Object and need:** `D-5JYEI`, Galois extension and Galois group.
  The closing remark states that separable degree counts embeddings but then shows only a legacy image with filename alt text instead of the formula.

- **Observed evidence:** the card ended with `![figures/2021-08-09_22-29-40.png](../../assets/figures/...)`; no surrounding prose stated the embedding set or explained how the Galois automorphism count follows.

- **Impact and owner:** the card's last mathematical claim was inaccessible to text readers and dependent on an unexplained asset.
  The relevant formula is intrinsic to the theorem and should be authored as mathematics on the card.

- **Uncertainty:** none; for a finite extension, the separable degree is the number of `$k$`-embeddings into a fixed algebraic closure.

- **Repair:** the same repair commit replaces the screenshot with the formula `$[L:k]_s=\size\Hom_{k\text{-alg}}(L,\bar k)$` and explains why normality identifies these embeddings with `\Gal(L/k)` in the Galois case.

### Duplicate lower-central-series cards D-BGNME and D-D7L4X

- **Object and need:** `D-BGNME` and `D-D7L4X` in `corpus/theory/Algebra`. The two cards gave the same definition of the lower central series (`CARD-04`, `SOURCE-02`).

- **Observed evidence:** both complete cards define `$G^0=G$` and `$G^{i+1}=[G,G^i]$` using the same commutator convention.
  `D-D7L4X` declares itself `variant-of: D-BGNME`; `D-BGNME` additionally records the nilpotence characterization.
  The wiki and algebra guide exposed both.

- **Impact and owner:** two intrinsic addresses for the same definition split links and duplicate the recall unit.
  `D-BGNME` is already used by `T-4INET` and contains the strictly richer local exposition.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit redirects the wiki to `D-BGNME`, removes the duplicate guide entry, and deletes `D-D7L4X`.

### D-KRKV7 printed an incorrect presentation of the quaternion group

- **Object and need:** `D-KRKV7`, Quaternion group `$Q_8$`. The second displayed presentation must actually force the generators to have the quaternion orders.

- **Observed evidence:** the card printed `$\gens{x,y\mid x^4=y^4,\ x^2=y^2,\ yxy^{-1}=x^{-1}}$`. The relation `$x^4=y^4$` follows already from `$x^2=y^2$` and does not impose `$x^4=1$`.

- **Impact and owner:** the displayed group need not be finite and is not the standard presentation of `$Q_8$`. The canonical presentation requires `$x^4=1$`, `$x^2=y^2$`, and `$yxy^{-1}=x^{-1}$`.

- **Uncertainty:** none; the standard two-generator presentation is explicit.

- **Repair:** the same repair commit replaces `$x^4=y^4$` by `$x^4=1$` and states the eight quaternion elements directly rather than treating `-1` as a presentation generator.

### D-LIEMF marked the free-module universal map as injective without hypothesis

- **Object and need:** `D-LIEMF`, Free module.
  The universal property of the free module uses a set map `$\iota:\mathcal B\to M$`; injectivity is not part of the universal property's statement.

- **Observed evidence:** the commutative diagram rendered the arrow labelled `$\iota$` with `hook`, although item (2) only assumes a map of sets.
  Over the zero ring, the free module on a nonempty set is the zero module and the universal structure map is not injective as a set map.

- **Impact and owner:** the diagram asserted a stronger property than the proposition and one that fails in an allowed ring case.

- **Uncertainty:** none; the free-module adjunction requires a map, not an injection.

- **Repair:** the same repair commit removes the hook decoration from the `$\iota$` arrow and leaves the universal property unchanged.

### Gram matrix had two defining cards

- **Object and need:** `D-H4TDM` and `D-RG5FO` in `corpus/theory/Algebra`. Both cards defined the Gram matrix of a bilinear form, contrary to the single canonical defining-occurrence policy.

- **Observed evidence:** `D-H4TDM` defines the matrix `$(b(e_i,e_j))$` and records change of basis and nondegeneracy; `D-RG5FO` independently defined the same matrix and then proved the distinct proposition that Gram matrices classify bilinear forms in a fixed basis.
  The wiki linked the term “Gram matrix” to `D-RG5FO` while other theory cards linked it to `D-H4TDM`.

- **Impact and owner:** the duplicated definition split the canonical link, while the useful classification proposition on `D-RG5FO` should be retained as separate mathematics.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit keeps `D-H4TDM` as the definition owner, converts `D-RG5FO` to the proposition “Bilinear forms and Gram matrices,” and redirects the wiki's definitional link to `D-H4TDM`.

### D-SSGKC duplicated the quadratic-form definition

- **Object and need:** `D-NRRIT` and `D-SSGKC` in `corpus/theory/Algebra`. `D-NRRIT` is the basis-free definition of a quadratic form, while `D-SSGKC` independently redefined a quadratic form as a degree-two polynomial before discussing its coordinate matrix and real signature.

- **Observed evidence:** the two complete cards define the same object in equivalent forms when the characteristic is not `2`; `D-SSGKC` already had a relation to `D-NRRIT` and a final concept block restating the basis-free definition.

- **Impact and owner:** the coordinate card duplicated the canonical definiendum rather than using it, while its matrix/signature material is distinct and useful.

- **Uncertainty:** none; in characteristic different from `2`, a basis-free quadratic form on `$k^n$` has a unique symmetric coordinate matrix.

- **Repair:** the same repair commit makes `D-SSGKC` use `D-NRRIT`, defines only the coordinate matrix and signature locally, and moves the Artin citation onto Sylvester's law of inertia.

### D-TZXBO used commutative Noetherian terminology on arbitrary rings

- **Object and need:** `D-TZXBO`, Noetherian ring.
  `D-GURUB` allows noncommutative rings and `D-GOFWL` defines an unqualified ideal there to mean a two-sided ideal.

- **Observed evidence:** `D-TZXBO` quantified over an arbitrary ring and called ACC on those two-sided ideals “Noetherian.”
  In noncommutative ring theory the standard notions are left-Noetherian and right-Noetherian; ACC only on two-sided ideals is a different condition.
  Every current use of `D-TZXBO` in the corpus and wiki is in commutative algebra.

- **Impact and owner:** the canonical definition silently changed meaning outside the commutative setting and could be read as the standard noncommutative notion when it is not.

- **Uncertainty:** none about current scope; all observed consumers are commutative.

- **Repair:** the same repair commit restricts `D-TZXBO` to commutative rings and leaves left/right Noetherian notions for separate definitions if they are ever needed.

### Group action had two defining cards

- **Object and need:** `D-WYC7C` and `D-3T6O2` in `corpus/theory/Algebra`. Both cards independently defined a group action, while `D-3T6O2` also contained the distinct action/homomorphism correspondence.

- **Observed evidence:** both complete cards used the same axioms `$e\cdot x=x$` and `$g\cdot(h\cdot x)=(gh)\cdot x$`. `D-WYC7C` additionally owns orbit, stabilizer, and fixed-point definitions and is already the main dependency of the action theorems.
  Reader-facing links were split between the two cards.

- **Impact and owner:** duplicate defining occurrences split the canonical concept link, while deleting `D-3T6O2` would discard its useful proposition identifying actions with homomorphisms into `\Aut(X)`.

- **Uncertainty:** none after reading both live cards; the older candidate `D-BVOUL` is absent from the current tree.

- **Repair:** the same repair commit keeps `D-WYC7C` as the definition owner, converts `D-3T6O2` to the action/homomorphism proposition, and redirects definitional links to `D-WYC7C`.

### Duplicate UFD cards D-INULL and FD-25SUQ

- **Object and need:** `D-INULL` and `FD-25SUQ` in `corpus/theory/Algebra`. Both cards gave the full definition of a unique factorization domain, including existence and uniqueness up to order and associates.

- **Observed evidence:** the complete statements are mathematically identical; `D-INULL` is the dependency used by the UFD theorems and polynomial-ring material, while `FD-25SUQ` came from the flashcard migration.
  The wiki and algebra guide displayed both adjacent to one another.

- **Impact and owner:** the duplicate flashcard creates a second defining occurrence and splits review/navigation without adding mathematics.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the flashcard review prompt to `D-INULL`, removes duplicate reader-facing references, and deletes `FD-25SUQ`.

### Duplicate integral-domain cards D-QJ3QL and FD-2A5XH

- **Object and need:** `D-QJ3QL` and `FD-2A5XH` in `corpus/theory/Algebra`. Both cards define a nonzero commutative ring with no nonzero zero divisors.

- **Observed evidence:** the complete statements are mathematically identical.
  `D-QJ3QL` is the dependency used throughout the ring and factorization theory; `FD-2A5XH` is a migrated flashcard and the wiki displayed it immediately beside `D-QJ3QL`.

- **Impact and owner:** the flashcard duplicate creates a second canonical definition without additional mathematics.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the review prompt to `D-QJ3QL`, removes the duplicate wiki entry, and deletes `FD-2A5XH`.

### Duplicate indecomposable-module cards D-4HEUB and FD-2EUYX

- **Object and need:** `D-4HEUB` and `FD-2EUYX` in `corpus/theory/Algebra`. `D-4HEUB` already defines decomposable and indecomposable modules; `FD-2EUYX` repeats the indecomposable definition.

- **Observed evidence:** both complete statements say that a nonzero module is indecomposable exactly when it cannot be written as a direct sum of two nonzero submodules.
  The wiki and algebra guide displayed both adjacent to one another.

- **Impact and owner:** the flashcard duplicate adds no mathematics and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the review prompt to `D-4HEUB`, removes duplicate reader-facing references, and deletes `FD-2EUYX`.

### Simple ring had a second defining occurrence on the simple-module card

- **Object and need:** `FD-SNOTW` and `D-4KM4P` in `corpus/theory/Algebra`. `FD-SNOTW` defines simple rings for arbitrary rings, while `D-4KM4P` independently defined the commutative special case alongside simple modules.

- **Observed evidence:** `D-4KM4P` called a commutative ring simple when it is simple as a module over itself, equivalently when its only ideals are `0` and `R`; `FD-SNOTW` gives the same two-sided-ideal definition without the unnecessary commutativity restriction.

- **Impact and owner:** the term “simple” had two defining occurrences for rings, while `D-4KM4P` is otherwise the canonical simple-module card.

- **Uncertainty:** none; the general ring definition specializes to the commutative statement.

- **Repair:** the same repair commit leaves `FD-SNOTW` as the sole simple-ring owner, removes the ring definition from `D-4KM4P`, and records the relation between the two cards.

### Duplicate cyclic-module cards D-HY7UU and FD-S2W5E

- **Object and need:** `D-HY7UU` and `FD-S2W5E` in `corpus/theory/Algebra`. Both define a cyclic module as a module generated by one element.

- **Observed evidence:** the definition blocks are identical.
  `FD-S2W5E` additionally proves the standard characterization `$M\cong R/I$` for a left ideal `$I$`. The wiki and algebra guide displayed both cards.

- **Impact and owner:** the duplicate definition splits the recall unit, while the quotient characterization is useful and should be retained on the canonical card.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the prompt and quotient characterization/proof to `D-HY7UU`, removes duplicate reader-facing references, and deletes `FD-S2W5E`.

### Duplicate torsion-free-module card FD-U6KUJ

- **Object and need:** `D-ZJJ7G` and `FD-U6KUJ` in `corpus/theory/Algebra`. `D-ZJJ7G` already defines torsion-free modules; `FD-U6KUJ` restates the integral-domain special case as vanishing of the torsion submodule.

- **Observed evidence:** over an integral domain the torsion set on `D-ZJJ7G` is exactly the torsion submodule of `FD-BPUNZ`, so `$M_t=\{0\}$` and `$\tor(M)=0$` are the same condition.
  The wiki and algebra guide exposed both definitions.

- **Impact and owner:** the flashcard adds no distinct mathematics and splits the definition of torsion-free modules.

- **Uncertainty:** none after reading the canonical torsion card, the domain-specific torsion-submodule card, and `FD-U6KUJ`.

- **Repair:** the same repair commit moves the review prompt to `D-ZJJ7G`, removes duplicate reader-facing references, and deletes `FD-U6KUJ`.

### Duplicate simple-group cards D-T2NZ4 and FD-2UWAQ

- **Object and need:** `D-T2NZ4` and `FD-2UWAQ` in `corpus/theory/Algebra`. Both cards define a nontrivial group whose only normal subgroups are the identity subgroup and the whole group.

- **Observed evidence:** the complete definitions are mathematically identical.
  `D-T2NZ4` is used by the alternating-group and finite-index arguments; `FD-2UWAQ` is a migrated flashcard.
  The wiki and algebra guide exposed both, and one flashcard-derived series card still linked to the duplicate.

- **Impact and owner:** the flashcard duplicate creates a second defining occurrence and splits dependencies.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the prompt and citation to `D-T2NZ4`, redirects the remaining dependency, removes duplicate reader-facing references, and deletes `FD-2UWAQ`.

### Duplicate composition-series cards D-FYX4I and FD-PLAEO

- **Object and need:** `D-FYX4I` and `FD-PLAEO` in `corpus/theory/Algebra`. They define the same finite normal series, with `D-FYX4I` descending by maximal proper normal subgroups and `FD-PLAEO` ascending with simple successive quotients.

- **Observed evidence:** those conditions are equivalent, since `$N_i\normal N_{i+1}$` is maximal proper exactly when `$N_{i+1}/N_i$` is simple.
  `FD-PLAEO` additionally names the successive simple quotients as composition factors.
  The wiki and algebra guide exposed both cards, and `FD-T7IQV` linked to the flashcard duplicate.

- **Impact and owner:** two cards owned one definition, while the composition factor terminology belongs naturally on the canonical series card.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the prompt and composition-factor terminology to `D-FYX4I`, redirects `FD-T7IQV`, removes duplicate reader-facing references, and deletes `FD-PLAEO`.

### FD-T7IQV restated solvability as a definition instead of a finite-group criterion

- **Object and need:** `D-DFIDP` and `FD-T7IQV` in `corpus/theory/Algebra`. `D-DFIDP` canonically defines solvable groups by a finite normal series with abelian quotients; `FD-T7IQV` independently defined finite-group solvability via abelian composition factors.

- **Observed evidence:** the latter condition is an equivalent theorem for finite groups, not a second definition owner.
  No other card states this composition-factor criterion.

- **Impact and owner:** keeping the card as a definition duplicated the term, while deleting it would lose a useful finite-group characterization.

- **Uncertainty:** none; the equivalence follows because subgroups and quotients of solvable groups are solvable and a simple solvable group is abelian.

- **Repair:** the same repair commit converts `FD-T7IQV` to the proposition “Solvability via composition factors,” links it to the canonical solvability and composition-series cards, and adds the proof of the equivalence.

### Duplicate finite-Galois card FD-4GFTY

- **Object and need:** `D-5JYEI` and `FD-4GFTY` in `corpus/theory/Algebra`. The canonical Galois card defines finite Galois extensions by normality and separability and proves the automorphism-count condition as an equivalent characterization; the flashcard restates that characterization as a second definition.

- **Observed evidence:** `D-5JYEI` item (5) states `$\size\Aut_F(K)=[K:F]_s=[K:F]$`; `FD-4GFTY` defines Galois by `$\abs{\Aut(K/F)}=[K:F]$`. The wiki and algebra guide displayed both.

- **Impact and owner:** the flashcard duplicates an equivalent condition already owned by the canonical card and creates a second defining surface.

- **Uncertainty:** none after reading both cards.

- **Repair:** the same repair commit moves the automorphism-count review prompt to `D-5JYEI`, removes duplicate reader-facing references, and deletes `FD-4GFTY`.

### Duplicate finite-Galois characterization theorem FT-3WWKN

- **Object and need:** `D-5JYEI` and `FT-3WWKN` in `corpus/theory/Algebra`. Both list equivalent characterizations of a finite Galois extension.

- **Observed evidence:** `FT-3WWKN` lists separable splitting field, fixed field, full automorphism count, and normal-plus-separable.
  `D-5JYEI` already contains all four and additionally the irreducible separable splitting-field characterization and the separable-degree equality.

- **Impact and owner:** the flashcard theorem duplicates a strictly richer canonical card; one downstream example still linked to the duplicate.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit adds a characterization review prompt to `D-5JYEI`, redirects the downstream link, removes duplicate reader-facing references, and deletes `FT-3WWKN`.

### Duplicate fundamental-theorem-of-Galois-theory cards

- **Object and need:** `FT-GJ6NR` and `T-NLPZY` in `corpus/theory/Algebra`. Both state the subgroup/intermediate-field anti-isomorphism and its standard consequences.

- **Observed evidence:** the field/subgroup bijection, inclusion reversal, degree formulas, normal-subgroup criterion, and compositum/intersection formulas agree exactly.
  `T-NLPZY` additionally records the normalizer of an intermediate field and distinguishes `$\langle H_1,H_2\rangle$` from the product set `$H_1H_2$`; `FT-GJ6NR` contributes only the review prompt.

- **Impact and owner:** the same major theorem had two intrinsic addresses in the Galois wiki and algebra guide.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the review prompt to `T-NLPZY`, removes duplicate reader-facing references, and deletes `FT-GJ6NR`.

### Duplicate fixed-point congruence lemmas L-354HC and L-DJKXL

- **Object and need:** `L-354HC` and `L-DJKXL` in `corpus/theory/Algebra`. Both state that for a finite `$p$`-group acting on a finite set, the total number of points is congruent modulo `$p$` to the number of global fixed points.

- **Observed evidence:** the statements and orbit-partition proofs agree term-for-term up to notation.
  The wiki used `L-354HC`; three Sylow-theory cards used `L-DJKXL`; the algebra guide listed both.

- **Impact and owner:** one lemma had two intrinsic addresses and split its dependency graph.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit retains `L-354HC`, adds the explicit action/orbit-stabilizer dependencies, redirects the three theorem links, removes the duplicate guide entry, and deletes `L-DJKXL`.

### Duplicate irreducible-element cards D-TO3IY and FD-6LLJF

- **Object and need:** `D-TO3IY` and `FD-6LLJF` in `corpus/theory/Algebra`. Both define a nonzero nonunit `$r$` to be irreducible when every factorization `$r=ab$` has a unit factor.

- **Observed evidence:** the complete definitions are mathematically identical.
  `D-TO3IY` is used by the UFD and prime-element material; `FD-6LLJF` is a migrated flashcard and the wiki displayed it beside the canonical card.

- **Impact and owner:** the flashcard duplicate creates a second defining occurrence without additional mathematics.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the review prompt to `D-TO3IY`, removes the duplicate wiki link, and deletes `FD-6LLJF`.

### Duplicate prime-element cards D-AWSKI and FD-S52W7

- **Object and need:** `D-AWSKI` and `FD-S52W7` in `corpus/theory/Algebra`. Both define a nonzero nonunit `$p$` to be prime when `$p\divides ab$` implies `$p\divides a$` or `$p\divides b$`.

- **Observed evidence:** the definition bodies are mathematically identical.
  `D-AWSKI` is the dependency used by the prime-versus-irreducible theorem and factorization wiki; the wiki displayed `FD-S52W7` beside it.

- **Impact and owner:** the flashcard adds no distinct mathematics and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the review prompt to `D-AWSKI`, removes the duplicate wiki link, and deletes `FD-S52W7`.

### FD-R4K7Z was a second irreducible-element duplicate with a false variant edge

- **Object and need:** `FD-R4K7Z` in `corpus/theory/Algebra`. The card defines irreducible elements of a commutative ring, which is already owned by `D-TO3IY`, but declared itself `variant-of: FD-GHY34`, a polynomial irreducibility card.

- **Observed evidence:** its body is the same ring-element condition as `D-TO3IY`: a nonzero nonunit `$p$` with every factorization `$p=ab$` having a unit factor.
  `FD-GHY34` instead quantifies over polynomials in `$K[x]$`.

- **Impact and owner:** the card both duplicated the canonical definition and asserted a variant relation between different levels of generality/objects.

- **Uncertainty:** none after reading all three cards.

- **Repair:** the same repair commit removes the duplicate wiki link and deletes `FD-R4K7Z`; `D-TO3IY` already carries the equivalent review prompt.

### Duplicate irreducible-polynomial cards D-BVMTZ, FD-GHY34, and FD-KPW3H

- **Object and need:** `D-BVMTZ`, `FD-GHY34`, and `FD-KPW3H` in `corpus/theory/Algebra`. All three define irreducibility of a polynomial over a field by absence of a factorization into two positive-degree factors.

- **Observed evidence:** the definitions are equivalent; `FD-GHY34` added the observation that degree-one polynomials are irreducible, while `FD-KPW3H` restates the same condition as “no factorization into two strictly lower-degree factors.”
  `D-BVMTZ` is the dependency used throughout Galois and factorization theory.
  The wiki exposed the flashcard definitions beside the canonical card.

- **Impact and owner:** the flashcard duplicates the defining occurrence while its small useful remark can live on the canonical card.

- **Uncertainty:** none after reading all three complete cards.

- **Repair:** the first repair moved the prompt and linear-polynomial remark to `D-BVMTZ` and deleted `FD-GHY34`; the later repair moves the factor-degree review prompt to the same canonical card and deletes `FD-KPW3H`.

### FD-6WSIA duplicated the separable-extension definition

- **Object and need:** `D-JGYLA` and `FD-6WSIA` in `corpus/theory/Algebra`. Both cards defined separability of an algebraic field extension through separability of every element's minimal polynomial.

- **Observed evidence:** the definition blocks are equivalent; `FD-6WSIA` additionally proves the distinct criterion that an irreducible polynomial is separable exactly when its formal derivative is nonzero.

- **Impact and owner:** deleting the flashcard would discard useful mathematics, but retaining its definition would leave two owners for separable extension.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the two review prompts to `D-JGYLA` and converts `FD-6WSIA` to the proposition-only card “Irreducible separability criterion.”

### Duplicate projective-module cards D-RHJMK and FD-6XJ7D

- **Object and need:** `D-RHJMK` and `FD-6XJ7D` in `corpus/theory/Algebra`. Both define projective modules by the lifting property and prove that projective modules are exactly direct summands of free modules.

- **Observed evidence:** `D-RHJMK` contains the same lifting diagram and direct-summand proof and additionally records splitting of short exact sequences and exactness of `\Hom_R(P,-)`. The wiki and algebra guide displayed both cards.

- **Impact and owner:** the flashcard duplicates a strictly richer canonical card without preserving distinct mathematics.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the review prompt to `D-RHJMK`, removes duplicate reader-facing references, and deletes `FD-6XJ7D`.

### Duplicate maximal-ideal cards D-7XH2R and FD-CD2FE

- **Object and need:** `D-7XH2R` and `FD-CD2FE` in `corpus/theory/Algebra`. Both define a proper ideal to be maximal when no proper strictly larger ideal exists.

- **Observed evidence:** the complete definitions are mathematically identical.
  `D-7XH2R` is the dependency used throughout the ideal and local ring theory; `FD-CD2FE` is a migrated flashcard and the wiki displayed it beside the canonical card.

- **Impact and owner:** the duplicate flashcard adds no mathematics and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the review prompt to `D-7XH2R`, removes the duplicate wiki link, and deletes `FD-CD2FE`.

### Duplicate prime-ideal cards D-5BM46 and FD-OSSYR

- **Object and need:** `D-5BM46` and `FD-OSSYR` in `corpus/theory/Algebra`. Both define a proper ideal `$\mathfrak p$` of a commutative ring to be prime when `$ab\in\mathfrak p$` implies `$a\in\mathfrak p$` or `$b\in\mathfrak p$`.

- **Observed evidence:** the definitions are identical.
  `D-5BM46` is the dependency used by the prime spectrum, quotient criterion, and height theorems; the wiki displayed `FD-OSSYR` immediately beside it.

- **Impact and owner:** the flashcard adds no distinct mathematics and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the review prompt to `D-5BM46`, removes the duplicate wiki link, and deletes `FD-OSSYR`.

### Sign homomorphism used incompatible codomains under one symbol

- **Object and need:** `D-BZ3KD`, `D-TMME3`, and the permutation/determinant cards using `\sgn`. The canonical sign map must have one type.

- **Observed evidence:** `D-BZ3KD` defined `$\sgn:S_n\to\ZZ/2$` by transposition parity, and `D-TMME3` therefore used `$\sgn(\sigma)=0$` for even permutations.
  `FD-GHDF2`, `FD-X4DBP`, and the determinant formulas use the conventional multiplicative sign `$\sgn:S_n\to\{\pm1\}$`.

- **Impact and owner:** the same notation had two incompatible codomains, so links to the canonical sign definition did not type-check against formulas using it multiplicatively.

- **Uncertainty:** none.
  The parity map and multiplicative sign are equivalent via `$k\bmod2\mapsto(-1)^k$`, but they are not the same typed map.

- **Repair:** the same repair commit makes `D-BZ3KD` own the conventional multiplicative sign, updates `D-TMME3` to use sign `1` for even permutations, and links `FD-GHDF2` to the canonical definition.

### Duplicate alternating-group card FD-X4DBP

- **Object and need:** `D-TMME3` and `FD-X4DBP` in `corpus/theory/Algebra`. `D-TMME3` already defines even/odd permutations and the alternating group as the kernel of the sign homomorphism; `FD-X4DBP` repeats only the latter definition.

- **Observed evidence:** both complete cards state `$A_n=\ker(\sgn)=\{\sigma\in S_n:\sgn(\sigma)=1\}$`. The wiki and algebra guide displayed both cards adjacent to one another.

- **Impact and owner:** the flashcard adds no distinct mathematics and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the kernel review prompt to `D-TMME3`, removes duplicate reader-facing references, and deletes `FD-X4DBP`.

### Duplicate even/odd-permutation card FD-PIVQZ

- **Object and need:** `D-TMME3` and `FD-PIVQZ` in `corpus/theory/Algebra`. `D-TMME3` already owns the definition of even permutations and the alternating group; `FD-PIVQZ` repeats evenness and adds oddness plus the parity characterization.

- **Observed evidence:** after the sign convention repair, both use the same multiplicative sign `$S_n\to\{\pm1\}$`. The wiki and algebra guide exposed both recall units, and `FD-X4DBP` linked to the flashcard for “even.”

- **Impact and owner:** the duplicated evenness definition splits a basic permutation concept; the odd terminology and parity statement can be preserved on the canonical alternating-group card.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the prompt, odd definition, and parity remark to `D-TMME3`, redirects `FD-X4DBP`, removes duplicate reader-facing references, and deletes `FD-PIVQZ`.

### FD-CI4NB misclassified polynomial rings as a variant of rational-function fields

- **Object and need:** `FD-CI4NB`, Polynomial ring, and its relation to `FD-24RNF`, the field of rational functions.

- **Observed evidence:** the polynomial-ring card declared `variant-of: FD-24RNF`, although `$R[x]$` and `$K(x)$` are different constructions and the latter is the fraction field of `$K[x]$` when `$K$` is a field.
  The card also used `$K$` for an arbitrary commutative ring, making the coefficient type look field-specific.

- **Impact and owner:** the relation asserted mathematical equivalence where there is only a constructional relation, and the notation obscured the stated ring-level scope.

- **Uncertainty:** none after reading both cards.

- **Repair:** the same repair commit renames the coefficient ring `$R$`, uses the title `Polynomial ring $R[x]$`, and changes the relation to `related-to: FD-24RNF`.

### Duplicate characteristic-polynomial cards had inconsistent coefficient scope

- **Object and need:** `D-QFYAC` and `FD-GOB47` in `corpus/theory/Algebra`. Both define `$\det(xI-A)$`, but the canonical card unnecessarily restricted to matrices over a field while the flashcard used the correct commutative-ring scope.

- **Observed evidence:** the determinant definition makes sense over any commutative ring.
  The only field-specific content on `D-QFYAC` is its later Smith-normal-form remark over `$k[x]$`. The wiki and algebra guide displayed both definitions.

- **Impact and owner:** retaining both split a standard definition and made the canonical card less general than the duplicate.

- **Uncertainty:** none; characteristic polynomials are defined over arbitrary commutative coefficient rings, while Smith normal form here requires the field hypothesis.

- **Repair:** the same repair commit broadens `D-QFYAC` to a commutative ring, scopes its SNF remark to the field case, moves the review prompt there, removes duplicate reader-facing references, and deletes `FD-GOB47`.

### PR-4K4XZ unnecessarily restricted free-module torsionfreeness

- **Object and need:** `PR-4K4XZ`, Free modules over an integral domain are torsionfree.
  Its title asserted the general theorem while the body and slogan inserted finite generation.

- **Observed evidence:** the proposition read “Every finitely generated free `$R$`-module is torsionfree.”
  The proof of the standard statement is coordinatewise and does not use finite generation: a vector in a direct sum has finite support by definition.

- **Impact and owner:** the body understated its own title and could suggest finite generation is needed for torsionfreeness.

- **Uncertainty:** none.

- **Repair:** the same repair commit removes “finitely generated” from the proposition and slogan.

### PR-E4T3S repeated its quartic-Galois classification only as unlabeled screenshots

- **Object and need:** `PR-E4T3S`, Galois groups of irreducible quartics over `$\QQ$`. The proposition already states the complete discriminant/resolvent decision tree in authored text.

- **Observed evidence:** the closing remark appended two image-only summaries, `2021-08-09_14-48-55.png` and `2021-07-20_22-06-48.png`, with empty alt text and no mathematical content not already present in the proposition.

- **Impact and owner:** the duplicated decision procedure was inaccessible to text readers and depended on opaque legacy assets rather than authored corpus copy.

- **Uncertainty:** none; the textual proposition already enumerates every case.

- **Repair:** the same repair commit removes the two redundant screenshots and retains the distinct cycle-type remark for `$D_4$` versus `$C_4$`.

### Duplicate normal-extension cards D-LZTAK and FD-JJFZ3

- **Object and need:** `D-LZTAK` and `FD-JJFZ3` in `corpus/theory/Algebra`. Both define an algebraic extension to be normal when every irreducible polynomial with one root in the extension splits there.

- **Observed evidence:** the complete definitions are equivalent.
  `D-LZTAK` is the dependency used by Galois and splitting-field theory; `FD-JJFZ3` is a migrated flashcard, and one proposition plus the wiki/guide still linked to it.

- **Impact and owner:** the flashcard creates a second definition and splits dependencies for a basic Galois-theory concept.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** `D-LZTAK` remains the sole definition card.
  `FD-JJFZ3` is preserved as the distinct corollary that an irreducible polynomial over the base either has no root in a normal extension or splits completely there; the duplicated sentence is removed from `D-LZTAK`, and the remaining definition link on `PR-MHOVR` is redirected to `D-LZTAK`.

### Duplicate characteristic cards D-JNCUB and FD-LXZIW

- **Object and need:** `D-JNCUB` and `FD-LXZIW` in `corpus/theory/Algebra`. Both define the characteristic of a ring as the least positive `$n$` with `$n\cdot1_R=0$`, or `0` when no such integer exists.

- **Observed evidence:** the definitions are identical.
  `FD-LXZIW` adds the useful characterization as the nonnegative generator of the kernel of `$\ZZ\to R$`; `D-JNCUB` is the canonical dependency used by the field and separability theory.
  One problem card and a wiki page still linked to the flashcard duplicate.

- **Impact and owner:** the duplicate splits a basic ring invariant while the useful kernel characterization belongs naturally on the canonical card.

- **Uncertainty:** none after reading both complete cards; the older candidate `D-O26OY` is absent from the live tree.

- **Repair:** the same repair commit moves the review prompt and kernel characterization to `D-JNCUB`, redirects the problem-card reference, removes the duplicate wiki entry, and deletes `FD-LXZIW`.

### Duplicate Euclidean-domain cards D-NKRGN and FD-GXXBV

- **Object and need:** `D-NKRGN` and `FD-GXXBV` in `corpus/theory/Algebra`. Both define a Euclidean domain by a Euclidean function and the division-with-remainder inequality.

- **Observed evidence:** the only difference is that `D-NKRGN` defines the function on all of `$R$`, while `FD-GXXBV` defines it on `$R\setminus\{0\}$`; the Euclidean condition never requires a value at zero.
  The wiki and algebra guide displayed both cards.

- **Impact and owner:** the flashcard adds no mathematical distinction and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the review prompt to `D-NKRGN`, removes duplicate reader-facing references, and deletes `FD-GXXBV`.

### Duplicate elementary-divisor card FD-H764S

- **Object and need:** `D-JQNJQ` and `FD-H764S` in `corpus/theory/Algebra`. `D-JQNJQ` defines the elementary-divisor decomposition for all finitely generated abelian groups; `FD-H764S` restates the finite special case and names the same prime-power factors.

- **Observed evidence:** `FD-H764S` explicitly invokes `D-JQNJQ` and then reproduces the decomposition with free rank zero.
  The wiki and algebra guide displayed both cards.

- **Impact and owner:** the finite flashcard adds no distinct mathematics and creates a second definition of elementary divisors.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the finite-group review prompt to `D-JQNJQ`, removes duplicate reader-facing references, and deletes `FD-H764S`.

### Perfect-field definition, criterion, and finite-field corollary shared three owners

- **Object and need:** `D-KQFIV`, `PR-IK6AM`, and `FD-YYLYR` in `corpus/theory/Algebra`. The first two both stated the characteristic/Frobenius criterion, while `FD-YYLYR` independently defined perfect fields and repeated the same criterion.

- **Observed evidence:** `D-KQFIV` and `FD-YYLYR` gave equivalent definitions and overlapping proofs; `PR-IK6AM` restated the same criterion without a proof.
  Reader-facing links were split between `D-KQFIV` and `FD-YYLYR`.

- **Impact and owner:** the standard notion had two defining occurrences, and the Frobenius criterion had no single result card.

- **Uncertainty:** none after reading all three cards and their live references.

- **Repair:** `D-KQFIV` becomes the sole definition card and owns the equivalence with separability of finite extensions; `PR-IK6AM` owns the characteristic/Frobenius criterion and its proof; `FD-YYLYR` is preserved as the distinct corollary that finite fields are perfect.
  Live uses of the term link `D-KQFIV`, and the nearby wiki copy points to the criterion rather than restating it.

### Duplicate matrix-power counterexamples

- **Object and need:** `FE-ISVDM`, `FE-W56LS`, and later `FF-VKYM3` in `corpus/theory/Algebra`. They answer the same prompt about whether `$A^n=B^n$` forces `$A=B$`.

- **Observed evidence:** `FE-ISVDM` and `FE-W56LS` both use `$M=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$`, `$M^2=I$`, and `$M\ne I$`; `FE-W56LS` already declares itself `variant-of: FE-ISVDM`. `FF-VKYM3` gives the same claim with another square-root-of-`$-I$` example.
  All three examples only treated `$n=2$`, even though their body copy said “for `$n\ge2$`.”

- **Impact and owner:** one intrinsic counterexample question had multiple addresses, and the displayed witnesses did not justify the universal `$n\ge2$` wording.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the first repair retained `FE-ISVDM` and deleted `FE-W56LS`. The later repair replaces its witness by the rotation matrix through `$2\pi/n$`, which works for every `$n\ge2$`, redirects the remaining guide and wiki references, and deletes `FF-VKYM3`.

### FF-6MNV6 called a disjoint-cycle product a cycle and changed sign notation

- **Object and need:** `FF-6MNV6`, the worked sign computation for a permutation in `$S_{18}$`.

- **Observed evidence:** the review prompt called `$(123456)(789)(10~11)(12~13~14~15)(16~17~18)$` “the cycle,” although it is a product of five disjoint cycles.
  The body also denoted sign by `$\varepsilon$` while the canonical sign homomorphism is `\sgn` on `D-BZ3KD`.

- **Impact and owner:** the prompt misstated the object type and the worked example drifted from the corpus's canonical sign notation.

- **Uncertainty:** none.

- **Repair:** the same repair commit says “permutation,” links the canonical sign card, and uses `\sgn` throughout the computation.

### FF-7U6UY had malformed and underspecified review copy

- **Object and need:** `FF-7U6UY`, the Jacobson-radical fact.
  Its review prompt should name the invariant in ordinary notation and scope the geometric interpretation to the hypotheses used by the card.

- **Observed evidence:** the prompt read `What is ${J ({R}) }$? How is it interpreted geometrically?`, while the geometric remark specifically uses a finitely generated algebra over an algebraically closed field.

- **Impact and owner:** the prompt exposed malformed legacy TeX and asked a broader geometric question than the answer on the card supports.

- **Uncertainty:** none.

- **Repair:** the same repair commit writes `$J(R)$` normally and states the finite-type/algebraically-closed scope in the prompt.

### Regular rings had two defining cards across Algebra and Algebraic Geometry

- **Object and need:** `D-DEFREGLR` and `FF-CQSNC`. Both cards defined regular local rings by the equality `$\dim R=\dim_k\mfm/\mfm^2$`, and both defined regular rings by regularity of all prime localizations.

- **Observed evidence:** `D-DEFREGLR` is the existing definition card used by the scheme-theory material.
  `FF-CQSNC` independently introduced the same definitions before applying Nakayama to identify the vector-space dimension with the minimal number of generators of `\mfm`.

- **Impact and owner:** the duplicate defining occurrences split one standard commutative-algebra concept across areas.
  The Nakayama/embedding-dimension observation is distinct and should remain available without redefining the term.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit makes `D-DEFREGLR` explicitly own `regular ring`, moves the review prompt there, and converts `FF-CQSNC` to the proposition “Embedding dimension criterion for regular local rings.”

### FF-ESIOA named only the nonzerodivisor corollary as Hauptidealsatz

- **Object and need:** `FF-ESIOA` and the canonical principal-ideal theorem on `PR-VARHT`.

- **Observed evidence:** `FF-ESIOA` was titled “Krull's Hauptidealsatz” but assumed the generator was a nonunit nonzerodivisor and concluded height exactly `1`. The actual principal ideal theorem says every prime minimal over a principal ideal has height at most `1`; exact height `1` is the stated corollary under the extra nonzerodivisor hypothesis.
  `PR-VARHT` already owns both statements.

- **Impact and owner:** the Algebra card mislabeled a strengthened corollary as the theorem itself, and `FF-CQSNC` linked to it when invoking Krull's height theorem.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit retitles `FF-ESIOA` as the nonzerodivisor corollary, links it to `PR-VARHT`, and redirects the height-theorem reference on `FF-CQSNC` to the canonical theorem card.

### Duplicate lying-over/going-up cards FF-IBDAT and PR-RJ3P7

- **Object and need:** `FF-IBDAT` and `PR-RJ3P7`. Both state lying over for integral extensions and the going-up theorem for chains of prime ideals.

- **Observed evidence:** the Algebra card is exactly the two algebraic clauses already contained in the first theorem block of `PR-RJ3P7`; the latter also proves closedness and states going down.
  The Algebra wiki and guide pointed to `FF-IBDAT`, while the algebraic-geometry wiki pointed to `PR-RJ3P7`.

- **Impact and owner:** one standard theorem had two intrinsic addresses split by subject area, with no mathematical or source-appearance distinction.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the plain “What is going up?”
  prompt to `PR-RJ3P7`, redirects the Algebra wiki and guide, and deletes `FF-IBDAT`.

### Krull's maximal-ideal theorem had three intrinsic cards

- **Object and need:** `PR-UTFSY`, `T-QSTRJ`, and `FF-QELG7` in `corpus/theory/Algebra`. All three state that every proper ideal is contained in a maximal ideal.

- **Observed evidence:** `PR-UTFSY` gives the full Zorn proof for arbitrary unital rings; `T-QSTRJ` states the same theorem without proof; `FF-QELG7` repeats it for commutative rings with the same Zorn proof and contributes the review prompt.
  The wiki and algebra guide displayed all three together.

- **Impact and owner:** one standard theorem had three canonical-looking addresses, and a downstream Jacobson-radical proof linked to the flashcard duplicate.

- **Uncertainty:** none after reading all three complete cards.

- **Repair:** the same repair commit keeps `PR-UTFSY`, gives it the Krull title and review prompt, redirects all live references, and deletes `T-QSTRJ` and `FF-QELG7`.

### Duplicate Eisenstein theorem cards FT-2P5VV and T-CF6S3

- **Object and need:** `FT-2P5VV` and `T-CF6S3` in `corpus/theory/Algebra`. Both state Eisenstein's criterion for `$f\in\ZZ[x]$` and prove it by Gauss's lemma and reduction modulo `$p$`.

- **Observed evidence:** the hypotheses and proof are the same.
  `T-CF6S3` additionally records the primitive-polynomial consequence giving irreducibility in `$\ZZ[x]$`; `FT-2P5VV` contributes only the review prompt.
  The Galois-theory wiki and algebra guide displayed both.

- **Impact and owner:** one standard irreducibility criterion had two theorem addresses, while the richer card strictly contains the other.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the review prompt to `T-CF6S3`, redirects the remaining theorem link, removes duplicate reader-facing references, and deletes `FT-2P5VV`.

### Gauss's lemma was split across two theorem cards

- **Object and need:** `FT-OXN3Y` and `T-JEZZY` in `corpus/theory/Algebra`. Both are standard forms of Gauss's lemma rather than genuinely separate theorems.

- **Observed evidence:** `FT-OXN3Y` states that a factorization in the fraction field descends to `$R[x]$` with the same factor degrees; `T-JEZZY` gives the primitive-polynomial irreducibility equivalence and the sharper scalar rescaling statement.
  The wiki and algebra guide displayed both together.

- **Impact and owner:** one theorem was split between two addresses, and a Hartshorne collection card linked specifically to the weaker half.

- **Uncertainty:** none after reading both cards; the two forms are standard parts of the same Gauss lemma.

- **Repair:** the same repair commit merges both forms and the polynomial-UFD consequence onto `T-JEZZY`, moves the review prompt there, redirects all live references, and deletes `FT-OXN3Y`.

### PR-25FLW's title was broader than its theorem statement

- **Object and need:** `PR-25FLW`, “Algebraic extensions of perfect fields are separable.”
  The body should state the perfect-field theorem named by the title.

- **Observed evidence:** the proposition assumed only “characteristic zero or finite,” then immediately proved the result by observing that such a field is perfect.
  The same proof works for every perfect field by definition.

- **Impact and owner:** the title promised the general theorem while the body exposed only two sufficient subclasses.

- **Uncertainty:** none; `D-KQFIV` defines perfectness by separability of all irreducible polynomials.

- **Repair:** the same repair commit assumes `$k$` perfect, adds the canonical dependency, and retains characteristic-zero and finite fields as explicit examples.

### Duplicate reduced-ring card FF-U4FHF

- **Object and need:** `D-PQHHJ` and `FF-U4FHF` in `corpus/theory/Algebra`. Both say that a ring is reduced exactly when it has no nonzero nilpotent elements.

- **Observed evidence:** `D-PQHHJ` is the canonical definition used by the radical-ideal quotient criterion; `FF-U4FHF` repeats it for commutative rings and adds only the review prompt and the equivalent nilradical formulation.
  The wiki and algebra guide displayed both.

- **Impact and owner:** the flashcard adds no independent mathematics and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the prompt and commutative nilradical equivalence to `D-PQHHJ`, removes duplicate reader-facing references, and deletes `FF-U4FHF`.

### Duplicate stabilizer card FD-IGEOR

- **Object and need:** `D-WYC7C` and `FD-IGEOR` in `corpus/theory/Algebra`. `D-WYC7C` already defines the stabilizer `$G_x$`; `FD-IGEOR` repeats that definition and adds only prompts plus the proof that `$G_x$` is a subgroup.

- **Observed evidence:** both complete cards use `$G_x=\{g\in G\mid g\cdot x=x\}$`. The canonical action card is the dependency used throughout orbit–stabilizer theory, while the wiki and algebra guide displayed the flashcard as an additional recall unit.

- **Impact and owner:** the duplicated definition splits a basic group-action concept, while the subgroup fact belongs naturally on the canonical card.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the two prompts and subgroup proposition/proof to `D-WYC7C`, removes duplicate reader-facing references, and deletes `FD-IGEOR`.

### Duplicate subset-centralizer card FD-SSR6N

- **Object and need:** `D-PX64W` and `FD-SSR6N` in `corpus/theory/Algebra`. `D-PX64W` already defines the centralizer of an arbitrary subset; `FD-SSR6N` repeats the same condition with notation `$Z_G(S)$`.

- **Observed evidence:** both cards define the subgroup of `$g\in G$` that satisfy `$gsg^{-1}=s$` for every `$s\in S$`. The wiki displayed the flashcard beside the canonical centralizer card.

- **Impact and owner:** the flashcard adds no distinct mathematics and creates a second defining occurrence for subset centralizers.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the review prompt to `D-PX64W`, removes the duplicate wiki link, and deletes `FD-SSR6N`.

### Duplicate transitive-action cards D-KGGWK and FD-KSKDG

- **Object and need:** `D-KGGWK` and `FD-KSKDG` in `corpus/theory/Algebra`. Both define transitivity of a group action by the condition that for every `$x,y\in X$` some `$g\in G$` satisfies `$g\cdot x=y$`.

- **Observed evidence:** the definitions are identical.
  `D-KGGWK` is the dependency used by transitive subgroups, covering-space theory, and the canonical group-action card; the wiki displayed `FD-KSKDG` beside it.

- **Impact and owner:** the flashcard adds no distinct mathematics and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** the same repair commit moves the review prompt to `D-KGGWK`, removes the duplicate wiki link, and deletes `FD-KSKDG`.

### FD-J3HIA treated $K(\alpha)$ as a variant of $K[\alpha]$

- **Object and need:** `FD-J3HIA`, generated subfield `$K(\alpha)$`, and `FD-3V3ZW`, generated subring `$K[\alpha]$`.

- **Observed evidence:** `FD-J3HIA` declared `variant-of: FD-3V3ZW`, although the two constructions differ for transcendental `$\alpha$`.

- **Impact and owner:** the relation asserted equivalence between a subfield and a subring construction.
  Equality requires the additional hypothesis that `$\alpha$` is algebraic over `$K$`.

- **Uncertainty:** none.

- **Repair:** the same repair commit changes the edge to `related-to` and records `$K[\alpha]\subseteq K(\alpha)$`, equality for algebraic `$\alpha$`, and the polynomial/rational-function distinction in the transcendental case.

### Duplicate generated-subfield card FD-QPNDA

- **Object and need:** `FD-J3HIA` and `FD-QPNDA` in `corpus/theory/Algebra`. Both define `$K(\alpha)$` as the smallest subfield of an ambient extension containing `$K$` and `$\alpha$`.

- **Observed evidence:** the definition bodies are identical.
  `FD-QPNDA` declared itself `variant-of: FD-J3HIA` and also repeated the already-false `variant-of: FD-3V3ZW` edge to the generated subring `$K[\alpha]$`. The wiki and algebra guide exposed both generated-subfield cards.

- **Impact and owner:** the duplicate adds no mathematics and reintroduces the subfield/subring conflation repaired on `FD-J3HIA`.

- **Uncertainty:** none after reading both complete generated-subfield cards.

- **Repair:** the same repair commit moves the additional review prompt to `FD-J3HIA`, removes duplicate reader-facing references, and deletes `FD-QPNDA`.

### Berkeley Spring 2016 Problem 6B has the least-squares sign reversed

- **Object and need:** `P-BKS16-6B` in `SRC-BERKELEY-PRELIM-SPRING-2016`. The printed problem asks for the sign of `$A^T(y-Ax)$` at a nonnegative least-squares minimizer.

- **Observed evidence:** `Sp16_Exam.pdf` states that `$A^T(y-Ax)$` has nonnegative entries.
  The vendored `Sp16_Solutions.pdf` instead argues by assuming a negative entry of `$A^T(Ax-y)$` and decreasing the objective, which proves `$A^T(Ax-y)\geq0$`, equivalently `$A^T(y-Ax)\leq0$`.

- **Impact and owner:** the exam statement is false as printed.
  For example, with `$A=[1]$`, `$y=-1$`, the feasible minimizer is `$x=0$` but `$A^T(y-Ax)=-1$`. The problem card correctly preserves the source wording, so the solution must identify the source error rather than silently reverse the statement.

- **Uncertainty:** none; the one-dimensional counterexample and the supplied solution agree on the corrected sign.

- **Repair:** the solution on `P-BKS16-6B` gives the counterexample and proves the corrected coordinatewise inequality `$A^T(y-Ax)\leq0$`, while a remark records the discrepancy with the source solution.

### GRE Chapter 2 Problem 21 solution omits the critical point $x=\pi$

- **Object and need:** `P-GRECH2-21` in `SRC-GRE-MATH-CH2-REVIEW`. A solution locating the local maximum of `$f(x)=\int_x^{2x}(\sin t/t)\,dt$` on `$(0,3\pi/2)$` must identify all critical points in that interval before classifying them.

- **Observed evidence:** the retained Chapter 8 solution correctly derives `$f'(x)=\sin x(2\cos x-1)/x$`, then states that `\sin x=0` or `\cos x=1/2` implies only `$x=\pi/3$` in the interval and consequently claims that `$f$` has only one critical point there.
  However `$x=\pi$` also lies in `$(0,3\pi/2)$` and satisfies `\sin x=0`.

- **Impact and owner:** the source reasoning omits a genuine critical point.
  The final answer remains correct: `$f'$` changes from positive to negative at `$\pi/3$`, giving the local maximum, and from negative to positive at `$\pi$`, giving a local minimum.

- **Uncertainty:** none; the derivative formula and the missing root `$\sin\pi=0$` are explicit.

- **Repair:** the authored solution on `P-GRECH2-21` lists both critical points and classifies them by the sign of `$f'$`; retain this entry as source-solution errata.

### GRE Chapter 2 Problem 32 omitted the figure that defines the region

- **Object and need:** `P-GRECH2-32` in `SRC-GRE-MATH-CH2-REVIEW`. The problem asks for the polar-area expression of a shaded region bounded by two circles, so the circle equations and the shaded side of their boundaries must be present on the card.

- **Observed evidence:** both checked Markdown extractions refer to an image but do not retain it, and the card consequently said only “pictured below” while displaying no figure.
  Direct inspection of page 110 of the retained book PDF (printed page 100) shows the circles labeled `$r=\sqrt3\sin\theta$` and `$r=3\cos\theta$`, with their common lens in the first quadrant shaded.

- **Impact and owner:** without the figure, the card did not determine which region bounded by the two circles was intended.
  The mathematical data are recoverable exactly from the retained source page and belong in the problem statement rather than in a missing image reference.

- **Uncertainty:** none after direct inspection of the retained PDF page.

- **Repair:** `P-GRECH2-32` now states the two polar equations and identifies their common first-quadrant region in text; its solution derives the source answer from those data.

## Workflow and rendering papercuts

### Overlapping workstream owners edited the same Author-solutions card

- **Object and need:** the `new-qual-site` Core2 workstream must have one active author on its selected card, under `QUAL-03` and `QUAL-07`.

- **Observed evidence:** on 2026-09-22, repeated successful `workstream` continuation calls were followed by `WORKSTREAM_SETUP_REQUIRED` on calls carrying the returned ID. One response explicitly reported a superseded owner's already-admitted call still settling.
  During the same session, `1b56ef019` committed `P-BERK90S-07` with this session's partial solution followed by another complete solution; subsequent edits completed the first block, producing two proofs of the same integral by the same method.

- **Impact and owner:** the workstream handoff/dispatch boundary permits overlapping authorship and rejected calls.
  This is not a corpus parser, mathematical, or publication-gate defect.

- **Uncertainty:** the rejected calls and overlapping card contents were observed directly; the mechanism initiating the competing continuations has not been established.

- **Repair:** the card is reconciled by removing this session's duplicate and retaining the other complete proof unchanged.
  The external handoff remains unresolved: a successor must not race a still-writing predecessor, and must reread the final settled card before editing it.

### PR-E6VI4 duplicated the smallest-prime-index normality theorem

- **Object and need:** `PR-E6VI4` and `PR-PADL7` in `corpus/theory/Algebra`. Both stated that a subgroup whose index is the smallest prime dividing the group order is normal.

- **Observed evidence:** the two cards had the same title, slogan, hypotheses, conclusion, and coset-action proof.
  `PR-E6VI4` differed only by a `variant-of: PR-PADL7` relation.

- **Impact and owner:** the duplicate violated the single-defining-occurrence policy while the underlying coset-action proof contains a distinct structural statement: the action kernel is exactly the subgroup.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** `PR-PADL7` remains the normality theorem.
  `PR-E6VI4` is rewritten as the distinct proposition identifying the kernel of the coset action, and its relation becomes `related-to`.

### PR-EDD7U bundled the rational root theorem into an unrelated matrix card

- **Object and need:** `PR-EDD7U`, Characteristic polynomials via traces of exterior powers.
  After its matrix proposition and example, the same card contained the rational root theorem and a polynomial-division remark.

- **Observed evidence:** the rational-root statement has independent hypotheses, notation, applications, and subject matter; the Galois guide also restated it in prose, while the minimal-polynomial page used it by name.

- **Impact and owner:** one card had two unrelated primary propositions, and the rational root theorem had no independent address for the pages that use it.

- **Uncertainty:** none after reading the complete card and both reader-facing uses.

- **Repair:** `PR-EDD7U` is restricted to the characteristic-polynomial proposition and its example.
  The rational root theorem moves intact to `PR-RRTST`, with its proof and polynomial-division remark, and reader-facing uses link that canonical card.

### PR-LJE4C's title omitted half of the card's stated theorem

- **Object and need:** `PR-LJE4C` in `corpus/theory/Algebra`. Its title named only the ideal correspondence theorem.

- **Observed evidence:** the proposition also states the subring correspondence and the third isomorphism theorem `((R/I)/(J/I)) \cong R/J`.

- **Impact and owner:** the title did not name the full mathematical unit on the card and made the iterated-quotient theorem invisible in card lists.

- **Uncertainty:** none after reading the complete proposition.

- **Repair:** retitle the card “Correspondence and third isomorphism theorems for quotient rings”; the existing slogan already names both components.

### PR-JLDJ6 defined the Möbius function inside a cyclotomic proposition

- **Object and need:** `PR-JLDJ6` in `corpus/theory/Algebra`. Its cyclotomic formula introduced the Möbius function by an inline three-case definition.

- **Observed evidence:** no Möbius-function definition card existed anywhere in the corpus, while the proposition uses `\mu` as named mathematical data.

- **Impact and owner:** the function was defined in running proposition copy rather than at an addressable definition, and the recursive formula wrote polynomial division as multiplication by an untyped inverse.

- **Uncertainty:** none after searching the full corpus and wiki for the number-theoretic Möbius function.

- **Repair:** add `D-6V3PZ`, which defines the Möbius function and records its basic divisor-sum identity; link it from `PR-JLDJ6` and write the recursive cyclotomic formula as an explicit quotient.

### PR-MK2W6 restated the definition of a perfect field as a proposition

- **Object and need:** `PR-MK2W6` in `corpus/theory/Algebra`.

- **Observed evidence:** after `D-KQFIV` became the sole definition card, `PR-MK2W6` said only that irreducible polynomials over a perfect field are separable, which is exactly the defining condition.
  Its distinct content was the imperfect-field example `x^p-t` over `\FF_p(t)`.

- **Impact and owner:** the proposition created a second statement of the definition while the example had no card-level identity of its own.

- **Uncertainty:** none after reading the definition, proposition, and example.

- **Repair:** preserve `PR-MK2W6` as an example card for the irreducible inseparable polynomial `x^p-t`, and supply the irreducibility and inseparability proof instead of restating perfectness.

### PR-N6S6P bundled unrelated automorphism, Hom, and semidirect-product results

- **Object and need:** `PR-N6S6P` in `corpus/theory/Algebra`.

- **Observed evidence:** parts (a)--(e) concern automorphisms of finite cyclic groups, but parts (f)--(i) separately state automorphisms of $C_m^n$, the order of $\GL_n(\FF_p)$, the count of $\Hom(C_n,C_m)$, an isomorphism criterion for semidirect products, and $\Inn(G)\cong G/Z(G)$.

- **Impact and owner:** several independently reusable theorems had no independent addresses and were hidden under a cyclic-group title.

- **Uncertainty:** none after reading the complete card and searching the Algebra theory corpus for the four statements.

- **Repair:** keep `PR-N6S6P` for cyclic-group automorphisms and extract the independent results to their own proposition cards.
  The first extraction is `PR-IN9ZP`, which owns the inner-automorphism quotient theorem.
  `PR-SD8CY` now owns the semidirect-product action-change theorem and its canonical-form remark.
  `PR-HM7QK` now owns the count of homomorphisms between finite cyclic groups.
  `PR-6JQ2M` now owns automorphisms of $C_m^n$ and the order of $\GL_n(\FF_p)`, leaving `PR-N6S6P` focused on finite cyclic groups.

### PR-O5YUI duplicated the canonical tensor--Hom isomorphism

- **Object and need:** `PR-O5YUI` and `PR-LPJLD` in `corpus/theory/Algebra` stated the same canonical isomorphism `$V^*\otimes_k W\cong\Hom_k(V,W)$` under the same finite-dimensional hypotheses.

- **Observed evidence:** `PR-O5YUI` differed only by carrying the basis proof and a `variant-of: PR-LPJLD` relation.

- **Impact and owner:** the same theorem had two proposition addresses, while the useful matrix-unit description in the proof had no statement of its own.

- **Uncertainty:** none after reading both cards.

- **Repair:** keep `PR-LPJLD` as the canonical isomorphism and rewrite `PR-O5YUI` as the distinct basis-level proposition sending `$e_i^*\otimes f_j$` to matrix units and giving the explicit inverse.

### PR-TGFTL duplicated the canonical trace-pairing isomorphism

- **Object and need:** `PR-TGFTL` and `PR-GXII2` in `corpus/theory/Algebra` had identical titles and identical isomorphism statements for the trace pairing between opposite Hom spaces.

- **Observed evidence:** `PR-TGFTL` declared `variant-of: PR-GXII2` and added only the matrix-unit proof.

- **Impact and owner:** the trace-pairing theorem had two addresses while the useful coordinate duality exhibited by the proof had none.

- **Uncertainty:** none after reading both cards.

- **Repair:** keep `PR-GXII2` as the canonical trace-pairing isomorphism and rewrite `PR-TGFTL` as the distinct matrix-unit duality proposition, with a `related-to` relation.

### GRE Chapter 2 answer 38 gives the wrong exceptional exponent

- **Object and need:** the external answer to Chapter 2 review question 38 in `assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md`, used when reviewing `P-GRECH2-38`.

- **Observed evidence:** after substituting $u=\log x$, the source writes $\int u^{-n}\,du$ with the power-rule branch for $n\ne-1$ and the logarithmic branch for $n=-1$.
  The logarithmic exceptional case is instead $n=1$.

- **Impact and owner:** the source solution contains a mathematical typo in its antiderivative case split.
  The corpus solution must not reproduce it.

- **Expected result:** the authored proof treats $n=1$ as the exceptional case and derives convergence exactly for $n>1$.

- **Uncertainty:** none.

- **Repair:** `P-GRECH2-38` handles $n=1$ separately and derives $\int_e^\infty dx/(x(\log x)^n)=1/(n-1)$ for the convergent range; the external source is left unchanged.

### GRE Chapter 2 question 42 asks for the wrong extremum

- **Object and need:** `P-GRECH2-42` and Chapter 2 review question 42 in `Cracking the GRE Mathematics Subject Test`.

- **Observed evidence:** the source asks for the *smallest* $b$ such that every $0\le a<b$ gives convergence, while its Chapter 8 solution derives convergence for $0\le a<4$ and selects (E), $b=4$.
  Every positive $b\le4$ therefore satisfies the literal implication, so $4$ is not its smallest solution.

- **Impact and owner:** the source problem is mathematically ill-posed as a threshold question.
  Among the listed choices, (A), $b=1$, satisfies the literal request; the supplied answer (E) is the largest convergence threshold.

- **Expected result:** preserve the source wording but make the authored solution distinguish the literal statement from the intended maximal threshold.

- **Uncertainty:** none; the question wording agrees in both source extractions, and the source's own ratio-test solution explicitly selects $b=4$ as the threshold.

- **Repair:** `P-GRECH2-42` proves the convergence range, proves that $4$ is the largest threshold, and records why the literal word “smallest” cannot yield the source's answer.

### GRE Chapter 2 answer 49 conflates Taylor degree with number of terms

- **Object and need:** `P-GRECH2-49` and the Chapter 8 answer to Chapter 2 review question 49 in `Cracking the GRE Mathematics Subject Test`.

- **Observed evidence:** the question asks for the minimum number of Taylor terms.
  The source answer labels (C), $5$, but its proof introduces the degree-$n$ Taylor polynomial $P_n$ and concludes that $n=5$ is the minimum degree.
  A degree-$5$ Taylor polynomial contains the six terms indexed $0,1,\ldots,5$.

- **Impact and owner:** the supplied answer is off by one.
  Five terms leave an error greater than the first omitted term $1/(5^5 5!)=1/375000>10^{-6}$, whereas six terms have error less than $10^{-6}$.
  The literal correct choice is (D), $6$.

- **Expected result:** distinguish polynomial degree from number of terms and prove the minimal term count directly.

- **Uncertainty:** none; the question wording explicitly asks for terms, and the source solution explicitly establishes degree $5$.

- **Repair:** `P-GRECH2-49` proves that five terms are insufficient and six terms suffice, and selects (D). The external source is left unchanged.

### GRE Chapter 7 question 21 prints a second non-tautology in choice (E)

- **Object and need:** `P-GRECH7-21` and Chapter 7 review question 21 in `Cracking the GRE Mathematics Subject Test`. The multiple-choice problem asks for the unique formula that is not a tautology.

- **Observed evidence:** direct inspection of page 5 of the retained `assets/attachments/Chapter-7.pdf` shows choice (E) printed as `$A\lor(B\land C)\leftrightarrow(A\land B)\lor(A\land C)$`. With `$A$` true and `$B,C$` false, its left side is true and its right side is false, so (E) is not a tautology.
  Choice (C) is also not a tautology: with the same assignment, `$(A\land B)\to C$` is true while `$A\to(B\lor C)$` is false.
  The Chapter 8 solution nevertheless labels (C) as the answer and calls (E) the distributive property.

- **Impact and owner:** the printed source problem has two correct choices.
  The distributive law evidently intended in (E) is `$A\lor(B\land C)\leftrightarrow(A\lor B)\land(A\lor C)$`; with that correction, (C) is the unique non-tautology.

- **Expected result:** preserve the source-faithful choices on the card, prove that both printed (C) and (E) fail, and identify the corrected distributive formula that recovers the source's intended answer (C).

- **Uncertainty:** none; the retained PDF scan, both extracted copies, the explicit truth assignments, and the source's own description of (E) as the distributive property agree on the defect and intended correction.

- **Repair:** `P-GRECH7-21` records the literal two-answer defect, supplies counterexamples for (C) and (E), and states the corrected distributive law; the external source is left unchanged.

### GRE Chapter 7 answer 22 incorrectly rejects an isomorphic graph

- **Object and need:** `P-GRECH7-22` and Chapter 7 review question 22 in `Cracking the GRE Mathematics Subject Test`. The question asks which of three drawn graphs are mutually isomorphic.

- **Observed evidence:** direct inspection of page 5 of `assets/attachments/Chapter-7.pdf` gives edge sets `$E(I)=\{AB,BC,CD\}$`, `$E(II)=\{FG,FH,EG\}$`, and `$E(III)=\{JK,KL,LM\}$`. The crossing of the two diagonal edges in Graph II is not a vertex; its only vertices are the labeled `$E,F,G,H$`. The bijection `$A\mapsto E$, `$B\mapsto G$, `$C\mapsto F$, `$D\mapsto H$` sends the three edges of I to `$EG,GF,FH$`, exactly the edges of II. The Chapter 8 solution rejects I versus II only because the different trial bijection `$A\mapsto E$, `$B\mapsto F$, `$C\mapsto G$, `$D\mapsto H$` fails.

- **Impact and owner:** the source answer (C), “I and III only,” is false.
  Failure of one candidate bijection does not prove nonisomorphism; all three drawn graphs are copies of the path on four vertices, so the correct choice is (E), “I, II, and III.”

- **Expected result:** use an explicit adjacency-preserving bijection to prove I is isomorphic to II and to III, and select (E).

- **Uncertainty:** none; the retained scan shows the complete drawings and the explicit bijections can be checked edge by edge.

- **Repair:** `P-GRECH7-22` records the edge sets, gives explicit isomorphisms, and selects (E); the external source is left unchanged.

### GRE Chapter 7 question 32 cannot define a probability density as printed

- **Object and need:** `P-GRECH7-32` and Chapter 7 review question 32 in `Cracking the GRE Mathematics Subject Test`. The problem asks for a constant `$c$` making a piecewise linear function a probability density.

- **Observed evidence:** direct inspection of page 7 of `assets/attachments/Chapter-7.pdf` shows the first branch printed as `$x/2+c$` under the condition `$0\le t\le8$`, even though the function is written `$f(x)$`. Reading the evident variable typo as `$0\le x\le8$`, normalization requires `$1=\int_0^8(x/2+c)\,dx=16+8c$`, hence `$c=-15/8$`; then `$f(0)=-15/8<0$`, so the result is not a density.
  Conversely any `$c\ge0$` makes the integral at least `$16$`. The Chapter 8 solution instead writes `$[x^2/4+cx]_0^8=64/4+6c$` and selects (E), `$c=-4/3$`; both the coefficient of `$c$` and the resulting algebra are incorrect.

- **Impact and owner:** the literal piecewise formula is malformed because its branch condition uses an unrelated variable, and the evident corrected problem has no real solution.
  None of the five answer choices can make the function a probability density.

- **Expected result:** preserve the source wording, explain the variable typo, prove that normalization and nonnegativity are incompatible under the natural `$x$`-support interpretation, and do not reproduce the supplied answer.

- **Uncertainty:** none; the retained scan confirms the printed formula and interval, while the two defining density conditions give a direct contradiction for every real `$c$`.

- **Repair:** `P-GRECH7-32` proves that no real `$c$` works and records why the source answer `$-4/3$` fails both normalization and nonnegativity; the external source is left unchanged.

### GRE Chapter 7 question 35 does not specify whether the committees are distinguished

- **Object and need:** `P-GRECH7-35` and Chapter 7 review question 35 in `Cracking the GRE Mathematics Subject Test`. The problem asks for the number of ways to separate 12 employees into four equally-sized committees.

- **Observed evidence:** the printed question supplies no committee names, tasks, or labels.
  If the four three-person committees are unlabeled, the number of set partitions is `$12!/((3!)^4 4!)=15,400$`, which is not an answer choice.
  The Chapter 8 solution instead computes `$\binom{12}{3}\binom{9}{3}\binom{6}{3}\binom{3}{3}=369,600$` and explains that it matters which committee each employee joins, thereby treating the committees as distinguished.

- **Impact and owner:** the source statement is ambiguous between the standard unlabeled-partition count and the labeled-committee count.
  Its supplied answer (A) is correct only under the latter convention.

- **Expected result:** distinguish the two conventions mathematically, give both counts, and identify (A) as the intended answer under the convention explicitly used by the source solution.

- **Uncertainty:** the counting under each convention is exact; the only uncertainty is the convention omitted from the problem statement.

- **Repair:** `P-GRECH7-35` proves both counts and states the source's intended distinguished-committee answer without silently treating the wording as unambiguous; the external source is left unchanged.

### GRE Chapter 7 question 38 uses decreasing “distribution functions” and omits independence

- **Object and need:** `P-GRECH7-38` and Chapter 7 review question 38 in `Cracking the GRE Mathematics Subject Test`. The problem asks for the probability that at least one of two random variables exceeds $2$.

- **Observed evidence:** direct inspection of page 9 of `assets/attachments/Chapter-7.pdf` prints `$F_X(t)=1/3^t$` and `$F_Y(t)=1/4^t$` and calls them distribution functions.
  These are decreasing on the positive integers, so they cannot be cumulative distribution functions.
  The Chapter 8 solution instead uses `$P(X\le2)=1-1/9$` and `$P(Y\le2)=1-1/16$`, which treats the printed quantities as survival probabilities.
  It then multiplies those probabilities on the assertion that `$X$` and `$Y$` are independent, although independence is absent from the problem statement.

- **Impact and owner:** the printed marginal functions are mislabeled, and even after interpreting them as tail probabilities the requested union probability is not determined by the marginals without a joint-distribution assumption.
  The supplied answer `$1/6$` follows only after both corrections: tail-function interpretation and independence.

- **Expected result:** identify the cumulative-distribution defect, distinguish marginal information from a joint law, and compute `$1/6$` only under the source's implicit independence assumption.

- **Uncertainty:** none about either defect; monotonicity rules out the printed cumulative-distribution interpretation, and the union formula explicitly depends on `$P(X>2,Y>2)$`, which the marginals do not determine.

- **Repair:** `P-GRECH7-38` proves the two defects and derives choice (E) under the source's two implicit corrections; the external source is left unchanged.

### GRE Chapter 7 question 44 prints ten flips and supplies the wrong answer even for one hundred

- **Object and need:** `P-GRECH7-44` and Chapter 7 review question 44 in `Cracking the GRE Mathematics Subject Test`. The problem asks for the probability of obtaining between 40 and 50 heads.

- **Observed evidence:** direct inspection of page 10 of `assets/attachments/Chapter-7.pdf` shows “A fair coin is flipped 10 times,” so the literal event is impossible and has probability zero.
  The Chapter 8 solution silently changes the experiment to 100 flips and supplies choice (D), 47%. For 100 fair flips the exact probability is `$2^{-100}\sum_{k=40}^{50}\binom{100}{k}\approx0.5221945186$`, whose closest listed percentage is 53%, choice (E). The source's own stated continuity correction gives standardized limits `-2.1` and `0.1`, for which `$\Phi(0.1)-\Phi(-2.1)\approx0.5219$`, again near 52%, not 47%.

- **Impact and owner:** the printed problem has no listed answer.
  Correcting the evident “10” typo to “100” still does not recover the supplied answer; the correct multiple-choice selection for the corrected problem is (E).

- **Expected result:** solve the ten-flip statement literally, then separately solve the evident 100-flip correction exactly and check the normal approximation rather than laundering the source's 47% answer.

- **Uncertainty:** none; the retained scan fixes the printed trial count and the corrected binomial probability is an exact finite sum.

- **Repair:** `P-GRECH7-44` records probability zero for the printed problem and derives approximately 52.219% for 100 flips, selecting (E) under the evident correction; the external source is left unchanged.

### GRE Chapter 7 question 46 has corrupted duplicate answer choices

- **Object and need:** `P-GRECH7-46` and Chapter 7 review question 46 in `Cracking the GRE Mathematics Subject Test`. The problem asks for all complex solutions of `$\cos z=3$`.

- **Observed evidence:** direct high-resolution inspection of page 10 of `assets/attachments/Chapter-7.pdf` shows `$\sqrt{2i}$` in every printed choice.
  Choices (B) and (C) are identical, while (A), (D), and (E) are identical.
  Solving the equation gives `$e^{iz}=3\pm2\sqrt2$` and hence `$z=2k\pi-i\log(3\pm2\sqrt2)$`. The Chapter 8 solution derives exactly this formula and labels it choice (C), despite the printed (C) containing `$\sqrt{2i}$`.

- **Impact and owner:** none of the printed answer choices matches the actual solution, and the duplicated choices cannot support a unique multiple-choice answer.
  The derivation in the solution section is mathematically consistent; the corruption lies in the printed choices.

- **Expected result:** derive the solution independently, preserve the source-faithful printed choices, and record that the Chapter 8 formula is the intended answer even though no printed choice contains it.

- **Uncertainty:** none; the retained scan resolves the radical visibly and the quadratic reduction of `$\cos z=3$` determines the required `$\sqrt2$` term.

- **Repair:** `P-GRECH7-46` proves the full solution set and explains why no retained answer choice is correct as printed; the external source is left unchanged.

### Harvard Math 21b Practice Final 5 Problem 14 source solution solves the wrong characteristic roots and particular coefficient

- **Object and need:** `P-HM21B18-PF5-14` in `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-5`. The problem asks for the general solution of `$D^{30}f-f=\sin(2t)$`.

- **Observed evidence:** direct inspection of page 18 of `assets/attachments/solution5.pdf` shows the supplied solution using modes `$e^{2\pi i k t/30}$`. The characteristic roots are instead `$\zeta_k=e^{2\pi i k/30}$`, so the homogeneous modes are `$e^{\zeta_k t}$`. The same source then gives the particular coefficient `$1/(2^{30}-1)$`, but `$D^{30}\sin(2t)=-2^{30}\sin(2t)$`; hence `$(D^{30}-1)(A\sin(2t))=-A(2^{30}+1)\sin(2t)$` and the required coefficient is `$A=-1/(2^{30}+1)$`.

- **Impact and owner:** both the homogeneous exponentials and the particular solution in the supplied source answer are mathematically incorrect.
  The corpus solution must derive both from the characteristic polynomial rather than reproduce the source answer.

- **Expected result:** the authored solution uses the thirty roots of unity as characteristic roots and the particular solution `$-\sin(2t)/(2^{30}+1)$`.

- **Uncertainty:** none; the retained PDF fixes the printed formulas and the differential-operator computation is exact.

- **Repair:** `P-HM21B18-PF5-14` gives the corrected complete solution; the external source is left unchanged.

### Harvard Math 21b Practice Final 7 Problem 7 prints the wrong normal-equation right-hand side

- **Object and need:** `P-HM21B18-PF7-07` in `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-7`. The problem asks for the least-squares fit of `$z=axy+bx^2$` to three data points.

- **Observed evidence:** direct inspection of page 11 of `assets/attachments/solution7.pdf` shows the design matrix `$A=\left[\begin{smallmatrix}1&1\\2&1\\0&1\end{smallmatrix}\right]$`, the data vector `$(4,6,8)^T$`, and the printed claim `$A^T(4,6,8)^T=(8,9)^T$`. Direct multiplication gives instead `$A^T(4,6,8)^T=(16,18)^T$`.

- **Impact and owner:** the printed intermediate normal equation is wrong by a factor of two on its right-hand side.
  The source's final answer `$a=-1,b=7$` is correct only for the corrected vector `$(16,18)^T`.

- **Expected result:** use `$\left[\begin{smallmatrix}5&3\\3&3\end{smallmatrix}\right](a,b)^T=(16,18)^T$` and derive the fit `$z=-xy+7x^2$`.

- **Uncertainty:** none; the retained PDF fixes the printed numbers and the matrix multiplication is exact.

- **Repair:** `P-HM21B18-PF7-07` derives the least-squares solution from the corrected normal equations; the external source is left unchanged.

### Harvard Math 21b Practice Final 7 Problem 14 has an incorrect QR step and assumes convergence of accumulated Q factors

- **Object and need:** `P-HM21B18-PF7-14` in `SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-7`. The problem asks about one QR iteration `$A=QR\mapsto RQ$` and the eigenvectors produced by iteration.

- **Observed evidence:** direct inspection of page 17 of `assets/attachments/solution7.pdf` shows the supplied part (b) using `$C=\left[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right]$` and printing `$T(C)=\frac15\left[\begin{smallmatrix}6&13\\-3&6\end{smallmatrix}\right]$`. With the standard positive-diagonal QR factorization, direct computation gives instead `$T(C)=\frac15\left[\begin{smallmatrix}14&3\\3&6\end{smallmatrix}\right]$`. The printed matrix cannot be correct under any orthogonal QR step for this symmetric `$C$`, because `$T(C)=Q^TCQ$` must remain symmetric.
  The supplied part (d) also writes `$\lim_k Q_1\cdots Q_k$` without deriving existence of that limit from the only convergence granted in the problem, namely `$A_k\to D$`.

- **Impact and owner:** the numerical counterexample offered for nonlinearity contains a wrong QR iterate, and the eigenvector argument assumes an extra convergence statement.
  Neither defect changes the requested conclusions.

- **Expected result:** prove nonlinearity with an explicitly checked QR counterexample.
  For the eigenvectors, write `$A_k=S_k^TAS_k$`, `$S_k=Q_1\cdots Q_k$`; compactness of `$O(n)$` gives a convergent subsequence `$S_{k_j}\to S$`, and `$A_k\to D$` then yields `$D=S^TAS$`, so the columns of `$S$` are an orthonormal eigenbasis.

- **Uncertainty:** none about the two displayed logical/numerical defects.
  A full-sequence limit of the accumulated `$Q$` factors can hold under extra QR hypotheses, but it does not follow from the convergence assumption stated in this problem alone.

- **Repair:** `P-HM21B18-PF7-14` supplies the corrected QR computations and the compactness argument; the external source is left unchanged.

### UCLA Spring 2017 Analysis Problem 5 is false for complex measures on the closed interval

- **Object and need:** `P-UCLARA17S-05` in `SRC-UCLA-RA-SPRING-2017`. The official problem asks for preservation of Fourier-coefficient decay under absolute continuity for finite complex Borel measures on the literal closed interval `[0,1]`.

- **Observed evidence:** the official UCLA Spring 2017 exam states `[0,1]` for both measures.
  Take `\mu=\delta_0-\delta_1`. Then `\widehat\mu(n)=1-e^{2\pi i n}=0` for every integer `n`. Take `\nu=\delta_0`; one has `|\nu|\ll|\mu|`, and even `d\nu=f\,d\mu` with `f(0)=1,f(1)=0`, but `\widehat\nu(n)=1` for every `n`. The retained source solution also uses the false claim that periodic trigonometric polynomials are uniformly dense in all of `C([0,1])`; they cannot distinguish the two endpoints.

- **Impact and owner:** the requested conclusion cannot be proved from the printed hypotheses.
  The standard Rajchman-band theorem is valid on the circle (equivalently on a half-open fundamental interval such as `[0,1)`), where the endpoint-cancellation counterexample disappears.

- **Expected result:** preserve the source-faithful statement, refute it by the endpoint counterexample, and state/prove the corrected circle or `[0,1)` version separately rather than silently changing the source.

- **Uncertainty:** none under the standard total-variation notion of absolute continuity for complex measures; the same counterexample also satisfies the Radon--Nikodym representation used by the retained source solution.

- **Repair:** `P-UCLARA17S-05` records the counterexample and proves the corrected periodic version; the external exam and supplied solution remain unchanged.

### Wesleyan August 2013 Topology Part I Problem 2 omits the nonempty-index hypothesis

- **Object and need:** `P-WESTOP13-I2` in `SRC-WESLEYAN-TOP-SUMMER-2013`. Part 2 asks to prove that `X = \prod_{\alpha\in J}Y_\alpha` is not compact, where every factor is either the `K`-topology interval or the lower-limit interval, but the source does not state that `J` is nonempty.

- **Observed evidence:** the retained August 7, 2013 exam transcription gives an arbitrary index set `J` and no nonemptiness condition.
  For `J=\varnothing`, the product is the one-point space, hence compact.

- **Impact and owner:** the printed conclusion has a degenerate counterexample.
  For every nonempty `J`, the intended proof works exactly as requested: the given product topology is strictly finer than the ordinary Hausdorff product topology on `[0,1]^J`, so part 1 rules out compactness.

- **Expected result:** preserve the literal source, record the empty-product exception, and prove noncompactness for `J\ne\varnothing`.

- **Uncertainty:** none; this is the standard empty-product convention.

- **Repair:** `P-WESTOP13-I2` records the exception and proves the intended nonempty-index-set statement.

### UCLA Fall 2001 Basic Problem 1 omits the nonempty-set hypothesis

- **Object and need:** `P-UCLAB01F-01` in `SRC-UCLA-BASIC-FALL-2001`. The problem asks for a maximizer of a continuous real-valued function on a compact subset `K\subset\mathbb R`.

- **Observed evidence:** page 1 of `assets/attachments/basic-01F.pdf` states only that `K` is compact and asks for a point `x_0\in K` satisfying `f(x)\le f(x_0)` for every `x\in K`. Under the standard convention, the empty set is compact.
  For `K=\varnothing`, there is no point `x_0\in K`, so the conclusion is false.

- **Impact and owner:** the printed statement has a degenerate counterexample.
  For every nonempty compact `K`, the intended conclusion is the extreme value theorem.

- **Expected result:** preserve the source-faithful statement, record the empty-set exception, and prove the intended theorem under the missing hypothesis `K\ne\varnothing`.

- **Uncertainty:** none; `K=\varnothing` settles the literal statement.

- **Repair:** `P-UCLAB01F-01` records the exception and proves the intended nonempty-compact-set statement.

### UCLA Fall 2016 Basic Problem 5 allows the zero span

- **Object and need:** `P-UCLAB16F-05` in `SRC-UCLA-BASIC-FALL-2016`. The problem asks to prove that a complex number `\beta` preserving the finite-dimensional `\mathbb Q`-span `V` of `\alpha_1,\ldots,\alpha_n` is algebraic of degree at most `n`.

- **Observed evidence:** the retained statement imposes no hypothesis that one of the `\alpha_i` is nonzero.
  If all `\alpha_i=0`, then `V=\{0\}` and `\beta V\subseteq V` holds for every complex `\beta`, including transcendental numbers.

- **Impact and owner:** the printed statement is false in the degenerate zero-space case.
  If `V\ne\{0\}`, the intended argument works: for nonzero `v\in V`, the `n+1` vectors `v,\beta v,\ldots,\beta^n v` are linearly dependent over `\mathbb Q`.

- **Expected result:** preserve the source statement, record the zero-span counterexample, and prove the intended result under `V\ne\{0\}`.

- **Uncertainty:** none; `V=\{0\}` makes the multiplier condition vacuous.

- **Repair:** `P-UCLAB16F-05` records the exception and proves the corrected nonzero-span statement.

### Nori Galois Theory Problem 6.1 reverses the multiplication order for left-module generators

- **Object and need:** `P-NORI-GT-6-01` in `SRC-NORI-GALOIS-THEORY-PROBLEMS`. The source composes ring homomorphisms `A -> B -> C`, treats `B` as a left `A`-module and `C` as a left `B`-module, but asks for the `A`-module generators `\gamma_i g(\beta_j)`.

- **Observed evidence:** direct inspection of page 6 of the retained `Nori_Galois_Theory_Problems.pdf` confirms that the source itself prints `\gamma_i.g(\beta_j)`, so this is not an extraction reversal.
  For arbitrary rings the left scalar actions instead produce `g(\beta_j)\gamma_i`. A concrete counterexample is obtained from the diagonal subring `A\subset M_2(k)=B=C`, with left `A`-basis `I,P` of `B` and left `B`-basis `\gamma=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}` of `C`: the left `A`-span of `\gamma` and `\gamma P` contains only matrices whose first-row entries are equal.

- **Impact and owner:** part (1) is false as printed for arbitrary rings, and therefore part (2) is false with the same displayed family.
  Reversing the product to `g(\beta_j)\gamma_i` gives the standard correct left-module statement.
  The printed order is also valid under an additional hypothesis that every `g(\beta_j)` commutes with every `\gamma_i`, for example when `C` is commutative.

- **Expected result:** preserve the printed problem statement, refute the arbitrary-ring assertion, prove the corrected left-module statement with `g(\beta_j)\gamma_i`, and state the commutativity condition under which the printed order becomes valid.

- **Uncertainty:** none; the retained PDF fixes the printed order and the matrix counterexample directly violates the claimed spanning conclusion.

- **Repair:** `P-NORI-GT-6-01` records the source erratum, gives the explicit counterexample, proves the corrected spanning and basis statements, and notes the sufficient commuting hypothesis.
  The external source is unchanged.

### Wesleyan 2016 Real Analysis Problem B4 card dropped the source restriction to $[0,1]$

- **Object and need:** `P-WESRA16-B4` in `SRC-WESLEYAN-RA-SUMMER-2016`. The retained source defines all three sets `X`, `Y`, and `Z` by conditions on points `x\in[0,1]`, but the card had transcribed only `{f>1}`, `{f=1}`, and `{f<1}`.

- **Observed evidence:** the checked-in MinerU extraction of the July 7, 2016 exam explicitly prints `X = { x \in [0,1] : f(x)>1 }`, and likewise for `Y` and `Z`. Since the same problem assumes `supp(f)\subseteq[0,1]`, the truncated card instead made every point outside `[0,1]` belong to `Z`.

- **Impact and owner:** under the truncated card statement, `Z` has infinite Lebesgue measure, so the requested decomposition by `\lambda(Z)` no longer states the source problem and introduces an unnecessary extended-arithmetic ambiguity.
  This is a card transcription defect, not source errata.

- **Expected result:** restore the literal `x\in[0,1]` restrictions from the source and solve the resulting three-region decomposition using monotone convergence on `X` and dominated convergence on `Z`.

- **Uncertainty:** none; the retained extraction contains all three interval restrictions explicitly.

- **Repair:** `P-WESRA16-B4` restores the omitted restrictions and supplies the complete structured proof.

### UGA Math 8150 Homework 3 Problem 1 card lost the arrow in $r\to0$

- **Object and need:** `P-UGA8150S21-HW3-01` in `SRC-UGA-MATH8150-SPRING-2021-HW3`. The card displayed the limit subscript as `r  0`, inherited from the checked-in extraction.

- **Observed evidence:** direct inspection of page 1 of the retained `8150-hw3.pdf` shows the limit explicitly as `r\to0` in the normalized small-circle integral.

- **Impact and owner:** the missing arrow makes the limiting process malformed in the authored problem statement.
  The source PDF itself is unambiguous.

- **Expected result:** restore `r\to0` literally from the source and prove the stated equivalence with complex differentiability.

- **Uncertainty:** none after direct inspection of the retained PDF page.

- **Repair:** `P-UGA8150S21-HW3-01` restores the arrow and supplies the complete structured proof.

### UGA Math 8150 Homework 3 Problem 10 is false without control at the exceptional point

- **Object and need:** `P-UGA8150S21-HW3-10` in `SRC-UGA-MATH8150-SPRING-2021-HW3`. The source assumes only that `f'(z)` exists away from one point `w` and asks for vanishing of the integral around a triangle containing `w`.

- **Observed evidence:** the retained source PDF has no continuity or boundedness hypothesis at `w`. Defining `f(w)=0` and `f(z)=1/(z-w)` for `z\ne w` satisfies differentiability away from `w`, but every positively oriented triangle containing `w` has integral `2\pi i`.

- **Impact and owner:** the requested conclusion is false as printed.
  Local boundedness near `w` is sufficient, and continuity at `w` is a standard stronger sufficient hypothesis.

- **Expected result:** preserve the source statement and erratum, refute the printed claim explicitly, and prove the corrected locally bounded version.

- **Uncertainty:** none; the counterexample directly violates the source conclusion.

- **Repair:** `P-UGA8150S21-HW3-10` gives the counterexample and proves the corrected statement by excising a small square around `w` and applying Goursat's theorem to the remaining triangulated region.

### Wesleyan August 2013 Supplemental Real Analysis Problem II2 extraction changed $1/2$ to $3/2$

- **Object and need:** `P-WESRA13A-II2` in `SRC-WESLEYAN-RA-AUGUST-2013-SUPPLEMENTAL`. The checked-in extraction reads `\mu(B_i)>3/2`, impossible under the simultaneous hypothesis `\mu(X)=1`.

- **Observed evidence:** direct inspection of page 1 of the retained `analysis_2008-2013.pdf` shows the printed threshold clearly as `\mu(B_i)>1/2`.

- **Impact and owner:** the extracted threshold made the premise impossible and reduced the problem to a vacuous implication.
  The retained source is unambiguous.

- **Expected result:** restore the source threshold `1/2` and prove that the average of the indicators exceeds `1/2` on a positive-measure set.

- **Uncertainty:** none after direct page inspection.

- **Repair:** `P-WESRA13A-II2` restores the source threshold and supplies the complete structured proof.

### Wesleyan August 2013 Supplemental Real Analysis Problem II5 extraction lost the target in part (a)

- **Object and need:** `P-WESRA13A-II5` in `SRC-WESLEYAN-RA-AUGUST-2013-SUPPLEMENTAL`. The checked-in extraction kept “Does this imply that” in part (a) but destroyed the derivative condition being asked about.

- **Observed evidence:** direct inspection of page 2 of the retained `analysis_2008-2013.pdf` shows that part (a) asks whether a strictly increasing function `F:[0,1]\to\mathbb R` must satisfy `F'(x)>0` almost everywhere.

- **Impact and owner:** the card previously could not state or answer part (a) without guessing the missing formula.
  The retained source page resolves the question unambiguously.

- **Expected result:** restore the literal derivative condition from the source and answer both implications in the two-part problem.

- **Uncertainty:** none after direct inspection of the retained PDF page.

- **Repair:** `P-WESRA13A-II5` restores the missing target and supplies counterexamples to both implications in a complete structured proof.

### Wesleyan 2016 Complex Analysis Problem 8 is false for the zero function

- **Object and need:** P-WESCA16-8 in SRC-WESLEYAN-CA-2016. The source assumes only that a holomorphic function satisfies \(f(0)=f'(0)=f''(0)=0\), then asks to prove that every sufficiently small value has at least three preimages counted with multiplicity.

- **Observed evidence:** the retained source states no nonconstancy hypothesis.
  The function \(f\equiv0\) satisfies all three displayed derivative conditions, but for every nonzero \(w\) the equation \(f(z)=w\) has no solutions.

- **Impact and owner:** the literal claim cannot be proved.
  If \(f\) is assumed nonconstant, the intended conclusion follows from the isolated zero at \(0\) and Rouché's theorem: on a sufficiently small circle, \(f\) and \(f-w\) have the same number of zeros, namely the order of the zero of \(f\) at \(0\), which is at least three.

- **Expected result:** preserve the source statement, refute it with \(f\equiv0\), and prove the corrected nonconstant version.

- **Uncertainty:** none about the literal counterexample or the retained source wording; the missing nonconstancy hypothesis is the minimal natural correction.

- **Repair:** TODO.md section 7 / issue #2. P-WESCA16-8 should record the counterexample and prove the corrected theorem under \(f\not\equiv0\).

### Week 5 Practice Problem 4 gives a non-homomorphism in its supplied solution

- **Object and need:** `P-PRACT20-W5-04` in `SRC-PRELIM-PRACTICE-WEEK5-2020`. The problem asks for all endomorphisms of `U_4={1,i,-1,-i}` under multiplication.

- **Observed evidence:** `assets/attachments/Week5_solns.pdf` lists the map `phi(x)=-x` as the homomorphism corresponding to `phi(i)=-i`. But this map sends the identity `1` to `-1`, so it is not a group homomorphism.

- **Impact and owner:** the source's list contains the correct number of endomorphisms but gives the wrong formula for the endomorphism sending `i` to `-i`. The correct map is `phi(z)=z^3`.

- **Expected result:** the authored solution should derive all four maps from cyclicity of `U_4` and list them as `z -> z^m` for `m=0,1,2,3`.

- **Uncertainty:** none; preservation of the identity already disproves the printed formula.

- **Repair:** TODO.md section 7 / issue #2. `P-PRACT20-W5-04` supplies the correct four endomorphisms and explicitly identifies the source error.

### Week 5 Practice Problem 28 drops the minus sign in the contour integral

- **Object and need:** `P-PRACT20-W5-28` in `SRC-PRELIM-PRACTICE-WEEK5-2020`. The problem asks for the positively oriented integral of `sin(z) - cos(z)/(z-pi/4)` around `|z|=pi`.

- **Observed evidence:** `assets/attachments/Week5_solns.pdf` correctly computes the residue of `cos(z)/(z-pi/4)` as `cos(pi/4)=sqrt(2)/2`, but its final integral is positive `sqrt(2) pi i`, dropping the minus sign present in the original integrand.

- **Impact and owner:** the supplied numerical answer has the wrong sign.
  The entire sine term contributes zero, while Cauchy's formula gives `-2 pi i cos(pi/4)=-sqrt(2) pi i`.

- **Expected result:** retain the source problem and give the negative value, explicitly preserving the sign of the pole term.

- **Uncertainty:** none; the sign follows directly from linearity of the contour integral and the printed integrand.

- **Repair:** TODO.md section 7 / issue #2. `P-PRACT20-W5-28` supplies the corrected value and derivation.

### UGA Math 8210 Homework 1 Exercise 6 omits smoothness of the graph map

- **Object and need:** `P-UGA8210F18-HW1-06` in `SRC-UGA-MATH8210-FALL-2018-HW1`. The final part asks to show that the graph of an arbitrary map `h:X->Y` is a smooth manifold.

- **Observed evidence:** direct inspection of `assets/attachments/HW1.pdf` confirms that the source says only “suppose that h:X->Y” and does not assume continuity or smoothness before the graph claim.

- **Impact and owner:** the literal assertion is false.
  For example, with `X=Y=R` and `h(0)=1`, `h(x)=0` for `x!=0`, the graph has an isolated point together with non-isolated points and is not a manifold of any fixed dimension.
  The intended standard theorem is that the graph of a smooth map is a smooth embedded submanifold, diffeomorphic to `X`.

- **Expected result:** preserve the literal source statement, refute it, and prove the intended theorem under the added hypothesis that `h` is smooth.

- **Uncertainty:** none about the printed wording or counterexample; the missing smoothness hypothesis is forced by the hint using a diffeomorphism `X -> graph(h)`.

- **Repair:** TODO.md section 7 / issue #2. `P-UGA8210F18-HW1-06` supplies the counterexample and proves the corrected smooth-map version.

### UCLA Spring 2014 Analysis Problem 10 has the wrong density hypothesis

- **Object and need:** `P-UCLARA14S-10` in `SRC-UCLA-RA-SPRING-2014`. The source assumes `alpha in [0,1] \ Q` and uses the boundary points `exp(i alpha n)`, then asks to prove that the resulting analytic function has the unit circle as a natural boundary.

- **Observed evidence:** the retained `assets/attachments/UCLA_Solutions.pdf` uses exactly `e^{i alpha n}` and then asserts that irrationality of `alpha` makes these points dense in the unit circle.
  This is false: `alpha=pi/5` lies in `[0,1] \ Q`, but `e^{i alpha n}=e^{2 pi i n/10}` takes only ten values.

- **Impact and owner:** the literal problem is false.
  For `alpha=pi/5`, the pole locations form a finite set, so after grouping equal denominators the series is meromorphic across all other boundary points and cannot have the whole unit circle as a natural boundary.

- **Expected result:** preserve the literal source statement and counterexample, then prove the intended theorem under the minimal corrected hypothesis `alpha/(2 pi) notin Q` (equivalently, replace `e^{i alpha n}` by `e^{2 pi i alpha n}` while retaining `alpha notin Q`).

- **Uncertainty:** none about the counterexample or source wording.
  The intended normalization is ambiguous between correcting the exponent and correcting the hypothesis; both give the same density mechanism.

- **Repair:** TODO.md section 7 / issue #2. `P-UCLARA14S-10` records the false literal case and proves the corrected natural-boundary statement under `alpha/(2 pi) notin Q`.

### UCLA Spring 2013 Analysis Problem 11 has an incorrect residue formula

- **Object and need:** `P-UCLARA13S-11` in `SRC-UCLA-RA-SPRING-2013`. The problem asks for the poles and residues of `f(z)=-pi z cot(pi z)`.

- **Observed evidence:** the retained `assets/attachments/UCLA_Solutions.pdf` gives the residue at a nonzero integer `m` as `(-1)^(m+1)m`. But `sin(pi z)` has derivative `pi cos(pi m)=pi(-1)^m` at `m`, while the numerator is `-pi m cos(pi m)=-pi m(-1)^m`; their quotient is exactly `-m`.

- **Impact and owner:** the source answer in part (a) is wrong.
  The poles are the nonzero integers and every residue is `-m` at `z=m`; the apparent singularity at `0` is removable.

- **Expected result:** the authored solution should give residue `-m` at every nonzero integer and independently verify the Taylor-coefficient formula in part (b).

- **Uncertainty:** none; the residue follows directly from the quotient formula for a simple zero of `sin(pi z)`.

- **Repair:** TODO.md section 7 / issue #2. `P-UCLARA13S-11` supplies the corrected residue computation and the coefficient proof.

### UCLA Spring 2011 Analysis Problem 10 card and retained solution use different domains

- **Object and need:** `P-UCLARA11S-10` in `SRC-UCLA-RA-SPRING-2011`. The current card asks for `sup Re f'(i/2)` over holomorphic maps from the upper half of the unit disk to the unit disk.

- **Observed evidence:** the retained `assets/attachments/UCLA_Solutions.pdf` instead states and solves the problem for holomorphic maps `H -> D`, where `H` is the upper half-plane.
  Its conformal map and its value `1` are specific to that domain.

- **Impact and owner:** the two extremal problems have different answers.
  For the current half-disk card, the biholomorphism `Phi(z)=((1+z)/(1-z))^2` maps the domain to the upper half-plane and Schwarz--Pick gives the sharp value `5/3` at `z=i/2`. Thus the retained source solution cannot be attached to the current statement.

- **Expected result:** solve the literal current card with value `5/3`. Separately, source reconciliation should determine whether the card statement or the retained solution transcription reflects the intended exam problem.

- **Uncertainty:** the mathematical distinction is certain; the intended source version is not resolved by the retained compendium alone.

- **Repair:** TODO.md section 7 / issue #2. `P-UCLARA11S-10` supplies the complete proof for its literal half-disk statement.

### Maxim algebraic topology 4.12 lost the middle mapping arrow during extraction

- **Object and need:** `P-MAXAT-4-12` in `SRC-MAXIM-PROBLEMS-ALGEBRAIC-TOPOLOGY`.

- **Observed evidence:** the retained Markdown extraction renders the middle mapping-space problem as `S^{\bar 1} S^2`, while its neighboring clauses are `S^1 -> S^3` and `S^1 -> CP^n`. The corresponding free-loop-space exercise is the standard `S^1 -> S^2` case.

- **Impact and owner:** the malformed card statement is not mathematically parseable and obscures one of the three spaces whose cohomology is requested.

- **Expected result:** normalize the middle clause to `S^1 -> S^2` and solve the three free-loop-space calculations.

- **Uncertainty:** none about the missing arrow; the source context fixes the intended middle target as `S^2`.

- **Repair:** TODO.md section 7 / issue #2. `P-MAXAT-4-12` now carries the corrected statement and complete integral cohomology calculation.

### Maxim algebraic topology 6.6 has the parity of the projective space reversed

- **Object and need:** `P-MAXAT-6-06` in `SRC-MAXIM-PROBLEMS-ALGEBRAIC-TOPOLOGY`.

- **Observed evidence:** both the card and the retained source extraction state that `RP^{2k+1}` cannot be a boundary.
  This is false: multiplication by `i` on `S^{2k+1} \subset C^{k+1}` descends to a fixed-point-free involution of `RP^{2k+1}`, and the standard quotient `(M x [-1,1])/(x,t)~(T(x),-t)` gives a manifold bounded by `M`.

- **Impact and owner:** the literal source problem asks for a proof of a false statement.
  In fact every odd-dimensional real projective space is null-bordant as an unoriented manifold.

- **Expected result:** refute the literal statement and prove the standard corrected assertion `RP^{2k}` cannot be a boundary, using `chi(RP^{2k})=1` and the fact that every closed boundary has even Euler characteristic.

- **Uncertainty:** none about the mathematical defect; the intended corrected exponent is inferred from the standard characteristic-class/bordism result.

- **Repair:** TODO.md section 7 / issue #2. `P-MAXAT-6-06` records the counterexample/construction and proves the corrected even-dimensional statement.

### Maxim algebraic topology 6.8 asks for an exact embedding dimension not known in general

- **Object and need:** `P-MAXAT-6-08` in `SRC-MAXIM-PROBLEMS-ALGEBRAIC-TOPOLOGY`.

- **Observed evidence:** the retained source literally asks for the smallest `k` for which `CP^n` smoothly embeds in `R^{2n+k}`, with arbitrary `n`. Determining this minimum is the Euclidean embedding-dimension problem for complex projective spaces, treated in specialized work of Atiyah--Hirzebruch/Feder--Segal, Mukherjee, Davis--Mahowald, and others.
  Published bounds do not coincide for all `n`; for example the literature leaves `CP^7` with embedding dimension in `{23,24}`.

- **Impact and owner:** there is no single currently established formula that can serve as the requested answer for arbitrary `n`. Treating a general upper or lower bound as “the smallest k” would state an unproved result.

- **Expected result:** record the invariant `N(n)=min{N: CP^n embeds smoothly in R^N}`, give rigorous classical lower and upper bounds, and identify the families in which they coincide.

- **Uncertainty:** the exact value is known in many special cases but not uniformly; the source gives no restriction on `n` that would make the problem determinate.

- **Repair:** TODO.md section 7 / issue #2. `P-MAXAT-6-08` states the correct research-status answer and the exact values forced by the classical bounds in the standard low-binary-weight families.

### MTH 674 Problem I is only an unrecovered cross-reference to homework

- **Object and need:** `P-MTH674-01` in `SRC-MTH674-DIFFGEOM-MIDTERM-SAMPLE`.

- **Observed evidence:** the retained source extraction reads only “Problem I. Homework assignments I and II.” No statement from either homework assignment is included in the retained source bytes or in the card.

- **Impact and owner:** this card is not a self-contained mathematical problem, so a proof cannot be authored without inventing missing source content.

- **Expected result:** recover the referenced Homework I and II source material, replace the placeholder by the actual posed mathematics, and only then author a solution.

- **Uncertainty:** the titles/content of the referenced homework assignments are not recoverable from the current source packet.

- **Repair:** blocked on source recovery; section 7 proceeds to the next self-contained card rather than fabricating a solution.

### Series Assignment 2 Problem 2 omits the finite-limsup hypothesis used by its own proof

- **Object and need:** `P-SERIES-A2-02` in `SRC-SEQUENCES-SERIES-ASSIGNMENT-2`.

- **Observed evidence:** the retained source states for an arbitrary real sequence that `limsup a_n = sup S`, where `S` is the set of finite subsequential limits.
  Its supplied proof immediately treats `L=limsup a_n` as a finite real number and constructs a subsequence converging to `L`.

- **Impact and owner:** the literal statement is false for unbounded sequences.
  For example `a_n=n` has no finite convergent subsequence, so `S=empty`, while `limsup a_n=+infinity`.

- **Expected result:** state and prove the theorem when `limsup a_n` is finite (equivalently in the usual bounded-sequence setting), and analogously for finite `liminf`; explicitly record the counterexample to the literal unrestricted formulation.

- **Uncertainty:** none; the source proof itself makes the missing finiteness assumption.

- **Repair:** TODO.md section 7 / issue #2. `P-SERIES-A2-02` records the counterexample and proves the corrected finite-extreme-subsequential-limit statements.

### Contact Topology Exercise 2.24 has incompatible coefficients and requested foliation

- **Object and need:** `P-UTCT-2-24` in `SRC-UT-M392C-CONTACT-TOPOLOGY-FALL-2017`.

- **Observed evidence:** the retained source itself prints `alpha = dz + a dx + b dy` with constant `a,b`, but then asks to compute the contact sign/divergence and to check that the characteristic foliation is `x^b y^a = c`.

- **Impact and owner:** for the printed form, `d alpha=0`, hence `alpha wedge d alpha=0`; it is not a contact form.
  On the `xy`-plane the characteristic line field is `ker(a dx+b dy)`, whose leaves are `a x+b y=c`, not `x^b y^a=c`.

- **Expected result:** solve the literal printed problem and state that the advertised monomial foliation does not follow.
  The natural corrected form `alpha = dz + b y dx + a x dy` has characteristic vector field `a x partial_x-b y partial_y`, leaves `x^b y^a=c` on sign-compatible quadrants, and divergence/contact sign determined by `a-b`.

- **Uncertainty:** the retained source does not specify which coefficients were intended; the corrected form above is the minimal one reproducing the displayed first integral and the intended divergence discussion.

- **Repair:** TODO.md section 7 / issue #2. `P-UTCT-2-24` records the literal calculation and the natural corrected calculation separately.

### Hatcher qual-review Problem 1 omits the cocycle hypothesis in the Kronecker pairing

- **Object and need:** `P-QUAL-REVIEW-HATCHER-01` in `SRC-QUAL-REVIEW-HATCHER`.

- **Observed evidence:** the retained source says that if `z-z'` is a boundary then `<z,alpha>=<z',alpha>` for arbitrary `alpha in C^k(X;R)`. This is false unless `alpha` is a cocycle.

- **Impact and owner:** the first claimed invariance does not descend from chains to homology for arbitrary cochains.
  For example in degree zero on an interval, `[1]-[0]` is a boundary, but an arbitrary zero-cochain can take different values on the endpoints.

- **Expected result:** require `delta alpha=0` in the first assertion; then `<partial w,alpha>=<w,delta alpha>=0`. Together with the corresponding coboundary calculation, this yields the well-defined Kronecker pairing on `H_k x H^k`.

- **Uncertainty:** none; the correction is the standard chain/cochain pairing identity.

- **Repair:** TODO.md section 7 / issue #2. `P-QUAL-REVIEW-HATCHER-01` records the literal counterexample and proves the corrected statement.

### Hatcher qual-review Problem 2 omits the projective/free hypothesis needed for its numerical Hom calculation

- **Object and need:** `P-QUAL-REVIEW-HATCHER-02` in `SRC-QUAL-REVIEW-HATCHER`.

- **Observed evidence:** the retained source asks for `H_*(underline Hom(C_*,D_*))` from the homology groups of `C_*` and `D_*` alone, after stating only that `C_*,D_*` are bounded below.
  Its preceding fact (i) itself says quasi-isomorphism invariance in the second variable only when the first complex is free.

- **Impact and owner:** raw total Hom is not determined by the two homology groups without a projective/free model hypothesis.
  The acyclic bounded complex `0 -> Z --2--> Z -> Z/2 -> 0` is not contractible, and `underline Hom(-,Z)` has a nonzero `Z/2` homology class on it.
  Thus adding this acyclic summand changes total-Hom homology without changing `H_*(C)`.

- **Expected result:** prove the chain-homotopy invariance assertion exactly as stated.
  For the numerical computation, state the intended hypothesis that `C_*` is a bounded-below complex of free abelian groups (equivalently, compute the derived Hom represented by a free model), then use the Hom/Ext Künneth-style decomposition.

- **Uncertainty:** none about the missing hypothesis; the source's reference to the Künneth proof strongly indicates the intended free-chain setting.

- **Repair:** TODO.md section 7 / issue #2. `P-QUAL-REVIEW-HATCHER-02` records the counterexample, proves homotopy invariance, and gives the corrected free-source numerical answer.

### Wesleyan Complex Analysis 2006 Problem 3 omits boundary regularity

- **Object and need:** `P-WESCA06-II3` in `SRC-WESLEYAN-CA-SUMMER-2006`.

- **Observed evidence:** the retained source says only that `f,g` are analytic in a bounded domain `D` with compact closure, then asks to show `|f|+|g|` attains its maximum on `∂D`.

- **Impact and owner:** the literal statement is not well-defined in general, because functions holomorphic only on `D` need not extend to the boundary.
  For instance `f(z)=1/(1-z)` on the unit disk has no finite boundary value at `z=1`.

- **Expected result:** assume `f,g` are continuous on `\overline D` and holomorphic on `D` (or holomorphic on a neighborhood of `\overline D`), then prove the boundary-maximum claim by the source's phase-alignment hint and the maximum modulus principle.

- **Uncertainty:** none about the missing regularity; the standard corrected hypothesis is uniquely determined by the requested boundary maximum.

- **Repair:** TODO.md section 7 / issue #2. `P-WESCA06-II3` records the literal counterexample and proves the corrected statement.

### Wesleyan Topology 2010 Part II Problem 1(c) has a likely lost negation

- **Object and need:** `P-WESTOP10-II1` in `SRC-WESLEYAN-TOP-SUMMER-2010`.

- **Observed evidence:** the retained source reads “Describe two connected spaces `X,Y` such that `H_i(X) ≅ H_i(Y)` for all `i`, but `π_1(X) ≅ π_1(Y)`.” The contrastive “but” makes the second isomorphism vacuous rather than contrasting with the homology condition.

- **Impact and owner:** the printed problem is trivially solved by taking `X=Y`; it almost certainly intended `π_1(X) not≅ π_1(Y)`, but the retained source does not preserve a negation symbol.

- **Expected result:** preserve and answer the literal extracted statement, while separately giving the natural intended example `T^2` and `S^1 vee S^1 vee S^2`, which have identical integral homology in every degree but fundamental groups `Z^2` and `F_2`.

- **Uncertainty:** the missing negation is strongly indicated by wording but cannot be asserted as recovered source text.

- **Repair:** TODO.md section 7 / issue #2. `P-WESTOP10-II1` now answers both the literal reading and the likely intended contrastive reading, explicitly distinguished.

### Wesleyan Topology 2010 Part II Problem 2(b) repeats its compactness hypothesis

- **Object and need:** `P-WESTOP10-II2` in `SRC-WESLEYAN-TOP-SUMMER-2010`.

- **Observed evidence:** the retained source says: if `X` is compact and every fiber `p^{-1}(x)` is finite, show that `X` is compact.

- **Impact and owner:** the literal conclusion is identical to an assumption, so the second half contains no mathematical task.
  The standard covering-space theorem in this context is that the total space `\widetilde X` is compact when the base is compact and every fiber is finite.

- **Expected result:** preserve the literal statement and identify it as immediate, then prove the standard intended finite-sheeted compactness theorem for `\widetilde X` without silently replacing the source.

- **Uncertainty:** the intended replacement is strongly supported by the canonical covering-space exercise, but the retained Wesleyan source itself does not preserve the corrected symbol.

- **Repair:** TODO.md section 7 / issue #2. `P-WESTOP10-II2` records the source defect, proves the Hausdorff assertion, and proves the standard intended total-space compactness result separately.

### Wesleyan Complex Analysis August 2013 Problem II.1 has an unrecovered nonholomorphic third formula

- **Object and need:** `P-WESCA13A-II1` in `SRC-WESLEYAN-CA-AUGUST-2013`.

- **Observed evidence:** the retained deterministic extraction renders the third function as `sqrt(conj(z))/(z-1)`, while the problem asks to classify isolated singularities of holomorphic functions and compute pole orders/residues where applicable.

- **Impact and owner:** the extracted third expression is not holomorphic on any punctured neighborhood, so the requested isolated-singularity classification is not mathematically applicable to it.
  The first two subparts are unambiguous.

- **Expected result:** solve the first two functions exactly and leave the third explicitly blocked until an independent source recovers the intended formula.

- **Uncertainty:** the intended third function is not recoverable from the retained extraction without guessing.

- **Repair:** TODO.md section 7 / issue #2. `P-WESCA13A-II1` contains the complete first-two classifications and records the exact obstruction for the third.

### Hatcher qual-review Problem 2 asks for raw total-Hom homology from insufficient data

- **Object and need:** `P-QUAL-REVIEW-HATCHER-02` in `SRC-QUAL-REVIEW-HATCHER`.

- **Observed evidence:** the retained source assumes only that `C_*` and `D_*` are bounded below, then gives only their homology groups and asks for the homology of the raw total complex `underline Hom(C_*,D_*)`. It separately states the needed invariance fact only under the hypothesis that `C_*` is free.

- **Impact and owner:** without a projective/K-projective hypothesis on the first variable, raw Hom does not preserve quasi-isomorphisms, so its homology is not determined by `H_*(C)` and `H_*(D)`. For example the bounded exact complex `0 -> Z -> Q -> Q/Z -> 0` is acyclic but its raw Hom into `Z[0]` has nonzero homology.

- **Expected result:** prove the chain-homotopy preservation statement literally, then perform the numerical calculation under the intended hypothesis that `C_*` is a bounded-below complex of free abelian groups, or equivalently for `RHom(C,D)` after a free replacement.

- **Uncertainty:** none about the logical gap; the intended projective convention is inferred from fact (1) and the instruction to imitate the Künneth proof.

- **Repair:** TODO.md section 7 / issue #2. `P-QUAL-REVIEW-HATCHER-02` states the defect, proves the sign-correct homotopy formula, and gives the complete derived/free-model homology table.

### UCLA Spring 2013 Analysis Problem 11 has an incorrect residue formula

- **Object and need:** `P-UCLARA13S-11` in `SRC-UCLA-RA-SPRING-2013`. Part (a) asks for the poles and residues of `f(z)=-pi z cot(pi z)`.

- **Observed evidence:** the retained `assets/attachments/UCLA_Solutions.pdf` gives the residue at a nonzero integer `m` as `(-1)^(m+1) m`. But `cot(pi z)` has residue `1/pi` at every integer: both the numerator `cos(pi m)` and the derivative of the denominator `pi cos(pi m)` carry the same factor `(-1)^m`. Therefore `Res_{z=m}[-pi z cot(pi z)]=-m`.

- **Impact and owner:** the source answer for part (a) has the wrong sign for every even nonzero integer.
  The pole locations are otherwise correct; the apparent singularity at `0` is removable.

- **Expected result:** the authored solution should give simple poles at every nonzero integer with residue `-m`, and then derive the requested Taylor coefficients independently from the standard cotangent partial fraction expansion.

- **Uncertainty:** none; the residue follows directly from the quotient formula for a simple zero of `sin(pi z)`.

- **Repair:** TODO.md section 7 / issue #2. `P-UCLARA13S-11` supplies the corrected residues and coefficient calculation.

### UNL Math 872 assignment cards retain lost TeX escapes

- **Object and need:** cards for assignments 10.B.1–3, 10.C.1–4 and 11.B.1–2, 11.C.1 in `SRC-UNL-MATH872-SPRING-2014-PROBLEM-SETS` must preserve readable mathematical notation.

- **Observed evidence:** while repairing control bytes rejected by the push gate, reading these cards showed additional transport damage: `P-UNL872S14-10-B-3` has `operatorname{Homeo}`, `Fcirc q_G` and bare `[` display delimiters; `P-UNL872S14-10-C-4` has `ho:G` where the command prefix was lost.
  Restoring backspace, vertical-tab and form-feed bytes does not repair the missing escapes elsewhere.

- **Impact and owner:** the authored cards need a source-faithful notation repair; a successful corpus parse does not establish that their rendered formulas are correct.

- **Uncertainty:** the listed byte and text defects were inspected directly.
  The original sources have not been reread for a complete repair, and the remaining affected population has not been established beyond these ten cards.

- **Repair:** TODO.md section 7 / issue #2. Read each retained source, restore the intended notation without changing the mathematical claims, and inspect the rendered result at the normal publication boundary.
