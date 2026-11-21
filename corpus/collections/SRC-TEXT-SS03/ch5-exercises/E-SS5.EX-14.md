---
schema: qual/card@1
id: E-SS5.EX-14
kind: problem
title: An entire function of non-integral order has infinitely many zeros
classification:
  areas:
  - complex-analysis
  topics:
  - Hadamard Factorization
  - Zeros
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 5 growth-order convention.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so. Each step re-read: Hadamard factors an entire function with
    finitely many zeros as e^P times a polynomial; a constant P gives a polynomial, of order 0; and
    for deg P = d >= 1 the upper bound gives order at most d while the lower bound along the ray
    where c e^{id theta} = |c| gives order at least d, so the order is exactly d. The conclusion
    excludes non-integral orders. Not claimed: the converse, or the identity theorem step for
    functions of infinite order, where Hadamard's theorem does not apply in this form.
---

::: {.exercise}
Deduce from Hadamard’s theorem that if $F$ is entire and of growth order $\rho$ that is non-integral, then F has infinitely many zeros.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none was located for this exercise among the retained sets. It is checked against Stein and Shakarchi, Complex Analysis (2003), Chapter 5 Exercise 14, and uses Hadamard's factorization theorem as the exercise directs.

::: pf

::: {.pf-step #factorisation}
If $F$ is entire with finitely many zeros then $F=e^{P}Q$ with $P$ and $Q$ polynomials.

::: pf-proof
Hadamard's factorization theorem writes an entire function of finite order as $e^{P}$ times a canonical product over its zeros; with finitely many zeros the product is a polynomial, and $P$ is a polynomial because the order is finite.
:::

:::

::: {.pf-step #constant}
If $P$ is constant then $F$ has growth order $0$.

::: pf-proof
Then $F=e^{c}Q$ is a polynomial, and a polynomial is bounded by $A(1+\abs{z})^{N}$, so $\log\log M(r)=O(\log\log r)$ and the order is $0$.
:::

:::

::: {.pf-step #degree}
If $\deg P=d\ge1$ then $F$ has growth order exactly $d$.

:::: pf-proof

::: {.pf-step #upper}
$\abs{F(z)}\le Ae^{B\abs{z}^{d}}$ for suitable constants.

::: pf-proof
$\abs{P(z)}\le A_{1}\abs{z}^{d}$ for large $\abs{z}$ and hence $\abs{P(z)}\le A_{2}(1+\abs{z})^{d}$ everywhere, giving $\abs{e^{P(z)}}\le e^{A_{2}(1+\abs{z})^{d}}$; and $\abs{Q(z)}\le A_{3}(1+\abs{z})^{N}$. Multiplying gives the claim, so the order is at most $d$.
:::

:::

::: {.pf-step #lower}
$\log\abs{F(re^{i\theta})}=\abs{c}r^{d}+O(r^{d-1})$ along a suitable ray, so the order is at least $d$.

::: pf-proof
Write $P(z)=cz^{d}+\text{(lower terms)}$ with $c\ne0$ and choose $\theta$ with $ce^{id\theta}=\abs{c}$, which is possible since both sides have modulus $\abs{c}$. Then $P(re^{i\theta})=ce^{id\theta}r^{d}+O(r^{d-1})=\abs{c}r^{d}+O(r^{d-1})$, so $\Re P(re^{i\theta})=\abs{c}r^{d}+O(r^{d-1})$; and $\log\abs{Q(re^{i\theta})}=O(\log r)$ for large $r$ away from the finitely many zeros of $Q$. A growth-order bound with exponent $\sigma<d$ would force $\log\abs{F(z)}=O(\abs{z}^{\sigma})$, which this lower bound contradicts.
:::

:::

:::

:::

::: {.pf-step #integral}
An entire function with finitely many zeros has growth order $0$ or a positive integer.

::: pf-proof
By step [](#factorisation){.pf-ref} write $F=e^{P}Q$; if $P$ is constant the order is $0$ by step [](#constant){.pf-ref}, and otherwise it is $\deg P$ by step [](#degree){.pf-ref}.
:::

:::

::: {.pf-step}
If the growth order of $F$ is a non-integral $\rho$ then $F$ has infinitely many zeros.

::: pf-proof
A non-integral $\rho$ is neither $0$ nor a positive integer, so it is excluded by step [](#integral){.pf-ref}; hence $F$ cannot have finitely many zeros:
$$
\boxed{\rho\notin\ZZ_{\ge0}\implies F\text{ has infinitely many zeros}.}
$$
The argument uses Hadamard's theorem and nothing else about $F$.
:::

:::

:::
:::
