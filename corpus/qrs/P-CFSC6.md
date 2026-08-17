---
schema: qual/card@1
id: P-CFSC6
kind: problem
title: "Suppose that $f\\in C([0,1])$ and that $\\displaystyle \\int_0^1 f(x)x^n\\,dx=0$ for all $n=99,100,101,\\ldots$. Show that $f\\equiv 0$.\\"
classification:
  areas:
  - real-analysis
  topics:
  - stone-weierstrass
  - density
  - integrals
relations: []
review: draft
---

::: problem
Suppose that $f\in C([0,1])$ and that $\displaystyle \int_0^1 f(x)x^n\,dx=0$ for all $n=99,100,101,\ldots$.
Show that $f\equiv 0$.\

> Note: Many variations on this problem exist.
> See June 2012 \#6b and others.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. The hypotheses give $\int_0^1 f(x)\,x^{99}p(x)\,dx = 0$ for every polynomial $p$.
    Proof: $x^{99}p(x) = \sum_j a_j x^{99 + j}$ is a finite linear combination of powers $x^{99}, x^{100}, \ldots$, each of which integrates to $0$ against $f$ by hypothesis.

<1>2. Consequently $\int_0^1 f(x)\,x^{99}h(x)\,dx = 0$ for every $h \in C([0,1])$.
    <2>1. Polynomials are dense in $C([0,1])$: given $h$, there are polynomials $p_k \to h$ uniformly.
        Proof: Weierstrass approximation theorem.
    <2>2. Then $x^{99}p_k(x) \to x^{99}h(x)$ uniformly.
        Proof: $|x^{99}p_k(x) - x^{99}h(x)| \le \|p_k - h\|_\infty \to 0$ since $0 \le x^{99} \le 1$.
    <2>3. Q.E.D.
        Proof: $\int f\,x^{99}h = \lim_k \int f\,x^{99}p_k = 0$ by <1>1, the limit passing under the integral by uniform convergence (or dominated convergence with dominating function $\|f\|_\infty (1 + \|h\|_\infty)$).

<1>3. Take $h = f$: $\int_0^1 x^{99} f(x)^2\,dx = 0$.
    Proof: <1>2 with $h = f \in C([0,1])$.

<1>4. $f \equiv 0$.
    Proof: $x^{99}f(x)^2 \ge 0$ on $[0,1]$ and continuous; a continuous non-negative function with integral $0$ vanishes identically, so $f(x) = 0$ for $x \in (0,1]$; continuity at $0$ gives $f(0) = 0$.

<1>5. Q.E.D.
    Proof: <1>3 and <1>4.
:::
