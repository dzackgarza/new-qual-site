---
schema: qual/card@1
id: P-KSRING17-087
kind: problem
title: An integral domain finite-dimensional over a subfield is a field
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 87 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be an integral domain containing the subfield F and assume that R is finite dimensional over F when viewed as a vector space over F . Prove that R is a field.
:::

::: {.solution}
Let
$$
0\ne a\in R.
$$
Define
$$
\mu_a:R\to R
$$
by
$$
\mu_a(x)
\coloneqq
ax.
$$

<1>1. The map $\mu_a$ is $F$-linear.

::: {.proof}
For
$$
x,y\in R
$$
and
$$
\lambda\in F,
$$
one has
$$
\mu_a(x+y)
=
a(x+y)
=
ax+ay
=
\mu_a(x)+\mu_a(y),
$$
and, because $R$ is commutative and
$$
F\subseteq R,
$$
$$
\mu_a(\lambda x)
=
a(\lambda x)
=
\lambda(ax)
=
\lambda\mu_a(x).
$$
Thus $\mu_a$ is an $F$-linear transformation.
:::

<1>2. The map $\mu_a$ is injective.

::: {.proof}
Suppose
$$
\mu_a(x)=0.
$$
Then
$$
ax=0.
$$
Since $R$ is an integral domain and
$$
a\ne0,
$$
one must have
$$
x=0.
$$
Therefore
$$
\ker\mu_a=0,
$$
so $\mu_a$ is injective.
:::

<1>3. The map $\mu_a$ is surjective.

::: {.proof}
The vector space
$$
R
$$
is finite dimensional over
$$
F
$$
by hypothesis.
An injective linear endomorphism of a finite-dimensional vector space is surjective.
Step <1>2 shows that $\mu_a$ is injective.
Hence $\mu_a$ is surjective.
:::

<1>4. There exists
$$
b\in R
$$
such that
$$
ab=1.
$$

::: {.proof}
By step <1>3,
$$
\mu_a
$$
is surjective.
Therefore the element
$$
1\in R
$$
has a preimage
$$
b\in R.
$$
Thus
$$
\mu_a(b)
=
ab
=
1.
$$
:::

<1>5. Every nonzero element of $R$ is a unit.

::: {.proof}
The nonzero element
$$
a\in R
$$
was arbitrary.
Step <1>4 constructs
$$
b\in R
$$
with
$$
ab=1.
$$
Since $R$ is commutative,
$$
ba=1
$$
as well.
Hence every nonzero element is invertible.
:::

<1>6. Therefore
$$
\boxed{
R\text{ is a field}.
}
$$

::: {.proof}
The ring $R$ is already a commutative ring with identity and has no zero divisors.
Step <1>5 shows that every nonzero element has an inverse.
This is exactly the definition of a field.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
