---
schema: qual/card@1
id: P-QJ7MD
kind: problem
title: A subgroup of index $2$ is normal; the same for index the smallest prime dividing
  $\abs{G}$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
---

::: {.problem}
(a) Prove that every subgroup of index $2$ is normal.

(b) More generally, let $G$ be finite and let $p$ be the smallest prime dividing $\abs{G}$. Prove that every subgroup of index $p$ is normal.
:::

::: {.solution}

::: pf

::: pf-step
(a) A subgroup $H\le G$ of index $2$ is normal.

::: pf-proof
There are exactly two left cosets and two right cosets of $H$. For $g\notin H$, both $gH$ and $Hg$ are the complement $G\setminus H$; for $g\in H$, both are $H$. Hence $gH=Hg$ for every $g\in G$, so $H\trianglelefteq G$.
:::

:::

::: pf-step
(b) If $G$ is finite, $p$ is the smallest prime dividing $\abs{G}$, and $[G:H]=p$, then $H\trianglelefteq G$.

::: pf-proof
Let $\rho:G\to S_p$ be the action of $G$ on the $p$ left cosets $G/H$, and $K=\ker\rho$.

::: {.pf-step #image}
$\abs{\rho(G)}=p$.

::: pf-proof
The action is transitive, so $p$ divides $\abs{\rho(G)}$. Also $\abs{\rho(G)}=[G:K]$ divides $\abs{G}$ and, as $\rho(G)\le S_p$, divides $p!$. Every prime divisor of $\abs{G}$ is at least $p$, and every prime divisor of $p!$ is at most $p$, so $\abs{\rho(G)}$ is a power of $p$. Since $p^2\nmid p!$, $\abs{\rho(G)}=p$.
:::

:::

::: pf-step
$H=K$, so $H$ is normal.

::: pf-proof
An element of $K$ fixes the coset $H$, so $K\subseteq H$. By step [](#image){.pf-ref}, $[G:K]=p=[G:H]$, so $K=H$. A kernel is normal.
:::

:::

:::

:::

:::

:::
