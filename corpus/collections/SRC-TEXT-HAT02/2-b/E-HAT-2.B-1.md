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
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 1, printed page
    176; the statement matches word for word. Checked: Alexander duality
    H̃_i(S^n − X) ≅ H̃^{n−i−1}(X) (Theorem 3.44, p. 253) applies to these compact
    locally contractible X; H̃^j(S^k ∨ S^ℓ) is Z in degrees k and ℓ (Z^2 when
    k = ℓ) and H̃^0 = 0, giving Z in degrees n−k−1 and n−ℓ−1; for the disjoint union
    there is also H̃^0 = Z, giving one more Z in degree n−1. Degree shifts and the
    ordinary H_0 statement checked. No defect.
---
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Source coverage and degree accounting verified against DeMason, M382C Full Credit HW Problems
    (2021), Hatcher 2.B.1, pp.68-70. The wedge's reduced cohomology is the direct sum of the two
    sphere contributions; the disjoint case has one further H~^0=Z, and terms at the coinciding
    indices n-k-1, n-l-1, n-1 must be summed. Explicitly, at n=1 and k=l=0, X has four points and
    the complement has H~_0=Z^3, so H_0=Z^4. This refines the existing correct formula without
    invoking an inappropriate connectedness assumption for S^0.

---

::: {.problem}
Compute $H_i(S^n - X)$ when $X$ is a subspace of $S^n$ homeomorphic to $S^k \vee S^\ell$ or to $S^k \amalg S^\ell$.
:::

::: {.solution}
We use Alexander duality in the form
$$
\widetilde H_i(S^n-X;\ZZ)\cong \widetilde H^{\,n-i-1}(X;\ZZ)
$$
for these compact locally contractible subspaces of $S^n$.

::: pf

::: {.pf-step #s1}

If $X=S^k\vee S^\ell$, then
$$
\widetilde H^j(X)\cong
\begin{cases}
\ZZ,&j=k\ne\ell,\\
\ZZ,&j=\ell\ne k,\\
\ZZ^2,&j=k=\ell,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

Reduced cohomology takes a finite wedge to the direct sum of the reduced cohomologies of the two spheres. Each sphere has one copy of $\ZZ$ in its dimension and zero reduced cohomology elsewhere.

:::

:::

::: pf-step

Consequently, for $X=S^k\vee S^\ell$,
$$
\widetilde H_i(S^n-X)\cong
\begin{cases}
\ZZ,&i=n-k-1\ne n-\ell-1,\\
\ZZ,&i=n-\ell-1\ne n-k-1,\\
\ZZ^2,&i=n-k-1=n-\ell-1,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

Apply Alexander duality to step [](#s1){.pf-ref}, replacing the cohomological degree $j$ by $n-i-1$.

:::

:::

::: pf-step

If $X=S^k\amalg S^\ell$, then reduced cohomology has, in addition to the sphere factors, the summand
$$
\widetilde H^0(X)\cong\ZZ.
$$
For every $k$ and $\ell$ (including zero, where $S^0$ itself is disconnected), the value of Alexander duality is
$$
\widetilde H_i(S^n-X)
\cong
\widetilde H^{\,n-i-1}(S^k\amalg S^\ell).
$$
Hence extra copies of $\ZZ$ occur at the indices $n-k-1$, $n-\ell-1$ and $n-1$ when these are relevant; repeated indices are summed rather than counted separately or lost. In particular, when $n=1$ and $k=\ell=0$, the degree-$0$ reduced group is $\ZZ^3$, not merely $\ZZ$ from the displayed $\widetilde H^0(X)$.

::: pf-proof

A disjoint union of two connected spaces has reduced $H^0$ equal to $\ZZ$, while its positive-degree cohomology is the direct sum of that of its two components. Alexander duality gives the stated complement groups.

:::

:::

:::

The unreduced group $H_0$ is obtained, as usual, by adjoining one copy of $\ZZ$ to $\widetilde H_0$.The two decompositions and their sphere-class computations are in **Kenneth DeMason, *M382C Full Credit HW Problems* (4 April 2021)**, Hatcher 2.B.1, printed pp. 68--70. The present proof collates those cases by Alexander duality, which applies here because a sphere is compact and locally contractible (Theorem 3.45, p. 254 of Hatcher). In the disjoint union case, as in the source, the extra reduced component class accompanies the sphere classes only once their indices are summed; the unreduced $H_0$ is obtained afterward.


:::
