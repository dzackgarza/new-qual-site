---
schema: qual/card@1
id: P-UCLAB02F-01
kind: problem
title: Positive distance between disjoint compact and closed sets
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Fall 2002 PDF.
---

::: {.problem}
Let $K$ be a compact subset and $F$ a closed subset of a metric space $X$.
Suppose $K\cap F=\varnothing$.
Prove that
$$
0<\inf\{d(x,y):x\in K,\ y\in F\}.
$$
:::

::: {.solution}

If $K=\varnothing$ or $F=\varnothing$, the set of distances is empty; with the extended-real convention $\inf\varnothing=+\infty$, the conclusion is immediate. If the infimum is understood only for nonempty subsets of $\RR$, then nonemptiness of $K$ and $F$ is implicit. Consider therefore the substantive case $K,F\ne\varnothing$.

::: pf

::: {.pf-step #s1-1}

For every $x\in K$, there exists $r_x>0$ such that
$$
B(x,r_x)\cap F=\varnothing.
$$


::: pf-proof

Since $K\cap F=\varnothing$, every $x\in K$ lies in the complement $X\setminus F$. The set $F$ is closed, so $X\setminus F$ is open. Hence there is $r_x>0$ with
$$
B(x,r_x)\subseteq X\setminus F.
$$

:::

:::

::: {.pf-step #s1-2}

There are points $x_1,\ldots,x_m\in K$ such that
$$
K\subseteq\bigcup_{i=1}^m B\left(x_i,\frac{r_{x_i}}2\right).
$$


::: pf-proof

The balls
$$
\left\{B\left(x,\frac{r_x}{2}\right):x\in K\right\}
$$
form an open cover of $K$. Since $K$ is compact, a finite subcover exists.

:::

:::

::: {.pf-step #s1-3}

Let
$$
\delta=\min_{1\le i\le m}\frac{r_{x_i}}2.
$$
Then $\delta>0$ and
$$
d(x,y)\ge\delta
$$
for every $x\in K$ and $y\in F$.


::: pf-proof

The minimum is positive because it is the minimum of finitely many positive numbers.

Fix $x\in K$ and $y\in F$. By step [](#s1-2){.pf-ref}, choose $i$ such that
$$
d(x,x_i)<\frac{r_{x_i}}2.
$$
By step [](#s1-1){.pf-ref}, $y\notin B(x_i,r_{x_i})$, so
$$
d(x_i,y)\ge r_{x_i}.
$$
The triangle inequality gives
$$
d(x,y)
\ge
d(x_i,y)-d(x,x_i)
>
r_{x_i}-\frac{r_{x_i}}2
=
\frac{r_{x_i}}2
\ge\delta.
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{
0<
\inf\{d(x,y):x\in K,\ y\in F\}.
}
$$


::: pf-proof

Step [](#s1-3){.pf-ref} shows that every element of the distance set is at least the positive number $\delta$. Hence its infimum is at least $\delta>0$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion in the nonempty case, and the opening observation covers the empty-set convention.

:::

:::

:::
