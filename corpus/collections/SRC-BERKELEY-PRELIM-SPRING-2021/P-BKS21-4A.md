---
schema: qual/card@1
id: P-BKS21-4A
kind: problem
title: Schwarz lemma derivative bound at the origin
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2021 maximum-modulus argument for $g(z)=f(z)/z$. The proof is correct; the solution below makes the removable value $g(0)=f'(0)$ explicit.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified analyticity of the extended quotient, the radius-$r$ maximum-modulus estimate, and the limit $r\uparrow1$.
---

::: {.problem}
If $f$ is analytic from the unit disk into itself and $f(0)=0$, prove that
$$
|f'(0)|\le1.
$$
:::

Define
$$
g(z)=
\begin{cases}
\dfrac{f(z)}{z},&z\neq0,\\[4pt]
f'(0),&z=0.
\end{cases}
$$

::: pf

::: pf-step

The function $g$ is analytic on the unit disk.


::: pf-proof

Since $f$ is analytic and $f(0)=0$, its Taylor expansion at $0$ has the form
$$
f(z)=a_1z+a_2z^2+\cdots.
$$
Thus
$$
\frac{f(z)}{z}=a_1+a_2z+\cdots
$$
for $z\neq0$, and the removable value at $0$ is $a_1=f'(0)$. Hence the displayed definition extends $f(z)/z$ analytically across $0$.

:::

:::

::: pf-step

For every $0<r<1$,
$$
|g(0)|\leq\frac1r.
$$


::: pf-proof

On the circle $|z|=r$, the hypothesis that $f$ maps the unit disk into itself gives $|f(z)|<1$. Therefore
$$
|g(z)|=\frac{|f(z)|}{|z|}<\frac1r.
$$
By the maximum modulus principle applied to $g$ on the closed disk $|z|\leq r$,
$$
|g(0)|
\leq
\max_{|z|=r}|g(z)|
\leq
\frac1r.
$$

:::

:::

::: pf-step

One has
$$
\boxed{|f'(0)|\leq1}.
$$


::: pf-proof

By definition, $g(0)=f'(0)$. Step <1>2 holds for every $0<r<1$; letting $r\uparrow1$ gives
$$
|f'(0)|=|g(0)|\leq1.
$$

:::

:::

::: pf-qed

Step <1>3 is the required inequality.

:::

:::
