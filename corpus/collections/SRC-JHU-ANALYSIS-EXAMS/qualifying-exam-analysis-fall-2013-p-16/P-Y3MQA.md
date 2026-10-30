---
schema: qual/card@1
id: P-Y3MQA
kind: problem
title: Schwarz-Pick type inequality for holomorphic self-map of disk
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both displayed inequalities with Spring 2014 problem 5 on PDF page 15, including the different signs in their denominators."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the disk normalization, both reverse-triangle estimates, positivity of the denominators, and the lower bound when its numerator is negative."
---

::: {.problem}
Let $D = \{z \in \CC : \abs{z} < 1\}$ and $f : D \to D$ be a holomorphic function.
Prove

$$\frac{\abs{f(0)} - \abs{z}}{1 + \abs{f(0)} \cdot \abs{z}} \leq \abs{f(z)} \leq \frac{\abs{f(0)} + \abs{z}}{1 - \abs{f(0)} \cdot \abs{z}}, \quad \forall z \in D.$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Normalization at the origin gives a Schwarz-lemma estimate.

::: pf-proof

Put $c=f(0)$ and define
$$
H(z)=\frac{f(z)-c}{1-\overline c f(z)}.
$$
The denominator is nonzero because $\abs{c},\abs{f(z)}<1$.
For every $w\in D$,
$$
1-\abs{\frac{w-c}{1-\overline c w}}^2
=\frac{(1-\abs{c}^2)(1-\abs{w}^2)}{\abs{1-\overline c w}^2}>0.
$$
Thus $H:D\to D$ is holomorphic and $H(0)=0$.
Schwarz's lemma gives $\abs{H(z)}\leq\abs{z}$ [@SS03], or
$$
\abs{f(z)-c}\leq \abs{z}\,\abs{1-\overline c f(z)}.
$$

:::

:::

::: pf-step

The triangle inequalities give both requested bounds.

::: pf-proof

For fixed $z\in D$, write $a=\abs{c}$, $b=\abs{f(z)}$ and
$r=\abs{z}$. Step [](#s1){.pf-ref} implies
$$
\abs{b-a}\leq \abs{f(z)-c}\leq r(1+ab).
$$
Using $b-a\leq r(1+ab)$ gives
$b(1-ar)\leq a+r$. Since $ar<1$, division yields
$b\leq(a+r)/(1-ar)$.
Using $a-b\leq r(1+ab)$ instead gives
$a-r\leq b(1+ar)$, hence $b\geq(a-r)/(1+ar)$.
The latter denominator is positive even when $a-r<0$,
so no additional case assumption is needed. Substituting
back gives the two stated inequalities at every point,
including $z=0$.

:::

:::

:::

:::
