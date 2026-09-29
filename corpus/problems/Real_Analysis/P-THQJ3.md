---
schema: qual/card@1
id: P-THQJ3
kind: problem
title: $E^\perp$ is a closed subspace of a Hilbert space and $(E^\perp)^\perp=\overline{E}$
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $E \subseteq H$ a Hilbert space.

a. Show that $E\perp \subseteq H$ is a closed subspace.

b. Show that $(E^\perp)^\perp = \cl_H(E)$.
:::
::: {.solution}

::: pf

::: {.pf-step #s1}

$E^\perp$ is a subspace of $H$.

::: pf-proof

$E^\perp = \{x \in H : \langle x, e\rangle = 0 \ \forall e \in E\}$.

If $x, y \in E^\perp$ and $\alpha \in \CC$, then $\langle \alpha x + y, e\rangle = \alpha\langle x,e\rangle + \langle y,e\rangle = 0$ for all $e \in E$, so $\alpha x + y \in E^\perp$.

:::

:::

::: {.pf-step #s2}

$E^\perp$ is closed.

::: pf-proof

if $x_n \in E^\perp$ and $x_n \to x$, then for each $e \in E$, $\langle x, e\rangle = \lim_n \langle x_n, e\rangle = 0$ (continuity of the inner product), so $x \in E^\perp$.

:::

:::

::: {.pf-step #s3}

$E \subseteq (E^\perp)^\perp$, hence $\cl_H(E) \subseteq (E^\perp)^\perp$.

::: pf-proof

for $e \in E$ and $x \in E^\perp$, $\langle e, x\rangle = \overline{\langle x, e\rangle} = 0$, so $e \in (E^\perp)^\perp$.

Since $(E^\perp)^\perp$ is closed by step [](#s2){.pf-ref} (applied to $E^\perp$), the closure of $E$ lies inside it.

:::

:::

::: pf-step

$(E^\perp)^\perp \subseteq \cl_H(E)$.

::: pf-proof

let $M = \cl_H(E)$, a closed subspace.

Take $x \in (E^\perp)^\perp$ and write $x = y + z$ with $y \in M$, $z \in M^\perp$ (Hilbert space projection onto the closed subspace $M$). Since $M^\perp \subseteq E^\perp$ (as $E \subseteq M$), $z \in E^\perp$; and $z = x - y \in (E^\perp)^\perp$ (a subspace, by step [](#s1){.pf-ref}, containing $x$ and $y \in M \subseteq (E^\perp)^\perp$ by step [](#s3){.pf-ref}). Hence $z \in E^\perp \cap (E^\perp)^\perp$, so $\langle z, z\rangle = 0$ and $z = 0$.
Thus $x = y \in M$.

:::

:::

:::

:::
