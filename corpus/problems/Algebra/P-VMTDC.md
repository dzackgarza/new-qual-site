---
schema: qual/card@1
id: P-VMTDC
kind: problem
title: Maschke's theorem
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Semisimplicity
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
State and prove Maschke's theorem.
What can go wrong if you work over the real field?
What can go wrong in characteristic $p$?
:::

::: {.solution}
Maschke's theorem: let $G$ be a finite group and $k$ a field with $\characteristic k\nmid \abs{G}$. Then every finite-dimensional $k$-representation $V$ of $G$ is completely reducible.

::: pf

::: {.pf-step #complement}

Every $G$-stable subspace $W\subseteq V$ has a $G$-stable complement.

::: pf-proof

Choose any linear projection $p_0:V\to W$ and average it over the group:
$$
p=\frac1{\abs{G}}\sum_{g\in G}g\,p_0\,g^{-1}.
$$
The scalar $\abs{G}^{-1}$ exists by hypothesis. For $h\in G$, reindexing the sum gives $h\,p\,h^{-1}=p$, so $p$ is $G$-equivariant. Each $g\,p_0\,g^{-1}$ maps $V$ into $W$ and fixes $W$ pointwise, since $W$ is $G$-stable; hence $p$ has image $W$ and restricts to the identity on $W$. Therefore $V=W\oplus\ker p$, and $\ker p$ is $G$-stable because $p$ is equivariant.

:::

:::

::: pf-step

$V$ is a direct sum of irreducible subrepresentations.

::: pf-proof

Induct on $\dim V$. If $V$ is not irreducible, it has a $G$-stable subspace $0\ne W\ne V$, and step [](#complement){.pf-ref} gives $V=W\oplus W'$ with both summands $G$-stable and of smaller dimension.

:::

:::

::: pf-step

Over $\RR$, Maschke's theorem still holds.

::: pf-proof

$\RR$ has characteristic $0$. What changes from the complex theory is the form of irreducibles and Schur's lemma: for an irreducible real representation, the division algebra $\Endo_G(V)$ can be $\RR$, $\CC$, or $\HH$.

:::

:::

::: pf-step

If $\characteristic k=p$ divides $\abs{G}$, complete reducibility can fail: for $G=C_p=\langle g\rangle$ and $k=\FF_p$, the representation $\rho(g)=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ is not completely reducible.

::: pf-proof

With $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $N^2=0$ gives $(I+N)^p=I+pN=I$ in characteristic $p$, so $\rho$ is a representation of $C_p$. The line spanned by $e_1$ is invariant, but it has no invariant complementary line: the only eigenline of $\rho(g)$ is $\langle e_1\rangle$.

:::

:::

:::

:::
