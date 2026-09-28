---
schema: qual/card@1
id: P-BKS03-7A
kind: problem
title: When a union of subgroups is a subgroup
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
(a) If $H_1,H_2\le G$ and $H_1\cup H_2$ is a subgroup, prove that $H_1\subseteq H_2$ or $H_2\subseteq H_1$.

(b) For every $n\ge3$, construct a group $G$ with subgroups $H_1,\dots,H_n$, none contained in another, such that $H_1\cup\cdots\cup H_n$ is a subgroup.
:::

::: {.solution}
(a) If not, there exists $h_1\in H_1-H_2$ and $h_2\in H_2-H_1$. Since $h_1$ and $h_2$ belong to the subgroup $H_1\cup H_2$, we also have $h_1h_2\in H_1\cup H_2$. If $h_1h_2\in H_1$, we get the contradiction $h_2=h_1^{-1}(h_1h_2)\in H_1$. If $h_1h_2\in H_2$, we get the contradiction $h_1=(h_1h_2)h_2^{-1}\in H_2$.

(b) Let $G=(\ZZ/2\ZZ)^{n-1}$. For $1\leq i\leq n-1$, let $H_i=\{(x_1,\ldots,x_{n-1})\in G:x_i=0\}$. Then $H_1\cup\cdots\cup H_{n-1}=G-\{(1,1,\ldots,1)\}$. Let $H_n=\{(x_1,\ldots,x_{n-1})\in G:x_1+x_2=0\}$. Then $(1,1,\ldots,1)\in H_n$, so $H_1\cup\cdots\cup H_n=G$. No $H_i$ is contained in any other, since they are distinct subgroups of the same order.
:::
