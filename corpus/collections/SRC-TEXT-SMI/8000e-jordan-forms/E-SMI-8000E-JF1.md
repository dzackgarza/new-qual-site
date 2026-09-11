---
schema: qual/card@1
id: E-SMI-8000E-JF1
kind: problem
title: Enumerating Jordan forms from minimal and invariant factors
classification:
  areas:
  - algebra
  topics:
  - Modules over PIDs
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared all four Jordan-form requests with the PDF text layer and local 8000e extraction, Jordan forms exercise 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Enumerated partitions constrained by largest block sizes in parts (i)--(iii), and converted each invariant-factor exponent into the corresponding elementary divisor/Jordan block in part (iv)."
---

::: {.exercise}
(i) Find all $5 \times 5$ Jordan matrices with $m(t) = (X - 5)^2$.

(ii) Find all $5 \times 5$ Jordan matrices with $m(t) = (X - 1)(X - 3)(X + 6)$.

(iii) Find all $6 \times 6$ Jordan matrices with $m(t) = (X - 1)^2 (X - 2)^2$.

(iv) Find the Jordan form of $T$, if the $k[X]$ module $(M, T)$ has invariant factors $(X-1)(X-2)$, $(X-1)^3(X-2)$, $(X-1)^3(X-2)^2(X-5)^3$.
:::


::: solution
Write $J_r(a)$ for a Jordan block of size $r$ with eigenvalue $a$.

<1>1. Solve part (i).
::: proof
If the minimal polynomial is
$$
(X-5)^2,
$$
then $5$ is the only eigenvalue and the largest Jordan block has size exactly
$2$. Since the matrix is $5\times5$, the Jordan block sizes form a partition
of $5$ into parts at most $2$, with at least one part equal to $2$.

The only possibilities are
$$
5=2+2+1
$$
and
$$
5=2+1+1+1.
$$
Hence the complete list is
$$
\boxed{
J_2(5)\oplus J_2(5)\oplus J_1(5),
\qquad
J_2(5)\oplus J_1(5)^{\oplus3}.}
$$
:::

<1>2. Solve part (ii).
::: proof
The minimal polynomial
$$
(X-1)(X-3)(X+6)
$$
has three distinct linear factors. Therefore every such matrix is
diagonalizable, and each of the eigenvalues
$$
1,\quad3,\quad-6
$$
must occur with positive multiplicity.

If these multiplicities are $a,b,c$, then
$$
a+b+c=5,
\qquad
a,b,c\ge1.
$$
Thus a complete list is
$$
\boxed{
I_a\oplus 3I_b\oplus(-6)I_c,
\qquad
(a,b,c)\in
\{(1,1,3),(1,2,2),(1,3,1),(2,1,2),(2,2,1),(3,1,1)\}.}
$$
There are six Jordan forms.
:::

<1>3. Solve part (iii).
::: proof
The minimal polynomial
$$
(X-1)^2(X-2)^2
$$
requires both eigenvalues $1$ and $2$, and the largest Jordan block for each
eigenvalue must have size exactly $2$.

Let $d_1$ and $d_2$ be the dimensions of the generalized eigenspaces for
$1$ and $2$. Since each must contain a size-$2$ block,
$$
d_1,d_2\ge2,
\qquad
d_1+d_2=6.
$$
Hence
$$
(d_1,d_2)=(2,4),(3,3),(4,2).
$$
For primary dimension $2$ the only allowed partition is $(2)$; for dimension
$3$ it is $(2,1)$; for dimension $4$ the possibilities are $(2,2)$ and
$(2,1,1)$. Consequently the five Jordan forms are
$$
\boxed{
\begin{aligned}
&J_2(1)\oplus J_2(2)\oplus J_2(2),\\
&J_2(1)\oplus J_2(2)\oplus J_1(2)\oplus J_1(2),\\
&J_2(1)\oplus J_1(1)\oplus J_2(2)\oplus J_1(2),\\
&J_2(1)\oplus J_2(1)\oplus J_2(2),\\
&J_2(1)\oplus J_1(1)\oplus J_1(1)\oplus J_2(2).
\end{aligned}}
$$
Each has largest block size $2$ at both eigenvalues, and every allowed
partition pair occurs exactly once.
:::

<1>4. Convert the invariant factors in part (iv) to elementary divisors.
::: proof
The invariant factors are
$$
f_1=(X-1)(X-2),
$$
$$
f_2=(X-1)^3(X-2),
$$
and
$$
f_3=(X-1)^3(X-2)^2(X-5)^3.
$$
For a split polynomial, the powers of each linear prime appearing across the
invariant factors are precisely the sizes of the Jordan blocks for that
eigenvalue.

For $X-1$, the exponents are
$$
1,3,3,
$$
so the blocks at eigenvalue $1$ have sizes
$$
1,3,3.
$$
For $X-2$, the exponents are
$$
1,1,2,
$$
so the blocks at eigenvalue $2$ have sizes
$$
1,1,2.
$$
For $X-5$, only the exponent $3$ occurs, giving one size-$3$ block.
:::

<1>5. State the Jordan form in part (iv).
::: proof
Combining the elementary divisors from step <1>4 gives
$$
\boxed{
J_3(1)\oplus J_3(1)\oplus J_1(1)
\oplus J_2(2)\oplus J_1(2)\oplus J_1(2)
\oplus J_3(5).}
$$
The order of the Jordan blocks is immaterial.
:::
:::
