---
schema: qual/card@1
id: P-ALGF18E
kind: problem
title: Subring of $\mathbb{Z}[T]$ missing degree one; fractions, integrality, UFD, generators
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problems 6 and 7 of the official UCSD Algebra Qualifying Exam, Fall 2018 source; the ring and all four questions agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the fraction-field computation, the integral nonmember T obstruction to UFD, and the degree argument excluding a one-generator Z-algebra presentation.
---

::: problem
Let
\[
A := \{ a_0 + a_2 T^2 + a_3 T^3 + \cdots + a_n T^n \mid n = 0,2,3,\ldots;\; a_0,a_2,\ldots,a_n \in \mathbb{Z} \}
\]
(no degree one term) be a subring of the ring $\mathbb{Z}[T]$ of polynomials.

(a) Find the field of fractions of $A$.

(b) Show that $T$ is integral over $A$; that means it is a zero of a monic polynomial in $A[x]$.

(c) Is $A$ a UFD?

(d) Is there $f(T)$ such that $A = \mathbb{Z}[f(T)]$?
:::

::: {.solution}
<1>1. The field of fractions of $A$ is
\[
\mathbb Q(T).
\]
::: {.proof}
Since
\[
A\subseteq\mathbb Z[T],
\]
we have
\[
\operatorname{Frac}(A)\subseteq\mathbb Q(T).
\]
Conversely, $\mathbb Z\subseteq A$, so
\[
\mathbb Q\subseteq\operatorname{Frac}(A).
\]
Also $T^2,T^3\in A$, and therefore
\[
T=\frac{T^3}{T^2}\in\operatorname{Frac}(A).
\]
Thus $\mathbb Q(T)\subseteq\operatorname{Frac}(A)$, proving
\[
\operatorname{Frac}(A)=\mathbb Q(T).
\]
This answers part (a).
:::

<1>2. The element $T$ is integral over $A$ but does not belong to $A$.
::: {.proof}
The polynomial
\[
x^2-T^2\in A[x]
\]
is monic and has $T$ as a root, because $T^2\in A$.
Hence $T$ is integral over $A$.
By the defining description of $A$, every element of $A$ has zero coefficient of $T$, so
\[
T\notin A.
\]
This proves part (b).
:::

<1>3. Every UFD is integrally closed in its field of fractions.
::: {.proof}
Let $D$ be a UFD and suppose
\[
z=\frac ab\in\operatorname{Frac}(D)
\]
is integral over $D$, where $a,b\in D$ have no common nonunit factor.
Choose a monic equation
\[
z^n+d_{n-1}z^{n-1}+\cdots+d_0=0,
\qquad
d_i\in D.
\]
Multiplying by $b^n$ gives
\[
a^n=-b\left(d_{n-1}a^{n-1}+d_{n-2}a^{n-2}b+\cdots+d_0b^{n-1}\right).
\]
Thus
\[
b\mid a^n.
\]
Unique factorization and the coprimality of $a$ and $b$ force $b$ to be a unit.
Hence $z\in D$.
Therefore $D$ is integrally closed.
:::

<1>4. The ring $A$ is not a UFD.
::: {.proof}
The ring $A$ is a domain because it is a subring of the domain $\mathbb Z[T]$.
By <1>1,
\[
T\in\operatorname{Frac}(A),
\]
and by <1>2, $T$ is integral over $A$ but $T\notin A$.
Thus $A$ is not integrally closed.
By <1>3, a UFD must be integrally closed, so $A$ is not a UFD.
This answers part (c).
:::

<1>5. There is no polynomial $f(T)$ such that
\[
A=\mathbb Z[f(T)].
\]
::: {.proof}
Suppose that such an $f$ exists.
It cannot be constant, because $T^2\in A$.
Set
\[
d:=\deg f\ge1.
\]
For every nonconstant polynomial $h(x)\in\mathbb Z[x]$,
\[
\deg h(f(T))=(\deg h)d.
\]
Since $T^2,T^3\in A=\mathbb Z[f(T)]$, it follows that
\[
d\mid2
\qquad\text{and}\qquad
d\mid3.
\]
Hence
\[
d=1.
\]
But $f(T)\in\mathbb Z[f(T)]=A$, while no element of $A$ has degree $1$.
This contradiction proves that no such $f(T)$ exists, answering part (d).
:::
:::
