---
schema: qual/card@1
id: P-TRIV-DE25
kind: problem
title: Recurrence relations for Bessel functions of the first kind
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 25, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Prove the following properties of the Bessel functions of the first kind:

(a) $\frac{d}{dx}\left( x^\nu J_\nu(x) \right) = x^\nu J_{\nu-1}(x)$

(b) $\frac{d}{dx}\left( x^{-\nu} J_\nu(x) \right) = -x^{-\nu} J_{\nu+1}(x)$

(c) $\frac{d}{dx} J_\nu(x) = \frac{1}{2}\left( J_{\nu-1}(x) - J_{\nu+1}(x) \right)$

(d) $J_{\nu-1}(x) + J_{\nu+1}(x) = \frac{2\nu}{x} J_\nu(x)$
:::

::: {.solution}

Use the series
$$
J_\nu(x)=\sum_{k=0}^{\infty}
\frac{(-1)^k}{k!\,\Gamma(k+\nu+1)}
\left(\frac x2\right)^{2k+\nu}.
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
\boxed{\frac d{dx}\left(x^\nu J_\nu(x)\right)=x^\nu J_{\nu-1}(x)}.
$$


::: pf-proof

Multiplying the defining series by $x^\nu$ and differentiating termwise gives
$$
\sum_{k=0}^{\infty}
\frac{(-1)^k(2k+2\nu)x^{2k+2\nu-1}}
{2^{2k+\nu}k!\,\Gamma(k+\nu+1)}.
$$
Using $\Gamma(k+\nu+1)=(k+\nu)\Gamma(k+\nu)$ reduces this to
$$
x^\nu\sum_{k=0}^{\infty}
\frac{(-1)^k}{k!\,\Gamma(k+\nu)}
\left(\frac x2\right)^{2k+\nu-1}
=x^\nu J_{\nu-1}(x).
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
\boxed{\frac d{dx}\left(x^{-\nu}J_\nu(x)\right)=-x^{-\nu}J_{\nu+1}(x)}.
$$


::: pf-proof

After multiplying the series by $x^{-\nu}$, termwise differentiation annihilates the $k=0$ term and gives
$$
\sum_{k=1}^{\infty}
\frac{(-1)^k(2k)x^{2k-1}}
{2^{2k+\nu}k!\,\Gamma(k+\nu+1)}.
$$
Set $j=k-1$. Since $k!=k j!$, this becomes
$$
-x^{-\nu}\sum_{j=0}^{\infty}
\frac{(-1)^j}{j!\,\Gamma(j+\nu+2)}
\left(\frac x2\right)^{2j+\nu+1}
=-x^{-\nu}J_{\nu+1}(x).
$$

:::

:::

::: {.pf-step #s1-3}

Expanding step [](#s1-1){.pf-ref} by the product rule gives
$$
J_\nu'(x)+\frac\nu xJ_\nu(x)=J_{\nu-1}(x).
$$


::: pf-proof

Divide the identity in step [](#s1-1){.pf-ref} by $x^\nu$ after applying the product rule to its left side.

:::

:::

::: {.pf-step #s1-4}

Expanding step [](#s1-2){.pf-ref} by the product rule gives
$$
J_\nu'(x)-\frac\nu xJ_\nu(x)=-J_{\nu+1}(x).
$$


::: pf-proof

Divide the identity in step [](#s1-2){.pf-ref} by $x^{-\nu}$ after applying the product rule.

:::

:::

::: {.pf-step #s1-5}

Subtracting step [](#s1-4){.pf-ref} from step [](#s1-3){.pf-ref} gives
$$
\boxed{J_{\nu-1}(x)+J_{\nu+1}(x)=\frac{2\nu}{x}J_\nu(x)}.
$$


::: pf-proof

The $J_\nu'$ terms cancel, leaving $2\nu J_\nu/x$ on one side and $J_{\nu-1}+J_{\nu+1}$ on the other.

:::

:::

::: {.pf-step #s1-6}

Adding steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} gives
$$
\boxed{J_\nu'(x)=\frac12\left(J_{\nu-1}(x)-J_{\nu+1}(x)\right)}.
$$


::: pf-proof

The terms $\nu J_\nu/x$ cancel. Dividing the resulting identity by $2$ gives the formula.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} prove parts (a)--(b), step [](#s1-6){.pf-ref} proves part (c), and step [](#s1-5){.pf-ref} proves part (d).

:::

:::

:::
