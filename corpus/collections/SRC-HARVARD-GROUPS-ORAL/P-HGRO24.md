---
schema: qual/card@1
id: P-HGRO24
kind: problem
title: Finite p-groups are solvable
classification:
  areas: [algebra]
  topics: [Solvable Groups]
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $G$ be a group of order $p^r$, where $p$ is prime.
Prove that $G$ is solvable.
:::

::: {.solution}

::: pf

::: pf-step

$G$ has a nontrivial center $Z(G) \neq 1$.

::: pf-proof

the class equation $|G| = |Z(G)| + \sum [G : C_G(g_i)]$; each $[G : C_G(g_i)]$ is divisible by $p$, and $|G| = p^r$ is divisible by $p$, so $p \mid |Z(G)|$, hence $Z(G) \neq 1$.

:::

:::

::: pf-step

$Z(G)$ is abelian and normal in $G$.

::: pf-proof

the center is always abelian and normal.

:::

:::

::: {.pf-step #s3}

$G/Z(G)$ has order $p^{r'}$ with $r' < r$.

::: pf-proof

$|Z(G)| > 1$ divides $p^r$, so $|G/Z(G)| = p^{r'}$ with $r' < r$.

:::

:::

::: {.pf-step #s4}

By induction on $r$, $G/Z(G)$ is solvable.

::: pf-proof

the base case $r = 0$ (trivial group) is solvable; step [](#s3){.pf-ref} reduces the exponent.

:::

:::

::: {.pf-step #s5}

Hence $G$ is solvable.

::: pf-proof

$1 \trianglelefteq Z(G) \trianglelefteq G$ with $Z(G)$ abelian and $G/Z(G)$ solvable (step [](#s4){.pf-ref}); an extension of a solvable group by an abelian group is solvable.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref}.

:::

:::

:::
