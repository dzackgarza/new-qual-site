---
schema: qual/card@1
id: PR-E6VI4
kind: proposition
title: Kernel of the coset action at smallest-prime index
slogan: 'At smallest-prime index, the coset-action kernel is the subgroup.'
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Normal Subgroups
  - Cosets and Lagrange
relations:
- kind: related-to
  target: PR-PADL7
review: draft
---

::: {.proposition}
Let $G$ be a finite group and $H \leq G$ a subgroup such that $p \coloneqq [G:H]$ is the smallest prime dividing $\abs{G}$.
Let
$$
\phi\colon G\longrightarrow \operatorname{Sym}(G/H)
$$
be the action homomorphism induced by left translation on the left cosets of $H$.
Then
$$
\ker\phi=H.
$$
:::

::: {.proof}
Put $K\coloneqq\ker\phi$.
Then $K\subseteq H$, since $gH=H$ for every $g\in K$.
By the first isomorphism theorem, $G/K$ embeds in $\operatorname{Sym}(G/H)\cong S_p$, so
$$
[G:K]=p[H:K]
$$
divides $p!$. Hence $[H:K]$ divides $(p-1)!$.
Every prime divisor of $[H:K]$ divides $\abs{G}$, so is at least $p$, and every prime divisor of $(p-1)!$ is less than $p$.
Therefore $[H:K]=1$, so $K=H$.
:::
