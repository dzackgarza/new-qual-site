---
schema: qual/card@1
id: P-UCLAB03S-05
kind: problem
title: Extremizing a binary quadratic form on the unit circle
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the official UCLA Basic Examination, May 2003 PDF. The source defines the constraint set using the undefined symbol $s^2+y^2=1$; the variables everywhere else are $(x,y)$, so the intended unit-circle equation is $x^2+y^2=1$.
---

::: {.problem}
Consider
\[
F(x,y)=ax^2+2bxy+cy^2
\]
on the unit circle
\[
A=\{(x,y):x^2+y^2=1\}.
\]

(a) Show that $F$ has a maximum and a minimum on $A$.

(b) Use Lagrange multipliers to show that, if the maximum of $F$ on $A$ occurs at $(x_0,y_0)$, then $(x_0,y_0)$ is an eigenvector of
\[
\begin{pmatrix}
a&b\\
b&c
\end{pmatrix}.
\]
:::

::: {.solution}

Set
\[
M=\begin{pmatrix}a&b\\b&c\end{pmatrix},
\qquad
h(x,y)=x^2+y^2.
\]

::: pf

::: {.pf-step #s1-1}

The set $A$ is compact.


::: pf-proof

The set
\[
A=\{(x,y)\in\RR^2:h(x,y)=1\}
\]
is closed because $h$ is continuous and $\{1\}$ is closed. It is bounded because every $(x,y)\in A$ satisfies $x^2+y^2=1$. Hence $A$ is compact by the Heine--Borel theorem.

:::

:::

::: {.pf-step #s1-2}

The function $F$ attains both a maximum and a minimum on $A$.


::: pf-proof

The polynomial
\[
F(x,y)=ax^2+2bxy+cy^2
\]
is continuous on $\RR^2$. By step [](#s1-1){.pf-ref}, $A$ is compact and nonempty. The extreme value theorem therefore gives points of $A$ at which $F$ attains its maximum and minimum.

:::

:::

::: {.pf-step #s1-3}

If $F$ attains its maximum on $A$ at $(x_0,y_0)$, then there is $\lambda\in\RR$ such that
\[
\nabla F(x_0,y_0)=\lambda\nabla h(x_0,y_0).
\]


::: pf-proof

At every point $(x,y)\in A$,
\[
\nabla h(x,y)=(2x,2y)\neq(0,0),
\]
because $x^2+y^2=1$. Thus the constraint is regular at the maximizing point supplied by step [](#s1-2){.pf-ref}. The Lagrange multiplier theorem therefore gives the stated scalar $\lambda$.

:::

:::

::: {.pf-step #s1-4}

The vector $(x_0,y_0)^T$ satisfies
\[
M\binom{x_0}{y_0}=\lambda\binom{x_0}{y_0}.
\]


::: pf-proof

Direct differentiation gives
\[
\nabla F(x,y)
=
\bigl(2ax+2by,\,2bx+2cy\bigr)
=
2M\binom{x}{y},
\]
while
\[
\nabla h(x,y)=2\binom{x}{y}.
\]
Substituting these formulas into step [](#s1-3){.pf-ref} and dividing by $2$ gives
\[
M\binom{x_0}{y_0}
=
\lambda\binom{x_0}{y_0}.
\]

:::

:::

::: {.pf-step #s1-5}

The maximizing vector $(x_0,y_0)^T$ is an eigenvector of $M$.


::: pf-proof

Since $(x_0,y_0)\in A$, one has $x_0^2+y_0^2=1$, so $(x_0,y_0)^T\neq0$. Step [](#s1-4){.pf-ref} therefore exhibits this nonzero vector as an eigenvector of $M$ with eigenvalue $\lambda$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), and step [](#s1-5){.pf-ref} proves part (b).

:::

:::

:::
