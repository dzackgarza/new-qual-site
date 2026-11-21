---
schema: qual/card@1
id: E-SS2.EX-8
kind: problem
title: Derivatives inherit polynomial growth on a strip
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so; the printed hint to use the Cauchy inequalities is what the
    proof does. Each step re-read: the circle of radius 1/2 about a real point stays in the strip
    because its imaginary part is at most 1/2 in modulus; Cauchy's inequality on that disc gives
    the factorial and the power 2^n; the two triangle-inequality bounds give the two-sided
    comparison of 1+|z| with 1+|x|; and the constant is the maximum of the two powers, which
    handles both signs of eta. The card states A_n explicitly. Not claimed: any bound on the
    growth of A_n in n, or any statement for a strip of a different width.
---

::: {.exercise}
If $f$ is a holomorphic function on the strip $-1 < y < 1$, $x \in \RR$ with
$$
\abs{f(z)} \leq A(1 + \abs{z})^{\eta}, \quad \eta \text{ a fixed real number}
$$
for all $z$ in that strip, show that for each integer $n \geq 0$ there exists $A_n \geq 0$ so that
$$
\abs{f^{(n)}(x)} \leq A_n (1 + \abs{x})^{\eta}, \quad \text{for all } x \in \RR.
$$
[Hint: Use the Cauchy inequalities.]
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none was located for this exercise among the retained sets. It is checked against Stein and Shakarchi, Complex Analysis (2003), Chapter 2 Exercise 8, which prints the hint to use the Cauchy inequalities.

::: pf

::: {.pf-step #circle}
For fixed $x\in\RR$ the circle $\abs{z-x}=\tfrac12$ lies in the strip $-1<\operatorname{Im}z<1$.

::: pf-proof
Points of the circle satisfy $\abs{z-x}=\tfrac12$, so $\abs{\operatorname{Im}z}=\abs{\operatorname{Im}(z-x)}\le\abs{z-x}=\tfrac12<1$.
:::

:::

::: {.pf-step #cauchy}
$\abs{f^{(n)}(x)}\le n!\,2^{n}\sup_{\abs{z-x}=1/2}\abs{f(z)}$.

::: pf-proof
$f$ is holomorphic on a neighbourhood of the closed disc bounded by the circle, since the circle and its interior lie in the strip; Cauchy's inequalities for the disc of radius $1/2$ give $\abs{f^{(n)}(x)}\le n!\,\rho^{-n}\sup_{\abs{z-x}=\rho}\abs{f(z)}$ with $\rho=\tfrac12$.
:::

:::

::: {.pf-step #comparison}
$\tfrac12(1+\abs{x})\le1+\abs{z}\le\tfrac32(1+\abs{x})$ on the circle.

::: pf-proof
The triangle inequality gives $\abs{z}\le\abs{x}+\tfrac12$ and $\abs{z}\ge\abs{x}-\tfrac12$. Hence $1+\abs{z}\le1+\abs{x}+\tfrac12\le\tfrac32(1+\abs{x})$, since $\tfrac12\le\tfrac12\abs{x}+\tfrac12$; and $1+\abs{z}\ge1+\abs{x}-\tfrac12=\abs{x}+\tfrac12\ge\tfrac12(1+\abs{x})$.
:::

:::

::: {.pf-step #constant}
There is $C_{\eta}\ge0$ with $(1+\abs{z})^{\eta}\le C_{\eta}(1+\abs{x})^{\eta}$ on the circle, for either sign of $\eta$.

::: pf-proof
If $\eta\ge0$, monotonicity of $t\mapsto t^{\eta}$ on $[0,\infty)$ and the upper bound give $(1+\abs{z})^{\eta}\le\bigl(\tfrac32\bigr)^{\eta}(1+\abs{x})^{\eta}$. If $\eta<0$, the same monotonicity applied to the lower bound gives $(1+\abs{z})^{\eta}\le\bigl(\tfrac12\bigr)^{\eta}(1+\abs{x})^{\eta}=2^{-\eta}(1+\abs{x})^{\eta}$. So $C_{\eta}=\max\{(\tfrac32)^{\eta},2^{-\eta}\}$ works in both cases, and it is nonnegative.
:::

:::

::: {.pf-step #estimate}
$\abs{f^{(n)}(x)}\le A_{n}(1+\abs{x})^{\eta}$ with $A_{n}=n!\,2^{n}A\,C_{\eta}$.

::: pf-proof
On the circle, $\abs{f(z)}\le A(1+\abs{z})^{\eta}\le A\,C_{\eta}(1+\abs{x})^{\eta}$ by the hypothesis and step [](#constant){.pf-ref}. Substituting into step [](#cauchy){.pf-ref} gives $\abs{f^{(n)}(x)}\le n!\,2^{n}A\,C_{\eta}(1+\abs{x})^{\eta}$.
:::

:::

::: {.pf-step}
For each $n\ge0$ there is $A_{n}\ge0$ with $\abs{f^{(n)}(x)}\le A_{n}(1+\abs{x})^{\eta}$ for all real $x$.

::: pf-proof
Step [](#estimate){.pf-ref} establishes it with $A_{n}=n!\,2^{n}A\,C_{\eta}$, which does not depend on $x$:
$$
\boxed{A_{n}=n!\,2^{n}A\max\bigl\{(\tfrac32)^{\eta},2^{-\eta}\bigr\}.}
$$
The power of $2$ in the constant grows with $n$, which is why the conclusion bounds the derivatives by the same growth rate $\eta$ but with constants growing factorially.
:::

:::

:::
:::
