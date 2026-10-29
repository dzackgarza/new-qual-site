---
schema: qual/card@1
id: P-TIE-S14-02
kind: problem
title: $\int_\gamma z^n\,dz$ over circles not enclosing the origin without Cauchy's theorem
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2014, question 1, part 2.
---

::: {.problem}
Without using Cauchy's theorem, evaluate
$$
\int_\gamma z^n\,dz
$$
for every integer $n$, where $\gamma$ is any positively oriented circle that does not contain the origin.
:::

::: {.solution}

Write the circle as
$$
\gamma(t)=c+\rho e^{it},
\qquad
0\le t\le2\pi,
$$
where $\rho>0$ and $\abs{c}>\rho$, since the origin is outside the enclosed disk.

::: pf

::: {.pf-step #s1-1}

If $n\ne-1$, then
$$
\int_\gamma z^n\,dz=0.
$$


::: pf-proof

For $n\ne-1$, the function
$$
F(z)\coloneqq\frac{z^{n+1}}{n+1}
$$
is analytic on $\CC\setminus\{0\}$ and satisfies
$$
F'(z)=z^n.
$$
The circle $\gamma$ avoids the origin, so the fundamental theorem for complex line integrals gives
$$
\int_\gamma z^n\,dz
=
F(\gamma(2\pi))-F(\gamma(0))
=0.
$$

:::

:::

::: {.pf-step #s1-2}

On $\gamma$,
$$
\frac1z
=
\sum_{k=0}^{\infty}
\frac{(-\rho)^k}{c^{k+1}}e^{ikt},
$$
and this series converges uniformly in $t\in[0,2\pi]$.


::: pf-proof

Since $\abs{c}>\rho$,
$$
\abs{\frac{\rho}{c}}<1.
$$
Thus
$$
\begin{aligned}
\frac1{c+\rho e^{it}}
&=
\frac1c
\frac1{1+\frac{\rho}{c}e^{it}}\\
&=
\frac1c
\sum_{k=0}^{\infty}
\left(-\frac{\rho}{c}e^{it}\right)^k\\
&=
\sum_{k=0}^{\infty}
\frac{(-\rho)^k}{c^{k+1}}e^{ikt}.
\end{aligned}
$$
The ratio has modulus $\rho/\abs{c}<1$ independently of $t$, so the geometric series converges uniformly.

:::

:::

::: {.pf-step #s1-3}

For $n=-1$,
$$
\int_\gamma z^{-1}\,dz=0.
$$


::: pf-proof

By step [](#s1-2){.pf-ref} and
$$
dz=i\rho e^{it}\,dt,
$$
uniform convergence permits termwise integration:
$$
\begin{aligned}
\int_\gamma \frac{dz}{z}
&=
i\rho
\sum_{k=0}^{\infty}
\frac{(-\rho)^k}{c^{k+1}}
\int_0^{2\pi}e^{i(k+1)t}\,dt.
\end{aligned}
$$
For every $k\ge0$,
$$
\int_0^{2\pi}e^{i(k+1)t}\,dt=0,
$$
so the whole sum is $0$.

:::

:::

::: {.pf-step #s1-4}

Therefore, for every integer $n$,
$$
\boxed{
\int_\gamma z^n\,dz=0.
}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} covers $n\ne-1$, and step [](#s1-3){.pf-ref} covers $n=-1$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested value for every integer $n$ without using Cauchy's theorem.

:::

:::

:::
