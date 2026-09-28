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

::: {.fact}
Every zero of a meromorphic $f$ is a simple pole of $\logd f$ whose residue is its multiplicity.
If $z_0$ is a root of multiplicity $m$, write $f(z) = (z-z_0)^m g(z)$ with $g$ holomorphic and nonvanishing near $z_0$, and take logarithmic derivatives:
$$
\begin{aligned}
\logd f(z)
&= \logd (z-z_0)^m + \logd g(z) \\
&= {m\over (z-z_0)} + {g'(z) \over g(z)}
\end{aligned}.$$
Since $g$ is holomorphic and nonvanishing there, so is $g'/g$, and the only contribution at $z_0$ is $m$.

:::

::: {.remark}
For a nonzero rational function $f\in\CC(x)$ and $p\in\CC$, the residue of the logarithmic derivative at $p$ is the valuation $v_p(f)$ of $f$ at the prime ideal $\gens{x-p} \subseteq \CC[x]$:
$$
d \qty{ \log(f) } = {f'\over f}\dz \implies \Res_{z=p}(d \log(f) ) = v_p(f)
.$$

:::

## The statement

[[D-PJ7JM]]

[[T-JXDQT]]

::: {.proof}
\envlist

- If $z_0$ is a zero of $f$ of order $m$, write $f(z) = (z-z_0)^m g(z)$ with $g$ holomorphic and nonvanishing on a neighborhood of $z_0$, and compute
$$
\begin{aligned}
\logd f(z)
&=
\frac{m\left(z-z_{0}\right)^{m-1} g(z)+\left(z-z_{0}\right)^{m} g^{\prime}(z)}{\left(z-z_{0}\right)^{m} g(z)} \\
&= {m \over z-z_0} + \logd g(z)
\end{aligned},$$
so $z_0$ is a simple pole of $\logd f$ with $\res_{z=z_0} \logd f = m$.

- If $z_0$ is a pole of $f$ of order $m$, write $f(z) = (z-z_0)^{-m} g(z)$, so that
$$
\logd f = {-m \over z-z_0} + \logd g
,$$
and $z_0$ is again a simple pole, now with residue $-m$.

- Apply the residue theorem and group the residues by sign:
$$
\begin{aligned}
{1\over 2\pi i } \int_{\gamma} \logd f(z) \dz
&= \sum_{z_i \in P_{\logd f}} \Res_{z=z_i} \logd f(z)\\
&= \sum_{z_k \text{ a zero of } f} \operatorname{ord}_{z_k} f - \sum_{z_j \text{ a pole of } f} \operatorname{ord}_{z_j} (1/f) \\
&= Z_f - P_f
\end{aligned}.$$

:::

## The index version

[[T-52HK6]]

::: {.proof}
Change variables by $w = f(z)$, so that $z=\gamma(t) \mapsto w = (f\circ \gamma)(t)$ and $\dw = f'(z) \dz$:
$$
{1\over 2\pi i }\int_{\gamma} \logd f(z) \dz
= {1\over 2\pi i} \int_{f\circ \gamma} {1\over w} \dw = \Index_{w=0} (f\circ \gamma)
.$$

:::

::: {.example title="Using the index version"}
Let $f(z) = z^2 + z = z(z+1)$.

- $\gamma_1 \coloneqq \ts{\abs z = 2}$ encloses 2 zeros and no poles, so $f\circ \gamma_1$ winds twice about the origin counterclockwise.
- $\gamma_2 \coloneqq \ts{\abs z = {1\over 2}}$ encloses 1 zero and no poles, so $f\circ \gamma_2$ winds once.

:::

::: {.remark title="Tracking the argument by hand"}
The winding number is the total change of a continuous branch of $\arg$ along the image curve, divided by $2\pi$, and it is additive over sub-curves.
For a curve in $\HH$ from a point of $(0,\infty)$ to a point of $(-\infty,0)$, a continuous branch of $\arg$ with values in $[0,\pi]$ changes by $\pi$.

![](../../../../assets/assets/figures/2021-12-10_18-06-04.png)

:::

## Counting solutions of $f(z) = w$

::: {.remark}
The integral
$$
F(w) \coloneqq {1\over 2\pi i} \oint_{\bd \Omega} {f'(z) \over f(z) - w} \dz
$$
is $\frac{1}{2\pi i}\oint_{\bd\Omega} \logd g_w(z)\dz$ for $g_w(z) \coloneqq f(z) - w$, so for holomorphic $f$ it counts the solutions of $f(z) = w$ in $\Omega$ with multiplicity.
It is a continuous function of $w$ on each connected component of $\CC\sm f(\bd\Omega)$ and takes values in $\ZZ$, hence is constant on each component.

A solution of $f(z) = a$ of multiplicity $m \geq 2$ is a zero of $f'$.

:::

## Exercises

[[E-VI5ZS]]
[[E-PWVJS]]
[[E-WTCTP]]
