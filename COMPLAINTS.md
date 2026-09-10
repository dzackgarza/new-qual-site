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
- **Impact and owner:** the surviving text is both truncated and mathematically contradictory.
- **Repair:** recover the omitted preceding part and the intended final continuity/noncontinuity domain from the source before authoring a proof.

### P-V4OZH omits the value range for b and has a denominator typo

- **Object and need:** `P-V4OZH` in `SRC-UNSORTED-COMPLEX-ANALYSIS`; the card defines a product intended to be a finite Blaschke product and asks to prove that $f(z)=b$ has exactly $n$ solutions in the unit disk.
- **Observed evidence:** the first factor is written with denominator $1-\bar a_q z$ rather than $1-\bar a_1 z$, so the displayed definition contains an undefined index $q$. More importantly, no condition on $b$ is stated. For example, if all $a_k=0$, then $f(z)=z^n$; for $|b|>1$ the equation $z^n=b$ has no solution in $\mathbb D$, contradicting the claimed conclusion.
- **Impact and owner:** the intended theorem is valid for a finite Blaschke product and $|b|<1$, counting multiplicity, but neither the correct first denominator nor the hypothesis on $b$ is present in the local statement.
- **Uncertainty:** both defects are explicit in the card. The unsorted collection provides no independent provenance from which to restore the intended wording.
- **Repair:** recover the originating source and restore the first denominator and the required hypothesis on $b$ before attaching a proof.

### P-QGCXS has an unresolved statement transcription defect

- **Object and need:** `P-QGCXS` in `SRC-UNSORTED-COMPLEX-ANALYSIS` should state a complete mathematical problem before solution authorship.
- **Observed evidence:** the card asks for the standard roots-of-unity sine sum, but its final displayed term is written `\cdots \frac{2(n-1)\pi}{n}=0` with the `\sin` missing.
- **Impact and owner:** the intended mathematics is recognizable, but inserting the missing sine would alter source-authored problem text without independent provenance. The unsorted compilation/card statement owns the repair.
- **Uncertainty:** the local defect is explicit and verified. No independent source is attached to the card in the unsorted collection, so the intended exact wording has not been source-verified.
- **Repair:** recover the originating source and restore the missing symbol before attaching a solution.

### P-LLNJ7 needs uniform convergence in the vertical parameter

- **Object and need:** `P-LLNJ7` in `SRC-UNSORTED-COMPLEX-ANALYSIS`; the card assumes only that $f(x+iy)\to A$ as $x\to\infty$ for each fixed $y\in[0,b]$, with the same limit $A$, and concludes convergence of the integrals over the vertical segments $\gamma_x$.
- **Observed evidence:** take $b=1$, $x_0=1$, $A=0$, and choose a continuous nonnegative function $\phi$ supported in $[-1,1]$ with $\int\phi=c>0$. Define
  \[
  f(x+iy)=x^2\phi\bigl(x^2(y-1/x)\bigr),\qquad x\ge1,\ 0\le y\le1.
  \]
  This is continuous. For every fixed $y>0$, the argument $x^2y-x\to+\infty$, while for $y=0$ it equals $-x$; hence $f(x+iy)\to0$ for every fixed $y$. But for all sufficiently large $x$,
  \[
  \int_{\gamma_x}f(z)\,dz
  =i\int_0^1x^2\phi(x^2(y-1/x))\,dy
  =i\int_{-x}^{x^2-x}\phi(u)\,du
  =ic\ne0.
  \]
- **Impact and owner:** the claimed conclusion is false under pointwise convergence alone. Uniform convergence in $y$ (or another valid domination/equicontinuity hypothesis) would justify passing the limit through the finite-interval integral.
- **Uncertainty:** the counterexample is decisive. The card appears only in the unsorted complex-analysis compilation and has no independent provenance presently identified.
- **Repair:** recover the originating source and restore the intended uniformity or domination hypothesis before attaching a proof.

### P-HZ3G4 has the wrong half-plane of convergence

- **Object and need:** `P-HZ3G4` in `SRC-UNSORTED-COMPLEX-ANALYSIS`; the card asks to prove uniform convergence of $\sum_{n\ge1}\sin(nz)/2^n$ on the full half-plane $\{\Im z<\log 2\}$.
- **Observed evidence:** take $z=-iy$ with $y>\log 2$. Then $\sin(nz)=-i\sinh(ny)$, so
  \[
  \left|\frac{\sin(nz)}{2^n}\right|=\frac{\sinh(ny)}{2^n}\sim \frac12\left(\frac{e^y}{2}\right)^n,
  \]
  which does not tend to zero because $e^y/2>1$. Thus the series fails even pointwise on part of the stated region.
