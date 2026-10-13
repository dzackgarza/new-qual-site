---
schema: qual/card@1
id: P-KSRING17-088
kind: problem
title: Greatest common divisors from principal ideal sums
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 88 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D be an integral domain.

(a) For $a , b \in D$ define a greatest common divisor of a and b.

(b) For $x \in D$ denote $( x ) = \{ d x \mid d \in D \}$ . Prove that if $( a ) + ( b ) = ( d )$ , then d is a greatest common divisor of a and b.
:::

::: {.solution}
<1>1. A greatest common divisor of
$$
a,b\in D
$$
is an element
$$
d\in D
$$
such that
$$
d\mid a,
\qquad
d\mid b,
$$
and whenever
$$
c\mid a
\qquad\text{and}\qquad
c\mid b,
$$
one has
$$
c\mid d.
$$

::: {.proof}
This is the standard divisibility definition of a greatest common divisor in an integral domain.
Such a gcd is unique only up to multiplication by a unit.
:::

<1>2. Assume
$$
(a)+(b)=(d).
$$
Then
$$
d\mid a
\qquad\text{and}\qquad
d\mid b.
$$

::: {.proof}
Since
$$
a\in(a)
\subseteq
(a)+(b)
=(d),
$$
there exists
$$
r\in D
$$
such that
$$
a=rd.
$$
Hence
$$
d\mid a.
$$

Similarly,
$$
b\in(b)
\subseteq
(d),
$$
so
$$
b=sd
$$
for some
$$
s\in D.
$$
Thus
$$
d\mid b.
$$
:::

<1>3. Because
$$
d\in(d)
=(a)+(b),
$$
there exist
$$
u,v\in D
$$
such that
$$
d=ua+vb.
$$

::: {.proof}
By definition,
$$
(a)+(b)
=
\{ra+sb:r,s\in D\}.
$$
Since
$$
d
\in
(a)+(b),
$$
the displayed representation follows.
:::

<1>4. Let
$$
c\in D
$$
be any common divisor of $a$ and $b$.
Then
$$
c\mid d.
$$

::: {.proof}
Because
$$
c\mid a
\qquad\text{and}\qquad
c\mid b,
$$
write
$$
a=cr,
\qquad
b=cs
$$
for some
$$
r,s\in D.
$$
Using step <1>3,
$$
\begin{aligned}
d
&=
ua+vb\\
&=
u(cr)+v(cs)\\
&=
c(ur+vs).
\end{aligned}
$$
Hence
$$
c\mid d.
$$
:::

<1>5. Therefore
$$
\boxed{
d
\text{ is a greatest common divisor of }a\text{ and }b.
}
$$

::: {.proof}
Step <1>2 shows that $d$ is a common divisor.
Step <1>4 shows that every common divisor divides $d$.
These are exactly the two conditions in the definition from step <1>1.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>1 answers part (a), and step <1>5 proves part (b).
:::
:::
