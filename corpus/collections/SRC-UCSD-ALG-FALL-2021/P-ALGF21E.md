---
schema: qual/card@1
id: P-ALGF21E
kind: problem
title: Jordan form of a $7\times 7$ matrix with $A^5 = 2A^4 + A^3$, rank $5$, trace $4$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Suppose that $A$ is a complex $7 \times 7$ matrix such that $A^5 = 2A^4 + A^3$.
Suppose that $\mathrm{rk}\, A = 5$ and $\mathrm{tr}\, A = 4$, where $\mathrm{rk}$ indicates the rank and $\mathrm{tr}$ indicates the trace of a matrix.
Find the Jordan canonical form of $A$.
:::

::: {.solution}
<1>1. $A^5 = 2A^4 + A^3$ means $A^3(A^2 - 2A - I) = 0$, so $A$ satisfies $p(x) = x^3(x^2 - 2x - 1)$.
Proof: rearrange: $A^5 - 2A^4 - A^3 = A^3(A^2 - 2A - I) = 0$.

<1>2. Hence the minimal polynomial divides $x^3(x^2 - 2x - 1)$, so the eigenvalues are $0$ and the roots of $x^2 - 2x - 1 = 0$, namely $1 \pm \sqrt{2}$.
Proof: eigenvalues are roots of the minimal polynomial.

<1>3. $\operatorname{tr} A = 4$ is the sum of the eigenvalues (with multiplicity).
Proof: the trace is the sum of eigenvalues.

<1>4. $\operatorname{rk} A = 5$ means the nullity of $A$ is $7 - 5 = 2$, so the eigenvalue $0$ has geometric multiplicity $2$ (there are $2$ Jordan blocks for eigenvalue $0$).
Proof: rank-nullity.

<1>5. The eigenvalues $1 + \sqrt{2}$ and $1 - \sqrt{2}$ are distinct and irrational, so they each occur with some multiplicity; since the trace is $4$ (rational), the multiplicities of $1 + \sqrt{2}$ and $1 - \sqrt{2}$ must be equal (so their irrational parts cancel).
Proof: the trace is rational, so the sum of the irrational eigenvalues must be rational, forcing equal multiplicities.

<1>6. Let $m$ be the common multiplicity of $1 + \sqrt{2}$ and $1 - \sqrt{2}$. Then the total dimension is $7 = (\text{multiplicity of } 0) + 2m$.
Proof: counting dimensions.

<1>7. The multiplicity of $0$ is at least $2$ (geometric multiplicity $2$), and the trace condition gives: $0 \cdot (\text{mult of } 0) + m(1 + \sqrt{2}) + m(1 - \sqrt{2}) = 2m = 4$, so $m = 2$.
Proof: <1>3 and <1>5.

<1>8. Hence the multiplicity of $0$ is $7 - 2m = 7 - 4 = 3$.
Proof: <1>6 and <1>7.

<1>9. The eigenvalue $0$ has algebraic multiplicity $3$ and geometric multiplicity $2$, so its Jordan blocks are of sizes $2$ and $1$ (one block of size $2$ and one of size $1$).
Proof: <1>4 and <1>8.

<1>10. The eigenvalues $1 + \sqrt{2}$ and $1 - \sqrt{2}$ each have multiplicity $2$; since the minimal polynomial has $x^2 - 2x - 1$ (not $(x^2 - 2x - 1)^2$) as a factor, each has Jordan blocks of size $1$ (two blocks of size $1$ each).
Proof: <1>2 and <1>7 (the minimal polynomial divides $x^3(x^2 - 2x - 1)$, so the blocks for $1 \pm \sqrt{2}$ have size $1$).

<1>11. Hence the Jordan form has: one $2 \times 2$ block for $0$, one $1 \times 1$ block for $0$, two $1 \times 1$ blocks for $1 + \sqrt{2}$, and two $1 \times 1$ blocks for $1 - \sqrt{2}$.
Proof: <1>9 and <1>10.

<1>12. Q.E.D.
Proof: <1>11.
:::
