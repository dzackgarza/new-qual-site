---
schema: qual/card@1
id: FD-6WSIA
kind: definition
title: Separable field extension
prompts:
- What does it mean for a field extension $L/K$ to be separable?
- What does it mean for a field extension $L/K$ to be separable, in terms of minimal polynomials?
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Field Extensions
relations: []
review: draft
---

::: {.definition}
Let $L/K$ be an algebraic field extension.
$L/K$ is \dfn{separable} if for every $\alpha \in L$ the minimal polynomial $m_\alpha\in K[x]$ of $\alpha$ over $K$ is [[D-ZT46D|separable]].
:::

::: {.proposition}
Let $K$ be a field and $f\in K[x]$ irreducible.
Then $f$ is separable if and only if its formal derivative $f'$ is nonzero.
:::

::: {.proof}
Let $\bar K$ be an algebraic closure of $K$.
A root $\beta\in\bar K$ of $f$ is repeated if and only if $f'(\beta)=0$, since writing $f=(x-\beta)g$ gives $f'(\beta)=g(\beta)$.
If $f'=0$, every root of $f$ is repeated, so $f$ is not separable.
If $f'\neq0$ and $\beta$ is a repeated root, then $f$, being irreducible, is a scalar multiple of the minimal polynomial of $\beta$ over $K$, so $f$ divides $f'$; this is impossible because $\deg f'<\deg f$ and $f'\neq0$.
:::
