---
schema: qual/card@1
id: P-KSRING17-104
kind: problem
title: If nonzero primes of $D[x]$ are maximal then $D$ is a field
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 104 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D be an integral domain and $D [ x ]$ the polynomial ring over D in the indeterminate x. Show that if every nonzero prime ideal of $D [ x ]$ is a maximal ideal, then D is a field.
:::

::: {.solution}
<1>1. Define the evaluation homomorphism
$$
\operatorname{ev}_0:D[x]\to D
$$
by
$$
\operatorname{ev}_0(f)
\coloneqq
f(0).
$$
Then
$$
\ker\operatorname{ev}_0
=(x).
$$

::: {.proof}
The map is a surjective ring homomorphism because every
$$
d\in D
$$
is the image of the constant polynomial $d$.

A polynomial
$$
f(x)
=
a_0+a_1x+\cdots+a_nx^n
$$
lies in the kernel exactly when
$$
a_0=0.
$$
This is equivalent to
$$
f(x)
=
x(a_1+a_2x+\cdots+a_nx^{n-1}),
$$
so
$$
f\in(x).
$$
Thus
$$
\ker\operatorname{ev}_0=(x).
$$
:::

<1>2. Therefore
$$
\boxed{
D[x]/(x)
\cong
D.
}
$$

::: {.proof}
Apply the first isomorphism theorem to the surjective map in step <1>1.
:::

<1>3. The ideal
$$
(x)
$$
is prime in
$$
D[x].
$$

::: {.proof}
By step <1>2,
$$
D[x]/(x)
\cong
D.
$$
The ring $D$ is an integral domain by hypothesis.
Hence the quotient
$$
D[x]/(x)
$$
is an integral domain.
By the prime-ideal quotient criterion,
$$
(x)
$$
is prime.
:::

<1>4. The ideal
$$
(x)
$$
is nonzero.

::: {.proof}
The polynomial
$$
x
$$
is a nonzero element of
$$
D[x]
$$
because
$$
D
$$
is a nonzero integral domain.
Hence
$$
(x)\ne(0).
$$
:::

<1>5. By hypothesis,
$$
(x)
$$
is maximal.

::: {.proof}
Steps <1>3--<1>4 show that
$$
(x)
$$
is a nonzero prime ideal of
$$
D[x].
$$
The hypothesis says every such ideal is maximal.
:::

<1>6. The quotient
$$
D[x]/(x)
$$
is a field.

::: {.proof}
By step <1>5,
$$
(x)
$$
is maximal.
The maximal-ideal quotient criterion therefore gives that
$$
D[x]/(x)
$$
is a field.
:::

<1>7. Therefore
$$
\boxed{
D
\text{ is a field}.
}
$$

::: {.proof}
By step <1>2,
$$
D
\cong
D[x]/(x).
$$
Step <1>6 shows the quotient is a field.
Being a field is preserved under ring isomorphism.
Hence $D$ is a field.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
