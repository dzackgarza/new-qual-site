---
schema: qual/card@1
id: E-HAT-2.B-1
kind: problem
title: "Homology of complements of wedges and disjoint unions in spheres"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the Alexander-duality and Mayer--Vietoris calculations and all degree shifts.
---

::: {.problem}
Compute $H_i(S^n - X)$ when $X$ is a subspace of $S^n$ homeomorphic to $S^k \vee S^\ell$ or to $S^k \amalg S^\ell$.
:::

::: {.solution}
We use Alexander duality in the form
\[
\widetilde H_i(S^n-X;\ZZ)\cong \widetilde H^{\,n-i-1}(X;\ZZ)
\]
for these compact locally contractible subspaces of $S^n$.

::: pf

::: {.pf-step #s1}

If $X=S^k\vee S^\ell$, then
\[
\widetilde H^j(X)\cong
\begin{cases}
\ZZ,&j=k\ne\ell,\\
\ZZ,&j=\ell\ne k,\\
\ZZ^2,&j=k=\ell,\\
0,&\text{otherwise}.
\end{cases}
\]

::: pf-proof

Reduced cohomology takes a finite wedge to the direct sum of the reduced cohomologies of the two spheres. Each sphere has one copy of $\ZZ$ in its dimension and zero reduced cohomology elsewhere.

:::

:::

::: pf-step

Consequently, for $X=S^k\vee S^\ell$,
\[
\widetilde H_i(S^n-X)\cong
\begin{cases}
\ZZ,&i=n-k-1\ne n-\ell-1,\\
\ZZ,&i=n-\ell-1\ne n-k-1,\\
\ZZ^2,&i=n-k-1=n-\ell-1,\\
0,&\text{otherwise}.
\end{cases}
\]

::: pf-proof

Apply Alexander duality to step [](#s1){.pf-ref}, replacing the cohomological degree $j$ by $n-i-1$.

:::

:::

::: pf-step

If $X=S^k\amalg S^\ell$, then in addition to the two positive-dimensional sphere classes there is
\[
\widetilde H^0(X)\cong\ZZ.
\]
Thus
\[
\widetilde H_i(S^n-X)
\cong
\widetilde H^{\,n-i-1}(S^k\amalg S^\ell).
\]
Explicitly this contributes one copy of $\ZZ$ in degree $i=n-1$, and copies of $\ZZ$ in degrees $n-k-1$ and $n-\ell-1$ (combined to $\ZZ^2$ when $k=\ell$).

::: pf-proof

A disjoint union of two connected spaces has reduced $H^0$ equal to $\ZZ$, while its positive-degree cohomology is the direct sum of that of its two components. Alexander duality gives the stated complement groups.

:::

:::

:::

The unreduced group $H_0$ is obtained, as usual, by adjoining one copy of $\ZZ$ to $\widetilde H_0$.
:::
