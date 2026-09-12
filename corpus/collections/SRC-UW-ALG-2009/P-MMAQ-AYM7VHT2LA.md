---
schema: qual/card@1
id: P-MMAQ-AYM7VHT2LA
kind: problem
title: Chain conditions force injective or surjective module endomorphisms to be automorphisms
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Fix a ring $R$, an $R$-module $M$, and an $R$-module homomorphism $f:M\rightarrow M$.

- If $M$ satisfies the descending chain condition on submodules, show that if $f$ is injective, then $f$ is surjective.

  > Hint: note that if $f$ is injective, so are $f\circ f$, $f\circ f\circ f$, etc.

- Give an example of a ring $R$, an $R$-module $M$, and an injective $R$-module homomorphism $f:M\rightarrow M$ which is not surjective.

- If $M$ satisfies the ascending chain condition on submodules, show that if $f$ is surjective, then $f$ is injective.

- Give an example of a ring $R$, an $R$-module $M$, and a surjective $R$-module homomorphism $f:M\rightarrow M$ which is not injective.
:::


::: solution
<1>1. Suppose $M$ satisfies the descending chain condition and $f:M\to M$ is injective. Then $f$ is surjective.
::: {.proof}
The images form a descending chain
\[
M\supseteq f(M)\supseteq f^2(M)\supseteq\cdots.
\]
By the descending chain condition, there is some $n$ such that
\[
f^n(M)=f^{n+1}(M).
\]
Let $x\in M$. Then $f^n(x)\in f^n(M)=f^{n+1}(M)$, so there exists $y\in M$ with
\[
f^n(x)=f^{n+1}(y)=f^n(f(y)).
\]
Since $f$ is injective, so is $f^n$, hence $x=f(y)$. Thus every $x\in M$ lies in $f(M)$ and $f$ is surjective.
:::

<1>2. The descending chain condition is necessary: there are injective non-surjective endomorphisms without it.
::: {.proof}
Take $R=\mathbb Z$, $M=\mathbb Z$, and
\[
f(n)=2n.
\]
This is a $\mathbb Z$-module homomorphism and is injective, but it is not surjective because $1\notin f(\mathbb Z)$.
:::

<1>3. Suppose $M$ satisfies the ascending chain condition and $f:M\to M$ is surjective. Then $f$ is injective.
::: {.proof}
The kernels form an ascending chain
\[
\ker f\subseteq\ker f^2\subseteq\ker f^3\subseteq\cdots.
\]
By the ascending chain condition, there exists $n$ such that
\[
\ker f^n=\ker f^{n+1}.
\]
Let $x\in\ker f$. Since $f$ is surjective, so is $f^n$, so choose $y\in M$ with $f^n(y)=x$. Then
\[
f^{n+1}(y)=f(x)=0,
\]
so $y\in\ker f^{n+1}=\ker f^n$. Therefore
\[
x=f^n(y)=0.
\]
Thus $\ker f=0$ and $f$ is injective.
:::

<1>4. The ascending chain condition is necessary: there are surjective non-injective endomorphisms without it.
::: {.proof}
Let $k$ be any field and let
\[
M=\bigoplus_{j\ge1}ke_j.
\]
Define the $k$-linear map
\[
f(e_1)=0,
\qquad
f(e_{j+1})=e_j\quad(j\ge1).
\]
Every basis vector $e_j$ is $f(e_{j+1})$, so $f$ is surjective. But $e_1\ne0$ and $f(e_1)=0$, so $f$ is not injective.
:::
:::
