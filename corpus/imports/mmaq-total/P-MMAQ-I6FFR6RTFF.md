---
schema: qual/card@1
id: P-MMAQ-I6FFR6RTFF
kind: problem
title: "Let $f\\in L^1(\\RR)$. Show that $\\lim _{x \\rightarrow 0} \\int_{\\mathbb{R}}|f(y-x)-f(y)| d y=0$"
classification:
  areas:
  - real-analysis
  topics:
  - l1
  - norms
  - convergence-of-integrals
relations: []
review: draft
---

::: problem
Let $f\in L^1(\RR)$.
Show that
$$
\lim _{x \rightarrow 0} \int_{\mathbb{R}}|f(y-x)-f(y)| d y=0
$$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that translation is continuous in $L^1$: for $f \in L^1(\RR)$, $\norm{f(\cdot - x) - f}_1 \to 0$ as $x \to 0$.

<1>1. The claim holds for continuous functions with compact support.
    Proof: This is precisely part (a) of the companion problem: a continuous compactly supported function is uniformly continuous, and its translates share a common compact support, so the $L^1$ norm of the difference is bounded by support measure times the uniform modulus (the $2$-line argument).

<1>2. Continuous compactly supported functions are dense in $L^1(\RR)$.
    Proof: Standard result: truncate $f$ to a bounded interval and convolve with a mollifier (or approximate by step functions then by smooth compactly supported functions in $L^1$).

<1>3. The claim extends from <1>1 to all of $L^1$ by a $3\eps$ argument.
    <2>1. Fix $\eps > 0$ and choose $g \in C_c(\RR)$ with $\norm{f - g}_1 < \eps/3$.
        Proof: By <1>2.
    <2>2. For $\abs{x}$ small, $\norm{g(\cdot - x) - g}_1 < \eps/3$.
        Proof: By <1>1 applied to $g$.
    <2>3. $\norm{f(\cdot - x) - f}_1 \leq \norm{f(\cdot-x) - g(\cdot-x)}_1 + \norm{g(\cdot-x) - g}_1 + \norm{g - f}_1$.
        Proof: Triangle inequality, inserting $\pm g(\cdot - x)$.
    <2>4. The first and last terms equal $\norm{f - g}_1 < \eps/3$ (translation invariance of the norm), so the whole is $< \eps$ for $\abs{x}$ small.
        Proof: $\norm{f(\cdot-x) - g(\cdot-x)}_1 = \norm{(f - g)(\cdot - x)}_1 = \norm{f - g}_1$; combine with <2>2 and <2>3.
    <2>5. Q.E.D.
        Proof: $\eps > 0$ was arbitrary.

<1>4. Conclusion: $\lim_{x\to 0} \int_\RR \abs{f(y-x) - f(y)} ~dy = 0$.
    Proof: The integral is $\norm{f(\cdot - x) - f}_1$, which goes to $0$ by <1>3.
:::
