---
schema: qual/card@1
id: P-TOP-WORKSHOP-D9-03
kind: problem
title: Fundamental group and homology of $\RR^4\setminus S^1$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homology
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured the two computations into numbered steps and supplied what the prose compressed: that
    a loop bounds a 2-disc in R^4 because R^4 is simply connected, that a 2-disc can be pushed off
    the 1-dimensional circle by transversality since 2 + 1 < 4, and that the resulting null-homotopy
    stays in M; and, for homology, that compactifying adds the single point infinity so that
    A = S^1 disjoint union {point} has reduced cohomology Z in degrees 0 and 1 only, whence
    Alexander duality gives H-tilde_3 and H-tilde_2 of M, with H_0 = Z because M is connected.
    Also recorded why the answer is consistent with the general position computation, M being
    homotopy equivalent to S^2. Every macro used is one the preamble defines. Nothing was checked
    against a printed page.
---

::: {.problem}
(Michigan May ’09) Let $$S^1=\{(x,y,0,0)\in\RR^4\mid x^2+y^2=1\}$$ be the unit circle and consider $M=\RR^4\setminus S^1$.
Compute the fundamental group $\pi_1(M)$ and the homology groups $H_*(M)$ of $M$.
:::

::: {.solution}

The argument is the card's own; no source text or solution set is retained for it. Write $S^{1}=\{(x,y,0,0)\mid x^{2}+y^{2}=1\}\subset\RR^{4}$ and $M=\RR^{4}\setminus S^{1}$.

::: pf

::: {.pf-step #loop}
Every loop in $M$ is null-homotopic in $M$.

::: pf-proof
$M$ is an open subset of $\RR^{4}$ and $\RR^{4}$ is simply connected, so a loop $\gamma$ in $M$ bounds a map of the $2$-disc, $D\colon(D^{2},\partial D^{2})\to(\RR^{4},\gamma)$. The disc has dimension $2$ and $S^{1}$ has dimension $1$, and $2+1<4$, so the map $D$ may be perturbed rel boundary to a map into $\RR^{4}\setminus S^{1}=M$: by transversality a generic perturbation makes $D$ meet the submanifold $S^{1}$ of codimension $3$ in a set of dimension $2-3<0$, that is, in no point, and the perturbation may be taken fixed on the boundary, by the relative form of the transversality theorem for maps of pairs $((D^{2},\partial D^{2})\to(\RR^{4},\RR^{4}\setminus S^{1}))$, which applies because $\gamma$ already lands in $\RR^{4}\setminus S^{1}$. The resulting disc lies in $M$ and has boundary $\gamma$, so $\gamma$ is null-homotopic in $M$.
:::

:::

::: {.pf-step #pi1}
$\pi_{1}(M)=0$.

::: pf-proof
Step [](#loop){.pf-ref} shows every loop in $M$ is null-homotopic there, which is simple connectedness; $M$ is also path connected, being the complement of a codimension-$3$ subset of $\RR^{4}$, so any two points are joined by a path avoiding $S^{1}$ by the same general position argument applied to a path (dimension $1$, and $1+1<4$). Hence $\pi_{1}(M)=0$.
:::

:::

::: {.pf-step #compactify}
Compactifying, $M=S^{4}\setminus A$ where $A=S^{1}\sqcup\{\infty\}$.

::: pf-proof
$\RR^{4}\subset S^{4}=\RR^{4}\cup\{\infty\}$, and $S^{1}\subset\RR^{4}$ does not contain $\infty$; so $S^{4}\setminus(S^{1}\cup\{\infty\})=(\RR^{4}\cup\{\infty\})\setminus(S^{1}\cup\{\infty\})=\RR^{4}\setminus S^{1}=M$. The set $A=S^{1}\cup\{\infty\}$ is the disjoint union of the circle and the extra point, and it is compact and closed in $S^{4}$.
:::

:::

::: {.pf-step #cohomology-A}
$\widetilde H^{0}(A;\ZZ)\cong\ZZ$, $H^{1}(A;\ZZ)\cong\ZZ$, and all other reduced cohomology of $A$ vanishes.

::: pf-proof
$A$ is the disjoint union of two path-connected closed-and-open pieces, $S^{1}$ and $\{\infty\}$; reduced cohomology is additive over disjoint unions. For a point, $\widetilde H^{*}=0$; for the circle, $\widetilde H^{0}=0$, $H^{1}\cong\ZZ$ and higher groups vanish. The unreduced $\widetilde H^{0}$ of the two-point space $A$ is $\ZZ$, sitting in the sequence $0\to\widetilde H^{0}(A)\to H^{0}(A)\to\ZZ\to0$ with $H^{0}(A)=\ZZ^{2}$.
:::

:::

::: {.pf-step #duality}
Alexander duality gives $\widetilde H_{i}(M)\cong\widetilde H^{3-i}(A;\ZZ)$ for all $i$.

::: pf-proof
Alexander duality states that for a compact subset $A$ of $S^{n}$ and any abelian group $G$ there are isomorphisms $\widetilde H_{i}(S^{n}\setminus A;G)\cong\widetilde H^{n-i-1}(A;G)$. Here $n=4$ and $S^{4}\setminus A=M$, so $\widetilde H_{i}(M)\cong\widetilde H^{3-i}(A)$, which is the displayed form.
:::

:::

::: {.pf-step #homology}
$H_{0}(M)\cong\ZZ$, $H_{2}(M)\cong\ZZ$, $H_{3}(M)\cong\ZZ$, and all other homology vanishes.

::: pf-proof
By steps [](#duality){.pf-ref} and [](#cohomology-A){.pf-ref}: $\widetilde H_{3}(M)\cong\widetilde H^{0}(A)\cong\ZZ$, $\widetilde H_{2}(M)\cong\widetilde H^{1}(A)\cong\ZZ$, and $\widetilde H_{i}(M)=0$ for $i\neq2,3$ because the corresponding reduced cohomology of $A$ vanishes. Adding the reduced-to-unreduced correction in degree $0$, $H_{0}(M)=\ZZ$ since $M$ is path connected by step [](#pi1){.pf-ref}, and $H_{i}(M)=\widetilde H_{i}(M)$ for $i\geq1$.
:::

:::

::: {.pf-step}
$M$ is simply connected and $H_{i}(M)=\ZZ$ for $i=0,2,3$, zero otherwise.

::: pf-proof
Steps [](#pi1){.pf-ref} and [](#homology){.pf-ref}. As a check, $M$ is simply connected with a single nonzero higher homology group in degree $2$, freely generated, so by Hurewicz $M$ has the homology of $S^{2}$; indeed $M$ is homotopy equivalent to $S^{2}$, which the answer is consistent with.
:::

:::

:::

:::
