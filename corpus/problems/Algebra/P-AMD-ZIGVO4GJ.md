---
schema: qual/card@1
id: P-AMD-ZIGVO4GJ
kind: problem
title: $R/\nilrad{R}$ is reduced
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Ideals
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
Let $R$ be a commutative ring and let $\operatorname{nil}(R) = \sqrt{(0)}$ be its nilradical (the ideal of all nilpotent elements in $R$).
Prove that the quotient ring $R / \operatorname{nil}(R)$ is reduced (i.e. has no non-zero nilpotent elements).
:::

::: solution
**Goal:** Prove that $\operatorname{nil}(R / \operatorname{nil}(R)) = \{0\}$ for any commutative ring $R$.

<1>1. Setting and Quotient Element:
    *Proof:*
    <2>1. Let $R$ be a commutative ring with 1.
    <2>2. The **nilradical** $\mathfrak{N} = \operatorname{nil}(R)$ is defined as:
        $$\mathfrak{N} = \{x \in R \mid x^k = 0 \text{ for some } k \in \mathbb{N}\}.$$
    <2>3. Because $R$ is commutative, $\mathfrak{N}$ is an ideal of $R$ (if $x^k = 0$ and $y^m = 0$, $(x+y)^{k+m-1} = 0$ by the binomial theorem, and $(rx)^k = r^k x^k = 0$).
    <2>4. Consider the quotient ring $\bar{R} = R / \mathfrak{N}$, and let $\bar{x} = x + \mathfrak{N} \in \bar{R}$ be an arbitrary element.

<1>2. Proof that any nilpotent element in $R/\mathfrak{N}$ is zero:
    *Proof:*
    <2>1. Suppose $\bar{x} \in \bar{R}$ is nilpotent.
    <2>2. By definition of nilpotence in the quotient ring, there exists an integer $n \ge 1$ such that:
        $$\bar{x}^n = \bar{0} \in R / \mathfrak{N}.$$
    <2>3. In terms of cosets, $\bar{x}^n = (x + \mathfrak{N})^n = x^n + \mathfrak{N} = \mathfrak{N}$.
    <2>4. This equality of cosets means:
        $$x^n \in \mathfrak{N} = \operatorname{nil}(R).$$
    <2>5. By definition of the nilradical $\operatorname{nil}(R)$, since $x^n \in \operatorname{nil}(R)$, there exists an integer $m \ge 1$ such that:
        $$(x^n)^m = 0 \in R.$$
    <2>6. By the laws of exponents in $R$:
        $$x^{n m} = 0.$$
    <2>7. Since $n m \ge 1$ is a positive integer, $x$ itself is a nilpotent element of $R$:
        $$x \in \operatorname{nil}(R) = \mathfrak{N}.$$
    <2>8. Therefore, the coset $\bar{x} = x + \mathfrak{N} = \mathfrak{N} = \bar{0}$ is the zero element in $R / \mathfrak{N}$.

<1>3. Geometric / Spec Interpretation:
    *Proof:*
    <2>1. Since $\operatorname{nil}(R) = \bigcap_{\mathfrak{p} \in \operatorname{Spec}(R)} \mathfrak{p}$, the quotient $R / \operatorname{nil}(R)$ has nilradical $\bigcap_{\mathfrak{p} \supseteq \mathfrak{N}} \mathfrak{p}/\mathfrak{N} = (\bigcap \mathfrak{p})/\mathfrak{N} = \mathfrak{N}/\mathfrak{N} = (0)$.

<1>4. Conclusion:
    The only nilpotent element in $R / \operatorname{nil}(R)$ is $\bar{0}$, so $R / \operatorname{nil}(R)$ is reduced. Q.E.D.
:::
