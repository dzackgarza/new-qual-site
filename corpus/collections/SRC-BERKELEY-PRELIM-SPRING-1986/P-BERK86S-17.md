---
schema: qual/card@1
id: P-BERK86S-17
kind: problem
title: Finite-dimensional differentiation-invariant function spaces are translation-invariant
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
    Represented differentiation by a constant matrix M in a basis of V.
    The row of basis functions satisfies F'=FM, so F(x+a)=F(x)e^{aM};
    every translated function is therefore another linear combination of
    the same basis.
---

::: {.problem}
Let $V$ be a finite-dimensional complex vector space of $C^\infty$ functions on $\mathbb R$. Suppose $V$ is closed under differentiation. Prove that $V$ is closed under translations: if $f\in V$ and $a\in\mathbb R$, then
\[
x\longmapsto f(x+a)
\]
also lies in $V$.
:::

::: {.solution}
If $V=\{0\}$, the conclusion is immediate. Assume henceforth that
$$
\dim_{\CC}V=d\geq1,
$$
and choose a basis $f_1,\ldots,f_d$ of $V$.

::: pf

::: {.pf-step #differentiation-matrix}
There is a matrix $M=(M_{ij})\in M_d(\CC)$ such that
$$
f_j'
=
\sum_{i=1}^d M_{ij}f_i
$$
for every $1\leq j\leq d$.

::: pf-proof
By hypothesis, differentiation maps $V$ into itself. Therefore each
$f_j'$ is a unique linear combination of the chosen basis. Put its
coefficients in the $j$th column of $M$.
:::

:::

::: {.pf-step #f-prime-equation}
For the row vector
$$
F(x)\coloneqq
\begin{pmatrix}
f_1(x)&\cdots&f_d(x)
\end{pmatrix},
$$
one has
$$
F'(x)=F(x)M.
$$

::: pf-proof
The $j$th component of $F'(x)$ is $f_j'(x)$. By step [](#differentiation-matrix){.pf-ref},
$$
f_j'(x)
=
\sum_{i=1}^d f_i(x)M_{ij},
$$
which is exactly the $j$th component of the row vector $F(x)M$.
:::

:::

::: {.pf-step #f-exponential-formula}
For every $x\in\RR$,
$$
F(x)=F(0)e^{xM}.
$$

::: pf-proof
Consider
$$
G(x)\coloneqq F(x)e^{-xM}.
$$
Since
$$
\frac{d}{dx}e^{-xM}
=
-Me^{-xM},
$$
step [](#f-prime-equation){.pf-ref} gives
$$
\begin{aligned}
G'(x)
&=
F'(x)e^{-xM}
+F(x)\frac{d}{dx}e^{-xM}\\
&=
F(x)Me^{-xM}
-F(x)Me^{-xM}\\
&=0.
\end{aligned}
$$
Thus $G$ is constant, so
$$
F(x)e^{-xM}=F(0).
$$
Right multiplication by $e^{xM}$ yields the claim.
:::

:::

::: {.pf-step #translation-formula}
For every $a,x\in\RR$,
$$
F(x+a)=F(x)e^{aM}.
$$

::: pf-proof
By step [](#f-exponential-formula){.pf-ref},
$$
\begin{aligned}
F(x+a)
&=
F(0)e^{(x+a)M}\\
&=
F(0)e^{xM}e^{aM}\\
&=
F(x)e^{aM}.
\end{aligned}
$$
The middle equality holds because both matrix exponentials are functions
of the same matrix $M$.
:::

:::

::: {.pf-step #translate-in-v}
If
$$
f=\sum_{j=1}^d c_jf_j\in V,
$$
then for every $a\in\RR$ the translate
$$
x\longmapsto f(x+a)
$$
also belongs to $V$.

::: pf-proof
Let
$$
c=
\begin{pmatrix}
c_1\\
\vdots\\
c_d
\end{pmatrix}.
$$
Then
$$
f(x)=F(x)c.
$$
By step [](#translation-formula){.pf-ref},
$$
f(x+a)
=
F(x+a)c
=
F(x)e^{aM}c.
$$
The column vector $e^{aM}c$ is independent of $x$, so the last expression
is a fixed complex linear combination of $f_1(x),\ldots,f_d(x)$. Hence
the translated function lies in $V$.
:::

:::

::: {.pf-step #closed-under-translation-boxed}
Therefore
$$
\boxed{V\text{ is closed under every real translation}}.
$$

::: pf-proof
Step [](#translate-in-v){.pf-ref} applies to every $f\in V$ and every $a\in\RR$; the zero-space
case was settled before step [](#differentiation-matrix){.pf-ref}.
:::

:::

::: pf-qed
Step [](#closed-under-translation-boxed){.pf-ref} is the required conclusion.
:::

:::
:::
