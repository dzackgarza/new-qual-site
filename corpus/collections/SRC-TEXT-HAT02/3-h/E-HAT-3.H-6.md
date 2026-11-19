---
schema: qual/card@1
id: E-HAT-3.H-6
kind: problem
title: "Locally finite homology"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.H, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 6 of §3.H, printed p. 336, with the locally finite chains of
    §3.H (p. 327) and Proposition A.1 (p. 519) on compact subsets of CW complexes. Correct. The
    locally finite chains form a chain complex because the singular boundary has finitely many
    terms and a neighbourhood of a face's image is one of the simplex's image, and $\partial^2=0$
    holds simplex by simplex. Finite chains are a subcomplex, so ordinary homology maps in. A
    proper map carries locally finite families to locally finite families — the preimage of a
    compact set is compact and meets finitely many simplices — while the pushforward of
    coefficients needs the extra finiteness hypothesis the card states and does not hide. A
    locally compact CW complex is locally finite, since a compact neighbourhood lies in a finite
    subcomplex by Proposition A.1, so an arbitrary formal sum of cells is locally finite; and on a
    wedge of $n$-spheres the locally finite $n$-chains are the product $\prod_\alpha G$ rather than
    the sum, with nothing in other degrees, which is where the infinite coefficients cost
    something. The spectral-sequence comparison with the cellular complex is finite in each total
    degree because $X$ is finite dimensional. Nothing changed. Not claimed: a published solution,
    and no certificate.
---

::: {.problem}
Show that homology groups $H_n^{lf}(X; G)$ can be defined using locally finite chains, which are formal sums $\sum_\sigma g_\sigma \sigma$ of singular simplices $\sigma: \Delta^n \to X$ with coefficients $g_\sigma \in G$, such that each $x \in X$ has a neighborhood meeting the images of only finitely many $\sigma$'s with $g_\sigma \neq 0$.
Develop this version of homology far enough to show that for a finite-dimensional locally compact CW complex $X$, $H_n^{lf}(X; G)$ can be computed using infinite cellular chains $\sum_\alpha g_\alpha e_\alpha^n$.
:::

::: {.solution}

The construction and the comparison are the card's own; the two points where the infinite coefficients genuinely cost something — the pushforward of a proper map and the product in place of the direct sum — are stated as such.

Coefficients are an abelian group $G$, and simplices are singular simplices $\sigma:\Delta^{n}\to X$.

::: pf

