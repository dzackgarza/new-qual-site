---
schema: qual/card@1
id: E-HAT-4.3-22
kind: problem
title: "Principal fibrations with sections split"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Show that a principal fibration $\Omega C \to E \xrightarrow{p} B$ is fiber homotopy equivalent to the product $\Omega C \times B$ if it has a section, a map $s: B \to E$ with $ps = \mathbb{1}$.
:::

::: {.solution}

::: pf

::: pf-step

A principal fibration $\Omega C \to E \xrightarrow{p} B$ is a fibration whose fiber is the loop space $\Omega C$, with a compatible action of $\Omega C$ on $E$.

::: pf-proof

definition of a principal fibration.

:::

:::

::: pf-step

The section $s: B \to E$ gives a basepoint in each fiber $p^{-1}(b)$.

::: pf-proof

$s(b) \in p^{-1}(b)$ since $ps = 1$.

:::

:::

::: pf-step

Define $\Phi: \Omega C \times B \to E$ by $\Phi(\omega, b) = \omega \cdot s(b)$ (the action of the loop $\omega$ on the basepoint $s(b)$).

::: pf-proof

use the principal action of the fiber $\Omega C$ on $E$.

:::

:::

::: pf-step

$\Phi$ is a fiber-preserving map over $B$.

::: pf-proof

$p(\Phi(\omega, b)) = p(\omega \cdot s(b)) = p(s(b)) = b$ (the action preserves fibers).

:::

:::

::: pf-step

$\Phi$ restricts to a homotopy equivalence on each fiber.

::: pf-proof

on the fiber over $b$, $\Phi(-, b): \Omega C \to p^{-1}(b)$ is the orbit map $\omega \mapsto \omega \cdot s(b)$, which is a homeomorphism (the action of $\Omega C$ on a principal fiber is free and transitive).

:::

:::

::: {.pf-step #s6}

Hence $\Phi$ is a fiber homotopy equivalence.

::: pf-proof

a fiber-preserving map that is a homotopy equivalence on each fiber is a fiber homotopy equivalence (for fibrations over a CW base, or by the standard criterion).

:::

:::

::: pf-qed

Step [](#s6){.pf-ref}.

:::

:::

:::
