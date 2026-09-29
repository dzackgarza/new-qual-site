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

::: {.problem}
Suppose $G$ is a finite group, and $\Phi(G)$ is its Frattini subgroup (the intersection of all maximal subgroups of $G$). Suppose $G/\Phi(G)$ is nilpotent.

(a) Let $P$ be a Sylow $p$-subgroup of $G$.
Prove that $P\Phi(G)$ is a normal subgroup of $G$.

(b) Prove that $P \trianglelefteq G$.

Hint: $P$ is a Sylow $p$-subgroup of $P\Phi(G)$; use Frattini's argument.

(c) Prove that $G$ is nilpotent.
:::

::: {.solution}

::: pf

::: pf-step

The Frattini subgroup \(\Phi(G)\) is characteristic in \(G\), hence normal.

::: pf-proof

Every automorphism of \(G\) permutes the maximal subgroups of \(G\), so it preserves their intersection.

:::

:::

::: {.pf-step #s2}

If \(P\) is a Sylow \(p\)-subgroup of \(G\), then \(P\cap\Phi(G)\) is a Sylow \(p\)-subgroup of \(\Phi(G)\).

::: pf-proof

For any normal subgroup \(N\trianglelefteq G\) and Sylow \(p\)-subgroup \(P\) of \(G\), the subgroup \(P\cap N\) is Sylow in \(N\). Apply this with \(N=\Phi(G)\).

:::

:::

::: {.pf-step #s3}

The subgroup
\[
P\Phi(G)/\Phi(G)
\]
is a Sylow \(p\)-subgroup of \(G/\Phi(G)\).

::: pf-proof

By the second isomorphism theorem,
\[
P\Phi(G)/\Phi(G)\cong P/(P\cap\Phi(G)).
\]
By step [](#s2){.pf-ref}, its order is exactly the \(p\)-part of \(|G/\Phi(G)|\).

:::

:::

::: {.pf-step #s4}

Since \(G/\Phi(G)\) is nilpotent, \(P\Phi(G)/\Phi(G)\trianglelefteq G/\Phi(G)\). Therefore
\[
P\Phi(G)\trianglelefteq G.
\]

::: pf-proof

In a finite nilpotent group every Sylow subgroup is normal. The correspondence theorem then lifts normality from the quotient.

:::

:::

::: {.pf-step #s5}

Put \(N=P\Phi(G)\). Then \(N\trianglelefteq G\), and \(P\) is a Sylow \(p\)-subgroup of \(N\).

::: pf-proof

Normality is step [](#s4){.pf-ref}. Since \(N\le G\) contains the Sylow \(p\)-subgroup \(P\) of \(G\), no larger \(p\)-subgroup can occur in \(N\).

:::

:::

::: {.pf-step #s6}

Frattini's argument gives
\[
G=N_G(P)N=N_G(P)\Phi(G).
\]

::: pf-proof

Because \(N\trianglelefteq G\) and \(P\) is a Sylow \(p\)-subgroup of \(N\), Frattini's argument gives \(G=N_G(P)N\). Since \(P\le N_G(P)\) and \(N=P\Phi(G)\), this becomes \(G=N_G(P)\Phi(G)\).

:::

:::

::: {.pf-step #s7}

One must have \(N_G(P)=G\). Hence \(P\trianglelefteq G\).

::: pf-proof

If \(N_G(P)<G\), choose a maximal subgroup \(M\) containing \(N_G(P)\). By definition \(\Phi(G)\subseteq M\). Then step [](#s6){.pf-ref} gives
\[
G=N_G(P)\Phi(G)\subseteq M,
\]
a contradiction. Thus \(N_G(P)=G\), which is equivalent to \(P\trianglelefteq G\).

:::

:::

::: pf-step

Therefore every Sylow subgroup of \(G\) is normal, so \(G\) is nilpotent.

::: pf-proof

The argument in steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} applies to every prime divisor \(p\) of \(|G|\). A finite group is nilpotent if and only if all of its Sylow subgroups are normal.

:::

:::

:::

:::
