---
schema: qual/card@1
id: P-TRIV-DE38
kind: problem
title: Distributional derivative of $\log x$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 38, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains a leading nonprinting control byte at this source position; the byte was removed from the authored card as a nonsemantic extraction artifact.
---

::: {.problem}
Show that ${ \frac { d } { d x } } \log x = { \frac { 1 } { x } } - i \pi \delta ( x )$
:::

::: {.solution}

Interpret $\log x$ as the boundary value $\log(x+i0)$ of the principal complex logarithm. Then
$$
\log(x+i0)=\log\abs{x}+i\pi H(-x),
$$
where $H$ is the Heaviside function.

::: pf

::: {.pf-step #s1-1}

Distributionally,
$$
\frac d{dx}\log\abs{x}=\operatorname{pv}\frac1x.
$$


::: pf-proof

For a test function $\phi$,
$$
\left\langle\frac d{dx}\log\abs{x},\phi\right\rangle
=-\int_{-\infty}^{\infty}\log\abs{x}\,\phi'(x)\,dx.
$$
Integrating by parts separately on $(-\infty,-\epsilon)$ and $(\epsilon,\infty)$ gives
$$
\int_{\abs{x}>\epsilon}\frac{\phi(x)}x\,dx
+\log\epsilon\bigl(\phi(-\epsilon)-\phi(\epsilon)\bigr).
$$
The last term tends to zero because $\phi(-\epsilon)-\phi(\epsilon)=O(\epsilon)$, while the first tends by definition to $\langle\operatorname{pv}(1/x),\phi\rangle$.

:::

:::

::: {.pf-step #s1-2}

Distributionally,
$$
\frac d{dx}H(-x)=-\delta(x).
$$


::: pf-proof

For every test function $\phi$,
$$
\left\langle\frac d{dx}H(-x),\phi\right\rangle
=-\int_{-\infty}^{0}\phi'(x)\,dx
=-\phi(0)
=\langle-\delta,\phi\rangle.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\frac d{dx}\log(x+i0)
=\operatorname{pv}\frac1x-i\pi\delta(x)}.
$$


::: pf-proof

Differentiate the boundary-value decomposition preceding step [](#s1-1){.pf-ref} and apply steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}:
$$
\frac d{dx}\bigl(\log\abs{x}+i\pi H(-x)\bigr)
=\operatorname{pv}\frac1x-i\pi\delta(x).
$$

:::

:::

::: {.pf-step #s1-4}

This is the source's identity when its symbol $1/x$ is understood as the principal-value distribution.


::: pf-proof

The ordinary function $1/x$ is not locally integrable at the origin and therefore does not itself define the distribution required by the formula. Step [](#s1-3){.pf-ref} supplies the precise distributional meaning.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} establish the stated identity with its necessary boundary-value and principal-value interpretations.

:::

:::

:::
