---
schema: qual/card@1
id: P-UCLARA13F-09
kind: problem
title: Separate boundedness of a bilinear form implies joint boundedness
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Fall 2013 section.
---

::: {.problem}
Let $X$ be a Banach space, $Y$ a normed linear space, and $B:X\times Y\to\RR$ bilinear.
Suppose that for each $x\in X$ there is $C_x\ge0$ with
$$
\abs{B(x,y)}\le C_x\norm{y}\qquad(y\in Y),
$$
and for each $y\in Y$ there is $C_y\ge0$ with
$$
\abs{B(x,y)}\le C_y\norm{x}\qquad(x\in X).
$$
Show that there is $C\ge0$ such that
$$
\abs{B(x,y)}\le C\norm{x}\norm{y}
$$
for all $x\in X$ and $y\in Y$.
:::

::: {.solution}

For each $y\in Y$, regard $B(\,·\,,y)$ as a bounded linear functional on the Banach space $X$.

::: pf

::: {.pf-step #s1-1}

For each $y\in Y$, define
$$
T_y:X\to\RR,
\qquad
T_y(x)=B(x,y).
$$
Then $T_y\in X^*$.


::: pf-proof

Bilinearity makes $T_y$ linear. The second hypothesis gives
$$
\abs{T_y(x)}=\abs{B(x,y)}\leq C_y\norm{x},
$$
so $T_y$ is bounded.

:::

:::

::: {.pf-step #s1-2}

Consider the family
$$
\mathcal T=\{T_y:\norm{y}\leq1\}\subset X^*.
$$
For each fixed $x\in X$, this family is pointwise bounded:
$$
\sup_{\norm{y}\leq1}\abs{T_y(x)}<\infty.
$$


::: pf-proof

The first hypothesis gives a constant $C_x$ such that
$$
\abs{T_y(x)}=\abs{B(x,y)}\leq C_x\norm{y}.
$$
Thus for $\norm{y}\leq1$,
$$
\abs{T_y(x)}\leq C_x,
$$
and taking the supremum gives a finite bound.

:::

:::

::: {.pf-step #s1-3}

By the Uniform Boundedness Principle, there exists $C\geq0$ such that
$$
\norm{T_y}_{X^*}\leq C
\qquad\text{whenever }\norm{y}\leq1.
$$


::: pf-proof

The domain $X$ is Banach by hypothesis, every $T_y$ in the family is a bounded linear map by step [](#s1-1){.pf-ref}, and the family is pointwise bounded by step [](#s1-2){.pf-ref}. The Uniform Boundedness Principle therefore gives
$$
\sup_{\norm{y}\leq1}\norm{T_y}<\infty.
$$
Call this supremum $C$.

:::

:::

::: {.pf-step #s1-4}

If $\norm{y}\leq1$, then for every $x\in X$,
$$
\abs{B(x,y)}\leq C\norm{x}.
$$


::: pf-proof

By definition of operator norm,
$$
\abs{B(x,y)}=\abs{T_y(x)}\leq\norm{T_y}\,\norm{x},
$$
and step [](#s1-3){.pf-ref} bounds $\norm{T_y}$ by $C$.

:::

:::

::: {.pf-step #s1-5}

For arbitrary $y\ne0$, bilinearity gives
$$
B(x,y)=\norm{y}B\left(x,\frac y{\norm{y}}\right).
$$


::: pf-proof

Since $y=\norm{y}(y/\norm{y})$, linearity in the second argument gives the identity.

:::

:::

::: {.pf-step #s1-6}

Therefore, for all $x\in X$ and $y\in Y$,
$$
\boxed{\abs{B(x,y)}\leq C\norm{x}\norm{y}.}
$$


::: pf-proof

If $y=0$, both sides give the desired inequality immediately. If $y\ne0$, apply step [](#s1-4){.pf-ref} to the unit vector $y/\norm{y}$ and use step [](#s1-5){.pf-ref}:
$$
\abs{B(x,y)}
=\norm{y}\abs{B\left(x,\frac y{\norm{y}}\right)}
\leq C\norm{x}\norm{y}.
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required joint boundedness estimate.

:::

:::

:::
