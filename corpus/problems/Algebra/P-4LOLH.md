---
schema: qual/card@1
id: P-4LOLH
kind: problem
title: Noetherian rings and $\bigcap I^n$
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Ideals
  - Nakayama's Lemma
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

::: problem
What is a Noetherian ring?
If $I$ is an ideal in a Noetherian ring with a unit, what is the intersection of $I^n$ over all positive integers $n$?
:::

::: solution
A commutative ring $R$ is Noetherian if every ideal is finitely generated; equivalently, every ascending chain of ideals stabilizes.

Let $I\trianglelefteq R$ and set
\[
J=\bigcap_{n\ge1} I^n.
\]
Since $R$ is Noetherian, the ideal $J$ is finitely generated. By Artin--Rees applied to the inclusion $J\subseteq R$, there is $k$ such that
\[
I^n\cap J=I^{\,n-k}(I^k\cap J)\qquad(n\ge k).
\]
Because $J\subseteq I^n$ for every $n$, taking $n=k+1$ gives
\[
J=IJ.
\]
The determinant trick applied to the finitely generated module $J$ now yields some $x\in I$ such that
\[
(1-x)J=0.
\]
Thus every $a\in J$ satisfies $(1-x)a=0$ for some $x\in I$.

Conversely, if $(1-x)a=0$ for some $x\in I$, then $a=xa=x^2a=\cdots=x^na$ for every $n$, so $a\in I^n$ for every $n$. Hence
\[
\bigcap_{n\ge1}I^n
=
\{a\in R:(1-x)a=0\text{ for some }x\in I\}.
\]

In particular, if $I$ is contained in the Jacobson radical (for example, if $(R,\mathfrak m)$ is local and $I\subseteq\mathfrak m$), then $1-x$ is a unit for every $x\in I$, so the intersection is $0$. If $R$ is a domain and $I\ne R$, then $1-x\ne0$ and $(1-x)a=0$ again forces $a=0$, so the intersection is also $0$.
:::
