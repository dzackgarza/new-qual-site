---
schema: qual/card@1
id: P-BKS08-1A
kind: problem
title: Finite-dimensional commutators cannot equal the identity
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the finite-dimensional trace obstruction and the
    polynomial differentiation/multiplication example against the vendored
    solution.
---

::: {.problem}
Prove that there do not exist linear operators $A,B$ on a nonzero finite-dimensional complex vector space such that
$$
AB-BA=I.
$$
Give an example of two operators on an infinite-dimensional complex vector space for which $AB-BA=I$.
:::

::: {.solution}
<1>1. On a nonzero finite-dimensional complex vector space, no
operators $A,B$ can satisfy
$$
AB-BA=I.
$$

::: {.proof}
Suppose the vector space has dimension $n>0$. Taking traces and using
cyclicity of trace gives
$$
\operatorname{tr}(AB-BA)
=\operatorname{tr}(AB)-\operatorname{tr}(BA)
=0.
$$
If $AB-BA=I$, however, then
$$
\operatorname{tr}(AB-BA)=\operatorname{tr}(I)=n\ne0,
$$
a contradiction.
:::

<1>2. On the infinite-dimensional complex vector space $\CC[x]$, let
$$
A(p)\coloneqq p',
\qquad
B(p)\coloneqq xp.
$$
Then
$$
\boxed{AB-BA=I}.
$$

::: {.proof}
For every polynomial $p$,
$$
\begin{aligned}
(AB-BA)(p)
&=\frac{d}{dx}(xp)-x\frac{dp}{dx}\\
&=p+xp'-xp'\\
&=p.
\end{aligned}
$$
Thus the commutator acts as the identity on every element of
$\CC[x]$.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>1 proves the finite-dimensional impossibility, and step <1>2
provides the required infinite-dimensional example.
:::
:::
