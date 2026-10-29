---
schema: qual/card@1
id: P-EHLPT
kind: problem
title: Liouville's theorem via $\lim_{R\to\infty}\int_{\abs{z}=R}\frac{f(z)}{(z-a)(z-b)}\,dz$
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Cauchy Integral Formula
  - Residues
  - Entire Functions
relations: []
review: draft
---

::: {.problem}
Let $f(z)$ be bounded and analytic in $\CC$. Let $a \neq b$ be any fixed complex numbers. Show that the following limit exists:
$$
\lim_{R \rightarrow \infty} \int_{\abs{z}=R} \frac{f(z)}{(z-a)(z-b)} dz
.$$

Use this to show that $f(z)$ must be a constant (Liouville's theorem).
:::

::: {.solution}

Let $\abs{f}\le M$ on $\CC$, and for $R>\max(\abs{a},\abs{b})$ let $I(R)\coloneqq\int_{\abs{z}=R}\frac{f(z)}{(z-a)(z-b)}\,dz$.

::: pf

::: {.pf-step #constant}
$I(R)=\frac{2\pi i}{a-b}(f(a)-f(b))$ for every $R>\max(\abs{a},\abs{b})$, so the limit exists.

::: pf-proof
By partial fractions, $\frac1{(z-a)(z-b)}=\frac1{a-b}\left(\frac1{z-a}-\frac1{z-b}\right)$, and Cauchy's integral formula gives $\int_{\abs{z}=R}\frac{f(z)}{z-c}\,dz=2\pi if(c)$ for $c\in\{a,b\}$.
:::

:::

::: {.pf-step #vanishes}
$I(R)\to0$ as $R\to\infty$.

::: pf-proof
On $\abs{z}=R$, $\abs{z-a}\ge R-\abs{a}$ and $\abs{z-b}\ge R-\abs{b}$, so $\abs{I(R)}\le\frac{2\pi RM}{(R-\abs{a})(R-\abs{b})}\to0$.
:::

:::

::: pf-step
$f$ is constant.

::: pf-proof
Steps [](#constant){.pf-ref} and [](#vanishes){.pf-ref} give $f(a)=f(b)$, and $a\ne b$ were arbitrary.
:::

:::

:::

:::
