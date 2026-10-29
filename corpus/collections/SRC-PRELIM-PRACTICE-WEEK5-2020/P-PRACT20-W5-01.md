---
schema: qual/card@1
id: P-PRACT20-W5-01
kind: problem
title: A unique element of order $2$ is central
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 1).
---

::: {.problem}
Suppose $G$ is a group and $x \in G$ is only element in $G$ of order $2$. Show that $xa = ax$ for all $a \in G$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $a\in G$, the conjugate
$$
axa^{-1}
$$
has order $2$.


::: pf-proof

Since $x$ has order $2$,
$$
x^2=e.
$$
Therefore
$$
(axa^{-1})^2
=axa^{-1}axa^{-1}
=ax^2a^{-1}
=e.
$$
Also $axa^{-1}\ne e$, because otherwise conjugating by $a^{-1}$ would give
$x=e$, contradicting that $x$ has order $2$. Hence $axa^{-1}$ has order
exactly $2$.

:::

:::

::: {.pf-step #s1-2}

For every $a\in G$,
$$
axa^{-1}=x.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, $axa^{-1}$ is an element of order $2$. By hypothesis, $x$ is
the unique element of $G$ of order $2$. Hence the two elements are equal.

:::

:::

::: {.pf-step #s1-3}

Thus
$$
\boxed{xa=ax\qquad(a\in G)}.
$$


::: pf-proof

From step [](#s1-2){.pf-ref},
$$
axa^{-1}=x.
$$
Multiplying on the right by $a$ gives
$$
ax=xa,
$$
equivalently $xa=ax$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves that $x$ commutes with every element of $G$.

:::

:::

:::
