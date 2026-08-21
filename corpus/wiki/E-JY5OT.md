---
schema: qual/card@1
id: E-JY5OT
kind: exercise
title: Reverse triangle inequality, $\sup$ and $\inf$, and the Archimedean property
classification:
  areas:
  - real-analysis
  topics:
  - Norms
  - Sequences of Numbers
relations: []
review: draft
solved: true
---

::: exercise
- Derive the reverse triangle inequality from the triangle inequality.

- Let $E\subseteq \RR$.
  Define $\sup E$ and $\inf E$.

- What is the **Archimedean** property?
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. Reverse triangle inequality: $||x| - |y|| \le |x - y|$ in any normed space.
<2>1. $|x| \le |x - y| + |y|$, so $|x| - |y| \le |x - y|$.
Proof: triangle inequality applied to $x = (x - y) + y$.
<2>2. Symmetrically $|y| - |x| \le |x - y|$.
Proof: triangle inequality applied to $y = (y - x) + x$, using $|y - x| = |x - y|$.
<2>3. Q.E.D. Proof: <2>1 and <2>2 combine to $||x| - |y|| \le |x - y|$.

<1>2. Definitions of $\sup E$ and $\inf E$ for $E \subseteq \RR$.
<2>1. $\sup E$ is the least upper bound: $\sup E = s$ iff (i) $x \le s$ for all $x \in E$ and (ii) for every $\eps > 0$ there is $x \in E$ with $x > s - \eps$ (equivalently, $t \ge x$ for all $x \in E$ forces $t \ge s$). Proof: definition of the supremum; exists (as a real number or $+\infty$) for every nonempty $E$ by completeness of $\RR$.
<2>2. $\inf E$ is the greatest lower bound: $\inf E = i$ iff (i) $x \ge i$ for all $x \in E$ and (ii) for every $\eps > 0$ there is $x \in E$ with $x < i + \eps$.
Proof: definition of the infimum; $\inf E = -\sup(-E)$.

<1>3. Archimedean property: for every real $x$ there is an integer $n$ with $n > x$ (equivalently, for every $\eps > 0$ there is $n \in \NN$ with $1/n < \eps$). Proof: if no integer exceeded $x$, then $\NN$ would be bounded above, so by completeness it would have a least upper bound $s$; but then $s - 1$ is not an upper bound, so some $n > s - 1$, giving $n + 1 > s$, contradicting that $s$ is an upper bound.
:::
