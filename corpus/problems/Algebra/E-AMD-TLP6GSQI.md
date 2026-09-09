---
schema: qual/card@1
id: E-AMD-TLP6GSQI
kind: problem
title: Finitely generated modules over a Noetherian local ring are flat iff free
classification:
  areas:
  - algebra
  topics:
  - Nakayama's Lemma
  - Free Modules
  - Homological Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Show that a finitely generated module over a Noetherian local ring is flat iff it is free using Nakayama and Tor.
:::


::: {.solution}
Let $(R,\mathfrak m)$ be the Noetherian local ring and let $M$ be finitely generated.

<1>1. If $M$ is free, then $M$ is flat.
::: {.proof}
Every free module is flat, since tensoring with a direct sum of copies of $R$ is a direct sum of copies of the original exact sequence.
:::

<1>2. Suppose $M$ is flat. Choose elements $x_1,\ldots,x_n\in M$ whose residue classes form a basis of the $R/\mathfrak m$-vector space $M/\mathfrak mM$.
::: {.proof}
The vector space $M/\mathfrak mM$ is finite-dimensional because $M$ is finitely generated. Lift a basis to elements $x_1,\ldots,x_n\in M$. By Nakayama's lemma these lifts generate $M$.
:::

<1>3. Let
\[
0\longrightarrow K\longrightarrow R^n\xrightarrow{\varphi}M\longrightarrow0,
\qquad
\varphi(e_i)=x_i.
\]
Then $K$ is finitely generated.
::: {.proof}
The map $\varphi$ is surjective by <1>2. Since $R$ is Noetherian, the finite free module $R^n$ is Noetherian, so its submodule $K$ is finitely generated.
:::

<1>4. One has $K/\mathfrak mK=0$.
::: {.proof}
Put $k=R/\mathfrak m$. Tensor the exact sequence in <1>3 with $k$. The associated Tor sequence contains
\[
\operatorname{Tor}_1^R(M,k)\longrightarrow K\otimes_R k
\longrightarrow k^n\xrightarrow{\overline\varphi}M\otimes_R k\longrightarrow0.
\]
Because $M$ is flat,
\[
\operatorname{Tor}_1^R(M,k)=0.
\]
Moreover, under the identifications
\[
K\otimes_Rk\cong K/\mathfrak mK,
\qquad
M\otimes_Rk\cong M/\mathfrak mM,
\]
the map $\overline\varphi:k^n\to M/\mathfrak mM$ sends the standard basis to the basis $\overline x_1,\ldots,\overline x_n$ chosen in <1>2. Hence $\overline\varphi$ is an isomorphism. Exactness therefore gives
\[
K/\mathfrak mK=0.
\]
:::

<1>5. The kernel $K$ is zero, so $M$ is free.
::: {.proof}
By <1>3, $K$ is finitely generated, and by <1>4, $K=\mathfrak mK$. Nakayama's lemma gives $K=0$. Thus $\varphi:R^n\to M$ is an isomorphism, so $M$ is free.
:::

<1>6. Therefore a finitely generated module over a Noetherian local ring is flat if and only if it is free.
::: {.proof}
Combine <1>1 and <1>5.
:::
:::
