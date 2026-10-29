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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Part (b) of the exam asked to show that A has no nontrivial invariant subspace, which is false because t^4+1 factors over R into two coprime quadratics; part (b) now asks to prove or disprove that assertion.
---

::: {.problem}
Problem 1.

(a) Find a real matrix $A$ whose minimal polynomial is
\[
t^4+1.
\]

(b) Prove or disprove: the usual real linear map determined by $v\mapsto Av$ has no nontrivial invariant subspace.
:::

::: {.solution}

Part (a) has a straightforward example. The assertion in part (b) is false.

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

Therefore
\[
(A^4+I)=0.
\]


::: pf-proof

This is immediate from step [](#s1-1){.pf-ref}.
Thus the polynomial
\[
t^4+1
\]
annihilates $A$.

:::

:::

::: {.pf-step #s1-3}

The vectors
\[
e_1,\ Ae_1,\ A^2e_1,\ A^3e_1
\]
form a basis of $\RR^4$.


::: pf-proof

By step [](#s1-1){.pf-ref},
\[
e_1,\ Ae_1,\ A^2e_1,\ A^3e_1
=
e_1,e_2,e_3,e_4.
\]
This is the standard basis.

:::

:::

::: {.pf-step #s1-4}

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
By step [](#s1-3){.pf-ref}, the four vectors are linearly independent.
Hence
\[
c_0=c_1=c_2=c_3=0.
\]
Thus only the zero polynomial of degree at most $3$ annihilates $A$.

:::

:::

::: {.pf-step #s1-5}

The minimal polynomial of $A$ is
\[
\boxed{\mu_A(t)=t^4+1}.
\]


::: pf-proof

Step [](#s1-2){.pf-ref} shows that the minimal polynomial divides
\[
t^4+1.
\]
Step [](#s1-4){.pf-ref} shows that its degree cannot be at most $3$.
Therefore it has degree $4$.
Since it is monic and divides the monic degree-$4$ polynomial $t^4+1$, it must equal that polynomial.
This proves part (a).

:::

:::

::: {.pf-step #s1-6}

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

::: {.pf-step #s1-7}

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

By step [](#s1-6){.pf-ref},
\[
q(t)r(t)=t^4+1.
\]
By step [](#s1-5){.pf-ref},
\[
(A^4+I)=0.
\]
Therefore
\[
q(A)r(A)=0.
\]

:::

:::

::: {.pf-step #s1-8}

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
This contradicts step [](#s1-5){.pf-ref}, because the minimal polynomial has degree $4$.

:::

:::

::: {.pf-step #s1-9}

The subspace
\[
W=\operatorname{im}r(A)
\]
is nonzero and invariant under $A$.


::: pf-proof

Nonzeroness follows from step [](#s1-8){.pf-ref}.

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

::: {.pf-step #s1-10}

The invariant subspace $W$ is proper.


::: pf-proof

By step [](#s1-7){.pf-ref},
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
W=\RR^4,
\]
then $q(A)$ would vanish on all of $\RR^4$, so
\[
q(A)=0.
\]
That would make the degree-$2$ polynomial $q$ an annihilating polynomial for $A$, again contradicting step [](#s1-5){.pf-ref}.
Therefore
\[
W\ne\RR^4.
\]
Together with step [](#s1-9){.pf-ref},
\[
\boxed{0\ne W\ne\RR^4}.
\]

:::

:::

::: {.pf-step #s1-11}

Therefore the assertion in part (b) is false.


::: pf-proof

The matrix in part (a) has minimal polynomial
\[
t^4+1
\]
by step [](#s1-5){.pf-ref}.
Steps [](#s1-9){.pf-ref} through [](#s1-10){.pf-ref} exhibit a nonzero proper invariant real subspace
\[
W=\operatorname{im}r(A).
\]
Thus the assertion that the associated real linear map has no nontrivial invariant subspace is false.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} answers part (a).
Step [](#s1-11){.pf-ref} disproves the assertion in part (b).

:::

:::

:::
