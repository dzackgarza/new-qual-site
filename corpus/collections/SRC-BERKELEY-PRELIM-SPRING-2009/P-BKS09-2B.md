---
schema: qual/card@1
id: P-BKS09-2B
kind: problem
title: $BA-AB=A$ forces $A$ nilpotent in characteristic zero
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with the Spring 2009 solution-packet extraction and independently reviewed its eigenvector-shift induction.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked scalar extension, the characteristic-zero eigenvalue shift, B-invariance of ker A, and the quotient induction.
---

::: {.problem}
Let A and B be $n \times n$ matrices over a field of characteristic zero.
Prove that the condition $B A - A B = A$ implies that A is nilpotent.
(Hint: what does A do to eigenvectors of B?)
:::

::: {.solution}
Let $K$ be the ground field.

<1>1. It suffices to prove the result after extending scalars from $K$ to an
algebraic closure $\overline K$.

::: {.proof}
The relation
$$
BA-AB=A
$$
is unchanged by scalar extension. If the resulting matrix over
$\overline K$ satisfies $A^N=0$, then the same matrix power, whose entries
already lie in $K$, is zero over $K$. Thus nilpotence after scalar extension
implies nilpotence over the original field.
:::

<1>2. Suppose the ground field is algebraically closed. If $v$ is an
eigenvector of $B$ with eigenvalue $\lambda$ and $Av\neq0$, then $Av$ is
an eigenvector of $B$ with eigenvalue $\lambda+1$.

::: {.proof}
The given relation is equivalent to
$$
BA=A(B+I).
$$
Hence
$$
B(Av)
=
A(B+I)v
=
(\lambda+1)Av.
$$
If $Av\neq0$, this says exactly that $Av$ is an eigenvector with the stated
eigenvalue.
:::

<1>3. Under the hypotheses of step <1>2, the kernel of $A$ is nonzero.

::: {.proof}
Because the field is algebraically closed, $B$ has an eigenvector
$v\neq0$, say $Bv=\lambda v$. Repeated application of step <1>2 shows
that, as long as $A^rv\neq0$, the vector $A^rv$ is an eigenvector of $B$
with eigenvalue
$$
\lambda+r.
$$
In characteristic zero the scalars
$$
\lambda,\lambda+1,\lambda+2,\ldots
$$
are all distinct. Since an $n\times n$ matrix has only finitely many
eigenvalues, $A^rv$ must vanish for some $r\geq1$. For the least such $r$,
the vector
$$
w\coloneqq A^{r-1}v
$$
is nonzero and satisfies $Aw=0$. Hence $\ker A\neq0$.
:::

<1>4. The subspace $W\coloneqq\ker A$ is invariant under $B$.

::: {.proof}
Rearranging the relation gives
$$
AB=BA-A.
$$
If $w\in W$, then $Aw=0$, so
$$
A(Bw)
=
B(Aw)-Aw
=
0.
$$
Thus $Bw\in W$.
:::

<1>5. Over an algebraically closed field, $A$ is nilpotent.

::: {.proof}
Proceed by induction on $n$. The assertion is immediate for $n=0$. Assume
$n>0$. By step <1>3, the subspace
$$
W=\ker A
$$
is nonzero, and by step <1>4 it is invariant under both $A$ and $B$.
Therefore $A$ and $B$ induce endomorphisms $\overline A,\overline B$ on
the quotient $V/W$, where $V=\overline K^n$. Passing the relation to the
quotient gives
$$
\overline B\,\overline A
-
\overline A\,\overline B
=
\overline A.
$$
Since $\dim(V/W)<n$, the induction hypothesis gives
$$
\overline A^N=0
$$
for some $N$. Thus
$$
A^N(V)\subseteq W=\ker A,
$$
and consequently
$$
A^{N+1}=0.
$$
So $A$ is nilpotent.
:::

<1>6. The original matrix $A$ over $K$ is nilpotent.

::: {.proof}
Step <1>5 proves nilpotence after extending scalars to $\overline K$.
Step <1>1 then descends the same matrix identity $A^N=0$ to $K$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
