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
---

::: {.problem}
Show that homology groups $H_n^{lf}(X; G)$ can be defined using locally finite chains, which are formal sums $\sum_\sigma g_\sigma \sigma$ of singular simplices $\sigma: \Delta^n \to X$ with coefficients $g_\sigma \in G$, such that each $x \in X$ has a neighborhood meeting the images of only finitely many $\sigma$'s with $g_\sigma \neq 0$.
Develop this version of homology far enough to show that for a finite-dimensional locally compact CW complex $X$, $H_n^{lf}(X; G)$ can be computed using infinite cellular chains $\sum_\alpha g_\alpha e_\alpha^n$.
:::

::: {.solution}
A locally finite singular $n$-chain is a formal sum
$$
c=\sum_\sigma g_\sigma\sigma
$$
such that every point of $X$ has a neighborhood meeting the images of only finitely many simplices with nonzero coefficient. The usual singular boundary formula
$$
\partial\sigma=\sum_{i=0}^n(-1)^i\sigma\restrict[v_0,\dots,\widehat v_i,\dots,v_n]
$$
extends termwise to locally finite sums. It remains locally finite, since any neighborhood meeting the image of a face also meets the image of its parent simplex, and each simplex has only finitely many faces. Thus the locally finite chains form a chain complex
$$
C_*^{lf}(X;G),
$$
and we define
$$
H_*^{lf}(X;G)=H_*(C_*^{lf}(X;G)).
$$
Ordinary finite chains embed as a subcomplex. A proper map $f\colon X\to Y$ carries a locally finite family $\{\sigma\}$ of $X$ to a locally finite family $\{f\circ\sigma\}$ of $Y$: a compact neighborhood $K$ of a point of $Y$ has compact inverse image, which meets only finitely many of the $\sigma$, hence $K$ meets only finitely many of the images. When in addition only finitely many of the $\sigma$ with $g_\sigma\neq0$ map to any one simplex — as for a covering projection, or whenever the fibres of $f$ on simplices are finite — the coefficient sums are finite and $f$ induces $f_*\colon C_*^{lf}(X;G)\to C_*^{lf}(Y;G)$. With infinite multiplicities the termwise sum is not defined, so this is a genuine hypothesis rather than a formality.

Now suppose $X$ is a finite-dimensional locally compact CW complex. Then $X$ is locally finite: a point $x$ has a compact neighborhood $N$, and by Proposition A.1 (p. 520) $N$ is contained in a finite subcomplex of $X$, so $N$ meets only finitely many cells. Hence an arbitrary formal cellular chain
$$
\sum_\alpha g_\alpha e_\alpha^n
$$
is locally finite precisely in the geometric sense required above, and the cellular boundary is well-defined termwise. Indeed, near any point only finitely many cells occur, so only finitely many terms can contribute locally.

Filter $C_*^{lf}(X;G)$ by the skeleta. The relative locally finite homology of successive skeleta is concentrated in the cell dimension:
$$
H_k^{lf}(X^n,X^{n-1};G)=0\quad(k\ne n),
$$
while
$$
H_n^{lf}(X^n,X^{n-1};G)
\cong\prod_{e_\alpha^n}G,
$$
the product rather than the direct sum, since infinitely many $n$-cells may carry nonzero coefficients and all of them may be taken nonzero at once ($X$ is locally finite). Concretely the relative complex in degree $n$ consists of all formal sums $\sum_\alpha g_\alpha e^n_\alpha$, with no finiteness restriction, and it has no other degrees after passing to the quotient $X^n/X^{n-1}=\bigvee_\alpha S^n_\alpha$. The passage to the quotient is excision, Theorem 2.20 (p. 119), and the homology of that wedge is $\prod_\alpha G$ in degree $n$ and $0$ elsewhere. The long exact sequences of the pairs $(X^n,X^{n-1})$ are those of Theorem 2.16 (p. 117), available here because $C_*^{lf}(X^{n-1})\to C_*^{lf}(X^n)\to C_*^{lf}(X^n,X^{n-1})$ is short exact. The boundary maps in the exact couples of the skeletal filtration are therefore exactly the usual cellular incidence-number boundary maps, extended to these infinite locally finite sums.

Because $X$ is finite-dimensional, the skeletal filtration is finite in each total degree, so the standard cellular-homology argument — the five-lemma of Lemma 2.34 (p. 137) and the comparison with the singular complex in Theorem 2.35 (p. 139) — applies without convergence issues; the only change is that the chain groups are these products rather than direct sums, which affects none of the incidence-number algebra. It yields a chain equivalence between $C_*^{lf}(X;G)$ and the locally finite cellular complex
$$
C_n^{lf,cell}(X;G)=\left\{\sum_\alpha g_\alpha e_\alpha^n\right\},
$$
with the ordinary cellular boundary formula. Consequently
$$
\boxed{H_n^{lf}(X;G)
\cong H_n(C_*^{lf,cell}(X;G)).}
$$
Thus locally finite homology of a finite-dimensional locally compact CW complex is computed by infinite cellular chains.
:::
