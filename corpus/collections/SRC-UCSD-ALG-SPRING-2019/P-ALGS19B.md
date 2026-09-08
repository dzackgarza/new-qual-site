---
schema: qual/card@1
id: P-ALGS19B
kind: problem
title: "Frattini subgroup, Sylow subgroups, and nilpotence"
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
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Suppose $G$ is a finite group, and $\Phi(G)$ is its Frattini subgroup (the intersection of all maximal subgroups of $G$). Suppose $G/\Phi(G)$ is nilpotent.

(a) Let $P$ be a Sylow $p$-subgroup of $G$.
Prove that $P\Phi(G)$ is a normal subgroup of $G$.

(b) Prove that $P \trianglelefteq G$.

Hint: $P$ is a Sylow $p$-subgroup of $P\Phi(G)$; use Frattini's argument.

(c) Prove that $G$ is nilpotent.
:::

::: {.solution}
<1>1. Put \(\Phi=\Phi(G)\). The subgroup \(P\Phi/\Phi\) is a Sylow \(p\)-subgroup of \(G/\Phi\).
::: {.proof}
Because \(\Phi\trianglelefteq G\), the image of a Sylow \(p\)-subgroup under the quotient map is a Sylow \(p\)-subgroup of the quotient.
Equivalently, \(P\Phi/\Phi\cong P/(P\cap\Phi)\) has the full \(p\)-part of \(|G/\Phi|\).
:::

<1>2. The subgroup \(P\Phi\) is normal in \(G\).
::: {.proof}
The finite group \(G/\Phi\) is nilpotent, so each of its Sylow subgroups is normal.
By <1>1, \(P\Phi/\Phi\trianglelefteq G/\Phi\). Taking its inverse image under \(G\to G/\Phi\) gives \(P\Phi\trianglelefteq G\).
:::

<1>3. The subgroup \(P\) is a Sylow \(p\)-subgroup of \(P\Phi\).
::: {.proof}
Since \(P\le P\Phi\le G\) and \(P\) is Sylow in \(G\), no \(p\)-subgroup of \(P\Phi\) can have larger order.
:::

<1>4. Frattini's argument gives
\[
G=(P\Phi)N_G(P)=\Phi N_G(P).
\]
::: {.proof}
By <1>2, \(P\Phi\trianglelefteq G\), and by <1>3, \(P\) is a Sylow \(p\)-subgroup of \(P\Phi\). Frattini's argument therefore gives \(G=(P\Phi)N_G(P)\). Since \(P\le N_G(P)\), this product equals \(\Phi N_G(P)\).
:::

<1>5. One has \(N_G(P)=G\), hence \(P\trianglelefteq G\).
::: {.proof}
Suppose \(N_G(P)<G\). Since \(G\) is finite, choose a maximal subgroup \(M\) with \(N_G(P)\le M<G\). By definition of the Frattini subgroup, \(\Phi\le M\). Hence <1>4 gives
\[
G=\Phi N_G(P)\le M,
\]
a contradiction.
Therefore \(N_G(P)=G\), which is exactly \(P\trianglelefteq G\).
:::

<1>6. The group \(G\) is nilpotent.
::: {.proof}
The argument in <1>1--<1>5 applies to every prime \(p\mid |G|\), so every Sylow subgroup of \(G\) is normal.
A finite group is nilpotent exactly when all of its Sylow subgroups are normal.
:::
:::
