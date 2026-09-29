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
::: pf

::: {.pf-step #converges-absolutely}
The improper integral converges absolutely.

::: pf-proof
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

:::

::: {.pf-step #i-equals-two-j}
If
$$
J\coloneqq\int_0^{\pi/2}\log(\sin x)\,dx,
$$
then
$$
I=2J.
$$

::: pf-proof
The substitution $u=\pi-x$ gives
$$
\int_{\pi/2}^{\pi}\log(\sin x)\,dx
=
\int_0^{\pi/2}\log(\sin u)\,du
=J.
$$
The substitutions are legitimate by step [](#converges-absolutely){.pf-ref}.
:::

:::

::: {.pf-step #j-with-cosine}
One also has
$$
J
=
\int_0^{\pi/2}\log(\cos x)\,dx.
$$

::: pf-proof
Use the substitution $u=\pi/2-x$ and the identity
$$
\sin(\pi/2-u)=\cos u.
$$
:::

:::

::: {.pf-step #two-j-equation}
The number $J$ satisfies
$$
2J
=
-\frac{\pi}{2}\log2+J.
$$

::: pf-proof
By step [](#j-with-cosine){.pf-ref},
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
With $u=2x$ and step [](#i-equals-two-j){.pf-ref},
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

:::

::: {.pf-step #value-boxed}
Therefore
$$
\boxed{
I
=
-\pi\log2
}.
$$

::: pf-proof
Step [](#two-j-equation){.pf-ref} gives
$$
J=-\frac{\pi}{2}\log2.
$$
Apply $I=2J$ from step [](#i-equals-two-j){.pf-ref}.
:::

:::

::: pf-qed
Step [](#converges-absolutely){.pf-ref} proves convergence and step [](#value-boxed){.pf-ref} evaluates the integral.
:::

:::
:::
