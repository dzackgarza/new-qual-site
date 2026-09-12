---
schema: qual/card@1
id: E-HAT-3.F-2
kind: problem
title: "Mittag--Leffler condition and $\\varprojlim^1$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.F, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that $\varprojlim^1 G_i = 0$ if the sequence $\cdots \to G_2 \xrightarrow{\alpha_2} G_1 \xrightarrow{\alpha_1} G_0$ satisfies the Mittag–Leffler condition that for each $i$ the images of the maps $G_{i+n} \to G_i$ are independent of $n$ for sufficiently large $n$.

::: {.solution}
For a tower
\[
\cdots\xrightarrow{\alpha_2}G_1\xrightarrow{\alpha_1}G_0,
\]
write
\[
\Phi:\prod_{i\ge0}G_i\longrightarrow\prod_{i\ge0}G_i,
\qquad
\Phi((g_i))=(g_i-\alpha_{i+1}(g_{i+1}))_i.
\]
By definition,
\[
\varprojlim G_i=\ker\Phi,
\qquad
\varprojlim{}^1G_i=\operatorname{coker}\Phi.
\]
Thus it suffices to prove that $\Phi$ is surjective under the Mittag--Leffler hypothesis.

For each $i$, let
\[
I_i=\operatorname{im}(G_j\to G_i)
\]
for all sufficiently large $j$; this is well-defined by Mittag--Leffler stabilization. The bonding maps carry $I_{i+1}$ onto $I_i$. Indeed, choose $j$ large enough that both stable images have been reached. Then
\[
I_i=\operatorname{im}(G_j\to G_i)
=\alpha_{i+1}\bigl(\operatorname{im}(G_j\to G_{i+1})\bigr)
=\alpha_{i+1}(I_{i+1}).
\]
Hence the tower $(I_i)$ has surjective bonding maps, so its $\varprojlim{}^1$ vanishes: given $(b_i)\in\prod I_i$, choose $g_0$ arbitrarily and then recursively choose $g_{i+1}$ with
\[
\alpha_{i+1}(g_{i+1})=g_i-b_i.
\]
This solves $\Phi(g)=b$.

Now let $Q_i=G_i/I_i$. The quotient tower is pro-zero: for every $i$ some sufficiently long composite
\[
Q_j\longrightarrow Q_i
\]
is zero, since the image of $G_j\to G_i$ is then exactly $I_i$. Passing to a cofinal subsequence, we may assume each bonding map $Q_{i+1}\to Q_i$ is zero. For a zero-bonding tower,
\[
\Phi((q_i))=(q_i),
\]
so $\Phi$ is an isomorphism and $\varprojlim{}^1Q_i=0$.

The short exact sequence of towers
\[
0\to I_i\to G_i\to Q_i\to0
\]
gives the standard exact sequence for inverse limits and their first derived limits. Since both outer $\varprojlim{}^1$ terms vanish, so does the middle one:
\[
\boxed{\varprojlim{}^1G_i=0.}
\]
:::
