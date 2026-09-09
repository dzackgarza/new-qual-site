---
schema: qual/card@1
id: E-HAT-3.F-9
kind: problem
title: "Spliced exact sequences for $p$-primary components"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.F, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

For an abelian group $A$ let $p: A \to A$ be multiplication by $p$, and let ${}_pA = \ker p$, $pA = \operatorname{im} p$, and $A_p = \operatorname{coker} p$ as in the proof of Proposition 3F.12. Show that the six-term exact sequences involving $\operatorname{Hom}(-, \mathbb{Z})$ and $\operatorname{Ext}(-, \mathbb{Z})$ associated to the short exact sequences $0 \to {}_pA \to A \to pA \to 0$ and $0 \to pA \to A \to A_p \to 0$ can be spliced together to yield an exact sequence

$$\operatorname{Hom}(pA, \mathbb{Z}) \to \operatorname{Ext}(A_p, \mathbb{Z}) \to \operatorname{Ext}(A, \mathbb{Z}) \xrightarrow{p} \operatorname{Ext}(A, \mathbb{Z}) \to \operatorname{Ext}({}_pA, \mathbb{Z}) \to 0$$

where the map labeled "$p$" is multiplication by $p$.
Use this to show:

(a) $\operatorname{Ext}(A, \mathbb{Z})$ is divisible if $A$ is torsionfree.

(b) $\operatorname{Ext}(A, \mathbb{Z})$ is torsionfree if $A$ is divisible, and the converse holds if $\operatorname{Hom}(A, \mathbb{Z}) = 0$.

::: {.solution}
Consider the two short exact sequences
\[
0\to{}_pA\to A\xrightarrow{p}pA\to0,
\qquad
0\to pA\to A\to A_p\to0.
\]
Since ${}_pA$ and $A_p$ are killed by $p$, every homomorphism from either group to the torsionfree group $\mathbb Z$ is zero.

Applying $\operatorname{Hom}(-,\mathbb Z)$ and $\operatorname{Ext}(-,\mathbb Z)$ to the first sequence gives the tail
\[
0\to\operatorname{Ext}(pA,\mathbb Z)
\to\operatorname{Ext}(A,\mathbb Z)
\to\operatorname{Ext}({}_pA,\mathbb Z)\to0.
\]
Applying them to the second gives
\[
0\to\operatorname{Hom}(A,\mathbb Z)	o\operatorname{Hom}(pA,\mathbb Z)
\to\operatorname{Ext}(A_p,\mathbb Z)
\to\operatorname{Ext}(A,\mathbb Z)
\to\operatorname{Ext}(pA,\mathbb Z)\to0.
\]
Splicing at $\operatorname{Ext}(pA,\mathbb Z)$ yields
\[
\operatorname{Hom}(pA,\mathbb Z)	o\operatorname{Ext}(A_p,\mathbb Z)	o
\operatorname{Ext}(A,\mathbb Z)	o\operatorname{Ext}(A,\mathbb Z)	o
\operatorname{Ext}({}_pA,\mathbb Z)	o0.
\]
The composite of the two middle maps is induced contravariantly by
\[
A\xrightarrow{p}pA\hookrightarrow A,
\]
which is multiplication by $p$ on $A$. By functoriality of Ext, the composite is therefore multiplication by $p$ on $\operatorname{Ext}(A,\mathbb Z)$. Hence the spliced sequence is precisely
\[
\boxed{
\operatorname{Hom}(pA,\mathbb Z)\to\operatorname{Ext}(A_p,\mathbb Z)	o
\operatorname{Ext}(A,\mathbb Z)\xrightarrow{p}
\operatorname{Ext}(A,\mathbb Z)\to
\operatorname{Ext}({}_pA,\mathbb Z)\to0.}
\]

<1>1. If $A$ is torsionfree, then $\operatorname{Ext}(A,\mathbb Z)$ is divisible.
::: {.proof}
Torsionfreeness gives ${}_pA=0$. Exactness at the second copy of $\operatorname{Ext}(A,\mathbb Z)$ says multiplication by $p$ is surjective for every prime $p$. Therefore multiplication by every positive integer is surjective, so $\operatorname{Ext}(A,\mathbb Z)$ is divisible.
:::

<1>2. If $A$ is divisible, then $\operatorname{Ext}(A,\mathbb Z)$ is torsionfree.
::: {.proof}
Divisibility gives $A_p=0$ for every prime $p$. Exactness at the first copy of $\operatorname{Ext}(A,\mathbb Z)$ then says multiplication by $p$ has zero kernel. Thus the Ext group has no $p$-torsion for any prime $p$, hence is torsionfree.
:::

<1>3. Conversely, if $\operatorname{Hom}(A,\mathbb Z)=0$ and $\operatorname{Ext}(A,\mathbb Z)$ is torsionfree, then $A$ is divisible.
::: {.proof}
Precomposition with the surjection $A\xrightarrow p pA$ injects
\[
\operatorname{Hom}(pA,\mathbb Z)\hookrightarrow\operatorname{Hom}(A,\mathbb Z)=0,
\]
so $\operatorname{Hom}(pA,\mathbb Z)=0$. The spliced exact sequence therefore identifies
\[
\operatorname{Ext}(A_p,\mathbb Z)
\]
with the kernel of multiplication by $p$ on $\operatorname{Ext}(A,\mathbb Z)$. This kernel is zero by torsionfreeness.

But $A_p$ is a vector space over $\mathbb Z_p$, and if it were nonzero it would admit a nonzero homomorphism to the subgroup $\mathbb Z_p\subset\mathbb Q/\mathbb Z$. Using
\[
\operatorname{Ext}(A_p,\mathbb Z)
\cong\operatorname{Hom}(A_p,\mathbb Q/\mathbb Z)
\]
from Exercise 5 (since $\operatorname{Hom}(A_p,\mathbb Q)=0$), this would contradict $\operatorname{Ext}(A_p,\mathbb Z)=0$. Hence $A_p=0$, i.e. $pA=A$, for every prime $p$. Therefore $A$ is divisible.
:::
:::
