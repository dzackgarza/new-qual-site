---
schema: qual/card@1
id: PR-E6VI4
kind: proposition
title: A subgroup whose index is the smallest prime dividing $\abs{G}$ is normal
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Normal Subgroups
  - Cosets and Lagrange
relations:
- kind: variant-of
  target: PR-PADL7
review: draft
---

::: {.proposition}
Let $G$ be a finite group and $H \leq G$ a subgroup such that $p \coloneqq [G:H]$ is the smallest prime dividing $\abs{G}$.
Then $H \normal G$.
:::

::: {.proof}
The action of $G$ on the $p$ left cosets of $H$ by left translation gives a homomorphism $\phi\colon G \to S_p$.
Its kernel $K$ satisfies $K \subseteq H$, since $gH = H$ for $g \in K$, and $K \normal G$.
By the first isomorphism theorem, $G/K$ embeds in $S_p$, so $[G:K] = p\,[H:K]$ divides $p!$, hence $[H:K]$ divides $(p-1)!$.
Every prime divisor of $[H:K]$ divides $\abs{G}$, so is at least $p$, and every prime divisor of $(p-1)!$ is less than $p$.
Therefore $[H:K] = 1$, so $H = K$ is normal in $G$.
:::
