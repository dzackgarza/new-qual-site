---
schema: qual/card@1
id: P-2JEMA
kind: problem
title: $\Inn(G)\cong G/Z(G)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Centralizers and Normalizers
  - Isomorphism Theorems
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Reduced the duplicate inner-automorphism proof to the conjugation homomorphism.
---

::: {.problem}
Show that
$$
\Inn(G)\cong G/Z(G).
$$
:::

::: {.solution}
Define
$$
\Phi:G\longrightarrow\Aut(G),
\qquad
\Phi(g)(x)=gxg^{-1}.
$$

::: pf

::: {.pf-step #hom}

$\Phi$ is a homomorphism with image $\Inn(G)$.

::: pf-proof

Each $\Phi(g)$ is an automorphism with inverse $\Phi(g^{-1})$, and $\Phi(gh)(x)=ghxh^{-1}g^{-1}=\Phi(g)(\Phi(h)(x))$. By definition, $\Inn(G)$ is the set of the automorphisms $\Phi(g)$.

:::

:::

::: {.pf-step #kernel}

$\ker\Phi=Z(G)$.

::: pf-proof

$g\in\ker\Phi$ if and only if $gxg^{-1}=x$ for all $x\in G$, that is, if and only if $g\in Z(G)$.

:::

:::

::: pf-step

$G/Z(G)\cong\Inn(G)$.

::: pf-proof

Apply the first isomorphism theorem to $\Phi$, using steps [](#hom){.pf-ref} and [](#kernel){.pf-ref}.

:::

:::

:::

:::
