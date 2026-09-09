---
schema: qual/card@1
id: E-HAT-2.1-21
kind: problem
title: Explicit chain maps inducing suspension isomorphism
classification:
  areas:
  - topology
  topics:
  - Homology
  - Suspension
  - Chain Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 21; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof checked at chain/skeletal/combinatorial level.
---

Making the preceding problem more concrete, construct explicit chain maps $s: C_n(X) \to C_{n+1}(SX)$ inducing isomorphisms $\tilde{H}_n(X) \to \tilde{H}_{n+1}(SX)$.

::: {.solution}
Let $i:X\hookrightarrow SX$ be the equatorial inclusion. For a singular simplex $\sigma:\Delta^n\to X$, let $C_+\sigma$ and $C_-\sigma$ be the singular $(n+1)$-simplices obtained by coning $i\sigma$ to the upper and lower suspension vertices, respectively, with the cone vertex listed first in the orientation. Define
\[
s_n(\sigma)=C_+\sigma-C_-\sigma
\]
and extend linearly.

<1>1. The cone operators satisfy
\[
\partial C_\pm + C_\pm\partial=i_\#.
\]
::: {.proof}
For an oriented simplex $[v_0,\dots,v_n]$, the oriented cone is $[w_\pm,v_0,\dots,v_n]$. Its boundary is
\[
[v_0,\dots,v_n]-\sum_{j=0}^n(-1)^j[w_\pm,v_0,\dots,\widehat v_j,\dots,v_n],
\]
which is exactly $i_\#\sigma-C_\pm(\partial\sigma)$. This identity extends linearly to all singular chains.
:::

<1>2. Hence
\[
\partial s_n=-s_{n-1}\partial.
\]
Thus $s$ is a degree-one chain map, equivalently a chain map $C_*(X)\to C_{*+1}(SX)$ when the shifted complex has differential $-\partial$.
::: {.proof}
Subtract the two identities in <1>1:
\[
\partial(C_+-C_-)+(C_+-C_-)\partial=0.
\]
This is precisely the displayed formula.
:::

<1>3. Therefore $s$ sends cycles to cycles and boundaries to boundaries, and induces
\[
s_*:\widetilde H_n(X)\longrightarrow \widetilde H_{n+1}(SX).
\]
::: {.proof}
If $\partial z=0$, then $\partial s(z)=-s(\partial z)=0$. If $z=\partial c$, then
\[
s(z)=s(\partial c)=-\partial s(c),
\]
so the homology class of $s(z)$ is zero. The same formulas hold for augmented chains in degree $0$, hence give the reduced-homology map as well.
:::

<1>4. The induced map $s_*$ is an isomorphism for every $n$.
::: {.proof}
Write
\[
SX=C_+X\cup C_-X,
\qquad C_+X\cap C_-X=X.
\]
Both cones are contractible. In the reduced Mayer--Vietoris sequence, the connecting homomorphism
\[
\delta:\widetilde H_{n+1}(SX)\longrightarrow\widetilde H_n(X)
\]
is therefore an isomorphism.

For a cycle $z$ in $X$, the chain $s(z)=C_+z-C_-z$ decomposes as an upper-cone chain plus a lower-cone chain. By the chain-level definition of the Mayer--Vietoris connecting map,
\[
\delta([s(z)])=[\partial C_+z]=[z]
\]
(up to the harmless global sign determined by the convention for $\delta$). Thus $\delta\circ s_*=\pm\operatorname{id}$. Since $\delta$ is an isomorphism, so is $s_*$.
:::

Hence the explicit maps
\[
\boxed{s_n(\sigma)=C_+\sigma-C_-\sigma}
\]
induce the suspension isomorphisms
\[
\widetilde H_n(X)\cong\widetilde H_{n+1}(SX).
\]
:::
