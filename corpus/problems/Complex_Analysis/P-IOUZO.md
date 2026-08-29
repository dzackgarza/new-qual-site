---
schema: qual/card@1
id: P-IOUZO
kind: problem
title: Polynomial approximation on $\bar\DD$ and entire functions with a vanishing
  Taylor coefficient
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Polynomials
  - Power Series
  - Entire Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Can every continuous function on $\bar \DD$ be uniformly approximated by polynomials in the variable $z$?

> Hint: compare to Weierstrass for the real interval.

- Suppose $f$ is analytic, defined on all of $\CC$, and for each $z_0 \in \CC$ there is at least one coefficient in the expansion $f(z) = \sum_{n=0}^\infty c_n(z-z_0)^n$ is zero.
  Prove that $f$ is a polynomial.

> Hint: use the fact that $c_n n! = f^{(n)}(z_0)$ and use a countability argument.

![[_attachments/Pasted image 20210527172954.png]]

![[_attachments/Pasted image 20210527173005.png]]

![[_attachments/Pasted image 20210527173030.png]]
:::

::: {.solution}
**Part 1.**

<1>1. No, not every continuous function on $\bar\DD$ is uniformly approximable by polynomials in $z$.
<2>1. A uniform limit of holomorphic polynomials on $\bar\DD$ is holomorphic on the interior $\DD$.
Proof: a uniform limit of holomorphic functions is holomorphic (Morera's theorem).
<2>2. But there are continuous functions on $\bar\DD$ that are not holomorphic on $\DD$.
Proof: e.g. $f(z) = \bar z$ is continuous on $\bar\DD$ but not holomorphic.
<2>3. Hence $\bar z$ (or any such function) cannot be uniformly approximated by polynomials in $z$.
Proof: <2>1 and <2>2.

<1>2. Q.E.D. (part 1).
Proof: <1>1.

**Part 2.**

<1>1. For each $n \ge 0$, let $E_n = \{z \in \CC : f^{(n)}(z) = 0\}$.
Proof: define the zero sets of the derivatives.

<1>2. Each $E_n$ is closed, and $\CC = \bigcup_{n=0}^{\infty} E_n$.
Proof: $f^{(n)}$ is continuous so $E_n$ is closed; the hypothesis says that for each $z_0$ some coefficient $c_n = f^{(n)}(z_0)/n!$ is zero, i.e. $f^{(n)}(z_0) = 0$ for some $n$, so $z_0 \in E_n$.

<1>3. By the Baire category theorem, some $E_n$ has nonempty interior.
Proof: $\CC$ is a complete metric space and is the countable union of the closed sets $E_n$, so one of them has nonempty interior.

<1>4. Hence $f^{(n)} \equiv 0$ on $\CC$.
Proof: $f^{(n)}$ is entire and vanishes on a set with nonempty interior (an open disk), so by the identity theorem it vanishes identically.

<1>5. Therefore $f$ is a polynomial of degree at most $n-1$.
Proof: $f^{(n)} \equiv 0$ implies $f$ is a polynomial of degree $< n$.

<1>6. Q.E.D. (part 2).
Proof: <1>5.
:::