- **Impact and owner:** the card cannot receive the requested proof as written. The correct pointwise and compact-uniform region for the displayed series is the strip $|\Im z|<\log 2$; any source-faithful repair must determine whether a missing lower bound on $\Im z$ was intended.
- **Uncertainty:** the counterexample is decisive. The card appears only in `SRC-UNSORTED-COMPLEX-ANALYSIS`, with no independent source currently identified.
- **Repair:** recover the originating source and restore the intended convergence domain before attaching a solution.

### P-DFHS3 mixes the integration variable with an unexplained parameter

- **Object and need:** `P-DFHS3`; the card asks to calculate $\int_0^\infty ((1+z)^2(z+9x^2))^{-1}\,dx$.
- **Observed evidence:** the integration variable is $x$, but the first two factors use an unexplained symbol $z$. No hypothesis specifies $z$, its branch, or a range ensuring convergence and avoiding poles. The title reproduces the same mixed-variable expression.
- **Impact and owner:** the integral is not a single numerical problem as written. Replacing $z$ by $x$ or treating $z$ as a parameter would lead to different mathematics and cannot be chosen without source evidence.
- **Uncertainty:** the malformed local statement is verified; the unsorted collection supplies no independent provenance.
- **Repair:** recover the originating source and restore the intended variable/parameter before attaching a solution.

### P-DEJGY(b)(ii) omits the second level-set value

- **Object and need:** `P-DEJGY`; part (b)(ii) asks for the angles of intersection between the level curves `Re(f)=0` and `Im(f)` for $f(z)=z^2$.
- **Observed evidence:** the second expression is not an equation and therefore does not specify a level curve. Part (b)(i) discusses the level curves of both real and imaginary parts, but part (ii) provides the level value only for the real part.
- **Impact and owner:** the requested pair of curves is underdetermined. The likely intended second curve is $\operatorname{Im}f=0$, but inserting that value would alter the problem statement without source support.
- **Uncertainty:** the local omission is verified; the card appears in the unsorted complex-analysis compilation without independent provenance.
- **Repair:** recover the source and restore the omitted imaginary-part level before attaching a solution.

### E-QVMUV has inconsistent Laurent-coefficient notation and an incorrect integral index

- **Object and need:** `E-QVMUV`; the card is intended to state the Cauchy integral formula for Laurent coefficients and the annulus of convergence.
- **Observed evidence:** the opening display reads `f(z) \sum_{k\in\ZZ} c_k(z-z_0)^k` with the equality sign missing; the asserted formula labels the coefficient $c_k$ but divides by $(z-z_0)^{n+1}$; the convergence radii are then written in terms of coefficients $a_{\pm n}$ rather than the $c_k$ introduced above. These are mutually inconsistent variable names in the mathematical statement, not merely presentation differences.
- **Impact and owner:** the card does not currently state a single well-defined coefficient formula. The intended standard formula is plausibly $c_k=(2\pi i)^{-1}\int_\gamma f(z)(z-z_0)^{-k-1}\,dz$, with radii expressed using the same coefficients, but the unsorted card has no independent source establishing which local symbols were intended.
- **Uncertainty:** the local inconsistencies are verified; `SRC-UNSORTED-COMPLEX-ANALYSIS` supplies no independent provenance for the card.
- **Repair:** recover the originating source or notes and normalize all coefficient/index variables from that source before attaching a proof.

### E-XIT36 omits the series sign in its summation-by-parts task

- **Object and need:** `E-XIT36`; the card says “Use summation by parts to show that $\sin(n)/n$ converges.”
- **Observed evidence:** $\sin(n)/n$ is a sequence, whose convergence to $0$ is immediate and does not use summation by parts. The natural summation-by-parts problem is convergence of the series $\sum_{n\ge1}\sin(n)/n$, but the summation sign is absent from the card.
- **Impact and owner:** as written, the requested method does not match the mathematical assertion. Adding a summation sign would materially change the statement and therefore needs source support.
- **Uncertainty:** the mismatch is verified locally; the card appears only in the unsorted compilation and no originating source has been identified.
- **Repair:** recover the source and determine whether the intended object was the series $\sum \sin(n)/n$ before authoring a solution.

### E-N5RKI omits hypotheses needed for its boundary maximum-principle claim

