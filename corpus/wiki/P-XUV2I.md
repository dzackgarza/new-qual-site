---
schema: qual/card@1
id: P-XUV2I
kind: problem
title: $\sum a_nb_n<\infty$ for all $b\in\ell^2$ implies $\sum a_n^2<\infty$
classification:
  areas:
  - real-analysis
  topics:
  - L²
  - Functional Analysis
  - Series of Numbers
relations: []
review: draft
---

Let $\theset{a_n}$ be a sequence of real numbers such that
\[
\theset{b_n} \in \ell^2(\NN) \implies \sum a_n b_n < \infty.
\]
Show that $\sum a_n^2 < \infty$.

> Note: Assume $a_n, b_n$ are all non-negative.

:::{.solution}
\envlist
- Define a sequence of operators 
\[  
T_N: \ell^2 &\to \ell^1\\
\theset{b_n} &\mapsto \sum_{n=1}^N a_n b_n
.\]
- By assumption, these are well defined: the image is $\ell^1$ since $\abs{T_N(\theset{b_n})} < \infty$ for all $N$ and all $\theset{b_n} \in \ell^2$.
- So each $T_N \in \qty{\ell^2}\dual$ is a linear functional on $\ell^2$.
- For each $x\in \ell^2$, we have $\norm{T_N(x)}_{\RR} = \sum_{n=1}^N a_n b_n < \infty$ by assumption, so each $T_N$ is pointwise bounded.
- By the Uniform Boundedness Principle, $\sup_N \norm{T_N}_{\text{op}} < \infty$.
- Define $T = \lim_{N \to\infty } T_N$, then $\norm{T}_{\text{op}} < \infty$.
- By the Riesz Representation theorem,
\[  
\sqrt{\sum a_n^2} \definedas \norm{\theset{a_n}}_{\ell^2} = \norm{T}_{\qty{\ell^2}\dual} = \norm{T}_{\text{op}} < \infty
.\]

- So $\sum a_n^2 < \infty$.
:::
