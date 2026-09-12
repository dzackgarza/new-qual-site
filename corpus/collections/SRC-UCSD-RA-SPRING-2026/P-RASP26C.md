---
schema: qual/card@1
id: P-RASP26C
kind: problem
title: "Open unit ball plus subspace in a Banach space"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 3 of the official UCSD Spring 2026 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $X$ be a Banach space with open unit ball $B = \{x \in X : \|x\| < 1\}$.
Let $u \in X$ and $\mathcal{M} \subsetneq X$ be a proper vector subspace such that $X = \{\lambda u + y : \lambda \in \mathbb{C},\; y \in \mathcal{M}\}$.

(1) Prove that $B + \mathcal{M} = X$ if and only if $\mathcal{M}$ is not closed.

(2) Prove that $B + \mathcal{M}$ is weakly open, regardless of whether or not $\mathcal{M}$ is closed.
:::

::: solution
Because
\[
X=\operatorname{span}\{u\}+\mathcal M
\]
and $\mathcal M\ne X$, the quotient $X/\mathcal M$ is one-dimensional.

<1>1. If $\mathcal M$ is not closed, then $B+\mathcal M=X$.
::: proof
The closure $\overline{\mathcal M}$ is a vector subspace containing $\mathcal M$. Since $\mathcal M$ has algebraic codimension one, there is no vector subspace strictly between $\mathcal M$ and $X$. Because $\mathcal M$ is not closed,
\[
\mathcal M\subsetneq\overline{\mathcal M},
\]
so necessarily
\[
\overline{\mathcal M}=X.
\]
Thus $\mathcal M$ is dense.

Fix $x\in X$. By density, choose $m\in\mathcal M$ such that
\[
\|x-m\|<1.
\]
Then $x-m\in B$, so
\[
x=(x-m)+m\in B+\mathcal M.
\]
Hence
\[
\boxed{B+\mathcal M=X.}
\]
:::

<1>2. If $\mathcal M$ is closed, then $B+\mathcal M\ne X$.
::: proof
Since $u\notin\mathcal M$ and $\mathcal M$ is closed,
\[
d:=\operatorname{dist}(u,\mathcal M)>0.
\]
For every scalar $\lambda$,
\[
\operatorname{dist}(\lambda u,\mathcal M)=|\lambda|d.
\]
Choose $|\lambda|>1/d$. If $\lambda u\in B+\mathcal M$, then
\[
\lambda u=b+m
\]
for some $b\in B$ and $m\in\mathcal M$. Hence
\[
\operatorname{dist}(\lambda u,\mathcal M)
\le\|b\|<1,
\]
contradicting
\[
\operatorname{dist}(\lambda u,\mathcal M)=|\lambda|d>1.
\]
Thus $B+\mathcal M\ne X$.

Combining Steps 1 and 2 proves
\[
\boxed{B+\mathcal M=X\iff\mathcal M\text{ is not closed}.}
\]
:::

<1>3. Prove weak openness when $\mathcal M$ is not closed.
::: proof
In this case Step 1 gives
\[
B+\mathcal M=X,
\]
which is weakly open.
:::

<1>4. Prove weak openness when $\mathcal M$ is closed.
::: proof
Since $\mathcal M$ is a closed codimension-one subspace, there exists a nonzero bounded linear functional
\[
\varphi\in X^*
\]
such that
\[
\ker\varphi=\mathcal M.
\]
The map $\varphi:X\to\mathbb C$ is surjective. By the Open Mapping Theorem,
\[
\varphi(B)
\]
is an open subset of $\mathbb C$.

We claim
\[
B+\mathcal M=\varphi^{-1}(\varphi(B)).
\]
Indeed, if $x=b+m$ with $b\in B$ and $m\in\mathcal M$, then
\[
\varphi(x)=\varphi(b)\in\varphi(B).
\]
Conversely, if $\varphi(x)=\varphi(b)$ for some $b\in B$, then
\[
x-b\in\ker\varphi=\mathcal M,
\]
so $x\in B+\mathcal M$.

The functional $\varphi$ is continuous for the weak topology by definition. Hence the preimage of the open set $\varphi(B)$ is weakly open. Therefore
\[
\boxed{B+\mathcal M\text{ is weakly open}.}
\]
:::
:::
