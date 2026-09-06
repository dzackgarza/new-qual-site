---
schema: qual/card@1
id: P-RC7YY
kind: problem
title: Unitary operators, invertibility of $S-\lambda I$ for $|\lambda|<1$, and the
  positive harmonic function $\operatorname{Re}\langle(S+\lambda I)(S-\lambda I)^{-1}v,v\rangle$
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Harmonic Functions
  - Functional Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against problem 7 of the UCLA Analysis Qualifying Exam, Fall 2009, from the collection provenance PDF.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Replaced the old definition, which omitted surjectivity, and the invalid
    infinite-dimensional inference injective=>invertible. Factored
    S-lambda I through I-lambda S^{-1} and used the Neumann series. For
    w=(S-lambda I)^{-1}v, direct expansion gives
    Re h=(1-|lambda|^2)||w||^2; holomorphy follows from the same Neumann series.
---

::: {.problem}
a. Define *unitary operator* on a complex Hilbert space.

b. Let $S$ be a unitary operator on a complex Hilbert space.
Prove that for every complex number $|\lambda|<1$ the operator $S-\lambda I$ is invertible.

c. For a fixed vector $v$ in the Hilbert space and all $|\lambda|<1$, define $$h(\lambda) = \langle (S+\lambda I)(S-\lambda I)^{-1}v, v\rangle.$$ Show $\text{Re}(h)$ is a positive harmonic function (you may not use the spectral theorem).
:::

::: {.solution}
<1>1. A bounded linear operator $S:H\to H$ on a complex Hilbert space is unitary if it is surjective and
\[
\langle Sx,Sy\rangle=\langle x,y\rangle
\]
for all $x,y\in H$.
Equivalently,
\[
S^*S=SS^*=I.
\]
::: {.proof}
The first condition is a standard definition.
It implies
\[
\|Sx\|=\|x\|,
\]
so $S$ is an isometry.
Surjectivity then makes it bijective, and its inverse is its adjoint:
\[
S^{-1}=S^*.
\]
Thus $S^*S=SS^*=I$.
Conversely, those two identities imply both inner-product preservation and invertibility.
:::

<1>2. If $|\lambda|<1$, then
\[
I-\lambda S^{-1}
\]
is invertible, with
\[
(I-\lambda S^{-1})^{-1}
=\sum_{n=0}^\infty\lambda^nS^{-n}
\]
where the series converges in operator norm.
::: {.proof}
Since $S$ is unitary,
\[
\|S^{-1}\|=1.
\]
Hence
\[
\|\lambda S^{-1}\|=|\lambda|<1.
\]
The Neumann series theorem therefore gives
\[
(I-\lambda S^{-1})^{-1}
=\sum_{n=0}^\infty(\lambda S^{-1})^n
=\sum_{n=0}^\infty\lambda^nS^{-n}.
\]
:::

<1>3. For every $|\lambda|<1$, the operator $S-\lambda I$ is invertible.
::: {.proof}
Factor
\[
S-\lambda I
=S(I-\lambda S^{-1}).
\]
Both factors are invertible: $S$ by unitarity and the second factor by <1>2.
Thus
\[
(S-\lambda I)^{-1}
=(I-\lambda S^{-1})^{-1}S^{-1}.
\]
This proves part (b).
:::

<1>4. The scalar-valued function
\[
h(\lambda)
=\langle(S+\lambda I)(S-\lambda I)^{-1}v,v\rangle
\]
is holomorphic on the unit disk.
::: {.proof}
By <1>2--<1>3,
\[
(S-\lambda I)^{-1}
=\left(\sum_{n=0}^\infty\lambda^nS^{-n}\right)S^{-1}
=\sum_{n=0}^\infty\lambda^nS^{-(n+1)},
\]
with convergence in operator norm uniformly on every closed disk
\[
|\lambda|\le r<1.
\]
Thus
\[
\lambda\longmapsto(S-\lambda I)^{-1}
\]
is an operator-valued holomorphic function on $|\lambda|<1$.
Multiplication by $S+\lambda I$, application to the fixed vector $v$, and pairing with $v$ preserve holomorphy.
Hence $h$ is holomorphic.
:::

<1>5. For $|\lambda|<1$, let
\[
w=(S-\lambda I)^{-1}v.
\]
Then
\[
\operatorname{Re}h(\lambda)
=(1-|\lambda|^2)\|w\|^2.
\]
::: {.proof}
Since
\[
v=(S-\lambda I)w,
\]
we have
\[
h(\lambda)
=\langle(S+\lambda I)w,(S-\lambda I)w\rangle.
\]
Using the convention that the inner product is linear in its first variable, expand:
\[
\begin{aligned}
h(\lambda)
&=\|Sw\|^2-|\lambda|^2\|w\|^2
-\overline\lambda\langle Sw,w\rangle
+\lambda\langle w,Sw\rangle.
\end{aligned}
\]
Because
\[
\langle w,Sw\rangle
=\overline{\langle Sw,w\rangle},
\]
the last two terms have purely imaginary sum.
Therefore
\[
\operatorname{Re}h(\lambda)
=\|Sw\|^2-|\lambda|^2\|w\|^2.
\]
Unitarity gives
\[
\|Sw\|=\|w\|,
\]
so
\[
\operatorname{Re}h(\lambda)
=(1-|\lambda|^2)\|w\|^2.
\]
:::

<1>6. The function $\operatorname{Re}h$ is harmonic and nonnegative on the unit disk; if $v\ne0$, it is strictly positive.
::: {.proof}
By <1>4, $h$ is holomorphic.
The real part of a holomorphic function is harmonic, so
\[
\operatorname{Re}h
\]
is harmonic.

By <1>5 and $|\lambda|<1$,
\[
\operatorname{Re}h(\lambda)
=(1-|\lambda|^2)\|(S-\lambda I)^{-1}v\|^2
\ge0.
\]
If $v\ne0$, invertibility of $S-\lambda I$ implies
\[
(S-\lambda I)^{-1}v\ne0,
\]
so the right side is strictly positive.
If $v=0$, then $h\equiv0$, giving the nonnegative degenerate case.
This proves part (c) without the spectral theorem.
:::
:::
