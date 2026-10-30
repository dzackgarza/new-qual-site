---
schema: qual/card@1
id: P-WESRA16-B2
kind: problem
title: '$L^\\infty$ convergence on finite-measure support implies convergence of integrals'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Group B, problem B2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md. Flash drops the convergence arrows in the final sentence; the $L^\infty$ hypothesis and two displayed integrals determine the intended convergence.
---

::: {.problem}
Let $X\subset\RR^d$ be measurable with $\lambda(X)<\infty$.
Let $g,f_n$ be measurable with supports contained in $X$.
Prove that if
$$
f_n\to g\quad\text{in }L^\infty,
$$
then
$$
\int_{\RR^d}f_n\to\int_{\RR^d}g.
$$
:::

::: {.solution}

::: pf

::: pf-step

Each $f_n$ and $g$ is integrable on $\RR^d$.


::: pf-proof

Convergence in $L^\infty$ takes place in the normed space $L^\infty$, so $g$ and every $f_n$ have finite essential supremum. Since all supports are contained in $X$ and $\lambda(X)<\infty$,
$$
\int_{\RR^d}\abs{f_n}
=\int_X\abs{f_n}
\leq\lambda(X)\norm{f_n}_{L^\infty}<\infty,
$$
and similarly for $g$.

:::

:::

::: {.pf-step #s1-2}

For every $n$,
$$
\abs{\int_{\RR^d}f_n-\int_{\RR^d}g}
\leq
\lambda(X)\norm{f_n-g}_{L^\infty}.
$$


::: pf-proof

The function $f_n-g$ vanishes almost everywhere outside $X$. Therefore
$$
\begin{aligned}
\abs{\int_{\RR^d}f_n-\int_{\RR^d}g}
&=\abs{\int_X(f_n-g)}\\
&\leq\int_X\abs{f_n-g}\\
&\leq\lambda(X)\norm{f_n-g}_{L^\infty}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{\int_{\RR^d}f_n\longrightarrow\int_{\RR^d}g}.
$$


::: pf-proof

By hypothesis,
$$
\norm{f_n-g}_{L^\infty}\longrightarrow0.
$$
Multiplying by the finite constant $\lambda(X)$ and applying the estimate from step [](#s1-2){.pf-ref} gives the desired convergence.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
