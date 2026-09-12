---
schema: qual/card@1
id: P-JHUFA02CAF
kind: problem
title: Failure of holomorphic and meromorphic extension from an annulus
classification:
  areas:
  - complex-analysis
  topics:
  - Analytic Continuation
  - Laurent Series
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both extension assertions and the annulus/disk radii with Fall 2002 Complex Analysis problem 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Used 1/z for failure of holomorphic extension and e^(1/z) for failure of meromorphic extension, with identity-theorem arguments ruling out alternative extensions."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified both counterexamples and corrected the title, which asserted meromorphic extendibility despite the second part's counterexample."
---

1. (a) (5 points) Give a counterexample to the assertion: If f is holomorphic on the annulus $\{ z : 1 < | z | < 3 \}$ , then f extends holomorphically to the disc $\{ z : | z | < 3 \}$

(b) (15 points) Determine whether the following is true: If f is holomorphic on the annulus $\{ z : 1 < | z | < 3 \}$ , then f extends meromorphically to the disc $\{ z : | z | < 3 \}$


::: solution
Both assertions are false.

<1>1. Part (a) fails for $f(z)=1/z$.
::: proof
The function
$$
f(z)=\frac1z
$$
is holomorphic on the annulus $1<|z|<3$. Suppose it had a holomorphic extension
$F$ to the disk $|z|<3$. On the annulus one would have $zF(z)=1$. Since both
sides are holomorphic on the whole disk, the identity theorem [@SS03] would imply
$$
zF(z)=1
$$
for every $|z|<3$. Evaluating at $z=0$ gives $0=1$, a contradiction. Thus no
holomorphic extension exists.
:::

<1>2. Part (b) fails for $f(z)=e^{1/z}$.
::: proof
The function
$$
f(z)=e^{1/z}
$$
is holomorphic on $1<|z|<3$. Suppose there were a meromorphic function $F$ on
$|z|<3$ agreeing with $f$ on that annulus. On the punctured disk
$0<|z|<3$, both $F$ and $e^{1/z}$ are meromorphic, and they agree on the
nonempty open subset $1<|z|<3$. The identity theorem for meromorphic functions [@SS03]
therefore gives
$$
F(z)=e^{1/z}\qquad(0<|z|<3).
$$
But
$$
e^{1/z}=\sum_{n=0}^{\infty}\frac{1}{n!}z^{-n}
$$
has infinitely many nonzero negative Laurent coefficients at zero, so zero is
an essential singularity. A meromorphic function at zero can have only a
removable singularity or a pole. This contradiction shows that no such
meromorphic extension exists.
:::
:::
