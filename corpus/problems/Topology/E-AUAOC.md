---
schema: qual/card@1
id: E-AUAOC
kind: problem
title: $S^n$ is not a strong deformation retract of $\bB^{n+1}$
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Homology
  - Homotopy
relations: []
review: draft
---

::: {.exercise}
Show that $S^n$ is not a strong deformation retract of $\bB^{n+1}$.
:::

::: {.solution}
Let $\iota: S^n \injects \bB^{n+1}$ be the inclusion, and suppose, for a contradiction, that $S^n$ is a strong deformation retract of $\bB^{n+1}$.

::: pf

::: {.pf-step #retraction}

There is a map $p: \bB^{n+1} \to S^n$ with $p\circ \iota = \id_{S^n}$.

::: pf-proof

A strong deformation retraction $H: \bB^{n+1}\times[0,1]\to\bB^{n+1}$ ends at a map $p = H(\wait, 1)$ with image in $S^n$ that fixes $S^n$ pointwise.

:::

:::

::: pf-qed

Apply reduced homology $\tilde H_n$. By step [](#retraction){.pf-ref}, $\id_{\tilde H_n(S^n)} = p_*\circ\iota_*$ factors through $\tilde H_n(\bB^{n+1}) = 0$, because $\bB^{n+1}$ is contractible. But $\tilde H_n(S^n)\cong\ZZ\ne 0$, so its identity map does not factor through $0$, a contradiction.

:::

:::

:::