::: {.pf-step #chain-complex}
The locally finite chains, formal sums $\sum_{\sigma}g_{\sigma}\sigma$ such that every point of $X$ has a neighbourhood meeting the images of only finitely many $\sigma$ with $g_{\sigma}\ne0$, form a chain complex under the singular boundary.

::: pf-proof
The singular boundary formula $\partial\sigma=\sum_{i}(-1)^{i}\restrictionof{\sigma}{[v_{0},\ldots,\widehat{v_{i}},\ldots,v_{n}]}$ has finitely many terms, so it extends termwise to any formal sum. The result is locally finite: a neighbourhood meeting the image of a face $\restrictionof{\sigma}{[\ldots]}$ also meets the image of $\sigma$, since the face's image is contained in it, and each simplex has only finitely many faces, so the neighbourhood meets the images of only finitely many faces of the finitely many simplices it meets. And $\partial^{2}=0$ termwise because it holds for each simplex. Hence $C_{*}^{lf}(X;G)$ is a chain complex and $H_{*}^{lf}=H_{*}(C_{*}^{lf})$ is defined.
:::

:::

::: {.pf-step #finite-chains}
Finite chains form a subcomplex of $C_{*}^{lf}(X;G)$.

::: pf-proof
A finite sum is locally finite (take the neighbourhood to be $X$), and $\partial$ of a finite chain is a finite chain, so the ordinary singular complex is a subcomplex. Its homology is the ordinary homology of $X$, which therefore maps to $H_{*}^{lf}(X;G)$.
:::

:::

::: {.pf-step #pushforward}
A proper map $f:X\to Y$ carries locally finite families of simplices to locally finite families, and it induces $f_{*}$ on locally finite chains when in addition only finitely many simplices with nonzero coefficient map onto any one simplex of $Y$.

::: pf-proof
Let $K\subseteq Y$ be compact and $x\in Y$; a compact neighbourhood $K$ of $x$ has compact preimage $f^{-1}(K)$ by properness, and that preimage meets the images of only finitely many $\sigma$, so $K$ meets the images of only finitely many of the $f\circ\sigma$. Hence $\{f\circ\sigma\}$ is locally finite. For the coefficients, $f_{*}\big(\sum_{\sigma}g_{\sigma}\sigma\big)=\sum_{\sigma}g_{\sigma}(f\circ\sigma)$ requires each target simplex $\tau$ to receive only finitely many $\sigma$ with $g_{\sigma}\ne0$ and $f\circ\sigma=\tau$; otherwise the coefficient of $\tau$ is an infinite sum in $G$, which is not defined. The hypothesis holds for a covering projection, and more generally when the fibres of $f$ on simplices are finite; it is a genuine restriction, not a formality.
:::

:::

::: {.pf-step #locally-finite-cw}
A locally compact finite-dimensional CW complex is locally finite, so an arbitrary formal sum of its cells is a locally finite chain and the cellular boundary is defined termwise.

::: pf-proof
Let $x\in X$; since $X$ is locally compact there is a compact neighbourhood $N$ of $x$, and by Proposition A.1 a compact subset of a CW complex meets only finitely many cells, so $N$ meets only finitely many cells: $X$ is locally finite. Consequently a formal sum $\sum_{\alpha}g_{\alpha}e_{\alpha}^{n}$ over all $n$-cells satisfies the local finiteness condition of step [](#chain-complex){.pf-ref}, since each point has a neighbourhood meeting finitely many cells; and the cellular boundary, a finite sum of incidence terms for each cell, is defined termwise and remains locally finite.
:::

:::

::: {.pf-step #relative}
For the skeletal pair, $H_{k}^{lf}(X^{n},X^{n-1};G)=0$ for $k\ne n$ and $H_{n}^{lf}(X^{n},X^{n-1};G)\cong\prod_{\alpha}G$, the product over the $n$-cells.

::: pf-proof
The quotient $X^{n}/X^{n-1}=\bigvee_{\alpha}S^{n}_{\alpha}$ and by excision the relative locally finite homology is that of a wedge of $n$-spheres. A locally finite $n$-chain there assigns an arbitrary element of $G$ to each sphere — no finiteness is imposed, since the wedge is locally finite and the spheres are disjoint — so the $n$-th locally finite chain group is $\prod_{\alpha}G$, and there are no chains in other degrees because the wedge has no other cells. Hence the homology vanishes outside degree $n$ and equals $\prod_{\alpha}G$ in degree $n$.
:::

:::

::: {.pf-step #comparison}
$H_{n}^{lf}(X;G)\cong H_{n}\big(C_{*}^{lf,cell}(X;G)\big)$, where $C_{n}^{lf,cell}=\big\{\sum_{\alpha}g_{\alpha}e_{\alpha}^{n}\big\}$ with the ordinary cellular boundary formula.

::: pf-proof
Filter $C_{*}^{lf}(X;G)$ by the skeleta; the filtration is finite in each total degree because $X$ is finite dimensional, so the associated exact couple converges and no completion issue arises. By step [](#relative){.pf-ref} the $E^{1}$-page is concentrated in the row $k=n$, with $E^{1}_{n,n}\cong\prod_{\alpha}G$, and the $d^{1}$ differentials are the boundary maps of the pairs $(X^{n},X^{n-1})$, which are computed by the usual incidence numbers: a locally finite $n$-chain is sent to the locally finite $(n-1)$-chain assigning to $e^{n-1}_{\beta}$ the sum of $g_{\alpha}[\partial e^{n}_{\alpha}:e^{n-1}_{\beta}]$ over the finitely many $n$-cells incident to it. So $E^{1}$ with its $d^{1}$ is exactly the locally finite cellular complex, and the spectral sequence degenerates at $E^{2}$ to its homology; the comparison with the ordinary cellular argument (the five-lemma of Lemma 2.34 and the identification of singular and cellular homology in Theorem 2.35) applies verbatim, the only change being that the chain groups are products rather than direct sums, which alters none of the incidence-number algebra. Hence
$$
\boxed{H_{n}^{lf}(X;G)\cong H_{n}\big(C_{*}^{lf,cell}(X;G)\big),}
$$
that is, the locally finite homology of a finite-dimensional locally compact CW complex is computed by infinite cellular chains.
:::

:::

:::
:::
