---
schema: qual/card@1
id: P-ALGS18F
kind: problem
title: "Degree of irreducible factors of x^{p^n} - x over F_p divides n"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Suppose $f(x) \in \mathbb{F}_p[x]$ is an irreducible factor of $x^{p^n} - x$ where $p$ is a prime number.
Prove that $\deg f$ divides $n$.
:::

::: {.solution}

::: pf

::: pf-step

Let $d=\deg f$, and let $\alpha$ be a root of $f$ in an algebraic closure $\overline{\mathbb F}_p$.

::: pf-proof

Since $f$ is irreducible over $\mathbb F_p$, it is the minimal polynomial of $\alpha$ over $\mathbb F_p$, so $[\mathbb F_p(\alpha):\mathbb F_p]=d$.

:::

:::

::: {.pf-step #s2}

Because $f$ divides $x^{p^n}-x$, one has
\[
\alpha^{p^n}=\alpha.
\]

::: pf-proof

Every root of $f$ is a root of the polynomial $x^{p^n}-x$.

:::

:::

::: {.pf-step #s3}

Let $\varphi:\overline{\mathbb F}_p\to\overline{\mathbb F}_p$ be Frobenius, $\varphi(x)=x^p$.
The least positive integer $r$ such that $\varphi^r(\alpha)=\alpha$ is $d$.

::: pf-proof

The distinct conjugates of $\alpha$ over $\mathbb F_p$ are
\[
\alpha,\alpha^p,\alpha^{p^2},\ldots,\alpha^{p^{d-1}}.
\]
Indeed, Frobenius fixes $\mathbb F_p$, so these are roots of the minimal polynomial; conversely the finite extension $\mathbb F_p(\alpha)$ has $p^d$ elements, hence Frobenius has order $d$ on the orbit of a generator of this degree-$d$ extension.
Thus the orbit length is exactly $d$.

:::

:::

::: {.pf-step #s4}

By step [](#s2){.pf-ref}, $\varphi^n(\alpha)=\alpha$, so $d$ divides $n$.

::: pf-proof

For any permutation orbit of length $d$, the powers fixing a point are precisely the multiples of $d$.
By step [](#s3){.pf-ref}, the Frobenius orbit of $\alpha$ has length $d$, while step [](#s2){.pf-ref} says the $n$-th power of Frobenius fixes $\alpha$.

:::

:::

::: pf-step

Therefore $\deg f\mid n$.

::: pf-proof

By definition $d=\deg f$, and step [](#s4){.pf-ref} gives $d\mid n$.

:::

:::

:::

:::
