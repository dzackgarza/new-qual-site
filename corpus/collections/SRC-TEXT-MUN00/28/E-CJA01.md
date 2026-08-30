---
schema: qual/card@1
id: E-CJA01
kind: exercise
title: The unit interval is not limit point compact in the lower limit topology
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}

Show that $[0, 1]$ is not limit point compact as a subspace of $\mathbb{R}_\ell$.
:::

::: solution
**Goal:** Find an infinite subset of $[0,1]$ with no limit point in $\mathbb{R}_\ell$.

<1> Work in the Sorgenfrey subspace $[0,1]\subseteq\mathbb{R}_\ell$ and let
    $$A=\{1-\tfrac1n\mid n\ge2\}\subseteq[0,1].$$
    The set $A$ is infinite.

<1> Show no point of $[0,1]$ is a limit point of $A$.
    *Proof:*
    <2>1. Points of $A$ are ordered
        $$\frac12<\frac23<\frac34<\cdots<1- \frac1n<\cdots .$$
    <2>2. Let $x_n=1-\frac1n$ with $n\ge2$.
    <2>3. If $x=x_n$, choose
        $$\epsilon=\frac12\!\left(\frac{1}{n}-\frac{1}{n+1}\right)>0.$$
        Then the basic neighborhood $[x_n,x_n+\epsilon)$ contains no point of $A$ except $x_n$.
    <2>4. If $x\in\left[0,\frac12\right)$, choose $\epsilon<\frac12-x$.
        Then $[x,x+\epsilon)\cap A=\varnothing$.
    <2>5. If $x\in(x_n,x_{n+1})$ for some $n\ge2$, choose
        $$\epsilon< x_{n+1}-x .$$
        Then $[x,x+\epsilon)\cap A=\varnothing$.
    <2>6. At $x=1$, the basic neighborhood $[1,1+\epsilon)$ is $\{1\}$ in the subspace $[0,1]$ and has empty intersection with $A$.

<1> Conclusion:
    <2>1. $A$ has no limit point in $[0,1]$.
    <2>2. Therefore $[0,1]$ is not limit point compact in $\mathbb{R}_\ell$.

Authored by **Codex 5.3 Spark Extra High**.
:::
