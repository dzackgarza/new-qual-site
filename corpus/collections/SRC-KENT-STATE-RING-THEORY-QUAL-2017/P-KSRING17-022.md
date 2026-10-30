---
schema: qual/card@1
id: P-KSRING17-022
kind: problem
title: Unital extension of a ring of characteristic $n$ with quotient $\ZZ/n\ZZ$
classification:
  areas: [algebra]
  topics:
  - Rings Without Identity
  - Unitization
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 22 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring, not necessarily with identity, and assume there is some fixed positive integer n such that $n r = 0$ for all $r \in R .$ . Prove that R embeds in a ring S with identity so that R is an ideal of S and $S / R \cong \ZZ / n \ZZ$
:::

::: {.solution}

Let
$$
A
\coloneqq
\ZZ/n\ZZ.
$$
Because
$$
nr=0
$$
for every $r\in R$, the additive group of $R$ is naturally an $A$-module via
$$
\overline k\,r
\coloneqq
kr.
$$

::: pf

::: {.pf-step #s1-1}

The scalar action of $A$ on $R$ is well-defined.


::: pf-proof

Suppose
$$
\overline k=\overline\ell
\in
\ZZ/n\ZZ.
$$
Then
$$
k-\ell=qn
$$
for some $q\in\ZZ$. Hence for every $r\in R$,
$$
kr-\ell r
=
(k-\ell)r
=
qnr
=
0.
$$
Thus
$$
kr=\ell r,
$$
so the action depends only on the residue class modulo $n$.

:::

:::

::: {.pf-step #s1-2}

Define
$$
S
\coloneqq
A\oplus R
$$
as an abelian group, with multiplication
$$
(\alpha,r)(\beta,s)
\coloneqq
\left(
\alpha\beta,
\alpha s+\beta r+rs
\right).
$$
Then $S$ is a commutative ring.


::: pf-proof

The multiplication is well-defined by step [](#s1-1){.pf-ref}.
Distributivity follows from distributivity in $A$ and $R$ and from the $A$-module structure.

Commutativity holds because $A$ and $R$ are commutative:
$$
\begin{aligned}
(\alpha,r)(\beta,s)
&=
(\alpha\beta,\alpha s+\beta r+rs)\\
&=
(\beta\alpha,\beta r+\alpha s+sr)\\
&=
(\beta,s)(\alpha,r).
\end{aligned}
$$

For associativity, compute
$$
\begin{aligned}
((\alpha,r)(\beta,s))(\gamma,t)
&=
(\alpha\beta,\alpha s+\beta r+rs)(\gamma,t)\\
&=
\bigl(
\alpha\beta\gamma,\,
\alpha\beta t
+\gamma\alpha s
+\gamma\beta r
+\gamma rs\\
&\qquad\qquad
+\alpha st
+\beta rt
+rst
\bigr),
\end{aligned}
$$
while
$$
\begin{aligned}
(\alpha,r)((\beta,s)(\gamma,t))
&=
(\alpha,r)(\beta\gamma,\beta t+\gamma s+st)\\
&=
\bigl(
\alpha\beta\gamma,\,
\alpha\beta t
+\alpha\gamma s
+\alpha st\\
&\qquad\qquad
+\beta\gamma r
+\beta rt
+\gamma rs
+rst
\bigr).
\end{aligned}
$$
The second coordinates agree by commutativity of scalar multiplication, so multiplication is associative.

:::

:::

::: {.pf-step #s1-3}

The element
$$
1_S
\coloneqq
(\overline1,0)
$$
is a multiplicative identity of $S$.


::: pf-proof

For every
$$
(\alpha,r)\in S,
$$
one has
$$
\begin{aligned}
(\overline1,0)(\alpha,r)
&=
(\alpha,\overline1\,r+\alpha0+0r)\\
&=
(\alpha,r).
\end{aligned}
$$
Commutativity gives the same identity on the other side.

:::

:::

::: {.pf-step #s1-4}

The map
$$
\iota:R\to S,
\qquad
\iota(r)
\coloneqq
(0,r)
$$
is an injective ring homomorphism.


::: pf-proof

It is clearly injective and additive. Moreover,
$$
\iota(r)\iota(s)
=
(0,r)(0,s)
=
(0,rs)
=
\iota(rs).
$$
Thus $\iota$ is a ring embedding.

:::

:::

::: {.pf-step #s1-5}

The image
$$
\iota(R)
=
\{(0,r):r\in R\}
$$
is an ideal of $S$.


::: pf-proof

It is an additive subgroup. For
$$
(\alpha,s)\in S
$$
and
$$
(0,r)\in\iota(R),
$$
one has
$$
(\alpha,s)(0,r)
=
(0,\alpha r+sr)
\in
\iota(R).
$$
By commutativity, multiplication on the other side gives the same conclusion. Hence $\iota(R)\trianglelefteq S$.

:::

:::

::: {.pf-step #s1-6}

The projection
$$
\pi:S\to A,
\qquad
\pi(\alpha,r)
\coloneqq
\alpha
$$
is a surjective ring homomorphism with kernel $\iota(R)$.


::: pf-proof

The definition of multiplication in $S$ gives
$$
\pi((\alpha,r)(\beta,s))
=
\alpha\beta
=
\pi(\alpha,r)\pi(\beta,s),
$$
and addition is preserved coordinatewise. Surjectivity follows from
$$
\pi(\alpha,0)=\alpha.
$$
Finally,
$$
\pi(\alpha,r)=0
\iff
\alpha=0,
$$
so
$$
\ker\pi
=
\{(0,r):r\in R\}
=
\iota(R).
$$

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
S/\iota(R)
\cong
\ZZ/n\ZZ.
}
$$


::: pf-proof

By step [](#s1-6){.pf-ref}, the first isomorphism theorem gives
$$
S/\ker\pi
\cong
A.
$$
Substitute
$$
\ker\pi=\iota(R)
$$
and
$$
A=\ZZ/n\ZZ.
$$

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} construct a unital ring $S$, steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} embed $R$ as an ideal of $S$, and step [](#s1-7){.pf-ref} identifies the quotient.

:::

:::

:::
