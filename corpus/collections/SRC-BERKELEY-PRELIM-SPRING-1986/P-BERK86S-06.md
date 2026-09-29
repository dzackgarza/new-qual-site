---
schema: qual/card@1
id: P-BERK86S-06
kind: problem
title: Two square-zero operators satisfying $AB+BA=I$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Restricted A and B to the two null spaces. The relation AB+BA=I makes
    these restrictions inverse isomorphisms, while every vector splits as
    ABv+BAv; the two-dimensional normal form follows from a vector in N_B.
---

::: {.problem}
Let $V$ be finite-dimensional and let $A,B\in\operatorname{End}(V)$ satisfy
\[
A^2=B^2=0,
\qquad
AB+BA=I.
\]
Let $N_A,N_B$ denote their null spaces.

1. Prove that
   \[
   N_A=A(N_B),
   \qquad
   N_B=B(N_A),
   \qquad
   V=N_A\oplus N_B.
   \]
2. Prove that $\dim V$ is even.
3. If $\dim V=2$, prove that there is a basis in which
   \[
   A=\begin{pmatrix}0&1\\0&0\end{pmatrix},
   \qquad
   B=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
   \]
:::

::: {.solution}
::: pf

::: {.pf-step #inclusions}
One has
$$
A(N_B)\subseteq N_A
\qquad\text{and}\qquad
B(N_A)\subseteq N_B.
$$

::: pf-proof
If $x\in N_B$, then
$$
A(Ax)=A^2x=0,
$$
so $Ax\in N_A$. Thus $A(N_B)\subseteq N_A$.
Similarly, if $y\in N_A$, then
$$
B(By)=B^2y=0,
$$
so $By\in N_B$.
:::

:::

::: {.pf-step #equalities-boxed}
In fact,
$$
\boxed{
N_A=A(N_B),
\qquad
N_B=B(N_A)
}.
$$

::: pf-proof
Let $x\in N_A$. Then $Ax=0$, so
$$
x
=(AB+BA)x
=
ABx.
$$
Moreover $Bx\in N_B$ because $B^2x=0$. Hence
$$
x=A(Bx)\in A(N_B).
$$
Together with step [](#inclusions){.pf-ref} this gives $N_A=A(N_B)$.

Interchanging $A$ and $B$ gives the second equality: if $y\in N_B$, then
$$
y
=(AB+BA)y
=
BAy
=
B(Ay),
$$
and $Ay\in N_A$.
:::

:::

::: {.pf-step #direct-sum-boxed}
One has
$$
\boxed{V=N_A\oplus N_B}.
$$

::: pf-proof
For every $v\in V$,
$$
v
=(AB+BA)v
=
A(Bv)+B(Av).
$$
Since $Bv\in N_B$ and $Av\in N_A$, step [](#inclusions){.pf-ref} gives
$$
A(Bv)\in N_A,
\qquad
B(Av)\in N_B.
$$
Thus $V=N_A+N_B$.

If $x\in N_A\cap N_B$, then
$$
x
=(AB+BA)x
=0.
$$
Therefore $N_A\cap N_B=\{0\}$, and the sum is direct.
:::

:::

::: {.pf-step #restrictions-inverse}
The restrictions
$$
A|_{N_B}:N_B\to N_A
\qquad\text{and}\qquad
B|_{N_A}:N_A\to N_B
$$
are inverse isomorphisms.

::: pf-proof
By step [](#inclusions){.pf-ref} the restrictions have the displayed codomains. If
$x\in N_A$, then
$$
A(Bx)
=
ABx
=
(AB+BA)x
=x,
$$
because $Ax=0$. If $y\in N_B$, then
$$
B(Ay)
=
BAy
=
(AB+BA)y
=y,
$$
because $By=0$. Hence the two restrictions are inverse linear maps.
:::

:::

::: {.pf-step #dim-even-boxed}
The dimension of $V$ is even.

::: pf-proof
By step [](#restrictions-inverse){.pf-ref},
$$
\dim N_A=\dim N_B.
$$
Using the direct sum from step [](#direct-sum-boxed){.pf-ref},
$$
\dim V
=
\dim N_A+\dim N_B
=
2\dim N_A.
$$
Thus
$$
\boxed{\dim V\text{ is even}}.
$$
:::

:::

::: {.pf-step #basis-boxed}
If $\dim V=2$, there is a basis in which
$$
\boxed{
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}
}.
$$

::: pf-proof
By steps [](#direct-sum-boxed){.pf-ref}, [](#restrictions-inverse){.pf-ref}, and [](#dim-even-boxed){.pf-ref},
$$
\dim N_A=\dim N_B=1.
$$
Choose a nonzero vector $v\in N_B$. Step [](#restrictions-inverse){.pf-ref} implies that
$$
Av\neq0,
$$
and $Av\in N_A$. Hence
$$
e_1\coloneqq Av,
\qquad
e_2\coloneqq v
$$
is a basis of $V$.

Now
$$
Ae_1=A^2v=0,
\qquad
Ae_2=Av=e_1.
$$
Also
$$
Be_2=Bv=0,
$$
while
$$
Be_1
=
BAv
=
(AB+BA)v-ABv
=
v
=e_2,
$$
because $Bv=0$. These four formulas give exactly the displayed matrices
in the ordered basis $(e_1,e_2)$.
:::

:::

::: pf-qed
Steps [](#equalities-boxed){.pf-ref} and [](#direct-sum-boxed){.pf-ref} prove part 1, step [](#dim-even-boxed){.pf-ref} proves part 2, and step
[](#basis-boxed){.pf-ref} proves part 3.
:::

:::
:::
