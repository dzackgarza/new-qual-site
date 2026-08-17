---
schema: qual/card@1
id: P-AIDWR
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
solved: true
---

::: problem
Suppose that $f\in C([0,1])$ and that $\displaystyle \int_0^1 f(x)x^n\,dx=0$ for all $n=99,100,101,\ldots$.
Show that $f\equiv 0$.\

> Note: Many variations on this problem exist.
> See June 2012 6b and others.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. The hypotheses give $\int_0^1 f(x)\,x^{99}p(x)\,dx = 0$ for every polynomial $p$.
Proof: $x^{99}p(x)$ is a finite linear combination of powers $x^{99}, x^{100}, \ldots$, each of which integrates to $0$ against $f$.

<1>2. Consequently $\int_0^1 f(x)\,x^{99}h(x)\,dx = 0$ for every $h \in C([0,1])$.
<2>1. Polynomials are dense in $C([0,1])$ (Weierstrass), so $p_k \to h$ uniformly.
Proof: Weierstrass approximation theorem.
<2>2. $x^{99}p_k \to x^{99}h$ uniformly.
Proof: $|x^{99}p_k - x^{99}h| \le \|p_k - h\|_\infty \to 0$.
<2>3. Q.E.D. Proof: $\int f\,x^{99}h = \lim_k \int f\,x^{99}p_k = 0$ by uniform convergence under the integral.

<1>3. Take $h = f$: $\int_0^1 x^{99}f(x)^2\,dx = 0$.
Proof: <1>2 with $h = f \in C([0,1])$.

<1>4. $f \equiv 0$.
Proof: $x^{99}f(x)^2 \ge 0$ is continuous with integral $0$, hence identically $0$; so $f = 0$ on $(0,1]$, and continuity at $0$ gives $f(0) = 0$.
:::
