---
schema: qual/card@1
id: P-AGH3109MIRACLEFLAT
kind: problem
title: Miracle flatness for a Cohen-Macaulay source
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Cohen-Macaulay Schemes
  - Fibre Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.10.9 and its hint in the Hartshorne source context.
    Independently derived the local regular-sequence argument, then checked it
    against Hartshorne II.8.21A and the standard local miracle-flatness proof.
    The solution below proves the needed local flatness from the regular
    sequence via the local Tor criterion rather than citing miracle flatness
    circularly.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $f: X \to Y$ be a morphism of varieties over $k$.
Assume that $Y$ is regular, that $X$ is Cohen-Macaulay, and that every fibre of $f$ has dimension equal to $\dim X - \dim Y$.
Show that $f$ is flat.

Hint: imitate the proof of (10.4), using (II, 8.21A).
:::

::: {.solution}
Put
$$
m=\dim X,
\qquad
n=\dim Y,
\qquad
d=m-n.
$$

::: pf

::: {.pf-step #s1}

It is enough to prove that $f$ is flat at every closed point of $X$.

::: pf-proof

Let $\xi\in X$ be arbitrary. Choose a closed point
$$
x\in\overline{\{\xi\}}.
$$
Then $f(x)$ is closed, while $f(\xi)$ is a generization of $f(x)$.
The point $\xi$ corresponds to a prime of $\OO_{X,x}$, whose contraction
in $\OO_{Y,f(x)}$ is the prime corresponding to $f(\xi)$.

Thus, if
$$
\OO_{Y,f(x)}\longrightarrow\OO_{X,x}
$$
is flat, localizing this map at those two primes gives the flat map
$$
\OO_{Y,f(\xi)}\longrightarrow\OO_{X,\xi}.
$$
Hence flatness at all closed points implies flatness everywhere.

:::

:::

::: {.pf-step #s2}

Fix a closed point $x\in X$, put $y=f(x)$, and write
$$
A=\OO_{Y,y},
\qquad
B=\OO_{X,x}.
$$
Then $A$ is a regular local ring of dimension $n$, while $B$ is a Cohen--Macaulay local ring of dimension $m$.

::: pf-proof

Because $x$ and $y$ are closed points of the varieties $X$ and $Y$,
$$
\dim B=\dim X=m,
\qquad
\dim A=\dim Y=n.
$$
The first ring is Cohen--Macaulay because $X$ is Cohen--Macaulay, and the
second is regular because $Y$ is regular.

Choose a regular system of parameters
$$
t_1,\ldots,t_n
$$
for $A$. Since $A$ is regular, these elements generate its maximal ideal
$\mathfrak m_A$ and form an $A$-regular sequence.

:::

:::

::: {.pf-step #s3}

The local ring of the fibre at $x$ has dimension exactly $d$:
$$
\dim B/\mathfrak m_A B
=
\dim B/(t_1,\ldots,t_n)B
=d.
$$

::: pf-proof

The quotient
$$
B/\mathfrak m_A B
$$
is the local ring $\OO_{X_y,x}$ of the fibre $X_y$ at $x$.
By hypothesis,
$$
\dim X_y=d,
$$
so
$$
\dim B/\mathfrak m_A B\le d.
$$

On the other hand, quotienting a Noetherian local ring by one element can
decrease its dimension by at most one. Applying this successively to
$t_1,\ldots,t_n$ gives
$$
\dim B/(t_1,\ldots,t_n)B
\ge
\dim B-n
=m-n
=d.
$$
The two inequalities give equality.

:::

:::

::: {.pf-step #s4}

The images of $t_1,\ldots,t_n$ in $B$ form a $B$-regular sequence.

::: pf-proof

By step [](#s2){.pf-ref}, $B$ is Cohen--Macaulay of dimension $m$. Step [](#s3){.pf-ref} gives
$$
\dim B/(t_1,\ldots,t_n)B
=m-n.
$$
Hartshorne II.8.21A(c) characterizes regular sequences in a
Cohen--Macaulay local ring by this dimension drop. Therefore
$$
t_1,\ldots,t_n
$$
is a $B$-regular sequence.

:::

:::

::: {.pf-step #s5}

We have
$$
\Tor_1^A\bigl(\kappa(y),B\bigr)=0.
$$

::: pf-proof

Since $t_1,\ldots,t_n$ is an $A$-regular sequence generating
$\mathfrak m_A$, the Koszul complex
$$
K_A(t_1,\ldots,t_n)
$$
is a finite free resolution of
$$
\kappa(y)=A/\mathfrak m_A.
$$
Tensoring this resolution with $B$ gives
$$
K_A(t_1,\ldots,t_n)\tensor_A B
\cong
K_B(t_1,\ldots,t_n).
$$
By step [](#s4){.pf-ref} the same sequence is $B$-regular, so the latter Koszul complex
is exact in every positive degree. Its first homology is therefore zero,
which is precisely the displayed $\Tor_1$ group.

:::

:::

::: {.pf-step #s6}

The local map
$$
A\longrightarrow B
$$
is flat.

::: pf-proof

Modulo the maximal ideal of $A$,
$$
B/\mathfrak m_A B
$$
is a module over the field
$$
A/\mathfrak m_A=\kappa(y),
$$
and hence is flat over that field. Step [](#s5){.pf-ref} gives
$$
\Tor_1^A\bigl(A/\mathfrak m_A,B\bigr)=0.
$$
The [[T-FLATCRIT|local criterion for flatness]] now implies that $B$ is
flat over $A$.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} proves flatness at every closed point $x\in X$. Step [](#s1){.pf-ref}
localizes these flat local maps to every point of $X$. Therefore
$$
\boxed{f:X\to Y\text{ is flat}.}
$$

:::

:::

:::
