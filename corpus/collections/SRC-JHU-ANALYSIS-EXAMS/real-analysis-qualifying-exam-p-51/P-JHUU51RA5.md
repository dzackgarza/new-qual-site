---
schema: qual/card@1
id: P-JHUU51RA5
kind: problem
title: "$\\|f\\|_p\\to\\|f\\|_\\infty$ as $p\\to\\infty$ for $f\\in L^1\\cap L^\\infty$"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against entry 5 of the JHU Real Analysis Qualifying Exam on p. 51 of the preserved packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Verified the upper and lower bounds and the essential-supremum argument.
---

::: {.problem}
Let $(X, \mathcal{M}, \mu)$ be a measure space, and let $f \in L^{1}(\mu) \cap L^{\infty}(\mu)$.
Prove that:
$$
\lim_{p \to \infty} \|f\|_p = \|f\|_{\infty}.
$$
:::

::: {.solution}
If $\norm f_\infty=0$ then $f=0$ almost everywhere and every $\norm f_p$ is $0$. Assume $\norm f_\infty>0$, so that $0<\norm f_1<\infty$.

::: pf

::: {.pf-step #s1}

$\limsup_{p\to\infty}\norm f_p\le\norm f_\infty$.

::: pf-proof

For $p>1$, $\int\abs f^p\le\norm f_\infty^{p-1}\norm f_1$, so $\norm f_p\le\norm f_\infty^{(p-1)/p}\norm f_1^{1/p}$, and the right side tends to $\norm f_\infty$.

:::

:::

::: {.pf-step #s2}

$\liminf_{p\to\infty}\norm f_p\ge\norm f_\infty$.

::: pf-proof

Let $0<\eps<\norm f_\infty$ and $E=\{\abs f>\norm f_\infty-\eps\}$. By definition of the essential supremum $\mu(E)>0$, and $\mu(E)\le\norm f_1/(\norm f_\infty-\eps)<\infty$. Then $\norm f_p\ge(\norm f_\infty-\eps)\mu(E)^{1/p}$, whose limit is $\norm f_\infty-\eps$. Let $\eps\to0$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give $\lim_{p\to\infty}\norm f_p=\norm f_\infty$.

:::

:::

:::
