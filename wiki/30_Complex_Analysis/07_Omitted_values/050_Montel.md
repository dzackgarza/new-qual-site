---
order: 50
---

# Montel

::: {.remark}
"Locally" means "on all compact subsets".
:::

## Equicontinuity

[[D-TIHRR]]

::: {.slogan}
Equicontinuity is uniform continuity which is also uniform across the family.
:::

[[T-6F3GO]]

::: {.remark}
If $A$ is a sequence of continuous functions, it contains a subsequence converging uniformly and the limit is continuous.
The proof is an $\eps/3$ argument.
:::

## Normal Families

[[D-VZNMF]]

[[T-MCB7V]]

[[D-HL4KE]]

::: {.remark}
If $f: \Omega \to \Omega'$ is a univalent surjection, $f$ is invertible on $\Omega$ and $f\inv$ is holomorphic.
Compare to real functions: $f(x) = x^3$ is injective on $(-c, c)$ for any $c$ but $f'(0) = 0$ and $f\inv(x) \da x^{1/3}$ is not differentiable at zero.
:::

[[D-IJMPJ]]

[[FD-VTT7T]]

[[D-MBDTR]]

[[D-PPYCK]]

[[FD-4GI2R]]

::: {.remark}
Equicontinuity is uniform continuity, where the uniformity extends across all $f\in \mcf$.
The following is a stark difference between holomorphic and smooth functions, and is used in the Riemann mapping theorem:
:::

::: {.example title="Negating equicontinuity"}
To negate equicontinuity, show that there exists $\eps>0$ and a bad tuple $(x, y, f\in \mcf)$ such that for any $\delta$, we can arrange $\abs{x-y} < \delta$ to be small but $\abs{f(x) - f(y)} > \eps$ is large.
This produces sequences $x_k, y_k, f_k$ with $\abs{x_k-y_k}\to 0$ but $\abs{f_k(x_k) - f_k(y_k)} > \eps$.
:::

[[E-ISFYB]] [[E-LXY7N]] [[E-YFL4K]]

## Montel's Theorem

[[T-4ALS2]]

::: {.slogan}
Locally uniformly bounded families are normal.
For bounded sequences of holomorphic functions, pointwise convergence is the same as uniform convergence on bounded sets.
:::

::: {.remark}
This says that a sequence of holomorphic functions avoiding the exterior of a disc contains a locally uniformly convergent subsequence.
In particular, the limit is holomorphic.

Moreover, if $f_n\to f$ pointwise where $f$ fails continuity or differentiability at a single point, then $\ts{f_n}$ can not be uniformly bounded on all compact subsets.
:::

## Exercise

[[E-UJAF4]] [[E-C5QHZ]] [[E-GFNDF]]
