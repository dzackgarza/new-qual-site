---
schema: qual/card@1
id: E-SMI-8000E-FG3
kind: problem
title: Classification with prescribed kernel dimensions
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Modules over PIDs
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared all four classification requests with the PDF text layer and local 8000e extraction, finitely-generated-modules problem 3; the card already resolves the PDF's abbreviated kernel notation in part (b)."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used dimensions of successive kernels to count cyclic/Jordan blocks and their lengths, then used exponent equal to total order and maximal Jordan-block sizes to force the final two unique classifications."
---

::: {.exercise}
(a) Find all abelian groups of order $2^3 \cdot 3^4$ with $\ker(2) \cong \ZZ/2 \times \ZZ/2$ and $\ker(2^2) \cong \ZZ/2 \times \ZZ/4$, i.e. $\ker(2)$ has dimension 2 over $\ZZ/2$, and $\ker(2^2)/\ker(2)$ has dimension 1 over $\ZZ/2$; and $\ker(3) \cong \ZZ/3 \times \ZZ/3$ and $\ker(3^2) \cong \ZZ/9 \times \ZZ/9$, i.e. $\ker(3)$ has dimension 2 over $\ZZ/3$, and $\ker(3^2)/\ker(3)$ has dimension 2 over $\ZZ/3$.

(b) Find all Jordan matrices $A$ with characteristic polynomial $(t - 2)^3 (t - 3)^4$ and $\ker(A - 2)$ of dimension 2, $\ker(A - 2)^2$ of dimension 3, $\ker(A - 3)$ of dimension 2, and $\ker(A - 3)^2$ of dimension 4 — i.e. $\dim(\ker(A - 2)^2 / \ker(A - 2)) = 1$, and $\dim(\ker(A - 3)^2 / \ker(A - 3)) = 2$.

(c) Find all abelian groups of order $648 = 2^3 \cdot 3^4$ with annihilator 648.

(d) Find all 7 by 7 Jordan matrices over $\QQ$ with minimal polynomial

$$
(t - 2)^3 (t - 3)^4.
$$
:::


::: solution
<1>1. Determine the $2$-primary part in part (a).
::: proof
Let $G_{(2)}$ be the $2$-primary component. Since its order is $2^3$, its
cyclic decomposition corresponds to a partition of $3$.

For a cyclic summand $\mathbb Z/2^e$, the kernel of multiplication by $2$ has
one-dimensional $\mathbb F_2$-dimension, and
$$
\dim_{\mathbb F_2}
\frac{\ker(2^2)}{\ker(2)}
$$
receives one additional dimension exactly when $e\ge2$.

The hypotheses say
$$
\dim_{\mathbb F_2}\ker(2)=2
$$
and
$$
\dim_{\mathbb F_2}\ker(2^2)/\ker(2)=1.
$$
Thus there are exactly two cyclic summands, exactly one of which has exponent
at least $4$. Their exponents must sum to $3$, so the partition is
$$
3=2+1.
$$
Hence
$$
\boxed{G_{(2)}\cong\mathbb Z/4\oplus\mathbb Z/2.}
$$
:::

<1>2. Determine the $3$-primary part in part (a).
::: proof
Let $G_{(3)}$ be the $3$-primary component. Its order is $3^4$. As above,
$$
\dim_{\mathbb F_3}\ker(3)
$$
counts the cyclic summands, while
$$
\dim_{\mathbb F_3}\ker(3^2)/\ker(3)
$$
counts those summands whose exponent is at least $9$.

Both dimensions are $2$. Thus there are exactly two cyclic summands and both
have exponent at least $9$. Since their exponent lengths sum to $4$, the only
partition is
$$
4=2+2.
$$
Therefore
$$
\boxed{G_{(3)}\cong\mathbb Z/9\oplus\mathbb Z/9.}
$$
:::

<1>3. Conclude part (a).
::: proof
Primary decomposition gives the unique group
$$
\boxed{
G\cong
\mathbb Z/4\oplus\mathbb Z/2
\oplus\mathbb Z/9\oplus\mathbb Z/9.}
$$
It has the required order and the kernel conditions are immediate on each
cyclic factor.
:::

<1>4. Determine the Jordan blocks at eigenvalue $2$ in part (b).
::: proof
Put
$$
N_2=A-2I
$$
on the generalized $2$-eigenspace. Its total dimension is $3$, since the
characteristic polynomial contains $(t-2)^3$.

For a nilpotent Jordan block of size $e$, the contribution to
$\dim\ker N_2$ is $1$, and its contribution to
$$
\dim\ker N_2^2-\dim\ker N_2
$$
is $1$ exactly when $e\ge2$.

The hypotheses give
$$
\dim\ker N_2=2,
\qquad
\dim\ker N_2^2-\dim\ker N_2=1.
$$
Thus there are two blocks, exactly one of size at least $2$, with total size
$3$. Their sizes are uniquely
$$
(2,1).
$$
Hence the $2$-primary Jordan part is
$$
J_2(2)\oplus J_1(2).
$$
:::

<1>5. Determine the Jordan blocks at eigenvalue $3$ in part (b).
::: proof
On the generalized $3$-eigenspace, the total dimension is $4$. The hypotheses
say there are two Jordan blocks and
$$
\dim\ker(A-3I)^2-\dim\ker(A-3I)=2,
$$
so both blocks have size at least $2$. Their sizes sum to $4$, hence both have
size $2$. Thus the $3$-primary Jordan part is
$$
J_2(3)\oplus J_2(3).
$$
:::

<1>6. Conclude part (b).
::: proof
The unique Jordan matrix is
$$
\boxed{
J_2(2)\oplus J_1(2)\oplus J_2(3)\oplus J_2(3).}
$$
:::

<1>7. Classify the groups in part (c).
::: proof
For a finite abelian group, the positive generator of its annihilator ideal is
its exponent. Thus the hypothesis says that $G$ has order and exponent both
$$
648=2^3 3^4.
$$

The $2$-primary component has order $2^3$ and exponent $2^3$. In its cyclic
decomposition there must therefore be a cyclic factor of order $8$; that
factor already accounts for the entire order of the $2$-primary component, so
$$
G_{(2)}\cong\mathbb Z/8.
$$
Similarly,
$$
G_{(3)}\cong\mathbb Z/81.
$$
Since $8$ and $81$ are coprime,
$$
\mathbb Z/8\oplus\mathbb Z/81\cong\mathbb Z/648.
$$
Therefore the unique group is
$$
\boxed{G\cong\mathbb Z/648.}
$$
:::

<1>8. Classify the matrices in part (d).
::: proof
The minimal polynomial
$$
(t-2)^3(t-3)^4
$$
requires at least one Jordan block of size $3$ at eigenvalue $2$ and at least
one block of size $4$ at eigenvalue $3$. Those two blocks already use
$$
3+4=7
$$
dimensions, the full size of the matrix. Hence no other blocks can occur.
Thus the unique Jordan matrix is
$$
\boxed{J_3(2)\oplus J_4(3).}
$$
:::
:::
