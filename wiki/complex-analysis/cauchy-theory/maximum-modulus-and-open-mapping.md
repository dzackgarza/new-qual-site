---
title: Maximum modulus and open mapping
order: 60
problems:
  topics:
  - Maximum Modulus Principle
  - Maximum Principle
  - Minimum Principle
  - Open Mapping Theorem

---

# Maximum modulus and open mapping

Two statements of one fact: a nonconstant holomorphic map cannot hold still.
It is open, and therefore its modulus has no interior maximum.

## The open mapping theorem

[[C-FRF33]]

[[FT-OEYLQ]]

:::{.proof title="Using Rouché"}

![](../../../../assets/assets/figures/2021-12-14_16-26-16.png)

:::

:::{.proof title="using the argument principle"}

![](../../../../assets/assets/figures/2022-01-02_02-14-55.png)

![](../../../../assets/assets/figures/2021-12-14_17-24-45.png)

:::

:::{.proof title="using local degrees"}

![attachments/Pasted image 20211215022640.png](../../../../assets/assets/attachments/Pasted%20image%2020211215022640.png)

:::

:::{.remark title="Where the proofs come from"}
All three count solutions of $f(z) = w$ for $w$ near $f(z_0)$ and show the count is positive on a whole neighborhood, which is [[complex-analysis/counting-zeros/how-many-zeros-in-this-region|counting zeros]] again.
Rouché is the shortest route: perturbing $w$ slightly cannot change the number of solutions.

:::

## Maximum modulus

[[T-BYNL5]]

[[FT-DWCQ7]]

:::{.proof title="by the open mapping theorem"}
The map $z\mapsto \abs z$ is open away from $z=0$, and $f$ is open by the previous theorem.
If $\abs f$ attained a maximum at an interior $z_0$, there would be a neighborhood $U \ni z_0$ with $\abs{f(U)}$ open in $\RR$, and such an interval contains values larger than $\abs{f(z_0)}$.

:::

:::{.proof title="by the mean value property"}
Let $z_0\in\Omega$ and pick $R$ with $\DD_R(z_0) \subseteq \Omega$.
The mean value property gives
\[
f(z_0) = {1\over 2\pi} \int_0^{2\pi } f(Re^{it} + z_0) \dt
,\]
so
\[
\abs{f(z_0)} \leq {1\over 2\pi}\int_0^{2\pi }\abs{f(Re^{it} + z_0 )} \dt \leq \max_{t \in [0, 2\pi]} \abs{f(Re^{it} + z_0) }
.\]
Taking $z_R$ to be the maximizing point, $\abs{f(z_0)} \leq \abs{f(z_R)}$.
Since this holds for every $R$, equality throughout forces $f$ constant on $\DD_R(z_0)$, and the identity principle extends that to $\Omega$.

:::

:::{.remark title="The real version underneath"}
The mean value proof never uses holomorphy directly, only the averaging identity, so it proves the statement for harmonic functions at the same time.
That is why the real and complex maximum principles are the same theorem told twice.

:::

[[PR-6WOTK]]

:::{.proof title="from Gamelin"}
The idea is to use the mean value property to show $\ts{u(z)=M}$ is open.
Suppose $u(z_1)=M$ and write the mean value equality as
\[
0=\int_{0}^{2 \pi}\left[u\left(z_{1}\right)-u\left(z_{1}+r e^{i \theta}\right)\right] \frac{\dtheta}{2 \pi}, \quad 0<r<\rho
.\]
The integrand is nonnegative and continuous, so the integral vanishes only if the integrand does.
Thus $u(z_1+re^{i\theta})=u(z_1)=M$ for all such $r, \theta$, and $\ts{u(z)=M}$ contains a disc about each of its points, hence is open.
The set $\ts{u(z)<M}$ is open by continuity.
Since $D$ is connected one of them is empty, so either $u<M$ throughout or $u\equiv M$.

:::

[[PR-QW3ZK]]

:::{.proof title="from Gamelin"}
Replace $h(z)$ by $\lambda h(z)$ for a unimodular constant $\lambda$ so that $h(z_0) = M$, and set $u = \Re h$.
Then $u$ is harmonic on $D$ and attains its maximum at $z_0$, so $u \equiv M$ by the real version.
Since $\abs h \leq M$ and $\Re h = M$, we get $\Im h = 0$, so $h$ is constant.

:::

[[C-KOFDQ]]

:::{.proof}
A continuous function on a compact space attains its maximum modulus; if that happens at an interior point, the strict maximum principle makes $h$ constant.

:::

## Minimum modulus

[[T-YLI6Y]]

:::{.proof}
Suppose $f\neq 0$ on $G$.
If $f$ vanishes somewhere on $\bd G$ we are done, so assume $f \neq 0$ on $\bar G$.
Then $1/f$ is holomorphic on $G$ and continuous on $\bar G$, so $\max_{z\in \bar G}\abs{1/f(z)} = \max_{z\in \bd G} \abs{1/f(z)}$, which is the claim.

:::

:::{.warnings}
The nonvanishing hypothesis is the whole theorem.
A zero of $f$ in the interior is an interior minimum of $\abs f$, so dropping it makes the statement false rather than merely unproven.

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
