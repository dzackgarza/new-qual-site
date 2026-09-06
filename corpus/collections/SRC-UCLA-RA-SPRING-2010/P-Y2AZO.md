---
schema: qual/card@1
id: P-Y2AZO
kind: problem
title: The Hardy–Littlewood weak-type $(1,1)$ inequality
classification:
  areas:
  - real-analysis
  topics:
  - Maximal Functions
  - Measure Theory
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against problem 3 of the UCLA Analysis Qualifying Exam, Spring 2010, from the collection provenance PDF; the UCLA solution compilation refers this problem to Fall 2011 problem 5.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Replaced the prior covering argument. Its final constant was off by a factor of two, and its greedy extraction did not justify the uncountable-family selection. The revised proof first shows the maximal level set is open, proves a finite interval covering lemma by selecting a longest remaining interval, applies it to finite covers of compact subsets, and exhausts the level set. This gives the valid constant A=3.
---

::: {.problem}
For $f:\mathbb{R}\to\mathbb{R}$ in $L^1(\mathbb{R})$, let $Mf$ be the (centered) Hardy-Littlewood maximal function.
Prove there is a constant $A$ such that for any $\lambda>0$, $$m\{x\in\mathbb{R}: Mf(x)>\lambda\} \le \frac{A}{\lambda}||f||_{L^1}$$ where $m$ is Lebesgue measure.
If you use a covering lemma, you should prove it.
:::

::: {.solution}
Write
\[
Mf(x)=\sup_{r>0}\frac1{2r}\int_{x-r}^{x+r}|f(t)|\,dt
\]
and, for $\lambda>0$, set
\[
E_\lambda=\{x\in\mathbb R:Mf(x)>\lambda\}.
\]

<1>1. The set $E_\lambda$ is open.
::: {.proof}
Fix $x\in E_\lambda$.
Choose $r>0$ such that
\[
\frac1{2r}\int_{x-r}^{x+r}|f(t)|\,dt>\lambda.
\]
Define
\[
F(s)=\int_{-\infty}^{s}|f(t)|\,dt.
\]
Because $f\in L^1(\mathbb R)$, the function $F$ is continuous.
Hence
\[
y\longmapsto \int_{y-r}^{y+r}|f(t)|\,dt
=F(y+r)-F(y-r)
\]
is continuous.
It is strictly larger than $2r\lambda$ at $y=x$, so it remains larger than $2r\lambda$ for all $y$ in some neighborhood of $x$.
For such $y$,
\[
Mf(y)\ge\frac1{2r}\int_{y-r}^{y+r}|f(t)|\,dt>\lambda.
\]
Thus a neighborhood of $x$ lies in $E_\lambda$.
:::

<1>2. Finite interval covering lemma: if $\mathcal F$ is a finite family of bounded intervals, then there are pairwise disjoint intervals $I_1,\ldots,I_N\in\mathcal F$ such that
\[
\bigcup_{I\in\mathcal F}I
\subseteq
\bigcup_{j=1}^N 3I_j,
\]
where $3I_j$ denotes the interval with the same center as $I_j$ and three times its length.
::: {.proof}
Choose from $\mathcal F$ an interval $I_1$ of maximal length.
Delete $I_1$ and every interval of $\mathcal F$ that meets $I_1$.
If any intervals remain, choose among them one of maximal length, call it $I_2$, and again delete it together with every remaining interval that meets it.
Continue until no interval remains.
Because $\mathcal F$ is finite, this process stops after finitely many steps.
By construction the selected intervals $I_1,\ldots,I_N$ are pairwise disjoint.

Let $J\in\mathcal F$.
At the stage when $J$ was deleted, it either was itself selected or it met a selected interval $I_j$ with
\[
|J|\le |I_j|,
\]
because $I_j$ had maximal length among the intervals then remaining.
Let $c_J,c_j$ be the centers of $J,I_j$ and put $L=|I_j|$.
Since $J$ meets $I_j$,
\[
|c_J-c_j|\le\frac{|J|+L}{2}\le L.
\]
For every $y\in J$,
\[
|y-c_j|
\le |y-c_J|+|c_J-c_j|
\le\frac{|J|}{2}+L
\le\frac{3L}{2}.
\]
Thus $J\subseteq3I_j$.
This holds for every $J\in\mathcal F$, proving the lemma.
:::

<1>3. Every compact set $K\subseteq E_\lambda$ satisfies
\[
m(K)\le\frac{3}{\lambda}\|f\|_{L^1}.
\]
::: {.proof}
For every $x\in K$, choose $r_x>0$ such that the centered interval
\[
I_x=(x-r_x,x+r_x)
\]
satisfies
\[
\frac1{|I_x|}\int_{I_x}|f(t)|\,dt>\lambda.
\]
The intervals $I_x$ form an open cover of the compact set $K$, so finitely many of them, say
\[
J_1,\ldots,J_M,
\]
still cover $K$.
Apply <1>2 to this finite family.
We obtain pairwise disjoint intervals
\[
I_1,\ldots,I_N
\]
among the $J_i$ such that
\[
K\subseteq\bigcup_{j=1}^N3I_j.
\]
Therefore
\[
\begin{aligned}
m(K)
&\le \sum_{j=1}^N|3I_j|\\
&=3\sum_{j=1}^N|I_j|\\
&<\frac3\lambda\sum_{j=1}^N\int_{I_j}|f(t)|\,dt\\
&\le\frac3\lambda\|f\|_{L^1}.
\end{aligned}
\]
The last inequality uses the pairwise disjointness of the selected intervals.
:::

<1>4. One has
\[
m(E_\lambda)\le\frac{3}{\lambda}\|f\|_{L^1}.
\]
::: {.proof}
Since $E_\lambda$ is open by <1>1, define
\[
K_n=\left\{x\in E_\lambda:
|x|\le n,
\ \operatorname{dist}(x,E_\lambda^c)\ge\frac1n
\right\}.
\]
Each $K_n$ is closed and bounded, hence compact.
The sets are increasing and
\[
\bigcup_{n=1}^{\infty}K_n=E_\lambda:
\]
indeed, every point of the open set $E_\lambda$ has positive distance from its complement and finite absolute value.
By continuity of Lebesgue measure from below and <1>3,
\[
\begin{aligned}
m(E_\lambda)
&=\lim_{n\to\infty}m(K_n)\\
&\le\frac3\lambda\|f\|_{L^1}.
\end{aligned}
\]
Thus the desired weak-type $(1,1)$ estimate holds with $A=3$.
:::
:::
