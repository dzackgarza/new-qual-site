---
schema: qual/card@1
id: P-UCLAB05F-03
kind: problem
title: Uniform convergence and convergence of square integrals
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 of the official UCLA Basic Examination, September 2005 PDF.
---

::: {.problem}
(a) Let $f_j:[0,1]\to\RR$ be continuous functions converging uniformly on $[0,1]$ to a continuous function $F:[0,1]\to\RR$.
Prove that
\[
\int_0^1F(x)^2\,dx
=
\lim_{j\to\infty}\int_0^1f_j(x)^2\,dx.
\]

(b) Give a sequence of continuous functions $f_j:[0,1]\to\RR$ converging pointwise to a continuous function $F:[0,1]\to\RR$ such that
\[
\lim_{j\to\infty}\int_0^1f_j(x)^2\,dx
\]
exists but is not equal to
\[
\int_0^1F(x)^2\,dx.
\]
:::

::: {.solution}

::: pf

::: pf-step

The sequence $(f_j)$ is uniformly bounded for all sufficiently large $j$.


::: pf-proof

Since $F$ is continuous on the compact interval $[0,1]$, there is
\[
K=\|F\|_\infty<\infty.
\]
Uniform convergence gives $J$ such that
\[
\|f_j-F\|_\infty<1
\]
for $j\ge J$. Hence
\[
\|f_j\|_\infty
\le
\|F\|_\infty+\|f_j-F\|_\infty
<
K+1
\]
for all $j\ge J$.

:::

:::

::: {.pf-step #s1-2}

One has
\[
\|f_j^2-F^2\|_\infty\longrightarrow0.
\]


::: pf-proof

For $j\ge J$ and every $x\in[0,1]$,
\[
\begin{aligned}
|f_j(x)^2-F(x)^2|
&=
|f_j(x)-F(x)|\,|f_j(x)+F(x)|\\
&\le
\|f_j-F\|_\infty
\bigl(\|f_j\|_\infty+\|F\|_\infty\bigr)\\
&\le
(2K+1)\|f_j-F\|_\infty.
\end{aligned}
\]
Taking the supremum over $x$ gives
\[
\|f_j^2-F^2\|_\infty
\le
(2K+1)\|f_j-F\|_\infty\to0.
\]

:::

:::

::: {.pf-step #s1-3}

In part (a),
\[
\boxed{
\int_0^1F(x)^2\,dx
=
\lim_{j\to\infty}\int_0^1f_j(x)^2\,dx
}.
\]


::: pf-proof

By step [](#s1-2){.pf-ref},
\[
\begin{aligned}
\left|
\int_0^1f_j(x)^2\,dx
-
\int_0^1F(x)^2\,dx
\right|
&\le
\int_0^1|f_j(x)^2-F(x)^2|\,dx\\
&\le
\|f_j^2-F^2\|_\infty
\longrightarrow0.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-4}

For part (b), define $F=0$ and, for each positive integer $j$, define $f_j:[0,1]\to\RR$ by
\[
f_j(x)=
\begin{cases}
0,
&0\le x\le \frac1{2j},\\[2mm]
2j^{3/2}\left(x-\frac1{2j}\right),
&\frac1{2j}\le x\le\frac1j,\\[2mm]
2j^{3/2}\left(\frac3{2j}-x\right),
&\frac1j\le x\le\frac3{2j},\\[2mm]
0,
&\frac3{2j}\le x\le1.
\end{cases}
\]
Then every $f_j$ is continuous.


::: pf-proof

The four formulas agree at the three break points:
\[
f_j\left(\frac1{2j}\right)=0,
\qquad
f_j\left(\frac1j\right)=\sqrt j,
\qquad
f_j\left(\frac3{2j}\right)=0.
\]
Each piece is linear or constant, so $f_j$ is continuous on $[0,1]$.

:::

:::

::: {.pf-step #s1-5}

The sequence $f_j$ converges pointwise to $F=0$.


::: pf-proof

At $x=0$, every $f_j(0)=0$. Fix $x>0$. Since
\[
\frac3{2j}\to0,
\]
for all sufficiently large $j$ one has
\[
\frac3{2j}<x.
\]
Then $x$ lies outside the support
\[
\left[\frac1{2j},\frac3{2j}\right]
\]
of $f_j$, so $f_j(x)=0$. Thus $f_j(x)\to0$ for every $x\in[0,1]$.

:::

:::

::: {.pf-step #s1-6}

For every $j$,
\[
\int_0^1 f_j(x)^2\,dx=\frac13.
\]


::: pf-proof

By symmetry of the triangular graph about $x=1/j$,
\[
\begin{aligned}
\int_0^1f_j(x)^2\,dx
&=
2\int_{1/(2j)}^{1/j}
4j^3\left(x-\frac1{2j}\right)^2\,dx\\
&=
8j^3
\int_0^{1/(2j)}t^2\,dt\\
&=
8j^3\cdot\frac1{3(2j)^3}\\
&=
\frac13.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-7}

The example in steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} satisfies
\[
\lim_{j\to\infty}\int_0^1f_j(x)^2\,dx
=
\frac13
\ne
0
=
\int_0^1F(x)^2\,dx.
\]


::: pf-proof

Step [](#s1-6){.pf-ref} makes the left side constantly $1/3$, while $F=0$ makes the right side zero.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-7){.pf-ref} provides the counterexample required in part (b).

:::

:::

:::
