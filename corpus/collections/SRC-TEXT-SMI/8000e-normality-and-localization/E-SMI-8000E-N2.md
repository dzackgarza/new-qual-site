---
schema: qual/card@1
id: E-SMI-8000E-N2
kind: problem
title: Minimal primes of a ufd are principal
classification:
  areas:
  - algebra
  topics:
  - Integral Closure
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
In a ufd $R$, prove all "minimal" prime ideals are principal — i.e. if the only prime ideal contained in $P$ is $\ts{0}$, then $P$ is principal.
:::

::: {.solution}
**Goal.** In a UFD $R$, show a minimal nonzero prime ideal $P$ is principal.

<1>1. Let $0 \neq a \in P$ be a nonzero element.
::: {.proof}
$P \neq 0$ (we consider a minimal nonzero prime).
:::

<1>2. Factor $a = p_1 p_2 \cdots p_k$ into irreducibles.
::: {.proof}
$R$ is a UFD, so every nonzero nonunit factors into irreducibles.
:::

<1>3. Some irreducible factor $p_i$ lies in $P$.
::: {.proof}
$P$ is prime and $p_1 \cdots p_k = a \in P$, so some $p_i \in P$.
:::

<1>4. $(p_i)$ is a prime ideal.
::: {.proof}
in a UFD, an irreducible element generates a prime ideal.
:::

<1>5. $(p_i) \subseteq P$ and $(p_i)$ is prime, so by minimality of $P$, $(p_i) = P$.
::: {.proof}
$P$ is minimal among nonzero primes, and $(p_i)$ is a nonzero prime contained in $P$.
:::

<1>6. Hence $P = (p_i)$ is principal.
::: {.proof}
<1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6 is the claim.
:::
:::
