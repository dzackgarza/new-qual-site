---
title: Cauchy estimates and Liouville
order: 30
topics:
- Cauchy Estimates
- Growth Estimates
- Derivative Estimates
---

# Cauchy estimates and Liouville

## The estimates

[[T-22RQZ]]

[[FT-5MASA]] [[FT-REHJT]]

[[FF-HO7RN]]

::: {.slogan}
The $k$th Taylor coefficient of $f$ at $z_0$ is bounded by the supremum of $\abs f$ on a circle of radius $R$ about $z_0$, divided by $R^k$:
$$
\abs{c_k} \leq {\sup_{\abs{z-z_0}=R}\abs{f(z)} \over R^k}
.$$

:::

::: {.proof title="Cauchy's inequality"}
\envlist

- Given $z_0\in \Omega$, let $r>0$ with $\overline{D_r(z_0)} \subset \Omega$, let $C = \bd D_r(z_0)$, and let $M\coloneqq \sup_{C}\abs f$.
- Apply the integral formula for $f^{(n)}$:

$$
\begin{aligned}
\left|f^{(n)}(z_0)\right|
&= \abs{ \frac{n !}{2 \pi i} \int_{C} \frac{f(\zeta) }{(\zeta-z_0)^{n+1}} \dzeta } \\
&=\left|\frac{n !}{2 \pi i} \int_{0}^{2 \pi} \frac{f\left(z_0 + r e^{i \theta}\right) r i e^{i \theta} }{\left(r e^{i \theta}\right)^{n+1}} \dtheta \right| \\
&\leq \frac{n !}{2 \pi} \int_{0}^{2 \pi}\left|\frac{f\left( z_0 +r e^{i \theta}\right) r i e^{i \theta}}{\left(r e^{i \theta}\right)^{n+1}}\right| \dtheta \\
&=\frac{n !}{2 \pi} \int_{0}^{2 \pi} \frac{\left|f\left(z_0 +r e^{i \theta}\right)\right|}{r^{n}} \dtheta \\
&\leq \frac{n !}{2 \pi} \int_{0}^{2 \pi} \frac{M}{r^{n}} \dtheta \\
&=\frac{M n !}{r^{n}}
\end{aligned}.$$

:::

::: {.remark title="Growth bounds for entire functions"}
Let $f$ be entire with $\abs{f(z)} \leq A \abs z^n$ for all $\abs z\geq R_0$.
For fixed $z_0$ and large $R$, $\abs f\leq A(R+\abs{z_0})^n$ on the circle $\abs{z-z_0}=R$, so the estimate gives $\abs{f^{(n+1)}(z_0)} \leq (n+1)!\,A (R+\abs{z_0})^n/R^{n+1}\to 0$ as $R\to\infty$.
Hence $f^{(n+1)}\equiv 0$ and $f$ is a polynomial of degree at most $n$.
The case $n=0$ is Liouville's theorem.

:::

## Liouville

[[T-QHIHJ]]

::: {.proof title="Liouville's theorem"}
\envlist

- Since $f$ is bounded, $\abs{f(z)} \leq M$ uniformly on $\CC$.
- Apply the estimate for the first derivative:
$$
\abs{f'(z)} \leq { 1! \norm{f}_{C_R} \over R } \leq {M \over R}\converges{R\to\infty}\too 0
,$$
  so $f'(z) = 0$ for all $z$, and $f$ is constant on the connected set $\CC$.

:::

::: {.proof title="Liouville's theorem, alternative"}

![](../../../../assets/assets/figures/2021-12-14_16-51-04.png)

:::

::: {.proof title="Liouville's theorem, using the Schwarz lemma"}
Suppose $f$ is entire and bounded.
Replacing $f$ by $(f - f(0))/(3\sup\abs f)$ when $\sup\abs f>0$, assume $f(0) = 0$ and $\abs f < 1$; the claim is $f\equiv 0$.
For $R>0$, the function $g(z) \coloneqq f(Rz)$ maps $\DD$ to $\DD$ with $g(0)=0$, so the Schwarz lemma gives $\abs{f(Rz)} \leq \abs z$ for $\abs z<1$.
For fixed $w$ and $R>\abs w$ this reads $\abs{f(w)} \leq \abs w/R$, and letting $R\to\infty$ gives $f(w)=0$.

:::

Other theorems whose conclusion is that a holomorphic function is constant are collected on [[complex-analysis/cauchy-theory/theorems-that-give-a-constant|Theorems that give a constant]].

## Exercises

[[E-FZLDN]]
[[E-BPSOU]]
[[E-4NGIV]]
[[E-EUGUZ]]
[[E-IPIKC]]
[[E-GQMTN]]
[[E-OEEU4]]
[[E-BXDQY]]
[[E-O5SOQ]]
[[E-37H2C]]
[[E-U2X4C]]
[[E-JLGWE]]
[[E-N6PDJ]]
