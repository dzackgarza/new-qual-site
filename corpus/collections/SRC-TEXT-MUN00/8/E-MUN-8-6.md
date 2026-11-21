---
schema: qual/card@1
id: E-MUN-8-6
kind: problem
title: A recursion with no solution, and one repaired by a case distinction
classification:
  areas:
  - topology
  topics:
  - Recursive Definition
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §8 Exercise 6, printed p. 56; both parts are
    stored as printed, R_+ being the positive reals.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 8.6,
    printed pp. 96-97 (tmp/sources/munkres-solutions-whitman.pdf). Part (a) is his
    computation h(1) = 3, h(2) = sqrt2, then h(3) = sqrt(sqrt2 - 1) in (0,1) so that
    h(3) - 1 < 0 and [h(4)]^2 < 0; the reason the principle is not violated - rho is not
    defined at every f - is his. Part (b) is his piecewise rho and its verification.
---

::: {.exercise}

(a) Show that there is no function $h: \ZZ_+ \to \RR_+$ satisfying the formula
$$
h(1) = 3,
\qquad
h(i) = [h(i-1) - 1]^{1/2} \quad \text{for } i > 1,
$$
and explain why this example does not violate the principle of recursive definition.

(b) Consider the recursion formula
$$
h(1) = 3,
\qquad
h(i) = \begin{cases}[h(i-1)-1]^{1/2} & \text{if } h(i-1) > 1,\\ 5 & \text{if } h(i-1)\le1,\end{cases} \quad \text{for } i > 1.
$$
Show that there exists a unique function $h:\ZZ_+\to\RR_+$ satisfying this formula.
:::

::: {.solution}

The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.6** (`tmp/sources/munkres-solutions-whitman.pdf`); both parts are his.

::: pf

::: {.pf-step #firstvalues}

Any $h$ satisfying the formula of (a) has $h(2)=\sqrt2$ and $h(3)=\sqrt{\sqrt2-1}\in(0,1)$.

::: pf-proof

$h(2)=[h(1)-1]^{1/2}=(3-1)^{1/2}=\sqrt2$, the positive square root. Since $1<\sqrt2<2$, we have $0<\sqrt2-1<1$ and therefore $0<\sqrt{\sqrt2-1}<1$, so $h(3)=[h(2)-1]^{1/2}=\sqrt{\sqrt2-1}$ lies strictly between $0$ and $1$.

:::

:::

::: {.pf-step #nosolution}

(a) No $h:\ZZ_{+}\to\RR_{+}$ satisfies the formula.

::: pf-proof

Suppose $h$ satisfies it. By step [](#firstvalues){.pf-ref} $h(3)<1$, so $h(3)-1<0$; the formula at $i=4$ says $h(4)=[h(3)-1]^{1/2}$, that is $[h(4)]^{2}=h(3)-1<0$. A square of a real number is nonnegative, so no real $h(4)$ exists, contradicting the existence of $h$ defined on all of $\ZZ_{+}$:
$$
\boxed{\text{no } h:\ZZ_{+}\to\RR_{+}\text{ satisfies the recursion of (a).}}
$$

:::

:::

::: {.pf-step #noprinciple}

This does not violate the principle of recursive definition.

::: pf-proof

The principle (Theorem 8.4) requires a *function* $\rho$ defined on every function from a nonempty section $\{1,\dots,n\}$ of $\ZZ_{+}$ into $A=\RR_{+}$, with $\rho(f)\in A$. The natural candidate here is $\rho(f)=[f(n)-1]^{1/2}$, which is not a real number when $f(n)\le1$, and by step [](#firstvalues){.pf-ref} the attempted values do reach this range. So no such $\rho$ exists, the hypothesis of the theorem fails, and there is no contradiction: the theorem says nothing about a recipe that is undefined on some of the functions it would have to accept.

:::

:::

::: {.pf-step #total}

(b) The modified recipe defines a total $\rho:\{\text{functions from a nonempty section into } \RR_{+}\}\to\RR_{+}$.

::: pf-proof

Set $\rho(f)=[f(n)-1]^{1/2}$ when $f(n)>1$ and $\rho(f)=5$ when $f(n)\le1$, where $n$ is the index determined by the section $\{1,\dots,n-1\}$ on which $f$ is defined. If $f(n)>1$ then $f(n)-1>0$ and the positive square root is a well-defined positive real; if $f(n)\le1$ then $\rho(f)=5\in\RR_{+}$. Every case is covered, so $\rho$ is defined on all of its stated domain and takes values in $\RR_{+}$.

:::

:::

::: {.pf-step #existence}

(b) There is a unique $h:\ZZ_{+}\to\RR_{+}$ with $h(1)=3$ and the displayed case rule for $i>1$.

::: pf-proof

Take $A=\RR_{+}$, $a_{0}=3$ and $\rho$ as in step [](#total){.pf-ref}. The principle of recursive definition then gives exactly one function $h:\ZZ_{+}\to\RR_{+}$ with $h(1)=3$ and $h(n)=\rho\big(\restrictionof{h}{\{1,\dots,n-1\}}\big)$ for $n>1$; for $n=i$ this says $h(i)=[h(i-1)-1]^{1/2}$ if $h(i-1)>1$ and $h(i)=5$ if $h(i-1)\le1$, which is the required formula. Uniqueness is the uniqueness clause of the same principle:
$$
\boxed{\exists!\,h:\ZZ_{+}\to\RR_{+}\ \text{satisfying the recursion of (b)}.}
$$

:::

:::

:::

:::
