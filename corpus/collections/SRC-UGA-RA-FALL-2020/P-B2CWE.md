---
schema: qual/card@1
id: P-B2CWE
kind: problem
title: Convolution against dilates of an $L^1$ kernel is bounded on $L^1$ and converges
  to $\alpha f$
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
  - L¹
relations: []
review: draft
---

::: {.problem}
Suppose $\varphi \in L^1(\RR)$ with
$$
\int_{\RR} \varphi(x) \, dx = \alpha.
$$
For each $\delta > 0$ and $f \in L^1(\RR)$, define
$$
A_\delta f(x) = \int_{\RR} f(x-y) \delta^{-1} \varphi(\delta^{-1} y) \, dy.
$$

(a) Prove that for all $\delta > 0$,
$$
\norm{A_\delta f}_{L^1} \le \norm{\varphi}_{L^1} \norm{f}_{L^1}.
$$

(b) Prove that
$$
A_\delta f \to \alpha f \quad \text{in } L^1(\RR) \text{ as } \delta \to 0^+.
$$

*(You may use without proof the fact that for all $f \in L^1(\RR)$, $\lim_{y \to 0} \int_{\RR} \abs{f(x-y) - f(x)} \, dx = 0$.)*
:::

::: {.solution}
**Goal:** Prove the boundedness of the family of convolution operators $A_\delta$ on $L^1(\RR)$ via Tonelli's Theorem in (a), and prove $L^1$ convergence to $\alpha f$ via the Dominated Convergence Theorem on translations in (b).

::: pf

::: pf-step
Part (a): Boundedness of $A_\delta f$ in $L^1(\RR)$.

::: pf-proof

::: pf-step
Define $\varphi_\delta(y) = \delta^{-1} \varphi(\delta^{-1} y)$.

:::

::: pf-step
By the change of variables $u = \delta^{-1} y$ ($du = \delta^{-1} dy$):
$$\norm{\varphi_\delta}_{L^1} = \int_{\RR} \delta^{-1} \abs{\varphi(\delta^{-1} y)} \, dy = \int_{\RR} \abs{\varphi(u)} \, du = \norm{\varphi}_{L^1}.$$

:::

::: pf-step
Apply the integral Minkowski inequality (or Tonelli's Theorem to the non-negative product):
$$\norm{A_\delta f}_{L^1} = \int_{\RR} \abs{ \int_{\RR} f(x-y) \varphi_\delta(y) \, dy } dx \le \int_{\RR} \int_{\RR} \abs{f(x-y)} \abs{\varphi_\delta(y)} \, dy \, dx.$$

:::

::: pf-step
By Tonelli's Theorem, interchange the order of integration:
$$\int_{\RR} \int_{\RR} \abs{f(x-y)} \abs{\varphi_\delta(y)} \, dy \, dx = \int_{\RR} \abs{\varphi_\delta(y)} \left( \int_{\RR} \abs{f(x-y)} \, dx \right) dy.$$

:::

::: pf-step
By translation invariance of Lebesgue measure, $\int_{\RR} \abs{f(x-y)} \, dx = \norm{f}_{L^1}$ for every $y \in \RR$.

:::

::: pf-step
Thus:
$$\norm{A_\delta f}_{L^1} \le \norm{f}_{L^1} \int_{\RR} \abs{\varphi_\delta(y)} \, dy = \norm{f}_{L^1} \norm{\varphi_\delta}_{L^1} = \norm{\varphi}_{L^1} \norm{f}_{L^1}.$$

:::

:::

:::

::: pf-step
Part (b): Representation of the error $A_\delta f(x) - \alpha f(x)$.

::: pf-proof

::: pf-step
By change of variables, $\int_{\RR} \varphi_\delta(y) \, dy = \int_{\RR} \delta^{-1} \varphi(\delta^{-1} y) \, dy = \int_{\RR} \varphi(u) \, du = \alpha$.

:::

::: pf-step
Multiply this identity by $f(x)$:
$$\alpha f(x) = \int_{\RR} f(x) \varphi_\delta(y) \, dy.$$

:::

::: pf-step
Subtract this from $A_\delta f(x)$:
$$A_\delta f(x) - \alpha f(x) = \int_{\RR} (f(x-y) - f(x)) \delta^{-1} \varphi(\delta^{-1} y) \, dy.$$

:::

::: pf-step
Substitute $y = \delta z$ ($dy = \delta dz$):
$$A_\delta f(x) - \alpha f(x) = \int_{\RR} (f(x - \delta z) - f(x)) \varphi(z) \, dz.$$

:::

:::

:::

::: pf-step
Part (b): $L^1$ norm estimate and Dominated Convergence Theorem.

::: pf-proof

::: pf-step
Take the $L^1$ norm:
$$\norm{A_\delta f - \alpha f}_{L^1} = \int_{\RR} \abs{ \int_{\RR} (f(x - \delta z) - f(x)) \varphi(z) \, dz } dx \le \int_{\RR} \int_{\RR} \abs{f(x - \delta z) - f(x)} \abs{\varphi(z)} \, dz \, dx.$$

:::

::: pf-step
By Tonelli's Theorem, interchange the order of integration:
$$\norm{A_\delta f - \alpha f}_{L^1} \le \int_{\RR} \abs{\varphi(z)} \left( \int_{\RR} \abs{f(x - \delta z) - f(x)} \, dx \right) dz = \int_{\RR} \abs{\varphi(z)} \norm{\tau_{\delta z} f - f}_{L^1} \, dz,$$
where $\tau_h f(x) = f(x - h)$.

:::

::: pf-step
Pointwise convergence:

- For each fixed $z \in \RR$, as $\delta \to 0^+$, the shift $h = \delta z \to 0$.
- By $L^1$-continuity of translations:
$$\lim_{\delta \to 0^+} \norm{\tau_{\delta z} f - f}_{L^1} = 0 \implies \lim_{\delta \to 0^+} \abs{\varphi(z)} \norm{\tau_{\delta z} f - f}_{L^1} = 0.$$

:::

::: pf-step
Domination:

- By the triangle inequality, $\norm{\tau_{\delta z} f - f}_{L^1} \le \norm{\tau_{\delta z} f}_{L^1} + \norm{f}_{L^1} = 2 \norm{f}_{L^1}$.
- Thus for all $\delta > 0$ and all $z \in \RR$:
$$\abs{\varphi(z)} \norm{\tau_{\delta z} f - f}_{L^1} \le 2 \norm{f}_{L^1} \abs{\varphi(z)} =: g(z).$$
- Since $\varphi \in L^1(\RR)$, $g \in L^1(\RR)$.

:::

::: pf-step
By the Dominated Convergence Theorem:
$$\lim_{\delta \to 0^+} \norm{A_\delta f - \alpha f}_{L^1} \le \int_{\RR} \lim_{\delta \to 0^+} \left( \abs{\varphi(z)} \norm{\tau_{\delta z} f - f}_{L^1} \right) dz = \int_{\RR} 0 \, dz = 0.$$

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$\norm{A_\delta f}_{L^1} \le \norm{\varphi}_{L^1} \norm{f}_{L^1}$ and $\lim_{\delta \to 0^+} \norm{A_\delta f - \alpha f}_{L^1} = 0$.
:::

:::

:::

:::

