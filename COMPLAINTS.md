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

### P-X7WUF is not present in the cited Fall 2016 UGA source and its residue formula omits a factorial

- **Object and need:** `P-X7WUF` in `SRC-UGA-CA-FALL-2016`; the local collection provenance should identify the actual source of each card, and the residue formula for a pole of order $m$ must include the standard normalization.
- **Observed evidence:** the collection cites UGA's official `Complex Analysis [Fall 2016].docx`. Direct inspection of that DOCX on 2026-09-09 shows its problem list ending with the disk-automorphism/two-fixed-points problem corresponding to `P-8CA16`; no pole-of-order-$m$ residue problem or integral of $e^\tau/(\tau^2+\pi^2)^2$ occurs in the document. Independently, `P-X7WUF(a)` omits the factor $1/(m-1)!$ from the pole-of-order-$m$ residue formula. For example, for $F(z)=z^{-3}+z^{-1}$ and $m=3$, the contour integral divided by $2\pi i$ equals the residue $1$, whereas the stated right-hand side is $\frac{d^2}{dz^2}(1+z^2)|_{z=0}=2$.
- **Impact and owner:** the card cannot be source-verified against its owning collection, and part (a) is mathematically false for $m>2$ without the factorial. The collection/card provenance and statement own the repair.
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
