---
schema: qual/card@1
id: P-AGH236FUNCTIONFIELD
kind: problem
title: The local ring at the generic point of an integral scheme is its function field
classification:
  areas:
  - algebraic-geometry
  topics:
  - Integral Schemes
  - Function Fields
  - Generic Points
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.6 statement and the standard generic-point description of the function field.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $X$ be an integral scheme.
Show that the local ring $\OO_{\xi}$ of the generic point $\xi$ of $X$ is a field.
It is called the **function field** of $X$ and is denoted by $K(X)$.

Show also that if $U = \Spec A$ is any open affine subset of $X$, then $K(X)$ is isomorphic to $\Frac(A)$.
:::

::: {.solution}
<1>1. Since $X$ is integral, it is irreducible and has a unique generic point $\xi$.
::: {.proof}
An integral scheme is, by definition, reduced and irreducible.  Every irreducible scheme has a unique generic point.
:::

<1>2. Every nonempty open subset of $X$ contains $\xi$.
::: {.proof}
The closure of $\{\xi\}$ is all of $X$.  If a nonempty open $U$ did not contain $\xi$, then the closed set $X\setminus U$ would contain $\xi$ and hence would contain its closure $X$, contradicting $U\ne\varnothing$.
:::

<1>3. Let
\[
U=\Spec A\subseteq X
\]
be a nonempty affine open.  Then $A$ is a domain and the point $\xi\in U$ corresponds to the prime ideal $(0)\subseteq A$.
::: {.proof}
Because $X$ is reduced and irreducible, every open subscheme is reduced and irreducible.  Thus the affine scheme $U=\Spec A$ is integral, which is equivalent to $A$ being a domain.

The generic point of $\Spec A$ is the zero prime.  By <1>2, the generic point $\xi$ of $X$ lies in $U$; its closure inside $U$ is all of $U$, so it is the generic point of $U$.  Hence it corresponds to $(0)$.
:::

<1>4. The local ring at the generic point is
\[
\boxed{
\mathcal O_{X,\xi}
\cong
A_{(0)}
=
\operatorname{Frac}(A).
}
\]
::: {.proof}
The local ring of the affine scheme $\Spec A$ at the prime $(0)$ is $A_{(0)}$.  Since $A$ is a domain, localizing at the complement of $(0)$ means inverting every nonzero element of $A$, which gives its fraction field.

The stalk of the restricted structure sheaf on the open set $U$ agrees with the stalk of $\mathcal O_X$ at $\xi$, so
\[
\mathcal O_{X,\xi}=\mathcal O_{U,\xi}\cong A_{(0)}.
\]
:::

<1>5. Therefore $\mathcal O_{X,\xi}$ is a field, and for every nonempty affine open $U=\Spec A$ there is a canonical isomorphism
\[
\boxed{K(X)=\mathcal O_{X,\xi}\cong\operatorname{Frac}(A).}
\]
::: {.proof}
Step <1>4 identifies the local ring with a fraction field, hence with a field.  The identification is canonical because both sides are the same stalk computed using the affine neighborhood $U$.
:::

<1>6. Q.E.D.
::: {.proof}
Steps <1>4--<1>5 prove both assertions.
:::
:::
