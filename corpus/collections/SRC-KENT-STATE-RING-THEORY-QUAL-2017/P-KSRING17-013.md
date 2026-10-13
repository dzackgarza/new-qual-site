---
schema: qual/card@1
id: P-KSRING17-013
kind: problem
title: When $\mathbb Z/n\mathbb Z$ is a direct sum of fields
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 13 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Determine for which integers n the ring $\mathbb { Z } / n \mathbb { Z }$ is a direct sum of fields.
Prove your answer.
:::

::: {.solution}
For a nonzero integer $n$, the quotient depends only on $\abs n$, so it suffices first to consider
$$
n>1.
$$

<1>1. If $n$ is squarefree, then
$$
\ZZ/n\ZZ
$$
is a finite direct product of fields.

::: {.proof}
Write
$$
n
=
p_1p_2\cdots p_r
$$
with distinct primes $p_i$. The ideals
$$
(p_i)
$$
are pairwise comaximal. By the Chinese remainder theorem,
$$
\ZZ/n\ZZ
\cong
\prod_{i=1}^{r}
\ZZ/p_i\ZZ.
$$
Each factor
$$
\ZZ/p_i\ZZ
$$
is the field $\FF_{p_i}$. Thus the quotient is a finite direct product, equivalently a finite direct sum, of fields.
:::

<1>2. A direct product of fields has no nonzero nilpotent elements.

::: {.proof}
Let
$$
R
=
\prod_{i=1}^{r}K_i
$$
with each $K_i$ a field. If
$$
x=(x_1,\ldots,x_r)
$$
satisfies
$$
x^m=0,
$$
then
$$
x_i^m=0
$$
in every field $K_i$. A field has no nonzero nilpotents, so
$$
x_i=0
$$
for every $i$. Hence
$$
x=0.
$$
:::

<1>3. If $n>1$ is not squarefree, then
$$
\ZZ/n\ZZ
$$
has a nonzero nilpotent element.

::: {.proof}
Since $n$ is not squarefree, there is a prime $p$ such that
$$
p^2\mid n.
$$
Set
$$
a
\coloneqq
\frac np.
$$
The class
$$
\overline a
\in
\ZZ/n\ZZ
$$
is nonzero, because
$$
0<a<n.
$$
But
$$
a^2
=
\frac{n^2}{p^2}
=
n
\left(
\frac{n}{p^2}
\right),
$$
so
$$
a^2\equiv0\pmod n.
$$
Thus $\overline a$ is a nonzero nilpotent.
:::

<1>4. If $n>1$ and
$$
\ZZ/n\ZZ
$$
is a direct sum of fields, then $n$ is squarefree.

::: {.proof}
If $n$ were not squarefree, step <1>3 would produce a nonzero nilpotent in the quotient. Step <1>2 shows that no direct product of fields can contain such an element. Hence $n$ must be squarefree.
:::

<1>5. Therefore, for
$$
\abs n>1,
$$
one has
$$
\boxed{
\ZZ/n\ZZ
\text{ is a direct sum of fields}
\iff
\abs n\text{ is squarefree}.
}
$$

::: {.proof}
Replace $n$ by $\abs n$ and combine steps <1>1 and <1>4.
:::

<1>6. The remaining integer values are exceptional only by convention:

- if $n=0$, then
  $$
  \ZZ/0\ZZ\cong\ZZ,
  $$
  which is not a direct sum of fields;
- if $n=\pm1$, then
  $$
  \ZZ/n\ZZ
  $$
  is the zero ring.

::: {.proof}
For $n=0$, the ring $\ZZ$ is not a field and has no nontrivial idempotents. A finite product of at least two nonzero fields has nontrivial idempotents, while a product of one field is a field. Hence $\ZZ$ is not such a product.

For $n=\pm1$, the quotient is the zero ring. If the empty direct sum of fields is allowed, it is included as that empty sum; under the usual convention that a direct sum here has at least one field factor, it is excluded.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>5 gives the substantive classification, with step <1>6 recording the degenerate integer cases.
:::
:::
