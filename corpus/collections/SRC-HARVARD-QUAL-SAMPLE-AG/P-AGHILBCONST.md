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

::: pf

::: {.pf-step #hilbert-euler-characteristic}
The Hilbert polynomial is the Euler characteristic polynomial:
\[
P_X(r)=\chi\bigl(X,\mathcal O_X(r)\bigr).
\]

::: pf-proof
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

:::

::: {.pf-step #constant-term-definition}
Therefore the constant term is
\[
\boxed{
P_X(0)=\chi(X,\mathcal O_X)
=\sum_i(-1)^i h^i(X,\mathcal O_X).
}
\]

::: pf-proof
Set $r=0$ in the polynomial identity from step [](#hilbert-euler-characteristic){.pf-ref}.
:::

:::

::: {.pf-step #curve-constant-term}
If $C$ is a projective curve, then
\[
\boxed{P_C(0)=1-p_a(C).}
\]

::: pf-proof
The arithmetic genus of a projective curve is defined by
\[
p_a(C)=1-\chi(C,\mathcal O_C).
\]
Use step [](#constant-term-definition){.pf-ref}.
:::

:::

::: {.pf-step #smooth-curve-formula}
In particular, if $C$ is a smooth connected projective curve of genus $g$, then
\[
\boxed{P_C(r)=\deg(C)\,r+1-g,}
\]
so the constant term is $1-g$.

::: pf-proof
For a smooth connected projective curve,
\[
p_a(C)=g.
\]
The coefficient of $r$ in the Hilbert polynomial is the degree, while step [](#curve-constant-term){.pf-ref} gives the constant term $1-g$.
:::

:::

::: {.pf-step #general-dimension-formula}
More generally, if $X$ has pure dimension $n$, the arithmetic genus satisfies
\[
p_a(X)=(-1)^n\bigl(\chi(\mathcal O_X)-1\bigr),
\]
so
\[
\boxed{P_X(0)=1+(-1)^n p_a(X).}
\]

::: pf-proof
Substitute the identity $P_X(0)=\chi(\mathcal O_X)$ from step [](#constant-term-definition){.pf-ref} into the definition of arithmetic genus and solve for $P_X(0)$.
:::

:::

::: pf-qed
Step [](#constant-term-definition){.pf-ref} identifies the constant term intrinsically, and steps [](#curve-constant-term){.pf-ref}, [](#smooth-curve-formula){.pf-ref} and [](#general-dimension-formula){.pf-ref} express it in the usual genus language.
:::

:::
:::
