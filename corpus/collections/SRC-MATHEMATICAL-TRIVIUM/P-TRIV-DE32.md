---
schema: qual/card@1
id: P-TRIV-DE32
kind: problem
title: $\delta(x)$ as the limit of $\frac1\pi\operatorname{Im}\frac{1}{x-i\epsilon}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 32, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Show that $\delta ( x ) = \operatorname* { l i m } _ { \epsilon \to 0 } \operatorname { I m } \frac { 1 } { \pi } \frac { 1 } { x - i \epsilon }$
:::

The limit is understood in the sense of distributions as $\epsilon\to0^+$.

::: pf

::: pf-step

For $\epsilon>0$,
\[
\frac1\pi\operatorname{Im}\frac1{x-i\epsilon}
=\frac1\pi\frac{\epsilon}{x^2+\epsilon^2}.
\]


::: pf-proof

Rationalizing the denominator gives
\[
\frac1{x-i\epsilon}=\frac{x+i\epsilon}{x^2+\epsilon^2},
\]
whose imaginary part is $\epsilon/(x^2+\epsilon^2)$.

:::

:::

::: pf-step

For every test function $\phi\in C_c^\infty(\mathbb R)$,
\[
\lim_{\epsilon\to0^+}
\int_{-\infty}^{\infty}
\frac1\pi\frac{\epsilon}{x^2+\epsilon^2}\phi(x)\,dx
=\phi(0).
\]


::: pf-proof

Set $x=\epsilon t$. The integral becomes
\[
\frac1\pi\int_{-\infty}^{\infty}
\frac{\phi(\epsilon t)}{1+t^2}\,dt.
\]
For every fixed $t$, $\phi(\epsilon t)\to\phi(0)$. Also
\[
\left|\frac{\phi(\epsilon t)}{1+t^2}\right|
\leq\frac{\|\phi\|_\infty}{1+t^2},
\]
and the right side is integrable. Dominated convergence therefore gives
\[
\frac{\phi(0)}\pi\int_{-\infty}^{\infty}\frac{dt}{1+t^2}
=\phi(0).
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
\delta(x)=\lim_{\epsilon\to0^+}
\frac1\pi\operatorname{Im}\frac1{x-i\epsilon}}
\]
in $\mathcal D'(\mathbb R)$.


::: pf-proof

By step <1>2, the family in step <1>1 converges on every test function $\phi$ to $\phi(0)=\langle\delta,\phi\rangle$, which is precisely convergence to the Dirac distribution.

:::

:::

::: pf-qed

Step <1>3 is the asserted distributional identity.

:::

:::
