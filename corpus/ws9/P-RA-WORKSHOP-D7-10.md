---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-10
kind: problem
title: 'Vanishing high moments force a continuous function to vanish'
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

::: {.problem title="?"}
(June 2005 #5) Suppose that $f\in C([0,1])$ and that $$\int_0^1f(x)x^n\,dx=0$$ for all $n=99,100,101,\ldots$.
Show that $f\equiv0$.

Note: Many variations on this problem exist.
See June 2012 #6b and others.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** Show $f \equiv 0$ given $f \in C([0,1])$ and $\int_0^1 f(x)x^n\,dx = 0$ for all $n = 99, 100, \ldots$.

<1>1. $\int_0^1 f(x) p(x)\,dx = 0$ for every polynomial $p$ with no terms of degree $< 99$.
    Proof: linearity of the integral; each monomial $x^n$ with $n \ge 99$ integrates to $0$ by hypothesis, and the hypothesis extends to all such monomials including $n = 99, 100, \ldots$.

<1>2. $\int_0^1 f(x) x^{99} q(x)\,dx = 0$ for every polynomial $q$.
    Proof: $x^{99}q(x)$ is a polynomial all of whose terms have degree $\ge 99$, so apply <1>1.

<1>3. The set $\{x^{99}q : q \text{ a polynomial}\}$ is dense in $C([0,1])$.
    Proof: $x \mapsto x^{99}$ is a homeomorphism of $[0,1]$ onto $[0,1]$, and $\{q(x^{99}) : q\}$ is the algebra of polynomials in $x^{99}$, which separates points and contains the constants, hence is dense in $C([0,1])$ by the Stone–Weierstrass theorem. But $x^{99}q(x)$ with $q$ ranging over all polynomials is the same set: every polynomial in $x^{99}$ is $x^{99}$ times a polynomial in $x^{99}$, and conversely $x^{99}q(x)$ is a polynomial in $x^{99}$.

<1>4. $f \equiv 0$.
    Proof: take $g_k \to f$ uniformly with $g_k = x^{99}q_k \in \{x^{99}q : q\}$ (possible by <1>3). Then by <1>2, $\int_0^1 f\,g_k = 0$ for all $k$. Since $g_k \to f$ uniformly, $\int_0^1 f\,g_k \to \int_0^1 f^2$, so $\int_0^1 f^2 = 0$. As $f$ is continuous, $f^2 \ge 0$ continuous with zero integral forces $f \equiv 0$.

<1>5. Q.E.D.
    Proof: <1>4 is the claim.

:::
