---
schema: qual/card@1
id: P-UCLARA15S-04
kind: problem
title: Density of translates in $L^1$ of the circle and nonvanishing Fourier coefficients
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2015, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f\in L^1_{\mathrm{loc}}(\RR)$ be $2\pi$-periodic.
Show that linear combinations of the translates $f(x-a)$, $a\in\RR$, are dense in $L^1((0,2\pi))$ if and only if each Fourier coefficient of $f$ is nonzero.
:::

::: {.solution}

For a $2\pi$-periodic integrable function $h$, write
$$
\widehat h(n)
\coloneqq
\frac1{2\pi}
\int_0^{2\pi}h(x)e^{-inx}\,dx,
\qquad n\in\ZZ.
$$
Let
$$
\mathcal T_f
\coloneqq
\operatorname{span}
\{f(\cdot-a):a\in\RR\}.
$$

::: pf

::: {.pf-step #s1-1}

If $\widehat f(n_0)=0$ for some $n_0\in\ZZ$, then $\mathcal T_f$ is not dense in $L^1((0,2\pi))$.


::: pf-proof

For a translate,
$$
\begin{aligned}
\widehat{f(\cdot-a)}(n)
&=
\frac1{2\pi}
\int_0^{2\pi}
f(x-a)e^{-inx}\,dx\\
&=
e^{-ina}\widehat f(n).
\end{aligned}
$$
Hence every $h\in\mathcal T_f$ satisfies
$$
\widehat h(n_0)=0.
$$
The functional
$$
L^1((0,2\pi))\to\CC,
\qquad
h\mapsto\widehat h(n_0)
$$
is continuous because
$$
|\widehat h(n_0)|
\le
\frac1{2\pi}\|h\|_1.
$$
Therefore the $L^1$-closure of $\mathcal T_f$ is contained in the proper closed subspace
$$
\{h:\widehat h(n_0)=0\}.
$$
It is proper because
$$
\widehat{e^{in_0x}}(n_0)=1.
$$
Thus $\mathcal T_f$ cannot be dense.

:::

:::

::: {.pf-step #s1-2}

Now suppose that
$$
\widehat f(n)\ne0
\qquad
(n\in\ZZ).
$$
If the closure
$$
X
\coloneqq
\overline{\mathcal T_f}^{\,L^1}
$$
were proper, then there would exist a nonzero $g\in L^\infty((0,2\pi))$ such that
$$
\int_0^{2\pi}
h(x)\overline{g(x)}\,dx
=0
\qquad
(h\in X).
$$


::: pf-proof

If $X$ is a proper closed subspace of $L^1((0,2\pi))$, the Hahn--Banach theorem gives a nonzero continuous linear functional
$$
\Lambda\in(L^1)^*
$$
that vanishes on $X$. The standard identification
$$
(L^1)^*=L^\infty
$$
gives a nonzero $g\in L^\infty((0,2\pi))$ such that
$$
\Lambda(h)
=
\int_0^{2\pi}
h(x)\overline{g(x)}\,dx.
$$
Since $\Lambda$ vanishes on $X$, the displayed annihilation identity follows.

:::

:::

::: {.pf-step #s1-3}

Under the assumption of step [](#s1-2){.pf-ref}, define
$$
H(a)
\coloneqq
\int_0^{2\pi}
f(x-a)\overline{g(x)}\,dx.
$$
Then
$$
H(a)=0
\qquad
(a\in\RR).
$$


::: pf-proof

For each $a$, the translate $f(\cdot-a)$ belongs to $\mathcal T_f\subset X$. The annihilation identity in step [](#s1-2){.pf-ref} therefore gives $H(a)=0$.

:::

:::

::: {.pf-step #s1-4}

For every $n\in\ZZ$,
$$
\widehat H(n)
=
2\pi
\widehat f(-n)
\overline{\widehat g(-n)}.
$$


::: pf-proof

Because $f\in L^1(0,2\pi)$ and $g\in L^\infty(0,2\pi)$, the function
$$
(a,x)
\longmapsto
f(x-a)\overline{g(x)}
$$
is integrable on the two-dimensional torus, so Fubini's theorem applies. Thus
$$
\begin{aligned}
\widehat H(n)
&=
\frac1{2\pi}
\int_0^{2\pi}
\int_0^{2\pi}
f(x-a)\overline{g(x)}
e^{-ina}\,dx\,da\\
&=
\frac1{2\pi}
\int_0^{2\pi}
\overline{g(x)}
\left(
\int_0^{2\pi}
f(x-a)e^{-ina}\,da
\right)dx.
\end{aligned}
$$
With $y=x-a$ and periodicity of $f$,
$$
\int_0^{2\pi}
f(x-a)e^{-ina}\,da
=
2\pi e^{-inx}\widehat f(-n).
$$
Hence
$$
\begin{aligned}
\widehat H(n)
&=
\widehat f(-n)
\int_0^{2\pi}
\overline{g(x)}e^{-inx}\,dx\\
&=
2\pi
\widehat f(-n)
\overline{\widehat g(-n)}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

The assumption that all Fourier coefficients of $f$ are nonzero forces
$$
\widehat g(n)=0
\qquad
(n\in\ZZ).
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, $H\equiv0$, so
$$
\widehat H(n)=0
\qquad
(n\in\ZZ).
$$
Step [](#s1-4){.pf-ref} therefore gives
$$
\widehat f(-n)
\overline{\widehat g(-n)}
=0.
$$
Since $\widehat f(-n)\ne0$ by hypothesis,
$$
\widehat g(-n)=0
$$
for every $n$, which is equivalent to the stated conclusion.

:::

:::

::: {.pf-step #s1-6}

The function $g$ in step [](#s1-2){.pf-ref} must vanish almost everywhere.


::: pf-proof

Since the interval $(0,2\pi)$ has finite measure,
$$
g\in L^\infty
\subset
L^1.
$$
By step [](#s1-5){.pf-ref} all Fourier coefficients of $g$ vanish. The uniqueness theorem for Fourier series of $L^1$ functions implies
$$
g=0
$$
almost everywhere.

:::

:::

::: {.pf-step #s1-7}

If every Fourier coefficient of $f$ is nonzero, then $\mathcal T_f$ is dense in $L^1((0,2\pi))$.


::: pf-proof

If the closure $X$ were proper, step [](#s1-2){.pf-ref} would produce a nonzero annihilator $g\in L^\infty$, whereas step [](#s1-6){.pf-ref} would force that annihilator to be zero almost everywhere. This contradiction shows
$$
X=L^1((0,2\pi)).
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves necessity, and step [](#s1-7){.pf-ref} proves sufficiency.

:::

:::

:::
