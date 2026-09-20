---
schema: qual/card@1
id: P-ALGQUAL18W-I2
kind: problem
title: Simple modules over upper-triangular complex matrices
classification: {areas: [algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, Problem 2 in the deterministic MinerU Flash extraction assets/attachments/qual18wintersol_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Independently proved that the nilpotent strictly upper-triangular ideal
    annihilates every simple module, reducing to simple modules over C^n.
    Compared afterward with the recorded source solution, which gives the
    equivalent Jacobson-radical argument.
---

::: {.problem}
Let $U_n(\mathbb C)$ be the ring of upper-triangular $n\times n$ matrices over $\mathbb C$.

True or false?
Justify your answer with a proof or counterexample: every irreducible $U_n(\mathbb C)$-module is one-dimensional over $\mathbb C$.
:::

::: {.solution}
The statement is **true**. Put
$$
R=U_n(\CC)
$$
and let
$$
N\subseteq R
$$
be the ideal of strictly upper-triangular matrices.

<1>1. The ideal $N$ is nilpotent:
$$
N^n=0.
$$

::: {.proof}
Multiplying a matrix supported strictly above the diagonal by another such
matrix moves every possible nonzero entry at least one diagonal farther
above the main diagonal. A product of $r$ strictly upper-triangular matrices
can therefore have nonzero entries only at least $r$ positions above the
main diagonal.

There are only $n-1$ superdiagonals in an $n\times n$ matrix, so every
product of $n$ elements of $N$ is zero. Hence
$$
N^n=0.
$$
:::

<1>2. If $M$ is a nonzero simple left $R$-module, then
$$
NM=0.
$$

::: {.proof}
Because $N$ is a two-sided ideal,
$$
NM
$$
is an $R$-submodule of $M$. Simplicity gives
$$
NM=0
\quad\text{or}\quad
NM=M.
$$

Suppose $NM=M$. Then
$$
N^2M
=
N(NM)
=
NM
=
M.
$$
Inductively,
$$
N^rM=M
$$
for every $r\geq1$. Taking $r=n$ contradicts step <1>1:
$$
M
=
N^nM
=
0.
$$
Since $M$ is nonzero, this is impossible. Therefore
$$
NM=0.
$$
:::

<1>3. Every simple $R$-module is naturally a simple module over
$$
R/N
\cong
\CC^n.
$$

::: {.proof}
Step <1>2 shows that $N$ acts trivially, so the $R$-action factors uniquely
through the quotient ring $R/N$.

The quotient remembers only the diagonal entries:
$$
R/N
\longrightarrow
\CC^n,
\qquad
(a_{ij})
\longmapsto
(a_{11},\ldots,a_{nn}).
$$
This is a ring isomorphism.

An $R/N$-submodule is exactly an $R$-submodule under the factored action, so
the resulting $R/N$-module remains simple.
:::

<1>4. Every simple $\CC^n$-module is one-dimensional over $\CC$.

::: {.proof}
Let
$$
e_i
=
(0,\ldots,0,1,0,\ldots,0)
\in\CC^n
$$
be the standard orthogonal idempotents. They satisfy
$$
1=e_1+\cdots+e_n.
$$
Hence for any nonzero $\CC^n$-module $M$,
$$
M=e_1M+\cdots+e_nM,
$$
so at least one $e_iM$ is nonzero.

Because $\CC^n$ is commutative, each $e_iM$ is a submodule. If $M$ is
simple, a nonzero $e_iM$ must equal $M$. For $j\ne i$,
$$
e_jM
=
e_je_iM
=
0.
$$
Thus the action of $\CC^n$ on $M$ factors through the $i$th coordinate
projection
$$
\CC^n\longrightarrow\CC.
$$

Choose
$$
0\ne m\in M.
$$
Then
$$
\CC m
$$
is a nonzero $\CC^n$-submodule of $M$, so simplicity gives
$$
M=\CC m.
$$
Therefore
$$
\dim_\CC M=1.
$$
:::

<1>5. Every irreducible $U_n(\CC)$-module is one-dimensional over $\CC$.

::: {.proof}
Let $M$ be an irreducible, equivalently simple, $U_n(\CC)$-module. Step
<1>3 reduces $M$ to a simple $\CC^n$-module, and step <1>4 proves that such
a module has complex dimension one. Hence
$$
\boxed{\dim_\CC M=1.}
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves that the statement in the problem is true.
:::
:::
