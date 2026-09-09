---
schema: qual/card@1
id: P-RASP22B
kind: problem
title: "Bounded sequence with vanishing local integrals against L^1 functions"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the official UCSD Spring 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $(f_n)_{n \in \mathbb{N}}$ be a sequence of Lebesgue measurable functions defined on $[0,1]$.
Assume there is a $C > 0$ such that $|f_n(x)| \leq C$ for almost every $x \in [0,1]$ and every $n$, and assume that $\lim_{n \to \infty} \int_0^a f_n(x)\,dx = 0$ for every $a \in (0,1)$.
Prove that
$$
\lim_{n \to \infty} \int_0^1 g(x) f_n(x)\,dx = 0
$$
for every function $g \in L^1([0,1])$.
:::


::: solution
First note that the hypothesis also implies
\[
\int_0^1 f_n(x)\,dx\longrightarrow0.
\]
Indeed, for any $a<1$,
\[
\left|\int_0^1f_n\right|
\le
\left|\int_0^af_n\right|+\left|\int_a^1f_n\right|
\le
\left|\int_0^af_n\right|+C(1-a).
\]
Taking $n\to\infty$ and then $a\uparrow1$ gives the claim.

Hence for every interval $(a,b)\subseteq[0,1]$,
\[
\int_a^bf_n
=\int_0^bf_n-\int_0^af_n
\longrightarrow0,
\]
where the endpoint cases follow from the preceding observation. Therefore, if $s$ is a step function, written as a finite linear combination of interval indicators, then
\[
\int_0^1s(x)f_n(x)\,dx\longrightarrow0.
\]

Now let $g\in L^1([0,1])$ and let $\varepsilon>0$. Choose a step function $s$ with
\[
\|g-s\|_1<\frac{\varepsilon}{2C}
\]
(if $C=0$, the conclusion is immediate). Since $|f_n|\le C$ a.e.,
\[
\left|\int_0^1(g-s)f_n\right|
\le C\|g-s\|_1
<\frac\varepsilon2
\]
for every $n$. For this fixed $s$, choose $N$ such that
\[
\left|\int_0^1s f_n\right|<\frac\varepsilon2
\]
whenever $n\ge N$. Then for $n\ge N$,
\[
\left|\int_0^1g f_n\right|
\le
\left|\int_0^1(g-s)f_n\right|
+
\left|\int_0^1s f_n\right|
<\varepsilon.
\]
Thus
\[
\boxed{\int_0^1g(x)f_n(x)\,dx\longrightarrow0}
\]
for every $g\in L^1([0,1])$.
:::
