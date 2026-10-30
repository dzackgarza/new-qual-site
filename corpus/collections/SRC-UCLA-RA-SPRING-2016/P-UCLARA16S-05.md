---
schema: qual/card@1
id: P-UCLARA16S-05
kind: problem
title: Unbounded $L^2$ growth of Fourier representations of planar wave solutions
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - L²
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
For $f\in C_0^\infty(\RR^2)$ define $u(x,t)$ by
$$
u(x,t)=\int_{\RR^2}e^{ix\cdot\xi}\frac{\sin(t\norm{\xi})}{\norm{\xi}}f(\xi)\,d\xi,
\qquad x\in\RR^2,\ t>0.
$$
Show that
$$
\lim_{t\to\infty}\norm{ u(\cdot,t)}_{L^2}=\infty
$$
for a set of $f$ that is dense in $L^2(\RR^2)$.
:::

::: {.solution}

Let
$$
\mathcal D
\coloneqq
\{f\in C_0^\infty(\RR^2):f(0)\ne0\}.
$$

::: pf

::: {.pf-step #s1-1}

For every $f\in\mathcal D$, there are constants $c>0$ and $r_0>0$ such that
$$
\abs{f(\xi)}\ge c
\qquad
(\norm{\xi}\le r_0).
$$


::: pf-proof

Since $f$ is continuous and $f(0)\ne0$, choose $r_0>0$ so that
$$
\abs{f(\xi)-f(0)}<\frac{\abs{f(0)}}{2}
\qquad
(\norm{\xi}\le r_0).
$$
Then
$$
\abs{f(\xi)}
\ge
\abs{f(0)}-\abs{f(\xi)-f(0)}
>
\frac{\abs{f(0)}}{2}.
$$
Take $c=\abs{f(0)}/2$.

:::

:::

::: {.pf-step #s1-2}

For every $f\in\mathcal D$ there is a constant $C_f>0$, independent of $t$, such that
$$
\norm{u(\cdot,t)}_{L^2}^2
\ge
C_f
\int_0^{t r_0}\frac{\sin^2 s}{s}\,ds.
$$


::: pf-proof

For fixed $t>0$, set
$$
g_t(\xi)
\coloneqq
\frac{\sin(t\norm{\xi})}{\norm{\xi}}f(\xi).
$$
The apparent singularity at $\xi=0$ is removable because
$$
\frac{\sin(t\norm{\xi})}{\norm{\xi}}
\longrightarrow t
\qquad
(\xi\to0),
$$
and $g_t$ has compact support. Hence $g_t\in L^2(\RR^2)$.

The function $u(\cdot,t)$ is the Fourier transform of $g_t$ up to the fixed Fourier-normalization convention, so Plancherel gives a constant $C_{\mathrm P}>0$, independent of $f$ and $t$, such that
$$
\norm{u(\cdot,t)}_{L^2}^2
=
C_{\mathrm P}
\int_{\RR^2}
\frac{\sin^2(t\norm{\xi})}{\norm{\xi}^2}
\abs{f(\xi)}^2\,d\xi.
$$
Using step [](#s1-1){.pf-ref} and polar coordinates,
$$
\begin{aligned}
\norm{u(\cdot,t)}_{L^2}^2
&\ge
C_{\mathrm P}c^2
\int_{\norm{\xi}\le r_0}
\frac{\sin^2(t\norm{\xi})}{\norm{\xi}^2}\,d\xi\\
&=
2\pi C_{\mathrm P}c^2
\int_0^{r_0}
\frac{\sin^2(tr)}{r}\,dr\\
&=
2\pi C_{\mathrm P}c^2
\int_0^{t r_0}
\frac{\sin^2 s}{s}\,ds.
\end{aligned}
$$
Take $C_f=2\pi C_{\mathrm P}c^2$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\int_0^R\frac{\sin^2 s}{s}\,ds
\longrightarrow\infty
\qquad
(R\to\infty).
$$


::: pf-proof

For every integer $k\ge0$ and every
$$
s\in
\left[k\pi+\frac{\pi}{4},
k\pi+\frac{3\pi}{4}\right],
$$
one has $\sin^2 s\ge1/2$. Therefore, whenever $R$ contains the first $N$ such intervals,
$$
\begin{aligned}
\int_0^R\frac{\sin^2 s}{s}\,ds
&\ge
\frac12
\sum_{k=0}^{N-1}
\int_{k\pi+\pi/4}^{k\pi+3\pi/4}
\frac{ds}{s}\\
&\ge
\frac12
\sum_{k=0}^{N-1}
\frac{\pi/2}{k\pi+3\pi/4}.
\end{aligned}
$$
The final series diverges by comparison with the harmonic series. Hence the integral tends to infinity.

:::

:::

::: {.pf-step #s1-4}

For every $f\in\mathcal D$,
$$
\boxed{
\lim_{t\to\infty}
\norm{u(\cdot,t)}_{L^2}
=\infty}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\norm{u(\cdot,t)}_{L^2}^2
\ge
C_f
\int_0^{t r_0}\frac{\sin^2 s}{s}\,ds.
$$
Since $t r_0\to\infty$ and the integral diverges by step [](#s1-3){.pf-ref}, the squared norm tends to infinity, hence so does the norm.

:::

:::

::: {.pf-step #s1-5}

The set $\mathcal D$ is dense in $L^2(\RR^2)$.


::: pf-proof

Fix $F\in L^2(\RR^2)$ and $\varepsilon>0$. Since $C_0^\infty(\RR^2)$ is dense in $L^2(\RR^2)$, choose
$$
\varphi\in C_0^\infty(\RR^2)
$$
with
$$
\norm{F-\varphi}_2<\frac{\varepsilon}{2}.
$$
Choose $\psi\in C_0^\infty(\RR^2)$ with $\psi(0)=1$. Pick a nonzero scalar $\delta$ such that
$$
\abs{\delta}\,\norm{\psi}_2<\frac{\varepsilon}{2}
\qquad\text{and}\qquad
\varphi(0)+\delta\ne0.
$$
Then
$$
h\coloneqq\varphi+\delta\psi
$$
belongs to $\mathcal D$, and
$$
\norm{F-h}_2
\le
\norm{F-\varphi}_2
+
\abs{\delta}\,\norm{\psi}_2
<
\varepsilon.
$$
Thus every $L^2$ function can be approximated arbitrarily closely by elements of $\mathcal D$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the required divergence for every $f\in\mathcal D$, and step [](#s1-5){.pf-ref} proves that $\mathcal D$ is dense in $L^2(\RR^2)$.

:::

:::

:::
