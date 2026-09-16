---
schema: qual/card@1
id: FF-7NXLO
kind: fact
title: Hahn--Banach theorem
prompts:
- What is the Hahn-Banach theorem?
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Dual Spaces
relations: []
review: draft
---

::: {.fact}
Let $V$ be a real vector space and let $p\colon V\to\RR$ be sublinear, that is, $p(x+y)\leq p(x)+p(y)$ and $p(tx) = tp(x)$ for all $x, y\in V$ and $t\geq 0$.
Let $U\subseteq V$ be a linear subspace and let $\phi\colon U\to\RR$ be linear with $\phi(u)\leq p(u)$ for all $u\in U$.
Then there exists a linear map $\tilde\phi\colon V\to\RR$ such that $\tilde\phi(u) = \phi(u)$ for all $u\in U$ and $\tilde\phi(x)\leq p(x)$ for all $x\in V$.
:::
