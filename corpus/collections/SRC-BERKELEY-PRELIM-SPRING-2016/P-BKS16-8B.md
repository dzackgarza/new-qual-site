---
schema: qual/card@1
id: P-BKS16-8B
kind: problem
title: Factorization of $6x^5+3x^4-9x^3+15x^2-13x-2$ over $\QQ$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Checked the statement against Problem 8B in the vendored Berkeley Spring 2016 exam and independently reviewed the supplied reciprocal-polynomial/Eisenstein solution.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the division by $x-1$, Eisenstein's criterion for the reciprocal quartic, and preservation of nontrivial factorizations under reversal.
---

::: {.problem}
Factor the polynomial
$$
f(x)=6x^5+3x^4-9x^3+15x^2-13x-2
$$
into a product of irreducible polynomials in the ring $\QQ[x]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The polynomial factors as
$$
f(x)=(x-1)g(x),
\qquad
g(x)=6x^4+9x^3+15x+2.
$$


::: pf-proof

Since
$$
f(1)=6+3-9+15-13-2=0,
$$
the factor theorem gives a factor $x-1$. Synthetic division by $x-1$ gives the quotient
$$
6x^4+9x^3+0x^2+15x+2.
$$

:::

:::

::: {.pf-step #s1-2}

The reciprocal polynomial
$$
h(x)\coloneqq x^4g(x^{-1})=2x^4+15x^3+9x+6
$$
is irreducible in $\QQ[x]$.


::: pf-proof

Eisenstein's criterion applies to $h$ with the prime $3$: the leading coefficient $2$ is not divisible by $3$, every other coefficient is divisible by $3$, and the constant coefficient $6$ is not divisible by $9$. Hence $h$ is irreducible over $\QQ$.

:::

:::

::: {.pf-step #s1-3}

The quartic $g$ is irreducible in $\QQ[x]$.


::: pf-proof

Suppose instead that
$$
g(x)=u(x)v(x)
$$
with $u,v\in\QQ[x]$ of positive degree. Since $g(0)=2\neq0$, both $u(0)$ and $v(0)$ are nonzero. Put
$$
\widetilde u(x)\coloneqq x^{\deg u}u(x^{-1}),
\qquad
\widetilde v(x)\coloneqq x^{\deg v}v(x^{-1}).
$$
The nonzero constant terms of $u$ and $v$ imply that $\deg\widetilde u=\deg u>0$ and $\deg\widetilde v=\deg v>0$. Since $\deg u+\deg v=4$,
$$
h(x)
=x^4g(x^{-1})
=\widetilde u(x)\widetilde v(x),
$$
contradicting step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The factorization into irreducibles is
$$
\boxed{f(x)=(x-1)(6x^4+9x^3+15x+2)}.
$$


::: pf-proof

The factor $x-1$ is irreducible because it has degree $1$, and step [](#s1-3){.pf-ref} proves that the quartic factor is irreducible.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the requested irreducible factorization.

:::

:::

:::
