---
schema: qual/card@1
id: P-BKS16-1B
kind: problem
title: $\int_0^\infty te^{-t/2}/(1-e^{-t})\,dt$ as a sum over odd squares
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Checked the statement against Problem 1B in the vendored Berkeley Spring 2016 exam and independently reviewed the supplied solution.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the geometric-series expansion, Tonelli interchange, and the Laplace integral by integration by parts.
---

::: {.problem}
Show that
$$
\int_0^\infty \frac{t e^{-t/2}}{1-e^{-t}}\,dt
=4\sum_{n=0}^\infty \frac{1}{(2n+1)^2}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $t>0$,
$$
\frac{e^{-t/2}}{1-e^{-t}}
=
\sum_{n=0}^{\infty}e^{-(n+1/2)t}.
$$


::: pf-proof

Since $0<e^{-t}<1$, the geometric-series identity gives
$$
\frac{1}{1-e^{-t}}
=
\sum_{n=0}^{\infty}e^{-nt}.
$$
Multiplying by $e^{-t/2}$ yields the displayed expansion.

:::

:::

::: {.pf-step #s1-2}

For every $\alpha>0$,
$$
\int_0^\infty t e^{-\alpha t}\,dt
=
\frac{1}{\alpha^2}.
$$


::: pf-proof

For $R>0$, integration by parts gives
$$
\begin{aligned}
\int_0^R t e^{-\alpha t}\,dt
&=
\left[-\frac{t}{\alpha}e^{-\alpha t}\right]_0^R
+
\frac1\alpha\int_0^R e^{-\alpha t}\,dt\\
&=
-\frac{R}{\alpha}e^{-\alpha R}
+
\frac{1-e^{-\alpha R}}{\alpha^2}.
\end{aligned}
$$
As $R\to\infty$, both $e^{-\alpha R}$ and $R e^{-\alpha R}$ tend to $0$, proving the formula.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\int_0^\infty \frac{t e^{-t/2}}{1-e^{-t}}\,dt
=
\boxed{4\sum_{n=0}^\infty \frac{1}{(2n+1)^2}}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the integrand is the pointwise sum of the nonnegative functions
$$
t\longmapsto t e^{-(n+1/2)t}.
$$
Tonelli's theorem therefore permits interchange of the sum and the integral:
$$
\begin{aligned}
\int_0^\infty \frac{t e^{-t/2}}{1-e^{-t}}\,dt
&=
\sum_{n=0}^\infty
\int_0^\infty t e^{-(n+1/2)t}\,dt\\
&=
\sum_{n=0}^\infty \frac{1}{(n+1/2)^2}
&&\text{by step [](#s1-2){.pf-ref}}\\
&=
4\sum_{n=0}^\infty \frac{1}{(2n+1)^2}.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required identity.

:::

:::

:::
