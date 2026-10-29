---
schema: qual/card@1
id: P-ROMKF
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
---

::: {.problem}
Let $a_n \neq 0$ and assume that $\displaystyle
\lim_{n \rightarrow \infty} \frac{|a_{n+1}|}{|a_n|} = L$. Show that
$\displaystyle
\lim_{n \rightarrow \infty}
\sqrt[n]{|a_n|} = L.$ In particular, this shows that when
applicable, the ratio test can be used to calculate the radius of
convergence of a power series.
:::

::: {.solution}
Here $0\le L\le\infty$. Write $r_k\coloneqq\abs{a_{k+1}}/\abs{a_k}$, so $r_k\to L$.

::: pf

::: {.pf-step #upper}

If $L<\infty$, then $\limsup_{n\to\infty}\abs{a_n}^{1/n}\le L$.

::: pf-proof

Let $q>L$. There is $K$ with $r_k<q$ for $k\ge K$, so $\abs{a_n}\le\abs{a_K}q^{n-K}$ for $n\ge K$. Hence
$$
\abs{a_n}^{1/n}\le\bigl(\abs{a_K}q^{-K}\bigr)^{1/n}q\longrightarrow q.
$$
Since $q>L$ is arbitrary, the claim follows.

:::

:::

::: {.pf-step #lower}

If $L>0$, then $\liminf_{n\to\infty}\abs{a_n}^{1/n}\ge L$.

::: pf-proof

Let $0<p<L$. There is $K$ with $r_k>p$ for $k\ge K$, so $\abs{a_n}\ge\abs{a_K}p^{n-K}$ for $n\ge K$. Hence
$$
\abs{a_n}^{1/n}\ge\bigl(\abs{a_K}p^{-K}\bigr)^{1/n}p\longrightarrow p.
$$
Since $p<L$ is arbitrary, the claim follows.

:::

:::

::: pf-step

$\boxed{\lim_{n\to\infty}\abs{a_n}^{1/n}=L}$.

::: pf-proof

If $0<L<\infty$, steps [](#upper){.pf-ref} and [](#lower){.pf-ref} together give the limit. If $L=0$, step [](#upper){.pf-ref} gives $\limsup\abs{a_n}^{1/n}\le0$, and the terms are positive. If $L=\infty$, step [](#lower){.pf-ref} gives $\liminf\abs{a_n}^{1/n}=\infty$.

:::

:::

:::

:::
