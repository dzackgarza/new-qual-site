---
schema: qual/card@1
id: P-FSSHC
kind: problem
title: Extreme points of the unit ball of convergent sequences, and whether the ball
  is their closed convex hull
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Functional Analysis
  - Norms
relations: []
review: draft
---

::: {.problem}
Let $C$ denote the Banach space of all convergent sequences under the norm $\|\cdot\|_\infty$.
Compute the extreme points of the unit ball $B$ of $C$ and determined that whether $B$ is the closed convex hull of its extreme points.
:::

::: {.solution}
Fix a $a\in B$, if there is a $m$ such that $|a(m)|<1$.
then there is a number $\delta$ such that $|a(m)-\delta|\le 1$ and $|a(m)+\delta|\le 1$.
Now define $b_1,b_2\in B$ such that $b_1(n)=a(n)$ whenever $n\ne m$ and $b_1(m)=a(m)+\delta$.
In the same manner, define $b_2(n)=a(n)$ whenever $n\ne m$ and $b_1(m)=a(m)-\delta$.
Then $a=(b_1+b_2)/2$.
Thus $a$ is not an extreme point.

If for all $n$, $|a_n|=1$.
Let $a=(b_1+b_2)/2$.
Since $|b_i(n)|\le 1$ for all $n$, $b_1(n)=b_2(n)=a(n)$, which implies that $a$ is an extreme point.
Thus $\text{Ext}(B)=\{a:\forall n, |a(n)|=1 \text{ and } \exists N,\forall n>N\ a(n)\equiv 1 \text{ or } a(n)\equiv -1.\}$

(Not sure) I think $\overline{\text{conv}}(\text{Ext}(B))\ne B$.
Let $e_0=(1,1,1,1,\dots)$, $e_n=(0,\dots,0,1,0,\dots)$ for $n\ge 1$.
It can be seen that $\pm e_n\in\text{conv}(\text{Ext}(B))$ for all $n\ge 0$.
Consider $\{e_n : n\ge 0\}$ form a basis of $C$.
Then $\overline{\text{conv}}(\text{Ext}(B))=B$ iff $\sum_{n=0}^k \alpha_n e_n \in \overline{\text{conv}}(\text{Ext}(B))$ for $1\ge|\alpha_n|\to 0$.
This may induce a contradiction of the convexity.
Like consider $(1/n)$.
:::
