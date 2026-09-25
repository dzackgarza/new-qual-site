---
schema: qual/card@1
id: P-BKS14-5B
kind: problem
title: Evaluate a cosine rational integral
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the upper-half-plane residue, explicit semicircle decay estimate, and the evenness factor relating the full-line real part to the requested integral.
---

::: {.problem}
Evaluate
\[
\int_0^\infty \frac{\cos x}{1+x^2}\,dx.
\]
:::

::: {.solution}
Set
$$
F(z)
\coloneqq
\frac{e^{iz}}{1+z^2}.
$$
For $R>1$, let $C_R$ be the upper semicircle
$$
z=Re^{i\theta},
\qquad
0\leq\theta\leq\pi,
$$
oriented from $R$ to $-R$.

<1>1. The semicircular contribution satisfies
$$
\lim_{R\to\infty}
\int_{C_R}F(z)\,dz
=
0.
$$

::: {.proof}
On $C_R$,
$$
\abs{1+z^2}
\geq
R^2-1
$$
and
$$
\abs{e^{iz}}
=
e^{-R\sin\theta}.
$$
Since
$$
\abs{dz}=R\,d\theta,
$$
one obtains
$$
\abs{
\int_{C_R}F(z)\,dz
}
\leq
\frac{R}{R^2-1}
\int_0^\pi e^{-R\sin\theta}\,d\theta.
$$

For
$$
0\leq\theta\leq\frac\pi2,
$$
concavity of sine gives
$$
\sin\theta\geq\frac{2\theta}{\pi}.
$$
Using symmetry about $\pi/2$,
$$
\begin{aligned}
\int_0^\pi e^{-R\sin\theta}\,d\theta
&\leq
2\int_0^{\pi/2}e^{-2R\theta/\pi}\,d\theta\\
&\leq
\frac{\pi}{R}.
\end{aligned}
$$
Therefore
$$
\abs{
\int_{C_R}F(z)\,dz
}
\leq
\frac{\pi}{R^2-1}
\longrightarrow0.
$$
:::

<1>2. The only pole of $F$ in the upper half-plane is $z=i$, and
$$
\operatorname{Res}_{z=i}F(z)
=
\frac{e^{-1}}{2i}.
$$

::: {.proof}
The denominator factors as
$$
1+z^2=(z-i)(z+i).
$$
Thus the upper-half-plane pole is $i$. It is simple, and
$$
\operatorname{Res}_{z=i}F(z)
=
\frac{e^{i\cdot i}}{i+i}
=
\frac{e^{-1}}{2i}.
$$
:::

<1>3. One has
$$
\int_{-\infty}^{\infty}
\frac{e^{ix}}{1+x^2}\,dx
=
\frac{\pi}{e}.
$$

::: {.proof}
For $R>1$, the residue theorem on the contour formed by $[-R,R]$ and
$C_R$ gives
$$
\int_{-R}^{R}\frac{e^{ix}}{1+x^2}\,dx
+
\int_{C_R}F(z)\,dz
=
2\pi i
\frac{e^{-1}}{2i}
=
\frac{\pi}{e}.
$$
Let $R\to\infty$ and apply step <1>1.
:::

<1>4. Taking real parts in step <1>3 gives
$$
\int_{-\infty}^{\infty}
\frac{\cos x}{1+x^2}\,dx
=
\frac{\pi}{e}.
$$

::: {.proof}
For every finite $R$,
$$
\operatorname{Re}
\int_{-R}^{R}
\frac{e^{ix}}{1+x^2}\,dx
=
\int_{-R}^{R}
\frac{\cos x}{1+x^2}\,dx.
$$
Pass to the limit using step <1>3.
:::

<1>5. Therefore
$$
\boxed{
\int_0^\infty
\frac{\cos x}{1+x^2}\,dx
=
\frac{\pi}{2e}
}.
$$

::: {.proof}
The real integrand is even, so its integral over the whole real line is
twice its integral over $[0,\infty)$. Apply step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required value.
:::
:::
