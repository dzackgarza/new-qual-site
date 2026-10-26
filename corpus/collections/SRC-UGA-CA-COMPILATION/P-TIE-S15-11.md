---
schema: qual/card@1
id: P-TIE-S15-11
kind: problem
title: Sup norm on a smaller disk bounded by the $L^1$ norm for holomorphic functions
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 11.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Repaired the garbled norm notation and the stray subscript on r, and moved the Stein note to a remark, against Spring 2015, question 11, page 12 of Questions_from_Tie.pdf (read from the page image).
---

::: {.problem}
Let $f$ be holomorphic in a neighborhood of $D_r(z_0)$. Show that for any $s < r$, there exists a constant $c > 0$ such that
$$
\norm{f}_{(\infty,s)} \le c\norm{f}_{(1,r)},
$$
where $\norm{f}_{(\infty,s)} = \sup_{z\in D_s(z_0)} \abs{f(z)}$ and $\norm{f}_{(1,r)} = \int_{D_r(z_0)} \abs{f(z)}\,dx\,dy$.
:::

::: {.remark}
The source adds "Note: Exercise 3.8.20 on p.107 in Stein et al is a straightforward consequence of this stronger result using the integral form of the Cauchy-Schwarz inequality in real analysis.", a pointer to Stein and Shakarchi, *Complex Analysis*; the statement does not depend on it.
:::

Set
$$
\rho\coloneqq r-s>0.
$$

::: pf

::: pf-step

If $z\in D_s(z_0)$, then
$$
D_\rho(z)\subset D_r(z_0).
$$


::: pf-proof

Let $w\in D_\rho(z)$. Then
$$
\abs{w-z_0}
\le
\abs{w-z}+\abs{z-z_0}
<
\rho+s
=
r.
$$
Thus $w\in D_r(z_0)$.

:::

:::

::: pf-step

For every $z\in D_s(z_0)$ and every $0<t<\rho$,
$$
\abs{f(z)}
\le
\frac1{2\pi}
\int_0^{2\pi}
\abs{f(z+te^{i\theta})}\,d\theta.
$$


::: pf-proof

By step <1>1, the closed circle
$$
\abs{w-z}=t
$$
lies in $D_r(z_0)$, where $f$ is holomorphic. Cauchy's integral formula gives
$$
f(z)
=
\frac1{2\pi}
\int_0^{2\pi}
f(z+te^{i\theta})\,d\theta.
$$
Taking absolute values yields the estimate.

:::

:::

::: pf-step

For every $z\in D_s(z_0)$,
$$
\abs{f(z)}
\le
\frac1{\pi\rho^2}
\int_{D_\rho(z)}
\abs{f(w)}\,dA(w).
$$


::: pf-proof

Multiply the inequality in step <1>2 by $2t$ and integrate from $t=0$ to $t=\rho$:
$$
\abs{f(z)}
\int_0^\rho 2t\,dt
\le
\frac1\pi
\int_0^\rho
\int_0^{2\pi}
\abs{f(z+te^{i\theta})}
t\,d\theta\,dt.
$$
Since
$$
\int_0^\rho2t\,dt=\rho^2,
$$
and the double integral on the right is the polar-coordinate expression for
$$
\int_{D_\rho(z)}\abs{f(w)}\,dA(w),
$$
division by $\rho^2$ gives the claimed estimate.

:::

:::

::: pf-step

For every $z\in D_s(z_0)$,
$$
\abs{f(z)}
\le
\frac1{\pi(r-s)^2}
\norm{f}_{(1,r)}.
$$


::: pf-proof

By step <1>1,
$$
D_\rho(z)\subset D_r(z_0).
$$
Hence step <1>3 gives
$$
\begin{aligned}
\abs{f(z)}
&\le
\frac1{\pi\rho^2}
\int_{D_\rho(z)}
\abs{f(w)}\,dA(w)\\
&\le
\frac1{\pi\rho^2}
\int_{D_r(z_0)}
\abs{f(w)}\,dA(w).
\end{aligned}
$$
Since $\rho=r-s$, this is the stated inequality.

:::

:::

::: pf-step

Therefore
$$
\boxed{
\norm{f}_{(\infty,s)}
\le
\frac1{\pi(r-s)^2}
\norm{f}_{(1,r)}.
}
$$


::: pf-proof

Take the supremum of the pointwise estimate in step <1>4 over all $z\in D_s(z_0)$.

:::

:::

::: pf-qed

Step <1>5 proves the assertion with
$$
\boxed{c=\frac1{\pi(r-s)^2}>0}.
$$

:::

:::
