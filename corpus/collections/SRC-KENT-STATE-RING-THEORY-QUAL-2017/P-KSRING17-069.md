---
schema: qual/card@1
id: P-KSRING17-069
kind: problem
title: Fixed rings of ring automorphisms of order 2 and quadratic integrality
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 69 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the arrow in the automorphism and set the statement in LaTeX against problem 69 on Ring_Theory_Qual_Problems.pdf PDF page 11.
---

::: {.problem}
Let $R$ be a commutative ring with identity and $\sigma : R \to R$ a ring automorphism.

(a) Show that $F = \{ r \in R \mid \sigma(r) = r \}$ is a subring of $R$ and the identity of $R$ is in $F$.

(b) Show that if $\sigma^2$ is the identity map on $R$, then each element of $R$ is the root of a monic polynomial of degree two in $F[x]$.
:::

::: {.solution}
Let
$$
F
\coloneqq
\{r\in R:\sigma(r)=r\}.
$$

<1>1. The set $F$ contains $0$.

::: {.proof}
Every ring homomorphism sends $0$ to $0$:
$$
\sigma(0)
=
\sigma(0+0)
=
\sigma(0)+\sigma(0),
$$
so subtraction gives
$$
\sigma(0)=0.
$$
Hence
$$
0\in F.
$$
:::

<1>2. The set $F$ is closed under subtraction.

::: {.proof}
Let
$$
a,b\in F.
$$
Then
$$
\sigma(a)=a,
\qquad
\sigma(b)=b.
$$
Therefore
$$
\sigma(a-b)
=
\sigma(a)-\sigma(b)
=
a-b.
$$
Thus
$$
a-b\in F.
$$
:::

<1>3. The set $F$ is closed under multiplication.

::: {.proof}
Let
$$
a,b\in F.
$$
Then
$$
\sigma(ab)
=
\sigma(a)\sigma(b)
=
ab.
$$
Hence
$$
ab\in F.
$$
:::

<1>4. The identity element $1_R$ belongs to $F$.

::: {.proof}
Because $\sigma$ is surjective, for every
$$
r\in R
$$
there exists
$$
s\in R
$$
with
$$
r=\sigma(s).
$$
Then
$$
\sigma(1_R)r
=
\sigma(1_R)\sigma(s)
=
\sigma(1_Rs)
=
\sigma(s)
=
r.
$$
Similarly,
$$
r\sigma(1_R)=r.
$$
Thus
$$
\sigma(1_R)
$$
is a two-sided identity of $R$.
By uniqueness of the identity,
$$
\sigma(1_R)=1_R.
$$
Hence
$$
1_R\in F.
$$
:::

<1>5. Therefore
$$
\boxed{
F
\text{ is a subring of }R
\text{ containing }1_R.
}
$$

::: {.proof}
Steps <1>1--<1>3 give closure under the ring operations, and step <1>4 gives the identity.
:::

<1>6. Assume now that
$$
\sigma^2
=
\operatorname{id}_R.
$$
For
$$
r\in R,
$$
define
$$
t_r
\coloneqq
r+\sigma(r)
$$
and
$$
n_r
\coloneqq
r\sigma(r).
$$
Then
$$
t_r,n_r\in F.
$$

::: {.proof}
Using
$$
\sigma^2(r)=r,
$$
one has
$$
\begin{aligned}
\sigma(t_r)
&=
\sigma(r)+\sigma^2(r)\\
&=
\sigma(r)+r\\
&=
t_r.
\end{aligned}
$$
Thus
$$
t_r\in F.
$$

Similarly,
$$
\begin{aligned}
\sigma(n_r)
&=
\sigma(r)\sigma^2(r)\\
&=
\sigma(r)r\\
&=
r\sigma(r)\\
&=
n_r,
\end{aligned}
$$
where commutativity of $R$ is used.
Hence
$$
n_r\in F.
$$
:::

<1>7. The polynomial
$$
p_r(X)
\coloneqq
X^2-t_rX+n_r
$$
lies in
$$
F[X]
$$
and is monic of degree $2$.

::: {.proof}
By step <1>6,
$$
t_r,n_r\in F.
$$
Therefore
$$
p_r(X)
=
X^2-t_rX+n_r
$$
has coefficients in $F$.
Its leading coefficient is $1\in F$ and its degree is $2$.
:::

<1>8. The element $r$ is a root of $p_r$.

::: {.proof}
Substitute
$$
X=r:
$$
$$
\begin{aligned}
p_r(r)
&=
r^2-(r+\sigma(r))r+r\sigma(r)\\
&=
r^2-r^2-r\sigma(r)+r\sigma(r)\\
&=
0.
\end{aligned}
$$
Thus
$$
p_r(r)=0.
$$
:::

<1>9. Hence every element of $R$ is the root of a monic quadratic polynomial over $F$.

::: {.proof}
The element
$$
r\in R
$$
was arbitrary.
Steps <1>7--<1>8 produce a monic polynomial
$$
p_r\in F[X]
$$
of degree $2$ with
$$
p_r(r)=0.
$$
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>5 proves part (a), and step <1>9 proves part (b).
:::
:::
