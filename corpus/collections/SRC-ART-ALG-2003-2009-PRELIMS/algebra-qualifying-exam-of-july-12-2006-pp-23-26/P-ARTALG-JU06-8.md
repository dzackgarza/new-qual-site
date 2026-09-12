---
schema: qual/card@1
id: P-ARTALG-JU06-8
kind: problem
title: 'Nonisomorphism of $\QQ(\sqrt{2})$ and $\QQ(\sqrt{3})$'
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the abstract field-isomorphism question with July 2006 Fields 8 in the retained source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked that any field isomorphism fixes the prime field and excluded both possible coefficient cases by parity of prime exponents."
---

::: problem
Show that $\mathbb{Q}(\sqrt{2})$ and $\mathbb{Q}(\sqrt{3})$ are not isomorphic.
:::

::: solution
<1>1. Every field isomorphism between these fields fixes $\mathbb Q$.

::: proof
A field isomorphism sends $1$ to $1$, hence fixes every integer.
It preserves inverses, so it also fixes every quotient of integers
with nonzero denominator. Thus it fixes the prime subfield
$\mathbb Q$ pointwise, even though this was not separately required
in the question.
:::

<1>2. The field $\mathbb Q(\sqrt3)$ contains no element whose square is $2$.

::: proof
For a prime $\ell$ and a nonzero rational number $r$, let
$v_\ell(r)$ be the exponent of $\ell$ in its numerator minus the
exponent in its denominator. Unique prime factorization gives
$v_\ell(r^2)=2v_\ell(r)$, an even integer. Consequently $3$ is
not a rational square, since $v_3(3)=1$. Hence
$1,\sqrt3$ are linearly independent over $\mathbb Q$ and form a
basis of the quadratic field $\mathbb Q(\sqrt3)$.

Suppose $(a+b\sqrt3)^2=2$ with $a,b\in\mathbb Q$. Expanding and
comparing the two basis coefficients gives
$$
a^2+3b^2=2,\qquad 2ab=0.
$$
If $b=0$, then $a^2=2$, contradicting $v_2(2)=1$.
If $a=0$, then $b^2=2/3$, contradicting $v_2(2/3)=1$.
The equation $2ab=0$ forces at least one of these cases, so there
is no such element.
:::

<1>3. The fields are not isomorphic.

::: proof
If an isomorphism $\sigma:\mathbb Q(\sqrt2)\to\mathbb Q(\sqrt3)$
existed, step <1>1 would give
$\sigma(\sqrt2)^2=\sigma(2)=2$. This contradicts step <1>2.
:::
:::
