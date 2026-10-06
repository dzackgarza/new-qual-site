---
schema: qual/card@1
id: P-UCLARA16S-01
kind: problem
title: $L^3\to L^\infty$ bounds for the heat kernel on $\mathbb R^3$
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
\[
K_t(x)=(4\pi t)^{-3/2}e^{-|x|^2/(4t)},\qquad x\in\mathbb R^3,\ t>0,
\]
where $|x|$ is the Euclidean norm of $x\in\mathbb R^3$.

(a) Show that the linear map
\[
L^3(\mathbb R^3)\ni f\longmapsto t^{1/2}K_t*f\in L^\infty(\mathbb R^3)
\]
is bounded, uniformly in $t>0$. Here
\[
K_t*f(x)=\int_{\mathbb R^3}K_t(x-y)f(y)\,dy.
\]

(b) Prove that $t^{1/2}\lVert K_t*f\rVert_{L^\infty}\to0$ as $t\to0$, for $f\in L^3(\mathbb R^3)$.
:::

::: {.solution}
<1>1. The heat kernel satisfies the scaling identity
\[
K_t(x)
=
t^{-3/2}K_1\!\left(\frac{x}{\sqrt t}\right).
\]

::: {.proof}
By definition,
\[
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
\]
:::

<1>2. One has
\[
\|K_t\|_{L^{3/2}}
=
t^{-1/2}\|K_1\|_{L^{3/2}}.
\]

::: {.proof}
Using step <1>1 and the change of variables
\[
y=\frac{x}{\sqrt t},
\qquad
dx=t^{3/2}\,dy,
\]
gives
\[
\begin{aligned}
\|K_t\|_{3/2}^{3/2}
&=
\int_{\mathbb R^3}
t^{-9/4}
\left|
K_1\!\left(\frac{x}{\sqrt t}\right)
\right|^{3/2}
dx\\
&=
t^{-9/4}t^{3/2}
\int_{\mathbb R^3}|K_1(y)|^{3/2}\,dy\\
&=
t^{-3/4}
\|K_1\|_{3/2}^{3/2}.
\end{aligned}
\]
Raising both sides to the power $2/3$ yields the claimed scaling.
:::

<1>3. For every $f\in L^3(\mathbb R^3)$ and every $t>0$,
\[
\boxed{
t^{1/2}\|K_t*f\|_{L^\infty}
\le
\|K_1\|_{L^{3/2}}\|f\|_{L^3}
}.
\]

::: {.proof}
Young's convolution inequality with exponents
\[
\frac{2}{3}+\frac{1}{3}=1
\]
gives
\[
\|K_t*f\|_\infty
\le
\|K_t\|_{3/2}\|f\|_3.
\]
Substitute the scaling from step <1>2 and multiply by $t^{1/2}$.
:::

<1>4. The operators
\[
T_t:L^3(\mathbb R^3)\to L^\infty(\mathbb R^3),
\qquad
T_tf=t^{1/2}K_t*f,
\]
are bounded uniformly in $t>0$.

::: {.proof}
Step <1>3 gives
\[
\|T_tf\|_\infty
\le
\|K_1\|_{3/2}\|f\|_3
\]
with a constant independent of $t$. This proves part (a).
:::

<1>5. If $g\in C_c(\mathbb R^3)$, then
\[
t^{1/2}\|K_t*g\|_\infty
\longrightarrow0
\qquad
(t\to0).
\]

::: {.proof}
The heat kernel has total mass $1$:
\[
\|K_t\|_1=1.
\]
Therefore Young's inequality gives
\[
\|K_t*g\|_\infty
\le
\|K_t\|_1\|g\|_\infty
=
\|g\|_\infty.
\]
Hence
\[
0
\le
t^{1/2}\|K_t*g\|_\infty
\le
t^{1/2}\|g\|_\infty
\longrightarrow0.
\]
:::

<1>6. For every $f\in L^3(\mathbb R^3)$,
\[
\boxed{
t^{1/2}\|K_t*f\|_\infty
\longrightarrow0
\qquad
(t\to0)
}.
\]

::: {.proof}
Fix $\varepsilon>0$. Since $C_c(\mathbb R^3)$ is dense in $L^3(\mathbb R^3)$, choose $g\in C_c(\mathbb R^3)$ such that
\[
\|f-g\|_3
<
\frac{\varepsilon}{2\|K_1\|_{3/2}}.
\]
By step <1>5, there exists $\delta>0$ such that
\[
t^{1/2}\|K_t*g\|_\infty
<
\frac{\varepsilon}{2}
\qquad
(0<t<\delta).
\]
For such $t$, step <1>3 gives
\[
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
\]
This proves part (b).
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>4 proves part (a), and step <1>6 proves part (b).
:::
:::
