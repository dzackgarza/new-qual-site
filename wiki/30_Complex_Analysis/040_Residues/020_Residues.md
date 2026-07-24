---
sort: 020
title: Residues
---

# Residues

:::{.remark}
On strategy: see <https://www.damtp.cam.ac.uk/user/reh10/lectures/nst-mmii-chapter5.pdf>

A quick shortcut (?) for the quotient rule:
\[
\dd{}{z} {p(z) \over q(z)} = {p'(z)\over q(z)} - {p(z)q'(z) \over q^2(z)}
.\]
Useful when taking $z\to z_0$ with $z_0$ a root of $p, p', q'$.

:::

:::{.remark}
Pedantic warning: $\Res_{z=p}(f)$ should really be $\Res_{z=p}(df)$ for $df = f(z) \dz$, since it's only an invariant of the 1-form $df$ and not necessarily $f$ itself.
We freely abuse notation!
:::

:::{.remark}
Check: do you need residues at all??
You may be able to just compute an integral!

- If the integrand is holomorphic throughout the region enclosed by $\gamma$, $\int_\gamma f = 0$
- If $f$ has a well-defined primitive $F$ on $\gamma$, then 
\[
\int_\gamma f = \int_\gamma F' = F(\gamma(1)) - F(\gamma(0)) = 0
.\]
- Use Cauchy's theorem when applicable:
\[
\int_\gamma {f(z) \over (z-a)^n} = 2\pi i f^{(n-1)}(a)
.\]

- Compute directly by parameterization:
\[
\int_\gamma f \dz = \int_a^b f(z(t))\, z'(t) \dt && \text{for } z(t) \text{ a parameterization of } \gamma
,\]

  - Note: you can parameterize a circle around $z_0$ using
  \[
  z= z_0 + re^{i \theta }
  .\]

:::

## Residue Formulas

:::{.theorem title="The residue theorem"}
Let $f$ be meromorphic on a region $\Omega$ with poles \( \ts{ \elts{z}{N} } \).
Then for any $\gamma \in \Omega\sm \ts{ \elts{z}{N} }$, 
\[
{1 \over 2\pi i } \int_\gamma f(z) \dz = \sum_{j=1}^N n_\gamma(z_j) \Res_{z=z_j} f
.\]
If $\gamma$ is a toy contour with winding number 1 about each pole, then
\[
{1\over 2\pi i}\int_\gamma f\dz = \sum_{j=1}^N \Res_{z=z_j}f
.\]

:::

:::{.theorem title="The residue formula"}
If $f$ has a pole $z_0$ of order $n$, then
\[  
\Res_{z=z_0} f = \lim_{z\to z_0} {1 \over (n-1)!} \qty{\dd{}{z}}^{n-1} (z-z_0)^n f(z)
.\]

As a special case, if $z_0$ is a simple pole of $f$, then
\[  
\Res_{z=z_0}f = \lim_{z\to z_0} (z-z_0) f(z)
.\]
:::

:::{.corollary title="Residue formula: rational function formula for simple poles"}
If additionally $f=g/h$ where $h(z_0) = 0$ and $h'(z_0)\neq 0$, 
\[
\Res_{z=z_0} {g(z) \over h(z)} = {g(z_0) \over h'(z_0)}
.\]

Note that if $f(z) = 1/h(z)$ and $z_0$ is a simple pole, this reduces to
\[
\Res_{z=z_0}{1\over h(z)} = {1\over h'(z_0)}
.\]

:::

:::{.warnings}
Note that only the denominator gets differentiated, not the numerator!
To remember this, just rederive the equation from L'Hopital's rule and use the product rule on $(z-z_0)g(z)$.
:::

:::{.proof title="Of derivative formula for simple poles"}
Apply L'Hopital:
\[
(z-z_0) {g(z) \over h(z)} = {(z-z_0) g(z) \over h(z) } \equalsbecause{LH}
{g(z) + (z-z_0) g'(z) \over h'(z)} \converges{z\to z_0}\too {g(z_0) \over h'(z_0)}
.\]
:::

:::{.theorem title="Residue formula: poles at infinity"}
\[
\Res_{z=\infty}f(z) = \Res_{z=0} g(z) && g(z) \da -{1 \over z^2}f\qty{1\over z} 
.\]

Note on where this weird formula comes from: residues are associated not to function $f$ but to *differential forms* $f(z)\dz$, and inversion sends $f(z) \dz\to f(1/z)d(1/z) = f(1/z)\cdot -{1\over z^2}\dz$.
This residue can alternatively be calculated for $f$ by taking $\gamma$ a contour enclosing all singularities of $f$ and computing
\[
\Res_{z=\infty}f(z) = -{1\over 2\pi}\int_\gamma f(z) \dz
.\]

:::

:::{.theorem title="Residue formula: fractional residues"}
If $z_0$ is an order 1 pole of $f$ and $\gamma_{\eps, \theta}$ is an arc of the circle $C_\eps \da \ts{ \abs{z-z_0} = \eps}$ subtending an angle of $\theta$, then
\[
\lim_{\eps\to 0} \int_{\gamma_{\eps, \theta}} f(z) \dz  = i\theta \Res_{z = z_0}f(z)
.\]

![](figures/2021-12-22_05-13-02.png)

:::

:::{.proof title="?"}

![](figures/2021-12-22_05-13-27.png)

:::

## Exercises

### Avoiding Residue Formulas

[[E-S6663]]
[[E-M5MWL]]
[[E-RGDJ7]]
[[E-M7K4C]]
[[E-AOQLK]]
[[E-TOZQJ]]
[[E-FCYUM]]
### Applying the formulas

[[E-YNZYA]]
[[E-ITVTT]]
[[E-U2A4C]]
