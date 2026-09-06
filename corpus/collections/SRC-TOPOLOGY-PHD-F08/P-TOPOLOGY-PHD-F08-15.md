---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-15
kind: problem
title: Associativity of the product of loop homotopy classes
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part Two, question 3 of the Topology Ph.D. Qualifying Exam dated January 17, 2009 in assets/attachments/F08phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Defined multiplication by concatenation, proved it is independent of loop
    representatives by pasting homotopies, and gave an explicit endpoint-fixed
    reparametrization homotopy between the two parenthesizations of a triple
    product.
---

::: {.problem}
Let $X$ be a topological space and let $x_0\in X$.
Define the product of homotopy classes of loops $[\alpha]_{x_0}$ based at $x_0$ and verify in detail that this product is associative.
:::

::: {.solution}
All homotopies of loops below are taken relative to the endpoints.

<1>1. For loops
\[
\alpha,
\beta:I\to X
\]
based at $x_0$, define their concatenation by
\[
(\alpha\mathbin{\cdot}\beta)(s)
=
\begin{cases}
\alpha(2s),&0\le s\le\frac12,\\
\beta(2s-1),&\frac12\le s\le1.
\end{cases}
\]
Then define the product of homotopy classes by
\[
[\alpha]_{x_0}[\beta]_{x_0}
=
[\alpha\mathbin{\cdot}\beta]_{x_0}.
\]
::: {.proof}
Since
\[
\alpha(1)=x_0=\beta(0),
\]
the two formulas for $\alpha\mathbin{\cdot}\beta$ agree at $s=1/2$.
The pasting lemma therefore makes the concatenation continuous.
Moreover,
\[
(\alpha\mathbin{\cdot}\beta)(0)=x_0
\qquad\text{and}\qquad
(\alpha\mathbin{\cdot}\beta)(1)=x_0,
\]
so it is again a loop based at $x_0$.
:::

<1>2. The product in <1>1 is well-defined on homotopy classes.
::: {.proof}
Suppose
\[
\alpha\simeq\alpha'
\qquad\text{and}\qquad
\beta\simeq\beta'
\]
through endpoint-fixed homotopies
\[
H:I\times I\to X,
\qquad
K:I\times I\to X.
\]
Define
\[
L:I\times I\to X
\]
by
\[
L(s,t)
=
\begin{cases}
H(2s,t),&0\le s\le\frac12,\\
K(2s-1,t),&\frac12\le s\le1.
\end{cases}
\]
At $s=1/2$, the first formula is
\[
H(1,t)=x_0
\]
and the second is
\[
K(0,t)=x_0,
\]
so $L$ is continuous by the pasting lemma.
Also
\[
L(-,0)=\alpha\mathbin{\cdot}\beta,
\qquad
L(-,1)=\alpha'\mathbin{\cdot}\beta',
\]
and
\[
L(0,t)=L(1,t)=x_0.
\]
Thus
\[
\alpha\mathbin{\cdot}\beta
\simeq
\alpha'\mathbin{\cdot}\beta',
\]
so the class of the concatenation depends only on $[\alpha]_{x_0}$ and $[\beta]_{x_0}$.
:::

<1>3. For three based loops $\alpha,\beta,\gamma$, define a single traversal
\[
P:[0,3]\to X
\]
by
\[
P(u)
=
\begin{cases}
\alpha(u),&0\le u\le1,\\
\beta(u-1),&1\le u\le2,\\
\gamma(u-2),&2\le u\le3.
\end{cases}
\]
Then $P$ is continuous.
::: {.proof}
At the two joining parameters,
\[
\alpha(1)=\beta(0)=x_0
\]
and
\[
\beta(1)=\gamma(0)=x_0.
\]
Hence the three formulas agree on their overlaps, and the pasting lemma gives continuity.
:::

<1>4. The two parenthesized concatenations are reparametrizations of $P$:
\[
(\alpha\mathbin{\cdot}\beta)\mathbin{\cdot}\gamma
=P\circ r_L,
\]
where
\[
r_L(s)
=
\begin{cases}
4s,&0\le s\le\frac12,\\
2s+1,&\frac12\le s\le1,
\end{cases}
\]
and
\[
\alpha\mathbin{\cdot}(\beta\mathbin{\cdot}\gamma)
=P\circ r_R,
\]
where
\[
r_R(s)
=
\begin{cases}
2s,&0\le s\le\frac12,\\
4s-1,&\frac12\le s\le1.
\end{cases}
\]
::: {.proof}
For the left parenthesization, expanding the definition of concatenation gives
\[
((\alpha\mathbin{\cdot}\beta)\mathbin{\cdot}\gamma)(s)
=
\begin{cases}
\alpha(4s),&0\le s\le\frac14,\\
\beta(4s-1),&\frac14\le s\le\frac12,\\
\gamma(2s-1),&\frac12\le s\le1.
\end{cases}
\]
This is precisely $P(r_L(s))$.

Similarly,
\[
(\alpha\mathbin{\cdot}(\beta\mathbin{\cdot}\gamma))(s)
=
\begin{cases}
\alpha(2s),&0\le s\le\frac12,\\
\beta(4s-2),&\frac12\le s\le\frac34,\\
\gamma(4s-3),&\frac34\le s\le1,
\end{cases}
\]
which is $P(r_R(s))$.
:::

<1>5. The two parenthesizations in <1>4 are homotopic relative to the endpoints.
::: {.proof}
For $t\in I$, set
\[
r_t(s)=(1-t)r_L(s)+t r_R(s).
\]
Both $r_L$ and $r_R$ are continuous and nondecreasing maps from $I$ to $[0,3]$ with
\[
r_L(0)=r_R(0)=0,
\qquad
r_L(1)=r_R(1)=3.
\]
Hence each $r_t$ is continuous, takes values in $[0,3]$, and has the same endpoint values.

Define
\[
F:I\times I\to X,
\qquad
F(s,t)=P(r_t(s)).
\]
This is continuous.
By <1>4,
\[
F(-,0)=(\alpha\mathbin{\cdot}\beta)\mathbin{\cdot}\gamma
\]
and
\[
F(-,1)=\alpha\mathbin{\cdot}(\beta\mathbin{\cdot}\gamma).
\]
Finally,
\[
F(0,t)=P(0)=x_0,
\qquad
F(1,t)=P(3)=x_0,
\]
so the endpoints remain fixed throughout the homotopy.
:::

<1>6. The product of based loop homotopy classes is associative:
\[
\boxed{([\alpha]_{x_0}[\beta]_{x_0})[\gamma]_{x_0}
=[\alpha]_{x_0}([\beta]_{x_0}[\gamma]_{x_0}).}
\]
::: {.proof}
By the definition in <1>1, the left side is represented by
\[
(\alpha\mathbin{\cdot}\beta)\mathbin{\cdot}\gamma
\]
and the right side by
\[
\alpha\mathbin{\cdot}(\beta\mathbin{\cdot}\gamma).
\]
These loops are endpoint-fixed homotopic by <1>5, so they determine the same homotopy class.
:::
:::
