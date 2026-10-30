---
schema: qual/card@1
id: P-UCLARA12S-04
kind: problem
title: 'A closed mean-zero subspace of $L^1$ and $L^2$ density'
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - L²
  - Density
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let
$$
S=\left\{f\in L^1(\RR^3):\int_{\RR^3}f(x)\,dx=0\right\}.
$$

(a) Show that $S$ is closed in the $L^1$ topology.

(b) Show that $S\cap L^2(\RR^3)$ is dense in $L^2(\RR^3)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The linear functional
$$
T:L^1(\RR^3)\to\RR,
\qquad
T(f)=\int_{\RR^3}f(x)\,dx,
$$
is continuous.


::: pf-proof

For every $f\in L^1(\RR^3)$,
$$
\abs{T(f)}
\le
\int_{\RR^3}\abs{f(x)}\,dx
=
\norm f_{L^1}.
$$
Thus $T$ is bounded, hence continuous.

:::

:::

::: {.pf-step #s1-2}

The subspace $S$ is closed in $L^1(\RR^3)$.


::: pf-proof

By definition,
$$
S=\ker T.
$$
The kernel of the continuous linear functional from step [](#s1-1){.pf-ref} is closed.

:::

:::

::: {.pf-step #s1-3}

Every compactly supported $h\in L^2(\RR^3)$ can be approximated arbitrarily closely in $L^2$ by an element of $S\cap L^2(\RR^3)$.


::: pf-proof

Because $h$ has compact support, $h\in L^1(\RR^3)$ by Cauchy--Schwarz. Set
$$
I\coloneqq\int_{\RR^3}h(x)\,dx.
$$
If $I=0$, then $h\in S\cap L^2$ already.

Assume $I\ne0$, and fix $\varepsilon>0$. Choose a measurable set $E\subset\RR^3$ of finite measure $V$ such that
$$
V>\frac{\abs I^2}{\varepsilon^2}.
$$
Define
$$
g
\coloneqq
h-\frac{I}{V}\mathbf 1_E.
$$
Then $g\in L^1\cap L^2$ and
$$
\int_{\RR^3}g
=
I-\frac{I}{V}V
=0,
$$
so $g\in S\cap L^2$. Moreover,
$$
\norm{g-h}_{L^2}
=
\frac{\abs I}{V}\norm{\mathbf1_E}_{L^2}
=
\frac{\abs I}{\sqrt V}
<\varepsilon.
$$

:::

:::

::: {.pf-step #s1-4}

The subspace $S\cap L^2(\RR^3)$ is dense in $L^2(\RR^3)$.


::: pf-proof

Let $f\in L^2(\RR^3)$ and $\varepsilon>0$. Compactly supported $L^2$ functions are dense in $L^2$, so choose a compactly supported $h\in L^2$ with
$$
\norm{f-h}_{L^2}<\frac{\varepsilon}{2}.
$$
By step [](#s1-3){.pf-ref}, choose $g\in S\cap L^2$ with
$$
\norm{h-g}_{L^2}<\frac{\varepsilon}{2}.
$$
Then
$$
\norm{f-g}_{L^2}
\le
\norm{f-h}_{L^2}
+\norm{h-g}_{L^2}
<\varepsilon.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), and step [](#s1-4){.pf-ref} proves part (b).

:::

:::

:::
