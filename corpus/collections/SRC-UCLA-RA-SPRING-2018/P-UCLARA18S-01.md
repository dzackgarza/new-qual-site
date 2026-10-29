---
schema: qual/card@1
id: P-UCLARA18S-01
kind: problem
title: $L^1$ functions with vanishing $L^1$ difference quotients are zero
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 1. Suppose $f\in L^1(\RR)$ satisfies
$$
\limsup_{h\to0}\int_{\RR}\left|\frac{f(x+h)-f(x)}{h}\right|\,dx=0.
$$
Show that $f=0$ almost everywhere.
:::

::: {.solution}

Define
$$
F(x)=\int_{-\infty}^{x}|f(t)|\,dt.
$$

::: pf

::: {.pf-step #s1-1}

For every $x\in\RR$ and every $h\ne0$,
$$
\left|
\frac{F(x+h)-F(x)}{h}
\right|
\le
\int_{\RR}
\left|
\frac{f(t+h)-f(t)}{h}
\right|\,dt.
$$


::: pf-proof

First suppose $h>0$. By the change of variables $s=t+h$,
$$
F(x+h)
=
\int_{-\infty}^{x+h}|f(s)|\,ds
=
\int_{-\infty}^{x}|f(t+h)|\,dt.
$$
Hence
$$
\begin{aligned}
\left|
\frac{F(x+h)-F(x)}{h}
\right|
&=
\left|
\frac1h
\int_{-\infty}^{x}
\bigl(|f(t+h)|-|f(t)|\bigr)\,dt
\right|\\
&\le
\int_{-\infty}^{x}
\frac{
\bigl||f(t+h)|-|f(t)|\bigr|
}{h}\,dt\\
&\le
\int_{\RR}
\frac{|f(t+h)-f(t)|}{h}\,dt.
\end{aligned}
$$
For $h<0$, the same computation with $|h|$ in the denominator gives the
identical final bound, namely
$$
\int_{\RR}
\left|
\frac{f(t+h)-f(t)}{h}
\right|\,dt.
$$

:::

:::

::: {.pf-step #s1-2}

The hypothesis implies
$$
\lim_{h\to0}
\int_{\RR}
\left|
\frac{f(t+h)-f(t)}{h}
\right|\,dt
=0.
$$


::: pf-proof

The integrals are nonnegative. A nonnegative function of $h$ whose
$\limsup$ at $0$ is $0$ has limit $0$.

:::

:::

::: {.pf-step #s1-3}

The function $F$ is differentiable at every $x$ and
$$
\boxed{F'(x)=0}.
$$


::: pf-proof

Fix $x\in\RR$. By step [](#s1-1){.pf-ref},
$$
\left|
\frac{F(x+h)-F(x)}{h}
\right|
$$
is bounded above by a quantity independent of $x$ that tends to $0$ by
step [](#s1-2){.pf-ref}. Therefore
$$
\lim_{h\to0}
\frac{F(x+h)-F(x)}{h}
=0.
$$

:::

:::

::: {.pf-step #s1-4}

The function $F$ is constant on $\RR$.


::: pf-proof

By step [](#s1-3){.pf-ref}, $F$ is differentiable everywhere with derivative identically
zero. The ordinary mean value theorem therefore gives
$$
F(y)-F(x)=0
$$
for every $x<y$.

:::

:::

::: {.pf-step #s1-5}

In fact,
$$
\boxed{F\equiv0}.
$$


::: pf-proof

Since $|f|\in L^1(\RR)$,
$$
\int_{-\infty}^{x}|f(t)|\,dt
\longrightarrow0
\qquad(x\to-\infty).
$$
Thus the constant value from step [](#s1-4){.pf-ref} must be $0$.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\int_{\RR}|f(t)|\,dt=0.
$$


::: pf-proof

By monotone convergence,
$$
\int_{\RR}|f(t)|\,dt
=
\lim_{x\to\infty}
\int_{-\infty}^{x}|f(t)|\,dt
=
\lim_{x\to\infty}F(x)
=0
$$
by step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{f=0\quad\text{almost everywhere}}.
$$


::: pf-proof

A nonnegative integrable function with integral zero vanishes almost
everywhere. Apply this to $|f|$ using step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
