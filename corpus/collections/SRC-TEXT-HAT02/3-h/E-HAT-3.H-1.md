---
schema: qual/card@1
id: E-HAT-3.H-1
kind: problem
title: "Homology of $S^1$ with twisted $\\ZZ$ coefficients"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.H, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: bundles of groups over $S^1$ are
    $\ZZ[\pi]$-modules, so the nontrivial one has monodromy $t\mapsto-1$; the cellular chain complex
    tensored with the twisted module has boundary $t-1\mapsto-2$; $\ker(-2)=0$ and
    $\operatorname{coker}(-2)=\ZZ_2$ give $H_1=0$, $H_0=\ZZ_2$; and the cochain complex
    $\operatorname{Hom}_{\ZZ[\pi]}(\ZZ[\pi],M)\cong M$ with the transposed differential gives
    $H^0=0$, $H^1=\ZZ_2$. Added: the two-homomorphism count behind 'the nontrivial bundle', the
    injectivity of multiplication by $2$ used in computing the cokernel, and the remark on why
    homology and cohomology sit in complementary degrees, none of which the earlier text stated. No
    defect found in the statement, §3.H Exercise 1. No retained solution set covers it.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 345 carries the running head 336.
    The durable part of the locator is that printed page; the file path names this machine's copy and
    `tmp/sources` does not survive a VM reset. No mathematics changed.
---

::: {.problem}
This is Exercise 1 of Section 3.H of Hatcher, *Algebraic Topology* (2002), printed p. 336, read in the copy retained on this machine as `tmp/sources/hatcher-2002-algebraic-topology.pdf` (printed page = PDF page - 9); the statement below is its wording.

Compute $H_*(S^1; E)$ and $H^*(S^1; E)$ for $E \to S^1$ the nontrivial bundle with fiber $\ZZ$.
:::

::: {.solution}
No retained solution set covers this exercise, so the computation is the card's own; it is the cellular chain and cochain complex of local coefficients, whose differential is read off from the monodromy.

::: pf

::: {.pf-step #bundle}
A bundle of groups $E\to S^1$ with fibre $\ZZ$ corresponds to a $\ZZ[\pi]$-module $M=\ZZ$ with $\pi=\pi_1(S^1)=\langle t\rangle$, that is, to a homomorphism $\rho\colon\pi\to\Aut(\ZZ)=\{\pm1\}$; the nontrivial bundle has $\rho(t)=-1$.

::: pf-proof
Proposition 3H.4 (p. 331) identifies bundles of groups over $S^1$ with $\ZZ[\pi]$-module structures on the fibre, and a $\ZZ$-module structure is an action of $\pi$ by group automorphisms of $\ZZ$, that is a homomorphism to $\{\pm1\}$. There are exactly two such homomorphisms, the trivial one and the one with $\rho(t)=-1$, and Example 3H.3 (p. 329) identifies the associated cover: if $\rho$ is onto, the subgroup $\pi'=\ker\rho$ has index $2$ and the cover $S^1_{\pi'}$ is $S^1$ again. The nontrivial bundle is the one with $\rho$ onto, so monodromy around the circle acts by $-1$.
:::

:::

::: {.pf-step #chains}
With $M$ the twisted module, the cellular chain complex of $S^1$ with local coefficients is
$$
0\to\ZZ\xrightarrow{-2}\ZZ\to0,
$$
in degrees $1$ and $0$.

::: pf-proof
$C_n(S^1;M)=C_n(\widetilde{S^1})\otimes_{\ZZ[\pi]}M$ (§3.H, p. 328), and these functors satisfy the Eilenberg--Steenrod axioms (p. 333), so the cellular computation of Theorem 2.35 (p. 139) applies. The two-cell complex has $C_0=\ZZ[\pi]$, $C_1=\ZZ[\pi]$ with $\partial e^1=(t-1)e^0$; tensoring over $\ZZ[\pi]$ with $M$ replaces $t$ by its action $-1$, so the boundary is multiplication by $(-1)-1=-2$.
:::

:::

::: {.pf-step #homology}
$H_1(S^1;E)=0$ and $H_0(S^1;E)\cong\ZZ_2$, all other homology vanishing.

::: pf-proof
$H_1=\ker(-2\colon\ZZ\to\ZZ)=0$ and $H_0=\operatorname{coker}(-2)=\ZZ/2\ZZ$, since multiplication by $2$ is injective on $\ZZ$ and has image $2\ZZ$. There are no chains above degree $1$, so the higher groups vanish.
:::

:::

::: {.pf-step #cohomology}
$H^0(S^1;E)=0$ and $H^1(S^1;E)\cong\ZZ_2$, all other cohomology vanishing.

::: pf-proof
Cohomology with local coefficients is the cohomology of $C^n(S^1;M)=\operatorname{Hom}_{\ZZ[\pi]}(C_n(\widetilde{S^1}),M)$ (p. 328), and $\operatorname{Hom}_{\ZZ[\pi]}(\ZZ[\pi],M)\cong M$ by evaluation at the identity, so the cochain complex is $M\xrightarrow{\delta}M$ with $\delta(\varphi)(e^1)=\varphi((t-1)e^0)=-2\varphi(e^0)$. Hence $H^0=\ker(-2)=0$ and $H^1=\operatorname{coker}(-2)=\ZZ_2$, with nothing above degree $1$.
:::

:::

::: {.pf-step}
$\boxed{H_n(S^1;E)=\ZZ_2\text{ for }n=0\text{ and }0\text{ otherwise};\quad H^n(S^1;E)=\ZZ_2\text{ for }n=1\text{ and }0\text{ otherwise}}$.

::: pf-proof
The two displays are steps [](#homology){.pf-ref} and [](#cohomology){.pf-ref}. The shift is the expected one: the twisted bundle has vanishing $H_0$ in cohomology and vanishing $H_1$ in homology, so the two computations sit in complementary degrees.
:::

:::

:::
:::
