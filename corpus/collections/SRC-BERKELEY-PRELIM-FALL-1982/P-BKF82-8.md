---
schema: qual/card@1
id: P-BKF82-8
kind: problem
title: Normal subgroups of a triangular matrix group
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used the surjective homomorphism g(a,b)↦log a with kernel N, then pulled back the subgroup Z<R to obtain a proper intermediate normal subgroup."
---

::: {.problem}
Let
\[
G=\left\{\begin{pmatrix}a&b\\0&a^{-1}\end{pmatrix}:a,b\in\mathbb R,\ a>0\right\},\qquad
N=\left\{\begin{pmatrix}1&b\\0&1\end{pmatrix}:b\in\mathbb R\right\}.
\]

(a) Show that $N\triangleleft G$ and prove $G/N\cong\mathbb R$.

(b) Find a normal subgroup $N'$ with $N\subsetneq N'\subsetneq G$, or prove none exists.
:::

::: {.solution}
For $a>0$ and $b\in\mathbb R$, write
$$
g(a,b)=\begin{pmatrix}a&b\\0&a^{-1}\end{pmatrix}.
$$

<1>1. Construct a quotient map onto the additive group $\mathbb R$.
::: {.proof}
Define
$$
\Phi:G\longrightarrow(\mathbb R,+),
\qquad
\Phi(g(a,b))=\log a.
$$
If $g(a,b),g(c,d)\in G$, the upper-left entry of their product is $ac$.
Therefore
$$
\Phi(g(a,b)g(c,d))
=\log(ac)
=\log a+\log c,
$$
so $\Phi$ is a homomorphism. It is surjective because for every
$t\in\mathbb R$,
$$
\Phi(g(e^t,0))=t.
$$
:::

<1>2. Identify the kernel and prove part (a).
::: {.proof}
We have
$$
\Phi(g(a,b))=0
\iff a=1.
$$
Hence
$$
\ker\Phi
=\left\{\begin{pmatrix}1&b\\0&1\end{pmatrix}:b\in\mathbb R\right\}
=N.
$$
Thus $N\trianglelefteq G$. By the first isomorphism theorem,
$$
\boxed{G/N\cong(\mathbb R,+).}
$$
:::

<1>3. Pull back a proper nontrivial subgroup of the quotient.
::: {.proof}
Take the subgroup $\mathbb Z<\mathbb R$. Since $\mathbb R$ is abelian,
$\mathbb Z$ is normal. Put
$$
N'=\Phi^{-1}(\mathbb Z)
=\left\{g(a,b):\log a\in\mathbb Z\right\}.
$$
As the inverse image of a normal subgroup, $N'\trianglelefteq G$.

Because $0\in\mathbb Z$, we have $N=\ker\Phi\subseteq N'$. The containment
is strict since
$$
g(e,0)\in N'\setminus N.
$$
It is also proper in $G$, since for example
$$
g(e^{1/2},0)\notin N'.
$$
Therefore
$$
\boxed{N\subsetneq N'\subsetneq G,
\qquad N'\trianglelefteq G.}
$$
:::
:::
