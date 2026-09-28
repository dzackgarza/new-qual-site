---
schema: qual/card@1
id: P-BERK85S-11
kind: problem
title: The cubic field $\mathbb Q(\sqrt[3]{2})$ and the inverse of $1-\sqrt[3]{2}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Identified F with Q[x]/(x^3-2) via evaluation at the real cube root of
    2; Eisenstein gives irreducibility and hence both the field property and
    uniqueness of degree-at-most-two representatives.
---

::: {.problem}
Let
\[
F=\{a+b\sqrt[3]{2}+c\sqrt[3]{4}:a,b,c\in\mathbb Q\}.
\]
Prove that $F$ is a field, that every element of $F$ has a unique representation of this form, and find
\[
(1-\sqrt[3]{2})^{-1}
\]
in $F$.
:::

::: {.solution}
Let
$$
\alpha\coloneqq\sqrt[3]{2}.
$$

<1>1. The polynomial
$$
m(x)\coloneqq x^3-2
$$
is irreducible in $\QQ[x]$.

::: {.proof}
Eisenstein's criterion applies with the prime $2$: every nonleading
coefficient is divisible by $2$, while the constant coefficient $-2$ is
not divisible by $4$.
:::

<1>2. Evaluation at $\alpha$ induces an isomorphism
$$
\QQ[x]/(x^3-2)
\cong
F.
$$

::: {.proof}
The evaluation homomorphism
$$
\operatorname{ev}_\alpha:\QQ[x]\to\CC,
\qquad
p(x)\longmapsto p(\alpha),
$$
has kernel $(x^3-2)$ by step <1>1, since $x^3-2$ is the minimal polynomial
of $\alpha$ over $\QQ$. Every polynomial has a unique remainder
$$
a+bx+cx^2
$$
after division by $x^3-2$. Hence the image of evaluation is precisely
$$
\{a+b\alpha+c\alpha^2:a,b,c\in\QQ\}=F.
$$
The first isomorphism theorem gives the stated isomorphism.
:::

<1>3. The set $F$ is a field.

::: {.proof}
By step <1>1, the ideal $(x^3-2)$ is maximal in the PID $\QQ[x]$.
Therefore $\QQ[x]/(x^3-2)$ is a field, and step <1>2 identifies it with
$F$.
:::

<1>4. Every element of $F$ has a unique expression
$$
a+b\sqrt[3]{2}+c\sqrt[3]{4},
\qquad
a,b,c\in\QQ.
$$

::: {.proof}
Existence is the definition of $F$. For uniqueness, suppose
$$
a+b\alpha+c\alpha^2=0.
$$
Then the polynomial $a+bx+cx^2$ lies in the kernel of
$\operatorname{ev}_\alpha$. By step <1>2 this kernel is $(x^3-2)$, but a
nonzero polynomial of degree at most $2$ cannot be divisible by the
degree-$3$ polynomial $x^3-2$. Hence $a=b=c=0$.
:::

<1>5. The requested inverse is
$$
\boxed{
(1-\sqrt[3]{2})^{-1}
=
-1-\sqrt[3]{2}-\sqrt[3]{4}
}.
$$

::: {.proof}
Since $\alpha^3=2$,
$$
\begin{aligned}
(1-\alpha)(-1-\alpha-\alpha^2)
&=
-(1-\alpha)(1+\alpha+\alpha^2)\\
&=
-(1-\alpha^3)\\
&=
1.
\end{aligned}
$$
The displayed inverse belongs to $F$ by step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>3, <1>4, and <1>5 establish respectively the field property,
uniqueness, and the requested inverse.
:::
:::
