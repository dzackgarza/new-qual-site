---
schema: qual/card@1
id: PR-PADL7
kind: proposition
title: A subgroup whose index is the smallest prime dividing $\abs{G}$ is normal
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Normal Subgroups
  - Cosets and Lagrange
relations: []
review: draft
---

::: {.proposition}
Let $G$ be a finite group, let $p$ be the smallest prime dividing $\abs{G}$, and let $H\leq G$ be a subgroup of [[D-VJGH5|index]] $[G:H]=p$.
Then $H$ is [[D-EKE4Q|normal]] in $G$.
:::

::: {.proof}
Let $G$ act on the set $G/H$ of left cosets by left translation, $g\cdot xH=gxH$.
This action is a homomorphism $\varphi\colon G\to\operatorname{Sym}(G/H)\cong S_p$; let $K\coloneqq\ker\varphi$.
If $g\in K$ then $gH=H$, so $K\subseteq H$, and $K\normal G$.
By the first isomorphism theorem $G/K$ embeds in $S_p$, so $[G:K]$ divides $p!$.
Also $[G:K]$ divides $\abs{G}$, so every prime factor of $[G:K]$ is at least $p$; the only such prime dividing $p!$ is $p$, and $p^2\nmid p!$.
Hence $[G:K]\in\theset{1,p}$.
Since $K\subseteq H$, $[G:K]\geq[G:H]=p$, so $[G:K]=p$ and $K=H$.
Therefore $H=\ker\varphi$ is normal in $G$.
:::
