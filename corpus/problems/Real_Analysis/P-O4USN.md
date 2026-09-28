---
schema: qual/card@1
id: P-O4USN
kind: problem
title: $\nu\perp\mu$ and $\nu\ll|\mu|$ implies $\nu=0$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Radon-Nikodym
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $\nu, \mu$ be signed measures, and show that
\[
\nu \perp \mu \text{ and } \nu \ll \abs{ \mu} \implies \nu = 0
.\]
:::
::: {.solution}
<1>1. There is a measurable $A$ with $|\mu|(A) = 0$ and $|\nu|(A^c) = 0$.

::: {.proof}
This is the definition of $\nu \perp \mu$: there is a partition $X = A \sqcup A^c$ with $A$ null for $\mu$ and $A^c$ null for $\nu$, and a set is null for a signed measure exactly when it has total variation measure $0$.
:::

<1>2. $|\nu|(A) = 0$.

::: {.proof}
$\nu \ll |\mu|$ means $|\nu|(E) = 0$ whenever $|\mu|(E) = 0$, equivalently $\nu(E) = 0$ for every measurable $E$ with $|\mu|(E) = 0$. Apply it to $E = A$ from step <1>1.
:::

<1>3. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2, $|\nu|(X) = |\nu|(A) + |\nu|(A^c) = 0$. Since $|\nu(E)| \le |\nu|(E)$ for every $E$, $\nu = 0$.
:::
:::
