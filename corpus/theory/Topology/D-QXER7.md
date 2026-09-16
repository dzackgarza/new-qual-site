---
schema: qual/card@1
id: D-QXER7
kind: definition
title: Limit of a diagram
classification:
  areas:
  - topology
  topics:
  - Category Theory
relations: []
review: draft
---

::: {.definition}
Let $J$ be a small category, $\mathcal C$ a category, and $F\colon J\to\mathcal C$ a functor.
A \dfn{cone} over $F$ is an object $Y$ of $\mathcal C$ with morphisms $\psi_j\colon Y\to F(j)$ for $j\in J$ such that $F(u)\circ\psi_j=\psi_k$ for every morphism $u\colon j\to k$ in $J$.
A \dfn{limit} of $F$ is a cone $(L,(\pi_j)_{j\in J})$ over $F$ such that for every cone $(Y,(\psi_j)_{j\in J})$ over $F$ there is a unique morphism $h\colon Y\to L$ with $\pi_j\circ h=\psi_j$ for all $j\in J$.
:::

::: {.example}
Products are limits over a category $J$ with no nonidentity morphisms, [[D-VWYRN|pullbacks]] are limits over $\bullet\to\bullet\leftarrow\bullet$, and [[D-OKSJJ|inverse limits]] are limits over a directed set, viewed as a category with a morphism $\beta\to\alpha$ whenever $\alpha\leq\beta$.
:::

::: {.remark}
The dual notion, obtained by reversing every morphism, is the [[D-5MX7E|colimit]].
If every functor $J\to\mathcal C$ has a limit, then $\lim\colon\mathcal C^J\to\mathcal C$ is a right adjoint of the diagonal functor $\Delta\colon\mathcal C\to\mathcal C^J$, which sends an object to the constant functor at it.
:::
