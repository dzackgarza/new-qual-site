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

::: problem
Let $G$ be a group.
Let $r \geq 2$ be an integer.
Assume that $G$ contains a non-trivial subgroup $H$ of index $[G:H] = r$.
Prove the following.

(a) If $G$ is simple, then $G$ is finite and $|G|$ divides $r!$.

(b) If $r \in \{2, 3, 4\}$, then $G$ cannot be simple.

(c) For all integers $r \geq 5$, there exist simple groups $G$ which contain non-trivial subgroups $H$ of index $[G:H] = r$.
:::

::: {.solution}
<1>1. The action of $G$ on the $r$ left cosets of $H$ gives a homomorphism
\[
\rho:G\longrightarrow S_r.
\]
::: {.proof}
For $g\in G$ and a left coset $xH$, define
\[
g\cdot(xH)=(gx)H.
\]
This is a well-defined permutation action on the set $G/H$, which has $r$ elements.
:::

<1>2. If $G$ is simple, then $\rho$ is injective.
::: {.proof}
The kernel of the coset action is
\[
\ker\rho=\bigcap_{g\in G}gHg^{-1},
\]
so $\ker\rho\trianglelefteq G$ and $\ker\rho\le H$. Since $[G:H]=r\ge2$, the subgroup $H$ is proper, hence $\ker\rho\ne G$. Simplicity forces $\ker\rho=1$.
:::

<1>3. If $G$ is simple, then $G$ is finite and $|G|\mid r!$.
::: {.proof}
By <1>2, $G$ embeds in the finite group $S_r$. Therefore $G$ is finite, and Lagrange's theorem gives
\[
|G|\mid|S_r|=r!.
\]
This proves part (a).
:::

<1>4. If $r\in\{2,3,4\}$, then $G$ cannot be simple.
::: {.proof}
Suppose $G$ were simple. Since $H$ is nontrivial and proper, $G$ cannot be cyclic of prime order; hence a simple $G$ here would be nonabelian. By <1>2, $G$ embeds in $S_r$.

For $r\le4$, the group $S_r$ is solvable: $S_2$ and $S_3$ are solvable, and
\[
1\trianglelefteq V_4\trianglelefteq A_4\trianglelefteq S_4
\]
has abelian successive quotients. Every subgroup of a solvable group is solvable, whereas a nonabelian simple group is not solvable. This contradiction proves part (b).
:::

<1>5. For every $r\ge5$, the alternating group $A_r$ is simple and contains a nontrivial subgroup of index $r$.
::: {.proof}
We use the standard theorem that $A_r$ is simple for every $r\ge5$. Let
\[
H=\{\sigma\in A_r:\sigma(r)=r\}
\]
be the stabilizer of the point $r$. Restriction to $\{1,\dots,r-1\}$ identifies $H$ with $A_{r-1}$, so $H$ is nontrivial for $r\ge5$. The natural action of $A_r$ on $\{1,\dots,r\}$ is transitive, hence orbit-stabilizer gives
\[
[A_r:H]=r.
\]
Thus $G=A_r$ supplies the required example for every $r\ge5$.
:::

<1>6. Therefore all three assertions hold.
::: {.proof}
Parts (a), (b), and (c) are <1>3, <1>4, and <1>5, respectively.
:::
:::
