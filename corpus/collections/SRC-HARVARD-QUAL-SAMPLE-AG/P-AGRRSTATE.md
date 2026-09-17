---
schema: qual/card@1
id: P-AGRRSTATE
kind: problem
title: Riemann--Roch, stated
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Roch
  - Divisors
  - Serre Duality
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Wodzicki's request to state Riemann--Roch.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
State Riemann--Roch.
:::

::: {.solution}
Let $X$ be a smooth projective connected curve of genus $g$ over an algebraically closed field, let $D$ be a divisor on $X$, and let $K$ be a canonical divisor.  Write
\[
\ell(D)=h^0(X,\mathcal O_X(D)).
\]

<1>1. Riemann--Roch states
\[
\boxed{
\ell(D)-\ell(K-D)=\deg D+1-g.
}
\]
::: {.proof}
This is the Riemann--Roch theorem for divisors on a smooth projective curve [@Har10a, Theorem IV.1.3].
:::

<1>2. By Serre duality,
\[
h^1(X,\mathcal O_X(D))
=\ell(K-D).
\]
Hence Riemann--Roch is equivalently
\[
\boxed{
\chi(\mathcal O_X(D))
=\deg D+1-g.
}
\]
::: {.proof}
Serre duality gives
\[
H^1(X,\mathcal O_X(D))
\cong
H^0(X,\mathcal O_X(K-D))^\vee.
\]
Therefore
\[
h^1(X,\mathcal O_X(D))=\ell(K-D).
\]
Subtracting this from
\[
h^0(X,\mathcal O_X(D))=\ell(D)
\]
turns <1>1 into
\[
\chi(\mathcal O_X(D))
=h^0-h^1
=\deg D+1-g.
\]
:::

<1>3. Taking $D=0$ gives
\[
\boxed{\ell(K)=g.}
\]
::: {.proof}
Since $X$ is connected and projective,
\[
\ell(0)=h^0(X,\mathcal O_X)=1.
\]
Putting $D=0$ into <1>1 gives
\[
1-\ell(K)=1-g,
\]
hence $\ell(K)=g$.
:::

<1>4. Taking $D=K$ gives
\[
\boxed{\deg K=2g-2.}
\]
::: {.proof}
With $D=K$, <1>1 gives
\[
\ell(K)-\ell(0)=\deg K+1-g.
\]
Using <1>3 and $\ell(0)=1$,
\[
g-1=\deg K+1-g,
\]
so
\[
\deg K=2g-2.
\]
:::

<1>5. If
\[
\deg D>2g-2,
\]
then
\[
\ell(D)=\deg D+1-g.
\]
::: {.proof}
By <1>4,
\[
\deg(K-D)<0.
\]
A divisor of negative degree has no nonzero global section, so
\[
\ell(K-D)=0.
\]
Apply <1>1.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>1 is the requested theorem statement; step <1>2 gives its cohomological form.
:::
:::
