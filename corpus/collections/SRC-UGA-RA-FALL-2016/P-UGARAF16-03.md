---
schema: qual/card@1
id: P-UGARAF16-03
kind: problem
title: Continuity of translation in $L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Density
relations: []
review: draft
---

::: {.problem}
Let $f\in L^1(\RR)$. Show that
$$
\lim_{x\to 0}\int_{\RR}\abs{f(y-x)-f(y)}\,dy=0.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $\varphi\in C_c(\RR)$, then $\int_\RR\abs{\varphi(y-x)-\varphi(y)}\,dy\to0$ as $x\to0$.

::: pf-proof

Let $\operatorname{supp}\varphi\subseteq[-R,R]$. For $\abs{x}\le1$, the integrand vanishes outside $[-R-1,R+1]$. A continuous function with compact support is uniformly continuous, so
$$
\omega(\delta):=\sup_{\abs{s-t}\le\delta}\abs{\varphi(s)-\varphi(t)}\longrightarrow0\qquad(\delta\downarrow0).
$$
Hence, for $\abs{x}\le1$,
$$
\int_\RR\abs{\varphi(y-x)-\varphi(y)}\,dy\le 2(R+1)\,\omega(\abs{x})\longrightarrow0.
$$

:::

:::

::: {.pf-step #s2}

For every $h\in L^1(\RR)$ and $x\in\RR$, $\int_\RR\abs{h(y-x)}\,dy=\norm{h}_1$.

::: pf-proof

Lebesgue measure is translation invariant, so the substitution $u=y-x$ preserves the integral of the nonnegative measurable function $\abs{h}$.

:::

:::

::: {.pf-step #s3}

For every $\varepsilon>0$ there is $\delta>0$ such that $\int_\RR\abs{f(y-x)-f(y)}\,dy<\varepsilon$ whenever $\abs{x}<\delta$.

::: pf-proof

Continuous functions with compact support are dense in $L^1(\RR)$, so there is $\varphi\in C_c(\RR)$ with $\norm{f-\varphi}_1<\varepsilon/3$. By the triangle inequality and step [](#s2){.pf-ref} applied to $h=f-\varphi$,
$$
\int_\RR\abs{f(y-x)-f(y)}\,dy
\le 2\norm{f-\varphi}_1+\int_\RR\abs{\varphi(y-x)-\varphi(y)}\,dy
<\frac{2\varepsilon}3+\int_\RR\abs{\varphi(y-x)-\varphi(y)}\,dy.
$$
By step [](#s1){.pf-ref} there is $\delta>0$ such that the last integral is less than $\varepsilon/3$ for $\abs{x}<\delta$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the definition of
$$
\lim_{x\to0}\int_\RR\abs{f(y-x)-f(y)}\,dy=0.
$$

:::

:::

:::
