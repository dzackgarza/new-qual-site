---
schema: qual/card@1
id: P-BKS08-5A
kind: problem
title: Centralizer of a nilpotent matrix
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the cyclic-vector argument for one Jordan block and
    the commuting block-projection obstruction when the nullspace has dimension
    greater than one.
---

::: {.problem}
Let $M$ be an $n\times n$ nilpotent matrix over $\mathbb C$. Let
$$
C(M)=\{A\in M_n(\mathbb C):AM=MA\}.
$$
Show that
$$
C(M)=\mathbb C[M]
$$
if and only if the null space of $M$ has dimension one.
:::

::: {.solution}
Let $V=\CC^n$, and regard $M$ as a nilpotent endomorphism of $V$.

::: pf

::: {.pf-step #jordan-blocks-count}
In the nilpotent Jordan form of $M$, the number of Jordan blocks
is
$$
\dim\ker M.
$$

::: pf-proof
Each nilpotent Jordan block has a one-dimensional kernel, and the
kernel of a block-diagonal matrix is the direct sum of the kernels of
its blocks.
:::

:::

::: {.pf-step #cyclic-basis}
Suppose $\dim\ker M=1$. Then there exists $v\in V$ such that
$$
v,Mv,\ldots,M^{n-1}v
$$
is a basis of $V$.

::: pf-proof
By step [](#jordan-blocks-count){.pf-ref}, the Jordan form of $M$ has exactly one block. Since the
block has size $n$, a vector at the top of its Jordan chain has the
displayed iterates as a basis.
:::

:::

::: {.pf-step #centralizer-subset-poly}
If $\dim\ker M=1$, then every $A\in C(M)$ belongs to
$\CC[M]$.

::: pf-proof
Take $v$ as in step [](#cyclic-basis){.pf-ref}. Write
$$
Av=\sum_{i=0}^{n-1}a_iM^iv
$$
and set
$$
p(t)=\sum_{i=0}^{n-1}a_it^i.
$$
Since $AM=MA$, for every $0\le j<n$,
$$
\begin{aligned}
A(M^jv)
&=M^j(Av)\\
&=\sum_{i=0}^{n-1}a_iM^{i+j}v\\
&=p(M)(M^jv).
\end{aligned}
$$
The vectors $M^jv$ form a basis by step [](#cyclic-basis){.pf-ref}, so $A=p(M)$.
Therefore $A\in\CC[M]$.
:::

:::

::: {.pf-step #equality-forward}
If $\dim\ker M=1$, then
$$
C(M)=\CC[M].
$$

::: pf-proof
Step [](#centralizer-subset-poly){.pf-ref} gives $C(M)\subseteq\CC[M]$. The reverse inclusion always
holds because every polynomial in $M$ commutes with $M$.
:::

:::

::: {.pf-step #multiple-blocks-not-equal}
Suppose instead that $\dim\ker M>1$. Then
$$
C(M)\ne\CC[M].
$$

::: pf-proof
By step [](#jordan-blocks-count){.pf-ref}, the Jordan form of $M$ has at least two blocks. In that
Jordan decomposition, let $P$ be the projection onto one block and
zero on all the others. Since both $P$ and $M$ are block diagonal,
$$
PM=MP,
$$
so $P\in C(M)$.

On the other hand, every polynomial $p(M)$ acts on $\ker M$ as
$$
p(M)|_{\ker M}=p(0)I_{\ker M},
$$
because $M$ vanishes on $\ker M$. The restriction of $P$ to
$\ker M$ is not scalar: it is the identity on the kernel line from
the selected block and zero on the kernel lines from the other blocks.
Thus $P\in C(M)\setminus\CC[M]$.
:::

:::

::: {.pf-step #equivalence}
Therefore
$$
\boxed{
C(M)=\CC[M]
\quad\Longleftrightarrow\quad
\dim\ker M=1.
}
$$

::: pf-proof
The forward implication is the contrapositive of step [](#multiple-blocks-not-equal){.pf-ref}, and the
reverse implication is step [](#equality-forward){.pf-ref}.
:::

:::

::: pf-qed
Step [](#equivalence){.pf-ref} is the desired equivalence.
:::

:::

:::
