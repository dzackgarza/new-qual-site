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

[[FF-XZGIY]]

::: {.remark title="Negation of uniform equicontinuity"}
A family $\mathcal F$ of functions on a metric space $X$ is not uniformly equicontinuous if and only if there exist $\varepsilon>0$, points $x_k, y_k\in X$, and $f_k\in \mathcal F$ with $\abs{x_k-y_k}\to 0$ and $\abs{f_k(x_k) - f_k(y_k)} \geq \varepsilon$ for all $k$.
:::

## Normal families

[[D-QTJ7T]]

[[D-MBDTR]]

[[D-OHFRH]]

::: {.example title="The real analogue fails"}
The map $f(x) = x^3$ is a bijection $\RR\to\RR$ with $f'(0)=0$, and $\inverseof{f}(x) = x^{1/3}$ is not differentiable at $0$.
:::

[[E-YFL4K]]

## Montel's theorem

[[T-4ALS2]]

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
