---
schema: qual/card@1
id: P-TIE-F15-04
kind: problem
title: Limit of integrals over vertical segments when $f(x+iy)\to A$ uniformly
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 4.
---

::: {.problem}
Assume $f$ is continuous in the region $x \geq x_{0}$, $0 \leq y \leq b$ and the limit
$$
\lim_{x \to +\infty} f(x + iy) = A
$$
exists uniformly with respect to $y$ (independent of $y$). Show that
$$
\lim_{x \to +\infty} \int_{\gamma_{x}} f(z) \, dz = iAb,
$$
where $\gamma_{x} \coloneqq \{z \st z = x + it,\ 0 \leq t \leq b\}$.
:::

::: {.solution}

Parametrize the vertical segment by
$$
\gamma_x(t)=x+it,
\qquad
0\le t\le b.
$$

::: pf

::: {.pf-step #s1-1}

For every $x\ge x_0$,
$$
\int_{\gamma_x}f(z)\,dz
=
i\int_0^b f(x+it)\,dt.
$$


::: pf-proof

Along the parametrization,
$$
d\gamma_x(t)=i\,dt.
$$
Substitution into the contour integral gives the stated identity.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\abs{
\int_{\gamma_x}f(z)\,dz-iAb
}
\le
b
\sup_{0\le t\le b}
\abs{f(x+it)-A}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\begin{aligned}
\int_{\gamma_x}f(z)\,dz-iAb
&=
i\int_0^b\left(f(x+it)-A\right)dt.
\end{aligned}
$$
Therefore
$$
\begin{aligned}
\abs{
\int_{\gamma_x}f(z)\,dz-iAb
}
&\le
\int_0^b\abs{f(x+it)-A}\,dt\\
&\le
b
\sup_{0\le t\le b}
\abs{f(x+it)-A}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\lim_{x\to+\infty}
\int_{\gamma_x}f(z)\,dz
=
iAb.
}
$$


::: pf-proof

The hypothesis says precisely that
$$
\sup_{0\le t\le b}
\abs{f(x+it)-A}
\longrightarrow0
$$
as $x\to+\infty$. The estimate in step [](#s1-2){.pf-ref} therefore forces the difference between the contour integral and $iAb$ to tend to $0$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required limit.

:::

:::

:::
