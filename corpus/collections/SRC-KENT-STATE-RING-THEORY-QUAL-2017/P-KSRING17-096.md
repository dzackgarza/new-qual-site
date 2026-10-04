---
schema: qual/card@1
id: P-KSRING17-096
kind: problem
title: Automorphisms of a domain extend uniquely to its fraction field
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 96 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D be an integral domain and F its field of fractions.
Show that if g is an isomorphism of D onto itself, then there is a unique isomorphism h of F onto F such that $h ( d ) = g ( d )$ for all d in D.
:::

::: {.solution}
For
$$
a,b\in D,
\qquad
b\ne0,
$$
define
$$
\boxed{
h\left(\frac ab\right)
\coloneqq
\frac{g(a)}{g(b)}.
}
$$

<1>1. The definition of $h$ is well-defined.

::: {.proof}
Suppose
$$
\frac ab
=
\frac cd
$$
in
$$
F.
$$
Then
$$
ad=bc.
$$
Applying the ring homomorphism $g$ gives
$$
g(a)g(d)
=
g(b)g(c).
$$
Because $g$ is injective,
$$
b\ne0
\implies
g(b)\ne0,
$$
and similarly
$$
d\ne0
\implies
g(d)\ne0.
$$
Thus
$$
\frac{g(a)}{g(b)}
=
\frac{g(c)}{g(d)}
$$
in the fraction field.
Hence the value of $h$ depends only on the fraction.
:::

<1>2. The map $h$ preserves addition.

::: {.proof}
For
$$
\frac ab,\frac cd\in F,
$$
one has
$$
\begin{aligned}
h\left(
\frac ab+\frac cd
\right)
&=
h\left(
\frac{ad+bc}{bd}
\right)\\
&=
\frac{
g(ad+bc)
}{
g(bd)
}\\
&=
\frac{
g(a)g(d)+g(b)g(c)
}{
g(b)g(d)
}\\
&=
\frac{g(a)}{g(b)}
+
\frac{g(c)}{g(d)}\\
&=
h\left(\frac ab\right)
+
h\left(\frac cd\right).
\end{aligned}
$$
:::

<1>3. The map $h$ preserves multiplication and identity.

::: {.proof}
One has
$$
\begin{aligned}
h\left(
\frac ab\frac cd
\right)
&=
h\left(
\frac{ac}{bd}
\right)\\
&=
\frac{g(ac)}{g(bd)}\\
&=
\frac{g(a)g(c)}{g(b)g(d)}\\
&=
h\left(\frac ab\right)
h\left(\frac cd\right).
\end{aligned}
$$
Also,
$$
h(1)
=
h\left(\frac11\right)
=
\frac{g(1)}{g(1)}
=
1.
$$
Thus $h$ is a unital ring homomorphism.
:::

<1>4. The map $h$ extends $g$.

::: {.proof}
For
$$
d\in D,
$$
view $d$ as
$$
d/1
\in F.
$$
Then
$$
\begin{aligned}
h(d)
&=
h\left(\frac d1\right)\\
&=
\frac{g(d)}{g(1)}\\
&=
g(d).
\end{aligned}
$$
:::

<1>5. Define
$$
k:F\to F
$$
by
$$
k\left(\frac ab\right)
\coloneqq
\frac{g^{-1}(a)}{g^{-1}(b)}.
$$
Then $k$ is a well-defined ring homomorphism.

::: {.proof}
The same argument as in steps <1>1--<1>3 applies to the ring automorphism
$$
g^{-1}:D\to D.
$$
:::

<1>6. The maps $h$ and $k$ are inverse to one another.

::: {.proof}
For
$$
\frac ab\in F,
$$
one has
$$
\begin{aligned}
k\left(
h\left(\frac ab\right)
\right)
&=
k\left(
\frac{g(a)}{g(b)}
\right)\\
&=
\frac{g^{-1}(g(a))}{g^{-1}(g(b))}\\
&=
\frac ab.
\end{aligned}
$$
Similarly,
$$
h\left(
k\left(\frac ab\right)
\right)
=
\frac ab.
$$
Thus
$$
k=h^{-1}.
$$
:::

<1>7. Therefore
$$
\boxed{
h:F\to F
\text{ is an isomorphism}.
}
$$

::: {.proof}
Steps <1>2--<1>3 show that $h$ is a ring homomorphism, and step <1>6 gives a two-sided inverse.
:::

<1>8. The extension $h$ is unique.

::: {.proof}
Let
$$
\widetilde h:F\to F
$$
be any ring isomorphism satisfying
$$
\widetilde h(d)=g(d)
$$
for all
$$
d\in D.
$$
For
$$
a/b\in F
$$
with
$$
b\ne0,
$$
one has
$$
\frac ab
=
a\,b^{-1}.
$$
Therefore
$$
\begin{aligned}
\widetilde h\left(\frac ab\right)
&=
\widetilde h(a)
\widetilde h(b^{-1})\\
&=
g(a)\,
\widetilde h(b)^{-1}\\
&=
g(a)g(b)^{-1}\\
&=
\frac{g(a)}{g(b)}\\
&=
h\left(\frac ab\right).
\end{aligned}
$$
Thus
$$
\widetilde h=h.
$$
:::

<1>9. Consequently there is a unique field automorphism
$$
\boxed{
h:F\overset{\sim}{\longrightarrow}F
}
$$
extending $g$.

::: {.proof}
Existence is step <1>7 together with step <1>4, and uniqueness is step <1>8.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the required conclusion.
:::
:::
