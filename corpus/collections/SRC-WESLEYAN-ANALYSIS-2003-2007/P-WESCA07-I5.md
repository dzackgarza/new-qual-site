---
schema: qual/card@1
id: P-WESCA07-I5
kind: problem
title: "Bound a contour integral along $\\gamma(t)=te^{it}$"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Section I, item 5 (Summer 2007) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let
$$
\gamma(t)=te^{it},\qquad 0\le t\le\pi.
$$
Show that
$$
\abs{\int_\gamma z\,dz}
\le \frac{\pi^2}{2}+\frac{\pi^3}{3}.
$$
:::

::: {.solution}

::: pf

::: pf-step

The derivative of the path is
$$
\gamma'(t)=e^{it}(1+it).
$$


::: pf-proof

Differentiate
$$
\gamma(t)=te^{it}
$$
using the product rule.

:::

:::

::: {.pf-step #s1-2}

For $0\le t\le\pi$,
$$
\abs{\gamma(t)}=t
\qquad\text{and}\qquad
\abs{\gamma'(t)}\le1+t.
$$


::: pf-proof

Since $\abs{e^{it}}=1$,
$$
\abs{\gamma(t)}=t.
$$
Also
$$
\abs{\gamma'(t)}=\abs{1+it}=\sqrt{1+t^2}\le1+t.
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
\abs{\int_\gamma z\,dz}
\le
\int_0^\pi t(1+t)\,dt.
$$


::: pf-proof

By the definition of a contour integral,
$$
\int_\gamma z\,dz
=\int_0^\pi \gamma(t)\gamma'(t)\,dt.
$$
Therefore, by the triangle inequality and step [](#s1-2){.pf-ref},
$$
\abs{\int_\gamma z\,dz}
\le
\int_0^\pi \abs{\gamma(t)}\,\abs{\gamma'(t)}\,dt
\le
\int_0^\pi t(1+t)\,dt.
$$

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{
\abs{\int_\gamma z\,dz}
\le \frac{\pi^2}{2}+\frac{\pi^3}{3}.}
$$


::: pf-proof

Evaluate the elementary integral from step [](#s1-3){.pf-ref}:
$$
\int_0^\pi t(1+t)\,dt
=\int_0^\pi t\,dt+\int_0^\pi t^2\,dt
=\frac{\pi^2}{2}+\frac{\pi^3}{3}.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required estimate.

:::

:::

:::
