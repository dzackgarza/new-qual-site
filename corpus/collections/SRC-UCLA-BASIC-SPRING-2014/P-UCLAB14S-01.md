---
schema: qual/card@1
id: P-UCLAB14S-01
kind: problem
title: Minimal polynomial $t^4+1$ and invariant subspaces
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
  note: 'Checked against Problem 1 of the retained UCLA Basic Examination, Spring 2014. Part (b) is false as printed: over the reals, $t^4+1=(t^2+\sqrt2\,t+1)(t^2-\sqrt2\,t+1)$ with coprime nonconstant factors, so an operator with minimal polynomial $t^4+1$ has nonzero proper invariant primary summands. The problem statement is preserved rather than silently corrected.'
---

::: {.problem}
Problem 1.

(a) Find a real matrix $A$ whose minimal polynomial is
\[
t^4+1.
\]

(b) Show that the usual real linear map determined by $v\mapsto Av$ has no nontrivial invariant subspace.
:::

Part (a) has a straightforward example. Part (b) is false as printed.

::: pf

::: pf-step

Let
\[
\boxed{
A=
\begin{pmatrix}
0&0&0&-1\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{pmatrix}.
}
\]
Then
\[
A^4=-I.
\]


::: pf-proof

Let
\[
e_1,e_2,e_3,e_4
\]
be the standard basis.
The matrix acts by
\[
Ae_1=e_2,\qquad
Ae_2=e_3,\qquad
Ae_3=e_4,\qquad
Ae_4=-e_1.
\]
Applying $A$ four times sends every basis vector to its negative.
Hence
\[
A^4=-I.
\]

:::

:::

::: pf-step

Therefore
\[
(A^4+I)=0.
\]


::: pf-proof

This is immediate from step <1>1.
Thus the polynomial
\[
t^4+1
\]
annihilates $A$.

:::

:::

::: pf-step

The vectors
\[
e_1,\ Ae_1,\ A^2e_1,\ A^3e_1
\]
form a basis of $\mathbb R^4$.


::: pf-proof

By step <1>1,
\[
e_1,\ Ae_1,\ A^2e_1,\ A^3e_1
=
e_1,e_2,e_3,e_4.
\]
This is the standard basis.

:::

:::

::: pf-step

No nonzero polynomial of degree at most $3$ annihilates $A$.


::: pf-proof

Suppose
\[
p(t)
=
c_0+c_1t+c_2t^2+c_3t^3
\]
satisfies
\[
p(A)=0.
\]
Apply the operator to $e_1$:
\[
0
=
p(A)e_1
=
c_0e_1
+
c_1Ae_1
+
c_2A^2e_1
+
c_3A^3e_1.
\]
By step <1>3, the four vectors are linearly independent.
Hence
\[
c_0=c_1=c_2=c_3=0.
\]
Thus only the zero polynomial of degree at most $3$ annihilates $A$.

:::

:::

::: pf-step

The minimal polynomial of $A$ is
\[
\boxed{\mu_A(t)=t^4+1}.
\]


::: pf-proof

Step <1>2 shows that the minimal polynomial divides
\[
t^4+1.
\]
Step <1>4 shows that its degree cannot be at most $3$.
Therefore it has degree $4$.
Since it is monic and divides the monic degree-$4$ polynomial $t^4+1$, it must equal that polynomial.
This proves part (a).

:::

:::

::: pf-step

Over the real numbers,
\[
\boxed{
t^4+1
=
\bigl(t^2+\sqrt2\,t+1\bigr)
\bigl(t^2-\sqrt2\,t+1\bigr).
}
\]


::: pf-proof

Multiply:
\[
\begin{aligned}
&\bigl(t^2+\sqrt2\,t+1\bigr)
\bigl(t^2-\sqrt2\,t+1\bigr)\\
&\qquad=
(t^2+1)^2-2t^2\\
&\qquad=
t^4+1.
\end{aligned}
\]
The two quadratic factors are distinct and relatively prime.

:::

:::

::: pf-step

Define
\[
q(t)=t^2+\sqrt2\,t+1
\]
and
\[
r(t)=t^2-\sqrt2\,t+1.
\]
Then
\[
q(A)r(A)=0.
\]


::: pf-proof

By step <1>6,
\[
q(t)r(t)=t^4+1.
\]
By step <1>5,
\[
(A^4+I)=0.
\]
Therefore
\[
q(A)r(A)=0.
\]

:::

:::

::: pf-step

The operator
\[
r(A)
\]
is not the zero operator.


::: pf-proof

If
\[
r(A)=0,
\]
Then the nonzero polynomial $r$ of degree $2$ would annihilate $A$.
This contradicts step <1>5, because the minimal polynomial has degree $4$.

:::

:::

::: pf-step

The subspace
\[
W=\operatorname{im}r(A)
\]
is nonzero and invariant under $A$.


::: pf-proof

Nonzeroness follows from step <1>8.

If
\[
w\in W,
\]
write
\[
w=r(A)v
\]
for some $v$.
Because $A$ commutes with every polynomial in $A$,
\[
Aw
=
Ar(A)v
=
r(A)Av
\in
\operatorname{im}r(A)
=
W.
\]
Thus $W$ is $A$-invariant.

:::

:::

::: pf-step

The invariant subspace $W$ is proper.


::: pf-proof

By step <1>7,
\[
q(A)r(A)=0.
\]
Hence
\[
q(A)w=0
\]
for every
\[
w\in W=\operatorname{im}r(A).
\]
Thus
\[
W\subseteq\ker q(A).
\]

If
\[
W=\mathbb R^4,
\]
then $q(A)$ would vanish on all of $\mathbb R^4$, so
\[
q(A)=0.
\]
That would make the degree-$2$ polynomial $q$ an annihilating polynomial for $A$, again contradicting step <1>5.
Therefore
\[
W\ne\mathbb R^4.
\]
Together with step <1>9,
\[
\boxed{0\ne W\ne\mathbb R^4}.
\]

:::

:::

::: pf-step

Therefore part (b) is false as printed.


::: pf-proof

The matrix in part (a) has minimal polynomial
\[
t^4+1
\]
by step <1>5.
Steps <1>9--<1>10 exhibit a nonzero proper invariant real subspace
\[
W=\operatorname{im}r(A).
\]
Thus the assertion that the associated real linear map has no nontrivial invariant subspace is false.

:::

:::

::: pf-qed

Step <1>5 answers part (a).
Step <1>11 gives the mathematically correct disposition of part (b), namely a counterexample to the source assertion.

:::

:::
