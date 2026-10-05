---
schema: qual/card@1
id: P-PRACT20-W5-30
kind: problem
title: The integral $\int_{-\infty}^\infty\frac{dx}{1+x^4}$ by residues
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 30).
---

::: {.problem}
Evaluate $\int_{-\infty}^{\infty} \frac{dx}{1 + x^4}$.
:::

::: {.solution}
Let
\[
F(z)=\frac1{1+z^4}.
\]

<1>1. The poles of $F$ in the open upper half-plane are
\[
z_1=e^{i\pi/4},
\qquad
z_2=e^{3i\pi/4}.
\]

::: {.proof}
The equation
\[
1+z^4=0
\]
is
\[
z^4=e^{i(\pi+2\pi k)}.
\]
Its four roots are
\[
e^{i\pi/4},\quad
e^{3i\pi/4},\quad
e^{5i\pi/4},\quad
e^{7i\pi/4}.
\]
Exactly the first two have positive imaginary part.
:::

<1>2. Their residue sum is
\[
\operatorname{Res}(F,z_1)+\operatorname{Res}(F,z_2)
=-\frac{i}{2\sqrt2}.
\]

::: {.proof}
Every pole is simple, and
\[
\operatorname{Res}(F,z_k)
=\frac1{4z_k^3}.
\]
Therefore
\[
\begin{aligned}
\operatorname{Res}(F,z_1)+\operatorname{Res}(F,z_2)
&=
\frac14
\left(
e^{-3i\pi/4}+e^{-9i\pi/4}
\right)\\
&=
\frac14
\left(
e^{-3i\pi/4}+e^{-i\pi/4}
\right)\\
&=
\frac14(-i\sqrt2)\\
&=
-\frac{i}{2\sqrt2}.
\end{aligned}
\]
:::

<1>3. Let $C_R$ be the upper semicircle $|z|=R$. Then
\[
\int_{C_R}F(z)\,dz\longrightarrow0
\qquad(R\to\infty).
\]

::: {.proof}
For $R>1$ and $z\in C_R$,
\[
|1+z^4|
\ge
|z|^4-1
=R^4-1.
\]
Hence
\[
|F(z)|
\le
\frac1{R^4-1}.
\]
The arc length of $C_R$ is $\pi R$, so the ML estimate gives
\[
\left|\int_{C_R}F(z)\,dz\right|
\le
\frac{\pi R}{R^4-1}
\longrightarrow0.
\]
:::

<1>4. One has
\[
\boxed{
\int_{-\infty}^{\infty}\frac{dx}{1+x^4}
=\frac{\pi}{\sqrt2}}.
\]

::: {.proof}
Integrate $F$ around the positively oriented contour consisting of
$[-R,R]$ and $C_R$. For $R>1$, the residue theorem and step <1>2 give
\[
\int_{-R}^R\frac{dx}{1+x^4}
+\int_{C_R}F(z)\,dz
=
2\pi i
\left(-\frac{i}{2\sqrt2}\right)
=
\frac{\pi}{\sqrt2}.
\]
Letting $R\to\infty$ and using step <1>3 gives the result.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested value.
:::
:::
