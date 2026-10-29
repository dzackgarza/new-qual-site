---
schema: qual/card@1
id: P-LJURM
kind: problem
title: A polynomial with Galois group $S_3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Give a polynomial with $S_3$ as its Galois group over $\QQ$, and prove it.
:::

::: {.solution}
Let $f(x)=x^3-2$, $\alpha=\sqrt[3]{2}\in\RR$, and $\omega$ a primitive cube root of unity.

::: pf

::: {.pf-step #splitting}
The splitting field of $f$ is $K=\QQ(\alpha,\omega)$, and $[K:\QQ]=6$.

::: pf-proof
The roots of $f$ are $\alpha$, $\alpha\omega$, $\alpha\omega^2$, which generate $\QQ(\alpha,\omega)$. By Eisenstein's criterion at $2$, $f$ is irreducible, so $[\QQ(\alpha):\QQ]=3$. Since $\QQ(\alpha)\subset\RR$ and $\omega\notin\RR$ is a root of $x^2+x+1$, $[K:\QQ(\alpha)]=2$.
:::

:::

::: pf-step
$\Gal(K/\QQ)\cong S_3$, so $\boxed{x^3-2}$ has Galois group $S_3$ over $\QQ$.

::: pf-proof
The Galois group acts faithfully on the three roots of the separable cubic $f$, so it embeds in $S_3$. By step [](#splitting){.pf-ref} it has order $6=\abs{S_3}$.
:::

:::

:::

:::
