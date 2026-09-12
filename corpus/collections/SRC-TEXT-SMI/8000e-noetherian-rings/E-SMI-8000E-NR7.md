---
schema: qual/card@1
id: E-SMI-8000E-NR7
kind: problem
title: In any ring every ideal sits in a maximal ideal, using Zorn
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

::: remark
The source says “every ideal,” but the statement necessarily excludes
$I=R$, since maximal ideals are proper.
:::

::: solution
Fix a proper ideal $I\subsetneq R$ and let
$$
\mathcal P
=\{J\subsetneq R:J\text{ is an ideal and }I\subseteq J\},
$$
ordered by inclusion.

<1>1. The poset $\mathcal P$ is nonempty.
::: proof
The ideal $I$ itself belongs to $\mathcal P$.
:::

<1>2. Every chain in $\mathcal P$ has an upper bound in $\mathcal P$.
::: proof
Let $\mathcal C\subseteq\mathcal P$ be a chain. By
[[E-SMI-8000E-NR6]],
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

<1>3. Apply Zorn's lemma.
::: proof
By steps <1>1--<1>2, Zorn's lemma gives a maximal element
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
