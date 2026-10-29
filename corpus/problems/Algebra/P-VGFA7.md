---
schema: qual/card@1
id: P-VGFA7
kind: problem
title: Homomorphisms from $S_n$ to a group of odd order
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Homomorphisms
  - Normal Subgroups
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
Let $n \ge 2$, and let $G$ be a finite group of odd order $\abs{G} = m$.
Let $\phi: S_n \to G$ be a group homomorphism.

(a) Prove that if $\tau \in S_n$ is a transposition, then $\tau \in \ker\phi$.

(b) Prove that $\phi$ is the trivial homomorphism ($\ker\phi = S_n$).

(c) Does this result depend on whether $n$ is even or odd?
:::

::: {.solution}

::: pf

::: {.pf-step #transp}

(a) Every transposition $\tau$ lies in $\ker\phi$.

::: pf-proof

Since $\tau^2=1$, $\phi(\tau)^2=1$, so the order of $\phi(\tau)$ divides $2$. It also divides $\abs{G}$, which is odd. Hence $\phi(\tau)$ has order $1$, so $\phi(\tau)=1$.

:::

:::

::: {.pf-step #trivial}

(b) $\ker\phi=S_n$.

::: pf-proof

Transpositions generate $S_n$, and by step [](#transp){.pf-ref} they all lie in the subgroup $\ker\phi$.

:::

:::

::: pf-step

(c) The result does not depend on the parity of $n$.

::: pf-proof

Steps [](#transp){.pf-ref} and [](#trivial){.pf-ref} use only $n\ge2$.

:::

:::

:::

:::
