---
title: Normal families and Montel
order: 40
topics:
- Normal Families
- Montel
- Equicontinuity

---

# Normal families and Montel

Montel's theorem gives compactness for locally uniformly bounded families of holomorphic functions.
In the proof of the [[complex-analysis/conformal-maps/the-riemann-mapping-theorem|Riemann mapping theorem]] it produces a locally uniformly convergent subsequence of injective maps, and [[complex-analysis/counting-zeros/hurwitz|Hurwitz's theorem]] shows that the nonconstant limit is injective.

::: {.remark}
Throughout, "locally uniformly" means "uniformly on every compact subset".
:::

## Equicontinuity

[[D-2CCDB]]

::: {.slogan}
A uniformly equicontinuous family is uniformly continuous with one $\delta(\varepsilon)$ for every member.
:::

[[FF-XZGIY]]

::: {.remark}
On a compact metric space, a pointwise bounded family that is equicontinuous at every point is uniformly bounded, so the Arzelà--Ascoli theorem applies to it: every sequence in it has a uniformly convergent subsequence, and the limit is continuous.
For holomorphic families on an open set $\Omega\subseteq\CC$, apply this on each compact subset of $\Omega$ and take a diagonal subsequence, which converges locally uniformly on $\Omega$.
:::

::: {.remark title="Negation of uniform equicontinuity"}
A family $\mathcal F$ of functions on a metric space $X$ is not uniformly equicontinuous if and only if there exist $\varepsilon>0$, points $x_k, y_k\in X$, and $f_k\in \mathcal F$ with $\abs{x_k-y_k}\to 0$ and $\abs{f_k(x_k) - f_k(y_k)} \geq \varepsilon$ for all $k$.
:::

## Normal families

[[D-QTJ7T]]

[[D-MBDTR]]

[[D-OHFRH]]

::: {.remark title="Univalent maps"}
If $f\colon \Omega \to \Omega'$ is holomorphic, injective, and surjective, then $f'$ does not vanish, and $\inverseof{f}$ is holomorphic ([[P-Z776N]]).
So a univalent surjection produced by the Riemann mapping argument is a biholomorphism.
:::

::: {.example title="The real analogue fails"}
The map $f(x) = x^3$ is a bijection $\RR\to\RR$ with $f'(0)=0$, and $\inverseof{f}(x) = x^{1/3}$ is not differentiable at $0$.
:::

[[E-YFL4K]]

## Montel's theorem

[[T-4ALS2]]

::: {.slogan}
Locally uniformly bounded families of holomorphic functions are normal.
:::

::: {.remark title="Pointwise convergence"}
If a locally uniformly bounded sequence of holomorphic functions on $\Omega$ converges pointwise on $\Omega$, then it converges locally uniformly.
By Montel's theorem every subsequence has a further subsequence converging locally uniformly, and pointwise convergence forces all of these limits to equal the pointwise limit.
Consequently, if $f_n \to f$ pointwise on $\Omega$ and $f$ is discontinuous or fails to be holomorphic at some point, then $\theset{f_n}$ is not uniformly bounded on compact subsets of $\Omega$.
:::

::: {.example}
A sequence of holomorphic functions on $\Omega$ with values in a fixed disc is uniformly bounded, so it has a locally uniformly convergent subsequence, and the limit is holomorphic.
:::

## Exercises

[[E-UJAF4]] [[E-C5QHZ]] [[E-GFNDF]]
