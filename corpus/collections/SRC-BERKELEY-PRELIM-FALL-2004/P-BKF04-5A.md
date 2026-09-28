---
schema: qual/card@1
id: P-BKF04-5A
kind: problem
title: Fekete's lemma for subadditive sequences
classification:
  areas: [prelim]
  topics: []
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
If $n=\ell m+r$ for integers $m,\ell\geq1$ and $r\in[0,m)$, then $a_n=a_{\ell m+r}\leq a_{\ell m}+a_r\leq\ell a_m+a_r$, where $a_0\coloneqq0$ so that the case $r=0$ is included, and dividing by $n$ yields

$$
\frac{a_n}{n}\leq\frac{\ell m}{n}\frac{a_m}{m}+\frac{a_r}{n}.
$$

Fix $m$ and let $n\to\infty$, so that $\ell$ and $r$ vary with $n$. Then $\ell m/n\to1$, and $a_r/n\to0$ because $r$ takes only the values $0,\ldots,m-1$. We obtain

$$
\limsup_{n\to\infty}\frac{a_n}{n}\leq\frac{a_m}{m}.
$$

This holds for each $m$, so

$$
\limsup_{n\to\infty}\frac{a_n}{n}\leq\inf_m\frac{a_m}{m}.
$$

On the other hand,

$$
\liminf_{n\to\infty}\frac{a_n}{n}\geq\inf_m\frac{a_m}{m}
$$

holds by definition. Thus

$$
\lim_{n\to\infty}\frac{a_n}{n}=\inf_m\frac{a_m}{m}.
$$
:::
