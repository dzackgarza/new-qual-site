---
schema: qual/card@1
id: E-HAT-3.3-34
kind: problem
title: Poincaré duality diagram for manifolds with boundary
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 34; the stored statement matches the current online text and diagram where applicable.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 34; it matches the printed text. The card writes $[M,\partial M]\frown-$ where the print abbreviates the same relative fundamental class as $[M]\frown-$; the diagram is otherwise transcribed as printed.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the diagram square by square: the middle square is naturality of the cap product, and the
    outer ones follow from the chain-level identity
    $\partial(c\frown\varphi)=(\partial c)\frown\varphi\pm c\frown\delta\varphi$ together with
    $\partial[M,\partial M]=[\partial M]$, the sign being left to the conventions as the exercise
    allows.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    The card left the signs to "the chosen cap and connecting-map conventions", which is exactly the
    part of the exercise that has content. The two outer squares are now computed from Hatcher's
    chain identity p.240 in the form $\partial(c\frown\varphi)=(-1)^\ell(\partial c\frown\varphi
    -c\frown\delta\varphi)$: the third square commutes up to $(-1)^k$, and the first exactly, once a
    cochain on the boundary is extended through the collar. The middle square is now justified by
    both sides being the same chain-level product rather than by the word "naturality". Not verified:
    the sign of the relative cap product forms, which is taken from p.240 and not recomputed.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The cochain extension in the first square formerly claimed to come from a retraction of M onto
    its boundary. No such retraction exists by Exercise 32 for compact M with nonempty boundary.
    It is replaced by the algebraic extension singular cohomology always provides: C_*(boundary M)
    is free on a subset of the singular-simplex basis of C_*(M), so define Psi by psi on that subset
    and zero on the remaining simplices. Then Psi restricts to psi and its coboundary is relative
    because psi is a cocycle. The sign computations are unchanged.

---

::: {.problem}
For a compact manifold $M$ verify that the following diagram relating Poincaré duality for $M$ and $\partial M$ is commutative, up to sign at least:

$$
\begin{array}{ccccccc}
H^{k-1}(\partial M;R)&\longrightarrow&H^k(M,\partial M;R)&\longrightarrow&H^k(M;R)&\longrightarrow&H^k(\partial M;R)\\
\downarrow { [\partial M]\frown - }&&\downarrow { [M,\partial M]\frown - }&&\downarrow { [M,\partial M]\frown - }&&\downarrow { [\partial M]\frown - }\\
H_{n-k}(\partial M;R)&\longrightarrow&H_{n-k}(M;R)&\longrightarrow&H_{n-k}(M,\partial M;R)&\longrightarrow&H_{n-k-1}(\partial M;R)
\end{array}
$$
:::

::: {.solution}
The top row is the cohomology long exact sequence of the pair $(M,\partial M)$,
$$
H^{k-1}(\partial M;R)\to H^k(M,\partial M;R)
\to H^k(M;R)\to H^k(\partial M;R),
$$
and the bottom row is the corresponding homology sequence
$$
H_{n-k}(\partial M;R)\to H_{n-k}(M;R)
\to H_{n-k}(M,\partial M;R)\to H_{n-k-1}(\partial M;R).
$$
The middle square commutes: both composites $\psi\mapsto j_*([M,\partial M]\frown\psi)$ and $\psi\mapsto[M,\partial M]\frown j^*\psi$ are computed from the same chain-level product, since $j^*$ does not change the values of a cochain on chains in $M$, so the square commutes exactly.

For the outer squares, write out the sign. Let $c\in C_n(M;R)$ represent $[M,\partial M]$, so that $\partial c$ represents $[\partial M]$ by Exercise 31, and let Hatcher's chain identity (p.240) for $\sigma$ of degree $k$ and $\varphi$ of degree $\ell$ be used in the form
$$
\partial(c\frown\varphi)=(-1)^{\ell}\bigl(\partial c\frown\varphi-c\frown\delta\varphi\bigr).
$$

Third square: take $\varphi$ a cocycle on $M$ of degree $k$, so $\delta\varphi=0$. Then $\partial(c\frown\varphi)=(-1)^k\,\partial c\frown\varphi = (-1)^k\,\partial c\frown i^*\varphi$ (the values of $\varphi$ on faces of $\partial c$ are those of its restriction to $\partial M$), which is the statement that $[\partial M]\frown i^*\varphi=(-1)^k\partial([M,\partial M]\frown\varphi)$: the square commutes up to the sign $(-1)^k$.

First square: take $\psi$ a cocycle on $\partial M$ of degree $k-1$. Extend it to a cochain $\Psi$ on $M$ by setting $\Psi(\sigma)=\psi(\sigma)$ for singular simplices $\sigma$ whose image lies in $\partial M$ and $\Psi(\sigma)=0$ on all other singular simplices. This defines a cochain because these two kinds of simplices give subsets of the free basis of $C_*(M)$ and $C_*(\partial M)$ respectively, so no retraction $M\to\partial M$ is needed. Then $\Psi\restrict_{\partial M}=\psi$, and $\delta\Psi$ vanishes on chains in $\partial M$ because $\psi$ is a cocycle; hence $\delta\Psi$ is a relative cocycle whose class is $\delta\psi$. The identity with $\ell=k-1$ gives
$$
\partial(c\frown\Psi)=(-1)^{k-1}\bigl(\partial c\frown\Psi-c\frown\delta\Psi\bigr),\qquad\text{so}\qquad c\frown\delta\Psi=\partial c\frown\Psi-(-1)^{k-1}\partial(c\frown\Psi).
$$
In $H_{n-k}(M;R)$ the second term on the right is a boundary, and $\partial c\frown\Psi=\partial c\frown\psi$ because $\Psi$ extends $\psi$; hence $[M,\partial M]\frown\delta\psi=i_*([\partial M]\frown\psi)$, with no sign beyond the one convention chosen for the relative connecting map. So the first square commutes, and the third commutes up to $(-1)^k$.
:::
