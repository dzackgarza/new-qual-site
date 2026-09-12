---
schema: qual/card@1
id: E-HAT-3.1-11
kind: problem
title: Hatcher Section 3.1 Exercise 11
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

# E-HAT-3.1-11

Let $X$ be a Moore space $M(\mathbb{Z}_m, n)$ obtained from $S^n$ by attaching a cell $e^{n+1}$ by a map of degree $m$.

(a) Show that the quotient map $X \to X/S^n = S^{n+1}$ induces the trivial map on $\widetilde{H}_i(-; \mathbb{Z})$ for all $i$, but not on $H^{n+1}(-; \mathbb{Z})$.
Deduce that the splitting in the universal coefficient theorem for cohomology cannot be natural.

(b) Show that the inclusion $S^n \hookrightarrow X$ induces the trivial map on $\widetilde{H}^i(-; \mathbb{Z})$ for all $i$, but not on $H_n(-; \mathbb{Z})$.

::: {.solution}
The cellular chain complex of
\[
X=M(\mathbb Z_m,n)=S^n\cup_m e^{n+1}
\]
in the two relevant degrees is
\[
0\to\mathbb Z\xrightarrow{\,m\,}\mathbb Z\to0.
\]
Hence
\[
\widetilde H_n(X;\mathbb Z)=\mathbb Z_m,
\qquad
\widetilde H_i(X;\mathbb Z)=0\quad(i\ne n),
\]
while the cellular cochain complex gives
\[
\widetilde H^{n+1}(X;\mathbb Z)=\mathbb Z_m,
\qquad
\widetilde H^i(X;\mathbb Z)=0\quad(i\ne n+1).
\]

<1>1. Let
\[
q:X\to X/S^n\cong S^{n+1}
\]
be the quotient map. Then $q_*$ is zero on all reduced integral homology groups.
::: {.proof}
The sphere has reduced homology only in degree $n+1$, but $\widetilde H_{n+1}(X)=0$. In degree $n$, the target sphere has zero homology. All other reduced groups on both sides vanish.
:::

<1>2. Nevertheless
\[
q^*:H^{n+1}(S^{n+1};\mathbb Z)=\mathbb Z
\longrightarrow H^{n+1}(X;\mathbb Z)=\mathbb Z_m
\]
is reduction modulo $m$, hence is nonzero.
::: {.proof}
On cellular cochains, the quotient identifies the unique $(n+1)$-cell of $X$ with the top cell of $S^{n+1}$. Thus the cochain map in degree $n+1$ is the identity $\mathbb Z\to\mathbb Z$ before passing to cohomology. The target cohomology is the cokernel of multiplication by $m$, so the induced map is the quotient $\mathbb Z\to\mathbb Z_m$.
:::

<1>3. Therefore the splitting in the cohomological universal coefficient theorem cannot be natural.
::: {.proof}
A natural splitting would express $H^{n+1}$ functorially as the direct sum of the Hom and Ext terms. Since $q_*$ is zero on all homology groups, naturality would force both induced Hom and Ext maps, and hence $q^*$, to be zero. This contradicts <1>2.
:::

<1>4. For the inclusion
\[
i:S^n\hookrightarrow X,
\]
the induced map on reduced integral cohomology is zero in every degree.
::: {.proof}
The only nonzero reduced cohomology of $X$ is in degree $n+1$, while the sphere has nonzero reduced cohomology only in degree $n$. Thus there is no degree in which both source and target of $i^*$ are nonzero.
:::

<1>5. But
\[
i_*:H_n(S^n;\mathbb Z)=\mathbb Z\to H_n(X;\mathbb Z)=\mathbb Z_m
\]
is reduction modulo $m$, hence nonzero.
::: {.proof}
The $n$-cell of the sphere is the $n$-cell of $X$. Passing from the cellular chain group to $H_n(X)$ quotients by the image $m\mathbb Z$ of the $(n+1)$-cell boundary. Thus $i_*$ is the quotient map $\mathbb Z\to\mathbb Z_m$.
:::
:::
