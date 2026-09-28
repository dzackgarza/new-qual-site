---
title: Maximum modulus and open mapping
order: 60
topics:
- Maximum Modulus Principle
- Maximum Principle
- Minimum Principle
- Open Mapping Theorem

---

# Maximum modulus and open mapping

A nonconstant holomorphic function on a connected open set is an open map, and its modulus has no local maximum.

## The open mapping theorem

[[C-FRF33]]

[[FT-OEYLQ]]

::: {.proof title="Using Rouché's theorem"}

![](../../../../assets/assets/figures/2021-12-14_16-26-16.png)

:::

::: {.proof title="Using the argument principle"}

![](../../../../assets/assets/figures/2022-01-02_02-14-55.png)

![](../../../../assets/assets/figures/2021-12-14_17-24-45.png)

:::

::: {.proof title="Using local degrees"}

![attachments/Pasted image 20211215022640.png](../../../../assets/assets/attachments/Pasted%20image%2020211215022640.png)

:::

::: {.remark title="Common structure of the proofs"}
Each proof shows that for $w$ near $w_0 \coloneqq f(z_0)$ the equation $f(z) = w$ has a solution near $z_0$, by [[complex-analysis/counting-zeros/how-many-zeros-in-this-region|counting zeros]] of $f - w$.
Since $f$ is nonconstant, the zeros of $f - w_0$ are isolated, so there is $r>0$ with $\delta \coloneqq \min_{\abs{z-z_0}=r}\abs{f(z)-w_0} > 0$.
For $\abs{w-w_0}<\delta$, Rouché's theorem applied to $f - w = (f-w_0) + (w_0 - w)$ shows that $f-w$ has as many zeros in $D_r(z_0)$ as $f-w_0$, hence at least one.

:::

## Maximum modulus

[[T-BYNL5]]

[[FT-DWCQ7]]

::: {.proof title="By the open mapping theorem"}
Suppose $\abs{f(z)}\leq\abs{f(z_0)}$ for $z$ in a disc $U$ about $z_0$, and that $f$ is nonconstant on $U$.
By [[C-FRF33|the open mapping theorem]], $f(U)$ is an open set containing $f(z_0)$, so it contains $(1+t)f(z_0)$ for small $t>0$ if $f(z_0)\neq 0$, and a small nonzero value if $f(z_0)=0$.
Either value has modulus larger than $\abs{f(z_0)}$, a contradiction, so $f$ is constant on $U$.

:::

::: {.proof title="By the mean value property"}
Suppose $\abs{f(z)}\leq\abs{f(z_0)}$ on a disc $\DD_R(z_0) \subseteq \Omega$.
For $0<r<R$ the mean value property gives
$$
\abs{f(z_0)} = \abs{{1\over 2\pi} \int_0^{2\pi } f(z_0 + re^{it}) \dt} \leq {1\over 2\pi}\int_0^{2\pi }\abs{f(z_0 + re^{it})} \dt \leq \abs{f(z_0)}
.$$
The integrand $\abs{f(z_0)} - \abs{f(z_0+re^{it})}$ is continuous and nonnegative with integral $0$, so it vanishes, and $\abs f = \abs{f(z_0)}$ on $\DD_R(z_0)$.
If $\abs{f(z_0)} = 0$ then $f\equiv 0$ there.
Otherwise $\bar f = \abs{f(z_0)}^2/f$ is holomorphic on $\DD_R(z_0)$, so $f$ and $\bar f$ both satisfy the Cauchy–Riemann equations, which forces $f' = 0$ and $f$ constant on $\DD_R(z_0)$.
On a connected $\Omega$, the identity principle extends this to $\Omega$.

:::

::: {.remark title="Harmonic functions"}
The first half of the mean value proof uses only continuity and the mean value property, which a real harmonic function $u$ also has; with $u$ in place of $\abs f$ it shows that $u$ is constant near a local maximum.

:::

[[PR-6WOTK]]

::: {.proof title="from Gamelin"}
The set $\ts{u(z)=M}$ is open.
Suppose $u(z_1)=M$ and $\DD_\rho(z_1)\subseteq D$, and write the mean value equality as
$$
0=\int_{0}^{2 \pi}\left[u\left(z_{1}\right)-u\left(z_{1}+r e^{i \theta}\right)\right] \frac{\dtheta}{2 \pi}, \quad 0<r<\rho
.$$
Since $u\leq M$, the integrand is nonnegative and continuous, so it vanishes identically.
Thus $u(z_1+re^{i\theta})=u(z_1)=M$ for all such $r, \theta$, and $\ts{u(z)=M}$ contains a disc about each of its points, hence is open.
The set $\ts{u(z)<M}$ is open by continuity.
Since $D$ is connected one of them is empty, so either $u<M$ throughout or $u\equiv M$.

:::

[[PR-QW3ZK]]

::: {.proof title="from Gamelin"}
Replace $h(z)$ by $\lambda h(z)$ for a unimodular constant $\lambda$ so that $h(z_0) = M$, and set $u = \Re h$.
Then $u$ is harmonic on $D$ and attains its maximum at $z_0$, so $u \equiv M$ by the real version.
Since $\abs h \leq M$ and $\Re h = M$, we get $\Im h = 0$, so $h$ is constant.

:::

[[C-KOFDQ]]

::: {.proof}
Since $\overline D$ is compact and $h$ is continuous on it, $\abs h$ attains its maximum on $\overline D$ at some $z^*$.
If $z^*\in\bd D$, then $\abs h\leq \abs{h(z^*)}\leq M$ on $D$.
If $z^*\in D$, then [[PR-QW3ZK]] makes $h$ constant on $D$, hence on $\overline D$ by continuity, and its constant modulus is at most $M$ because $\bd D$ is nonempty.

:::

## Minimum modulus

[[T-YLI6Y]]

::: {.proof}
Since $f$ does not vanish on $\Omega$, $g \coloneqq 1/f$ is holomorphic on $\Omega$.
A local minimum of $\abs f$ at $z_0$ is a local maximum of $\abs g$ at $z_0$, so $g$, and hence $f$, is constant near $z_0$ by the maximum modulus principle [[T-BYNL5]].
On a connected $\Omega$ the identity principle makes $f$ constant.

:::

::: {.example title="The nonvanishing hypothesis is necessary"}
The function $f(z) = z$ on $\DD$ is nonconstant, and $\abs f$ has its minimum at the interior point $0$.

:::

## Exercises

[[P-FHQAB]]
[[E-7ZCKU]] [[E-RKPAV]]
[[E-SS2.EX-15]]
[[E-ZC34M]]
[[E-ZDVLE]]
[[E-J3QMJ]]
[[E-TYPSR]]
[[E-6IZL3]]
