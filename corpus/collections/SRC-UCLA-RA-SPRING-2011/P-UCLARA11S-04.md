---
schema: qual/card@1
id: P-UCLARA11S-04
kind: problem
title: Uniform entropy integrability plus almost-everywhere convergence implies $L^1$ convergence
classification: {areas: [real-analysis], topics: []}
relations: []
review: draft
---

::: {.problem}
Let $f_n:[0,1]\to[0,\infty)$ be Borel functions satisfying
$$
\sup_n\int_0^1 f_n(x)\log(2+f_n(x))\,dx<\infty.
$$
Suppose $f_n\to f$ Lebesgue almost everywhere.
Show that $f\in L^1([0,1])$ and $f_n\to f$ in $L^1$.
:::

::: {.solution}

Choose $M<\infty$ such that
$$
\int_0^1
f_n(x)\log(2+f_n(x))\,dx
\le M
\qquad
(n\ge1).
$$

::: pf

::: {.pf-step #s1-1}

The limit function satisfies
$$
f\in L^1([0,1]).
$$


::: pf-proof

Since all functions are nonnegative, Fatou's lemma gives
$$
\int_0^1
f(x)\log(2+f(x))\,dx
\le
\liminf_{n\to\infty}
\int_0^1
f_n(x)\log(2+f_n(x))\,dx
\le M.
$$
Because
$$
\log(2+t)\ge\log2
\qquad
(t\ge0),
$$
one has
$$
\log2
\int_0^1f(x)\,dx
\le
M.
$$
Thus $f\in L^1([0,1])$.

:::

:::

::: {.pf-step #s1-2}

The family $(f_n)$ is uniformly integrable on $[0,1]$.


::: pf-proof

Fix $\varepsilon>0$. Choose $R>0$ so large that
$$
\frac{M}{\log(2+R)}
<
\frac\varepsilon2.
$$
If $E\subset[0,1]$ is measurable, then
$$
\begin{aligned}
\int_E f_n
&=
\int_{E\cap\{f_n\le R\}}f_n
+
\int_{E\cap\{f_n>R\}}f_n\\
&\le
R\setmeasure{E}
+
\frac1{\log(2+R)}
\int_{\{f_n>R\}}
f_n\log(2+f_n)\\
&\le
R\setmeasure{E}
+
\frac{M}{\log(2+R)}.
\end{aligned}
$$
Choose
$$
\delta
=
\frac{\varepsilon}{2R}.
$$
Then $\setmeasure{E}<\delta$ implies
$$
\int_E f_n<\varepsilon
$$
for every $n$.

:::

:::

::: {.pf-step #s1-3}

The limit function $f$ satisfies the same small-set estimate: for every $\varepsilon>0$ there is $\delta>0$ such that
$$
\setmeasure{E}<\delta
\quad\Longrightarrow\quad
\int_E f<\varepsilon.
$$


::: pf-proof

Take $\delta$ from step [](#s1-2){.pf-ref}. By Fatou's lemma applied on $E$,
$$
\int_Ef
\le
\liminf_{n\to\infty}
\int_Ef_n
\le
\varepsilon.
$$
If desired, start step [](#s1-2){.pf-ref} with $\varepsilon/2$ to obtain the strict inequality displayed here.

:::

:::

::: {.pf-step #s1-4}

For every $\varepsilon>0$, there is a measurable set $E\subset[0,1]$ such that
$$
\setmeasure{E}<\delta
$$
and
$$
f_n\longrightarrow f
$$
uniformly on $[0,1]\setminus E$, where $\delta$ is chosen as in steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}.


::: pf-proof

This is Egorov's theorem, since $[0,1]$ has finite measure and $f_n\to f$ almost everywhere.

:::

:::

::: {.pf-step #s1-5}

One has
$$
\norm{f_n-f}_1\longrightarrow0.
$$


::: pf-proof

Fix $\varepsilon>0$. Choose $\delta>0$ from steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} with $\varepsilon$ replaced by $\varepsilon/4$, and choose $E$ from step [](#s1-4){.pf-ref}.

Then
$$
\int_E f_n<\frac\varepsilon4,
\qquad
\int_E f<\frac\varepsilon4.
$$
On $E^c$, convergence is uniform, so for all sufficiently large $n$,
$$
\sup_{x\in E^c}\abs{f_n(x)-f(x)}
<
\frac\varepsilon2.
$$
Since $\setmeasure{E^c}\le1$,
$$
\begin{aligned}
\norm{f_n-f}_1
&\le
\int_{E^c}\abs{f_n-f}
+
\int_Ef_n
+
\int_Ef\\
&<
\frac\varepsilon2
+
\frac\varepsilon4
+
\frac\varepsilon4\\
&=
\varepsilon.
\end{aligned}
$$
Thus $f_n\to f$ in $L^1$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives $f\in L^1$, and step [](#s1-5){.pf-ref} gives the required $L^1$ convergence.

:::

:::

:::
