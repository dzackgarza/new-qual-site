---
schema: qual/card@1
id: P-KSRING17-120
kind: problem
title: Construction of the field of fractions of an integral domain
classification:
  areas: [algebra]
  topics:
  - Fields of Fractions
  - Integral Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 120 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be an integral domain.
Construct the field of fractions F of R by defining the set F and the two binary operations, and show that the two operations are well-defined.
Show that F has a multiplicative identity element and that every nonzero element of F has a multiplicative inverse.
:::

::: {.solution}

Let
$$
S
\coloneqq
\{(a,b)\in R\times R:b\ne0\}.
$$
Define a relation on $S$ by
$$
(a,b)\sim(c,d)
\quad\Longleftrightarrow\quad
ad=bc.
$$

::: pf

::: {.pf-step #s1-1}

The relation $\sim$ is reflexive.


::: pf-proof

For
$$
(a,b)\in S,
$$
one has
$$
ab=ba
$$
because $R$ is commutative.
Hence
$$
(a,b)\sim(a,b).
$$

:::

:::

::: {.pf-step #s1-2}

The relation $\sim$ is symmetric.


::: pf-proof

If
$$
(a,b)\sim(c,d),
$$
then
$$
ad=bc.
$$
By symmetry of equality,
$$
cb=da,
$$
so
$$
(c,d)\sim(a,b).
$$

:::

:::

::: {.pf-step #s1-3}

The relation $\sim$ is transitive.


::: pf-proof

Suppose
$$
(a,b)\sim(c,d)
$$
and
$$
(c,d)\sim(e,f).
$$
Then
$$
ad=bc
$$
and
$$
cf=de.
$$
Multiply the first equality by $f$:
$$
adf=bcf.
$$
Using
$$
cf=de,
$$
the right-hand side becomes
$$
bde.
$$
Thus
$$
d(af-be)=0.
$$
Since
$$
d\ne0
$$
and $R$ is an integral domain,
$$
af-be=0.
$$
Hence
$$
af=be,
$$
so
$$
(a,b)\sim(e,f).
$$

:::

:::

::: {.pf-step #s1-4}

Therefore $\sim$ is an equivalence relation on $S$.


::: pf-proof

Combine steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Define
$$
F
\coloneqq
S/{\sim}.
$$
Write the equivalence class of $(a,b)$ as
$$
\frac ab.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} makes the quotient set well-defined.

:::

:::

::: {.pf-step #s1-6}

Define addition on $F$ by
$$
\boxed{
\frac ab+\frac cd
\coloneqq
\frac{ad+bc}{bd}.
}
$$


::: pf-proof

Because
$$
b,d\ne0
$$
and $R$ is a domain,
$$
bd\ne0.
$$
Thus
$$
(ad+bc,bd)\in S,
$$
so the displayed expression determines an element of $F$.

:::

:::

::: {.pf-step #s1-7}

Addition is independent of the representatives.


::: pf-proof

Suppose
$$
\frac ab=\frac{a'}{b'}
$$
and
$$
\frac cd=\frac{c'}{d'}.
$$
Then
$$
ab'=a'b
$$
and
$$
cd'=c'd.
$$
We must show
$$
\frac{ad+bc}{bd}
=
\frac{a'd'+b'c'}{b'd'}.
$$
This is equivalent to
$$
(ad+bc)b'd'
=
(a'd'+b'c')bd.
$$
Expanding the left side,
$$
\begin{aligned}
(ad+bc)b'd'
&=
adb'd'
+bcb'd'\\
&=
(ab')dd'
+bb'(cd')\\
&=
(a'b)dd'
+bb'(c'd)\\
&=
a'd'bd
+b'c'bd\\
&=
(a'd'+b'c')bd.
\end{aligned}
$$
Thus the two sums represent the same equivalence class.

:::

:::

::: {.pf-step #s1-8}

Define multiplication on $F$ by
$$
\boxed{
\frac ab\cdot\frac cd
\coloneqq
\frac{ac}{bd}.
}
$$


::: pf-proof

Again,
$$
bd\ne0
$$
because $R$ is a domain and
$$
b,d\ne0.
$$
Thus the displayed fraction is an element of $F$.

:::

:::

::: {.pf-step #s1-9}

Multiplication is independent of the representatives.


::: pf-proof

Suppose
$$
\frac ab=\frac{a'}{b'}
$$
and
$$
\frac cd=\frac{c'}{d'}.
$$
Then
$$
ab'=a'b
$$
and
$$
cd'=c'd.
$$
We must prove
$$
\frac{ac}{bd}
=
\frac{a'c'}{b'd'}.
$$
Equivalently,
$$
ac\,b'd'
=
a'c'\,bd.
$$
But
$$
\begin{aligned}
ac\,b'd'
&=
(ab')(cd')\\
&=
(a'b)(c'd)\\
&=
a'c'\,bd.
\end{aligned}
$$
Hence multiplication is well-defined.

:::

:::

::: {.pf-step #s1-10}

The element
$$
0_F
\coloneqq
\frac01
$$
is an additive identity.


::: pf-proof

For every
$$
\frac ab\in F,
$$
$$
\frac ab+\frac01
=
\frac{a\cdot1+b\cdot0}{b\cdot1}
=
\frac ab.
$$

:::

:::

::: {.pf-step #s1-11}

The additive inverse of
$$
\frac ab
$$
is
$$
\frac{-a}{b}.
$$


::: pf-proof

One has
$$
\frac ab+\frac{-a}{b}
=
\frac{ab-ab}{b^2}
=
\frac0{b^2}
=
\frac01.
$$
The last equality holds because
$$
0\cdot1
=
0\cdot b^2.
$$

:::

:::

::: {.pf-step #s1-12}

The element
$$
1_F
\coloneqq
\frac11
$$
is a multiplicative identity.


::: pf-proof

For every
$$
\frac ab\in F,
$$
$$
\frac ab\cdot\frac11
=
\frac{a}{b}.
$$

:::

:::

::: {.pf-step #s1-13}

A fraction
$$
\frac ab
$$
is zero in $F$ if and only if
$$
a=0.
$$


::: pf-proof

One has
$$
\frac ab
=
\frac01
$$
if and only if
$$
a\cdot1
=
b\cdot0.
$$
Thus
$$
a=0.
$$

:::

:::

::: {.pf-step #s1-14}

If
$$
\frac ab\ne0,
$$
then
$$
a\ne0.
$$


::: pf-proof

This is the contrapositive direction of step [](#s1-13){.pf-ref}.

:::

:::

::: {.pf-step #s1-15}

If
$$
\frac ab\ne0,
$$
then
$$
\frac ba
$$
is a well-defined element of $F$.


::: pf-proof

By step [](#s1-14){.pf-ref},
$$
a\ne0.
$$
Thus
$$
(b,a)\in S,
$$
so
$$
b/a
$$
defines an element of $F$.

:::

:::

::: {.pf-step #s1-16}

Every nonzero element of $F$ has a multiplicative inverse.


::: pf-proof

Let
$$
\frac ab\ne0.
$$
By step [](#s1-15){.pf-ref},
$$
\frac ba\in F.
$$
Then
$$
\frac ab\cdot\frac ba
=
\frac{ab}{ba}
=
\frac11,
$$
because
$$
ab=ba.
$$
Thus
$$
\left(
\frac ab
\right)^{-1}
=
\frac ba.
$$

:::

:::

::: {.pf-step #s1-17}

The operations are associative and commutative and satisfy distributivity.


::: pf-proof

These identities follow by direct calculation from the corresponding identities in $R$.
For example,
$$
\begin{aligned}
\left(
\frac ab+\frac cd
\right)
+\frac ef
&=
\frac{ad+bc}{bd}
+\frac ef\\
&=
\frac{(ad+bc)f+bde}{bdf}\\
&=
\frac{adf+bcf+bde}{bdf},
\end{aligned}
$$
while
$$
\begin{aligned}
\frac ab
+
\left(
\frac cd+\frac ef
\right)
&=
\frac ab
+
\frac{cf+de}{df}\\
&=
\frac{adf+b(cf+de)}{bdf}\\
&=
\frac{adf+bcf+bde}{bdf}.
\end{aligned}
$$
The multiplicative and distributive checks are similar.

:::

:::

::: {.pf-step #s1-18}

Therefore
$$
\boxed{
F
\text{ is a field}.
}
$$


::: pf-proof

Steps [](#s1-6){.pf-ref} through [](#s1-9){.pf-ref} define well-defined binary operations.
Steps [](#s1-10){.pf-ref} through [](#s1-12){.pf-ref} give additive and multiplicative identities and additive inverses.
Step [](#s1-16){.pf-ref} gives multiplicative inverses for every nonzero element.
Step [](#s1-17){.pf-ref} supplies the remaining ring axioms.
Hence $F$ is a field.

:::

:::

::: {.pf-step #s1-19}

The map
$$
\iota:R\to F,
\qquad
\iota(r)
\coloneqq
\frac r1
$$
is an injective ring homomorphism.


::: pf-proof

The formulas for addition and multiplication give
$$
\iota(r+s)
=
\frac{r+s}{1}
=
\frac r1+\frac s1
$$
and
$$
\iota(rs)
=
\frac{rs}{1}
=
\frac r1\frac s1.
$$
If
$$
\iota(r)=\iota(s),
$$
then
$$
\frac r1=\frac s1,
$$
so
$$
r=s.
$$
Thus $\iota$ is injective.

:::

:::

::: pf-qed

Steps [](#s1-5){.pf-ref} through [](#s1-18){.pf-ref} construct the field of fractions and verify its operations, identity, and inverses.
Step [](#s1-19){.pf-ref} identifies $R$ with a subring of its fraction field.

:::

:::

:::
