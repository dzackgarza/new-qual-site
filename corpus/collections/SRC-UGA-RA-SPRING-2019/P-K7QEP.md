---
schema: qual/card@1
id: P-K7QEP
kind: problem
title: $L^2([0,1])$ is dense in $L^1([0,1])$, and Riesz representation for $L^1([0,1])$
classification:
  areas:
  - real-analysis
  topics:
  - Riesz Representation
  - Lp Spaces
  - Density
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2019 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2019.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---


::: {.problem}
1. Show that $L^2([0,1])\subseteq L^1([0,1])$ and that $L^2([0,1])$ is dense in $L^1([0,1])$.

2. Let $\Lambda$ be a continuous linear functional on $L^1([0,1])$.

   (a) Using the Riesz representation theorem for $L^2([0,1])$, prove that there is $g\in L^2([0,1])$ such that
   \[
   \Lambda(f)=\int_0^1 f(x)\overline{g(x)}\,dx
   \qquad(f\in L^2([0,1])).
   \]

   (b) Prove that $g\in L^\infty([0,1])$, that the same formula holds for every $f\in L^1([0,1])$, and that
   \[
   \|g\|_\infty=\|\Lambda\|_{(L^1)^*}.
   \]
:::

::: {.solution}
<1>1. Inclusion and density.
::: {.proof}
By Cauchy--Schwarz,
\[
\|f\|_1
=\int_0^1|f|\cdot1
\le \|f\|_2\|1\|_2
=\|f\|_2.
\]
Hence $L^2\subseteq L^1$ continuously.

Bounded measurable functions lie in $L^2([0,1])$, and bounded simple functions are dense in $L^1([0,1])$. Therefore $L^2([0,1])$ is dense in $L^1([0,1])$.
:::

<1>2. Restrict $\Lambda$ to $L^2$ and apply Riesz.
::: {.proof}
For $f\in L^2$,
\[
|\Lambda(f)|\le \|\Lambda\|\,\|f\|_1
\le \|\Lambda\|\,\|f\|_2.
\]
Thus $\Lambda|_{L^2}$ is a bounded linear functional on the Hilbert space $L^2([0,1])$. By the Riesz representation theorem, there is a unique $g\in L^2([0,1])$ such that
\[
\Lambda(f)=\int_0^1 f\overline g
\qquad(f\in L^2).
\]
:::

<1>3. Prove that $g\in L^\infty$ and $\|g\|_\infty\le\|\Lambda\|$.
::: {.proof}
Let $M:=\|\Lambda\|$. Suppose for contradiction that
\[
m(E)>0,
\qquad
E:=\{x:|g(x)|>M+\varepsilon\}
\]
for some $\varepsilon>0$. Since $E\subset[0,1]$, the function
\[
h(x):=\frac{1}{m(E)}\frac{g(x)}{|g(x)|}\mathbf1_E(x)
\]
belongs to both $L^1$ and $L^2$, and $\|h\|_1=1$. Using the $L^2$ representation,
\[
\begin{aligned}
|\Lambda(h)|
&=\left|\frac1{m(E)}\int_E |g(x)|\,dx\right|\\
&>M+\varepsilon,
\end{aligned}
\]
contradicting $|\Lambda(h)|\le M\|h\|_1=M$. Hence
\[
|g|\le M\quad\text{a.e.},
\]
so $g\in L^\infty$ and
\[
\|g\|_\infty\le\|\Lambda\|.
\]
:::

<1>4. Extend the representation to every $L^1$ function.
::: {.proof}
Let $f\in L^1$. Choose $f_n\in L^2$ with
\[
\|f_n-f\|_1\to0.
\]
Continuity of $\Lambda$ gives
\[
\Lambda(f_n)\to\Lambda(f).
\]
Since $g\in L^\infty$,
\[
\left|\int (f_n-f)\overline g\right|
\le \|f_n-f\|_1\|g\|_\infty\to0.
\]
Therefore
\[
\Lambda(f)=\int_0^1 f\overline g
\]
for every $f\in L^1$.
:::

<1>5. Prove equality of the norms.
::: {.proof}
The representation and Hölder's inequality give
\[
|\Lambda(f)|\le\|f\|_1\|g\|_\infty,
\]
so
\[
\|\Lambda\|\le\|g\|_\infty.
\]
Combined with Step 3,
\[
\|g\|_\infty\le\|\Lambda\|,
\]
we obtain
\[
\boxed{\|g\|_\infty=\|\Lambda\|.}
\]
:::
:::
