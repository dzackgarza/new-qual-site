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

(a) ${ \frac { d } { d x } } \left( x ^ { \nu } J _ { \nu } ( x ) \right) = x ^ { \nu } J _ { \nu - 1 } ( x )$

(b) ${ \frac { d } { d x } } \left( x ^ { - \nu } J _ { \nu } ( x ) \right) = - x ^ { - \nu } J _ { \nu + 1 } ( x )$

(c) $\frac { d } { d x } J _ { \nu } ( x ) = \frac { 1 } { 2 } \left( J _ { \nu - 1 } ( x ) - J _ { \nu + 1 } ( x ) \right)$

(d) $J _ { \nu - 1 } ( x ) + J _ { \nu + 1 } ( x ) = \frac { 2 \nu } { x } J _ { \nu } ( x )$
:::

Use the series
\[
J_\nu(x)=\sum_{k=0}^{\infty}
\frac{(-1)^k}{k!\,\Gamma(k+\nu+1)}
\left(\frac x2\right)^{2k+\nu}.
\]

::: pf

::: pf-step

One has
\[
\boxed{\frac d{dx}\left(x^\nu J_\nu(x)\right)=x^\nu J_{\nu-1}(x)}.
\]


::: pf-proof

Multiplying the defining series by $x^\nu$ and differentiating termwise gives
\[
\sum_{k=0}^{\infty}
\frac{(-1)^k(2k+2\nu)x^{2k+2\nu-1}}
{2^{2k+\nu}k!\,\Gamma(k+\nu+1)}.
\]
Using $\Gamma(k+\nu+1)=(k+\nu)\Gamma(k+\nu)$ reduces this to
\[
x^\nu\sum_{k=0}^{\infty}
\frac{(-1)^k}{k!\,\Gamma(k+\nu)}
\left(\frac x2\right)^{2k+\nu-1}
=x^\nu J_{\nu-1}(x).
\]

:::

:::

::: pf-step

One has
\[
\boxed{\frac d{dx}\left(x^{-\nu}J_\nu(x)\right)=-x^{-\nu}J_{\nu+1}(x)}.
\]


::: pf-proof

After multiplying the series by $x^{-\nu}$, termwise differentiation annihilates the $k=0$ term and gives
\[
\sum_{k=1}^{\infty}
\frac{(-1)^k(2k)x^{2k-1}}
{2^{2k+\nu}k!\,\Gamma(k+\nu+1)}.
\]
Set $j=k-1$. Since $k!=k j!$, this becomes
\[
-x^{-\nu}\sum_{j=0}^{\infty}
\frac{(-1)^j}{j!\,\Gamma(j+\nu+2)}
\left(\frac x2\right)^{2j+\nu+1}
=-x^{-\nu}J_{\nu+1}(x).
\]

:::

:::

::: pf-step

Expanding step <1>1 by the product rule gives
\[
J_\nu'(x)+\frac\nu xJ_\nu(x)=J_{\nu-1}(x).
\]


::: pf-proof

Divide the identity in step <1>1 by $x^\nu$ after applying the product rule to its left side.

:::

:::

::: pf-step

Expanding step <1>2 by the product rule gives
\[
J_\nu'(x)-\frac\nu xJ_\nu(x)=-J_{\nu+1}(x).
\]


::: pf-proof

Divide the identity in step <1>2 by $x^{-\nu}$ after applying the product rule.

:::

:::

::: pf-step

Subtracting step <1>4 from step <1>3 gives
\[
\boxed{J_{\nu-1}(x)+J_{\nu+1}(x)=\frac{2\nu}{x}J_\nu(x)}.
\]


::: pf-proof

The $J_\nu'$ terms cancel, leaving $2\nu J_\nu/x$ on one side and $J_{\nu-1}+J_{\nu+1}$ on the other.

:::

:::

::: pf-step

Adding steps <1>3 and <1>4 gives
\[
\boxed{J_\nu'(x)=\frac12\left(J_{\nu-1}(x)-J_{\nu+1}(x)\right)}.
\]


::: pf-proof

The terms $\nu J_\nu/x$ cancel. Dividing the resulting identity by $2$ gives the formula.

:::

:::

::: pf-qed

Steps <1>1--<1>2 prove parts (a)--(b), step <1>6 proves part (c), and step <1>5 proves part (d).

:::

:::
