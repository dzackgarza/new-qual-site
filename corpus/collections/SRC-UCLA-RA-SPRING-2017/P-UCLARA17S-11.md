---
schema: qual/card@1
id: P-UCLARA17S-11
kind: problem
title: $L^p$ harmonic functions on the plane vanish
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $1\le p<\infty$ and let $U(z)$ be harmonic on $\CC$ such that
$$
\iint_{\RR\times\RR}\abs{U(x+iy)}^p\,dx\,dy<\infty.
$$
Prove that $U(z)=0$ for all $z=x+iy\in\CC$.
:::

::: {.solution}

Let
$$
M\coloneqq\left(\iint_{\RR^2}\abs{U}^p\,dA\right)^{1/p}<\infty.
$$

::: pf

::: {.pf-step #s1-1}

For every $z_0\in\CC$ and every $R>0$,
$$
U(z_0)=\frac1{\pi R^2}\int_{B(z_0,R)}U(z)\,dA(z).
$$


::: pf-proof

This is the mean-value property for harmonic functions, applied to the disk $B(z_0,R)$. Since $U$ is harmonic on all of $\CC$, every radius $R>0$ is allowed.

:::

:::

::: {.pf-step #s1-2}

For every $z_0\in\CC$ and $R>0$,
$$
\abs{U(z_0)}\le \frac{M}{(\pi R^2)^{1/p}}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\abs{U(z_0)}
\le\frac1{\pi R^2}
\int_{B(z_0,R)}\abs{U(z)}\,dA(z).
$$
If $p>1$, Hölder's inequality with conjugate exponent $q=p/(p-1)$ gives
$$
\begin{aligned}
\int_{B(z_0,R)}\abs{U}
&\le
\left(\int_{B(z_0,R)}\abs{U}^p\right)^{1/p}
\left(\pi R^2\right)^{1/q}\\
&\le M(\pi R^2)^{1-1/p}.
\end{aligned}
$$
Dividing by $\pi R^2$ yields the displayed estimate. For $p=1$, the same estimate follows directly from
$$
\int_{B(z_0,R)}\abs{U}\le M.
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{U(z)=0\text{ for every }z\in\CC}.
$$


::: pf-proof

Fix $z_0\in\CC$. Step [](#s1-2){.pf-ref} gives, for every $R>0$,
$$
\abs{U(z_0)}\le \frac{M}{(\pi R^2)^{1/p}}.
$$
Since $p<\infty$, the right-hand side tends to $0$ as $R\to\infty$. Hence $\abs{U(z_0)}=0$. Because $z_0$ was arbitrary, $U$ vanishes identically.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
