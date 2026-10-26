---
schema: qual/card@1
id: P-KSRING17-023
kind: problem
title: An element with more than one right inverse has infinitely many
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 23 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a ring with identity 1 and $a , b \in R$ such that $a b = 1$ . Denote $X = \{ x \in R \mid a x = 1 \}$ Show the following.

(a) If $x \in X$ , then $b + ( 1 - x a ) \in X$

(b) If $\varphi : X \to X$ is the mapping given by $\varphi ( x ) = b + ( 1 - x a )$ , then $\varphi$ is one-to-one.

(c) If X has more than one element, then X is an infinite set.
:::

Recall
$$
X
\coloneqq
\{x\in R:ax=1\},
$$
and
$$
ab=1.
$$

::: pf

::: pf-step

If
$$
x\in X,
$$
then
$$
b+(1-xa)\in X.
$$


::: pf-proof

Since
$$
x\in X,
$$
one has
$$
ax=1.
$$
Therefore
$$
\begin{aligned}
a\bigl(b+(1-xa)\bigr)
&=
ab+a-axa\\
&=
1+a-(ax)a\\
&=
1+a-a\\
&=
1.
\end{aligned}
$$
Hence
$$
b+(1-xa)\in X.
$$

:::

:::

::: pf-step

The map
$$
\varphi:X\to X,
\qquad
\varphi(x)
\coloneqq
b+(1-xa)
$$
is well-defined.


::: pf-proof

This is exactly step <1>1.

:::

:::

::: pf-step

The map $\varphi$ is injective.


::: pf-proof

Suppose
$$
\varphi(x)=\varphi(y)
$$
for
$$
x,y\in X.
$$
Then
$$
b+(1-xa)
=
b+(1-ya),
$$
so
$$
xa=ya.
$$
Multiply on the right by $b$:
$$
xab
=
yab.
$$
Since
$$
ab=1,
$$
this becomes
$$
x=y.
$$
Thus $\varphi$ is one-to-one.

:::

:::

::: pf-step

Suppose $X$ is finite. Then $\varphi$ is surjective.


::: pf-proof

By step <1>3, $\varphi$ is an injective self-map of the finite set $X$. Every injective self-map of a finite set is surjective.

:::

:::

::: pf-step

Under the hypothesis of step <1>4, there exists
$$
x\in X
$$
such that
$$
\varphi(x)=b.
$$


::: pf-proof

Because
$$
ab=1,
$$
one has
$$
b\in X.
$$
By surjectivity from step <1>4, $b$ has a preimage $x\in X$.

:::

:::

::: pf-step

The element $x$ from step <1>5 is a two-sided inverse of $a$.


::: pf-proof

The equality
$$
\varphi(x)=b
$$
means
$$
b+(1-xa)
=
b.
$$
Therefore
$$
1-xa=0,
$$
so
$$
xa=1.
$$
Since
$$
x\in X,
$$
one also has
$$
ax=1.
$$
Thus $x$ is a two-sided inverse of $a$.

:::

:::

::: pf-step

If $a$ has a two-sided inverse $x$, then $X=\{x\}$.


::: pf-proof

Let
$$
y\in X.
$$
Then
$$
ay=1.
$$
Using
$$
xa=1,
$$
one gets
$$
y
=
1y
=
(xa)y
=
x(ay)
=
x.
$$
Hence every element of $X$ equals $x$.

:::

:::

::: pf-step

If $X$ has more than one element, then $X$ is infinite.


::: pf-proof

Suppose $X$ had more than one element but were finite. Steps <1>4--<1>6 would produce a two-sided inverse $x$ of $a$, and step <1>7 would then imply
$$
X=\{x\},
$$
contradicting the assumption that $X$ has more than one element.

Therefore
$$
\boxed{
\abs X>1
\implies
X\text{ is infinite}.
}
$$

:::

:::

::: pf-qed

Step <1>1 proves part (a), step <1>3 proves part (b), and step <1>8 proves part (c).

:::

:::
