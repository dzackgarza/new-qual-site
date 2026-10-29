---
schema: qual/card@1
id: P-UCLARA16S-11
kind: problem
title: Holomorphic functions cannot approximate $1/z$ on the unit circle
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Assume that $f(z)$ is holomorphic on $|z|<2$. Show that
$$
\max_{|z|=1}\left|f(z)-\frac1z\right|\ge1.
$$
:::

::: {.solution}

Let
$$
M
\coloneqq
\max_{|z|=1}
\left|f(z)-\frac1z\right|.
$$

::: pf

::: {.pf-step #s1-1}

If $\gamma$ is the positively oriented unit circle, then
$$
\int_\gamma
\left(f(z)-\frac1z\right)\,dz
=
-2\pi i.
$$


::: pf-proof

Since $f$ is holomorphic on the disk $|z|<2$, Cauchy's theorem gives
$$
\int_\gamma f(z)\,dz=0.
$$
Also,
$$
\int_\gamma\frac{dz}{z}=2\pi i.
$$
Subtracting gives the asserted value.

:::

:::

::: {.pf-step #s1-2}

One has
$$
2\pi
\le
2\pi M.
$$


::: pf-proof

Taking absolute values in step [](#s1-1){.pf-ref} and applying the ML inequality,
$$
\begin{aligned}
2\pi
&=
\left|
\int_\gamma
\left(f(z)-\frac1z\right)\,dz
\right|\\
&\le
\operatorname{length}(\gamma)
\max_{|z|=1}
\left|f(z)-\frac1z\right|\\
&=
2\pi M.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\max_{|z|=1}
\left|f(z)-\frac1z\right|
\ge1}.
$$


::: pf-proof

Divide the inequality in step [](#s1-2){.pf-ref} by $2\pi>0$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required estimate.

:::

:::

:::
