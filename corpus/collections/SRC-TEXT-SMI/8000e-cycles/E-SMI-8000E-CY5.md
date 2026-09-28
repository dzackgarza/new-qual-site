---
schema: qual/card@1
id: E-SMI-8000E-CY5
kind: problem
title: The sign homomorphism from the Vandermonde polynomial
classification:
  areas:
  - algebra
  topics:
  - Symmetric Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the statement with Smith 8000e cycles problem 5; the printed surjectivity assertion needs n>=2."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Showed transpositions negate the Vandermonde, deduced the sign homomorphism and surjectivity for n>=2, and proved its kernel is exactly the even-transposition subgroup."
---

::: {.exercise}
Assume $n\ge 2$.
Let

$$
f(X) = \prod_{i < j} (X_i - X_j),
$$

and let $S(n)$ act on $\ZZ[X_1, \ldots, X_n]$ by permuting the indices of the variables.
For example, if $n = 3$, $(12)$ sends

$$
f(X) = (X_1 - X_2)(X_1 - X_3)(X_2 - X_3)
$$

to $(X_2 - X_1)(X_2 - X_3)(X_1 - X_3) = -f(X)$.
Deduce that every permutation $m$ takes $f$ to either $f$ or $-f$, and that setting $\operatorname{sgn}(m) = c$, where $m(f) = c \cdot f$, defines a surjective homomorphism $S(n) \to \ts{\pm 1}$ whose kernel consists of those permutations which can be written as a product of an even number of 2-cycles.
Call that subgroup $A(n)$.
:::

::: {.remark}
The printed exercise asserts that the sign map $S_n\to\{\pm1\}$ is
surjective without restricting $n$. For $n=1$, the group $S_1$ is trivial,
so no map from it onto the two-element group can be surjective. The standard
statement therefore requires $n\ge2$, as assumed above.
:::

::: {.solution}
Let
$$
\Delta(X_1,\ldots,X_n)=\prod_{i<j}(X_i-X_j).
$$

<1>1. Every transposition sends $\Delta$ to $-\Delta$.
::: {.proof}
Consider the transposition $\tau=(ab)$, which interchanges the variables
$X_a$ and $X_b$. The factor involving exactly these two indices changes sign:
$$
X_a-X_b\longmapsto X_b-X_a=-(X_a-X_b).
$$
Every other factor is merely permuted with another factor of the product. For
example, if $k$ differs from $a,b$, the two factors involving $a,k$ and
$b,k$ are exchanged, up to the ordering convention $i<j$ already built into
the Vandermonde product. Thus the entire product acquires exactly one minus
sign:
$$
\boxed{\tau(\Delta)=-\Delta.}
$$
:::

<1>2. Every permutation sends $\Delta$ to either $\Delta$ or $-\Delta$.
::: {.proof}
By the preceding generation result, every $m\in S_n$ can be written as a
product of transpositions,
$$
m=\tau_1\tau_2\cdots\tau_r.
$$
Applying step <1>1 repeatedly gives
$$
m(\Delta)=(-1)^r\Delta.
$$
Hence there is a unique scalar
$$
\operatorname{sgn}(m)\in\{\pm1\}
$$
such that
$$
m(\Delta)=\operatorname{sgn}(m)\Delta.
$$
:::

<1>3. The sign function is a homomorphism.
::: {.proof}
For $m,n\in S_n$,
$$
\begin{aligned}
(mn)(\Delta)
&=m(n(\Delta))\\
&=m(\operatorname{sgn}(n)\Delta)\\
&=\operatorname{sgn}(n)\operatorname{sgn}(m)\Delta.
\end{aligned}
$$
Therefore
$$
\boxed{\operatorname{sgn}(mn)
=\operatorname{sgn}(m)\operatorname{sgn}(n).}
$$
:::

<1>4. The homomorphism is surjective for $n\ge2$.
::: {.proof}
The identity maps to $+1$, while the transposition $(12)$ maps to $-1$ by
step <1>1. Hence both elements of $\{\pm1\}$ occur, so
$$
\operatorname{sgn}:S_n\twoheadrightarrow\{\pm1\}
$$
is surjective.
:::

<1>5. Its kernel consists exactly of the permutations expressible as a product of an even number of transpositions.
::: {.proof}
If
$$
m=\tau_1\cdots\tau_r,
$$
then step <1>2 gives
$$
\operatorname{sgn}(m)=(-1)^r.
$$
Thus a product of an even number of transpositions lies in the kernel.
Conversely, if $m$ lies in the kernel, take any transposition decomposition
of $m$. Since
$$
1=\operatorname{sgn}(m)=(-1)^r,
$$
its length $r$ is even. In particular the parity of a transposition
decomposition is independent of the chosen decomposition.

Therefore
$$
\boxed{A_n=\ker(\operatorname{sgn})}
$$
is exactly the subgroup of even permutations.
:::
:::
