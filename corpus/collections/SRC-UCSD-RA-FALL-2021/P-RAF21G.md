---
schema: qual/card@1
id: P-RAF21G
kind: problem
title: "Heisenberg-type uncertainty inequality via Fourier analysis"
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

::: problem
For any $f \in L^2(\mathbb{R}) \cap C^1(\mathbb{R})$ show that
$$
\left(\int_\mathbb{R} x^2 |f(x)|^2 \, dx\right) \left(\int_\mathbb{R} \xi^2 |\hat{f}(\xi)|^2 \, d\xi\right) \geq \frac{1}{16\pi^2} \left(\int_\mathbb{R} |f(x)|^2 \, dx\right)^2.
$$

Here $\hat{f}$ is the Fourier transform of $f$ and $dx, d\xi$ represent the Lebesgue measure on $\mathbb{R}$.
:::

::: solution
<1>1. Reduce to the case in which both second moments are finite.
::: proof
If $f=0$ almost everywhere, the inequality is immediate. For nonzero $f$, if either
\[
\int_{\mathbb R}x^2|f(x)|^2\,dx
\]
or
\[
\int_{\mathbb R}\xi^2|\widehat f(\xi)|^2\,d\xi
\]
is infinite, the desired inequality is automatic. Hence assume both are finite.

With the Fourier convention used in the exam,
\[
\widehat{f'}(\xi)=2\pi i\xi\widehat f(\xi)
\]
in the distributional sense. Plancherel therefore gives
\[
\|f'\|_2=2\pi\|\xi\widehat f\|_2<\infty.
\]
:::

<1>2. Establish the basic integration-by-parts inequality.
::: proof
Choose $\chi\in C_c^\infty(\mathbb R)$ with $0\le\chi\le1$, $\chi=1$ on $[-1,1]$, and $\operatorname{supp}\chi\subset[-2,2]$. Put
\[
\chi_R(x)=\chi(x/R).
\]
Then $|x\chi_R'(x)|$ is bounded uniformly in $R$, and it is supported where $R\le|x|\le2R$.

Because $f,f'\in L^2$, the function $|f|^2$ belongs to $W^{1,1}$ with weak derivative
\[
(|f|^2)'=2\operatorname{Re}(f'\overline f).
\]
Integrating the derivative of the compactly supported function $x\chi_R(x)|f(x)|^2$ gives
\[
0=\int_{\mathbb R}(\chi_R+x\chi_R')|f|^2
+2\operatorname{Re}\int_{\mathbb R}x\chi_R f'\overline f.
\]
Hence
\[
\int\chi_R|f|^2
=-\int x\chi_R'|f|^2
-2\operatorname{Re}\int x\chi_R f'\overline f.
\]
As $R\to\infty$, dominated convergence gives
\[
\int\chi_R|f|^2\to\|f\|_2^2,
\]
while
\[
\left|\int x\chi_R'|f|^2\right|
\le C\int_{|x|\ge R}|f(x)|^2\,dx\to0.
\]
Finally, $|xf||f'|\in L^1$ by Cauchy--Schwarz, so
\[
\int x\chi_R f'\overline f\to\int x f'\overline f.
\]
Therefore
\[
\|f\|_2^2
=-2\operatorname{Re}\int_{
\mathbb R}x f'(x)\overline{f(x)}\,dx.
\]
Taking absolute values and applying Cauchy--Schwarz yields
\[
\|f\|_2^2
\le 2\|xf\|_2\|f'\|_2.
\]
:::

<1>3. Substitute the Fourier derivative identity.
::: proof
Using
\[
\|f'\|_2=2\pi\|\xi\widehat f\|_2,
\]
Step 2 gives
\[
\|xf\|_2\,\|\xi\widehat f\|_2
\ge \frac1{4\pi}\|f\|_2^2.
\]
Squaring both sides,
\[
\boxed{
\left(\int x^2|f(x)|^2\,dx\right)
\left(\int \xi^2|\widehat f(\xi)|^2\,d\xi\right)
\ge
\frac1{16\pi^2}
\left(\int |f(x)|^2\,dx\right)^2.}
\]
:::
:::
