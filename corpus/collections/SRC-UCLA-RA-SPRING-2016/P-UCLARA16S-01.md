---
schema: qual/card@1
id: P-UCLARA16S-01
kind: problem
title: $L^3\to L^\infty$ bounds for the heat kernel on $\RR^3$
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let
$$
K_t(x)=(4\pi t)^{-3/2}e^{-|x|^2/(4t)},\qquad x\in\RR^3,\ t>0,
$$
where $|x|$ is the Euclidean norm of $x\in\RR^3$.

(a) Show that the linear map
$$
L^3(\RR^3)\ni f\longmapsto t^{1/2}K_t*f\in L^\infty(\RR^3)
$$
is bounded, uniformly in $t>0$. Here
$$
K_t*f(x)=\int_{\RR^3}K_t(x-y)f(y)\,dy.
$$

(b) Prove that $t^{1/2}\lVert K_t*f\rVert_{L^\infty}\to0$ as $t\to0$, for $f\in L^3(\RR^3)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The heat kernel satisfies the scaling identity
$$
K_t(x)
=
t^{-3/2}K_1\!\left(\frac{x}{\sqrt t}\right).
$$


::: pf-proof

By definition,
$$
\begin{aligned}
t^{-3/2}K_1\!\left(\frac{x}{\sqrt t}\right)
&=
t^{-3/2}(4\pi)^{-3/2}
\exp\!\left(-\frac{|x|^2}{4t}\right)\\
&=
(4\pi t)^{-3/2}
\exp\!\left(-\frac{|x|^2}{4t}\right)\\
&=
K_t(x).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
\|K_t\|_{L^{3/2}}
=
t^{-1/2}\|K_1\|_{L^{3/2}}.
$$


::: pf-proof

Using step [](#s1-1){.pf-ref} and the change of variables
$$
y=\frac{x}{\sqrt t},
\qquad
dx=t^{3/2}\,dy,
$$
gives
$$
\begin{aligned}
\|K_t\|_{3/2}^{3/2}
&=
\int_{\RR^3}
t^{-9/4}
\left|
K_1\!\left(\frac{x}{\sqrt t}\right)
\right|^{3/2}
dx\\
&=
t^{-9/4}t^{3/2}
\int_{\RR^3}|K_1(y)|^{3/2}\,dy\\
&=
t^{-3/4}
\|K_1\|_{3/2}^{3/2}.
\end{aligned}
$$
Raising both sides to the power $2/3$ yields the claimed scaling.

:::

:::

::: {.pf-step #s1-3}

For every $f\in L^3(\RR^3)$ and every $t>0$,
$$
\boxed{
t^{1/2}\|K_t*f\|_{L^\infty}
\le
\|K_1\|_{L^{3/2}}\|f\|_{L^3}
}.
$$


::: pf-proof

Young's convolution inequality with exponents
$$
\frac{2}{3}+\frac{1}{3}=1
$$
gives
$$
\|K_t*f\|_\infty
\le
\|K_t\|_{3/2}\|f\|_3.
$$
Substitute the scaling from step [](#s1-2){.pf-ref} and multiply by $t^{1/2}$.

:::

:::

::: {.pf-step #s1-4}

The operators
$$
T_t:L^3(\RR^3)\to L^\infty(\RR^3),
\qquad
T_tf=t^{1/2}K_t*f,
$$
are bounded uniformly in $t>0$.


::: pf-proof

Step [](#s1-3){.pf-ref} gives
$$
\|T_tf\|_\infty
\le
\|K_1\|_{3/2}\|f\|_3
$$
with a constant independent of $t$. This proves part (a).

:::

:::

::: {.pf-step #s1-5}

If $g\in C_c(\RR^3)$, then
$$
t^{1/2}\|K_t*g\|_\infty
\longrightarrow0
\qquad
(t\to0).
$$


::: pf-proof

The heat kernel has total mass $1$:
$$
\|K_t\|_1=1.
$$
Therefore Young's inequality gives
$$
\|K_t*g\|_\infty
\le
\|K_t\|_1\|g\|_\infty
=
\|g\|_\infty.
$$
Hence
$$
0
\le
t^{1/2}\|K_t*g\|_\infty
\le
t^{1/2}\|g\|_\infty
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-6}

For every $f\in L^3(\RR^3)$,
$$
\boxed{
t^{1/2}\|K_t*f\|_\infty
\longrightarrow0
\qquad
(t\to0)
}.
$$


::: pf-proof

Fix $\varepsilon>0$. Since $C_c(\RR^3)$ is dense in $L^3(\RR^3)$, choose $g\in C_c(\RR^3)$ such that
$$
\|f-g\|_3
<
\frac{\varepsilon}{2\|K_1\|_{3/2}}.
$$
By step [](#s1-5){.pf-ref}, there exists $\delta>0$ such that
$$
t^{1/2}\|K_t*g\|_\infty
<
\frac{\varepsilon}{2}
\qquad
(0<t<\delta).
$$
For such $t$, step [](#s1-3){.pf-ref} gives
$$
\begin{aligned}
t^{1/2}\|K_t*f\|_\infty
&\le
t^{1/2}\|K_t*(f-g)\|_\infty
+
t^{1/2}\|K_t*g\|_\infty\\
&\le
\|K_1\|_{3/2}\|f-g\|_3
+
\frac{\varepsilon}{2}\\
&<
\varepsilon.
\end{aligned}
$$
This proves part (b).

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (a), and step [](#s1-6){.pf-ref} proves part (b).

:::

:::

:::
