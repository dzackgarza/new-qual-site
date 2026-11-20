---
schema: qual/card@1
id: P-JHUU51RA1
kind: problem
title: "Quantitative Riemann-Lebesgue decay under vanishing endpoint conditions"
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
  note: Checked against entry 1 of the JHU Real Analysis Qualifying Exam on p. 51 of the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with three steps, each carrying a `pf-proof`, and the remark that follows is kept outside the
    proof. The statement and the estimate are unchanged. Cited by number only: integration by
    parts and the Riemann--Lebesgue lemma. Checked: that the boundary term vanishes using
    $f(0)=f(2)=0$ alone, that $f'$ continuous on a compact interval gives $f'\in L^1$, that the
    convergence of the Fourier transform is of its modulus too, and that the threshold may be
    taken positive.
---

::: {.problem}
Let $f:[0,2]\to\RR$ be $C^1$ and suppose
$$
f(0)=f'(0)=f(2)=f'(2)=0.
$$
Prove that for every $\varepsilon>0$ there exists $t_\varepsilon>0$ such that
$$
\abs{\int_0^2 f(x)e^{itx}\,dx}\le\frac{\varepsilon}{t}
\qquad(t\ge t_\varepsilon).
$$
:::

::: {.solution}

::: pf

::: pf-step

For $t>0$, integration by parts and the endpoint conditions on $f$ give
$$
\int_0^2 f(x)e^{itx}\,dx
=\left[\frac{f(x)e^{itx}}{it}\right]_0^2
-\frac1{it}\int_0^2 f'(x)e^{itx}\,dx
=-\frac1{it}\int_0^2 f'(x)e^{itx}\,dx.
$$

::: pf-proof

$f$ is $C^1$ and $e^{itx}$ is $C^1$, so the product is $C^1$ on $[0,2]$ and integration by parts applies with $u=f$, $dv=e^{itx}dx$, $v=e^{itx}/(it)$: the boundary term is $\frac{f(2)e^{2it}}{it}-\frac{f(0)}{it}$, and $f(0)=f(2)=0$ makes it vanish. The remaining integral stands, with the constant $-\frac1{it}$ in front. (Only $f(0)=f(2)=0$ is used here, not the vanishing of $f'$ at the endpoints.)

:::

:::

::: pf-step

Since $f'$ is continuous on $[0,2]$ it lies in $L^1([0,2])$, and by the Riemann--Lebesgue lemma
$$
\int_0^2 f'(x)e^{itx}\,dx\longrightarrow0
\qquad(t\to\infty).
$$

::: pf-proof

A continuous function on the compact interval $[0,2]$ is bounded, so $\int_0^2\abs{f'}<\infty$ and $f'\in L^1$. The Riemann--Lebesgue lemma states that the Fourier transform of an $L^1$ function tends to $0$ at infinity; here $\int_0^2f'(x)e^{itx}dx=\widehat{f'}(-t/2\pi)$ up to the normalising constant, so it tends to $0$ as $t\to\infty$. In particular the limit is a real number, its modulus tending to $0$ as well.

:::

:::

::: pf-step

Hence for the given $\varepsilon>0$ there is $t_\varepsilon>0$ with
$$
\abs{\int_0^2 f'(x)e^{itx}\,dx}\le\varepsilon
\qquad(t\ge t_\varepsilon),
$$
and substituting into the integration-by-parts identity gives
$$
\abs{\int_0^2 f(x)e^{itx}\,dx}\le\frac{\varepsilon}{t}
\qquad(t\ge t_\varepsilon).
$$

::: pf-proof

Convergence to $0$ means that for every $\varepsilon>0$ there is $T$ with $\abs{\int_0^2f'e^{itx}}\le\varepsilon$ for all $t\ge T$; taking $t_\varepsilon=\max(T,1)$ makes the threshold positive. Multiplying the identity of step 1 by the modulus gives $\abs{\int_0^2fe^{itx}}=\frac1t\abs{\int_0^2f'e^{itx}}\le\frac\varepsilon t$ for $t\ge t_\varepsilon$, since $t>0$.

:::

:::

:::

:::

::: {.remark}
The argument uses only $f(0)=f(2)=0$ and $f'\in L^1([0,2])$.
:::
