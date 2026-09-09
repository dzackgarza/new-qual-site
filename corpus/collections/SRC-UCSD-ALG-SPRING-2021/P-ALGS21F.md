---
schema: qual/card@1
id: P-ALGS21F
kind: problem
title: "Unique similarity class from characteristic polynomial, minimal polynomial, and divisor counts"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
$A$ is a matrix in $M_{12}(\mathbb{C})$.
The characteristic polynomial of $A$ is $(x+2)^3(x-1)^3(x+1)^6$; the minimal polynomial of $A$ is $(x+2)^2(x-1)(x+1)^4$; $A$ has exactly 3 invariant factors; and $A$ has exactly 7 elementary divisors.

Show that there is exactly one similarity class of such matrices, and find an explicit matrix $A$ in this similarity class.
:::


::: {.solution}
<1>1. For eigenvalue \(-2\), the Jordan block sizes are \(2,1\).
::: {.proof}
The characteristic polynomial gives total algebraic multiplicity \(3\) at \(-2\). The exponent \(2\) of \((x+2)\) in the minimal polynomial says the largest Jordan block has size \(2\). The only partition of \(3\) with largest part \(2\) is \(2+1\).
:::

<1>2. For eigenvalue \(1\), the Jordan block sizes are \(1,1,1\).
::: {.proof}
The algebraic multiplicity is \(3\), and the exponent of \((x-1)\) in the minimal polynomial is \(1\). Hence every Jordan block for eigenvalue \(1\) has size \(1\), giving three such blocks.
:::

<1>3. There must be exactly two Jordan blocks for eigenvalue \(-1\), and their sizes are \(4,2\).
::: {.proof}
The total number of elementary divisors is the total number of Jordan blocks. From <1>1 and <1>2 there are already \(2+3=5\) blocks, so the \(-1\)-primary part contributes exactly \(2\) blocks. Their sizes sum to the algebraic multiplicity \(6\), and the exponent \(4\) of \((x+1)\) in the minimal polynomial says the largest block has size \(4\). The only partition of \(6\) into two positive parts with largest part \(4\) is \(4+2\).
:::

<1>4. Therefore the Jordan form is uniquely determined as
\[
J_2(-2)\oplus J_1(-2)\oplus J_1(1)\oplus J_1(1)\oplus J_1(1)
\oplus J_4(-1)\oplus J_2(-1).
\]
::: {.proof}
Combine <1>1--<1>3. Over \(\mathbb C\), a matrix is determined up to similarity by its Jordan block multiset.
:::

<1>5. The corresponding invariant factors are
\[
d_1=x-1,
\]
\[
d_2=(x+2)(x-1)(x+1)^2,
\]
\[
d_3=(x+2)^2(x-1)(x+1)^4.
\]
Thus there are exactly three invariant factors, as required.
::: {.proof}
For each eigenvalue, list the elementary-divisor exponents in nondecreasing order and pad on the left to three entries:
\[
-2:\ (0,1,2),\qquad
1:\ (1,1,1),\qquad
-1:\ (0,2,4).
\]
Multiplying the corresponding powers columnwise gives \(d_1,d_2,d_3\). They satisfy \(d_1\mid d_2\mid d_3\), their product is the characteristic polynomial, and \(d_3\) is the minimal polynomial.
:::

<1>6. An explicit representative is
\[
A=J_2(-2)\oplus[-2]\oplus[1]\oplus[1]\oplus[1]\oplus J_4(-1)\oplus J_2(-1).
\]
::: {.proof}
This block-diagonal matrix has exactly the Jordan blocks determined in <1>4, hence has the required characteristic polynomial, minimal polynomial, seven elementary divisors, and three invariant factors. By uniqueness of Jordan form, every matrix satisfying the stated data is similar to it.
:::
:::
