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
---

::: {.problem}
Compute $H_*(S^1; E)$ and $H^*(S^1; E)$ for $E \to S^1$ the nontrivial bundle with fiber $\ZZ$.
:::

::: {.solution}
Give $S^1$ its CW structure with one $0$-cell and one $1$-cell. By Proposition 3H.4 (p. 331) a bundle of groups $E\to S^1$ with fiber $\ZZ$ is the same thing as a $\ZZ[\pi]$-module $M=\ZZ$, $\pi=\pi_1(S^1)$, i.e. a homomorphism $\rho\colon\pi\to\operatorname{Aut}(\ZZ)=\{\pm1\}$; this is the case discussed in Example 3H.3 (p. 329), where $\pi'=\ker\rho$ is the subgroup of index $[\,\pi:\ker\rho\,]$ and the associated cover is $S^1_{\pi'}=S^1$ when $\rho$ is onto. The nontrivial bundle has $\rho$ onto, so $\rho(t)=-1$ for the generator $t$ of $\pi$: monodromy around the circle acts by $-1$.

Homology with coefficients in $M$ is by definition the homology of $C_n(S^1;M)=C_n(\widetilde{S^1})\otimes_{\ZZ[\pi]}M$ (§3.H, p. 328). These groups satisfy the long exact sequence of a pair and excision exactly as ordinary homology does (p. 333), so they are computed by cellular chains by the argument proving Theorem 2.35 (p. 139): use the two-cell complex with $C_0=\ZZ[\pi]$, $C_1=\ZZ[\pi]$. The boundary is $\partial e^1=(t-1)e^0$, and tensoring over $\ZZ[\pi]$ with $M$ replaces $t$ by $-1$, so the chain complex is
$$
0\longrightarrow \ZZ
\xrightarrow{(-1)-1=-2}\ZZ\longrightarrow0.
$$
Hence
$$
H_1(S^1;E)=\ker(-2)=0,
\qquad
H_0(S^1;E)=\operatorname{coker}(-2)\cong\ZZ_2.
$$

Cohomology with local coefficients is the cohomology of $C^n(S^1;M)=\operatorname{Hom}_{\ZZ[\pi]}(C_n(\widetilde{S^1}),M)$ (p. 328). Since $\operatorname{Hom}_{\ZZ[\pi]}(\ZZ[\pi],M)\cong M$ by evaluation at the identity, the cochain complex is $M\xrightarrow{\delta}M$ with $\delta(\varphi)(e^1)=\varphi\big((t-1)e^0\big)=(-2)\varphi(e^0)$, that is
$$
0\longrightarrow\ZZ
\xrightarrow{-2}\ZZ\longrightarrow0,
$$
so
$$
H^0(S^1;E)=\ker(-2)=0,
\qquad
H^1(S^1;E)=\operatorname{coker}(-2)\cong\ZZ_2.
$$
All other homology and cohomology groups vanish. Thus
$$
\boxed{H_n(S^1;E)=
\begin{cases}\ZZ_2,&n=0,\\0,&n\ne0,
\end{cases}}
$$
and
$$
\boxed{H^n(S^1;E)=
\begin{cases}\ZZ_2,&n=1,\\0,&n\ne1.
\end{cases}}
$$
:::
