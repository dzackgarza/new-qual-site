---
schema: qual/card@1
id: P-UGAP13F-07
kind: problem
title: Compare images and preimages under set operations
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $f:X\to Y$ be a map of sets, let $A,B\subseteq X$, and let $C,D\subseteq Y$. In each case choose the best relation among $\subseteq$, $\supseteq$, and $=$. No proofs are necessary.

(a)
$$
f(A\cap B)\qquad f(A)\cap f(B).
$$

(b)
$$
f^{-1}(C-D)\qquad f^{-1}(C)-f^{-1}(D).
$$

(c)
$$
f\bigl(f^{-1}(C)\bigr)\qquad C.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For part (a),
$$
\boxed{
f(A\cap B)
\subseteq
f(A)\cap f(B).
}
$$


::: pf-proof

If
$$
y\in f(A\cap B),
$$
then
$$
y=f(x)
$$
for some
$$
x\in A\cap B.
$$
Hence
$$
x\in A
\quad\text{and}\quad
x\in B,
$$
so
$$
y\in f(A)\cap f(B).
$$

The inclusion can be strict.
For example, let
$$
X=\{1,2\},
\qquad
Y=\{0\},
$$
let $f$ be constant, and take
$$
A=\{1\},
\qquad
B=\{2\}.
$$
Then
$$
f(A\cap B)
=
\varnothing,
$$
while
$$
f(A)\cap f(B)
=
\{0\}.
$$

:::

:::

::: {.pf-step #s1-2}

For part (b),
$$
\boxed{
f^{-1}(C-D)
=
f^{-1}(C)-f^{-1}(D).
}
$$


::: pf-proof

For
$$
x\in X,
$$
$$
\begin{aligned}
x\in f^{-1}(C-D)
&\Longleftrightarrow
f(x)\in C
\text{ and }
f(x)\notin D\\
&\Longleftrightarrow
x\in f^{-1}(C)
\text{ and }
x\notin f^{-1}(D)\\
&\Longleftrightarrow
x\in
f^{-1}(C)-f^{-1}(D).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

For part (c),
$$
\boxed{
f\bigl(f^{-1}(C)\bigr)
\subseteq
C.
}
$$


::: pf-proof

More precisely,
$$
f\bigl(f^{-1}(C)\bigr)
=
C\cap f(X).
$$
Indeed,
$$
y\in f(f^{-1}(C))
$$
exactly when
$$
y=f(x)
$$
for some $x\in X$ with
$$
f(x)\in C.
$$
Thus
$$
y\in C\cap f(X).
$$

The inclusion can be strict.
For example, let
$$
X=\{1\},
\qquad
Y=\{0,1\},
\qquad
f(1)=0,
\qquad
C=Y.
$$
Then
$$
f(f^{-1}(C))
=
\{0\}
\subsetneq
\{0,1\}
=
C.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore the best relations are
$$
\boxed{
\begin{array}{c|c}
(a)&\subseteq\\
(b)&=\\
(c)&\subseteq
\end{array}
}
$$


::: pf-proof

Collect steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested choices.

:::

:::

:::
