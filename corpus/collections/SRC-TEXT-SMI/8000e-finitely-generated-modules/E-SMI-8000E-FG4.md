---
schema: qual/card@1
id: E-SMI-8000E-FG4
kind: problem
title: k[X]-module structures on a three-dimensional vector space over Z/2
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
  note: "Compared the F_2[X]-module classification request with the PDF text layer and local 8000e extraction, finitely-generated-modules problem 4."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Enumerated elementary-divisor decompositions of total F_2-dimension three using the two linear irreducibles, unique quadratic irreducible, and two cubic irreducibles, obtaining fourteen classes."
---

::: {.exercise}
If $k = \ZZ/2\ZZ$, find all $k[X]$ module structures on $k^3$ up to isomorphism (which extend the natural $k$ module structure).
:::


::: solution
Write
$$
k=\mathbb F_2.
$$
A $k[X]$-module structure on the underlying vector space $k^3$ is equivalent
to choosing a $k$-linear operator
$$
T:k^3\to k^3,
$$
with $X$ acting as $T$. Two such module structures are isomorphic exactly when
the corresponding operators are similar.

By Cayley--Hamilton, every such module is a finitely generated torsion
$k[X]$-module. Since $k[X]$ is a PID, the elementary-divisor classification
applies.

<1>1. List the irreducible polynomials that can occur.
::: proof
Only irreducibles of degree at most $3$ can contribute to a module of
$k$-dimension $3$.

The monic linear irreducibles are
$$
p_0=X,
\qquad
p_1=X+1.
$$
There is one monic irreducible quadratic,
$$
q=X^2+X+1,
$$
and two monic irreducible cubics,
$$
r_1=X^3+X+1,
\qquad
r_2=X^3+X^2+1.
$$
These cubics have no roots in $\mathbb F_2$, so they are irreducible; every
reducible cubic over a field has a linear factor, and the standard count of
monic irreducible cubics over $\mathbb F_2$ gives exactly two.
:::

<1>2. List the six classes supported at a single linear irreducible.
::: proof
For either $p\in\{p_0,p_1\}$, a $p$-primary module of dimension $3$ is indexed
by a partition of $3$. The three possibilities are
$$
\boxed{
k[X]/(p^3),
\qquad
k[X]/(p^2)\oplus k[X]/(p),
\qquad
(k[X]/(p))^3.}
$$
There are three for $p_0$ and three for $p_1$, giving six classes.
:::

<1>3. List the four classes involving both linear irreducibles.
::: proof
One of $p_0,p_1$ contributes dimension $2$ and the other contributes dimension
$1$. For the dimension-$2$ primary part there are two partitions, $(2)$ and
$(1,1)$. Hence, for each ordered pair $(p,p')$ equal to
$$
(p_0,p_1)\quad\text{or}\quad(p_1,p_0),
$$
we obtain
$$
\boxed{
k[X]/(p^2)\oplus k[X]/(p'),
\qquad
(k[X]/(p))^2\oplus k[X]/(p').}
$$
This gives four further classes.
:::

<1>4. List the two classes containing the irreducible quadratic.
::: proof
The module
$$
k[X]/(q)
$$
has $k$-dimension $2$. The remaining one dimension must be supplied by one
of the two linear irreducibles. Thus the two possibilities are
$$
\boxed{
k[X]/(q)\oplus k[X]/(p_0),
\qquad
k[X]/(q)\oplus k[X]/(p_1).}
$$
:::

<1>5. List the two classes arising from an irreducible cubic.
::: proof
Each quotient by an irreducible cubic already has dimension $3$, so the two
possibilities are simply
$$
\boxed{
k[X]/(r_1),
\qquad
k[X]/(r_2).}
$$
:::

<1>6. Prove the list is complete and nonredundant.
::: proof
The structure theorem decomposes every finite torsion $k[X]$-module uniquely
into primary cyclic summands
$$
k[X]/(p^e).
$$
The $k$-dimension of such a summand is
$$
e\deg p.
$$
The cases in steps <1>2--<1>5 exhaust every way to write total weighted degree
$3$:

- $3$ at one linear prime;
- $2+1$ at the two distinct linear primes;
- $2+1$ from the irreducible quadratic and a linear prime;
- $3$ from an irreducible cubic.

Uniqueness of the elementary divisors shows that no two modules on the list
are isomorphic. Therefore there are exactly
$$
\boxed{6+4+2+2=14}
$$
isomorphism classes of $k[X]$-module structures on $k^3$.
:::
:::
