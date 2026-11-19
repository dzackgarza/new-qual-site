---
schema: qual/card@1
id: P-HGRO28
kind: problem
title: A Sylow normalizer is self-normalizing
classification:
  areas: [algebra]
  topics: [Sylow Theory]
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against the Lamport standard and checked: this is the Frattini argument. N <= N_G(N) is
    trivial. For the reverse inclusion, g in N_G(N) gives gPg^{-1} <= gNg^{-1} = N, and both P and
    gPg^{-1} are Sylow p-subgroups of N because |P| is the full p-part of |G| and hence of |N| (N
    contains P); Sylow conjugacy inside N gives n in N with gPg^{-1} = nPn^{-1}, so n^{-1}g
    normalizes P and lies in N, whence g in N. The card's steps follow this exactly, and the point
    that |P| is the full p-part of |N| is stated. Not claimed: any statement about N_G(H) for
    non-Sylow H, where the equality fails.
---

::: {.problem}
Let $P$ be a Sylow $p$-subgroup of a finite group $G$.
Prove that $N_G\bigl(N_G(P)\bigr) = N_G(P)$.
:::

::: {.solution}
Let $N\coloneqq N_G(P)$.

::: pf

::: {.pf-step #s1}

$N\subseteq N_G(N)$.

::: pf-proof

Every subgroup normalizes itself.

:::

:::

::: {.pf-step #s2}

$N_G(N)\subseteq N$.

::: pf-proof

Let $g\in N_G(N)$. Since $P\le N$ and $gNg^{-1}=N$, we have
$gPg^{-1}\le N$. The subgroups $P$ and $gPg^{-1}$ of $N$ have order $\abs{P}$,
the full $p$-part of $\abs{G}$ and hence of $\abs{N}$, so both are Sylow
$p$-subgroups of $N$. By Sylow's conjugacy theorem in $N$, there is $n\in N$
with $gPg^{-1}=nPn^{-1}$. Then $(n^{-1}g)P(n^{-1}g)^{-1}=P$, so
$n^{-1}g\in N$, and $g=n(n^{-1}g)\in N$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give $N_G(N_G(P))=N_G(P)$.

:::

:::

:::
