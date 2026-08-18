---
order: 20
---

# Argument Principle

[[D-WHYOA]]

:::{.fact}
It converts all poles and zeros of meromorphic $f$ into simple poles of $\logd f$.
If $z_0$ is a root of $f$ of multiplicity $m$, write $f(z) = (z-z_0)^m g(z)$ with $g$ holomorphic and nonzero near $z_0$.
Then take log derivatives:
\[
\logd f(z) 
&= \logd (z-z_0)^m g(z) \\
&= \logd (z-z_0)^m + \logd g(z) \\
&= {m\over (z-z_0)} + {g'(z) \over g(z)}
.\]

Then if $g$ is holomorphic and nonzero away from $z_0$, so is $g'/g$.
So the only contribution to $\Res_{z=z_0} \logd f$ is $m$.

:::

:::{.remark}
Note that the logarithmic derivative picks up the $p\dash$adic valuation for $\gens{x-p} \in \CC[x]$ a point:
\[
d \qty{ \log(f) } = {f'\over f}\dz  \implies \Res_{z=p}(d \log(f) ) = v_p(f)
.\]

:::

[[D-PJ7JM]]

[[T-JXDQT]]

:::{.proof title="?"}
\envlist

- If $z_0$ is a zero of $f$ of order $m$, write $f(z) = (z-z_0)^m g(z)$ with $g(z)$ holomorphic and nonzero on some neighborhood of $z_0$.
- Compute
\[
\logd f(z)
&=
\frac{m\left(z-z_{0}\right)^{m-1} g(z)+\left(z-z_{0}\right)^{m} g^{\prime}(z)}{\left(z-z_{0}\right)^{m} g(z)} \\
&= {m \over z-z_0} + \logd g(z)
,\]
so $z_0$ is a simple pole of $\logd f$ and $\res_{z=z_0} \logd f = m$.

- If $z_0$ is a pole of $f$ of order $m$, write $f(z) = (z-z_0)^{-m} g(z)$, then
\[
\logd f = {-m \over z-z_0} + \logd g
,\]
  so $z_0$ is a simple pole and $\Res_{z=z_0} \del_{\log f} = -m$.

- Now apply the residue theorem, and group residues according to sign:
\[
{1\over 2\pi i } \int_{\gamma} \del_{\log }f(z) \dz 
&= \sum_{z_i \in P_{\logd f}} \Res_{z=z_i} \logd f(z)\\
&= \sum_{z_k \in Z_f} \Res_{z=z_k} f(z) - \sum_{z_j \in P_f} \Res_{z=z_j} f(z)
.\]

:::

[[T-52HK6]]

:::{.proof title="?"}
Make the change of variables $w = f(z)$, then $z=\gamma(t) \mapsto w = (f\circ \gamma)(t)$ and $\dw = f'(z) \dz$, so
\[
{1\over 2\pi i }\int_{\gamma} \logd f(z) \dz 
= {1\over 2\pi i} \int_{f\circ \gamma} {1\over w} \dw \da \Index_{w=0} (f\circ \gamma)(w)
.\]

:::

:::{.example title="Using the index version of the argument principle"}
Let $f(z) = z^2 + z = z(z+1)$.

- $\gamma_1 \da \ts{\abs z = 2}$ contains 2 zeros and 0 poles, so $f\circ \gamma$ winds twice around zero counterclockwise.
- $\gamma_2 \da \ts{\abs z = {1\over 2}}$ contains 1 zero and 0 poles, so $f\circ \gamma$ winds once.

:::

:::{.remark}
You can track the change in argument by just breaking a curve up into sub-curves and evaluating a branch of the $\arg$ function at the endpoints.
For example, in this picture, the change in argument is $\pi$ no matter what the curve does in $\HH$:

![](../../../../assets/assets/figures/2021-12-10_18-06-04.png)

:::

:::{.remark}
The integral function
\[
F(w) \da {1\over 2\pi i} \oint_{\bd \Omega} {f'(z) \over f(z) - w} \dw
\]
counts the number of solutions to $f(z) = w$ in $\Omega$, since it's of the form $\int_\gamma \logd g_w(z)\dz$ for $g_w(z) \da f(z) - w$.
This is continuous provided $f(z) \neq w$ on $\bd \Omega$ and is $\ZZ\dash$valued, thus constant on connected components.

> Also useful: zeros of $f$ with multiplicity $m\geq 2$ are zeros of $f'$.
  This also holds for $f(z) -a$.

:::

## Exercises

[[E-PWVJS]]
[[E-WTCTP]]
