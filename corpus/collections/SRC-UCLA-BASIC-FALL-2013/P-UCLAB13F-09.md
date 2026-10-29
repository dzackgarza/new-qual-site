---
schema: qual/card@1
id: P-UCLAB13F-09
kind: problem
title: An annihilating polynomial of degree at most the dimension
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Fall 2013.
---

::: {.problem}
Let $A$ be an endomorphism of a vector space $V$ of dimension $d$ over a field $F$. Show from first principles, without using Jordan form or the Cayley–Hamilton theorem, that $A$ satisfies a polynomial $P(X)\in F[X]$ of degree at most $d$.
:::

::: {.solution}

The proof is by induction on
$$
d=\dim V.
$$

::: pf

::: {.pf-step #s1-1}

If $d=0$, the assertion is trivial.


::: pf-proof

On the zero vector space, every endomorphism is the zero map, so the polynomial
$$
P(X)=1
$$
satisfies
$$
P(A)=I_V=0.
$$
Its degree is $0\le d$.

:::

:::

::: {.pf-step #s1-2}

Assume $d>0$ and choose a nonzero vector $v\in V$.
There is a least integer
$$
1\le r\le d
$$
such that
$$
v,Av,\ldots,A^rv
$$
are linearly dependent.


::: pf-proof

The $d+1$ vectors
$$
v,Av,\ldots,A^dv
$$
lie in a $d$-dimensional vector space, so they are linearly dependent.
Choose the least index $r$ for which dependence occurs.
Since $v\ne0$, one has $r\ge1$.

:::

:::

::: {.pf-step #s1-3}

The vectors
$$
v,Av,\ldots,A^{r-1}v
$$
are linearly independent, and there exist coefficients
$$
c_0,\ldots,c_{r-1}\in F
$$
such that
$$
A^rv
=
-c_{r-1}A^{r-1}v
-\cdots
-c_1Av
-c_0v.
$$


::: pf-proof

Minimality of $r$ gives linear independence of the first $r$ vectors.
The dependence at stage $r$ therefore expresses $A^rv$ uniquely as a linear combination of them.

:::

:::

::: {.pf-step #s1-4}

Define
$$
W=\operatorname{span}\{v,Av,\ldots,A^{r-1}v\}.
$$
Then
$$
\dim W=r
$$
and $W$ is $A$-invariant.


::: pf-proof

The dimension statement follows from step [](#s1-3){.pf-ref}.
For invariance, note that
$$
A(A^jv)=A^{j+1}v\in W
$$
for
$$
0\le j\le r-2.
$$
For the last basis vector,
$$
A(A^{r-1}v)=A^rv\in W
$$
by the relation in step [](#s1-3){.pf-ref}.
Hence
$$
A(W)\subseteq W.
$$

:::

:::

::: {.pf-step #s1-5}

The polynomial
$$
p(X)
=
X^r+c_{r-1}X^{r-1}+\cdots+c_1X+c_0
$$
annihilates $W$:
$$
p(A)|_W=0.
$$


::: pf-proof

By construction,
$$
p(A)v=0.
$$
Because $p(A)$ is a polynomial in $A$, it commutes with $A$.
Thus for
$$
0\le j\le r-1,
$$
$$
p(A)A^jv
=
A^jp(A)v
=0.
$$
The vectors
$$
v,Av,\ldots,A^{r-1}v
$$
span $W$, so $p(A)$ vanishes on all of $W$.

:::

:::

::: {.pf-step #s1-6}

Since $W$ is $A$-invariant, $A$ induces an endomorphism
$$
\overline A:V/W\to V/W.
$$


::: pf-proof

Define
$$
\overline A(v+W)=Av+W.
$$
If
$$
v-v'\in W,
$$
then $A(v-v')\in W$ because $W$ is $A$-invariant.
Thus the definition is independent of the chosen representative.

:::

:::

::: {.pf-step #s1-7}

By the induction hypothesis, there exists
$$
q(X)\in F[X]
$$
with
$$
\deg q\le d-r
$$
such that
$$
q(\overline A)=0
$$
on $V/W$.


::: pf-proof

The quotient has dimension
$$
\dim(V/W)
=
d-r
<
d.
$$
Hence the induction hypothesis applies to the endomorphism $\overline A$.

:::

:::

::: {.pf-step #s1-8}

The relation
$$
q(\overline A)=0
$$
implies
$$
q(A)V\subseteq W.
$$


::: pf-proof

For every $u\in V$,
$$
q(\overline A)(u+W)
=
q(A)u+W.
$$
Since the left side is zero in the quotient,
$$
q(A)u\in W.
$$
Thus
$$
q(A)V\subseteq W.
$$

:::

:::

::: {.pf-step #s1-9}

The polynomial
$$
P(X)=p(X)q(X)
$$
annihilates $A$:
$$
\boxed{P(A)=0}.
$$


::: pf-proof

For every $u\in V$, step [](#s1-8){.pf-ref} gives
$$
q(A)u\in W.
$$
Step [](#s1-5){.pf-ref} says that $p(A)$ annihilates every vector in $W$.
Therefore
$$
P(A)u
=
p(A)q(A)u
=0.
$$
Since $u$ was arbitrary,
$$
P(A)=0.
$$

:::

:::

::: {.pf-step #s1-10}

The polynomial $P$ has degree at most $d$.


::: pf-proof

By construction,
$$
\deg p=r,
$$
and by step [](#s1-7){.pf-ref},
$$
\deg q\le d-r.
$$
Hence
$$
\deg P
=
\deg p+\deg q
\le
r+(d-r)
=d.
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-10){.pf-ref} prove by induction that every endomorphism of a $d$-dimensional vector space satisfies a polynomial of degree at most $d$, without using Jordan form or Cayley--Hamilton.

:::

:::

:::
