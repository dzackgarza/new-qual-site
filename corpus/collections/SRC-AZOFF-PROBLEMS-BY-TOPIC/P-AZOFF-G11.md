---
schema: qual/card@1
id: P-AZOFF-G11
kind: problem
title: $\int_0^\infty\frac{\sin^3 x}{x^3}\,dx$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Residues, Problem 11, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Integrated [3 exp(iz)-exp(3iz)-2]/z^3 over an indented upper
    semicircle. Its Laurent expansion at zero begins 3/z+4i, so the
    clockwise indentation contributes -3pi i; the outer arc vanishes.
    Taking imaginary parts gives 4 times the whole-line sin^3(x)/x^3
    integral, and evenness yields 3pi/8.
---

::: {.problem}
Evaluate $\int _ { 0 } ^ { \infty } { \frac { \sin ^ { 3 } x } { x ^ { 3 } } } d x$
:::

::: {.solution}
Set
$$
F(z)=\frac{3e^{iz}-e^{3iz}-2}{z^3}.
$$
For $0<\varepsilon<R$, use the upper-half-plane contour consisting of
$[-R,-\varepsilon]$, a clockwise upper semicircle of radius
$\varepsilon$ about $0$, $[\varepsilon,R]$, and the large upper
semicircle of radius $R$.

::: pf

::: {.pf-step #s1}

Near $z=0$,
$$
F(z)
=
\frac3z
+4i
+O(z).
$$

::: pf-proof

The exponential expansions give
$$
e^{iz}
=
1+iz-\frac{z^2}{2}-\frac{i z^3}{6}+O(z^4)
$$
and
$$
e^{3iz}
=
1+3iz-\frac{9z^2}{2}-\frac{9i z^3}{2}+O(z^4).
$$
Therefore
$$
3e^{iz}-e^{3iz}-2
=
3z^2+4iz^3+O(z^4).
$$
Divide by $z^3$.

:::

:::

::: {.pf-step #s2}

The small indented semicircle contributes
$$
-3\pi i
$$
as $\varepsilon\to0$.

::: pf-proof

By step [](#s1){.pf-ref},
$$
F(z)=\frac3z+H(z),
$$
where $H$ is bounded near $0$. Parametrize the clockwise upper semicircle by
$$
z=\varepsilon e^{i\theta},
\qquad
\pi\geq\theta\geq0.
$$
Then
$$
\int\frac3z\,dz
=
\int_\pi^0 3i\,d\theta
=
-3\pi i.
$$
The integral of $H$ tends to zero because its arc has length
$\pi\varepsilon$.

:::

:::

::: {.pf-step #s3}

The integral over the large upper semicircle tends to zero as
$R\to\infty$.

::: pf-proof

In the upper half-plane,
$$
\abs{e^{iz}}\leq1
\qquad\text{and}\qquad
\abs{e^{3iz}}\leq1.
$$
Hence on $\abs{z}=R$,
$$
\abs{F(z)}
\leq
\frac{3+1+2}{R^3}
=
\frac6{R^3}.
$$
The large arc has length $\pi R$, so
$$
\abs{
\int_{\text{large arc}}F(z)\,dz
}
\leq
\frac{6\pi}{R^2}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s4}

The symmetric indented real-axis integrals satisfy
$$
\lim_{\substack{R\to\infty\\ \varepsilon\to0^+}}
\left(
\int_{-R}^{-\varepsilon}F(x)\,dx
+
\int_{\varepsilon}^{R}F(x)\,dx
\right)
=
3\pi i.
$$

::: pf-proof

The indentation removes the only singularity of $F$, so the function is
holomorphic inside the indented contour. Cauchy's theorem gives total
contour integral zero. Thus the real-axis portions are the negatives of the
two arc integrals. Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give the displayed limit.

:::

:::

::: {.pf-step #s5}

For real $x\neq0$,
$$
\operatorname{Im}F(x)
=
4\frac{\sin^3x}{x^3}.
$$

::: pf-proof

The triple-angle identity
$$
\sin(3x)=3\sin x-4\sin^3x
$$
gives
$$
3\sin x-\sin(3x)=4\sin^3x.
$$
Taking the imaginary part of the numerator of $F(x)$ and dividing by
$x^3$ gives the claim.

:::

:::

::: {.pf-step #s6}

The whole-line integral satisfies
$$
4\int_{-\infty}^{\infty}
\frac{\sin^3x}{x^3}\,dx
=
3\pi.
$$

::: pf-proof

The function $\sin^3x/x^3$ extends continuously across $0$ with value
$1$, and it is absolutely integrable at infinity because it is bounded by
$1/\abs{x}^3$ there. Hence taking imaginary parts in step [](#s4){.pf-ref} and using
step [](#s5){.pf-ref} gives the ordinary improper integral in the display.

:::

:::

::: {.pf-step #s7}

The requested value is
$$
\boxed{
\int_0^{\infty}
\frac{\sin^3x}{x^3}\,dx
=
\frac{3\pi}{8}.
}
$$

::: pf-proof

The function $\sin^3x/x^3$ is even. Therefore step [](#s6){.pf-ref} becomes
$$
8\int_0^{\infty}
\frac{\sin^3x}{x^3}\,dx
=
3\pi.
$$
Divide by $8$.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the requested evaluation.

:::

:::

:::
