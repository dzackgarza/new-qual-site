---
schema: qual/card@1
id: P-UGARAF18-05
kind: problem
title: The layer-cake formula $\int_\RR f=\int_0^\infty m(\{f>t\})\,dt$ for $f\ge0$
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Measure Theory
relations: []
review: draft
---

::: {.problem}
Let $f\geq 0$ be a Lebesgue measurable function on $\RR$. Show that
$$
\int_{\RR}f=\int_{0}^{\infty}m(\{x:f(x)>t\})\,dt.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The set
$$
A=\theset{(x,t)\in\RR\times(0,\infty)\suchthat f(x)>t}
$$
is Lebesgue measurable in $\RR^2$.

::: pf-proof

The functions $F(x,t)=f(x)$ and $G(x,t)=t$ are Lebesgue measurable on $\RR^2$: $F^{-1}(U)=f^{-1}(U)\times\RR$ is a product of a measurable set with $\RR$, and $G$ is continuous. Hence $F-G$ is measurable on $\RR^2$ (on the set where $f=\infty$, $F-G=\infty$, which is still a measurable condition), and $A=\{F-G>0\}\cap(\RR\times(0,\infty))$.

:::

:::

::: {.pf-step #s2}

$$
\int_\RR\int_0^\infty\chi_A(x,t)\,dt\,dx=\int_0^\infty\int_\RR\chi_A(x,t)\,dx\,dt.
$$

::: pf-proof

$\chi_A$ is nonnegative and measurable by step [](#s1){.pf-ref}, so Tonelli's theorem for the $\sigma$-finite space $\RR\times(0,\infty)$ with Lebesgue measure allows the order of integration to be exchanged.

:::

:::

::: {.pf-step #s3}

For each $x$, $\int_0^\infty\chi_A(x,t)\,dt=f(x)$; for each $t>0$, $\int_\RR\chi_A(x,t)\,dx=m(\{x:f(x)>t\})$.

::: pf-proof

For fixed $x$, the section $\{t>0:t<f(x)\}$ is the interval $(0,f(x))$, of length $f(x)$ (also when $f(x)=0$ or $f(x)=\infty$). For fixed $t$, the section is $\{x:f(x)>t\}$.

:::

:::

::: pf-qed

Substituting step [](#s3){.pf-ref} into both sides of step [](#s2){.pf-ref} gives
$$
\int_\RR f=\int_0^\infty m(\{x:f(x)>t\})\,dt.
$$

:::

:::

:::
