---
schema: qual/card@1
id: P-WESRA09-2
kind: problem
title: 'State four measure/functional-analysis theorems'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
State the following theorems:

1. the uniqueness theorem for premeasures on rings;

2. the Dominated Convergence Theorem;

3. the Hahn–Banach Theorem;

4. the Uniform Boundedness (Banach–Steinhaus) Theorem.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The uniqueness theorem for premeasures on rings is the following: let $\mathcal R$ be a ring of subsets of a set $\Omega$, and let $\mu_0:\mathcal R\to[0,\infty]$ be a premeasure. Suppose $\mu_0$ is $\sigma$-finite on $\mathcal R$, meaning that there are sets $E_n\in\mathcal R$ with
$$
\Omega=\bigcup_{n=1}^\infty E_n,
\qquad
\mu_0(E_n)<\infty.
$$
If $\mu$ and $\nu$ are measures on $\sigma(\mathcal R)$ satisfying
$$
\mu(E)=\nu(E)=\mu_0(E)
\qquad(E\in\mathcal R),
$$
then $\boxed{\mu=\nu\text{ on }\sigma(\mathcal R)}$.

:::

::: pf-step

The Dominated Convergence Theorem is the following: let $(\Omega,\mathcal A,\mu)$ be a measure space, let $f_n:\Omega\to\RR$ or $\CC$ be measurable, and suppose $f_n\to f$ almost everywhere. If there is $g\in L^1(\mu)$ such that $|f_n|\le g$ almost everywhere for every $n$, then $f\in L^1(\mu)$,
$$
\boxed{\int_\Omega |f_n-f|\,d\mu\longrightarrow0},
$$
and in particular
$$
\boxed{\int_\Omega f_n\,d\mu\longrightarrow\int_\Omega f\,d\mu}.
$$

:::

::: pf-step

The Hahn--Banach Theorem in normed-space form is the following: let $X$ be a normed vector space over $\RR$ or $\CC$, let $M\subseteq X$ be a linear subspace, and let $f:M\to\RR$ or $\CC$ be a bounded linear functional. Then there is a bounded linear functional $F:X\to\RR$ or $\CC$ such that
$$
\boxed{F|_M=f,
\qquad
\|F\|=\|f\|}.
$$

:::

::: {.pf-step #s1-4}

The Uniform Boundedness Theorem is the following: let $X$ be a Banach space, let $Y$ be a normed vector space, and let $\mathcal F$ be a family of bounded linear maps $T:X\to Y$. If
$$
\sup_{T\in\mathcal F}\|Tx\|_Y<\infty
\qquad\text{for every }x\in X,
$$
then
$$
\boxed{\sup_{T\in\mathcal F}\|T\|<\infty}.
$$

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} state the four requested theorems, including the hypotheses needed for each conclusion.

:::

:::

:::
