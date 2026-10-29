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
---

::: {.problem}
Let $P = S_p$ be a Sylow $p$-subgroup of a finite group $G$.
Prove that the normalizer of $N_G(P)$ is self-normalizing:
$$N_G\bigl(N_G(P)\bigr) = N_G(P).$$
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
