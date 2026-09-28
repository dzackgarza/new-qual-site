---
schema: qual/card@1
id: P-AGHILBCONST
kind: problem
title: The constant term of $P_X(r)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hilbert Polynomial
  - Arithmetic Genus
  - Euler Characteristic
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is the follow-up asking for the meaning of the constant term of the Hilbert polynomial.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
What does the constant term of $P_X(r)$ represent?
:::

::: {.solution}
Let $X\subseteq\mathbb P^N$ be a projective scheme with Hilbert polynomial $P_X(r)$.

<1>1. The Hilbert polynomial is the Euler characteristic polynomial:
\[
P_X(r)=\chi\bigl(X,\mathcal O_X(r)\bigr).
\]
::: {.proof}
For $r\gg0$, Serre vanishing gives
\[
H^i(X,\mathcal O_X(r))=0
\qquad(i>0),
\]
so
\[
\chi(X,\mathcal O_X(r))
=h^0(X,\mathcal O_X(r))
=P_X(r).
\]
The Euler characteristic $\chi(X,\mathcal O_X(r))$ is itself polynomial in $r$, so equality for all sufficiently large integers identifies it with the same polynomial $P_X$.
:::

<1>2. Therefore the constant term is
\[
\boxed{
P_X(0)=\chi(X,\mathcal O_X)
=\sum_i(-1)^i h^i(X,\mathcal O_X).
}
\]
::: {.proof}
Set $r=0$ in the polynomial identity from <1>1.
:::

<1>3. If $C$ is a projective curve, then
\[
\boxed{P_C(0)=1-p_a(C).}
\]
::: {.proof}
The arithmetic genus of a projective curve is defined by
\[
p_a(C)=1-\chi(C,\mathcal O_C).
\]
Use <1>2.
:::

<1>4. In particular, if $C$ is a smooth connected projective curve of genus $g$, then
\[
\boxed{P_C(r)=\deg(C)\,r+1-g,}
\]
so the constant term is $1-g$.
::: {.proof}
For a smooth connected projective curve,
\[
p_a(C)=g.
\]
The coefficient of $r$ in the Hilbert polynomial is the degree, while <1>3 gives the constant term $1-g$.
:::

<1>5. More generally, if $X$ has pure dimension $n$, the arithmetic genus satisfies
\[
p_a(X)=(-1)^n\bigl(\chi(\mathcal O_X)-1\bigr),
\]
so
\[
\boxed{P_X(0)=1+(-1)^n p_a(X).}
\]
::: {.proof}
Substitute the identity $P_X(0)=\chi(\mathcal O_X)$ from <1>2 into the definition of arithmetic genus and solve for $P_X(0)$.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>2 identifies the constant term intrinsically, and steps <1>3--<1>5 express it in the usual genus language.
:::
:::
