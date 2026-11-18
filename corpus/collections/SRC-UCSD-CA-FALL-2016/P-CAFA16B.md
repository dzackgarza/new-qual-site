---
schema: qual/card@1
id: P-CAFA16B
kind: problem
title: 'Convergence of $\sum_n f(z^n)$ for a self-map $f$ of $\DD$ with $f(0)=0$'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Assume that $f: \DD \to \DD$ is an analytic function such that $f(0) = 0$.
Show that $g(z) = \sum_{n=1}^{\infty} f(z^n)$ converges to an analytic function on $\DD$.
:::

::: {.remark}
The official Fall 2016 exam starts the sum at $n=0$. Since $z^0=1$ and $f$ is only defined on the open unit disk, that term is undefined. The intended series necessarily starts at $n=1$.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/FA16_220_Complex_Analysis_Qual.pdf` and no solutions sheet accompanies it, so the argument below is the card's own. It rests on three standard facts, each named at the step where it is used: Schwarz's lemma, the Weierstrass $M$-test, and the theorem that a locally uniform limit of holomorphic functions is holomorphic. The remark before the solution keeps the correction of the printed index, which starts the series at $n=0$ although $z^{0}=1$ lies outside $\DD$.

Throughout, $\DD=\theset{w\in\CC\mid\abs{w}<1}$ and $f\colon\DD\to\DD$ is analytic with $f(0)=0$.

::: pf

::: {.pf-step #schwarz}
$\abs{f(w)}\leq\abs{w}$ for every $w\in\DD$.

::: pf-proof
This is Schwarz's lemma, whose hypotheses are exactly that $f$ maps $\DD$ into $\DD$ analytically and fixes $0$; its conclusion is $\abs{f(w)}\leq\abs{w}$ and moreover $\abs{f'(0)}\leq1$.
:::

:::

::: {.pf-step #bound-term}
For $0<r<1$ and $\abs{z}\leq r$ one has $\abs{f(z^{n})}\leq r^{n}$ for every $n\geq1$.

::: pf-proof
If $\abs{z}\leq r<1$ then $\abs{z^{n}}=\abs{z}^{n}\leq r^{n}<1$, so $z^{n}\in\DD$ and step [](#schwarz){.pf-ref} applies to $w=z^{n}$, giving $\abs{f(z^{n})}\leq\abs{z^{n}}=\abs{z}^{n}\leq r^{n}$.
:::

:::

::: {.pf-step #uniform-on-discs}
$\sum_{n\geq1}f(z^{n})$ converges uniformly on each closed disc $\overline{D(0,r)}$ with $0<r<1$.

::: pf-proof
By step [](#bound-term){.pf-ref} the $n$-th summand is bounded on $\overline{D(0,r)}$ by $M_{n}\coloneqq r^{n}$, and $\sum_{n}M_{n}=\frac{r}{1-r}<\infty$ because $0<r<1$. The Weierstrass $M$-test therefore gives uniform convergence of the series of functions on that disc, and with it absolute convergence at each point of it.
:::

:::

::: {.pf-step #defined}
$g(z)\coloneqq\sum_{n\geq1}f(z^{n})$ is defined at every $z\in\DD$.

::: pf-proof
Given $z\in\DD$ choose $r$ with $\abs{z}<r<1$, possible because $\abs{z}<1$; then $z\in\overline{D(0,r)}$ and step [](#uniform-on-discs){.pf-ref} shows the series converges at $z$.
:::

:::

::: pf-step
Therefore $g$ is analytic on $\DD$.

::: pf-proof
Each summand $z\mapsto f(z^{n})$ is holomorphic on $\DD$, being a composite of the holomorphic maps $z\mapsto z^{n}$ and $f$. By step [](#uniform-on-discs){.pf-ref} the series converges uniformly on every closed disc $\overline{D(0,r)}\subset\DD$, that is locally uniformly on $\DD$, and a locally uniform limit of holomorphic functions is holomorphic (Weierstrass's theorem). So $g$ is holomorphic, hence analytic, on $\DD$, which is the assertion to be proved.
:::

:::

:::

:::
