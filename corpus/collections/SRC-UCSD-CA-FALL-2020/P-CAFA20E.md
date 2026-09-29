---
schema: qual/card@1
id: P-CAFA20E
kind: problem
title: "Normal family characterized by an integral bound"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $\mathcal{F}$ be a non-empty family of analytic functions on the unit disc $\mathbb{D}$.
Assume for every $f \in \mathcal{F}$ it holds that $$\int_{\mathbb{D}} |f(z)|(1 - |z|)^5 \, dm < 10.$$ Prove $\mathcal{F}$ is a normal family.

Here $dm$ denotes the standard measure in $\mathbb{R}^2$ (i.e.\ $dm = dx\,dy$ for $z = x + iy$).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $f$ analytic on $\mathbb{D}$ and $z_0 \in \mathbb{D}$, the subharmonicity of $|f|$ gives
$$|f(z_0)| \le \frac{1}{\pi r^2} \int_{D(z_0, r)} |f(z)|\,dm(z)$$
for any $r$ with $D(z_0, r) \subseteq \mathbb{D}$.

::: pf-proof

mean value inequality for the subharmonic function $|f|$.

:::

:::

::: {.pf-step #s2}

For $z_0$ with $|z_0| < 1/2$, take $r = 1/4$; then $D(z_0, 1/4) \subseteq \mathbb{D}$ and $1 - |z| \ge 1/4$ on this disk.

::: pf-proof

if $|z_0| < 1/2$ and $|z - z_0| < 1/4$, then $|z| < 3/4$, so $1 - |z| > 1/4$.

:::

:::

::: {.pf-step #s3}

Hence $|f(z_0)| \le \frac{1}{\pi (1/4)^2} \int_{D(z_0,1/4)} |f|\,dm \le \frac{16}{\pi} \cdot 4^5 \int_{D(z_0,1/4)} |f| (1-|z|)^5\,dm$.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, using $(1-|z|)^{-5} \le 4^5$ on the disk.

:::

:::

::: {.pf-step #s4}

Therefore $|f(z_0)| \le \frac{16 \cdot 4^5}{\pi} \cdot 10 =: C$ for all $|z_0| < 1/2$.

::: pf-proof

Step [](#s3){.pf-ref} and the hypothesis $\int_{\mathbb{D}} |f|(1-|z|)^5\,dm < 10$.

:::

:::

::: {.pf-step #s5}

Hence $\mathcal{F}$ is uniformly bounded on the disk $|z| < 1/2$.

::: pf-proof

Step [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

By Montel's theorem, a uniformly bounded family of analytic functions on a domain is normal.

::: pf-proof

Montel's theorem.

:::

:::

::: {.pf-step #s7}

Therefore $\mathcal{F}$ is a normal family.

::: pf-proof

Steps [](#s5){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref}.

:::

:::

:::
