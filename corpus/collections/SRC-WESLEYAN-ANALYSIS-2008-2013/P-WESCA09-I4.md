---
schema: qual/card@1
id: P-WESCA09-I4
kind: problem
title: 'Cauchy–Riemann equations are not sufficient for analyticity'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Section I, item 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
True or false: satisfying the Cauchy–Riemann equations on a domain $D$ is sufficient to conclude that a function is analytic on $D$.
Justify your answer.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The statement is
$$
\boxed{\mathrm{False}}.
$$


::: pf-proof

Consider
$$
f(z)=
\begin{cases}
e^{-1/z^4},&z\ne0,\\
0,&z=0.
\end{cases}
$$
For $z\ne0$, the function is holomorphic, so its real and imaginary parts
satisfy the Cauchy--Riemann equations there.

Write $f=u+iv$. Along the real axis,
$$
f(x)=e^{-1/x^4}\in\RR
$$
for $x\ne0$, and along the imaginary axis,
$$
f(iy)=e^{-1/y^4}\in\RR
$$
for $y\ne0$. Since
$$
\lim_{t\to0}\frac{e^{-1/t^4}}{t}=0,
$$
it follows that
$$
u_x(0,0)=u_y(0,0)=v_x(0,0)=v_y(0,0)=0.
$$
Thus the Cauchy--Riemann equations also hold at the origin.

However, for $z=t e^{i\pi/4}$ one has $z^4=-t^4$, and hence
$$
f(t e^{i\pi/4})=e^{1/t^4},
$$
which is unbounded as $t\to0^+$. Therefore $f$ is not continuous at $0$, so
it is not analytic on $\CC$. Thus the Cauchy--Riemann equations alone,
without an additional regularity hypothesis, are not sufficient.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives a counterexample satisfying the equations throughout a domain
but failing to be analytic there.

:::

:::

:::
