---
schema: qual/card@1
id: P-ZCE6E
kind: problem
title: The subgraph of a nonnegative function is measurable if and only if the function
  is, and $m(\mathcal{A})=\int_{\RR^n}f=\int_0^\infty m(\{f\ge t\})\,dt$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
  - Fubini-Tonelli
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2019 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2019.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f\colon\RR^n\to[0,\infty]$ and define
$$
\mathcal A\coloneqq\theset{(x,t)\in\RR^n\times\RR \suchthat 0\le t\le f(x)}.
$$

1. Prove that $f$ is Lebesgue measurable if and only if $\mathcal A$ is Lebesgue measurable in $\RR^{n+1}$.

2. If $f$ is measurable, prove
$$
m_{n+1}(\mathcal A)
=\int_{\RR^n}f(x)\,dx
=\int_0^\infty m_n(\theset{x \suchthat f(x)\ge t})\,dt.
$$
:::

::: {.solution}

::: pf

::: pf-step
(1) $f$ is measurable if and only if $\mathcal A$ is measurable.

::: pf-proof

::: pf-step
If $f$ is measurable, then $\mathcal A$ is measurable.

::: pf-proof
The map $(x,t)\mapsto f(x)$ is measurable on $\RR^{n+1}$, since the preimage of a Borel set $B$ is $f^{-1}(B)\times\RR$, and $(x,t)\mapsto t$ is continuous.
Hence $H(x,t)\coloneqq f(x)-t$, with values in $(-\infty,\infty]$, is measurable, and
$$
\mathcal A
=(\RR^n\times[0,\infty))\cap H^{-1}([0,\infty])
$$
is Lebesgue measurable.
:::

:::

::: {.pf-step #a-measurable-implies-f-measurable}
If $\mathcal A$ is measurable, then $f$ is measurable.

::: pf-proof
For every $x\in\RR^n$, the vertical section is
$$
\mathcal A_x
\coloneqq\theset{t \suchthat (x,t)\in\mathcal A}
=[0,f(x)]\cap\RR,
$$
so
$$
f(x)=m_1(\mathcal A_x)
=\int_{\RR}\mathbf1_{\mathcal A}(x,t)\,dt.
$$
Since $\mathbf1_{\mathcal A}$ is a nonnegative measurable function on $\RR^{n+1}=\RR^n\times\RR$, Tonelli's theorem for Lebesgue measure implies that $x\mapsto \int_{\RR}\mathbf1_{\mathcal A}(x,t)\,dt$ is measurable.
Thus $f$ is measurable.
:::

:::

:::

:::

::: pf-step
(2) If $f$ is measurable, then $\boxed{m_{n+1}(\mathcal A)=\int_{\RR^n}f(x)\,dx=\int_0^\infty m_n(\theset{x \suchthat f(x)\ge t})\,dt.}$

::: pf-proof

By (1), $\mathcal A$ is measurable, so Tonelli's theorem applies to $\mathbf1_{\mathcal A}$ in either order.

::: pf-step
$m_{n+1}(\mathcal A)=\int_{\RR^n}f(x)\,dx$.

::: pf-proof
Integrating first in $t$ and using the sections computed in step [](#a-measurable-implies-f-measurable){.pf-ref},
$$
m_{n+1}(\mathcal A)
=\int_{\RR^n}\qty(\int_{\RR}\mathbf1_{\mathcal A}(x,t)\,dt)dx
=\int_{\RR^n}f(x)\,dx.
$$
:::

:::

::: pf-step
$m_{n+1}(\mathcal A)=\int_0^\infty m_n(\theset{x \suchthat f(x)\ge t})\,dt$.

::: pf-proof
For $t\ge0$, the horizontal section is
$$
\mathcal A^t
\coloneqq\theset{x \suchthat (x,t)\in\mathcal A}
=\theset{x \suchthat f(x)\ge t},
$$
and for $t<0$ it is empty.
Integrating first in $x$,
$$
m_{n+1}(\mathcal A)
=\int_0^\infty\qty(\int_{\RR^n}\mathbf1_{\mathcal A}(x,t)\,dx)dt
=\int_0^\infty m_n(\theset{x \suchthat f(x)\ge t})\,dt.
$$
:::

:::

:::

:::

:::

:::
