---
schema: qual/card@1
id: P-RC7YY
kind: problem
title: Unitary operators, invertibility of $S-\lambda I$ for $|\lambda|<1$, and the
  positive harmonic function $\operatorname{Re}\langle(S+\lambda I)(S-\lambda I)^{-1}v,v\rangle$
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Harmonic Functions
  - Functional Analysis
relations: []
review: draft
---

::: {.problem}
a. Define *unitary operator* on a complex Hilbert space.

b. Let $S$ be a unitary operator on a complex Hilbert space.
Prove that for every complex number $|\lambda|<1$ the operator $S-\lambda I$ is invertible.

c. For a fixed vector $v$ in the Hilbert space and all $|\lambda|<1$, define $$h(\lambda) = \langle (S+\lambda I)(S-\lambda I)^{-1}v, v\rangle.$$ Show $\text{Re}(h)$ is a positive harmonic function (you may not use the spectral theorem).
:::

:::{.solution}
(a) $S:H\to H$ is unitary if $\langle Sx,Sy\rangle = \langle x,y\rangle$ for all $x,y\in H$.

(b) Suppose $(S-\lambda I)x=0$ but $x\ne0$. Then we have
$$0 = \langle (S-\lambda I)x,(S-\lambda I)x\rangle = \langle Sx-\lambda x, Sx-\lambda x\rangle = ||Sx||^2+|\lambda|^2||x||^2-2\text{Re}(\lambda\langle x,Sx\rangle)$$
$$= (1+|\lambda|^2)||x||^2 - 2\text{Re}(\lambda\langle x,Sx\rangle).$$
Thus we have
$$(1+|\lambda|^2)||x||^2 = 2\text{Re}(\lambda\langle x,Sx\rangle) \le 2|\lambda|\,|\langle x,Sx\rangle| \le 2|\lambda|\,||x||\,||Sx|| = 2|\lambda|\,||x||^2.$$
Since we are assuming $x\ne0$ this implies $(1+|\lambda|^2) \le 2|\lambda|$, which is impossible for $|\lambda|<1$. Thus $S-\lambda I$ is injective and therefore invertible. $\square$

(c) [solution not given in source]
:::
