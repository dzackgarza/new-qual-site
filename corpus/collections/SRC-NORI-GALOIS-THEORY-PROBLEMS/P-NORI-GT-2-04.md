---
schema: qual/card@1
id: P-NORI-GT-2-04
kind: problem
title: Degree eight polynomial with root $\sqrt{x_1}+\sqrt{x_2}+\sqrt{x_3}$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 2.4 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $x _ { 1 } , x _ { 2 } , x _ { 3 } \in \textit { F }$ Find a monic degree eight $\begin{array} { r l r } { f } & { { } \in } & { F [ X ] } \end{array}$ which has ${ \sqrt { x _ { 1 } } } + { \sqrt { x _ { 2 } } } + { \sqrt { x _ { 3 } } }$ as a root.
:::

::: {.solution}

Put
$$
a=x_1,
\qquad b=x_2,
\qquad c=x_3,
\qquad
\alpha=\sqrt a+\sqrt b+\sqrt c.
$$

::: pf

::: {.pf-step #s1-1}

Consider
$$
P(X)=
\prod_{(\varepsilon_1,\varepsilon_2,\varepsilon_3)\in\{\pm1\}^3}
\left(X-\varepsilon_1\sqrt a-\varepsilon_2\sqrt b-\varepsilon_3\sqrt c\right).
$$
Then $P$ is monic of degree $8$ and $P(\alpha)=0$.


::: pf-proof

There are eight sign triples, so the product is monic of degree eight. The factor corresponding to $(1,1,1)$ is $X-\alpha$, hence $P(\alpha)=0$.

:::

:::

::: {.pf-step #s1-2}

Pairing each signed sum with its negative gives
$$
P(X)=
\prod_{\varepsilon_2,\varepsilon_3\in\{\pm1\}}
\left(X^2-(\sqrt a+\varepsilon_2\sqrt b+\varepsilon_3\sqrt c)^2\right).
$$


::: pf-proof

For each choice of $(\varepsilon_2,\varepsilon_3)$, the two sign triples
$$
(1,\varepsilon_2,\varepsilon_3)
\quad\text{and}\quad
(-1,-\varepsilon_2,-\varepsilon_3)
$$
give roots $r$ and $-r$. Their factors multiply to $(X-r)(X+r)=X^2-r^2$.

:::

:::

::: {.pf-step #s1-3}

Set
$$
S=a+b+c,
\qquad Y=X^2-S.
$$
Then the four factors in step [](#s1-2){.pf-ref} are
$$
Y-2(\varepsilon_2\sqrt{ab}+\varepsilon_3\sqrt{ac}+\varepsilon_2\varepsilon_3\sqrt{bc}).
$$


::: pf-proof

Expanding gives
$$
(\sqrt a+\varepsilon_2\sqrt b+\varepsilon_3\sqrt c)^2
=S+2\varepsilon_2\sqrt{ab}
+2\varepsilon_3\sqrt{ac}
+2\varepsilon_2\varepsilon_3\sqrt{bc}.
$$
Subtract this from $X^2$ and use $Y=X^2-S$.

:::

:::

::: pf-step

Put
$$
u=2\sqrt{ab},
\qquad v=2\sqrt{ac},
\qquad w=2\sqrt{bc}.
$$
Then
$$
P(X)=
(Y-u-v-w)(Y-u+v+w)(Y+u-v+w)(Y+u+v-w).
$$


::: pf-proof

These are exactly the four choices $(\varepsilon_2,\varepsilon_3)=(1,1),(1,-1),(-1,1),(-1,-1)$ in step [](#s1-3){.pf-ref}, reordered.

:::

:::

::: {.pf-step #s1-5}

Multiplying the first two and the last two factors yields
$$
P(X)
=\left((Y-u)^2-(v+w)^2\right)
\left((Y+u)^2-(v-w)^2\right).
$$


::: pf-proof

Use $(A-B)(A+B)=A^2-B^2$ on the first pair with $A=Y-u$, $B=v+w$, and on the second pair with $A=Y+u$, $B=v-w$.

:::

:::

::: {.pf-step #s1-6}

Define
$$
A=Y^2+u^2-v^2-w^2.
$$
Then
$$
P(X)=(A-2Yu-2vw)(A+2Yu+2vw).
$$


::: pf-proof

Expanding the two factors from step [](#s1-5){.pf-ref} gives
$$
(Y-u)^2-(v+w)^2
=A-2Yu-2vw
$$
and
$$
(Y+u)^2-(v-w)^2
=A+2Yu+2vw.
$$

:::

:::

::: {.pf-step #s1-7}

Hence
$$
P(X)=A^2-4(Yu+vw)^2.
$$


::: pf-proof

Apply the difference-of-squares identity to step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Substituting
$$
u^2=4ab,
\quad v^2=4ac,
\quad w^2=4bc,
\quad uvw=8abc,
$$
and simplifying gives
$$
\boxed{
P(X)=
\left(Y^2-4(ab+ac+bc)\right)^2
-64abc\,Y,
\qquad
Y=X^2-(a+b+c).}
$$


::: pf-proof

From step [](#s1-7){.pf-ref},
$$
A^2-4(Yu+vw)^2
=A^2-4Y^2u^2-8Yuvw-4v^2w^2.
$$
Using the displayed substitutions and $A=Y^2+4ab-4ac-4bc$, direct expansion and collection of terms gives
$$
Y^4-8(ab+ac+bc)Y^2-64abcY+16(ab+ac+bc)^2.
$$
This is equivalently
$$
\left(Y^2-4(ab+ac+bc)\right)^2-64abcY,
$$
which is the boxed expression.

:::

:::

::: {.pf-step #s1-9}

Therefore an explicit answer is
$$
\boxed{
f(X)=
\left(
\bigl(X^2-x_1-x_2-x_3\bigr)^2
-4(x_1x_2+x_1x_3+x_2x_3)
\right)^2
-64x_1x_2x_3\bigl(X^2-x_1-x_2-x_3\bigr).}
$$


::: pf-proof

Use the corrected simplification at the end of step [](#s1-8){.pf-ref} and substitute back $a=x_1$, $b=x_2$, $c=x_3$, and $Y=X^2-(a+b+c)$. The polynomial lies in $F[X]$, is monic of degree eight, and equals the product in step [](#s1-1){.pf-ref}, so $f(\alpha)=0$.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} supplies the requested monic degree-eight polynomial over $F$ and step [](#s1-1){.pf-ref} verifies the required root.

:::

:::

:::
