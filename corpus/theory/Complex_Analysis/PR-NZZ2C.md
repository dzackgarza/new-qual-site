---
schema: qual/card@1
id: PR-NZZ2C
kind: proposition
title: Zeros of $f'$ are isolated, and $f'=g'$ implies $f-g$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Holomorphic Functions
relations: []
review: draft
---

::: {.proposition}
Let $\Omega\subseteq\CC$ be a connected open set.

(a) If $f$ is [[D-V6UQJ|analytic]] and nonconstant on $\Omega$, then $f'$ is analytic on $\Omega$ and the [[D-65VIK|zeros]] of $f'$ are isolated.

(b) If $f,g$ are analytic on $\Omega$ with $f'=g'$, then $f-g$ is constant on $\Omega$.
:::

::: {.proof}
(a) A power series can be differentiated term by term inside its disc of convergence, so $f'$ is analytic on $\Omega$.
If $f'\equiv0$ on $\Omega$, then $f$ is locally constant, hence constant because $\Omega$ is connected.
So $f'$ is an analytic function on a connected open set that is not identically zero, and its zeros are isolated.

(b) Put $h\coloneqq f-g$. Then $h'=0$ on $\Omega$, so $h$ is locally constant: on a disc $D\subseteq\Omega$, $h(z)-h(z_0)=\int_{[z_0,z]}h'(w)\,dw=0$.
The set $\ts{z\in\Omega\st h(z)=h(z_0)}$ is therefore open, and it is closed by continuity, so it is all of $\Omega$.
:::
