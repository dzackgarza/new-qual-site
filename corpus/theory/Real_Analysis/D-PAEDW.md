---
schema: qual/card@1
id: D-PAEDW
kind: definition
title: Limit superior and limit inferior of a sequence of sets
slogan: '$\liminf$ means eventually always; $\limsup$ means infinitely often.'
prompts:
- What are $\limsup_n A_n$ and $\liminf_n A_n$ for a sequence of sets?
- Define $\limsup, \liminf$ for sequences of sets. What are their containments?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Borel-Cantelli
relations: []
review: draft
---

::: {.definition}
Let $(E_n)_{n\geq 1}$ be a sequence of subsets of a set $X$.
Its \dfn{limit inferior} and \dfn{limit superior} are
$$
\begin{aligned}
\liminf_{n\to\infty} E_{n} &\coloneqq \bigcup_{N=1}^\infty \bigcap_{n=N}^\infty E_{n} = \theset{x\in X \suchthat x\in E_{n} \text{ for all but finitely many } n}, \\
\limsup_{n\to\infty} E_{n} &\coloneqq \bigcap_{N=1}^\infty \bigcup_{n=N}^{\infty} E_{n} = \theset{x\in X \suchthat x\in E_{n} \text{ for infinitely many } n}.
\end{aligned}
$$
:::

::: {.remark}
The descriptions by membership follow from the formulas.
A point lies in $\bigcap_{n\geq N}E_n$ for some $N$ exactly when it lies in every $E_n$ with $n\geq N$ for some $N$, that is, in all but finitely many $E_n$.
A point lies in $\bigcup_{n\geq N}E_n$ for every $N$ exactly when for every $N$ it lies in some $E_n$ with $n\geq N$, that is, in infinitely many $E_n$.
A point in all but finitely many $E_n$ lies in infinitely many of them, so $\liminf_n E_n\subseteq\limsup_n E_n$.
:::
