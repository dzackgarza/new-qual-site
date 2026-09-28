---
schema: qual/card@1
id: P-BKS82-8
kind: problem
title: The integral $\int_{-\infty}^{\infty}\cos x/(x^4+1)\,dx$ by contour integration
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained PDF; the extracted markdown contains a different Problem 8.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the upper-half-plane poles, residues, semicircle estimate, and the final trigonometric simplification.
---

::: {.problem}
Evaluate by contour integration
\[
\int_{-\infty}^{\infty}\frac{\cos x}{x^4+1}\,dx.
\]
:::

::: {.solution}
Put
$$
F(z)\coloneqq\frac{e^{iz}}{z^4+1}
$$
and
$$
\alpha\coloneqq\frac1{\sqrt2}.
$$

<1>1. The poles of $F$ in the open upper half-plane are
$$
z_1=e^{i\pi/4}=\alpha(1+i),
\qquad
z_2=e^{3i\pi/4}=\alpha(-1+i),
$$
and
$$
\operatorname{Res}(F,z_k)
=
\frac{e^{iz_k}}{4z_k^3}
\qquad
(k=1,2).
$$

::: {.proof}
The zeros of $z^4+1$ are
$$
e^{i\pi/4},
\quad
e^{3i\pi/4},
\quad
e^{5i\pi/4},
\quad
e^{7i\pi/4}.
$$
The first two lie in the upper half-plane. All four zeros are simple, since
the derivative of $z^4+1$ is $4z^3$ and none of these roots is zero.
The simple-pole residue formula gives the stated residues.
:::

<1>2. If $C_R$ is the upper semicircle $\abs{z}=R$ with $R>1$, then
$$
\lim_{R\to\infty}\int_{C_R}F(z)\,dz=0.
$$

::: {.proof}
On $C_R$ one has
$$
\abs{e^{iz}}=e^{-\operatorname{Im}z}\le1
$$
and, by the reverse triangle inequality,
$$
\abs{z^4+1}\ge R^4-1.
$$
Since the length of $C_R$ is $\pi R$,
$$
\abs{
\int_{C_R}F(z)\,dz
}
\le
\frac{\pi R}{R^4-1}
\longrightarrow0.
$$
:::

<1>3. The exponential integral satisfies
$$
\int_{-\infty}^{\infty}\frac{e^{ix}}{x^4+1}\,dx
=
2\pi i
\left(
\operatorname{Res}(F,z_1)
+
\operatorname{Res}(F,z_2)
\right).
$$

::: {.proof}
For $R>1$, apply the residue theorem to the positively oriented contour
formed by $[-R,R]$ and $C_R$. It encloses exactly $z_1$ and $z_2$, so
$$
\int_{-R}^{R}\frac{e^{ix}}{x^4+1}\,dx
+
\int_{C_R}F(z)\,dz
=
2\pi i
\left(
\operatorname{Res}(F,z_1)
+
\operatorname{Res}(F,z_2)
\right).
$$
The real-axis integrand is absolutely integrable, and the semicircle term
tends to $0$ by step <1>2. Letting $R\to\infty$ gives the identity.
:::

<1>4. The sum of the two residues is
$$
\operatorname{Res}(F,z_1)
+
\operatorname{Res}(F,z_2)
=
-\frac{i\alpha}{2}
e^{-\alpha}
\bigl(
\cos\alpha+\sin\alpha
\bigr).
$$

::: {.proof}
Since
$$
z_1^3=z_2,
\qquad
z_2^3=z_1,
\qquad
\frac1{z_2}=-z_1,
\qquad
\frac1{z_1}=-z_2,
$$
step <1>1 gives
$$
\operatorname{Res}(F,z_1)
+
\operatorname{Res}(F,z_2)
=
-\frac14
\left(
z_1e^{iz_1}+z_2e^{iz_2}
\right).
$$
Also
$$
e^{iz_1}=e^{-\alpha}e^{i\alpha},
\qquad
e^{iz_2}=e^{-\alpha}e^{-i\alpha}.
$$
Writing $c=\cos\alpha$ and $s=\sin\alpha$,
$$
\begin{aligned}
z_1e^{iz_1}+z_2e^{iz_2}
&=
\alpha e^{-\alpha}
\left(
(1+i)(c+is)+(-1+i)(c-is)
\right)\\
&=
2i\alpha e^{-\alpha}(c+s).
\end{aligned}
$$
Substitution gives the stated residue sum.
:::

<1>5. Therefore
$$
\int_{-\infty}^{\infty}\frac{e^{ix}}{x^4+1}\,dx
=
\frac{\pi}{\sqrt2}
e^{-1/\sqrt2}
\left(
\cos\frac1{\sqrt2}
+
\sin\frac1{\sqrt2}
\right).
$$

::: {.proof}
Combine steps <1>3 and <1>4 and use
$\alpha=1/\sqrt2$:
$$
2\pi i
\left(
-\frac{i\alpha}{2}
e^{-\alpha}
(\cos\alpha+\sin\alpha)
\right)
=
\pi\alpha e^{-\alpha}
(\cos\alpha+\sin\alpha).
$$
:::

<1>6. Hence
$$
\boxed{
\int_{-\infty}^{\infty}\frac{\cos x}{x^4+1}\,dx
=
\frac{\pi}{\sqrt2}
e^{-1/\sqrt2}
\left(
\cos\frac1{\sqrt2}
+
\sin\frac1{\sqrt2}
\right)
}.
$$

::: {.proof}
The cosine integral is the real part of the exponential integral in step
<1>5. The quantity on the right-hand side of step <1>5 is real, so taking
real parts gives exactly the displayed value.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the requested contour-integral evaluation.
:::
:::
