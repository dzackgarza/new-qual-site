---
schema: qual/card@1
id: P-APAF25E
kind: problem
title: Normal algebra elements are $X+iY$ with commuting selfadjoint parts
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Let $\mathcal{A}$ be a unital associative algebra over $\mathbb{C}$ equipped with an antilinear and antimultiplicative involution $A\mapsto A^*$.
We say that $A\in\mathcal{A}$ is normal if $A$ and $A^*$ commute (example: normal matrices are normal elements of $\mathbb{C}^{N\times N}$). Prove that $A$ is normal if and only if $A=X+iY$ with $X,Y\in\mathcal{A}$ commuting ($XY=YX$) and selfadjoint ($X^*=X$, $Y^*=Y$).
:::

::: {.solution}

::: pf

::: {.pf-step #decomposition-exists}
Every \(A\in\mathcal A\) has a decomposition
\[
A=X+iY
\]
with
\[
X:=\frac{A+A^*}{2},
\qquad
Y:=\frac{A-A^*}{2i}.
\]
Both \(X\) and \(Y\) are selfadjoint.

::: pf-proof
Using antilinearity of the involution,
\[
X^*=\frac{A^*+A}{2}=X.
\]
Also
\[
Y^*
=\left(\frac1{2i}\right)^*(A-A^*)^*
=-\frac1{2i}(A^*-A)
=\frac{A-A^*}{2i}
=Y.
\]
Finally,
\[
X+iY
=\frac{A+A^*}{2}+\frac{A-A^*}{2}
=A.
\]
:::

:::

::: {.pf-step #commutator-formula}
If \(A=X+iY\) with \(X^*=X\) and \(Y^*=Y\), then
\[
A^*=X-iY
\]
and
\[
AA^*-A^*A=2i(YX-XY).
\]

::: pf-proof
Antilinearity gives
\[
A^*=(X+iY)^*=X-iY.
\]
Hence
\[
\begin{aligned}
AA^*&=(X+iY)(X-iY)=X^2+Y^2+i(YX-XY),\\
A^*A&=(X-iY)(X+iY)=X^2+Y^2+i(XY-YX).
\end{aligned}
\]
Subtracting yields
\[
AA^*-A^*A=2i(YX-XY).
\]
:::

:::

::: {.pf-step #normal-implies-xy-commute}
If \(A\) is normal, then in the decomposition from step [](#decomposition-exists){.pf-ref} the selfadjoint elements \(X,Y\) commute.

::: pf-proof
Normality means
\[
AA^*=A^*A.
\]
By step [](#commutator-formula){.pf-ref},
\[
2i(YX-XY)=0.
\]
Since the algebra is over \(\mathbb C\), the scalar \(2i\) is invertible, so
\[
YX=XY.
\]
:::

:::

::: {.pf-step #commuting-implies-normal}
Conversely, if \(A=X+iY\) with \(X,Y\) selfadjoint and commuting, then \(A\) is normal.

::: pf-proof
If \(XY=YX\), then step [](#commutator-formula){.pf-ref} gives
\[
AA^*-A^*A=2i(YX-XY)=0.
\]
Thus \(AA^*=A^*A\), so \(A\) is normal.
:::

:::

::: pf-step
Therefore \(A\) is normal if and only if it can be written as \(A=X+iY\) with \(X,Y\) commuting and selfadjoint.

::: pf-proof
The forward implication is step [](#decomposition-exists){.pf-ref} together with step [](#normal-implies-xy-commute){.pf-ref}; the reverse implication is step [](#commuting-implies-normal){.pf-ref}.
:::

:::

:::

:::
