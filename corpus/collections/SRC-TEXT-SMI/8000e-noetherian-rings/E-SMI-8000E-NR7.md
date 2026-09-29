---
schema: qual/card@1
id: E-SMI-8000E-NR7
kind: problem
title: In any ring every proper ideal lies in a maximal ideal, by Zorn's lemma
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Checked the PDF and extraction. The printed statement says every ideal, but I=R is a counterexample; added the necessary proper-ideal hypothesis."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Applied Zorn to proper ideals containing I, using the union of any chain as a proper upper bound by the preceding exercise."
---

::: {.exercise}
Using Zorn's lemma, prove in any ring $R$ that every proper ideal $I$ of $R$ is contained in a maximal ideal.
:::

::: {.solution}
Fix a proper ideal $I\subsetneq R$ and let
$$
\mathcal P
=\{J\subsetneq R:J\text{ is an ideal and }I\subseteq J\},
$$
ordered by inclusion.

::: pf

::: {.pf-step #s1}

The poset $\mathcal P$ is nonempty.

::: pf-proof

The ideal $I$ itself belongs to $\mathcal P$.

:::

:::

::: {.pf-step #s2}

Every chain in $\mathcal P$ has an upper bound in $\mathcal P$.

::: pf-proof

Let $\mathcal C\subseteq\mathcal P$ be a chain. If $\mathcal C$ is empty,
$I$ is an upper bound. Otherwise, by [[E-SMI-8000E-NR6]],
$$
J_{\mathcal C}=\bigcup_{J\in\mathcal C}J
$$
is a proper ideal of $R$. Every member of the chain contains $I$, so their
union also contains $I$. Thus
$$
J_{\mathcal C}\in\mathcal P,
$$
and it is an upper bound for the chain.

:::

:::

::: pf-step

Apply Zorn's lemma.

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, Zorn's lemma gives a maximal element
$$
\mathfrak m\in\mathcal P.
$$
Thus $\mathfrak m$ is a proper ideal containing $I$.

If $\mathfrak m\subseteq J\subsetneq R$ for an ideal $J$, then $J$ also
contains $I$, so $J\in\mathcal P$. Maximality of $\mathfrak m$ in
$\mathcal P$ forces
$$
J=\mathfrak m.
$$
Hence $\mathfrak m$ is a maximal ideal of $R$ and
$$
\boxed{I\subseteq\mathfrak m.}
$$

:::

:::

:::

:::

::: {.remark}
The source says "every ideal". The unit ideal $R$ lies in no maximal ideal,
since maximal ideals are proper, so the statement holds for proper ideals.
:::
