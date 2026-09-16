---
schema: qual/card@1
id: E-HAT-3.1-4
kind: problem
title: Homology defined by $\operatorname{Hom}(G,C_n(X))$
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.1, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the resolution and Hom-complex calculations directly from the definitions.
---

# E-HAT-3.1-4

What happens if one defines homology groups $h_n(X; G)$ as the homology groups of the chain complex $\cdots \to \operatorname{Hom}(G, C_n(X)) \to \operatorname{Hom}(G, C_{n-1}(X)) \to \cdots$?
More specifically, what are the groups $h_n(X; G)$ when $G = \mathbb{Z}$, $\mathbb{Z}_m$, and $\mathbb{Q}$?

::: {.solution}
For a space $X$, each singular chain group $C_n(X)$ is a free abelian group. We compute
\[
h_n(X;G)=H_n\bigl(\operatorname{Hom}(G,C_\bullet(X))\bigr)
\]
for the three specified groups $G$.

<1>1. If $G=\mathbb Z$, then
\[
\boxed{h_n(X;\mathbb Z)\cong H_n(X;\mathbb Z).}
\]
::: {.proof}
Evaluation at $1$ gives a natural isomorphism
\[
\operatorname{Hom}(\mathbb Z,C_n(X))\cong C_n(X)
\]
for every $n$, and under this identification the induced differential is the ordinary singular boundary. Thus the two chain complexes are naturally isomorphic.
:::

<1>2. If $G=\mathbb Z_m$, then
\[
\boxed{h_n(X;\mathbb Z_m)=0}
\]
for every $n$.
::: {.proof}
A homomorphism $\mathbb Z_m\to C_n(X)$ must send $1$ to an element annihilated by $m$. Since $C_n(X)$ is free abelian and therefore torsion-free, the only such element is $0$. Hence
\[
\operatorname{Hom}(\mathbb Z_m,C_n(X))=0
\]
in every degree.
:::

<1>3. If $G=\mathbb Q$, then
\[
\boxed{h_n(X;\mathbb Q)=0}
\]
for every $n$.
::: {.proof}
Let $\varphi:\mathbb Q\to C_n(X)$ be a homomorphism and put $c=\varphi(1)$. For every positive integer $r$,
\[
c=r\,\varphi(1/r),
\]
so $c$ is divisible by every $r$. A free abelian group has no nonzero element divisible by every positive integer, hence $c=0$. Then for $a/b\in\mathbb Q$,
\[
b\varphi(a/b)=a\varphi(1)=0,
\]
and torsion-freeness gives $\varphi(a/b)=0$. Thus every such homomorphism is zero.
:::

So this construction behaves very differently from ordinary homology: for torsion or divisible coefficient groups it can vanish identically.
:::
