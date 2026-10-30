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
   $$
   \Lambda(f)=\int_0^1 f(x)\overline{g(x)}\,dx
   \qquad(f\in L^2([0,1])).
   $$

   (b) Prove that $g\in L^\infty([0,1])$, that the same formula holds for every $f\in L^1([0,1])$, and that
   $$
   \norm{g}_\infty=\norm{\Lambda}_{(L^1)^*}.
   $$
:::

::: {.solution}

::: pf

::: pf-step
Inclusion and density.

::: pf-proof
By Cauchy--Schwarz,
$$
\norm{f}_1
=\int_0^1\abs{f}\cdot1
\le \norm{f}_2\norm{1}_2
=\norm{f}_2.
$$
Hence $L^2\subseteq L^1$ continuously.

Bounded measurable functions lie in $L^2([0,1])$, and bounded simple functions are dense in $L^1([0,1])$. Therefore $L^2([0,1])$ is dense in $L^1([0,1])$.
:::

:::

::: pf-step
Restrict $\Lambda$ to $L^2$ and apply Riesz.

::: pf-proof
For $f\in L^2$,
$$
\abs{\Lambda(f)}\le \norm{\Lambda}\,\norm{f}_1
\le \norm{\Lambda}\,\norm{f}_2.
$$
Thus $\Lambda\restrict_{L^2}$ is a bounded linear functional on the Hilbert space $L^2([0,1])$. By the Riesz representation theorem, there is a unique $g\in L^2([0,1])$ such that
$$
\Lambda(f)=\int_0^1 f\overline g
\qquad(f\in L^2).
$$
:::

:::

::: {.pf-step #g-in-linfty}
Prove that $g\in L^\infty$ and $\norm{g}_\infty\le\norm{\Lambda}$.

::: pf-proof
Let $M:=\norm{\Lambda}$. Suppose for contradiction that
$$
m(E)>0,
\qquad
E:=\{x:\abs{g(x)}>M+\varepsilon\}
$$
for some $\varepsilon>0$. Since $E\subset[0,1]$, the function
$$
h(x):=\frac{1}{m(E)}\frac{g(x)}{\abs{g(x)}}\mathbf1_E(x)
$$
belongs to both $L^1$ and $L^2$, and $\norm{h}_1=1$. Using the $L^2$ representation,
$$
\begin{aligned}
\abs{\Lambda(h)}
&=\abs{\frac1{m(E)}\int_E \abs{g(x)}\,dx}\\
&>M+\varepsilon,
\end{aligned}
$$
contradicting $\abs{\Lambda(h)}\le M\norm{h}_1=M$. Hence
$$
\abs{g}\le M\quad\text{a.e.},
$$
so $g\in L^\infty$ and
$$
\norm{g}_\infty\le\norm{\Lambda}.
$$
:::

:::

::: pf-step
Extend the representation to every $L^1$ function.

::: pf-proof
Let $f\in L^1$. Choose $f_n\in L^2$ with
$$
\norm{f_n-f}_1\to0.
$$
Continuity of $\Lambda$ gives
$$
\Lambda(f_n)\to\Lambda(f).
$$
Since $g\in L^\infty$,
$$
\abs{\int (f_n-f)\overline g}
\le \norm{f_n-f}_1\norm{g}_\infty\to0.
$$
Therefore
$$
\Lambda(f)=\int_0^1 f\overline g
$$
for every $f\in L^1$.
:::

:::

::: pf-step
Prove equality of the norms.

::: pf-proof
The representation and Hölder's inequality give
$$
\abs{\Lambda(f)}\le\norm{f}_1\norm{g}_\infty,
$$
so
$$
\norm{\Lambda}\le\norm{g}_\infty.
$$
Combined with Step [](#g-in-linfty){.pf-ref},
$$
\norm{g}_\infty\le\norm{\Lambda},
$$
we obtain
$$
\boxed{\norm{g}_\infty=\norm{\Lambda}.}
$$
:::

:::

:::

:::
