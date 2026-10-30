---
schema: qual/card@1
id: P-UCLARA18S-01
kind: problem
title: $L^1$ functions with vanishing $L^1$ difference quotients are zero
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Differentiation
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
\limsup_{h\to0}\int_{\RR}\abs{\frac{f(x+h)-f(x)}{h}}\,dx=0.
$$
Show that $f=0$ almost everywhere.
:::

::: {.solution}

Define
$$
F(x)=\int_{-\infty}^{x}\abs{f(t)}\,dt.
$$

::: pf

::: {.pf-step #s1-1}

For every $x\in\RR$ and every $h\ne0$,
$$
\abs{
\frac{F(x+h)-F(x)}{h}
}
\le
\int_{\RR}
\abs{
\frac{f(t+h)-f(t)}{h}
}\,dt.
$$


::: pf-proof

First suppose $h>0$. By the change of variables $s=t+h$,
$$
F(x+h)
=
\int_{-\infty}^{x+h}\abs{f(s)}\,ds
=
\int_{-\infty}^{x}\abs{f(t+h)}\,dt.
$$
Hence
$$
\begin{aligned}
\abs{
\frac{F(x+h)-F(x)}{h}
}
&=
\abs{
\frac1h
\int_{-\infty}^{x}
\bigl(\abs{f(t+h)}-\abs{f(t)}\bigr)\,dt
}\\
&\le
\int_{-\infty}^{x}
\frac{
\abs{\abs{f(t+h)}-\abs{f(t)}}
}{h}\,dt\\
&\le
\int_{\RR}
\frac{\abs{f(t+h)-f(t)}}{h}\,dt.
\end{aligned}
$$
For $h<0$, the same computation with $\abs{h}$ in the denominator gives the
identical final bound, namely
$$
\int_{\RR}
\abs{
\frac{f(t+h)-f(t)}{h}
}\,dt.
$$

:::

:::

::: {.pf-step #s1-2}

The hypothesis implies
$$
\lim_{h\to0}
\int_{\RR}
\abs{
\frac{f(t+h)-f(t)}{h}
}\,dt
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
\abs{
\frac{F(x+h)-F(x)}{h}
}
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

Since $\abs{f}\in L^1(\RR)$,
$$
\int_{-\infty}^{x}\abs{f(t)}\,dt
\longrightarrow0
\qquad(x\to-\infty).
$$
Thus the constant value from step [](#s1-4){.pf-ref} must be $0$.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\int_{\RR}\abs{f(t)}\,dt=0.
$$


::: pf-proof

By monotone convergence,
$$
\int_{\RR}\abs{f(t)}\,dt
=
\lim_{x\to\infty}
\int_{-\infty}^{x}\abs{f(t)}\,dt
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
everywhere. Apply this to $\abs{f}$ using step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
