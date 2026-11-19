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
:::

::: {.proof}
Write $h(z_0)=Me^{i\varphi}$ and put $U\coloneqq\Re\big(e^{-i\varphi}h\big)=u\cos\varphi+v\sin\varphi$, a real harmonic function on $D$.
Then $U\le\abs{h}\le M$ on $D$ and $U(z_0)=M$, so by the [[PR-6WOTK|strict maximum principle for real harmonic functions]] on a connected open set, $U\equiv M$.
Since $M=U\le\abs{e^{-i\varphi}h}\le M$, the imaginary part of $e^{-i\varphi}h$ vanishes, so $e^{-i\varphi}h\equiv M$ and $h\equiv Me^{i\varphi}$.

For (b), if $\abs h$ exceeded $M$ at an interior point, its maximum over the compact set $\overline D$ would be attained at an interior point $z_0$, and (a) would make $h$ constant with $\abs{h(z_0)}>M$, contradicting the bound on $\bd D$ at any boundary point.
:::
