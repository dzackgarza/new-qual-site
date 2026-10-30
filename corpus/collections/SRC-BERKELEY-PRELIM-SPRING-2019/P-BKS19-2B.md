---
schema: qual/card@1
id: P-BKS19-2B
kind: problem
title: Gaussian integral via $F(t)^2+G(t)$ constant
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 differentiation argument. The intended identity and value $F(\infty)=\sqrt{\pi}/2$ are correct; the solution below supplies the differentiation-under-the-integral calculation and limiting argument.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified $G'(t)=-2F(t)e^{-t^2}$, constancy of $F^2+G$, the constant value $\pi/4$, and decay of $G(t)$.
---

::: {.problem}
For $t\ge0$ let
$$
F(t)=\int_0^t e^{-x^2}\,dx
$$
and
$$
G(t)=\int_0^1\frac{e^{-t^2(1+x^2)}}{1+x^2}\,dx.
$$
Show that $F(t)^2+G(t)$ is constant and deduce the value of $F(\infty)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $t\geq0$,
$$
F'(t)=e^{-t^2}
$$
and
$$
G'(t)=-2e^{-t^2}F(t).
$$


::: pf-proof

The first identity is the fundamental theorem of calculus. For the second, differentiation under the integral sign is justified on every bounded $t$-interval because the integrand and its $t$-derivative are continuous there. Thus
$$
\begin{aligned}
G'(t)
&=\int_0^1
\frac{-2t(1+x^2)e^{-t^2(1+x^2)}}{1+x^2}\,dx\\
&=-2e^{-t^2}\,t\int_0^1 e^{-t^2x^2}\,dx.
\end{aligned}
$$
The substitution $u=tx$ gives
$$
t\int_0^1e^{-t^2x^2}\,dx
=
\int_0^t e^{-u^2}\,du
=F(t),
$$
with both sides equal to $0$ when $t=0$. This proves the second identity.

:::

:::

::: {.pf-step #s1-2}

The function $F(t)^2+G(t)$ is constant on $[0,\infty)$.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\frac{d}{dt}\bigl(F(t)^2+G(t)\bigr)
=
2F(t)e^{-t^2}-2F(t)e^{-t^2}
=0.
$$

:::

:::

::: {.pf-step #s1-3}

The constant value is
$$
F(t)^2+G(t)=\frac{\pi}{4}.
$$


::: pf-proof

At $t=0$,
$$
F(0)=0
$$
and
$$
G(0)
=
\int_0^1\frac{dx}{1+x^2}
=
\left[\arctan x\right]_0^1
=
\frac{\pi}{4}.
$$
Apply step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

One has $G(t)\to0$ as $t\to\infty$.


::: pf-proof

For $0\leq x\leq1$,
$$
0\leq
\frac{e^{-t^2(1+x^2)}}{1+x^2}
\leq
\frac{e^{-t^2}}{1+x^2}.
$$
Therefore
$$
0\leq G(t)\leq \frac{\pi}{4}e^{-t^2}\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-5}

The Gaussian half-integral is
$$
\boxed{F(\infty)=\frac{\sqrt{\pi}}{2}}.
$$


::: pf-proof

The function $F(t)$ is increasing and bounded above by step [](#s1-3){.pf-ref}, so $F(\infty)$ exists. Letting $t\to\infty$ in step [](#s1-3){.pf-ref} and using step [](#s1-4){.pf-ref} gives
$$
F(\infty)^2=\frac{\pi}{4}.
$$
Since $F(\infty)>0$, the positive square root gives the displayed value.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} prove constancy, and step [](#s1-5){.pf-ref} gives the requested value.

:::

:::

:::
