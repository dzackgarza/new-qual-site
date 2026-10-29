---
schema: qual/card@1
id: P-6YHN7
kind: problem
title: Schwarz lemma and $g(\{|z|<r\})\subseteq f(\{|z|<r\})$ for holomorphic $f,g:\DD\to\Omega$
  with $f$ a bijection and $f(0)=g(0)$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Biholomorphisms
  - Conformal Maps
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source assumed only f injective, which fails for Omega = D, f(z) = z/2, g(z) = z; the statement now assumes f is a bijection onto Omega.'
---

::: {.problem}
Suppose $f, g: \DD\to \Omega$ are holomorphic with $f$ a bijection onto $\Omega$ and $f(0) = g(0)$.

Show that 
\[  
\Forall 0 < r < 1,\qquad g\qty{\theset{\abs{z} < r}} \subseteq f\qty{\theset{\abs{z} < r}}
.\]

> The first part of this problem asks for a statement of the Schwarz lemma.
:::

::: {.solution}

::: pf

::: {.pf-step #h-self-map}

$h = f^{-1}\circ g$ is a holomorphic map $\DD\to\DD$ with $h(0)=0$.

::: pf-proof

An injective holomorphic map is a biholomorphism onto its image, so $f^{-1}\colon\Omega\to\DD$ is holomorphic. Hence $h$ is holomorphic, and $h(0) = f^{-1}(f(0)) = 0$.

:::

:::

::: {.pf-step #h-disk}

$h(\theset{\abs z<r}) \subseteq \theset{\abs z<r}$ for every $0<r<1$.

::: pf-proof

By step [](#h-self-map){.pf-ref} and Schwarz's lemma, $\abs{h(z)}\le\abs z$ for $z\in\DD$.

:::

:::

::: pf-qed

Since $g = f\circ h$, step [](#h-disk){.pf-ref} gives $g(\theset{\abs z<r}) = f(h(\theset{\abs z<r})) \subseteq f(\theset{\abs z<r})$.

:::

:::

:::
