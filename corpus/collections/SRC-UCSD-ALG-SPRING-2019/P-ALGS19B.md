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
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
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
<1>1. The Frattini subgroup \(\Phi(G)\) is characteristic in \(G\), hence normal.
::: {.proof}
Every automorphism of \(G\) permutes the maximal subgroups of \(G\), so it preserves their intersection.
:::

<1>2. If \(P\) is a Sylow \(p\)-subgroup of \(G\), then \(P\cap\Phi(G)\) is a Sylow \(p\)-subgroup of \(\Phi(G)\).
::: {.proof}
For any normal subgroup \(N\trianglelefteq G\) and Sylow \(p\)-subgroup \(P\) of \(G\), the subgroup \(P\cap N\) is Sylow in \(N\). Apply this with \(N=\Phi(G)\).
:::

<1>3. The subgroup
\[
P\Phi(G)/\Phi(G)
\]
is a Sylow \(p\)-subgroup of \(G/\Phi(G)\).
::: {.proof}
By the second isomorphism theorem,
\[
P\Phi(G)/\Phi(G)\cong P/(P\cap\Phi(G)).
\]
By <1>2, its order is exactly the \(p\)-part of \(|G/\Phi(G)|\).
:::

<1>4. Since \(G/\Phi(G)\) is nilpotent, \(P\Phi(G)/\Phi(G)\trianglelefteq G/\Phi(G)\). Therefore
\[
P\Phi(G)\trianglelefteq G.
\]
::: {.proof}
In a finite nilpotent group every Sylow subgroup is normal. The correspondence theorem then lifts normality from the quotient.
:::

<1>5. Put \(N=P\Phi(G)\). Then \(N\trianglelefteq G\), and \(P\) is a Sylow \(p\)-subgroup of \(N\).
::: {.proof}
Normality is <1>4. Since \(N\le G\) contains the Sylow \(p\)-subgroup \(P\) of \(G\), no larger \(p\)-subgroup can occur in \(N\).
:::

<1>6. Frattini's argument gives
\[
G=N_G(P)N=N_G(P)\Phi(G).
\]
::: {.proof}
Because \(N\trianglelefteq G\) and \(P\) is a Sylow \(p\)-subgroup of \(N\), Frattini's argument gives \(G=N_G(P)N\). Since \(P\le N_G(P)\) and \(N=P\Phi(G)\), this becomes \(G=N_G(P)\Phi(G)\).
:::

<1>7. One must have \(N_G(P)=G\). Hence \(P\trianglelefteq G\).
::: {.proof}
If \(N_G(P)<G\), choose a maximal subgroup \(M\) containing \(N_G(P)\). By definition \(\Phi(G)\subseteq M\). Then <1>6 gives
\[
G=N_G(P)\Phi(G)\subseteq M,
\]
a contradiction. Thus \(N_G(P)=G\), which is equivalent to \(P\trianglelefteq G\).
:::

<1>8. Therefore every Sylow subgroup of \(G\) is normal, so \(G\) is nilpotent.
::: {.proof}
The argument in <1>2--<1>7 applies to every prime divisor \(p\) of \(|G|\). A finite group is nilpotent if and only if all of its Sylow subgroups are normal.
:::
:::
