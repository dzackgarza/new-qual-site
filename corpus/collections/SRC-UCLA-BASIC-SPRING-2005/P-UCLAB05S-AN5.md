---
schema: qual/card@1
id: P-UCLAB05S-AN5
kind: problem
title: Convergence of Cesàro means and failure of the converse
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Analysis Problem 5 of the official UCLA Basic Exam, May 2005 PDF.
---

::: {.problem}
(a) Suppose
$$
\lim_{n\to\infty}a_n=A.
$$
Show that
$$
\lim_{N\to\infty}\frac1N\sum_{n=1}^N a_n=A.
$$

(b) Show by example that the converse is false.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Put
$$
b_n\coloneqq a_n-A.
$$
Then $b_n\to0$, and
$$
\frac1N\sum_{n=1}^N a_n-A
=\frac1N\sum_{n=1}^N b_n.
$$


::: pf-proof

The convergence $b_n\to0$ follows immediately from $a_n\to A$. Also,
$$
\frac1N\sum_{n=1}^N a_n-A
=\frac1N\sum_{n=1}^N(a_n-A)
=\frac1N\sum_{n=1}^N b_n.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
\frac1N\sum_{n=1}^N b_n\longrightarrow0.
$$


::: pf-proof

Let $\varepsilon>0$. Choose $N_0$ such that
$$
|b_n|<\frac\varepsilon2
$$
for every $n\ge N_0$. Set
$$
C\coloneqq\sum_{n=1}^{N_0-1}|b_n|.
$$
For $N\ge N_0$,
$$
\begin{aligned}
\left|\frac1N\sum_{n=1}^N b_n\right|
&\le
\frac1N\sum_{n=1}^{N_0-1}|b_n|
+\frac1N\sum_{n=N_0}^N|b_n|\\
&\le\frac CN+\frac\varepsilon2.
\end{aligned}
$$
Choose $N$ also large enough that $C/N<\varepsilon/2$. Then the displayed absolute value is less than $\varepsilon$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\lim_{N\to\infty}\frac1N\sum_{n=1}^N a_n=A.}
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the difference between the Cesàro mean and $A$ is the quantity in step [](#s1-2){.pf-ref}, which tends to $0$.

:::

:::

::: {.pf-step #s1-4}

The converse is false. For example, let
$$
\boxed{a_n=(-1)^n.}
$$


::: pf-proof

The sequence $(a_n)$ does not converge because its even terms equal $1$ and its odd terms equal $-1$. On the other hand,
$$
\sum_{n=1}^N(-1)^n
=
\begin{cases}
0,&N\text{ even},\\
-1,&N\text{ odd}.
\end{cases}
$$
Hence
$$
\left|\frac1N\sum_{n=1}^N(-1)^n\right|\le\frac1N\to0.
$$
Thus the Cesàro means converge although the original sequence does not.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-4){.pf-ref} gives the counterexample required in part (b).

:::

:::

:::
