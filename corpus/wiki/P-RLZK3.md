---
schema: qual/card@1
id: P-RLZK3
kind: problem
title: "The question as written on the original qual has several errors."
classification:
  areas:
  - complex-analysis
  topics:
  - blaschke-factors
  - schwarz-lemma
  - geometry
relations: []
review: draft
---
:::{.warnings}
The question as written on the original qual has several errors.
What is below is the correct version of the inequality.
:::

:::{.problem title="?"}
1. Let $z_{1}$ and $z_{2}$ be two complex numbers.

(a) Show that 
\[
\left|1-\bar{z}_{1} z_{2}\right|^{2}-\left|z_{1}-z_{2}\right|^{2}=\left(1-\left|z_{1}\right|^{2}\right)\left(1-\left|z_{2}\right|^2\right)
\]

(b) Show that if $\left|z_{1}\right|<1$ and $\left|z_{2}\right|<1$, then $\left|\frac{z_{1}-z_{2}}{1-\bar{z}_{1} z_{2}}\right|<1 .$

(c) Assume that $z_{1} \neq z_{2}$. Show that $\left|\frac{z_{1}-z_{2}}{1-\bar{z}_{1} z_{2}}\right|=1$ if only if $\left|z_{1}\right|=1$ or $\left|z_{2}\right|=1$.
:::

:::{.solution}
**Part 1**:
For ease of notation, let $z=z_1$ and $w=z_2$
We want to show
\[
\abs{1- z\bar{w}} - \abs{z-w}^2 
= \qty{{1 - \abs{z}^2 }} \qty{{1 - \abs{w}^2}}
.\]

So write
\[
\abs{1- z\bar{w}} - \abs{z-w}^2 
&= (1-z\bar w)(1-\bar z w) - (z-w)(\bar z - \bar w) \\
&= 1 - z\bar w - \bar z w - \abs{z}^2\abs{w}^2 - \abs{z}^2 - \abs{w}^2 + w\bar{z} + z\bar{w} \\
&= 1 - \abs{z}^2\abs{w}^2 - \abs{z}^2 - \abs{w}^2 \\
&=(1-\abs z^2)(1-\abs w^2)
.\]


**Part 2 and 3**:
\[
\abs{z-w \over 1 - \bar z w}^2 \leq 1 
&\iff 0 \leq \abs{1 - \bar z w}^2 - \abs{z-w}^2 \\
&\iff 0 \leq (1 - \abs z^2 )(1 - \abs w^2)
,\]
where we've used part 1.
But this is clearly true when $\abs{z}, \abs{w} < 1$, so the RHS is positive.
Moreover if $\abs{z} = \abs{w} = 1$, the RHS is zero, yielding equalities at every step instead.


:::

