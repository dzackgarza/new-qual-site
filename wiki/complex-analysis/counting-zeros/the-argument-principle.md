---
title: The argument principle
order: 10
topics:
- Argument Principle
- Winding Number
---

# The argument principle

## The logarithmic derivative

[[D-WHYOA]]

:::{.fact}
It converts every zero and pole of a meromorphic $f$ into a *simple* pole of $\logd f$, with the multiplicity as the residue.
If $z_0$ is a root of multiplicity $m$, write $f(z) = (z-z_0)^m g(z)$ with $g$ holomorphic and nonvanishing near $z_0$, and take logarithmic derivatives:
\[
\logd f(z)
&= \logd (z-z_0)^m + \logd g(z) \\
&= {m\over (z-z_0)} + {g'(z) \over g(z)}
.\]
Since $g$ is holomorphic and nonvanishing there, so is $g'/g$, and the only contribution at $z_0$ is $m$.

:::

:::{.remark}
Read arithmetically, the logarithmic derivative picks out the $p\dash$adic valuation at $\gens{x-p} \in \CC[x]$:
\[
d \qty{ \log(f) } = {f'\over f}\dz \implies \Res_{z=p}(d \log(f) ) = v_p(f)
.\]

:::

## The statement

[[D-PJ7JM]]

[[T-JXDQT]]

:::{.proof}
\envlist

- If $z_0$ is a zero of $f$ of order $m$, write $f(z) = (z-z_0)^m g(z)$ with $g$ holomorphic and nonvanishing on a neighborhood of $z_0$, and compute
\[
\logd f(z)
&=
\frac{m\left(z-z_{0}\right)^{m-1} g(z)+\left(z-z_{0}\right)^{m} g^{\prime}(z)}{\left(z-z_{0}\right)^{m} g(z)} \\
&= {m \over z-z_0} + \logd g(z)
,\]
so $z_0$ is a simple pole of $\logd f$ with $\res_{z=z_0} \logd f = m$.

- If $z_0$ is a pole of $f$ of order $m$, write $f(z) = (z-z_0)^{-m} g(z)$, so that
\[
\logd f = {-m \over z-z_0} + \logd g
,\]
and $z_0$ is again a simple pole, now with residue $-m$.

- Apply the residue theorem and group the residues by sign:
\[
{1\over 2\pi i } \int_{\gamma} \logd f(z) \dz
&= \sum_{z_i \in P_{\logd f}} \Res_{z=z_i} \logd f(z)\\
&= \sum_{z_k \in Z_f} \Res_{z=z_k} f(z) - \sum_{z_j \in P_f} \Res_{z=z_j} f(z)
.\]

:::

## The index version

[[T-52HK6]]

:::{.proof}
Change variables by $w = f(z)$, so that $z=\gamma(t) \mapsto w = (f\circ \gamma)(t)$ and $\dw = f'(z) \dz$:
\[
{1\over 2\pi i }\int_{\gamma} \logd f(z) \dz
= {1\over 2\pi i} \int_{f\circ \gamma} {1\over w} \dw \da \Index_{w=0} (f\circ \gamma)(w)
.\]

:::

:::{.example title="Using the index version"}
Let $f(z) = z^2 + z = z(z+1)$.

- $\gamma_1 \da \ts{\abs z = 2}$ encloses 2 zeros and no poles, so $f\circ \gamma_1$ winds twice about the origin counterclockwise.
- $\gamma_2 \da \ts{\abs z = {1\over 2}}$ encloses 1 zero and no poles, so $f\circ \gamma_2$ winds once.

:::

:::{.remark title="Tracking the argument by hand"}
The change in argument can be read off a picture: break the curve into sub-curves and evaluate a branch of $\arg$ at the endpoints.
Here the change is $\pi$ regardless of what the curve does inside $\HH$.

![](../../../../assets/assets/figures/2021-12-10_18-06-04.png)

:::

## Counting solutions of $f(z) = w$

:::{.remark}
The integral
\[
F(w) \da {1\over 2\pi i} \oint_{\bd \Omega} {f'(z) \over f(z) - w} \dz
\]
counts the solutions of $f(z) = w$ in $\Omega$, being $\int_\gamma \logd g_w(z)\dz$ for $g_w(z) \da f(z) - w$.
It is continuous wherever $f \neq w$ on $\bd\Omega$ and takes values in $\ZZ$, hence is constant on connected components.

Also useful: a zero of $f$ of multiplicity $m \geq 2$ is a zero of $f'$, and the same holds for $f - a$.

:::

## Exercises

[[E-VI5ZS]]
[[E-PWVJS]]
[[E-WTCTP]]
