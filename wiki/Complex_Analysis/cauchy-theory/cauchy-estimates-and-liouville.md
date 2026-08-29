---
title: Cauchy estimates and Liouville
order: 30
---

# Cauchy estimates and Liouville

## The estimates

[[T-22RQZ]]

[[FT-5MASA]] [[FT-REHJT]]

[[FF-HO7RN]]

:::{.slogan}
The $n$th Taylor coefficient of an analytic function is at most $\sup_{\abs z = R} \abs{f}/R^n$:
\[
\abs{c_k} \asymptotic {\norm{f}_\infty \over R^k}
.\]

:::

:::{.proof title="of Cauchy's inequality"}
\envlist

- Given $z_0\in \Omega$, pick the largest disc $D_R(z_0) \subset \Omega$ and let $C = \bd D_R$.
- Apply the integral formula:

\[
\left|f^{(n)}(z_0)\right|
&= \abs{ \frac{n !}{2 \pi i} \int_{C} \frac{f(\zeta) }{(\zeta-z_0)^{n+1}} \dzeta } \\
&=\left|\frac{n !}{2 \pi i} \int_{0}^{2 \pi} \frac{f\left(z_0 + r e^{i \theta}\right) r i e^{i \theta} }{\left(r e^{i \theta}\right)^{n+1}} \dtheta \right| \\
&\leq \frac{n !}{2 \pi} \int_{0}^{2 \pi}\left|\frac{f\left( z_0 +r e^{i \theta}\right) r i e^{i \theta}}{\left(r e^{i \theta}\right)^{n+1}}\right| \dtheta \\
&=\frac{n !}{2 \pi} \int_{0}^{2 \pi} \frac{\left|f\left(z_0 +r e^{i \theta}\right)\right|}{r^{n}} \dtheta \\
&\leq \frac{n !}{2 \pi} \int_{0}^{2 \pi} \frac{M}{r^{n}} \dtheta \\
&=\frac{M n !}{r^{n}}
.\]

:::

:::{.remark title="The only moving part is $R$"}
Every use of this estimate is the same move: bound $\norm{f}_{C_R}$ in terms of $R$, then send $R\to\infty$ and see which derivatives are forced to vanish.
A uniform bound kills $f'$, which is Liouville.
A bound $\bigo(R^n)$ kills $f^{(n+1)}$, which makes $f$ a polynomial of degree at most $n$.
Nothing else changes between those arguments.

:::

## Liouville

[[T-QHIHJ]]

:::{.proof title="of Liouville"}
\envlist

- Since $f$ is bounded, $\abs{f(z)} \leq M$ uniformly on $\CC$.
- Apply the estimate for the first derivative:
\[
\abs{f'(z)} \leq { 1! \norm{f}_{C_R} \over R } \leq {M \over R}\converges{R\to\infty}\too 0
,\]
  so $f'(z) = 0$ for all $z$, and $f$ is constant on the connected set $\CC$.

:::

:::{.proof title="of Liouville, alternative"}

![](../../../../assets/assets/figures/2021-12-14_16-51-04.png)

:::

:::{.proof title="of Liouville, using Schwarz"}
Suppose $f$ is entire and bounded.
After an affine change of variables in domain and range, $f(0) = 0$ and $\abs f \leq 1$, and the claim is $f\equiv 0$.
The function $g(z) \da f(Rz)$ satisfies the hypotheses of the Schwarz lemma, so $\abs{f(Rz)} \leq \abs z$, giving $\abs{f(w)} \leq \abs w/R \convergesto{R\to\infty} 0$.

:::

Which problems these close, and what else closes them, is [[Complex_Analysis/cauchy-theory/theorems-that-give-a-constant|Theorems that give a constant]].

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
