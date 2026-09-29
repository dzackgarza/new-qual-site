---
schema: qual/card@1
id: P-BKF08-5A
kind: problem
title: Isomorphism of $\mathbb R[x]/(x^2+x-1)$ and $\mathbb R[x]/(x^2+2x-3)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 5A of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the two real factorizations and the evaluation-map proof of the
    quotient-ring isomorphism with a product of two copies of the reals.
---

::: {.problem}
Are the rings
$$
\RR[x]/(x^2+x-1)
\qquad\text{and}\qquad
\RR[x]/(x^2+2x-3)
$$
isomorphic?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Each defining polynomial is a product of two distinct linear factors
over $\RR$.

::: pf-proof

For the first polynomial,
$$
x^2+x-1
=\left(x-\frac{-1+\sqrt5}{2}\right)
 \left(x-\frac{-1-\sqrt5}{2}\right),
$$
and the two roots are distinct. For the second,
$$
x^2+2x-3=(x-1)(x+3),
$$
whose roots $1$ and $-3$ are distinct.

:::

:::

::: {.pf-step #s2}

If $a,b\in\RR$ with $a\ne b$, then
$$
\RR[x]/((x-a)(x-b))\cong\RR\times\RR.
$$

::: pf-proof

Consider the evaluation homomorphism
$$
\varphi\colon\RR[x]\longrightarrow\RR\times\RR,
\qquad
\varphi(p)=(p(a),p(b)).
$$
It is surjective: for any $(u,v)\in\RR\times\RR$, the polynomial
$$
p(x)
=u\frac{x-b}{a-b}
+v\frac{x-a}{b-a}
$$
satisfies $p(a)=u$ and $p(b)=v$.

Moreover, $p\in\ker\varphi$ exactly when $p(a)=p(b)=0$. By the factor
theorem, this is equivalent to both $x-a$ and $x-b$ dividing $p$. Since
these distinct linear polynomials are coprime, their product divides $p$.
Thus
$$
\ker\varphi=((x-a)(x-b)).
$$
The first isomorphism theorem for rings therefore gives the displayed
isomorphism.

:::

:::

::: {.pf-step #s3}

Both rings in the problem are isomorphic to $\RR\times\RR$.

::: pf-proof

Apply step [](#s2){.pf-ref} to the two pairs of distinct real roots exhibited in
step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s4}

Hence
$$
\boxed{
\RR[x]/(x^2+x-1)
\cong
\RR[x]/(x^2+2x-3)
}.
$$

::: pf-proof

By step [](#s3){.pf-ref}, each quotient is isomorphic to the same ring
$\RR\times\RR$; composing one isomorphism with the inverse of the other
gives the asserted isomorphism.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} answers the question affirmatively.

:::

:::

:::
