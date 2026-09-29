---
schema: qual/card@1
id: P-AZOFF-D07
kind: problem
title: An entire function with $|f(z)|\le|z|^{1/2}$ for large $|z|$ is constant
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Integrals and Cauchy’s theorem, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    Page 4 of the retained PDF and its text layer both print the positive
    exponent 1/2 and ask to prove that f is the zero function. The printed
    conclusion is false: f identically 1 satisfies the stated growth bound.
    The card preserves the printed hypothesis and corrects the requested
    conclusion to constancy; the source's intended stronger hypothesis, if
    any, is unknown.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For every R>10, Cauchy's coefficient formula gives
    |a_n| <= R^(1/2-n). Letting R tend to infinity forces every coefficient
    of positive degree to vanish, so the entire function is constant.
---

::: {.problem}
Suppose $f : \mathbb { C } \to \mathbb { C }$ is entire and $| f ( z ) | \leq | z | ^ { \frac { 1 } { 2 } }$ whenever $| z | > 1 0$ . Prove that $f$ is constant.
:::

::: {.solution}
Write the Taylor series of $f$ at the origin as
$$
f(z)=\sum_{n=0}^{\infty}a_nz^n.
$$

::: pf

::: {.pf-step #s1}
For every $R>10$ and every integer $n\geq1$,
$$
\abs{a_n}\leq R^{1/2-n}.
$$

::: pf-proof
By Cauchy's coefficient formula,
$$
a_n
=
\frac{1}{2\pi i}
\int_{\abs{\zeta}=R}
\frac{f(\zeta)}{\zeta^{n+1}}
\,d\zeta.
$$
Since $R>10$, the hypothesis gives
$$
\abs{f(\zeta)}\leq R^{1/2}
$$
on the circle $\abs{\zeta}=R$. Hence
$$
\begin{aligned}
\abs{a_n}
&\leq
\frac{1}{2\pi}
(2\pi R)
\frac{R^{1/2}}{R^{n+1}}\\
&=
R^{1/2-n}.
\end{aligned}
$$
:::

:::

::: {.pf-step #s2}
For every integer $n\geq1$,
$$
a_n=0.
$$

::: pf-proof
Fix $n\geq1$. Step [](#s1){.pf-ref} holds for every $R>10$, while
$$
R^{1/2-n}\longrightarrow0
$$
as $R\to\infty$. Therefore
$$
\abs{a_n}=0.
$$
:::

:::

::: {.pf-step #s3}
The function $f$ is constant.

::: pf-proof
By step [](#s2){.pf-ref}, every coefficient of positive degree in the Taylor expansion
of $f$ vanishes. Thus
$$
f(z)=a_0
$$
for every $z\in\CC$.
:::

:::

::: pf-qed
Step [](#s3){.pf-ref} is the corrected conclusion.
:::

:::
:::

::: {.remark}
Erratum: the source asks to prove that $f$ is the zero function. This is
false. The constant function
$$
f\equiv1
$$
satisfies the printed hypothesis because
$$
1<\sqrt{10}<\abs{z}^{1/2}
$$
whenever $\abs{z}>10$. The printed growth bound forces constancy by
step [](#s3){.pf-ref} of the solution, but it does not force the constant to be zero.
:::
