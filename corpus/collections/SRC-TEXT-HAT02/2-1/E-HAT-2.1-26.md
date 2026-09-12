---
schema: qual/card@1
id: E-HAT-2.1-26
kind: problem
title: $H_1(X, A)$ not isomorphic to $\tilde{H}_1(X/A)$ for shrinking wedge of circles
classification:
  areas:
  - topology
  topics:
  - Homology
  - Relative Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 26; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof reviewed against the relevant chain, relative-homology, local-homology, or covering-space calculation.
---

Show that $H_1(X, A)$ is not isomorphic to $\tilde{H}_1(X/A)$ if $X = [0, 1]$ and $A$ is the sequence $1, {^1_2}, {^1_3}, \cdots$ together with its limit 0. [See Example 1.25.]

::: {.solution}
Let
\[
X=[0,1],
\qquad
A=\{0,1,1/2,1/3,\dots\}.
\]

<1>1. The group $H_1(X,A)$ is a countably generated free abelian group.
::: {.proof}
Since $X$ is contractible and $A$ is totally disconnected, the long exact sequence of the pair contains
\[
0=H_1(X)\longrightarrow H_1(X,A)
\longrightarrow H_0(A)\xrightarrow{\epsilon}H_0(X)\longrightarrow0.
\]
Each point of $A$ is a path component, so
\[
H_0(A)\cong\bigoplus_{a\in A}\mathbb Z[a],
\qquad H_0(X)\cong\mathbb Z,
\]
and $\epsilon$ is the augmentation map. Hence
\[
H_1(X,A)\cong\ker\epsilon.
\]
Taking $0$ as a distinguished point gives the free basis
\[
[a]-[0],\qquad a\in A-\{0\}.
\]
Thus $H_1(X,A)$ is free abelian of countable rank, in particular it is countable as a set.
:::

<1>2. The quotient $X/A$ is the shrinking wedge of countably many circles (the Hawaiian earring).
::: {.proof}
For each $n\ge1$, the interval
\[
I_n=[1/(n+1),1/n]
\]
has both endpoints in $A$. After all of $A$ is collapsed to one point, $I_n/\partial I_n$ becomes a circle. The diameters of these intervals tend to zero at the collapsed limit point, so the quotient topology is exactly the standard shrinking-wedge topology of the Hawaiian earring.
:::

<1>3. The group $H_1(X/A)$ is uncountable.
::: {.proof}
Let $C_n$ denote the $n$th circle of the shrinking wedge. For each binary sequence
\[
\varepsilon=(\varepsilon_1,\varepsilon_2,\dots)\in\{0,1\}^{\mathbb N},
\]
construct a loop $\gamma_\varepsilon$ by traversing $C_n$ once if $\varepsilon_n=1$ and staying at the wedge point if $\varepsilon_n=0$, using pairwise consecutive time intervals whose lengths tend to zero and accumulate only at the endpoint of the parameter interval. Because the circles $C_n$ shrink to the wedge point, this infinite concatenation is continuous.

For each $n$ there is a continuous retraction
\[
r_n:X/A\longrightarrow C_n
\]
that collapses all other circles to the wedge point. Hence the induced homomorphism
\[
(r_n)_*:H_1(X/A)\longrightarrow H_1(C_n)\cong\mathbb Z
\]
sends $[\gamma_\varepsilon]$ to $\varepsilon_n$. Therefore distinct binary sequences give distinct homology classes. Since $\{0,1\}^{\mathbb N}$ is uncountable, so is $H_1(X/A)$.
:::

<1>4. Consequently
\[
\boxed{H_1(X,A)\not\cong\widetilde H_1(X/A).}
\]
::: {.proof}
The quotient is path connected, so $\widetilde H_1(X/A)=H_1(X/A)$. By <1>1 the relative group is countable, while by <1>3 the quotient-space homology group is uncountable. Hence they cannot be isomorphic.
:::
:::
