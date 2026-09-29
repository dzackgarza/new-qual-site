---
schema: qual/card@1
id: P-ALGS17F
kind: problem
title: "The algebraic closure of a prime field is infinite-dimensional"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Let $F$ be a prime field, so that $F$ is either isomorphic to $\mathbb{Q}$ or $\mathbb{F}_p$ for a prime $p$.
Show that the algebraic closure of $F$ is infinite-dimensional over $F$.
:::

::: {.solution}

::: pf

::: pf-step

Let $\overline{F}$ be the algebraic closure of $F$.

::: pf-proof

setup.

:::

:::

::: {.pf-step #s2}

For each positive integer $n$, there is an irreducible polynomial of degree $n$ over $F$.

::: pf-proof

for $F = \mathbb{Q}$, $x^n - 2$ is irreducible (Eisenstein at $2$); for $F = \mathbb{F}_p$, there is an irreducible polynomial of every degree $n$ (the field $\mathbb{F}_{p^n}$ exists, and its generator over $\mathbb{F}_p$ has degree $n$).

:::

:::

::: {.pf-step #s3}

Hence for each $n$, there is an element $\alpha_n \in \overline{F}$ with $[F(\alpha_n) : F] = n$.

::: pf-proof

Step [](#s2){.pf-ref} (a root of an irreducible degree-$n$ polynomial).

:::

:::

::: {.pf-step #s4}

If $\overline{F}$ were finite-dimensional over $F$, say $[\overline{F} : F] = N < \infty$, then every element of $\overline{F}$ would have degree $\le N$ over $F$.

::: pf-proof

the degree of any element is at most the degree of the field extension.

:::

:::

::: {.pf-step #s5}

But step [](#s3){.pf-ref} gives elements of arbitrarily large degree, contradicting step [](#s4){.pf-ref}.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

Hence $\overline{F}$ is infinite-dimensional over $F$.

::: pf-proof

Step [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref}.

:::

:::

:::
