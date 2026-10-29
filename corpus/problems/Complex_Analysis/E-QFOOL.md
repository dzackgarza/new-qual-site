---
schema: qual/card@1
id: E-QFOOL
kind: problem
title: Automorphisms of the disc fixing $0$ are rotations
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Biholomorphisms
relations: []
review: draft
---

::: {.exercise}
Let $\Delta$ be the open unit disc.
Show that if $f: \Delta\to\Delta$ is a biholomorphism with $f(0) = 0$ then $f$ is a rotation.
:::

::: {.solution}

Let $h \coloneqq f^{-1}$, a biholomorphism of $\Delta$ with $h(0)=0$.

::: pf

::: {.pf-step #isometry}
$\abs{f(z)} = \abs{z}$ for every $z\in\Delta$.

::: pf-proof
By the Schwarz lemma applied to $f$ and to $h$, $\abs{f(z)}\leq\abs{z}$ and $\abs{h(w)}\leq\abs{w}$ for all $z,w\in\Delta$.
With $w=f(z)$,
$$
\abs{z} = \abs{h(f(z))} \leq \abs{f(z)} \leq \abs{z}.
$$
:::

:::

::: pf-step
$f(z) = \lambda z$ for some $\abs{\lambda}=1$.

::: pf-proof
By step [](#isometry){.pf-ref}, equality holds in the Schwarz lemma at any $z\neq0$, so $f$ is a rotation.
:::

:::

:::

:::

::: {.solution title="Using the derivative at 0"}

Let $g \coloneqq f^{-1}$, a biholomorphism of $\Delta$ with $g(0)=0$.

::: pf

::: {.pf-step #derivative}
$\abs{f'(0)} = 1$.

::: pf-proof
By the Schwarz lemma, $\abs{f'(0)}\leq1$ and $\abs{g'(0)}\leq1$.
Since $g\circ f = \operatorname{id}$, the chain rule gives $g'(0)f'(0)=1$, so $\abs{f'(0)} = 1/\abs{g'(0)}\geq1$.
:::

:::

::: pf-step
$f(z) = \lambda z$ for some $\abs{\lambda}=1$.

::: pf-proof
By step [](#derivative){.pf-ref}, equality holds in the Schwarz lemma bound $\abs{f'(0)}\leq1$, so $f$ is a rotation.
:::

:::

:::

:::