- **Object and need:** `E-N5RKI`; the card asks to show that if $|f|=0$ on $\partial\Omega$, then either $f$ is constant or $f$ has a zero in $\Omega$.
- **Observed evidence:** the card does not state that $f$ is holomorphic on $\Omega$, continuous up to $\partial\Omega$, or that $\Omega$ is bounded. Without those data the boundary condition is not a usable maximum-principle hypothesis. The title suggests a holomorphic maximum-modulus argument, but those hypotheses are absent from the problem body.
- **Impact and owner:** the problem is incomplete as a mathematical proposition; the missing analytic/domain assumptions cannot be inferred safely from its current text.
- **Uncertainty:** the omission is verified in the local card; no independent provenance is attached through the unsorted collection.
- **Repair:** recover the originating statement and restore its holomorphicity, boundary-continuity, and domain hypotheses before attaching a proof.

### P-6YHN7 is false as written in the unsorted complex-analysis compilation

- **Object and need:** `P-6YHN7`; the card assumes holomorphic maps $f,g:\mathbb D\to\Omega$ with $f$ injective and $f(0)=g(0)$ and asks to prove $g(r\mathbb D)\subseteq f(r\mathbb D)$ for every $0<r<1$.
- **Observed evidence:** take $\Omega=\mathbb D$, $f(z)=z/2$, and $g(z)=z$. Then $f$ is injective, $f(0)=g(0)=0$, but $g(r\mathbb D)=r\mathbb D$ while $f(r\mathbb D)=(r/2)\mathbb D$, so the claimed inclusion fails for every $r>0$.
- **Impact and owner:** the statement cannot receive a valid Schwarz-lemma proof as written. A natural valid comparison would require $f$ to be a biholomorphism from $\mathbb D$ onto $\Omega$, so that $f^{-1}\circ g$ is a disk self-map fixing $0$, but that surjectivity hypothesis is absent.
- **Uncertainty:** the card appears only in `SRC-UNSORTED-COMPLEX-ANALYSIS`; no independent source or erratum has been identified.
- **Repair:** recover the originating source and restore the intended hypothesis before attaching a solution.

### E-YEIQ5 is false on a general region

- **Object and need:** `E-YEIQ5` in `SRC-UNSORTED-COMPLEX-ANALYSIS`; the card claims that a holomorphic function on an arbitrary region must be constant if it maps one simple closed curve in the region into the real axis.
- **Observed evidence:** take the annulus $\Omega=\{1/2<|z|<2\}$, the unit circle $\gamma\subset\Omega$, and $f(z)=z+z^{-1}$. Then $f$ is nonconstant and holomorphic on $\Omega$, while for $z=e^{it}$ one has $f(z)=2\cos t\in\mathbb R$. The usual harmonic-maximum-principle proof would require the bounded component of $\mathbb C\setminus\gamma$ to lie in the domain, which need not hold for a general region.
- **Impact and owner:** the card is false as written and cannot receive a valid proof without an additional hypothesis, such as requiring the interior of $\gamma$ to be contained in $\Omega$ (or imposing a suitable simply connected-domain hypothesis). The unsorted source/card statement owns the repair.
- **Uncertainty:** the counterexample is decisive. `SRC-UNSORTED-COMPLEX-ANALYSIS` has no independent provenance identifying the intended original statement.
- **Repair:** recover the originating source or an independent version and add only the source-supported missing hypothesis; otherwise retain the card as a documented source defect.

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

### P-X7WUF and E-YZUOC contain a residue formula missing the factorial normalization

- **Object and need:** `P-X7WUF` in `SRC-UGA-CA-FALL-2016` and the parallel unsorted card `E-YZUOC`; the residue formula for a pole of order $m$ must include the standard normalization, and the UGA collection provenance should identify the actual source of `P-X7WUF`.
- **Observed evidence:** the collection cites UGA's official `Complex Analysis [Fall 2016].docx`. Direct inspection of that DOCX on 2026-09-09 shows its problem list ending with the disk-automorphism/two-fixed-points problem corresponding to `P-8CA16`; no pole-of-order-$m$ residue problem or integral of $e^\tau/(\tau^2+\pi^2)^2$ occurs in the document. Independently, `P-X7WUF(a)` omits the factor $1/(m-1)!$ from the pole-of-order-$m$ residue formula. For example, for $F(z)=z^{-3}+z^{-1}$ and $m=3$, the contour integral divided by $2\pi i$ equals the residue $1$, whereas the stated right-hand side is $\frac{d^2}{dz^2}(1+z^2)|_{z=0}=2$.
- **Impact and owner:** both cards' part (a) is mathematically false for $m>2$ without the factor $1/(m-1)!$, and `P-X7WUF` additionally cannot be source-verified against its owning collection. The collection/card provenance and statements own the repair.
- **Uncertainty:** the mismatch with the cited DOCX is verified; the actual source of `P-X7WUF` has not yet been identified.
- **Repair:** recover the true source for `P-X7WUF`, move or re-provenance the card accordingly, and restore the factor $1/(m-1)!$ before attaching a solution.

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
