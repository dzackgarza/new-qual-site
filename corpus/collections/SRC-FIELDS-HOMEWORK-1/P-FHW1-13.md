---
schema: qual/card@1
id: P-FHW1-13
kind: problem
title: Irreducibility and splitting field of $x^5-t$ over $\CC(t)$
classification:
  areas: [algebra]
  topics: [Irreducibility Criteria, Splitting Fields]
relations: []
review: draft
audit:
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Transcribed from the MinerU Flash extraction of assets/attachments/fields-homework-1.pdf and checked against the page image.
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Show that the polynomial $x^5-t$ is irreducible over the field $\CC(t)$ (here $t$ is a variable). Describe a splitting field.
:::

::: {.solution}
Write $t$ for the variable of $\CC(t)$, and let $\rho$ be a root of $x^5-t$ in an algebraic closure of $\CC(t)$, so that $\rho^5=t$.

::: pf

::: {.pf-step #irreducible}
$x^5-t$ is irreducible over $\CC(t)$.

::: pf-proof
The ring $\CC[t]$ is a unique factorization domain in which $t$ is a prime element, and $x^5-t\in\CC[t][x]$ is Eisenstein at $t$: the constant term $-t$ is divisible by $t$ but not by $t^2$, the leading coefficient $1$ is not divisible by $t$, and every other coefficient is $0$.
By Gauss's lemma and the Eisenstein criterion the polynomial is irreducible in $\CC(t)[x]$.
:::

:::

::: {.pf-step #splitting-field}
The splitting field of $x^5-t$ over $\CC(t)$ is $\boxed{\CC(t)(\rho)=\CC(\rho)}$, of degree $5$.

::: pf-proof
Every root of $x^5-t$ has the form $\rho\zeta^k$ with $\zeta=e^{2\pi i/5}$ and $0\le k\le4$, because the roots are the fifth roots of $t$.
The fifth roots of unity lie in $\CC\subseteq\CC(t)$, so every root of $x^5-t$ already lies in $\CC(t)(\rho)$, and $\CC(t)(\rho)$ is generated over $\CC(t)$ by a single root.
Hence $\CC(t)(\rho)$ is the splitting field; by step [](#irreducible){.pf-ref} the polynomial $x^5-t$ is the minimal polynomial of $\rho$, so the degree is $5$.
:::

:::

:::

:::
