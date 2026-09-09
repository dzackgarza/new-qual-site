---
schema: qual/card@1
id: P-9PL8R
kind: problem
title: $R/(k)\cong sA$ and $R/(s)\cong A[s]$ when $A=Ra$ is cyclic with annihilator
  $(r)$ and $r=sk$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Cyclic Groups
  - Isomorphism Theorems
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

::: problem
Let $R$ be a commutative domain, let $A=Ra$ be a cyclic $R$-module, and suppose
\[
\operatorname{Ann}_R(a)=(r)
\]
with
\[
r=sk
\]
for nonzero $s,k\in R$.

Prove that
\[
R/(k)\cong sA
\qquad\text{and}\qquad
R/(s)\cong A[s],
\]
where
\[
A[s]=\{x\in A:sx=0\}.
\]
:::


::: {.solution}
<1>1. Define
\[
\phi:R\to sA,
\qquad
x\mapsto sxa.
\]
Then $\phi$ is a surjective $R$-module homomorphism.
::: {.proof}
For $t,x,y\in R$,
\[
\phi(tx)=s(tx)a=t(sxa)=t\phi(x)
\]
and
\[
\phi(x+y)=s(x+y)a=sxa+sya=\phi(x)+\phi(y).
\]
Every element of $sA$ has the form $s(ya)=sya=\phi(y)$, so $\phi$ is surjective.
:::

<1>2. One has
\[
\ker\phi=(k).
\]
::: {.proof}
Certainly $k\in\ker\phi$, because
\[
\phi(k)=ska=ra=0.
\]
Thus $(k)\subseteq\ker\phi$.

Conversely, let $x\in\ker\phi$. Then
\[
sxa=0,
\]
so $sx\in\operatorname{Ann}_R(a)=(r)=(sk)$. Hence for some $t\in R$,
\[
sx=tsk=s(tk).
\]
Since $R$ is a domain and $s\ne0$, cancellation gives
\[
x=tk\in(k).
\]
Thus $\ker\phi=(k)$.
:::

<1>3. Therefore
\[
R/(k)\cong sA.
\]
::: {.proof}
Apply the first isomorphism theorem to the surjective map $\phi$ and use <1>2.
:::

<1>4. Define
\[
\psi:R\to A[s],
\qquad
x\mapsto kxa.
\]
Then $\psi$ is a well-defined surjective $R$-module homomorphism.
::: {.proof}
First,
\[
s\psi(x)=skxa=rxa=x(ra)=0,
\]
so $\psi(x)\in A[s]$. Linearity is immediate from the module laws.

For surjectivity, let $y\in A[s]$. Since $A=Ra$, write $y=ta$. The condition $sy=0$ says
\[
sta=0,
\]
so $st\in\operatorname{Ann}_R(a)=(r)=(sk)$. Thus
\[
st=usk
\]
for some $u\in R$. Since $R$ is a domain and $s\ne0$,
\[
t=uk.
\]
Therefore
\[
y=ta=uka=\psi(u).
\]
:::

<1>5. One has
\[
\ker\psi=(s).
\]
::: {.proof}
Since
\[
\psi(s)=ksa=r a=0,
\]
we get $(s)\subseteq\ker\psi$.

Conversely, if $x\in\ker\psi$, then
\[
kxa=0,
\]
so $kx\in(r)=(sk)$. Hence
\[
kx=usk=k(us)
\]
for some $u\in R$. Since $R$ is a domain and $k\ne0$, cancellation gives
\[
x=us\in(s).
\]
Thus $\ker\psi=(s)$.
:::

<1>6. Therefore
\[
R/(s)\cong A[s].
\]
::: {.proof}
Apply the first isomorphism theorem to $\psi$ and use <1>4 and <1>5.
:::
:::
