---
schema: qual/card@1
id: P-5WHIC
kind: problem
title: Multiplication and annihilator submodules of a cyclic PID module
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Cyclic Groups
  - Torsion
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Restored the omitted hypothesis that $R$ is a PID from an independent assignment explicitly reproducing Hungerford IV.6.3.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $R$ be a PID and let $A$ be a cyclic $R$-module of nonzero order $r\in R$.

1. Show that if $s$ is relatively prime to $r$, then $sA = A$ and $A[s] = 0$.

2. If $s$ divides $r$, so $sk = r$, then $sA \cong R/(k)$ and $A[s] \cong R/(s)$.
:::

::: solution
Choose a generator $a\in A$ with annihilator
\[
\operatorname{Ann}_R(a)=(r).
\]
Thus $A\cong R/(r)$ and $ra=0$.

<1>1. If $(s,r)=1$, then $sA=A$.
::: proof
By Bézout's identity there are $u,v\in R$ such that
\[
us+vr=1.
\]
For any $x\in A$, one has $rx=0$ because $A=Ra$ and $ra=0$. Hence
\[
x=(us+vr)x=s(ux)+v(rx)=s(ux)\in sA.
\]
Thus $A\subseteq sA$, while $sA\subseteq A$ is immediate. Therefore $sA=A$.
:::

<1>2. If $(s,r)=1$, then $A[s]=0$.
::: proof
Let $x\in A[s]$, so $sx=0$. With $u,v$ as in <1>1,
\[
x=(us+vr)x=u(sx)+v(rx)=0.
\]
Thus the only element annihilated by $s$ is $0$.
:::

Now suppose $s\mid r$, say $r=sk$.

<1>3. There is an isomorphism
\[
sA\cong R/(k).
\]
::: proof
Define
\[
\phi:R\longrightarrow sA,
\qquad
t\longmapsto tsa.
\]
Every element of $sA$ has the form $s(xa)=xsa$, so $\phi$ is surjective.
Moreover,
\[
t\in\ker\phi
\iff tsa=0
\iff ts\in(r)=(sk).
\]
Thus $ts=usk$ for some $u\in R$. Since $R$ is a domain and $s\ne0$, cancellation
gives $t=uk$, so $t\in(k)$. Conversely, every $t\in(k)$ plainly lies in the
kernel. Hence $\ker\phi=(k)$, and the first isomorphism theorem gives
\[
sA\cong R/(k).
\]
:::

<1>4. There is an isomorphism
\[
A[s]\cong R/(s).
\]
::: proof
Define
\[
\psi:R\longrightarrow A[s],
\qquad
t\longmapsto tka.
\]
The image lies in $A[s]$ because
\[
s(tka)=t(sk)a=tra=0.
\]

To prove surjectivity, let $x=ta\in A[s]$. Then $sta=0$, so
\[
st\in(r)=(sk).
\]
Hence $st=usk$ for some $u\in R$, and cancellation of the nonzero element $s$
gives $t=uk$. Thus $x=uka=\psi(u)$.

Finally,
\[
t\in\ker\psi
\iff tka=0
\iff tk\in(sk).
\]
Since $k\ne0$, cancellation gives $t\in(s)$. Conversely $(s)\subseteq\ker\psi$.
Therefore $\ker\psi=(s)$, and the first isomorphism theorem yields
\[
A[s]\cong R/(s).
\]
:::
:::
