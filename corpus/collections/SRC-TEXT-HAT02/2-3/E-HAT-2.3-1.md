---
schema: qual/card@1
id: E-HAT-2.3-1
kind: problem
title: Torsion subgroup and mod-torsion functor do not define homology theories
classification:
  areas:
  - topology
  topics:
  - Homology
  - Axiomatic Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.3, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
If $T_n(X, A)$ denotes the torsion subgroup of $H_n(X, A; \mathbb{Z})$, show that the functors $(X, A) \mapsto T_n(X, A)$, with the obvious induced homomorphisms $T_n(X, A) \to T_n(Y, B)$ and boundary maps $T_n(X, A) \to T_{n-1}(A)$, do not define a homology theory.
Do the same for the 'mod torsion' functor $MT_n(X, A) = H_n(X, A; \mathbb{Z}) / T_n(X, A)$.
:::

::: {.solution}
The exactness axiom fails for both constructions.

<1>1. For the pair $(D^2,S^1)$ the integral long exact sequence contains
\[
0=H_2(D^2)\longrightarrow H_2(D^2,S^1)\xrightarrow{\partial}H_1(S^1)\longrightarrow H_1(D^2)=0,
\]
so $\partial:\mathbb Z\to\mathbb Z$ is an isomorphism.
::: {.proof}
This is the long exact sequence of the pair, together with contractibility of $D^2$.
:::

<1>2. The torsion functors are not exact on this pair.
::: {.proof}
All four groups in <1>1 are torsion-free, hence
\[
T_2(D^2,S^1)=T_1(S^1)=0.
\]
This example alone does not detect failure, so instead use the Moore-space pair $(X,A)$ obtained from $A=S^1$ by attaching a $2$-cell by a degree-$m$ map, $m>1$. Then
\[
H_2(X,A)\cong\mathbb Z\xrightarrow{\partial=m}\mathbb Z\cong H_1(A)
\longrightarrow H_1(X)\cong\mathbb Z_m\longrightarrow0.
\]
Passing to torsion gives
\[
0\longrightarrow0\longrightarrow\mathbb Z_m\longrightarrow0,
\]
which is not exact at $T_1(X)=\mathbb Z_m$: the incoming image is $0$ while the outgoing kernel is all of $\mathbb Z_m$.
:::

<1>3. The mod-torsion functors are not exact on the same pair.
::: {.proof}
Passing the displayed integral sequence to quotients by torsion gives
\[
\mathbb Z\xrightarrow{m}\mathbb Z\longrightarrow0.
\]
Exactness at the second $\mathbb Z$ would require $m\mathbb Z=\mathbb Z$, false for $m>1$.
:::

Thus neither $T_*$ nor $MT_*$ satisfies the exactness axiom, so neither defines a homology theory.
:::
