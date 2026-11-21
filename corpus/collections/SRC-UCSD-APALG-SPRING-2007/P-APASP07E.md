---
schema: qual/card@1
id: P-APASP07E
kind: problem
title: "Minimal idempotent in the group algebra and the left-regular representation character"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $G$ be a finite group, and let $e_\lambda = \sum_g c_g g$ be a minimal idempotent in the simple component of $\CC[G]$ labeled by $\lambda$.
Let $d_\lambda$ be the dimension of a simple $G$-module on which $e_\lambda$ acts nonzero.

(a) What is the dimension of the space $\CC[G] e_\lambda$?
What is $\chi^{\text{reg}}(e_\lambda)$, where $\chi^{\text{reg}}$ is the character of the left-regular representation?

(b) Calculate the coefficient $c_e$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own Wedderburn computation follows, with the dimension, the character value and the coefficient as separate steps.

Let $G$ be finite, $e_{\lambda}$ a minimal idempotent in the $\lambda$-component of $\CC[G]$, and $d_{\lambda}$ the dimension of the corresponding simple module.

::: pf

::: {.pf-step #dimension}
$\dim_{\CC}\CC[G]e_{\lambda}=d_{\lambda}$.

::: pf-proof
By Maschke and Wedderburn, $\CC[G]\cong\bigoplus_{\mu}M_{d_{\mu}}(\CC)$ and the $\lambda$-component is $M_{d_{\lambda}}(\CC)$ acting on itself by left multiplication; a matrix algebra $M_{d}(\CC)$ is a direct sum of $d$ copies of its simple module $\CC^{d}$, and a minimal idempotent is conjugate to the matrix unit $E_{11}$, so $M_{d_{\lambda}}(\CC)e_{\lambda}\cong\CC^{d_{\lambda}}$ has dimension $d_{\lambda}$.
:::

:::

::: {.pf-step #character}
$\chi^{\mathrm{reg}}(e_{\lambda})=d_{\lambda}$.

::: pf-proof
The character of the left regular representation at an element $a$ is the trace of left multiplication by $a$ on $\CC[G]$. Under the Wedderburn decomposition this action acts on the $\lambda$-block $M_{d_{\lambda}}(\CC)$ by left multiplication, whose trace is $d_{\lambda}\operatorname{tr}(a)$ (each of the $d_{\lambda}$ columns of the matrix contributes $\operatorname{tr}$ of the corresponding diagonal entry), and by $0$ on the other blocks. For $a=e_{\lambda}$, conjugate to $E_{11}$ with $\operatorname{tr}E_{11}=1$, the trace is $d_{\lambda}$.
:::

:::

::: {.pf-step #coefficient}
$c_{e}=d_{\lambda}/\cardinality{G}$.

::: pf-proof
On a group element $g$ the regular character is $\chi^{\mathrm{reg}}(g)=\cardinality{G}\delta_{g,e}$, so on $e_{\lambda}=\sum_{g}c_{g}g$ it is $\chi^{\mathrm{reg}}(e_{\lambda})=\sum_{g}c_{g}\chi^{\mathrm{reg}}(g)=\cardinality{G}c_{e}$ (the scalar $\chi^{\mathrm{reg}}(g)$ multiplies, since the character is additive and $\CC$-linear). Comparing with step [](#character){.pf-ref} gives $\cardinality{G}c_{e}=d_{\lambda}$.
:::

:::

::: {.pf-qed}
(a) $\dim\CC[G]e_{\lambda}=d_{\lambda}$ and $\chi^{\mathrm{reg}}(e_{\lambda})=d_{\lambda}$ by steps [](#dimension){.pf-ref} and [](#character){.pf-ref}; (b) $c_{e}=d_{\lambda}/\cardinality{G}$ by step [](#coefficient){.pf-ref}. This is the usual formula $e_{\lambda}=\frac{d_{\lambda}}{\cardinality{G}}\sum_{g}\chi_{\lambda}(g^{-1})g$, whose coefficient at $e$ is $d_{\lambda}/\cardinality{G}$ because $\chi_{\lambda}(1)=d_{\lambda}$.
:::

:::

:::
