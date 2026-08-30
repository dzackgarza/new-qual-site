---
schema: qual/card@1
id: P-2UVDX
kind: problem
title: $e^{-\pi\xi^2}=\int_{-\infty}^\infty e^{-\pi x^2}e^{2\pi i x\xi}\,dx$ for all
  $\xi\in\CC$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Entire Functions
  - Integrals
  - Identity Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Prove by *justifying all steps* that for all $\xi \in {\mathbb C}$ we have $\displaystyle e^{- \pi \xi^2} = \int_{- \infty}^\infty e^{- \pi x^2} e^{2 \pi i x \xi} dx \; .$

> Hint: You may use that fact in Example 1 on p. 42 of the textbook without proof, i.e., you may assume the above is true for real values of $\xi$.
:::

::: solution
**Goal:** Prove that for all $\xi\in\mathbb C$,
$$
e^{-\pi\xi^2}=\int_{-\infty}^{\infty}e^{-\pi x^2}e^{2\pi i x\xi}\,dx.
$$

<1>1. Define the transform:
    *Proof:*
    <2>1. For $\xi=u+iv$, the integrand satisfies
        $$|e^{-\pi x^2}e^{2\pi i x\xi}|=e^{-\pi x^2-2\pi vx}=e^{-\pi(x+v)^2+\pi v^2}.$$
    <2>2. Hence
        $$F(\xi):=\int_{-\infty}^{\infty}e^{-\pi x^2}e^{2\pi i x\xi}\,dx$$
        is well-defined for all $\xi\in\mathbb C$ and is entire by dominated convergence on compact sets.

<1>2. Derive a differential equation:
    *Proof:*
    <2>1. Differentiate under the integral to get
        $$F'(\xi)=\int_{-\infty}^{\infty}(2\pi i x)e^{-\pi x^2}e^{2\pi i x\xi}\,dx.$$
    <2>2. Integrate by parts:
        $$
        \begin{aligned}
        F'(\xi)
        &= -i\int_{-\infty}^{\infty}\frac{d}{dx}\left(e^{-\pi x^2}\right)e^{2\pi i x\xi}\,dx\\
        &= -i\Big[e^{-\pi x^2}e^{2\pi i x\xi}\Big]_{-\infty}^{\infty}
        +\,2\pi i\xi\int_{-\infty}^{\infty}e^{-\pi x^2}e^{2\pi i x\xi}\,dx \\
        &= -2\pi\xi F(\xi).
        \end{aligned}
        $$

<1>3. Solve the ODE:
    *Proof:*
    <2>1. $F'+2\pi\xi F=0$ has general solution $F(\xi)=Ce^{-\pi\xi^2}$.
    <2>2. Evaluate at $\xi=0$:
        $$F(0)=\int_{-\infty}^{\infty}e^{-\pi x^2}\,dx=1,$$
        so $C=1$.

<1>4. Conclusion:
    By uniqueness of solutions to this linear ODE on entire functions,
    $$F(\xi)=e^{-\pi\xi^2}$$
    for all $\xi\in\mathbb C$. Q.E.D.
:::
