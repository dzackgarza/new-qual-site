---
schema: qual/card@1
id: P-UCLARA18F-03
kind: problem
title: Portmanteau theorem for continuity sets
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Borel Measures
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 3. Let $(X,\rho)$ be a compact metric space and let $\mathcal P(X)$ be the set of all probability measures on the Borel sigma-algebra of $X$. Assume $\{\mu_n\}$ is a sequence in $\mathcal P(X)$ and $\mu\in\mathcal P(X)$ such that, for every continuous $f:X\to\RR$,
$$
\int_X f(x)\,d\mu_n\longrightarrow\int_X f(x)\,d\mu
\qquad(n\to\infty).
$$
Prove that
$$
\mu_n(E)\to\mu(E)
\qquad(n\to\infty)
$$
whenever $E$ is a Borel subset of $X$ such that
$$
\mu(\overline E)=\mu(E^\circ),
$$
where $\overline E$ is the closure of $E$ and $E^\circ$ is the interior of $E$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every closed set $F\subseteq X$,
$$
\limsup_{n\to\infty}\mu_n(F)\le\mu(F).
$$


::: pf-proof

The assertion is immediate for $F=\varnothing$, so suppose $F\ne\varnothing$. For $k\ge1$, define
$$
\phi_k(x)=\max\{0,1-k\rho(x,F)\},
\qquad
\rho(x,F)=\inf_{y\in F}\rho(x,y).
$$
The distance function $x\mapsto\rho(x,F)$ is continuous, so $\phi_k\in C(X)$. Moreover
$$
0\le\phi_k\le1,
\qquad
\mathbf 1_F\le\phi_k,
\qquad
\phi_k(x)\longrightarrow\mathbf 1_F(x)
$$
for every $x\in X$. Thus the assumed convergence of integrals gives, for every fixed $k$,
$$
\limsup_{n\to\infty}\mu_n(F)
\le\lim_{n\to\infty}\int_X\phi_k\,d\mu_n
=\int_X\phi_k\,d\mu.
$$
By dominated convergence, $\int_X\phi_k\,d\mu\to\mu(F)$ as $k\to\infty$. Letting $k\to\infty$ proves the inequality.

:::

:::

::: {.pf-step #s1-2}

For every open set $G\subseteq X$,
$$
\liminf_{n\to\infty}\mu_n(G)\ge\mu(G).
$$


::: pf-proof

The complement $X\setminus G$ is closed. Since every $\mu_n$ and $\mu$ is a probability measure, step [](#s1-1){.pf-ref} gives
$$
\begin{aligned}
\liminf_{n\to\infty}\mu_n(G)
&=1-\limsup_{n\to\infty}\mu_n(X\setminus G)\\
&\ge1-\mu(X\setminus G)
=\mu(G).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

For the Borel set $E$ in the problem,
$$
\mu(E^\circ)
\le\liminf_{n\to\infty}\mu_n(E)
\le\limsup_{n\to\infty}\mu_n(E)
\le\mu(\overline E).
$$


::: pf-proof

Since $E^\circ\subseteq E\subseteq\overline E$, monotonicity and steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} give
$$
\begin{aligned}
\mu(E^\circ)
&\le\liminf_n\mu_n(E^\circ)
\le\liminf_n\mu_n(E)\\
&\le\limsup_n\mu_n(E)
\le\limsup_n\mu_n(\overline E)
\le\mu(\overline E).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{\mu_n(E)\longrightarrow\mu(E)}.
$$


::: pf-proof

By hypothesis, $\mu(E^\circ)=\mu(\overline E)$. Since
$$
E^\circ\subseteq E\subseteq\overline E,
$$
monotonicity also gives
$$
\mu(E^\circ)\le\mu(E)\le\mu(\overline E),
$$
so all three quantities are equal. Step [](#s1-3){.pf-ref} then forces
$$
\liminf_n\mu_n(E)=\limsup_n\mu_n(E)=\mu(E),
$$
which is exactly the asserted convergence.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the required convergence for every Borel continuity set $E$.

:::

:::

:::
