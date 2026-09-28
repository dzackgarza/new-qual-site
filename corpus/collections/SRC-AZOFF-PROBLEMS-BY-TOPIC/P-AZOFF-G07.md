---
schema: qual/card@1
id: P-AZOFF-G07
kind: problem
title: $\int_0^\infty\frac{\sin x}{x(x^2+1)}\,dx$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Residues, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Integrated exp(iz)/[z(z^2+1)] over an indented upper semicircle. The
    pole at i contributes -pi i/e, the clockwise indentation at zero
    contributes -pi i, and the outer arc vanishes. Taking imaginary parts
    and using evenness gives (pi/2)(1-e^(-1)).
---

::: {.problem}
Evaluate $\textstyle \int _ { 0 } ^ { \infty } { \frac { \sin x } { x ( x ^ { 2 } + 1 ) } } d x$
:::

::: {.solution}
Set
$$
F(z)=\frac{e^{iz}}{z(z^2+1)}.
$$
For $0<\varepsilon<1<R$, use the upper-half-plane contour consisting of
$[-R,-\varepsilon]$, a clockwise upper semicircle of radius
$\varepsilon$ about $0$, $[\varepsilon,R]$, and the large upper
semicircle of radius $R$.

<1>1. The only pole inside the indented contour is $z=i$, and
$$
\Res(F;i)=-\frac{e^{-1}}2.
$$

::: {.proof}
The poles of $F$ are $0$ and $\pm i$. The indentation excludes $0$, and
only $i$ lies in the upper half-plane. Since the pole at $i$ is simple,
$$
\begin{aligned}
\Res(F;i)
&=
\frac{e^{ii}}{i(i+i)}\\
&=
\frac{e^{-1}}{-2}\\
&=
-\frac{e^{-1}}2.
\end{aligned}
$$
:::

<1>2. The small indented semicircle contributes
$$
-\pi i
$$
in the limit $\varepsilon\to0$.

::: {.proof}
Near $0$,
$$
F(z)
=
\frac1z
+O(1).
$$
Indeed, $e^{iz}=1+O(z)$ and $(1+z^2)^{-1}=1+O(z^2)$. On the clockwise
upper semicircle
$$
z=\varepsilon e^{i\theta},
\qquad
\pi\geq\theta\geq0,
$$
one has
$$
\int\frac{dz}{z}
=
\int_\pi^0 i\,d\theta
=
-\pi i.
$$
The integral of the bounded remainder tends to zero with the arc length.
:::

<1>3. The integral over the large upper semicircle tends to zero as
$R\to\infty$.

::: {.proof}
For $z$ in the upper half-plane,
$$
\abs{e^{iz}}\leq1.
$$
On $\abs{z}=R$,
$$
\abs{z^2+1}\geq R^2-1.
$$
Hence
$$
\abs{F(z)}
\leq
\frac1{R(R^2-1)}.
$$
The arc length is $\pi R$, so the ML estimate gives
$$
\abs{
\int_{\text{large arc}}F(z)\,dz
}
\leq
\frac{\pi}{R^2-1}
\longrightarrow0.
$$
:::

<1>4. The symmetric indented real-axis integrals satisfy
$$
\lim_{\substack{R\to\infty\\ \varepsilon\to0^+}}
\left(
\int_{-R}^{-\varepsilon}F(x)\,dx
+
\int_{\varepsilon}^{R}F(x)\,dx
\right)
=
\pi i(1-e^{-1}).
$$

::: {.proof}
By the residue theorem and step <1>1, the full contour integral is
$$
2\pi i\Res(F;i)
=
-\pi i e^{-1}.
$$
Thus the two real-axis segments equal this residue contribution minus the
small and large arc integrals. By steps <1>2 and <1>3, their limit is
$$
-\pi i e^{-1}
-(-\pi i)
=
\pi i(1-e^{-1}).
$$
:::

<1>5. The whole-line sine integral is
$$
\int_{-\infty}^{\infty}
\frac{\sin x}{x(x^2+1)}\,dx
=
\pi(1-e^{-1}).
$$

::: {.proof}
The imaginary part of $F(x)$ is
$$
\frac{\sin x}{x(x^2+1)}.
$$
This function extends continuously across $x=0$, since
$$
\frac{\sin x}{x}\longrightarrow1.
$$
Taking imaginary parts in step <1>4 therefore gives the ordinary improper
whole-line integral displayed above.
:::

<1>6. The requested value is
$$
\boxed{
\int_0^{\infty}
\frac{\sin x}{x(x^2+1)}\,dx
=
\frac{\pi}{2}(1-e^{-1}).
}
$$

::: {.proof}
The integrand in step <1>5 is even, so its whole-line integral is twice the
half-line integral.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the requested evaluation.
:::
:::
