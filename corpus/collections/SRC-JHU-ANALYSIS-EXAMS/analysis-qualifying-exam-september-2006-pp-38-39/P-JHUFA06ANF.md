---
schema: qual/card@1
id: P-JHUFA06ANF
kind: problem
title: 'The oscillatory integral $\int_0^2 f(x)e^{itx}\,dx$ is $o(1/t)$ under endpoint vanishing'
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the JHU Analysis Qualifying Exam, September 2006, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Suppose $f\in C^1([0,2])$ and
$$
f(0)=f'(0)=f(2)=f'(2)=0.
$$
Prove that for every $\varepsilon>0$ there exists $T_\varepsilon$ such that for all $t>T_\varepsilon$,
$$
\abs{\int_0^2 f(x)e^{itx}\,dx}\le \frac{\varepsilon}{t}.
$$
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the compilation `assets/attachments/JHU Years of Analysis Exams.pdf` and no solutions sheet accompanies it, so the argument below is the card's own. It is integration by parts followed by the Riemann--Lebesgue lemma, and the closing step records which of the stated hypotheses the argument actually uses.

Throughout, $f\in C^{1}([0,2])$ with $f(0)=f(2)=0$, and $t>0$.

::: pf

::: {.pf-step #by-parts}
For $t>0$,
$$
\int_{0}^{2}f(x)\mathrm{e}^{itx}\,dx=-\frac{1}{it}\int_{0}^{2}f'(x)\mathrm{e}^{itx}\,dx.
$$

::: pf-proof
Integrate by parts with $u=f$ and $v=\mathrm{e}^{itx}/(it)$, legitimate because $f$ is continuously differentiable and $\mathrm{e}^{itx}$ is smooth:
$$
\int_{0}^{2}f(x)\mathrm{e}^{itx}\,dx=\Big[\frac{f(x)\mathrm{e}^{itx}}{it}\Big]_{0}^{2}-\frac{1}{it}\int_{0}^{2}f'(x)\mathrm{e}^{itx}\,dx.
$$
The boundary term is $\frac{f(2)\mathrm{e}^{2it}-f(0)}{it}=0$ because $f(2)=f(0)=0$.
:::

:::

::: {.pf-step #riemann-lebesgue}
$\displaystyle\int_{0}^{2}f'(x)\mathrm{e}^{itx}\,dx\to0$ as $t\to\infty$.

::: pf-proof
$f'$ is continuous on the compact interval $[0,2]$, hence bounded, hence integrable: $f'\in L^{1}([0,2])$. The Riemann--Lebesgue lemma states that the Fourier transform of an $L^{1}$ function tends to $0$ at infinity, which in this form is exactly the assertion.
:::

:::

::: {.pf-step #choice-of-T}
For every $\varepsilon>0$ there is $T_{\varepsilon}\geq0$ with $\big|\int_{0}^{2}f'(x)\mathrm{e}^{itx}\,dx\big|<\varepsilon$ for all $t>T_{\varepsilon}$.

::: pf-proof
This is the definition of convergence to $0$ of the expression in step [](#riemann-lebesgue){.pf-ref}: for the given $\varepsilon$ there is $T_{\varepsilon}$ beyond which the modulus is less than $\varepsilon$, and taking $T_{\varepsilon}$ nonnegative involves no loss.
:::

:::

::: pf-step
Therefore, for every $\varepsilon>0$ and every $t>T_{\varepsilon}$,
$$
\boxed{\Big|\int_{0}^{2}f(x)\mathrm{e}^{itx}\,dx\Big|\leq\frac{\varepsilon}{t},}
$$
so the integral is $o(1/t)$.

::: pf-proof
By step [](#by-parts){.pf-ref} and the triangle inequality for integrals,
$$
\Big|\int_{0}^{2}f(x)\mathrm{e}^{itx}\,dx\Big|=\frac{1}{t}\Big|\int_{0}^{2}f'(x)\mathrm{e}^{itx}\,dx\Big|<\frac{\varepsilon}{t}
$$
for $t>T_{\varepsilon}$, by step [](#choice-of-T){.pf-ref}, and $\varepsilon/t$ is the asserted bound. The hypotheses $f'(0)=f'(2)=0$ are not needed for this estimate: only $f(0)=f(2)=0$ makes the boundary term vanish. Those extra hypotheses would be needed to integrate by parts a second time and obtain the stronger decay $O(1/t^{2})$.
:::

:::

:::

:::
