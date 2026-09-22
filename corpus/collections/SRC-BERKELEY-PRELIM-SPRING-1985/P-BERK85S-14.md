---
schema: qual/card@1
id: P-BERK85S-14
kind: problem
title: Convergence and evaluation of $\int_0^\pi\log(\sin x)\,dx$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Proved absolute convergence at the two endpoints using
    sin(x)>=2x/pi on [0,pi/2], then evaluated the integral by symmetry and
    the double-angle identity.
---

::: {.problem}
Show that the improper Riemann integral
\[
I=\int_0^\pi\log(\sin x)\,dx
\]
converges, and evaluate $I$.
:::

::: {.solution}
<1>1. The improper integral converges absolutely.

::: {.proof}
For $0<x\leq\pi/2$, concavity of $\sin x$ on $[0,\pi]$ gives the chord
bound
$$
\sin x\geq\frac{2x}{\pi}.
$$
Since $0<\sin x\leq1$ on this interval,
$$
0
\leq
-\log(\sin x)
\leq
-\log\left(\frac{2x}{\pi}\right).
$$
The majorant is integrable at $0$, because
$$
\int_0^{\pi/2}
-\log\left(\frac{2x}{\pi}\right)\,dx
<\infty.
$$
Hence
$$
\int_0^{\pi/2}\abs{\log(\sin x)}\,dx<\infty.
$$

For $\pi/2\leq x<\pi$, put $u=\pi-x$. Then
$\sin x=\sin u$, so the same estimate applies at $\pi$. Thus
$$
\int_0^\pi\abs{\log(\sin x)}\,dx<\infty.
$$
In particular, the stated improper Riemann integral converges.
:::

<1>2. If
$$
J\coloneqq\int_0^{\pi/2}\log(\sin x)\,dx,
$$
then
$$
I=2J.
$$

::: {.proof}
The substitution $u=\pi-x$ gives
$$
\int_{\pi/2}^{\pi}\log(\sin x)\,dx
=
\int_0^{\pi/2}\log(\sin u)\,du
=J.
$$
The substitutions are legitimate by step <1>1.
:::

<1>3. One also has
$$
J
=
\int_0^{\pi/2}\log(\cos x)\,dx.
$$

::: {.proof}
Use the substitution $u=\pi/2-x$ and the identity
$$
\sin(\pi/2-u)=\cos u.
$$
:::

<1>4. The number $J$ satisfies
$$
2J
=
-\frac{\pi}{2}\log2+J.
$$

::: {.proof}
By step <1>3,
$$
\begin{aligned}
2J
&=
\int_0^{\pi/2}
\log(\sin x\cos x)\,dx\\
&=
\int_0^{\pi/2}
\log\left(\frac{\sin(2x)}2\right)\,dx\\
&=
-\frac{\pi}{2}\log2
+
\int_0^{\pi/2}\log(\sin(2x))\,dx.
\end{aligned}
$$
With $u=2x$ and step <1>2,
$$
\int_0^{\pi/2}\log(\sin(2x))\,dx
=
\frac12\int_0^\pi\log(\sin u)\,du
=
\frac12 I
=J.
$$
Substitution gives the claimed equation.
:::

<1>5. Therefore
$$
\boxed{
I
=
-\pi\log2
}.
$$

::: {.proof}
Step <1>4 gives
$$
J=-\frac{\pi}{2}\log2.
$$
Apply $I=2J$ from step <1>2.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>1 proves convergence and step <1>5 evaluates the integral.
:::
:::
