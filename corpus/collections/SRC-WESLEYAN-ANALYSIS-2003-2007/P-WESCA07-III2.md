---
schema: qual/card@1
id: P-WESCA07-III2
kind: problem
title: "A quadratic Schwarz-type estimate from a derivative bound"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Section III, problem 2 (Summer 2007) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let $f$ be analytic on the unit disk $D$, with
$$
f(0)=f'(0)=0,
\qquad
|f'(z)|<1\quad(z\in D).
$$
Show that
$$
|f(z)|\le\frac{|z|^2}{2}
\qquad(z\in D).
$$

Hint: represent $f(z)$ as a path integral along a convenient path.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The derivative $f'$ maps $D$ into the unit disk and satisfies
$$
f'(0)=0.
$$


::: pf-proof

This is exactly the given hypothesis
$$
|f'(z)|<1
$$
for $z\in D$, together with $f'(0)=0$.

:::

:::

::: {.pf-step #s1-2}

For every $w\in D$,
$$
|f'(w)|\le |w|.
$$


::: pf-proof

The function $f'$ is holomorphic on $D$, maps $D$ into itself by step [](#s1-1){.pf-ref}, and vanishes at $0$. Schwarz's lemma therefore gives
$$
|f'(w)|\le|w|.
$$

:::

:::

::: {.pf-step #s1-3}

For every $z\in D$,
$$
f(z)=\int_0^1 f'(tz)\,z\,dt.
$$


::: pf-proof

Integrate $f'$ along the straight-line path
$$
\gamma(t)=tz,
\qquad 0\le t\le1.
$$
Since $f(0)=0$,
$$
f(z)-f(0)
=\int_\gamma f'(w)\,dw
=\int_0^1 f'(tz)\,z\,dt.
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{|f(z)|\le\frac{|z|^2}{2}}
$$
for every $z\in D$.


::: pf-proof

By steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref},
$$
\begin{aligned}
|f(z)|
&\le\int_0^1 |f'(tz)|\,|z|\,dt\\
&\le\int_0^1 t|z|^2\,dt\\
&=\frac{|z|^2}{2}.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required estimate.

:::

:::

:::
