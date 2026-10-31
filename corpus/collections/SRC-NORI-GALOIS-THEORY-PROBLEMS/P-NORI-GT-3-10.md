---
schema: qual/card@1
id: P-NORI-GT-3-10
kind: problem
title: Quartic extensions containing a quadratic subfield have minimal polynomial $Q^2-cP^2$
classification:
  areas: [algebra]
  topics:
  - Quartic Polynomials
  - Quadratic Subfields
  - Minimal Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.10 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the polynomial type of Problem 3.9, on which this problem depends, from p. 2 of the Nori Galois Theory Problems PDF.
---

::: {.problem}
Problem 3.9 concerns polynomials $f = Q^2 - cP^2$ where $c \in F$ and $P, Q \in F[X]$ with $Q$ monic of degree two and $\deg(P) < 2$, and shows that if such an $f$ is irreducible, then the field $F(\theta)$ obtained by adjoining a root $\theta$ of $f$ contains a quadratic extension of $F$.

Conversely, let $E = F(\theta)$ be a degree four extension of $F$ that contains a quadratic extension of $F$.
Prove that the (monic) minimal polynomial is of the type described in the previous problem.
Here we are assuming that $\operatorname{char} F$ is $\neq 2$.
:::

::: {.solution}

Let
$$
F\subset K\subset E=F(\theta)
$$
with
$$
[K:F]=2,
\qquad
[E:F]=4.
$$

::: pf

::: pf-step

There is an element $c\in F$ that is not a square in $F$ such that
$$
K=F(\sqrt c).
$$


::: pf-proof

Choose $\alpha\in K\setminus F$. Its minimal polynomial over $F$ has degree $2$, say
$$
X^2+sX+t.
$$
Because $\operatorname{char}F\ne2$, set
$$
\beta=\alpha+\frac s2.
$$
Then
$$
\beta^2=\frac{s^2}{4}-t=:c\in F.
$$
Since $\beta\notin F$, the element $c$ is not a square in $F$. Also
$$
F(\beta)=F(\alpha)=K.
$$
Writing $\beta=\sqrt c$ gives the claim.

:::

:::

::: {.pf-step #s1-2}

One has
$$
[E:K]=2,
$$
and $E=K(\theta)$.


::: pf-proof

By the tower law,
$$
[E:F]=[E:K][K:F].
$$
Thus
$$
4=[E:K]\cdot2,
$$
so $[E:K]=2$. Since
$$
F\subset K\subset E
$$
and $E=F(\theta)$,
$$
K(\theta)
$$
contains $F(\theta)=E$ and is contained in $E$, hence equals $E$.

:::

:::

::: pf-step

The minimal polynomial of $\theta$ over $K$ is a monic quadratic
$$
h(X)=X^2+aX+b
$$
with $a,b\in K$.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
[K(\theta):K]=2.
$$
The degree of the minimal polynomial of $\theta$ over $K$ is therefore $2$.

:::

:::

::: {.pf-step #s1-4}

There are unique polynomials $Q,P\in F[X]$ such that
$$
h(X)=Q(X)+\sqrt c\,P(X),
$$
with $Q$ monic of degree $2$ and
$$
\deg P<2.
$$


::: pf-proof

Since
$$
K=F\oplus F\sqrt c
$$
as an $F$-vector space, write
$$
a=a_0+a_1\sqrt c,
\qquad
b=b_0+b_1\sqrt c
$$
with $a_i,b_i\in F$. Then
$$
h(X)
=
\bigl(X^2+a_0X+b_0\bigr)
+
\sqrt c\,(a_1X+b_1).
$$
Set
$$
Q(X)=X^2+a_0X+b_0,
\qquad
P(X)=a_1X+b_1.
$$
Then $Q$ is monic of degree $2$ and $\deg P<2$.

:::

:::

::: {.pf-step #s1-5}

Let $\sigma$ be the nontrivial $F$-automorphism of $K$, characterized by
$$
\sigma(\sqrt c)=-\sqrt c.
$$
Then
$$
\sigma(h)=Q-\sqrt c\,P.
$$


::: pf-proof

The quadratic extension $K/F$ is separable because $\operatorname{char}F\ne2$. Its nontrivial automorphism fixes $F$ and exchanges the two roots of $X^2-c$, hence sends $\sqrt c$ to $-\sqrt c$. Apply it coefficientwise to the expression in step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

The polynomial
$$
g(X)=h(X)\sigma(h)(X)
$$
belongs to $F[X]$ and satisfies
$$
\boxed{g(X)=Q(X)^2-cP(X)^2}.
$$


::: pf-proof

Using steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref},
$$
\begin{aligned}
g
&=(Q+\sqrt c\,P)(Q-\sqrt c\,P)\\
&=Q^2-cP^2.
\end{aligned}
$$
The right-hand side has coefficients in $F$, so $g\in F[X]$.

:::

:::

::: {.pf-step #s1-7}

The polynomial $g$ is monic of degree $4$ and satisfies
$$
g(\theta)=0.
$$


::: pf-proof

Both $h$ and $\sigma(h)$ are monic quadratics, so their product is monic of degree $4$. Since $h(\theta)=0$ by definition of $h$,
$$
g(\theta)=h(\theta)\sigma(h)(\theta)=0.
$$

:::

:::

::: {.pf-step #s1-8}

Let $f\in F[X]$ be the monic minimal polynomial of $\theta$ over $F$. Then
$$
f=g.
$$


::: pf-proof

Because $E=F(\theta)$ has degree $4$ over $F$,
$$
\deg f=4.
$$
By step [](#s1-7){.pf-ref}, $g\in F[X]$ is a monic degree-$4$ polynomial vanishing at $\theta$. Therefore the minimal polynomial $f$ divides $g$. Since both are monic of the same degree, they are equal.

:::

:::

::: {.pf-step #s1-9}

Consequently the minimal polynomial of $\theta$ has the form
$$
\boxed{
f(X)=Q(X)^2-cP(X)^2,
}
$$
where $Q\in F[X]$ is monic of degree $2$ and $\deg P<2$.


::: pf-proof

Combine steps [](#s1-6){.pf-ref} and [](#s1-8){.pf-ref}, together with the degree properties established in step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is exactly the converse statement requested in Problem 3.10.

:::

:::

:::
