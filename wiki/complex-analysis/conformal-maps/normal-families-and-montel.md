---
title: Normal families and Montel
order: 40
problems:
  topics:
  - Normal Families
  - Montel
  - Montel Theorem
  - Montel's Theorem
  - Equicontinuity
---

# Normal families and Montel

Compactness for families of holomorphic functions.
This is the machinery the Riemann mapping theorem runs on: it produces a limit out of a sequence, and [[complex-analysis/counting-zeros/hurwitz|Hurwitz]] then says the limit kept what the sequence had.

::: {.remark}
Throughout, "locally" means "on all compact subsets".
:::

## Equicontinuity

[[D-TIHRR]]

::: {.slogan}
Equicontinuity is uniform continuity which is also uniform across the family.
:::

[[T-6F3GO]]

::: {.remark}
A family of continuous functions that is equicontinuous and pointwise bounded contains a uniformly convergent subsequence, and the limit is continuous.
The proof is an $\eps/3$ argument.
:::

::: {.example title="Negating equicontinuity"}
To negate it, produce $\eps>0$ and a bad triple $(x, y, f\in \mcf)$ such that for any $\delta$ one can arrange $\abs{x-y} < \delta$ while $\abs{f(x) - f(y)} > \eps$.
This gives sequences $x_k, y_k, f_k$ with $\abs{x_k-y_k}\to 0$ but $\abs{f_k(x_k) - f_k(y_k)} > \eps$.
:::

## Normal families

[[D-VZNMF]]

[[T-MCB7V]]

[[D-HL4KE]]

[[D-IJMPJ]]

[[D-MBDTR]]

[[D-PPYCK]]

[[FD-4GI2R]]

::: {.remark title="Univalence, and how the complex case differs"}
If $f: \Omega \to \Omega'$ is a univalent surjection then $f$ is invertible with holomorphic inverse.
The real case is genuinely worse: $f(x) = x^3$ is injective on $(-c,c)$ for every $c$, yet $f'(0)=0$ and $f\inv(x) = x^{1/3}$ is not differentiable at zero.
Holomorphy is what rules that out, and it is why the Riemann mapping theorem can extract a *biholomorphism* rather than merely a bijection.
:::

[[E-ISFYB]] [[E-LXY7N]] [[E-YFL4K]]

## Montel's theorem

[[T-4ALS2]]

::: {.slogan}
Locally uniformly bounded families are normal.
For bounded sequences of holomorphic functions, pointwise convergence is the same as uniform convergence on bounded sets.
:::

::: {.remark}
A sequence of holomorphic functions avoiding the exterior of a disc has a locally uniformly convergent subsequence, and the limit is holomorphic.

Read backwards, this is a useful negative test: if $f_n \to f$ pointwise and $f$ fails continuity or differentiability at even one point, then $\ts{f_n}$ cannot have been uniformly bounded on all compact subsets.
:::

## Exercises

[[E-UJAF4]] [[E-C5QHZ]] [[E-GFNDF]]
