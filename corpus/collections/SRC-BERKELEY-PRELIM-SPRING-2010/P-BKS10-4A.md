---
schema: qual/card@1
id: P-BKS10-4A
kind: problem
title: Invertibility of a sum of commuting finite-order matrices
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
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked a direct kernel argument using commutativity and the relations A^3=I and B^5=I.
---

::: {.problem}
Let \(A,B\) be real \(n\times n\) matrices such that
\[
A^3=B^5=I_n,\qquad AB=BA.
\]
Show that \(A+B\) is invertible.
:::

::: {.solution}
<1>1. Let $v\in\RR^n$ satisfy
$$
(A+B)v=0.
$$
Then
$$
A^2v=B^2v
$$
and
$$
A^3v=-B^3v.
$$

::: {.proof}
The kernel assumption gives
$$
Av=-Bv.
$$
Using $AB=BA$,
$$
A^2v
=
A(-Bv)
=
-ABv
=
-BAv
=
B^2v.
$$
Applying $A$ once more and commuting it past $B^2$ gives
$$
A^3v
=
A(B^2v)
=
B^2Av
=
-B^3v.
$$
:::

<1>2. The vector $v$ satisfies
$$
B^3v=-v
$$
and
$$
B^2v=-v.
$$

::: {.proof}
Since $A^3=I_n$, step <1>1 gives
$$
v=A^3v=-B^3v,
$$
so $B^3v=-v$. Applying $B^2$ to this equality and using $B^5=I_n$ gives
$$
v
=
B^5v
=
-B^2v,
$$
hence $B^2v=-v$.
:::

<1>3. One has $v=0$.

::: {.proof}
Apply $B$ to the equality $B^2v=-v$ from step <1>2:
$$
B^3v=-Bv.
$$
The other equality in step <1>2 gives $B^3v=-v$, so
$$
Bv=v.
$$
Applying $B$ once more yields
$$
B^2v=v.
$$
But step <1>2 also gives $B^2v=-v$. Therefore
$$
v=-v.
$$
Over $\RR$ this forces $v=0$.
:::

<1>4. The matrix $A+B$ is invertible.

::: {.proof}
Step <1>3 shows
$$
\ker(A+B)=\{0\}.
$$
Thus the linear endomorphism of the finite-dimensional space $\RR^n$
defined by $A+B$ is injective, hence bijective. Therefore $A+B$ is
invertible.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
