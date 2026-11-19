---
schema: qual/card@1
id: PR-ASW5L
kind: proposition
title: An ideal of an integral domain is free if and only if it is principal
slogan: 'Over an integral domain, an ideal is free as a module exactly when it is principal.'
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Ideals
  - Principal Ideal Domains
relations: []
review: draft
---

::: {.proposition}
Let $R$ be an [[D-QJ3QL|integral domain]] and $I \subseteq R$ an ideal.
Then $I$ is a [[D-LIEMF|free]] $R$-module if and only if $I$ is a [[D-D7VK2|principal]] ideal.
:::

::: {.proof}
Suppose first that $I$ is free with basis $B$.
If $I=0$ then $I=\generations 0$ is principal, so suppose $I\neq0$, which makes $B$ nonempty.
Suppose $B$ contains distinct elements $m_1,m_2$.
Since $R$ is commutative,
$$
(-m_2)\, m_1 + m_1\, m_2 = 0,
$$
which is a relation among distinct basis elements whose coefficients $-m_2$ and $m_1$ are nonzero, an element of a basis being nonzero.
This contradicts $B$ being a basis, so $B=\theset m$ has one element and $I=\generations m$ is principal.

Conversely, let $I=\generations m$ be principal.
If $m=0$ then $I=0$ is free on the empty family.
If $m\neq0$ then every $x\in I$ is $\alpha m$, and $\alpha m=0$ forces $\alpha=0$ because $R$ is a domain, so $\theset m$ is a basis of $I$.
:::

::: {.example}
Over a ring with zero divisors, a principal ideal need not be free.
In $\ZZ/6\ZZ$, the principal ideal $\generators{2}$ is not a free $\ZZ/6\ZZ$-module, since $3 \cdot 2 = 0$ with $3 \neq 0$, whereas a nonzero element of a basis of a free module has zero annihilator.
:::
