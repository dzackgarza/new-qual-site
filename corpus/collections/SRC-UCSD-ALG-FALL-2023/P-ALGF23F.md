---
schema: qual/card@1
id: P-ALGF23F
kind: problem
title: "A surjective endomorphism of a finitely generated Q-algebra is an isomorphism"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 6 of the official UCSD Algebra Qualifying Exam, Fall 2023 source; the finite-generation, surjectivity, and kernel-chain hint agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified Noetherianity by Hilbert's basis theorem and injectivity by stabilization of the ascending chain of kernels of iterates of the surjective endomorphism.
---

::: {.problem}
Suppose $A$ is a finitely generated $\mathbb{Q}$-algebra, and $\phi: A \to A$ is a surjective ring homomorphism.

(a) Prove that $A$ is a Noetherian ring.

(b) Prove that $\phi$ is an isomorphism.

Hint: Consider $\{\ker \phi^n\}_{n=1}^{\infty}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The algebra $A$ is a quotient of a polynomial ring over $\mathbb Q$ in finitely many variables.

::: pf-proof

Because $A$ is finitely generated as a $\mathbb Q$-algebra, there exist
\[
a_1,\ldots,a_r\in A
\]
such that
\[
A=\mathbb Q[a_1,\ldots,a_r].
\]
Hence the evaluation map
\[
\mathbb Q[x_1,\ldots,x_r]\longrightarrow A,
\qquad
x_i\longmapsto a_i,
\]
is surjective.
Thus
\[
A\cong\mathbb Q[x_1,\ldots,x_r]/I
\]
for its kernel ideal $I$.

:::

:::

::: {.pf-step #s2}

The ring $A$ is Noetherian.

::: pf-proof

The field $\mathbb Q$ is Noetherian.
By Hilbert's basis theorem,
\[
\mathbb Q[x_1,\ldots,x_r]
\]
is Noetherian.
Every quotient of a Noetherian ring is Noetherian, so step [](#s1){.pf-ref} gives that $A$ is Noetherian.
This proves part (a).

:::

:::

::: {.pf-step #s3}

The ideals
\[
K_n:=\ker(\phi^n)
\qquad(n\ge1)
\]
form an ascending chain.

::: pf-proof

If $x\in K_n$, then
\[
\phi^n(x)=0.
\]
Applying $\phi$ gives
\[
\phi^{n+1}(x)=0,
\]
so $x\in K_{n+1}$.
Hence
\[
K_1\subseteq K_2\subseteq K_3\subseteq\cdots.
\]

:::

:::

::: {.pf-step #s4}

There exists $N\ge1$ such that
\[
K_N=K_{N+1}.
\]

::: pf-proof

By step [](#s2){.pf-ref}, $A$ is Noetherian, so every ascending chain of ideals stabilizes.
Apply this to the chain in step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

The homomorphism $\phi$ is injective.

::: pf-proof

Let
\[
x\in\ker\phi=K_1.
\]
Since $\phi$ is surjective, so is every iterate $\phi^N$.
Choose $y\in A$ with
\[
\phi^N(y)=x.
\]
Then
\[
\phi^{N+1}(y)=\phi(x)=0,
\]
so
\[
y\in K_{N+1}.
\]
By step [](#s4){.pf-ref},
\[
K_{N+1}=K_N,
\]
hence $y\in K_N$ and therefore
\[
x=\phi^N(y)=0.
\]
Thus $\ker\phi=0$.

:::

:::

::: pf-step

The map $\phi:A\to A$ is an isomorphism.

::: pf-proof

It is surjective by hypothesis and injective by step [](#s5){.pf-ref}.
Therefore it is a ring isomorphism.
This proves part (b).

:::

:::

:::

:::
