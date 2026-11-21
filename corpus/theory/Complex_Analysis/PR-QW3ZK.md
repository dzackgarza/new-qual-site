---
schema: qual/card@1
id: PR-QW3ZK
kind: proposition
title: Strict maximum principle for complex-valued harmonic functions
slogan: 'A bounded complex-valued harmonic function that attains its maximum modulus inside is constant.'
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Harmonic Functions
relations: []
review: draft
---

::: {.proposition}
Let $D\subseteq\CC$ be a connected open set and let $h=u+iv$ be a complex-valued function on $D$ whose real and imaginary parts are [[D-CFBSA|harmonic]].
(a) If $\abs{h(z)}\le M$ for all $z\in D$ and $\abs{h(z_0)}=M$ for some $z_0\in D$, then $h$ is constant on $D$.

(b) If moreover $D$ is bounded and $h$ extends continuously to $\overline D$, and $\abs{h(z)}\le M$ for all $z\in\bd D$, then $\abs{h(z)}\le M$ for all $z\in D$.

The real input is [@Ahl73, ch. 4, §6, Theorem 23], that a nonconstant harmonic function has neither a maximum nor a minimum in its region; the reduction of (a) to it, through the real harmonic function $\Re(e^{-i\varphi}h)$, is the card's own and is written out below. The boundary form (b) is the usual argument from (a).
:::

::: {.proof}
Write $h(z_0)=Me^{i\varphi}$ and put $U\coloneqq\Re\big(e^{-i\varphi}h\big)=u\cos\varphi+v\sin\varphi$, a real harmonic function on $D$.
Then $U\le\abs{h}\le M$ on $D$ and $U(z_0)=M$, so by the [[PR-6WOTK|strict maximum principle for real harmonic functions]] on a connected open set, $U\equiv M$.
Since $M=U\le\abs{e^{-i\varphi}h}\le M$, the imaginary part of $e^{-i\varphi}h$ vanishes, so $e^{-i\varphi}h\equiv M$ and $h\equiv Me^{i\varphi}$.

For (b), let $N$ be the maximum of $\abs h$ over the compact set $\overline D$. If $N>M$ then $N$ is attained at some $z_0\in D$, since $\abs h\le M$ on $\bd D$; applying (a) with the bound $N$ makes $h$ constant of modulus $N>M$, contradicting $\abs h\le M$ at a boundary point.
:::
