---
schema: qual/card@1
id: P-KSRING17-102
kind: problem
title: $D$-automorphisms of $D[x]$ are affine substitutions
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 102 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the arrow in the isomorphism and set the statement in LaTeX against problem 102 on Ring_Theory_Qual_Problems.pdf PDF page 13.
---

::: {.problem}
Let $D$ be an integral domain and $D[x]$ the polynomial ring over $D$.
Suppose $\varphi : D[x] \to D[x]$ is an isomorphism such that $\varphi(d) = d$ for all $d \in D$.
Show that $\varphi(x) = ax + b$ for some $a, b \in D$ and that $a$ is a unit of $D$.
:::

::: {.solution}
Set
$$
f(x)
\coloneqq
\varphi(x).
$$
Let
$$
\psi
\coloneqq
\varphi^{-1},
$$
and set
$$
g(x)
\coloneqq
\psi(x).
$$

<1>1. Both $f$ and $g$ are nonconstant polynomials.

::: {.proof}
Suppose
$$
f\in D
$$
were constant.
Because $\varphi$ fixes every element of $D$, every polynomial
$$
h(x)
=
\sum_{i=0}^{n}d_i x^i
$$
would satisfy
$$
\varphi(h)
=
\sum_{i=0}^{n}d_i f^i
\in
D.
$$
Thus the image of $\varphi$ would be contained in $D$ and could not contain the nonconstant polynomial $x$.
This contradicts surjectivity of $\varphi$.

Hence $f$ is nonconstant.
The same argument applied to the inverse automorphism $\psi$ shows that $g$ is nonconstant.
:::

<1>2. For every polynomial
$$
h(x)\in D[x],
$$
one has
$$
\varphi(h(x))
=
h(f(x)).
$$

::: {.proof}
Write
$$
h(x)
=
\sum_{i=0}^{n}d_i x^i
$$
with
$$
d_i\in D.
$$
Because $\varphi$ fixes each coefficient and is a ring homomorphism,
$$
\begin{aligned}
\varphi(h(x))
&=
\sum_{i=0}^{n}
\varphi(d_i)\varphi(x)^i\\
&=
\sum_{i=0}^{n}
d_i f(x)^i\\
&=
h(f(x)).
\end{aligned}
$$
:::

<1>3. Likewise, for every
$$
h(x)\in D[x],
$$
one has
$$
\psi(h(x))
=
h(g(x)).
$$

::: {.proof}
The inverse automorphism $\psi$ also fixes $D$ pointwise.
Apply the argument of step <1>2 with $\psi$ in place of $\varphi$.
:::

<1>4. The inverse relation
$$
\psi\circ\varphi
=
\operatorname{id}_{D[x]}
$$
gives
$$
f(g(x))
=
x.
$$

::: {.proof}
Apply
$$
\psi\circ\varphi
$$
to $x$:
$$
\begin{aligned}
x
&=
\psi(\varphi(x))\\
&=
\psi(f(x))\\
&=
f(g(x)),
\end{aligned}
$$
where the last equality uses step <1>3.
:::

<1>5. For nonconstant polynomials
$$
u,v\in D[x],
$$
one has
$$
\deg(u\circ v)
=
\deg(u)\deg(v).
$$

::: {.proof}
Write
$$
u(x)
=
a_mx^m+\text{ lower terms},
$$
and
$$
v(x)
=
b_nx^n+\text{ lower terms},
$$
with
$$
a_m,b_n\ne0.
$$
Then
$$
u(v(x))
$$
has leading term
$$
a_m
\left(
b_nx^n
\right)^m
=
a_m b_n^m x^{mn}.
$$
Because $D$ is an integral domain,
$$
a_m b_n^m\ne0.
$$
Thus
$$
\deg(u\circ v)=mn.
$$
:::

<1>6. One has
$$
\deg f
=
\deg g
=
1.
$$

::: {.proof}
By step <1>1, both degrees are positive.
By steps <1>4--<1>5,
$$
1
=
\deg x
=
\deg(f\circ g)
=
(\deg f)(\deg g).
$$
The only positive integers with product $1$ are
$$
1
\quad\text{and}\quad
1.
$$
Hence
$$
\deg f=\deg g=1.
$$
:::

<1>7. There exist
$$
a,b,c,d\in D
$$
with
$$
a,c\ne0
$$
such that
$$
f(x)=ax+b
$$
and
$$
g(x)=cx+d.
$$

::: {.proof}
This is exactly the meaning of
$$
\deg f=\deg g=1
$$
from step <1>6.
:::

<1>8. The identity
$$
f(g(x))
=
x
$$
implies
$$
ac=1.
$$

::: {.proof}
Substitute the expressions from step <1>7:
$$
\begin{aligned}
x
&=
f(g(x))\\
&=
a(cx+d)+b\\
&=
ac\,x
+
(ad+b).
\end{aligned}
$$
Equality of polynomials gives equality of coefficients.
Thus the coefficient of $x$ satisfies
$$
ac=1.
$$
:::

<1>9. Therefore $a$ is a unit of $D$.

::: {.proof}
Step <1>8 exhibits
$$
c\in D
$$
with
$$
ac=1.
$$
Since $D$ is commutative,
$$
ca=1
$$
as well.
Hence
$$
\boxed{
a\in D^\times.
}
$$
:::

<1>10. Consequently,
$$
\boxed{
\varphi(x)
=
ax+b
}
$$
for some
$$
a,b\in D
$$
with $a$ a unit.

::: {.proof}
By definition,
$$
\varphi(x)=f(x).
$$
Step <1>7 gives
$$
f(x)=ax+b,
$$
and step <1>9 shows
$$
a\in D^\times.
$$
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 is the required conclusion.
:::
:::
