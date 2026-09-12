---
schema: qual/card@1
id: P-ALGS12G
kind: problem
title: Irreducible $f$ divides $x^{q^n}-x$ iff $\deg f$ divides $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared against the official UCSD Spring 2012 Algebra qualifying exam; statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Reduced divisibility by x^(q^n)-x to the finite-field subfield criterion F_(q^d) subset F_(q^n) iff d divides n.
---

::: problem
Suppose that $K$ is a finite field with $|K| = q$.
Show that if $f \in K[x]$ is irreducible, then $f$ divides $x^{q^n} - x$ in $K[x]$ if and only if $\deg f$ divides $n$.
:::

::: {.solution}
Let $d=\deg f$ and let $\alpha$ be a root of $f$ in an algebraic closure $\overline K$.

<1>1. The field $K(\alpha)$ has $q^d$ elements.
::: {.proof}
Because $f$ is irreducible of degree $d$, it is the minimal polynomial of $\alpha$ over $K$, so
\[
[K(\alpha):K]=d.
\]
Since $|K|=q$, the finite extension $K(\alpha)$ therefore has $q^d$ elements.
Thus
\[
K(\alpha)\cong \mathbf F_{q^d}.
\]
:::

<1>2. We have
\[
f\mid x^{q^n}-x
\]
if and only if $\alpha\in \mathbf F_{q^n}$.
::: {.proof}
The roots of $x^{q^n}-x$ in $\overline K$ are exactly the elements of the unique field $\mathbf F_{q^n}\subset\overline K$.
The derivative of $x^{q^n}-x$ is $-1$, so all its roots are simple.

If $f$ divides $x^{q^n}-x$, then every root of $f$, in particular $\alpha$, is a root of $x^{q^n}-x$, hence lies in $\mathbf F_{q^n}$.

Conversely, if $\alpha\in\mathbf F_{q^n}$, then $x^{q^n}-x$ vanishes at $\alpha$.
Since $f$ is the minimal polynomial of $\alpha$ over $K$, it divides every polynomial in $K[x]$ vanishing at $\alpha$.
Hence $f\mid x^{q^n}-x$.
:::

<1>3. We have
\[
\mathbf F_{q^d}\subseteq \mathbf F_{q^n}
\quad\Longleftrightarrow\quad
 d\mid n.
\]
::: {.proof}
If $d\mid n$, write $n=dr$.
Every $a\in\mathbf F_{q^d}$ satisfies $a^{q^d}=a$, hence iterating Frobenius gives $a^{q^n}=a$; therefore $a\in\mathbf F_{q^n}$.

Conversely, suppose $\mathbf F_{q^d}\subseteq\mathbf F_{q^n}$.
Then by the tower law,
\[
n=[\mathbf F_{q^n}:\mathbf F_q]
  =[\mathbf F_{q^n}:\mathbf F_{q^d}]\,[\mathbf F_{q^d}:\mathbf F_q],
\]
so $d$ divides $n$.
:::

<1>4. Therefore
\[
f\mid x^{q^n}-x
\quad\Longleftrightarrow\quad
\deg f\mid n.
\]
::: {.proof}
By <1>1 and <1>2, divisibility is equivalent to
\[
K(\alpha)=\mathbf F_{q^d}\subseteq\mathbf F_{q^n}.
\]
Apply <1>3.
:::
:::
