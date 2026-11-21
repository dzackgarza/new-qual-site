---
schema: qual/card@1
id: P-BKF04-5A
kind: problem
title: Fekete's lemma for subadditive sequences
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
---

::: {.problem}
Let $(a_m)_{m\geq1}$ be a sequence of real numbers satisfying $a_{n+m}\leq a_n+a_m$. Prove that

$$
\lim_{n\to\infty}\frac{a_n}{n}=\inf_n\frac{a_n}{n}
$$

as an element of $[-\infty,\infty)$.
:::

::: {.solution}

The argument is the card's own: Fekete's subadditivity estimate bounds the limsup of $a_{n}/n$ by each $a_{m}/m$, and the liminf is bounded below by the infimum.

::: pf

::: {.pf-step #estimate}

With $a_{0}=0$ and $n=\ell m+r$, $0\le r<m$, $\ell\ge1$: $\displaystyle\frac{a_{n}}{n}\le\frac{\ell m}{n}\cdot\frac{a_{m}}{m}+\frac{a_{r}}{n}$.

::: pf-proof

Subadditivity iterated $\ell$ times gives $a_{\ell m}\le\ell a_{m}$, and then $a_{n}=a_{\ell m+r}\le a_{\ell m}+a_{r}\le\ell a_{m}+a_{r}$, with $a_{r}$ present only when $r\ge1$ — the convention $a_{0}=0$ covers $r=0$. Dividing by the positive $n$ and writing $\ell a_{m}/n=\frac{\ell m}{n}\cdot\frac{a_{m}}{m}$ gives the estimate.

:::

:::

::: {.pf-step #limsup}

$\displaystyle\limsup_{n\to\infty}\frac{a_{n}}{n}\le\frac{a_{m}}{m}$ for every $m\ge1$.

::: pf-proof

Fix $m$. For $n=\ell m+r$ we have $\ell=\frac{n-r}{m}$, hence $\frac{\ell m}{n}=1-\frac{r}{n}\to1$ as $n\to\infty$, since $0\le r<m$ is bounded. Also $\abs{a_{r}}\le M_{m}=\max\{\abs{a_{0}},\dots,\abs{a_{m-1}}\}$ for all $n$, so $a_{r}/n\to0$. Letting $n\to\infty$ along the full sequence in the inequality of step [](#estimate){.pf-ref} — the right side is a sum of a convergent family plus a null family — gives the claim.

:::

:::

::: {.pf-step #inf}

$\displaystyle\limsup_{n\to\infty}\frac{a_{n}}{n}\le\inf_{m}\frac{a_{m}}{m}\le\liminf_{n\to\infty}\frac{a_{n}}{n}$.

::: pf-proof

The first inequality holds because step [](#limsup){.pf-ref} bounds the limsup by every $a_{m}/m$, hence by their infimum. The second holds because $\inf_{m}a_{m}/m$ is a lower bound for every term $a_{n}/n$ (the index $n$ is one of the $m$), so it is at most every term, hence at most the liminf.

:::

:::

::: {.pf-step #conclusion}

$\displaystyle\lim_{n\to\infty}\frac{a_{n}}{n}=\inf_{n}\frac{a_{n}}{n}$ in $[-\infty,\infty)$.

::: pf-proof

Always $\liminf\le\limsup$. Step [](#inf){.pf-ref} gives $\limsup\le\inf\le\liminf$, so all three quantities coincide; in particular the limit exists in $[-\infty,\infty)$. Note $\inf_{n}a_{n}/n<+\infty$ since some term is finite, while the value $-\infty$ is allowed:
$$
\boxed{\lim_{n\to\infty}\frac{a_{n}}{n}=\inf_{n\ge1}\frac{a_{n}}{n}\in[-\infty,\infty).}
$$

:::

:::

:::

:::
