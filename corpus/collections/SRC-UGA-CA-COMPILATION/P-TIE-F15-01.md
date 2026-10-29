---
schema: qual/card@1
id: P-TIE-F15-01
kind: problem
title: If $\lim_{n\to\infty}|a_{n+1}|/|a_n|=L$ then $\lim_{n\to\infty}|a_n|^{1/n}=L$
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Power Series
  - Sequences of Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 1.
---

::: {.problem}
Let $a_n \neq 0$ and assume that $\displaystyle \lim_{n \to \infty} \frac{\abs{a_{n+1}}}{\abs{a_n}} = L$. Show that $\displaystyle \lim_{n \to \infty} \sqrt[n]{\abs{a_n}} = L$. In particular, this shows that when applicable, the ratio test can be used to calculate the radius of convergence of a power series.
:::

::: {.solution}

Set
$$
b_n\coloneqq\abs{a_n}>0.
$$

::: pf

::: {.pf-step #s1-1}

Suppose first that $L>0$. For every $\varepsilon$ with $0<\varepsilon<L$, there exists $N$ such that for every $k\ge N$,
$$
L-\varepsilon
<
\frac{b_{k+1}}{b_k}
<
L+\varepsilon.
$$


::: pf-proof

This is exactly the definition of
$$
\frac{b_{n+1}}{b_n}\longrightarrow L.
$$

:::

:::

::: {.pf-step #s1-2}

Under the hypotheses of step [](#s1-1){.pf-ref}, for every $n>N$,
$$
b_N(L-\varepsilon)^{n-N}
<
b_n
<
b_N(L+\varepsilon)^{n-N}.
$$


::: pf-proof

Multiply the inequalities from step [](#s1-1){.pf-ref} for
$$
k=N,N+1,\ldots,n-1.
$$
The product of the middle ratios telescopes:
$$
\prod_{k=N}^{n-1}\frac{b_{k+1}}{b_k}
=
\frac{b_n}{b_N}.
$$
Multiplying by $b_N$ gives the stated bounds.

:::

:::

::: {.pf-step #s1-3}

If $L>0$, then
$$
\lim_{n\to\infty}b_n^{1/n}=L.
$$


::: pf-proof

Taking $n$th roots in step [](#s1-2){.pf-ref} gives
$$
b_N^{1/n}(L-\varepsilon)^{1-N/n}
<
b_n^{1/n}
<
b_N^{1/n}(L+\varepsilon)^{1-N/n}.
$$
As $n\to\infty$,
$$
b_N^{1/n}\to1,
\qquad
1-\frac{N}{n}\to1.
$$
Therefore
$$
L-\varepsilon
\le
\liminf_{n\to\infty}b_n^{1/n}
\le
\limsup_{n\to\infty}b_n^{1/n}
\le
L+\varepsilon.
$$
Since this holds for every $0<\varepsilon<L$, letting $\varepsilon\downarrow0$ yields the claimed limit.

:::

:::

::: {.pf-step #s1-4}

If $L=0$, then
$$
\lim_{n\to\infty}b_n^{1/n}=0.
$$


::: pf-proof

Let $\varepsilon>0$. Since $b_{n+1}/b_n\to0$, there exists $N$ such that
$$
\frac{b_{k+1}}{b_k}<\varepsilon
$$
for every $k\ge N$. Multiplying as in step [](#s1-2){.pf-ref} gives
$$
b_n<b_N\varepsilon^{n-N}.
$$
Hence
$$
b_n^{1/n}
<
b_N^{1/n}\varepsilon^{1-N/n}.
$$
Taking the limit superior gives
$$
\limsup_{n\to\infty}b_n^{1/n}\le\varepsilon.
$$
Since $\varepsilon>0$ is arbitrary and $b_n^{1/n}\ge0$, the limit is $0$.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\lim_{n\to\infty}\sqrt[n]{\abs{a_n}}=L.
}
$$


::: pf-proof

Step [](#s1-3){.pf-ref} proves the assertion when $L>0$, and step [](#s1-4){.pf-ref} proves it when $L=0$.

:::

:::

::: {.pf-step #s1-6}

If $\sum_{n=0}^\infty a_nz^n$ is a power series and the ratio limit is $L$, then its radius of convergence is
$$
\boxed{R=\frac1L}
$$
with the convention $1/0=\infty$.


::: pf-proof

For a fixed $z$,
$$
\frac{\abs{a_{n+1}z^{n+1}}}{\abs{a_nz^n}}
=
\abs{z}\frac{\abs{a_{n+1}}}{\abs{a_n}}
\longrightarrow
L\abs{z}.
$$
The ratio test gives absolute convergence when $L\abs{z}<1$ and divergence when $L\abs{z}>1$. Thus the boundary between the two regions is $\abs{z}=1/L$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves the required root limit, and step [](#s1-6){.pf-ref} gives the stated consequence for power-series radii of convergence.

:::

:::

:::
