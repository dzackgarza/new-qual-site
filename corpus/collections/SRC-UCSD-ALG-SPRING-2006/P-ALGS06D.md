---
schema: qual/card@1
id: P-ALGS06D
kind: problem
title: "Simple groups with subgroups of bounded index"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $G$ be a group.
Let $r \geq 2$ be an integer.
Assume that $G$ contains a non-trivial subgroup $H$ of index $[G:H] = r$.
Prove the following.

(a) If $G$ is simple, then $G$ is finite and $|G|$ divides $r!$.

(b) If $r \in \{2, 3, 4\}$, then $G$ cannot be simple.

(c) For all integers $r \geq 5$, there exist simple groups $G$ which contain non-trivial subgroups $H$ of index $[G:H] = r$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $G$ act by left multiplication on the set $G/H$ of $r$ left cosets. This gives a homomorphism
\[
\rho:G\longrightarrow S_r.
\]
If $G$ is simple, then $\rho$ is injective.

::: pf-proof

The kernel of the coset action is a normal subgroup of $G$ contained in the stabilizer of the coset $H$, namely $H$.
Since $H<G$, the kernel is not all of $G$.
If $G$ is simple, the kernel must therefore be trivial.

:::

:::

::: pf-step

If $G$ is simple, then $G$ is finite and $|G|\mid r!$.

::: pf-proof

By step [](#s1){.pf-ref}, $G$ embeds in the finite group $S_r$.
Hence $G$ is finite, and Lagrange's theorem gives
\[
|G|\mid |S_r|=r!.
\]

:::

:::

::: {.pf-step #s3}

For $r\in\{2,3,4\}$, the symmetric group $S_r$ is solvable.

::: pf-proof

For $S_2$ this is immediate.
For $S_3$ use the normal series
\[
1\triangleleft A_3\triangleleft S_3,
\]
whose factors are cyclic.
For $S_4$ use
\[
1\triangleleft V_4\triangleleft A_4\triangleleft S_4,
\]
where $V_4$ is the Klein four subgroup; all successive quotients are abelian.

:::

:::

::: pf-step

If $r\in\{2,3,4\}$, then $G$ cannot be simple.

::: pf-proof

Suppose $G$ were simple. By step [](#s1){.pf-ref}, $G$ is isomorphic to a subgroup of $S_r$, hence is solvable by step [](#s3){.pf-ref} because subgroups of solvable groups are solvable.
A nontrivial simple solvable group must be abelian: otherwise its derived subgroup is a nontrivial proper normal subgroup at the last nontrivial stage of the derived series.
A finite simple abelian group has prime order and therefore has no nontrivial proper subgroup.
But $H$ is nontrivial and proper since $[G:H]=r\ge2$, a contradiction.

:::

:::

::: {.pf-step #s5}

Let $r\ge5$ and take $G=A_r$ acting naturally on $\{1,\dots,r\}$. Let
\[
H=\operatorname{Stab}_{A_r}(1).
\]
Then $H$ is nontrivial and $[G:H]=r$.

::: pf-proof

The natural action of $A_r$ is transitive for $r\ge3$.
Hence orbit-stabilizer gives
\[
[A_r:H]=r.
\]
Moreover $H\cong A_{r-1}$, which is nontrivial for $r\ge5$.

:::

:::

::: pf-step

The group $A_r$ is simple for every $r\ge5$, so step [](#s5){.pf-ref} gives the required example for every such $r$.

::: pf-proof

We use the standard theorem that the alternating group $A_r$ is simple for $r\ge5$.

:::

:::

:::

:::
