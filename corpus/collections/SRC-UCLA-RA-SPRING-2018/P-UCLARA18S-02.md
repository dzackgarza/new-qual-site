---
schema: qual/card@1
id: P-UCLARA18S-02
kind: problem
title: Nonnegativity and closed sublevel sets of the second-difference form $Q(f,h)$
classification:
  areas:
  - real-analysis
  topics:
  - L²
  - Fourier Transform
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Given $f\in L^2(\RR)$ and $h>0$, define
$$
Q(f,h)=\int_{\RR}\frac{2f(x)-f(x+h)-f(x-h)}{h^2}\,\overline{f(x)}\,dx.
$$

(a) Show that
$$
Q(f,h)\ge0
$$
for all $f\in L^2(\RR)$ and all $h>0$.

(b) Show that the set
$$
E=\left\{f\in L^2(\RR):\limsup_{h\to0}Q(f,h)\le1\right\}
$$
is closed in $L^2(\RR)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $f\in L^2(\RR)$ and $h>0$,
$$
\boxed{
Q(f,h)
=
\frac1{h^2}
\int_{\RR}\abs{f(x+h)-f(x)}^2\,dx}.
$$


::: pf-proof

Set
$$
A_h
=
\int_{\RR}f(x+h)\overline{f(x)}\,dx.
$$
By the change of variables $y=x-h$,
$$
\int_{\RR}f(x-h)\overline{f(x)}\,dx
=
\int_{\RR}f(y)\overline{f(y+h)}\,dy
=
\overline{A_h}.
$$
Therefore
$$
\begin{aligned}
h^2Q(f,h)
&=
2\norm{f}_2^2
-A_h
-\overline{A_h}\\
&=
2\norm{f}_2^2
-2\operatorname{Re}A_h.
\end{aligned}
$$
Translation preserves the $L^2$ norm, so
$$
\begin{aligned}
\norm{f(\cdot+h)-f}_2^2
&=
\norm{f(\cdot+h)}_2^2
+\norm{f}_2^2
-2\operatorname{Re}A_h\\
&=
2\norm{f}_2^2
-2\operatorname{Re}A_h.
\end{aligned}
$$
The two expressions are equal.

:::

:::

::: {.pf-step #s1-2}

Hence
$$
\boxed{Q(f,h)\ge0}.
$$


::: pf-proof

The right-hand side in step [](#s1-1){.pf-ref} is a nonnegative squared norm divided by
$h^2>0$.

:::

:::

::: {.pf-step #s1-3}

Let $\widehat f$ denote the unitary Fourier transform of $f$. Then
$$
\boxed{
Q(f,h)
=
\int_{\RR}
\frac{4\sin^2(h\xi/2)}{h^2}
\abs{\widehat f(\xi)}^2\,d\xi}.
$$


::: pf-proof

Translation satisfies
$$
\widehat{f(\cdot+h)}(\xi)
=
e^{ih\xi}\widehat f(\xi).
$$
By Plancherel and step [](#s1-1){.pf-ref},
$$
\begin{aligned}
Q(f,h)
&=
\frac1{h^2}
\int_{\RR}
\abs{e^{ih\xi}-1}^2
\abs{\widehat f(\xi)}^2\,d\xi\\
&=
\int_{\RR}
\frac{2-2\cos(h\xi)}{h^2}
\abs{\widehat f(\xi)}^2\,d\xi\\
&=
\int_{\RR}
\frac{4\sin^2(h\xi/2)}{h^2}
\abs{\widehat f(\xi)}^2\,d\xi.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

For every $\xi\in\RR$,
$$
\frac{4\sin^2(h\xi/2)}{h^2}
\longrightarrow
\xi^2
\qquad(h\to0),
$$
and
$$
0
\le
\frac{4\sin^2(h\xi/2)}{h^2}
\le
\xi^2.
$$


::: pf-proof

The limit follows from
$$
\frac{\sin t}{t}\to1.
$$
The bound follows from
$$
\abs{\sin t}\le\abs{t}.
$$

:::

:::

::: {.pf-step #s1-5}

For every $f\in L^2(\RR)$,
$$
\boxed{
\lim_{h\to0}Q(f,h)
=
\int_{\RR}
\xi^2\abs{\widehat f(\xi)}^2\,d\xi}
$$
as an equality in $[0,\infty]$.


::: pf-proof

If
$$
\int_{\RR}\xi^2\abs{\widehat f(\xi)}^2\,d\xi<\infty,
$$
then steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} allow the dominated convergence theorem, yielding
the equality.

If the weighted integral is infinite, Fatou's lemma applied to step [](#s1-3){.pf-ref}
gives
$$
\begin{aligned}
\liminf_{h\to0}Q(f,h)
&\ge
\int_{\RR}
\liminf_{h\to0}
\frac{4\sin^2(h\xi/2)}{h^2}
\abs{\widehat f(\xi)}^2\,d\xi\\
&=
\int_{\RR}
\xi^2\abs{\widehat f(\xi)}^2\,d\xi
=\infty.
\end{aligned}
$$
Thus $Q(f,h)\to\infty$ in this case.

:::

:::

::: {.pf-step #s1-6}

Consequently,
$$
\boxed{
E
=
\left\{
f\in L^2(\RR):
\int_{\RR}
\xi^2\abs{\widehat f(\xi)}^2\,d\xi
\le1
\right\}}.
$$


::: pf-proof

By step [](#s1-5){.pf-ref}, the limit of $Q(f,h)$ exists in $[0,\infty]$. Therefore
$$
\limsup_{h\to0}Q(f,h)
\le1
$$
is equivalent to the displayed weighted Fourier integral being at most $1$.

:::

:::

::: {.pf-step #s1-7}

Suppose
$$
f_n\in E
\qquad\text{and}\qquad
f_n\to f
$$
in $L^2(\RR)$. Then
$$
\widehat f_n\to\widehat f
$$
in $L^2(\RR)$.


::: pf-proof

This is Plancherel's theorem: the Fourier transform is unitary on
$L^2(\RR)$.

:::

:::

::: {.pf-step #s1-8}

There is a subsequence
$$
\widehat f_{n_j}
$$
converging to $\widehat f$ almost everywhere.


::: pf-proof

Every $L^2$-convergent sequence has a subsequence converging pointwise almost
everywhere. Apply this to the convergence in step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

One has
$$
\int_{\RR}
\xi^2\abs{\widehat f(\xi)}^2\,d\xi
\le1.
$$


::: pf-proof

By step [](#s1-8){.pf-ref} and Fatou's lemma,
$$
\begin{aligned}
\int_{\RR}
\xi^2\abs{\widehat f(\xi)}^2\,d\xi
&\le
\liminf_{j\to\infty}
\int_{\RR}
\xi^2\abs{\widehat f_{n_j}(\xi)}^2\,d\xi.
\end{aligned}
$$
Since every $f_{n_j}\in E$, step [](#s1-6){.pf-ref} gives
$$
\int_{\RR}
\xi^2\abs{\widehat f_{n_j}(\xi)}^2\,d\xi
\le1.
$$
Hence the liminf is at most $1$.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{f\in E}.
$$


::: pf-proof

Apply the characterization in step [](#s1-6){.pf-ref} to the estimate in step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Thus $E$ is closed in $L^2(\RR)$.


::: pf-proof

Every $L^2$ limit of a sequence in $E$ belongs to $E$ by steps [](#s1-7){.pf-ref} through
[](#s1-10){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), and step [](#s1-11){.pf-ref} proves part (b).

:::

:::

:::
