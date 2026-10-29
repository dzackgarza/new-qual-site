---
schema: qual/card@1
id: P-UCLARA17S-01
kind: problem
title: Averages of $L^\infty$ functions over a compact set are uniformly continuous
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $K\subset\RR$ be a compact set of positive measure and let $f\in L^\infty(\RR)$. Show that
\[
F(x)=\frac1{|K|}\int_K f(x+t)\,dt
\]
is uniformly continuous on $\RR$. Here $|K|$ denotes the Lebesgue measure of $K$.
:::

::: {.solution}

Let
$$
M\coloneqq\|f\|_{L^\infty(\RR)}.
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
|(K+h)\triangle K|\longrightarrow0
\qquad\text{as }h\to0.
$$


::: pf-proof

Let $\varepsilon>0$. By outer regularity of Lebesgue measure, choose an open set $U\supseteq K$ such that
$$
|U\setminus K|<\varepsilon.
$$
Since $K$ is compact and $U$ is open, there exists $\delta>0$ such that
$$
K+[-\delta,\delta]\subseteq U.
$$
Thus, if $|h|<\delta$, then $K+h\subseteq U$, so
$$
(K+h)\setminus K\subseteq U\setminus K
$$
and therefore
$$
|(K+h)\setminus K|<\varepsilon.
$$
Translation invariance gives $|K+h|=|K|$. Since both sets have finite measure,
$$
|(K+h)\setminus K|=|K\setminus(K+h)|.
$$
Hence
$$
|(K+h)\triangle K|<2\varepsilon.
$$
This proves the limit.

:::

:::

::: {.pf-step #s1-2}

For every $x,h\in\RR$,
$$
|F(x+h)-F(x)|
\le
\frac{M}{|K|}|(K+h)\triangle K|.
$$


::: pf-proof

By the change of variables $s=t+h$,
$$
F(x+h)=\frac1{|K|}\int_{K+h}f(x+s)\,ds.
$$
Therefore
$$
\begin{aligned}
|F(x+h)-F(x)|
&\le\frac1{|K|}
\int_{(K+h)\triangle K}|f(x+s)|\,ds\\
&\le\frac{M}{|K|}|(K+h)\triangle K|.
\end{aligned}
$$
The bound is independent of $x$.

:::

:::

::: {.pf-step #s1-3}

The function $F$ is uniformly continuous on $\RR$.


::: pf-proof

Let $\varepsilon>0$. By step [](#s1-1){.pf-ref}, choose $\delta>0$ such that
$$
|(K+h)\triangle K|
<\frac{\varepsilon|K|}{M+1}
$$
whenever $|h|<\delta$. Then step [](#s1-2){.pf-ref} gives, for every $x\in\RR$,
$$
|F(x+h)-F(x)|
\le\frac{M}{|K|}|(K+h)\triangle K|
<\varepsilon.
$$
Since the same $\delta$ works for every $x$, the continuity is uniform.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
