---
schema: qual/card@1
id: P-BKS19-1A
kind: problem
title: Decaying solutions of $y'''=y$
classification:
  areas:
  - prelim
  topics: []
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
  note: Independently reviewed the supplied Berkeley Spring 2019 characteristic-root solution. The argument is correct; the solution below makes explicit why the decaying hypothesis eliminates the root $1$.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the characteristic roots, the decay of the two nonreal modes, elimination of the growing mode, and the identity $1+r+r^2=0$ for the remaining roots.
---

::: {.problem}
Let $y$ be a solution of
$$
y'''-y=0
$$
such that $y(t)\to0$ as $t\to\infty$.
Show that
$$
y(0)+y'(0)+y''(0)=0.
$$
:::

::: {.solution}

Let
$$
\omega\coloneqq\frac{-1+i\sqrt3}{2},
\qquad
\overline\omega\coloneqq\frac{-1-i\sqrt3}{2}.
$$

::: pf

::: {.pf-step #s1-1}

Every solution has the form
$$
y(t)=c_0e^t+c_1e^{\omega t}+c_2e^{\overline\omega t}
$$
for constants $c_0,c_1,c_2$.


::: pf-proof

The characteristic polynomial is
$$
r^3-1=(r-1)(r^2+r+1),
$$
whose three distinct roots are $1$, $\omega$, and $\overline\omega$. The standard solution formula for a constant-coefficient linear differential equation with distinct characteristic roots gives the displayed expression.

:::

:::

::: {.pf-step #s1-2}

The condition $y(t)\to0$ as $t\to\infty$ forces $c_0=0$.


::: pf-proof

Since
$$
\operatorname{Re}(\omega)=\operatorname{Re}(\overline\omega)=-\frac12,
$$
both $e^{\omega t}$ and $e^{\overline\omega t}$ tend to $0$ as $t\to\infty$. Hence step [](#s1-1){.pf-ref} gives
$$
c_0e^t
=
y(t)-c_1e^{\omega t}-c_2e^{\overline\omega t}
\longrightarrow0.
$$
If $c_0\neq0$, then $\abs{c_0e^t}=\abs{c_0}e^t\to\infty$, a contradiction. Thus $c_0=0$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
y(0)+y'(0)+y''(0)=\boxed{0}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
y(t)=c_1e^{\omega t}+c_2e^{\overline\omega t}.
$$
Therefore
$$
\begin{aligned}
y(0)+y'(0)+y''(0)
&=c_1(1+\omega+\omega^2)
+c_2(1+\overline\omega+\overline\omega^2).
\end{aligned}
$$
Both $\omega$ and $\overline\omega$ are roots of $r^2+r+1$, so both parenthesized expressions vanish.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves the required identity.

:::

:::

:::
