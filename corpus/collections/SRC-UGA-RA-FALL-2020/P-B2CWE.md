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
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card carried no audit list; this one records the change. Fifteen steps asserted their claim with
    no justification and each now carries one: the dilation's $L^1$ norm by change of variables, the
    absolute-value-of-an-integral estimate and Tonelli interchange that give the operator bound, the
    translation invariance that evaluates the inner integral, the representation of the error after
    $y = \delta z$, and in part (b) the measurability, pointwise convergence, domination by
    $2\norm{f}_{L^1}\abs{\varphi}$ and dominated convergence that send the error to zero. Checked while
    writing: the domination constant must not depend on $\delta$, which the triangle inequality supplies,
    and the final limit is read as a bound on the $L^1$ norm of the error, not as an equality of
    integrals. One repair: the closing step had "Conclusion:" as its claim and now states the two
    conclusions. No page reference appears on the card. The statement is unchanged. The collection
    retains the UGA real analysis qualifying exam of Fall 2020 and no solution sheet, so the argument is
    the card's own.
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
$\norm{A_\delta f}_{L^1} \le \norm{\varphi}_{L^1}\norm{f}_{L^1}$ for every $\delta > 0$.

::: pf-proof

::: pf-step
Define $\varphi_\delta(y) = \delta^{-1} \varphi(\delta^{-1} y)$.


::: pf-proof
For each $\delta > 0$ the formula is a scalar multiple of the composition of the measurable $\varphi$ with the dilation $y \mapsto \delta^{-1}y$, so it defines a measurable function on $\RR$; this is the dilated kernel used throughout.
:::

:::

::: pf-step
By the change of variables $u = \delta^{-1} y$ ($du = \delta^{-1} dy$):
$$\norm{\varphi_\delta}_{L^1} = \int_{\RR} \delta^{-1} \abs{\varphi(\delta^{-1} y)} \, dy = \int_{\RR} \abs{\varphi(u)} \, du = \norm{\varphi}_{L^1}.$$


::: pf-proof
The substitution $u = \delta^{-1}y$ is a linear change of variables with $dy = \delta\,du$, so $\int \delta^{-1}\abs{\varphi(\delta^{-1}y)}\,dy = \int\abs{\varphi(u)}\,du$; the left side is $\norm{\varphi_\delta}_{L^1}$ and the right side is $\norm{\varphi}_{L^1}$.
:::

:::

