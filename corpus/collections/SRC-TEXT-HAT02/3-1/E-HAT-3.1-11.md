---
schema: qual/card@1
id: E-HAT-3.1-11
kind: problem
title: Moore spaces show the universal coefficient splitting is not natural
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.1, Exercise 11; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the cochain, exact-sequence, and universal-coefficient calculations directly.
---

::: {.problem}
Let $X$ be a Moore space $M(\ZZ_m, n)$ obtained from $S^n$ by attaching a cell $e^{n+1}$ by a map of degree $m$.

(a) Show that the quotient map $X \to X/S^n = S^{n+1}$ induces the trivial map on $\widetilde{H}_i(-; \ZZ)$ for all $i$, but not on $H^{n+1}(-; \ZZ)$.
Deduce that the splitting in the universal coefficient theorem for cohomology cannot be natural.

(b) Show that the inclusion $S^n \hookrightarrow X$ induces the trivial map on $\widetilde{H}^i(-; \ZZ)$ for all $i$, but not on $H_n(-; \ZZ)$.
:::

::: {.solution}
The cellular chain complex of
\[
X=M(\ZZ_m,n)=S^n\cup_m e^{n+1}
\]
in the two relevant degrees is
\[
0\to\ZZ\xrightarrow{\,m\,}\ZZ\to0.
\]
Hence
\[
\widetilde H_n(X;\ZZ)=\ZZ_m,
\qquad
\widetilde H_i(X;\ZZ)=0\quad(i\ne n),
\]
while the cellular cochain complex gives
\[
\widetilde H^{n+1}(X;\ZZ)=\ZZ_m,
\qquad
\widetilde H^i(X;\ZZ)=0\quad(i\ne n+1).
\]

::: pf

::: pf-step

Let
\[
q:X\to X/S^n\cong S^{n+1}
\]
be the quotient map. Then $q_*$ is zero on all reduced integral homology groups.

::: pf-proof

The sphere has reduced homology only in degree $n+1$, but $\widetilde H_{n+1}(X)=0$. In degree $n$, the target sphere has zero homology. All other reduced groups on both sides vanish.

:::

:::

::: {.pf-step #s2}

Nevertheless
\[
q^*:H^{n+1}(S^{n+1};\ZZ)=\ZZ
\longrightarrow H^{n+1}(X;\ZZ)=\ZZ_m
\]
is reduction modulo $m$, hence is nonzero.

::: pf-proof

On cellular cochains, the quotient identifies the unique $(n+1)$-cell of $X$ with the top cell of $S^{n+1}$. Thus the cochain map in degree $n+1$ is the identity $\ZZ\to\ZZ$ before passing to cohomology. The target cohomology is the cokernel of multiplication by $m$, so the induced map is the quotient $\ZZ\to\ZZ_m$.

:::

:::

::: pf-step

Therefore the splitting in the cohomological universal coefficient theorem cannot be natural.

::: pf-proof

A natural splitting would express $H^{n+1}$ functorially as the direct sum of the Hom and Ext terms. Since $q_*$ is zero on all homology groups, naturality would force both induced Hom and Ext maps, and hence $q^*$, to be zero. This contradicts step [](#s2){.pf-ref}.

:::

:::

::: pf-step

For the inclusion
\[
i:S^n\hookrightarrow X,
\]
the induced map on reduced integral cohomology is zero in every degree.

::: pf-proof

The only nonzero reduced cohomology of $X$ is in degree $n+1$, while the sphere has nonzero reduced cohomology only in degree $n$. Thus there is no degree in which both source and target of $i^*$ are nonzero.

:::

:::

::: pf-step

But
\[
i_*:H_n(S^n;\ZZ)=\ZZ\to H_n(X;\ZZ)=\ZZ_m
\]
is reduction modulo $m$, hence nonzero.

::: pf-proof

The $n$-cell of the sphere is the $n$-cell of $X$. Passing from the cellular chain group to $H_n(X)$ quotients by the image $m\ZZ$ of the $(n+1)$-cell boundary. Thus $i_*$ is the quotient map $\ZZ\to\ZZ_m$.

:::

:::

:::

:::
