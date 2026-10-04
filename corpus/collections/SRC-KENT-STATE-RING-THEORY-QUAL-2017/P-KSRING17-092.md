---
schema: qual/card@1
id: P-KSRING17-092
kind: problem
title: Irreducible elements of a UFD are not squares in the fraction field
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 92 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D be a unique factorization domain and F its field of fractions.
Prove that if d is an irreducible element in D, then there is no $x \in F$ such that $x ^ { 2 } = d .$
:::

::: {.solution}
Suppose, for contradiction, that there exists
$$
x\in F
$$
such that
$$
x^2=d.
$$

<1>1. Write
$$
x=\frac ab
$$
with
$$
a,b\in D,
\qquad
b\ne0,
$$
and with $a$ and $b$ having no common irreducible factor.

::: {.proof}
Every element of the fraction field has a representation
$$
a/b.
$$
Because $D$ is a UFD, common irreducible factors of numerator and denominator can be cancelled finitely many times.
Thus one may choose a representation in lowest terms.
:::

<1>2. The equation
$$
x^2=d
$$
implies
$$
a^2=db^2.
$$

::: {.proof}
Substitute
$$
x=a/b
$$
and multiply the equality
$$
\frac{a^2}{b^2}=d
$$
by
$$
b^2.
$$
:::

<1>3. Since $d$ is irreducible in a UFD, $d$ is prime.

::: {.proof}
In a unique factorization domain, every irreducible element is prime.
:::

<1>4. The relation
$$
a^2=db^2
$$
implies
$$
d\mid a.
$$

::: {.proof}
Step <1>2 gives
$$
d\mid a^2.
$$
By step <1>3, $d$ is prime.
Since
$$
a^2=a\cdot a,
$$
primality implies
$$
d\mid a.
$$
:::

<1>5. Write
$$
a=dc
$$
for some
$$
c\in D.
$$
Then
$$
b^2=dc^2.
$$

::: {.proof}
Substitute
$$
a=dc
$$
into step <1>2:
$$
d^2c^2
=
db^2.
$$
The element
$$
d
$$
is nonzero because it is irreducible in the domain $D$.
Cancelling one factor of $d$ gives
$$
dc^2=b^2.
$$
:::

<1>6. The relation in step <1>5 implies
$$
d\mid b.
$$

::: {.proof}
Step <1>5 gives
$$
d\mid b^2.
$$
By step <1>3, $d$ is prime.
Thus
$$
d\mid b.
$$
:::

<1>7. This contradicts the choice of $a/b$ in lowest terms.

::: {.proof}
Steps <1>4 and <1>6 show that the irreducible element
$$
d
$$
divides both
$$
a
$$
and
$$
b.
$$
This is a common irreducible factor of numerator and denominator, contradicting step <1>1.
:::

<1>8. Therefore no such $x\in F$ exists:
$$
\boxed{
x^2\ne d
\text{ for every }x\in F.
}
$$

::: {.proof}
The assumption that such an $x$ exists leads to the contradiction in step <1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required conclusion.
:::
:::
