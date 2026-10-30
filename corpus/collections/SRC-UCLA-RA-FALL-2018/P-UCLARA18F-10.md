---
schema: qual/card@1
id: P-UCLARA18F-10
kind: problem
title: Evaluation of $\int_0^\infty\frac{x^\beta}{1+x^2}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 10. For $-1<\beta<1$, evaluate
$$
\int_0^\infty\frac{x^\beta}{1+x^2}\,dx.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The improper integral converges for every $-1<\beta<1$.


::: pf-proof

On $(0,1]$,
$$
0\le \frac{x^\beta}{1+x^2}\le x^\beta,
$$
and $\int_0^1x^\beta\,dx<\infty$ because $\beta>-1$. On $[1,\infty)$,
$$
0\le \frac{x^\beta}{1+x^2}\le x^{\beta-2},
$$
and $\int_1^\infty x^{\beta-2}\,dx<\infty$ because $\beta<1$.

:::

:::

::: {.pf-step #s1-2}

Let
$$
F(z)=\frac{z^\beta}{1+z^2},
\qquad
z^\beta=\exp\!\bigl(\beta\Log z\bigr),
$$
where $\Log z=\log\abs{z}+i\arg z$ with $-\pi/2<\arg z<3\pi/2$. If $0<\varepsilon<1<R$, then integration around the positively oriented boundary $C_{\varepsilon,R}$ of the upper half-annulus $\{z:\varepsilon<\abs{z}<R,\ \operatorname{Im}z>0\}$ gives
$$
\int_{C_{\varepsilon,R}}F(z)\,dz
=\pi e^{i\pi\beta/2}.
$$


::: pf-proof

The chosen branch is holomorphic on a neighborhood of the closed upper half-annulus. Inside $C_{\varepsilon,R}$, the only pole of $F$ is the simple pole at $z=i$. Its residue is
$$
\operatorname{Res}(F,i)
=\frac{i^\beta}{2i}
=\frac{e^{i\pi\beta/2}}{2i}.
$$
The residue theorem therefore gives
$$
\int_{C_{\varepsilon,R}}F(z)\,dz
=2\pi i\,\operatorname{Res}(F,i)
=\pi e^{i\pi\beta/2}.
$$

:::

:::

::: {.pf-step #s1-3}

The contributions from the outer and inner semicircles tend to $0$ as $R\to\infty$ and $\varepsilon\to0$, respectively.


::: pf-proof

On the outer semicircle $\abs{z}=R$, one has $\abs{z^\beta}=R^\beta$ and $\abs{1+z^2}\ge R^2-1$. Hence
$$
\abs{\int_{\abs{z}=R,\ \operatorname{Im}z\ge0}F(z)\,dz}
\le \frac{\pi R^{\beta+1}}{R^2-1}
\longrightarrow0
$$
because $\beta<1$. On the inner semicircle $\abs{z}=\varepsilon$,
$$
\abs{\int_{\abs{z}=\varepsilon,\ \operatorname{Im}z\ge0}F(z)\,dz}
\le \frac{\pi\varepsilon^{\beta+1}}{1-\varepsilon^2}
\longrightarrow0
$$
because $\beta>-1$.

:::

:::

::: {.pf-step #s1-4}

The two straight sides of the contour satisfy
$$
\int_{\varepsilon}^{R}\frac{x^\beta}{1+x^2}\,dx
+\int_{-R}^{-\varepsilon}F(z)\,dz
=\bigl(1+e^{i\pi\beta}\bigr)
\int_{\varepsilon}^{R}\frac{x^\beta}{1+x^2}\,dx.
$$


::: pf-proof

On the positive real axis, $z^\beta=x^\beta$. On the negative real axis approached through the upper half-plane, $z=-x$ has argument $\pi$, so $(-x)^\beta=e^{i\pi\beta}x^\beta$. Parametrizing the segment from $-R$ to $-\varepsilon$ by $z=-x$, with $x$ decreasing from $R$ to $\varepsilon$, gives
$$
\int_{-R}^{-\varepsilon}F(z)\,dz
=e^{i\pi\beta}\int_{\varepsilon}^{R}\frac{x^\beta}{1+x^2}\,dx.
$$
Adding the positive-axis contribution proves the claim.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\int_0^\infty\frac{x^\beta}{1+x^2}\,dx
=\frac{\pi}{2\cos(\pi\beta/2)}}.
$$


::: pf-proof

Let $R\to\infty$ and $\varepsilon\to0$ in step [](#s1-2){.pf-ref}. By steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref}, and [](#s1-4){.pf-ref},
$$
\bigl(1+e^{i\pi\beta}\bigr)
\int_0^\infty\frac{x^\beta}{1+x^2}\,dx
=\pi e^{i\pi\beta/2}.
$$
Since
$$
1+e^{i\pi\beta}
=2e^{i\pi\beta/2}\cos(\pi\beta/2)
$$
and $-1<\beta<1$ implies $\cos(\pi\beta/2)>0$, division gives the displayed value.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required evaluation.

:::

:::

:::
