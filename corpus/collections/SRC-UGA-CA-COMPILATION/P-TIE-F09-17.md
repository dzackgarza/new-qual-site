---
schema: qual/card@1
id: P-TIE-F09-17
kind: problem
title: Limit of integrals over small circular arcs when $(z-a)f(z)\to A$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 17.
---

::: {.problem}
Assume f is continuous in the region: $0 < \abs{ z - a } \leq R , \ 0 \leq \arg ( z - a ) \leq \beta _ { 0 } \ ( 0 < \beta _ { 0 } \leq 2 \pi )$and the limit$\operatorname* { l i m } _ { z \to a } ( z - a ) f ( z ) = A$ exists.
Show that

$$
\operatorname * { l i m } _ { r  0 } \int _ { \gamma _ { r } } f ( z ) d z = i A \beta _ { 0 } \ ,
$$

where $\gamma _ { r } : = \lbrace z \mid z = a + r e ^ { i t } , 0 \leq t \leq \beta _ { 0 } \rbrace$
:::

::: {.solution}

Parametrize
$$
\gamma_r(t)=a+re^{it},
\qquad
0\le t\le\beta_0.
$$

::: pf

::: {.pf-step #s1-1}

For every $0<r\le R$,
$$
\int_{\gamma_r}f(z)\,dz
=
i\int_0^{\beta_0}
(\gamma_r(t)-a)f(\gamma_r(t))\,dt.
$$


::: pf-proof

Since
$$
\gamma_r'(t)=ire^{it}=i(\gamma_r(t)-a),
$$
the definition of the contour integral gives
$$
\begin{aligned}
\int_{\gamma_r}f(z)\,dz
&=
\int_0^{\beta_0}f(\gamma_r(t))\gamma_r'(t)\,dt\\
&=
i\int_0^{\beta_0}
(\gamma_r(t)-a)f(\gamma_r(t))\,dt.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

For every $\varepsilon>0$, there is $\delta>0$ such that
$$
\abs{
(\gamma_r(t)-a)f(\gamma_r(t))-A
}
<\varepsilon
$$
whenever $0<r<\delta$ and $0\le t\le\beta_0$.


::: pf-proof

The hypothesis
$$
\lim_{\substack{z\to a\\ z\text{ in the sector}}}(z-a)f(z)=A
$$
means that for every $\varepsilon>0$ there is $\delta>0$ such that
$$
\abs{(z-a)f(z)-A}<\varepsilon
$$
throughout the sector whenever $0<\abs{z-a}<\delta$. Since
$$
\abs{\gamma_r(t)-a}=r,
$$
the estimate holds simultaneously for every $t\in[0,\beta_0]$ once $r<\delta$.

:::

:::

::: {.pf-step #s1-3}

For $0<r<\delta$,
$$
\abs{
\int_{\gamma_r}f(z)\,dz-iA\beta_0
}
\le
\beta_0\varepsilon.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\int_{\gamma_r}f(z)\,dz-iA\beta_0
=
i\int_0^{\beta_0}
\left(
(\gamma_r(t)-a)f(\gamma_r(t))-A
\right)dt.
$$
Taking absolute values and applying step [](#s1-2){.pf-ref} gives
$$
\abs{
\int_{\gamma_r}f(z)\,dz-iA\beta_0
}
\le
\int_0^{\beta_0}\varepsilon\,dt
=
\beta_0\varepsilon.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\lim_{r\to0}
\int_{\gamma_r}f(z)\,dz
=
iA\beta_0
}.
$$


::: pf-proof

Given $\eta>0$, use step [](#s1-3){.pf-ref} with
$$
\varepsilon=\frac{\eta}{\beta_0}.
$$
Then the difference from $iA\beta_0$ is smaller than $\eta$ for all sufficiently small
$r>0$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required limit.

:::

:::

:::
