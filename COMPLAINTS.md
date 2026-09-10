# Mathematical issues and papercuts

Record issues encountered during source reading, solving, review, authoring or
site use under [QUAL-05](CONTRIBUTING.md#named-policies). Include findings outside
the selected card. This file owns observations; [TODO.md](TODO.md) owns selected
repair tasks and dependencies. Keep existing GitHub issue links rather than
copying their live status. The [review policy index](REVIEW_POLICY.md) supplies
named candidate patterns, not proof that a candidate is a defect.

## Recording an issue

Add a descriptive heading in the appropriate section below, with:

- **Object and need:** card/collection ID or affected workflow; the exact
  mathematical statement and hypotheses, or user action and expected behavior.
- **Observed evidence:** source page and passage, counterexample or proof gap,
  or actual action and result with the relevant path/revision.
- **Impact and owner:** affected parts or consumers, existing partial result,
  and the mathematical or tool boundary that must change.
- **Uncertainty:** distinguish a verified error from a source ambiguity or
  review candidate. State inspected scope and remaining questions. For absence
  claims supply Searched, Found, Conclusion, Confidence and Gaps.
- **Repair:** link the existing TODO task or issue when available and state
  the result that would resolve the observation.

A missing hypothesis with a concrete counterexample is a mathematical issue.
An unreadable source is an unresolved source question. An unsolved problem is
ordinary authoring work, not by itself a defect. A command that prevents reading
the intended card is a papercut even when it has a simple workaround.

Extend an existing entry when the same cause affects another card. Preserve
concurrent entries. If the selected proof requires a repair, link that dependency
and resolve it before relying on the statement; recording it does not make the
proof valid. Continue independent assigned mathematics.

After verifying the full repair, remove the resolved entry with evidence in the
fixing commit; retain any unresolved portion. Put durable mathematical errata
on the owning card and durable policy in CONTRIBUTING. Keep process notes out
of public mathematical remarks.

## Mathematical issues and source questions

### Repository writes can fail because the root filesystem is full

- **Observed evidence:** during the final complex-analysis residual scan on 2026-09-10, a shell write failed with `no space left on device`. `df -h` reports `/dev/vda2` at 100% usage with `0` bytes available, while inode usage is only 29%.
- **Impact:** repository checks, temporary authoring output, edits, and commits may fail nondeterministically even when the worktree itself is healthy.
- **Repair:** free byte capacity on the repository host. This stream removed only its own `/tmp/ca-unsorted-*.tsv` scratch files and did not delete shared caches or other workers' data.

### E-N6DX3 contains unresolved image-only and omnibus prompts

- **Object and need:** `E-N6DX3` in `SRC-UNSORTED-COMPLEX-ANALYSIS`.
- **Observed evidence:** the card mixes many definition/theory questions with several unresolved Obsidian image embeds such as `_attachments/Pasted image ...`, followed only by terse hints. Those image-only subproblems are not stated in text.
- **Impact and owner:** there is no complete mathematical statement to solve. Providing answers only to the visible bullets would falsely mark the omnibus card complete while silently omitting the missing image problems.
- **Repair:** restore or transcribe each missing image problem, preferably splitting the omnibus into atomic cards, before solution authoring.

### E-W3QMS contains open-ended external-resource placeholders

- **Object and need:** `E-W3QMS` in `SRC-UNSORTED-COMPLEX-ANALYSIS`.
- **Observed evidence:** alongside the precise task "show that $f'=0$ implies $f$ is constant using integrals and primitives," the card also says "Do any example from here" and "Anything from the homeworks," with external links and unresolved image embeds.
- **Impact and owner:** those open-ended placeholders do not define finite mathematical tasks, so a solution to the one precise bullet would not constitute a solution to the whole card.
- **Repair:** replace the external placeholders with explicit problem statements or split the precise derivative-zero exercise into its own card.

### P-XKYOG is truncated and contradicts the principal-logarithm claim

- **Object and need:** `P-XKYOG` in `SRC-UNSORTED-COMPLEX-ANALYSIS`.
- **Observed evidence:** the card begins mid-sentence with "equations take the form," then asks to use the polar Cauchy--Riemann equations to show that the principal logarithm is holomorphic on $r>0$, $-\pi<\theta<\pi$, and also to show that this same logarithm is "not continuous in $r>0$." On the stated slit plane the principal logarithm is holomorphic and therefore continuous.
- **Source verification:** `assets/attachments/extracted/Questions_from_Tie.md` and the parallel UGA Fall 2015 card `P-AMD-YDNWHPDM` restore the omitted part (a), but both preserve the same final phrase "not continuous in $r>0$." Thus the truncation is local, while the contradictory continuity clause is source-level rather than an extraction artifact.
- **Impact and owner:** the omitted polar Cauchy--Riemann setup is recoverable, but the final source claim still requires correction before the full exercise can receive a source-faithful proof.
- **Repair:** correct the source-level final clause to the intended nonextendability statement (for example, nonexistence of a continuous extension to $\CC^\times$) before authoring the complete proof.

### P-DEJGY(b)(ii) omits the second level-set value

- **Object and need:** `P-DEJGY`; part (b)(ii) asks for the angles of intersection between the level curves `Re(f)=0` and `Im(f)` for $f(z)=z^2$.
- **Observed evidence:** the second expression is not an equation and therefore does not specify a level curve. Part (b)(i) discusses the level curves of both real and imaginary parts, but part (ii) provides the level value only for the real part.
- **Impact and owner:** the requested pair of curves is underdetermined. The likely intended second curve is $\operatorname{Im}f=0$, but inserting that value would alter the problem statement without source support.
- **Source verification:** `assets/attachments/extracted/Questions_from_Tie.md`, Fall 2016 problem 2(b)(ii), contains the same incomplete phrase `Re(f)=0` and `Im(f)`; the missing imaginary level is therefore a source-level omission.
- **Repair:** correct the source-level statement by specifying the intended imaginary-part level before attaching a solution.

### E-QVMUV has inconsistent Laurent-coefficient notation and an incorrect integral index

- **Object and need:** `E-QVMUV`; the card is intended to state the Cauchy integral formula for Laurent coefficients and the annulus of convergence.
- **Observed evidence:** the opening display reads `f(z) \sum_{k\in\ZZ} c_k(z-z_0)^k` with the equality sign missing; the asserted formula labels the coefficient $c_k$ but divides by $(z-z_0)^{n+1}$; the convergence radii are then written in terms of coefficients $a_{\pm n}$ rather than the $c_k$ introduced above. These are mutually inconsistent variable names in the mathematical statement, not merely presentation differences.
- **Impact and owner:** the card does not currently state a single well-defined coefficient formula. The intended standard formula is plausibly $c_k=(2\pi i)^{-1}\int_\gamma f(z)(z-z_0)^{-k-1}\,dz$, with radii expressed using the same coefficients, but the unsorted card has no independent source establishing which local symbols were intended.
- **Uncertainty:** the local inconsistencies are verified; `SRC-UNSORTED-COMPLEX-ANALYSIS` supplies no independent provenance for the card.
- **Repair:** recover the originating source or notes and normalize all coefficient/index variables from that source before attaching a proof.

### P-4Y4QT has an unbound parameter and an incompatible convergence range

- **Object and need:** `P-4Y4QT` in `SRC-CA-ART-T34TG3`; the problem says “Let $0<a<4$” but asks to evaluate $\int_0^\infty x^{\alpha-1}/(1+x^3)\,dx$, so the parameter in the integrand is not bound by the stated hypothesis.
- **Observed evidence:** the local Spring 2020 HW 3 collection has no provenance beyond a relation to `SRC-TEXT-SS03`. The same wording is preserved in the older complex-analysis notes. Independently, the displayed integral converges exactly for $0<\operatorname{Re}\alpha<3$: near $0$ it behaves like $x^{\alpha-1}$ and near infinity like $x^{\alpha-4}$. Thus even identifying $a=\alpha$ would make the stated upper range $a<4$ incompatible with convergence on $3\le a<4$.
- **Impact and owner:** no source-faithful numerical/formula answer is determined by the current statement. The homework/card source record owns recovery of whether the intended denominator was $1+x^4$, the intended range was $0<a<3$, or another correction was meant.
- **Uncertainty:** the local wording and convergence obstruction are verified; no authoritative provenance for this homework card has been identified.
- **Repair:** recover the originating homework/source and correct the bound parameter and convergence range from that source before attaching a solution.

### P-CASP25E is false as printed in the official Spring 2025 UCSD source

- **Object and need:** `P-CASP25E` in `SRC-UCSD-CA-SPRING-2025`; the source claims that a bounded sequence of holomorphic functions on $\mathbb D$ must converge locally uniformly if it converges pointwise on an arbitrary convergent sequence $z_m\to z_*\in\mathbb D$.
- **Observed evidence:** direct inspection of Problem 5 in the official Spring 2025 UCSD PDF confirms that no distinctness hypothesis is imposed on the points $z_m$. Taking $z_m\equiv0$ and $f_n(z)=(-1)^n z$ gives a uniformly bounded sequence of holomorphic functions with $f_n(z_m)=0$ for every $m,n$, while $(f_n)$ does not converge locally uniformly on any compact set containing a nonzero point.
- **Impact and owner:** the printed statement is false. The usual Vitali/Montel argument becomes valid if the set of testing points has an accumulation point in $\mathbb D$, for example if the $z_m$ are distinct and converge in $\mathbb D$. The source/card statement owns the repair.
- **Uncertainty:** the source wording and counterexample are verified; no independent erratum has been located.
- **Repair:** recover an erratum or corrected copy before adding a missing distinctness/accumulation hypothesis; otherwise retain the card as a documented source defect.

### P-CASP13E is false as printed in the official Spring 2013 UCSD source

- **Object and need:** `P-CASP13E` in `SRC-UCSD-CA-SPRING-2013`; the source claims that a sequence of distinct real numbers $x_n$ is the horizontal part of a zero set $x_n+i$ of some holomorphic function on the upper half-plane if and only if $\sum_n (x_n^2+4)^{-1}<\infty$.
- **Observed evidence:** direct inspection of page 2 of the official Spring 2013 UCSD PDF confirms the statement exactly as transcribed. Take $x_n=\sqrt n$. Then $x_n+i$ is a discrete sequence in $\mathbb C_+$, so by the Weierstrass product theorem there is an entire function, hence a function holomorphic on $\mathbb C_+$, vanishing at all $x_n+i$. But $\sum_n 1/(x_n^2+4)=\sum_n1/(n+4)$ diverges.
- **Impact and owner:** the necessity direction is false for unrestricted holomorphic functions. A Blaschke condition would be appropriate for bounded holomorphic functions, but boundedness is absent from the official source. The source/card statement owns the repair.
- **Uncertainty:** the source wording and counterexample are verified. The likely intended hypothesis is that $f$ is bounded, but no erratum has been located.
- **Repair:** recover an independent erratum or corrected copy before changing the statement; otherwise retain the card as a documented source defect rather than attaching a proof.

### P-CASP07C is false as printed in the official Spring 2007 UCSD source

- **Object and need:** `P-CASP07C` in `SRC-UCSD-CA-SPRING-2007`; the official problem asks to prove that for every function analytic on $B(0,2)$, the series $\sum_{n=1}^\infty f^{(n)}(z)$ converges in $\mathcal O(\mathbb D)$.
- **Observed evidence:** direct inspection of page 2 of the official Spring 2007 UCSD PDF confirms the displayed series is exactly $\sum_{n=1}^\infty f^{(n)}(z)$. Taking $f(z)=1/(3-z)$, which is analytic on $B(0,2)$, gives $f^{(n)}(0)=n!/3^{n+1}$, whose terms do not even tend to zero. Hence the series diverges at $0$.
- **Impact and owner:** the card is mathematically false as printed and cannot receive a valid proof without recovering an intended normalization or other missing hypothesis. The source/card statement owns the repair.
- **Uncertainty:** the source formula and counterexample are both verified; the intended corrected series is unknown.
- **Repair:** recover an erratum or independent version of the exam before changing the displayed series; otherwise retain the card as a documented source defect.

### P-8CA12 is false as printed in the official Spring 2017 UGA source

- **Object and need:** `P-8CA12` in `SRC-UGA-CA-SPRING-2017`; the source asks to prove that for every real $\alpha>1$, the equation $\sin z=e^{\alpha z^3}$ has exactly three solutions in $|z|<1$.
- **Observed evidence:** direct inspection of the official Spring 2017 UGA DOCX confirms the OMML exponent is $\alpha z^3$. Let $F(z)=\sin z-e^{\alpha z^3}$. Since $\alpha$ is real, $F(\bar z)=\overline{F(z)}$, so nonreal zeros occur in conjugate pairs with the same multiplicity. There are no real zeros in $(-1,1)$: for $-1<x<0$, $\sin x<0<e^{\alpha x^3}$; for $0\le x<1$, $\sin x<1\le e^{\alpha x^3}$. Hence the number of zeros in the unit disk, counted with multiplicity, must be even and cannot equal three.
- **Impact and owner:** the card is mathematically false as printed, so no valid solution can be attached without first recovering the intended equation or root count. The source/card statement owns the repair.
- **Uncertainty:** the falsity of the printed statement and the DOCX grouping are verified. A plausible intended equation is $\sin z=e^\alpha z^3$, for which a three-root Rouché argument is natural, but no source evidence currently establishes that correction.
- **Repair:** locate an independent copy or erratum for the Spring 2017 exam and replace the statement only when the intended formula is source-supported; otherwise retain the card as a documented source defect.

### P-8CA06 omits the hypothesis $f(0)=0$ in the official Fall 2017 UGA source

- **Object and need:** `P-8CA06` in `SRC-UGA-CA-FALL-2017`; the problem asks for a positive integer $m$ with $f(0)=\cdots=f^{(m-1)}(0)=0$ and then Schwarz-type bounds of order $m$.
- **Observed evidence:** direct inspection of UGA's official `Complex Analysis [Fall 2017].docx` confirms the source assumes only that $f:\mathbb E\to\mathbb E$ is analytic and is not identically zero in some neighborhood of the origin. It does not assume $f(0)=0$. The constant function $f\equiv1/2$ satisfies the printed hypotheses but contradicts part (a), since no positive $m$ can have $f(0)=0$.
- **Impact and owner:** both parts rely on $0$ being a zero of positive order; as printed the problem is false. The source/card statement owns the repair.
- **Uncertainty:** the omission is verified against the official DOCX and the counterexample is decisive. The natural correction is to add $f(0)=0$, but no independent erratum has yet been located.
- **Repair:** add the missing hypothesis only if supported by an independent source or explicit erratum; otherwise retain the card as a documented source defect rather than attaching a proof to the false statement.

### P-X7WUF has an unresolved provenance and residue-normalization defect

- **Object and need:** `P-X7WUF` in `SRC-UGA-CA-FALL-2016`; its residue formula for a pole of order $m$ omits the standard factor $1/(m-1)!$, and its owning collection does not identify its actual source.
- **Observed evidence:** the collection cites UGA's official `Complex Analysis [Fall 2016].docx`. Direct inspection of that DOCX on 2026-09-09 shows its problem list ending with the disk-automorphism/two-fixed-points problem corresponding to `P-8CA16`; no pole-of-order-$m$ residue problem or integral of $e^\tau/(\tau^2+\pi^2)^2$ occurs in the document. Independently, for $F(z)=z^{-3}+z^{-1}$ and $m=3$, the contour integral divided by $2\pi i$ equals the residue $1$, whereas the formula printed on `P-X7WUF(a)` gives $\frac{d^2}{dz^2}(1+z^2)|_{z=0}=2$.
- **Impact and owner:** `P-X7WUF(a)` is false for $m>2$, and the card cannot presently be source-verified against its owning collection. The collection/card provenance and statement own the repair. The parallel unsorted card `E-YZUOC` has now been mathematically resolved by an explicit erratum and proof on that card.
- **Uncertainty:** the mismatch with the cited DOCX is verified; the actual source of `P-X7WUF` has not yet been identified.
- **Repair:** recover the true source for `P-X7WUF`, move or re-provenance the card accordingly, and restore the factor $1/(m-1)!$ before attaching its solution.

### P-MMAQ-WV7QEYSPXM omits the infinite-cyclic injectivity hypothesis

- **Object and need:** `P-MMAQ-WV7QEYSPXM`, Dummit--Foote §5.5 Exercise 6; the local statement must retain every hypothesis needed for the semidirect-product isomorphism.
- **Observed evidence:** the local card states the result for an arbitrary cyclic group $K$. Dummit--Foote's exercise adds: if $K$ is infinite, assume both $\varphi_1$ and $\varphi_2$ are injective. The same wording is independently reproduced in University of Utah Math 6320 Exercise 4 (DF-5.5.6-7).
- **Impact and owner:** without injectivity in the infinite case, conjugate finite cyclic images can be generated by different powers while the corresponding power map $K\to K$ is not an automorphism, so the requested construction is not justified. The problem card owns the repair.
- **Uncertainty:** the omitted clause is verified against two reproductions of the source exercise; no ambiguity remains about the intended hypothesis.
- **Repair:** restore the infinite-case injectivity clause on `P-MMAQ-WV7QEYSPXM` before attaching a proof.

### P-HGRO11 does not specify the coefficient field

- **Object and need:** `P-HGRO11` in `SRC-HARVARD-GROUPS-ORAL`; deciding whether a determinant-one matrix group is simple requires the coefficient field and whether the intended group is $SL_2(F)$ or its projective quotient.
- **Observed evidence:** both the preserved Harvard source extraction and the local card ask only whether “the group of $2\times2$ matrices of determinant $1$” is simple, with no coefficient field. For example, if $\operatorname{char}F\ne2$, then $-I$ is a nontrivial central element of $SL_2(F)$, while simplicity statements for $PSL_2(F)$ depend on $F$.
- **Impact and owner:** there is no source-faithful yes/no answer to the card as written. The Harvard group-orals source/card record owns recovery of the intended field or clarification that the question concerns a particular projective special linear group.
- **Uncertainty:** verified against the retained Harvard PDF extraction; the omitted field may have been supplied orally or by surrounding course context not present in the preserved question list.
- **Repair:** recover the intended coefficient field/group from an independent Harvard source or explicitly mark the source question as underdetermined before solution authorship resumes.

## Workflow and rendering papercuts

### Primary local repository connector can silently become unavailable

- **Object and need:** local-repository work through the Chat On Steroids connector; repository reads and terminal commands should remain available while a scoped authoring stream is active.
- **Observed evidence:** on 2026-09-09, the first attempt to read `AGENTS.md`, `CONTRIBUTING.md`, git status, and git history failed before executing with `Tunnel-client has not been seen for 300 seconds. Ensure tunnel-client is running and connected.` The secondary local connector was available and executed the same commands successfully.
- **Impact and owner:** repository work is blocked when no secondary connector is available; with a secondary connector, the failure still adds avoidable recovery work and makes the primary connection state misleading. This is tooling/infrastructure-owned rather than corpus-owned.
- **Uncertainty:** verified for one primary-connector call in this session; the duration and root cause of the disconnect were not observable from the repository side.
- **Repair:** make connector liveness visible before invocation or transparently fail over to an available local connector, so repository reads do not fail solely because one tunnel has aged out.
