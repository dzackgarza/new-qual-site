---
schema: qual/card@1
id: P-RAF21G
kind: problem
title: "Heisenberg uncertainty inequality $\\norm{xf}_2\\,\\norm{\\xi\\hat f}_2\\ge\\norm{f}_2^2/(4\\pi)$"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - Inequalities
  - L2 Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 7 of the official UCSD Fall 2021 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
For any $f \in L^2(\RR) \cap C^1(\RR)$ show that
$$
\left(\int_\RR x^2 \abs{f(x)}^2 \, dx\right) \left(\int_\RR \xi^2 \abs{\hat{f}(\xi)}^2 \, d\xi\right) \geq \frac{1}{16\pi^2} \left(\int_\RR \abs{f(x)}^2 \, dx\right)^2.
$$

Here $\hat{f}$ is the Fourier transform of $f$ and $dx, d\xi$ represent the Lebesgue measure on $\RR$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

We may assume $f\ne0$ and $\int x^2\abs{f}^2,\int\xi^2\abs{\widehat f}^2<\infty$; then $\norm{f'}_2=2\pi\norm{\xi\widehat f}_2$.

::: pf-proof

If $f=0$ almost everywhere, both sides are $0$. For nonzero $f$, both second moments are positive; if either
$$
\int_{\RR}x^2\abs{f(x)}^2\,dx
$$
or
$$
\int_{\RR}\xi^2\abs{\widehat f(\xi)}^2\,d\xi
$$
is infinite, the left side is $+\infty$. Hence assume both are finite.

With the convention $\widehat f(\xi)=\int_{\RR}f(x)e^{-2\pi ix\xi}\,dx$,
$$
\widehat{f'}(\xi)=2\pi i\xi\widehat f(\xi)
$$
in the distributional sense. Plancherel therefore gives
$$
\norm{f'}_2=2\pi\norm{\xi\widehat f}_2<\infty.
$$

:::

:::

::: {.pf-step #s2}

$\norm{f}_2^2\le2\norm{xf}_2\norm{f'}_2$.

::: pf-proof

Choose $\chi\in C_c^\infty(\RR)$ with $0\le\chi\le1$, $\chi=1$ on $[-1,1]$, and $\operatorname{supp}\chi\subset[-2,2]$. Put
$$
\chi_R(x)=\chi(x/R).
$$
Then $\abs{x\chi_R'(x)}$ is bounded uniformly in $R$, and it is supported where $R\le\abs{x}\le2R$.

Because $f,f'\in L^2$, the function $\abs{f}^2$ belongs to $W^{1,1}$ with weak derivative
$$
(\abs{f}^2)'=2\operatorname{Re}(f'\overline f).
$$
Integrating the derivative of the compactly supported function $x\chi_R(x)\abs{f(x)}^2$ gives
$$
0=\int_{\RR}(\chi_R+x\chi_R')\abs{f}^2
+2\operatorname{Re}\int_{\RR}x\chi_R f'\overline f.
$$
Hence
$$
\int\chi_R\abs{f}^2
=-\int x\chi_R'\abs{f}^2
-2\operatorname{Re}\int x\chi_R f'\overline f.
$$
As $R\to\infty$, dominated convergence gives
$$
\int\chi_R\abs{f}^2\to\norm{f}_2^2,
$$
while
$$
\abs{\int x\chi_R'\abs{f}^2}
\le C\int_{\abs{x}\ge R}\abs{f(x)}^2\,dx\to0.
$$
Finally, $\abs{xf}\abs{f'}\in L^1$ by Cauchy--Schwarz, so
$$
\int x\chi_R f'\overline f\to\int x f'\overline f.
$$
Therefore
$$
\norm{f}_2^2
=-2\operatorname{Re}\int_{
\RR}x f'(x)\overline{f(x)}\,dx.
$$
Taking absolute values and applying Cauchy--Schwarz yields
$$
\norm{f}_2^2
\le 2\norm{xf}_2\norm{f'}_2.
$$

:::

:::

::: pf-qed

Substituting $\norm{f'}_2=2\pi\norm{\xi\widehat f}_2$ from step [](#s1){.pf-ref} into step [](#s2){.pf-ref} gives
$$
\norm{xf}_2\,\norm{\xi\widehat f}_2
\ge \frac1{4\pi}\norm{f}_2^2.
$$
Squaring both sides,
$$
\boxed{
\left(\int x^2\abs{f(x)}^2\,dx\right)
\left(\int \xi^2\abs{\widehat f(\xi)}^2\,d\xi\right)
\ge
\frac1{16\pi^2}
\left(\int \abs{f(x)}^2\,dx\right)^2.}
$$

:::

:::

:::
