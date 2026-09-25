---
schema: qual/card@1
id: P-BKF99-4
kind: problem
title: Maximum modulus of a rational function on the closed upper half-plane
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Split according to the behavior at infinity. In the bounded case, used
    the maximum modulus principle on upper half-disks and controlled the
    semicircular boundary by the finite limit at infinity.
---

::: {.problem}
Let $f$ be a rational function with no poles in the closed upper half-plane. Prove that
\[
\sup\{|f(z)|:\operatorname{Im}z\ge0\}
=
\sup\{|f(z)|:\operatorname{Im}z=0\}.
\]
:::

::: {.solution}
Set
$$
M=\sup\{\abs{f(x)}:x\in\RR\}.
$$

<1>1. If $f$ has a pole at infinity, then both suprema in the statement are
$+\infty$.

::: {.proof}
Write $f=p/q$ with relatively prime polynomials. A pole at infinity means
$\deg p>\deg q$, so $\abs{f(x)}\to\infty$ as $\abs{x}\to\infty$ along
the real axis. Hence $M=+\infty$. Since the real axis is contained in the
closed upper half-plane, the supremum there is also $+\infty$.
:::

<1>2. Suppose $f$ has no pole at infinity. Then the finite limit
$$
L=\lim_{z\to\infty}f(z)
$$
exists and satisfies $\abs{L}\leq M$.

::: {.proof}
For a rational function $p/q$ with $\deg p\leq\deg q$, the limit at
infinity exists and is finite. Taking the limit along the real axis gives
$$
\abs{L}
=
\lim_{\abs{x}\to\infty}\abs{f(x)}
\leq M.
$$
:::

<1>3. Under the hypothesis of step <1>2, for every $z$ with
$\operatorname{Im}z\geq0$,
$$
\abs{f(z)}\leq M.
$$

::: {.proof}
Fix such a $z$ and let $\varepsilon>0$. By step <1>2 and the definition of
the limit at infinity, there is $R_0$ such that
$$
\abs{f(w)-L}<\varepsilon
$$
whenever $\abs{w}\geq R_0$. Choose
$R>\max\{R_0,\abs{z}\}$. On the semicircular part of the boundary of the
upper half-disk
$$
D_R=\{w:\abs{w}<R,\ \operatorname{Im}w>0\},
$$
the triangle inequality and step <1>2 give
$$
\abs{f(w)}
\leq
\abs{L}+\varepsilon
\leq
M+\varepsilon.
$$
On the diameter $[-R,R]$, the definition of $M$ gives
$\abs{f(w)}\leq M$. Since $f$ has no poles in the closed upper half-plane,
it is holomorphic on a neighborhood of the closed upper half-disk. The
maximum modulus principle therefore yields
$$
\abs{f(z)}\leq M+\varepsilon.
$$
As $\varepsilon>0$ is arbitrary, $\abs{f(z)}\leq M$.
:::

<1>4.
$$
\sup\{\abs{f(z)}:\operatorname{Im}z\geq0\}
=
\sup\{\abs{f(z)}:\operatorname{Im}z=0\}.
$$

::: {.proof}
If $f$ has a pole at infinity, step <1>1 proves the equality. Otherwise,
step <1>3 shows that the left-hand supremum is at most $M$, while inclusion
of the real axis in the closed upper half-plane shows that it is at least
$M$. The right-hand supremum is $M$ by definition.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required equality.
:::
:::
