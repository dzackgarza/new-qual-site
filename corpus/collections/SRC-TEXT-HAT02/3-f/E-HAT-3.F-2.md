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
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.F Exercise 2, printed page
    320; the statement matches word for word. Checked: with
    Φ((g_i)) = (g_i − α_{i+1}(g_{i+1})) on the product, lim G_i = ker Φ and
    lim¹ G_i = coker Φ (Hatcher's definition, p. 316); Mittag-Leffler makes the image
    of G_{i+n} in G_i stabilise at some I_i, and solving Φ(g) = h by choosing g_i in a
    stabilised preimage gives surjectivity of Φ, hence vanishing of lim¹. No defect.
---

::: {.problem}
Show that $\varprojlim^1 G_i = 0$ if the sequence $\cdots \to G_2 \xrightarrow{\alpha_2} G_1 \xrightarrow{\alpha_1} G_0$ satisfies the Mittag–Leffler condition that for each $i$ the images of the maps $G_{i+n} \to G_i$ are independent of $n$ for sufficiently large $n$.
:::

::: {.solution}
For a tower
$$
\cdots\xrightarrow{\alpha_2}G_1\xrightarrow{\alpha_1}G_0,
$$
write
$$
\Phi:\prod_{i\ge0}G_i\longrightarrow\prod_{i\ge0}G_i,
\qquad
\Phi((g_i))=(g_i-\alpha_{i+1}(g_{i+1}))_i.
$$
By definition,
$$
\varprojlim G_i=\ker\Phi,
\qquad
\varprojlim{}^1G_i=\operatorname{coker}\Phi.
$$
Thus it suffices to prove that $\Phi$ is surjective under the Mittag--Leffler hypothesis.

For each $i$, let
$$
I_i=\operatorname{im}(G_j\to G_i)
$$
for all sufficiently large $j$; this is well-defined by Mittag--Leffler stabilization. The bonding maps carry $I_{i+1}$ onto $I_i$. Indeed, choose $j$ large enough that both stable images have been reached. Then
$$
I_i=\operatorname{im}(G_j\to G_i)
=\alpha_{i+1}\bigl(\operatorname{im}(G_j\to G_{i+1})\bigr)
=\alpha_{i+1}(I_{i+1}).
$$
Hence the tower $(I_i)$ has surjective bonding maps, so its $\varprojlim{}^1$ vanishes. Precisely, since $\alpha_{i+1}(I_{i+1})=I_i$, the map $\Phi$ carries $\prod_i I_i$ into itself, so $\varprojlim{}^1I_i$ is the cokernel of the restriction of $\Phi$ to $\prod_i I_i$, and it is enough to solve $\Phi(g)=b$ with $g\in\prod_i I_i$, for each $b=(b_i)\in\prod_i I_i$. Take $g_0=0$, which lies in $I_0$, and then choose $g_{i+1}\in I_{i+1}$ recursively with
$$
\alpha_{i+1}(g_{i+1})=g_i-b_i.
$$
Each choice is possible: $g_i\in I_i$ by induction and $b_i\in I_i$, so $g_i-b_i\in I_i=\alpha_{i+1}(I_{i+1})$. The resulting $g=(g_i)\in\prod_i I_i$ satisfies
$$
g_i-\alpha_{i+1}(g_{i+1})=b_i\qquad\text{for all }i,
$$
that is, $\Phi(g)=b$.

Now let $Q_i=G_i/I_i$. The quotient tower is pro-zero: for every $i$ some sufficiently long composite
$$
Q_j\longrightarrow Q_i
$$
is zero, since the image of $G_j\to G_i$ is then exactly $I_i$. Since $\varprojlim$ and $\varprojlim{}^1$ do not change when the tower is replaced by a subsequence, with the appropriate composites of the $\alpha_i$ as bonding maps (Hatcher, page 313), we may pass to a cofinal subsequence and assume each bonding map $Q_{i+1}\to Q_i$ is zero. For a zero-bonding tower,
$$
\Phi((q_i))=(q_i),
$$
so $\Phi$ is an isomorphism and $\varprojlim{}^1Q_i=0$.

Taking products over $i$, the short exact sequence of towers
$$
0\to I_i\to G_i\to Q_i\to0
$$
gives a short exact sequence of two-term complexes $0\to\prod_i I_i\to\prod_i G_i\to\prod_i Q_i\to0$ whose boundary maps are $\delta$, and the snake lemma applied to $\delta$ yields the exact sequence
$$
0\to\varprojlim I_i\to\varprojlim G_i\to\varprojlim Q_i\to\varprojlim{}^1I_i\to\varprojlim{}^1G_i\to\varprojlim{}^1Q_i\to0.
$$
Since $\varprojlim{}^1I_i=0$ and $\varprojlim{}^1Q_i=0$, exactness at $\varprojlim{}^1G_i$ forces $\varprojlim{}^1G_i=0$:
$$
\boxed{\varprojlim{}^1G_i=0.}
$$
:::
