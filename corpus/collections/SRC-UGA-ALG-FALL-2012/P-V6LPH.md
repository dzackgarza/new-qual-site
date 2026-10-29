---
schema: qual/card@1
id: P-V6LPH
kind: problem
title: 'Groups of order $30$: normal subgroups of orders $3$, $5$, and $15$, presentations,
  and classification'
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Group Presentations
relations: []
review: draft
---

::: {.problem}
Let $G$ be a group of order 30.

a. Show that $G$ contains normal subgroups of orders 3, 5, and 15.

b. Give all possible presentations and relations for $G$.

c. Determine how many groups of order 30 there are up to isomorphism.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The group $G$ contains normal subgroups of orders $3$, $5$, and $15$.


::: pf-proof

By Sylow's theorems, $n_3$ is $1$ or $10$, and $n_5$ is $1$ or $6$. If both were greater than one, distinct Sylow subgroups would contribute $10\cdot2+6\cdot4=44$ nonidentity elements, impossible in a group of order $30$. Therefore a Sylow $3$- or $5$-subgroup $P$ is normal. Its product with a Sylow subgroup for the other odd prime is a subgroup $H$ of order $15$. Sylow's theorems inside $H$ give unique Sylow subgroups of orders $3$ and $5$, so $H\cong C_3\times C_5=C_{15}$. Since $[G:H]=2$, $H$ is normal. Its unique subgroups of orders $3$ and $5$ are characteristic in $H$, hence normal in $G$.

:::

:::

::: {.pf-step #s1-2}

Every group of order $30$ has a presentation
$$
\boxed{G_a=\langle r,s\mid r^{15}=s^2=1,\ srs^{-1}=r^a\rangle,\quad a\in\{1,4,11,14\}}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, choose $H=\langle r\rangle\trianglelefteq G$ of order $15$. Cauchy's theorem gives an involution $s\in G$ and $H\cap\langle s\rangle=1$, so $G=H\rtimes\langle s\rangle$. Conjugation by $s$ maps $r$ to $r^a$ for a unit $a\bmod15$. Since $s^2=1$, one has $a^2\equiv1\pmod{15}$; equivalently $a\equiv\pm1\pmod3$ and $a\equiv\pm1\pmod5$. The four solutions are $1,4,11,14$. Conversely each such action defines a semidirect product of order $30$ with the displayed presentation.

:::

:::

::: {.pf-step #s1-3}

The number of isomorphism classes of groups of order $30$ is
$$
\boxed{4}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives at most four. In $G_a$, the elements outside the odd-order subgroup $\langle r\rangle$ are $sr^k$, and $(sr^k)^2=r^{(a+1)k}$. Thus the number of involutions is $\gcd(a+1,15)$, equal to $1$, $5$, $3$, or $15$ for $a=1,4,11,14$, respectively. Distinct involution counts distinguish these groups, so all four isomorphism classes occur. They are $C_{30}$, $C_3\times D_{10}$, $C_5\times S_3$, and $D_{30}$, with the subscripts on $D$ indicating group orders.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} establish parts (a)--(c), respectively.

:::

:::

:::
