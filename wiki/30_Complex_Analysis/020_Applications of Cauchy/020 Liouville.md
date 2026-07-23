# Liouville's Theorem

:::{.theorem title="Liouville's Theorem" ref="Liouville"}
If $f$ is entire and bounded, $f$ is constant.
:::

:::{.proof title="of Liouville"}
\envlist

- Since $f$ is bounded, $f(z) \leq M$ uniformly on $\CC$.
- Apply Cauchy's estimate for the 1st derivative:
\[
\abs{f'(z)} \leq { 1! \norm{f}_{C_R} \over R } \leq {M \over R}\converges{R\to\infty}\too 0
,\]
  so $f'(z) = 0$ for all $z$.
:::

:::{.proof title="of Liouville, alternative"}

![](figures/2021-12-14_16-51-04.png)

:::

:::{.proof title="of Liouville, using Schwarz"}
Suppose $f$ is entire and bounded.
Under an affine change of variables in the domain and range, $f(0) = 0$ and $\abs{f(z)} \leq 1$, the claim is that $f\equiv 0$.
The function $g(z) \da f(Rz)$ satisfies the Schwarz lemma, so $\abs{f(Rz)} \leq \abs{z} \implies \abs{f(w)} \leq \abs{w}/R\convergesto{R\to\infty}0$.
:::

## Exercises

[[E-ORZ5S]]
[[E-3SZF6]]
[[E-WLFTP]]
[[E-VJ2QJ]]
[[E-CRMAC]]
[[E-FSLYP]]
[[E-Q6MJ4]]
[[E-GQRIP]]
[[E-YPKWZ]]
[[E-FQCKR]]
[[E-IJ6X6]]
