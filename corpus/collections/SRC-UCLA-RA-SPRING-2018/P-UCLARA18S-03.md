---
schema: qual/card@1
id: P-UCLARA18S-03
kind: problem
title: $L^1$ functions with finite energy $\iint\frac{\abs{f(x)f(y)}}{\abs{x-y}^2}$ vanish
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
Problem 3. Suppose $f\in L^1(\RR)$ satisfies
$$
\limsup_{\varepsilon\to0}\int_{\RR}\int_{\RR}
\frac{\abs{f(x)f(y)}}{\abs{x-y}^2+\varepsilon^2}\,dx\,dy<\infty.
$$
Show that $f=0$ almost everywhere.
:::

::: {.solution}

For $\varepsilon>0$, set
$$
I_\varepsilon
=
\int_{\RR}\int_{\RR}
\frac{\abs{f(x)f(y)}}
{\abs{x-y}^2+\varepsilon^2}
\,dx\,dy.
$$

::: pf

::: {.pf-step #s1-1}

Along any sequence $\varepsilon_n\downarrow0$, the integrands
$$
\frac{\abs{f(x)f(y)}}
{\abs{x-y}^2+\varepsilon_n^2}
$$
increase pointwise almost everywhere to
$$
\frac{\abs{f(x)f(y)}}{\abs{x-y}^2}.
$$


::: pf-proof

For fixed $(x,y)$ with $x\ne y$, the denominator decreases to
$\abs{x-y}^2$ as $\varepsilon_n\downarrow0$. The diagonal
$$
\{(x,x):x\in\RR\}
$$
has two-dimensional Lebesgue measure zero, so its value is irrelevant for
the double integral.

:::

:::

::: {.pf-step #s1-2}

The hypothesis implies
$$
\boxed{
\int_{\RR}\int_{\RR}
\frac{\abs{f(x)f(y)}}{\abs{x-y}^2}\,dx\,dy
<\infty}.
$$


::: pf-proof

Choose, for example,
$$
\varepsilon_n=\frac1n.
$$
Because
$$
\limsup_{\varepsilon\to0}I_\varepsilon<\infty,
$$
the sequence $(I_{\varepsilon_n})$ is bounded for all sufficiently large
$n$. By step [](#s1-1){.pf-ref} and the monotone convergence theorem,
$$
\begin{aligned}
\int_{\RR^2}
\frac{\abs{f(x)f(y)}}{\abs{x-y}^2}\,dx\,dy
&=
\lim_{n\to\infty}
I_{\varepsilon_n}
<\infty.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Suppose, toward a contradiction, that $f$ does not vanish almost
everywhere. Then there exists a Lebesgue point $a$ of $\abs{f}$ such that
$$
\abs{f(a)}>0.
$$


::: pf-proof

If $f$ is not zero almost everywhere, then
$$
E=\{x:\abs{f(x)}>0\}
$$
has positive measure. Since $\abs{f}\in L^1(\RR)$, the Lebesgue
differentiation theorem says that almost every point is a Lebesgue point of
$\abs{f}$. Hence $E$ contains such a point $a$.

:::

:::

::: {.pf-step #s1-4}

For every $r>0$,
$$
\int_{a-r}^{a+r}\int_{a-r}^{a+r}
\frac{\abs{f(x)f(y)}}{\abs{x-y}^2}\,dx\,dy
\ge
\left(
\frac1{2r}
\int_{a-r}^{a+r}\abs{f(t)}\,dt
\right)^2.
$$


::: pf-proof

If
$$
x,y\in[a-r,a+r],
$$
then
$$
\abs{x-y}\le2r.
$$
Thus, off the diagonal,
$$
\frac1{\abs{x-y}^2}
\ge
\frac1{(2r)^2}.
$$
Since the integrand is nonnegative, Tonelli's theorem gives
$$
\begin{aligned}
\int_{a-r}^{a+r}\int_{a-r}^{a+r}
\frac{\abs{f(x)f(y)}}{\abs{x-y}^2}\,dx\,dy
&\ge
\frac1{4r^2}
\int_{a-r}^{a+r}\int_{a-r}^{a+r}
\abs{f(x)}\abs{f(y)}\,dx\,dy\\
&=
\frac1{4r^2}
\left(
\int_{a-r}^{a+r}\abs{f(t)}\,dt
\right)^2,
\end{aligned}
$$
which is the stated bound.

:::

:::

::: {.pf-step #s1-5}

The right-hand side in step [](#s1-4){.pf-ref} tends to
$$
\abs{f(a)}^2>0
\qquad(r\downarrow0).
$$


::: pf-proof

Because $a$ is a Lebesgue point of $\abs{f}$,
$$
\frac1{2r}
\int_{a-r}^{a+r}\abs{f(t)}\,dt
\longrightarrow
\abs{f(a)}.
$$
Square both sides.

:::

:::

::: {.pf-step #s1-6}

The left-hand side in step [](#s1-4){.pf-ref} tends to $0$ as $r\downarrow0$.


::: pf-proof

By step [](#s1-2){.pf-ref}, the nonnegative function
$$
G(x,y)
=
\frac{\abs{f(x)f(y)}}{\abs{x-y}^2}
$$
belongs to $L^1(\RR^2)$. The squares
$$
[a-r,a+r]^2
$$
have two-dimensional measure
$$
4r^2\longrightarrow0.
$$
Absolute continuity of the Lebesgue integral for the integrable function
$G$ therefore gives
$$
\int_{[a-r,a+r]^2}G(x,y)\,dx\,dy
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-7}

Steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} give a contradiction.


::: pf-proof

Step [](#s1-4){.pf-ref} says the left-hand side is at least the right-hand side for every
$r>0$. Step [](#s1-6){.pf-ref} says the left-hand side tends to $0$, whereas step [](#s1-5){.pf-ref}
says the right-hand side tends to the strictly positive number
$\abs{f(a)}^2$.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{f=0\quad\text{almost everywhere}}.
$$


::: pf-proof

The contrary assumption in step [](#s1-3){.pf-ref} leads to the contradiction in step
[](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
