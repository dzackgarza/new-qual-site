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

::: {.problem}
For an abelian group $A$ let $p: A \to A$ be multiplication by $p$, and let ${}_pA = \ker p$, $pA = \operatorname{im} p$, and $A_p = \operatorname{coker} p$ as in the proof of Proposition 3F.12. Show that the six-term exact sequences involving $\operatorname{Hom}(-, \ZZ)$ and $\operatorname{Ext}(-, \ZZ)$ associated to the short exact sequences $0 \to {}_pA \to A \to pA \to 0$ and $0 \to pA \to A \to A_p \to 0$ can be spliced together to yield an exact sequence

$$\operatorname{Hom}(pA, \ZZ) \to \operatorname{Ext}(A_p, \ZZ) \to \operatorname{Ext}(A, \ZZ) \xrightarrow{p} \operatorname{Ext}(A, \ZZ) \to \operatorname{Ext}({}_pA, \ZZ) \to 0$$

where the map labeled "$p$" is multiplication by $p$.
Use this to show:

(a) $\operatorname{Ext}(A, \ZZ)$ is divisible if $A$ is torsionfree.

(b) $\operatorname{Ext}(A, \ZZ)$ is torsionfree if $A$ is divisible, and the converse holds if $\operatorname{Hom}(A, \ZZ) = 0$.
:::

::: {.solution}
Consider the two short exact sequences
\[
0\to{}_pA\to A\xrightarrow{p}pA\to0,
\qquad
0\to pA\to A\to A_p\to0.
\]
Since ${}_pA$ and $A_p$ are killed by $p$, every homomorphism from either group to the torsionfree group $\ZZ$ is zero.

Applying $\operatorname{Hom}(-,\ZZ)$ and $\operatorname{Ext}(-,\ZZ)$ to the first sequence gives the tail
\[
0\to\operatorname{Ext}(pA,\ZZ)
\to\operatorname{Ext}(A,\ZZ)
\to\operatorname{Ext}({}_pA,\ZZ)\to0.
\]
Applying them to the second gives
\[
0\to\operatorname{Hom}(A,\ZZ)\to\operatorname{Hom}(pA,\ZZ)
\to\operatorname{Ext}(A_p,\ZZ)
\to\operatorname{Ext}(A,\ZZ)
\to\operatorname{Ext}(pA,\ZZ)\to0.
\]
Splicing at $\operatorname{Ext}(pA,\ZZ)$ yields
\[
\operatorname{Hom}(pA,\ZZ)\to\operatorname{Ext}(A_p,\ZZ)\to
\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}(A,\ZZ)\to
\operatorname{Ext}({}_pA,\ZZ)\to0.
\]
The composite of the two middle maps is induced contravariantly by
\[
A\xrightarrow{p}pA\hookrightarrow A,
\]
which is multiplication by $p$ on $A$. By functoriality of Ext, the composite is therefore multiplication by $p$ on $\operatorname{Ext}(A,\ZZ)$. Hence the spliced sequence is precisely
\[
\boxed{
\operatorname{Hom}(pA,\ZZ)\to\operatorname{Ext}(A_p,\ZZ)\to
\operatorname{Ext}(A,\ZZ)\xrightarrow{p}
\operatorname{Ext}(A,\ZZ)\to
\operatorname{Ext}({}_pA,\ZZ)\to0.}
\]

::: pf

::: pf-step

If $A$ is torsionfree, then $\operatorname{Ext}(A,\ZZ)$ is divisible.

::: pf-proof

Torsionfreeness gives ${}_pA=0$. Exactness at the second copy of $\operatorname{Ext}(A,\ZZ)$ says multiplication by $p$ is surjective for every prime $p$. Therefore multiplication by every positive integer is surjective, so $\operatorname{Ext}(A,\ZZ)$ is divisible.

:::

:::

::: pf-step

If $A$ is divisible, then $\operatorname{Ext}(A,\ZZ)$ is torsionfree.

::: pf-proof

Divisibility gives $A_p=0$ for every prime $p$. Exactness at the first copy of $\operatorname{Ext}(A,\ZZ)$ then says multiplication by $p$ has zero kernel. Thus the Ext group has no $p$-torsion for any prime $p$, hence is torsionfree.

:::

:::

::: pf-step

Conversely, if $\operatorname{Hom}(A,\ZZ)=0$ and $\operatorname{Ext}(A,\ZZ)$ is torsionfree, then $A$ is divisible.

::: pf-proof

Precomposition with the surjection $A\xrightarrow p pA$ injects
\[
\operatorname{Hom}(pA,\ZZ)\hookrightarrow\operatorname{Hom}(A,\ZZ)=0,
\]
so $\operatorname{Hom}(pA,\ZZ)=0$. The spliced exact sequence therefore identifies
\[
\operatorname{Ext}(A_p,\ZZ)
\]
with the kernel of multiplication by $p$ on $\operatorname{Ext}(A,\ZZ)$. This kernel is zero by torsionfreeness.

But $A_p$ is a vector space over $\ZZ_p$, and if it were nonzero it would admit a nonzero homomorphism to the subgroup $\ZZ_p\subset\QQ/\ZZ$. Using
\[
\operatorname{Ext}(A_p,\ZZ)
\cong\operatorname{Hom}(A_p,\QQ/\ZZ)
\]
from Exercise 5 (since $\operatorname{Hom}(A_p,\QQ)=0$), this would contradict $\operatorname{Ext}(A_p,\ZZ)=0$. Hence $A_p=0$, i.e. $pA=A$, for every prime $p$. Therefore $A$ is divisible.

:::

:::

:::

:::
