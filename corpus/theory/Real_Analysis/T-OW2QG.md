---
schema: qual/card@1
id: T-OW2QG
kind: theorem
title: Hahn--Banach theorem
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Dual Spaces
relations: []
review: draft
---

::: {.theorem}
Let $\mathcal X$ be a real vector space and let $p\colon \mathcal X\to\RR$ be sublinear, that is, $p(x+y) \leq p(x) + p(y)$ and $p(\lambda x) = \lambda p(x)$ for all $x,y\in \mathcal X$ and all $\lambda \geq 0$.
Let $\mathcal M \subseteq \mathcal X$ be a linear subspace and $f\colon\mathcal M\to\RR$ a linear functional with $f \leq p$ on $\mathcal M$.
Then there exists a linear functional $F\colon\mathcal X\to\RR$ with $\ro{F}{\mathcal M} = f$ and $F \leq p$ on $\mathcal X$.

Let $\mathcal X$ be a complex vector space and let $p\colon\mathcal X\to\RR$ be a seminorm, that is, $p(x+y) \leq p(x) + p(y)$ and $p(\lambda x) = \abs{\lambda} p(x)$ for all $x,y\in \mathcal X$ and all $\lambda \in\CC$.
Let $\mathcal M \subseteq \mathcal X$ be a linear subspace and $f\colon\mathcal M\to\CC$ a [[D-EPSKF|linear functional]] with $\abs f \leq p$ on $\mathcal M$.
Then there exists a linear functional $F\colon\mathcal X\to\CC$ with $\ro{F}{\mathcal M} = f$ and $\abs F \leq p$ on $\mathcal X$ [@Fol13, Theorems 5.6 and 5.7].
:::

::: {.remark}
The proof extends $f$ one dimension at a time and applies Zorn's lemma.
:::

::: {.example}
The extension $F$ need not be unique.
On $\mathcal X=\RR^2$ let $p(x)\coloneqq\abs{x_1}+\abs{x_2}$, $\mathcal M\coloneqq\RR\times\theset{0}$, and $f(x_1,0)\coloneqq x_1$.
For every $c\in[-1,1]$, the functional $F_c(x)\coloneqq x_1+cx_2$ extends $f$ and satisfies $F_c\leq p$.
:::

::: {.corollary}
Let $\mathcal X$ be a normed vector space over $\RR$ or $\CC$ with dual space $\mathcal X\dual$ of continuous linear functionals and [[D-T4LOC|dual norm]].

1. If $\mathcal M \subseteq \mathcal X$ is a closed linear subspace and $x\in\mathcal X\setminus\mathcal M$, put $\delta \coloneqq \inf_{y\in \mathcal M}\norm{x-y}$. Then there is $f \in \mathcal X\dual$ with $\norm{f} = 1$, $\ro f {\mathcal M} = 0$, and $f(x) = \delta$.

2. For each $x\in\mathcal X$ with $x\neq 0$ there is $f\in \mathcal X\dual$ with $\norm f = 1$ and $f(x) = \norm x$. In particular, the functionals in $\mathcal X\dual$ separate the points of $\mathcal X$.

3. The map $\mathcal X \injects \mathcal X^{\vee\vee}$, $x \mapsto \hat x$ with $\hat x(f) \coloneqq f(x)$ for $f\in\mathcal X\dual$, is a linear isometry.

[@Fol13, Theorem 5.8]
:::
