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

[[D-TIHRR]]

::: {.slogan}
An equicontinuous family is uniformly continuous with one $\delta(\varepsilon)$ for every member.
:::

[[T-6F3GO]]

::: {.remark}
Applied on each compact set, the Arzelà--Ascoli theorem shows that a pointwise bounded, equicontinuous sequence of continuous functions on a compact metric space has a uniformly convergent subsequence, whose limit is continuous.
:::

::: {.remark title="Negation of equicontinuity"}
A family $\mathcal F$ of functions on a metric space $X$ is not equicontinuous if and only if there exist $\varepsilon>0$, points $x_k, y_k\in X$, and $f_k\in \mathcal F$ with $\abs{x_k-y_k}\to 0$ and $\abs{f_k(x_k) - f_k(y_k)} \geq \varepsilon$ for all $k$.
:::

## Normal families

[[D-IJMPJ]]

[[D-MBDTR]]

::: {.proposition title="Local boundedness implies equicontinuity"}
Let $\mathcal F$ be a family of holomorphic functions on $\Omega$ that is uniformly bounded on compact subsets.
Then $\mathcal F$ is equicontinuous on every compact $K\subseteq\Omega$.
:::

::: {.proof}
Choose $r>0$ such that $K_{2r}\coloneqq\ts{z : \operatorname{dist}(z,K)\leq 2r}\subseteq\Omega$, and let $M$ bound every $f\in\mathcal F$ on the compact set $K_{2r}$.
For $\xi\in K_r$ the closed disc $\overline{D_r(\xi)}$ lies in $K_{2r}$, so Cauchy's estimate gives $\abs{f'(\xi)}\leq M/r$.
For $z,w\in K$ with $\abs{z-w}<r$, the segment $[z,w]$ lies in $D_r(z)\subseteq K_r$, so $\abs{f(z)-f(w)}\leq (M/r)\abs{z-w}$ for every $f\in\mathcal F$.
:::

Montel's theorem follows by applying the Arzelà--Ascoli theorem on each set of an exhaustion of $\Omega$ by compact sets and taking a diagonal subsequence.

[[T-MCB7V]]

[[D-HL4KE]]

::: {.remark title="Univalent maps"}
If $f\colon \Omega \to \Omega'$ is holomorphic, injective, and surjective, then $f'$ does not vanish, and $f\inv$ is holomorphic.
So a univalent surjection produced by the Riemann mapping argument is a biholomorphism.
:::

::: {.example title="The real analogue fails"}
The map $f(x) = x^3$ is a bijection $\RR\to\RR$ with $f'(0)=0$, and $f\inv(x) = x^{1/3}$ is not differentiable at $0$.
:::

[[E-ISFYB]] [[E-LXY7N]] [[E-YFL4K]]

## Montel's theorem

[[T-4ALS2]]

::: {.slogan}
Locally uniformly bounded families of holomorphic functions are normal.
:::

::: {.remark title="Pointwise convergence"}
If a locally uniformly bounded sequence of holomorphic functions on $\Omega$ converges pointwise on $\Omega$, then it converges locally uniformly.
By Montel's theorem every subsequence has a further subsequence converging locally uniformly, and pointwise convergence forces all of these limits to equal the pointwise limit.
Consequently, if $f_n \to f$ pointwise on $\Omega$ and $f$ is discontinuous or fails to be holomorphic at some point, then $\ts{f_n}$ is not uniformly bounded on compact subsets of $\Omega$.
:::

::: {.example}
A sequence of holomorphic functions on $\Omega$ with values in a fixed disc is uniformly bounded, so it has a locally uniformly convergent subsequence, and the limit is holomorphic.
:::

## Exercises

[[E-UJAF4]] [[E-C5QHZ]] [[E-GFNDF]]
