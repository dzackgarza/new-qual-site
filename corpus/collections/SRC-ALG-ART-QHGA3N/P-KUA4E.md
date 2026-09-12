---
schema: qual/card@1
id: P-KUA4E
kind: problem
title: $N(N(P))=N(P)$ for a Sylow $p$-subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Centralizers and Normalizers
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $G$ be a finite group and let $P$ be a sylow $p\dash$subgroup for $p$ prime.
Show that $N(N(P)) = N(P)$ where $N$ is the normalizer in $G$.
:::

::: {.solution}
Write \(N_G(H)\) for the normalizer of a subgroup \(H\le G\).

<1>1. The subgroup \(P\) is normal in \(N_G(P)\), hence is the unique Sylow \(p\)-subgroup of \(N_G(P)\).
::: {.proof}
By definition, every element of \(N_G(P)\) conjugates \(P\) to itself, so \(P\trianglelefteq N_G(P)\). Since \(P\) is Sylow in \(G\), it has the largest possible \(p\)-power order among subgroups of \(G\), hence also among subgroups of \(N_G(P)\le G\). Thus \(P\) is Sylow in \(N_G(P)\). A normal Sylow subgroup is unique.
:::

<1>2. One always has
\[
N_G(P)\subseteq N_G(N_G(P)).
\]
::: {.proof}
Every subgroup is normal in its own normalizer. Applying this to the subgroup \(N_G(P)\le G\) gives \(N_G(P)\trianglelefteq N_G(N_G(P))\), hence the displayed inclusion.
:::

<1>3. If \(x\in N_G(N_G(P))\), then
\[
xPx^{-1}=P.
\]
::: {.proof}
Because \(x\) normalizes \(N_G(P)\),
\[
xN_G(P)x^{-1}=N_G(P).
\]
Since \(P\le N_G(P)\), this implies \(xPx^{-1}\le N_G(P)\). Conjugation preserves order, so \(xPx^{-1}\) is a Sylow \(p\)-subgroup of \(N_G(P)\). By the uniqueness from <1>1, it must equal \(P\).
:::

<1>4. Therefore
\[
N_G(N_G(P))=N_G(P).
\]
::: {.proof}
By <1>3, every element of \(N_G(N_G(P))\) normalizes \(P\), so
\[
N_G(N_G(P))\subseteq N_G(P).
\]
Combine this with <1>2.
:::
:::
