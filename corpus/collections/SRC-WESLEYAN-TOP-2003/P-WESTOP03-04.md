---
schema: qual/card@1
id: P-WESTOP03-04
kind: problem
title: Classification of compact connected surfaces and a torus-projective-plane connected sum
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. List the compact connected surfaces up to homeomorphism.
2. Explain in some detail how one knows that no two surfaces on the list are homeomorphic.
3. Identify, within this classification, the connected sum of a torus and a real projective plane, and justify the identification.
:::

All surfaces below are understood to be compact, connected, and without boundary.

::: pf

::: pf-step

Up to homeomorphism, the orientable surfaces are
\[
\Sigma_g=\#^g(S^1\times S^1),
\qquad g=0,1,2,\ldots,
\]
where $\Sigma_0=S^2$.


::: pf-proof

The classification theorem for compact connected surfaces says that every orientable closed surface is a sphere with $g$ handles, equivalently the connected sum of $g$ tori, for a unique integer $g\geq0$.

:::

:::

::: pf-step

Up to homeomorphism, the nonorientable surfaces are
\[
N_k=\#^k\mathbb{RP}^2,
\qquad k=1,2,3,\ldots.
\]


::: pf-proof

The nonorientable half of the classification theorem says that every nonorientable closed connected surface is a sphere with $k$ crosscaps, equivalently the connected sum of $k$ projective planes, for a unique integer $k\geq1$.

:::

:::

::: pf-step

No orientable surface $\Sigma_g$ is homeomorphic to a nonorientable surface $N_k$.


::: pf-proof

Orientability is a topological invariant: a homeomorphism transports local orientations and hence an orientation of one surface to the other. By construction $\Sigma_g$ is orientable and $N_k$ is not.

:::

:::

::: pf-step

The Euler characteristics are
\[
\chi(\Sigma_g)=2-2g,
\qquad
\chi(N_k)=2-k.
\]


::: pf-proof

The sphere has Euler characteristic $2$, the torus has Euler characteristic $0$, and $\mathbb{RP}^2$ has Euler characteristic $1$. For closed connected surfaces,
\[
\chi(M\#N)=\chi(M)+\chi(N)-2,
\]
because one removes an open disk from each surface, decreasing each Euler characteristic by $1$, and glues along a circle of Euler characteristic $0$. Induction gives the displayed formulas.

:::

:::

::: pf-step

Distinct orientable genera give nonhomeomorphic surfaces, and distinct nonorientable genera give nonhomeomorphic surfaces.


::: pf-proof

Euler characteristic is invariant under homeomorphism. If $\Sigma_g\cong\Sigma_h$, step <1>4 gives
\[
2-2g=2-2h,
\]
so $g=h$. If $N_k\cong N_\ell$, then
\[
2-k=2-\ell,
\]
so $k=\ell$. Together with step <1>3, this proves that no two distinct entries on the classification list are homeomorphic.

:::

:::

::: pf-step

The connected sum
\[
T^2\#\mathbb{RP}^2
\]
is nonorientable and has Euler characteristic
\[
-1.
\]


::: pf-proof

The connected sum with the nonorientable surface $\mathbb{RP}^2$ is nonorientable. Using the connected-sum formula,
\[
\chi(T^2\#\mathbb{RP}^2)
=\chi(T^2)+\chi(\mathbb{RP}^2)-2
=0+1-2=-1.
\]

:::

:::

::: pf-step

The unique nonorientable surface with Euler characteristic $-1$ is
\[
N_3=\mathbb{RP}^2\#\mathbb{RP}^2\#\mathbb{RP}^2.
\]


::: pf-proof

By step <1>4, $\chi(N_k)=2-k$. Solving
\[
2-k=-1
\]
gives $k=3$. The uniqueness assertion follows from the classification theorem and step <1>5.

:::

:::

::: pf-step

Therefore
\[
\boxed{
T^2\#\mathbb{RP}^2
\cong
\mathbb{RP}^2\#\mathbb{RP}^2\#\mathbb{RP}^2.}
\]


::: pf-proof

Step <1>6 places $T^2\#\mathbb{RP}^2$ in the nonorientable class with Euler characteristic $-1$, and step <1>7 identifies the unique member of the classification with those invariants.

:::

:::

::: pf-qed

Steps <1>1--<1>2 give the classification list, steps <1>3--<1>5 distinguish all entries, and steps <1>6--<1>8 identify the requested connected sum.

:::

:::
