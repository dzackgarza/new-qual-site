---
schema: qual/card@1
id: P-UCLAB04F-10
kind: problem
title: Stabilization and disjointness of generalized eigenspaces
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 10 of the official UCLA Basic Exam Fall 2004 PDF; the source sets $V=\mathbb R^n$ while allowing $\lambda\in\mathbb C$, so the displayed generalized eigenspace is not defined for nonreal $\lambda$ without complexification.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Records the source defect and proves both requested assertions after the standard correction $V=\mathbb C^n$ (equivalently, after complexifying the real operator).
---

::: {.problem}
The source sets $V=\mathbb R^n$, lets $T:V\to V$ be linear, and for $\lambda\in\mathbb C$ defines
\[
V(\lambda)=\{v\in V:(T-\lambda I)^Nv=0\text{ for some }N\geq1\}.
\]

(a) Prove that there is a fixed integer $M$ such that
\[
V(\lambda)=\ker((T-\lambda I)^M).
\]

(b) Prove that if $\lambda\ne\mu$, then
\[
V(\lambda)\cap V(\mu)=\{0\}.
\]

Hint: raise both sides of
\[
\frac{T-\lambda I}{\mu-\lambda}
+
\frac{T-\mu I}{\lambda-\mu}
=I
\]
to a sufficiently high power.
:::

::: {.solution}
As printed, the definition is not meaningful for nonreal $\lambda$: if $V=\mathbb R^n$, then $T-\lambda I$ is not an endomorphism of $V$.
Replace $V$ by $\mathbb C^n$, or equivalently complexify $T$.

Fix $\lambda\in\mathbb C$ and put
\[
A=T-\lambda I.
\]

<1>1. The chain
\[
\ker A\subseteq\ker A^2\subseteq\cdots
\]
stabilizes by the $n$th term.

::: {.proof}
The dimensions
\[
\dim\ker A,\ \dim\ker A^2,\ \ldots
\]
form a nondecreasing sequence of integers between $0$ and $n$. If
\[
\ker A^m=\ker A^{m+1}
\]
for some $m$, then the chain remains constant thereafter: if $A^{m+2}v=0$, then
\[
Av\in\ker A^{m+1}=\ker A^m,
\]
so
\[
A^{m+1}v=0.
\]
Thus $v\in\ker A^{m+1}$, proving
\[
\ker A^{m+2}=\ker A^{m+1}.
\]
Repeating this argument shows equality of all later kernels. Since a strictly increasing chain of subspaces of an $n$-dimensional space has length at most $n$, one obtains
\[
\ker A^n=\ker A^{n+1}=\ker A^{n+2}=\cdots.
\]
:::

<1>2. For every $\lambda\in\mathbb C$,
\[
\boxed{V(\lambda)=\ker((T-\lambda I)^n)}.
\]

::: {.proof}
By definition,
\[
V(\lambda)
=
\bigcup_{N\ge1}\ker A^N.
\]
Step <1>1 shows that every kernel in this union is contained in
\[
\ker A^n
\]
and every later kernel equals it. Hence the union is exactly $\ker A^n$.
:::

<1>3. Suppose $\lambda\ne\mu$ and
\[
v\in V(\lambda)\cap V(\mu).
\]
Then there exist positive integers $r,s$ such that
\[
(T-\lambda I)^rv=0,
\qquad
(T-\mu I)^sv=0.
\]

::: {.proof}
This is exactly the definition of membership in the two generalized eigenspaces.
:::

<1>4. There exist polynomials $a(X),b(X)\in\mathbb C[X]$ such that
\[
a(X)(X-\lambda)^r+b(X)(X-\mu)^s=1.
\]

::: {.proof}
Because $\lambda\ne\mu$, the polynomials
\[
(X-\lambda)^r
\quad\text{and}\quad
(X-\mu)^s
\]
have no common root and are therefore coprime. Bézout's identity in the principal ideal domain $\mathbb C[X]$ gives the stated polynomials.
:::

<1>5. One has
\[
v=0.
\]

::: {.proof}
Evaluate the Bézout identity from step <1>4 at the operator $T$ and apply it to $v$:
\[
\begin{aligned}
v
&=
a(T)(T-\lambda I)^rv
+
b(T)(T-\mu I)^sv\\
&=0+0
=0,
\end{aligned}
\]
using step <1>3.
:::

<1>6. If $\lambda\ne\mu$, then
\[
\boxed{V(\lambda)\cap V(\mu)=\{0\}}.
\]

::: {.proof}
Every vector in the intersection is zero by step <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 proves part (a), with the uniform choice $M=n$, and step <1>6 proves part (b) for the corrected complexified statement.
:::
:::
