---
schema: qual/card@1
id: P-TIE-F11-19
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2011, question 19.
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

For $0<r\le R$, parametrize $\gamma_r$ by
$$
z(t)=a+re^{it},
\qquad
0\le t\le\beta_0.
$$

::: pf

::: {.pf-step #s1-1}

The integral over $\gamma_r$ satisfies
$$
\int_{\gamma_r}f(z)\,dz
=
i\int_0^{\beta_0}
re^{it}f(a+re^{it})\,dt.
$$


::: pf-proof

Under the stated parametrization,
$$
dz=ire^{it}\,dt.
$$
Substitution gives
$$
\int_{\gamma_r}f(z)\,dz
=
\int_0^{\beta_0}
f(a+re^{it})ire^{it}\,dt,
$$
which is the asserted identity.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\lim_{r\to0^+}
\int_0^{\beta_0}
\left(
re^{it}f(a+re^{it})-A
\right)dt
=0.
$$


::: pf-proof

Since
$$
(z-a)f(z)\longrightarrow A
$$
as $z\to a$ within the given sector, for every $\varepsilon>0$ there exists $\delta>0$ such that
$$
\abs{(z-a)f(z)-A}
<
\frac{\varepsilon}{1+\beta_0}
$$
whenever $z$ lies in the sector and $0<\abs{z-a}<\delta$. If $0<r<\delta$, then every point $a+re^{it}$ on $\gamma_r$ satisfies this bound. Hence
$$
\begin{aligned}
\abs{
\int_0^{\beta_0}
\left(
re^{it}f(a+re^{it})-A
\right)dt
}
&\le
\int_0^{\beta_0}
\abs{
re^{it}f(a+re^{it})-A
}\,dt\\
&<
\frac{\beta_0}{1+\beta_0}\varepsilon
<\varepsilon.
\end{aligned}
$$
This proves the asserted limit.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\lim_{r\to0^+}
\int_{\gamma_r}f(z)\,dz
=
iA\beta_0.
}
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\int_{\gamma_r}f(z)\,dz-iA\beta_0
=
i\int_0^{\beta_0}
\left(
re^{it}f(a+re^{it})-A
\right)dt.
$$
The right-hand side tends to $0$ by step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required limit.

:::

:::

:::
