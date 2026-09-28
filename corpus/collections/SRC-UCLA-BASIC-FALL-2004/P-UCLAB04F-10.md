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

For the corrected statement, put $A=T-\lambda I$.
The chain
\[
\ker A\subseteq\ker A^2\subseteq\cdots
\]
is an ascending chain of subspaces of the finite-dimensional space $V$, hence stabilizes.
Thus for some $M$,
\[
\ker A^M=\ker A^{M+1}=\cdots,
\]
and therefore
\[
V(\lambda)=\bigcup_{N\geq1}\ker A^N=\ker A^M.
\]

Now suppose $v\in V(\lambda)\cap V(\mu)$ with $\lambda\ne\mu$.
Choose $r,s$ so that
\[
(T-\lambda I)^rv=0,
\qquad
(T-\mu I)^sv=0.
\]
The polynomials $(X-\lambda)^r$ and $(X-\mu)^s$ are coprime, so Bézout's identity gives polynomials $a,b$ such that
\[
a(X)(X-\lambda)^r+b(X)(X-\mu)^s=1.
\]
Evaluating at $T$ and applying to $v$ gives $v=0$.
Hence
\[
V(\lambda)\cap V(\mu)=\{0\}.
\]
:::