::: pf-step
Apply the integral Minkowski inequality (or Tonelli's Theorem to the non-negative product):
$$\norm{A_\delta f}_{L^1} = \int_{\RR} \abs{ \int_{\RR} f(x-y) \varphi_\delta(y) \, dy } dx \le \int_{\RR} \int_{\RR} \abs{f(x-y)} \abs{\varphi_\delta(y)} \, dy \, dx.$$


::: pf-proof
The absolute value of an integral is at most the integral of the absolute value, applied pointwise in $x$ to the inner integral, and the $L^1$ norm of $A_\delta f$ is the integral over $x$ of that absolute value; the integrand is measurable as a product of measurable functions.
:::

:::

::: pf-step
By Tonelli's Theorem, interchange the order of integration:
$$\int_{\RR} \int_{\RR} \abs{f(x-y)} \abs{\varphi_\delta(y)} \, dy \, dx = \int_{\RR} \abs{\varphi_\delta(y)} \left( \int_{\RR} \abs{f(x-y)} \, dx \right) dy.$$


::: pf-proof
The integrand $\abs{f(x-y)}\abs{\varphi_\delta(y)}$ is nonnegative and measurable on $\RR^2$, so Tonelli's theorem permits the interchange of the two integrations.
:::

:::

::: pf-step
By translation invariance of Lebesgue measure, $\int_{\RR} \abs{f(x-y)} \, dx = \norm{f}_{L^1}$ for every $y \in \RR$.


::: pf-proof
Lebesgue measure is translation invariant, so $x \mapsto x + y$ is measure preserving and $\int\abs{f(x-y)}\,dx = \int\abs{f(x)}\,dx = \norm{f}_{L^1}$, independently of $y$.
:::

:::

::: pf-step
Thus:
$$\norm{A_\delta f}_{L^1} \le \norm{f}_{L^1} \int_{\RR} \abs{\varphi_\delta(y)} \, dy = \norm{f}_{L^1} \norm{\varphi_\delta}_{L^1} = \norm{\varphi}_{L^1} \norm{f}_{L^1}.$$


::: pf-proof
Substituting the translation invariance into the double integral leaves $\norm{f}_{L^1}\int\abs{\varphi_\delta(y)}\,dy = \norm{f}_{L^1}\norm{\varphi_\delta}_{L^1}$, and that equals $\norm{f}_{L^1}\norm{\varphi}_{L^1}$ by the change of variables above.
:::

:::

:::

:::

::: pf-step
$A_\delta f(x) - \alpha f(x) = \int_{\RR} (f(x - \delta z) - f(x))\varphi(z)\,dz$ for every $x$ and every $\delta > 0$.

::: pf-proof

::: pf-step
By change of variables, $\int_{\RR} \varphi_\delta(y) \, dy = \int_{\RR} \delta^{-1} \varphi(\delta^{-1} y) \, dy = \int_{\RR} \varphi(u) \, du = \alpha$.


::: pf-proof
The substitution $u = \delta^{-1}y$ gives $\int\delta^{-1}\varphi(\delta^{-1}y)\,dy = \int\varphi(u)\,du = \alpha$, which is the hypothesis on $\varphi$.
:::

:::

::: pf-step
Multiply this identity by $f(x)$:
$$\alpha f(x) = \int_{\RR} f(x) \varphi_\delta(y) \, dy.$$


::: pf-proof
The number $f(x)$ does not depend on $y$, so it factors out of the integral: $\int f(x)\varphi_\delta(y)\,dy = f(x)\int\varphi_\delta(y)\,dy = \alpha f(x)$.
:::

:::

::: pf-step
Subtract this from $A_\delta f(x)$:
$$A_\delta f(x) - \alpha f(x) = \int_{\RR} (f(x-y) - f(x)) \delta^{-1} \varphi(\delta^{-1} y) \, dy.$$


::: pf-proof
Both terms are integrals over the same variable $y$ of integrable functions, and the difference of two such integrals is the integral of the difference by linearity.
:::

:::

::: pf-step
Substitute $y = \delta z$ ($dy = \delta dz$):
$$A_\delta f(x) - \alpha f(x) = \int_{\RR} (f(x - \delta z) - f(x)) \varphi(z) \, dz.$$


::: pf-proof
With $y = \delta z$ one has $dy = \delta\,dz$ and $\delta^{-1}\varphi(\delta^{-1}y)\delta = \varphi(z)$, so the integrand becomes $(f(x-\delta z) - f(x))\varphi(z)$ and the limits are unchanged.
:::

:::

:::

:::

::: pf-step
$\norm{A_\delta f - \alpha f}_{L^1} \to 0$ as $\delta \to 0^+$.

::: pf-proof

::: pf-step
Take the $L^1$ norm:
$$\norm{A_\delta f - \alpha f}_{L^1} = \int_{\RR} \abs{ \int_{\RR} (f(x - \delta z) - f(x)) \varphi(z) \, dz } dx \le \int_{\RR} \int_{\RR} \abs{f(x - \delta z) - f(x)} \abs{\varphi(z)} \, dz \, dx.$$


::: pf-proof
The absolute value of the inner integral is at most the integral of the absolute value, and the $L^1$ norm is the integral over $x$ of that absolute value, which gives the displayed bound.
:::

:::

::: pf-step
By Tonelli's Theorem, interchange the order of integration:
$$\norm{A_\delta f - \alpha f}_{L^1} \le \int_{\RR} \abs{\varphi(z)} \left( \int_{\RR} \abs{f(x - \delta z) - f(x)} \, dx \right) dz = \int_{\RR} \abs{\varphi(z)} \norm{\tau_{\delta z} f - f}_{L^1} \, dz,$$
where $\tau_h f(x) = f(x - h)$.


::: pf-proof
The integrand $\abs{f(x-\delta z) - f(x)}\abs{\varphi(z)}$ is nonnegative and measurable, so Tonelli permits the interchange; the inner integral over $x$ is by definition $\norm{\tau_{\delta z}f - f}_{L^1}$, where $\tau_h f(x) = f(x-h)$.
:::

:::

::: pf-step
Pointwise convergence:

- For each fixed $z \in \RR$, as $\delta \to 0^+$, the shift $h = \delta z \to 0$.
- By $L^1$-continuity of translations:
$$\lim_{\delta \to 0^+} \norm{\tau_{\delta z} f - f}_{L^1} = 0 \implies \lim_{\delta \to 0^+} \abs{\varphi(z)} \norm{\tau_{\delta z} f - f}_{L^1} = 0.$$


::: pf-proof
For fixed $z$ the shift $h = \delta z$ tends to $0$ as $\delta \to 0^+$, and continuity of translations in $L^1$ gives $\norm{\tau_h f - f}_{L^1} \to 0$ as $h \to 0$; composing with $h = \delta z$ gives the limit $0$, and multiplying by the fixed number $\abs{\varphi(z)}$ leaves it $0$.
:::

:::

::: pf-step
Domination:

- By the triangle inequality, $\norm{\tau_{\delta z} f - f}_{L^1} \le \norm{\tau_{\delta z} f}_{L^1} + \norm{f}_{L^1} = 2 \norm{f}_{L^1}$.
- Thus for all $\delta > 0$ and all $z \in \RR$:
$$\abs{\varphi(z)} \norm{\tau_{\delta z} f - f}_{L^1} \le 2 \norm{f}_{L^1} \abs{\varphi(z)} =: g(z).$$
- Since $\varphi \in L^1(\RR)$, $g \in L^1(\RR)$.


::: pf-proof
The triangle inequality gives $\norm{\tau_{\delta z}f - f}_{L^1} \le \norm{\tau_{\delta z}f}_{L^1} + \norm{f}_{L^1} = 2\norm{f}_{L^1}$, the equality being translation invariance; multiplying by the fixed factor $\abs{\varphi(z)}$ gives the displayed bound, and $2\norm{f}_{L^1}\abs{\varphi}$ is integrable because $\varphi$ is.
:::

:::

::: pf-step
By the Dominated Convergence Theorem:
$$\lim_{\delta \to 0^+} \norm{A_\delta f - \alpha f}_{L^1} \le \int_{\RR} \lim_{\delta \to 0^+} \left( \abs{\varphi(z)} \norm{\tau_{\delta z} f - f}_{L^1} \right) dz = \int_{\RR} 0 \, dz = 0.$$


::: pf-proof
The functions $z \mapsto \abs{\varphi(z)}\norm{\tau_{\delta z}f - f}_{L^1}$ are measurable, converge pointwise to $0$ by the previous step and are dominated by the integrable $g$; dominated convergence gives that their integrals tend to $\int 0 = 0$, and the $L^1$ norm of the error is bounded by those integrals, so it tends to $0$ too.
:::

:::

:::

:::

::: pf-step
$\norm{A_\delta f}_{L^1} \le \norm{\varphi}_{L^1}\norm{f}_{L^1}$ for every $\delta > 0$, and $\norm{A_\delta f - \alpha f}_{L^1} \to 0$ as $\delta \to 0^+$.

::: pf-proof
$\norm{A_\delta f}_{L^1} \le \norm{\varphi}_{L^1} \norm{f}_{L^1}$ and $\lim_{\delta \to 0^+} \norm{A_\delta f - \alpha f}_{L^1} = 0$.
:::

:::

:::

:::

