---
schema: qual/card@1
id: P-KSRING17-012
kind: problem
title: Finite commutative rings without zero divisors are fields
classification:
  areas: [algebra]
  topics:
  - Finite Rings
  - Fields
  - Zero Divisors
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 12 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a finite commutative ring with more than one element and no zero-divisors.
Show that R is a field.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every nonzero $a\in R$, the map
$$
L_a:R\to R,
\qquad
L_a(x)=ax
$$
is injective.


::: pf-proof

Suppose
$$
ax=ay.
$$
Then
$$
a(x-y)=0.
$$
Since $a\ne0$ and $R$ has no zero divisors,
$$
x-y=0.
$$
Hence
$$
x=y,
$$
so $L_a$ is injective.

:::

:::

::: {.pf-step #s1-2}

For every nonzero $a\in R$, the map $L_a$ is bijective.


::: pf-proof

The set $R$ is finite. Any injective self-map of a finite set is surjective. Apply this to $L_a$ from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The ring $R$ has a multiplicative identity.


::: pf-proof

Because $R$ has more than one element, choose
$$
a\in R,
\qquad
a\ne0.
$$
By step [](#s1-2){.pf-ref}, $L_a$ is surjective. Hence there exists
$$
e\in R
$$
such that
$$
ae=a.
$$

Let $x\in R$ be arbitrary. Using commutativity,
$$
\begin{aligned}
a(ex-x)
&=
aex-ax\\
&=
(ae)x-ax\\
&=
ax-ax\\
&=
0.
\end{aligned}
$$
Since $a\ne0$ and there are no zero divisors,
$$
ex-x=0.
$$
Thus
$$
ex=x
$$
for every $x\in R$. By commutativity also
$$
xe=x.
$$
Hence $e$ is a multiplicative identity.

:::

:::

::: {.pf-step #s1-4}

Every nonzero element of $R$ is invertible.


::: pf-proof

Let
$$
x\in R,
\qquad
x\ne0.
$$
By step [](#s1-2){.pf-ref}, the multiplication map
$$
L_x:R\to R
$$
is surjective. Therefore there exists
$$
y\in R
$$
such that
$$
xy=e,
$$
where $e$ is the identity from step [](#s1-3){.pf-ref}. Since $R$ is commutative,
$$
yx=e
$$
as well. Thus $y$ is the multiplicative inverse of $x$.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{R\text{ is a field}.}
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, $R$ is a nonzero commutative ring with identity. By step [](#s1-4){.pf-ref}, every nonzero element has a multiplicative inverse. This is exactly the definition of a field.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
