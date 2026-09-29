---
schema: qual/card@1
id: P-BERK89S-07
kind: problem
title: The matrix ODE $X'=AXB$ for two nilpotent shift matrices
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
    Solved the constant-coefficient matrix ODE by the nilpotent operator
    $L(Y)=AYB$, whose fourth power vanishes, and expanded the resulting finite
    exponential in both matrix and entrywise form.
---

::: {.problem}
Let
\[
A=\begin{pmatrix}
0&0&0&0\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{pmatrix},
\qquad
B=\begin{pmatrix}
0&1&0&0\\
0&0&1&0\\
0&0&0&1\\
0&0&0&0
\end{pmatrix}.
\]
Find the general solution of
\[
\frac{dX}{dt}=AXB
\]
for an unknown $4\times4$ matrix-valued function $X(t)$.
:::

::: {.solution}
Define the linear operator
$$
L:M_4(\RR)\longrightarrow M_4(\RR),
\qquad
L(Y)=AYB.
$$

::: pf

::: {.pf-step #l-power-formula}
For every integer $k\geq0$ and every $Y\in M_4(\RR)$,
$$
L^k(Y)=A^kYB^k,
$$
and in particular $L^4=0$.

::: pf-proof
The displayed identity follows by induction on $k$: if
$L^k(Y)=A^kYB^k$, then
$$
L^{k+1}(Y)=A(A^kYB^k)B=A^{k+1}YB^{k+1}.
$$
Both $A$ and $B$ are nilpotent shift matrices with $A^4=B^4=0$. Hence
$$
L^4(Y)=A^4YB^4=0
$$
for every $Y$.
:::

:::

::: {.pf-step #xc-is-solution}
For every constant matrix $C\in M_4(\RR)$, the function
$$
X_C(t)=C+tL(C)+\frac{t^2}{2}L^2(C)+\frac{t^3}{6}L^3(C)
$$
satisfies $X_C'=L(X_C)$ and $X_C(0)=C$.

::: pf-proof
Differentiating gives
$$
X_C'(t)
=L(C)+tL^2(C)+\frac{t^2}{2}L^3(C).
$$
On the other hand, using step [](#l-power-formula){.pf-ref},
$$
\begin{aligned}
L(X_C(t))
&=L(C)+tL^2(C)+\frac{t^2}{2}L^3(C)+\frac{t^3}{6}L^4(C)\\
&=L(C)+tL^2(C)+\frac{t^2}{2}L^3(C).
\end{aligned}
$$
Thus $X_C'=L(X_C)$, and substituting $t=0$ gives $X_C(0)=C$.
:::

:::

::: {.pf-step #general-solution-boxed}
The general solution is
$$
\boxed{
X(t)=C+tACB+\frac{t^2}{2}A^2CB^2+\frac{t^3}{6}A^3CB^3,
\qquad C\in M_4(\RR)\text{ arbitrary}.
}
$$

::: pf-proof
By steps [](#l-power-formula){.pf-ref} and [](#xc-is-solution){.pf-ref}, every displayed function is a solution with initial
value $X(0)=C$. Conversely, any solution has some initial value
$C=X(0)$. The uniqueness theorem for finite-dimensional linear systems applied
to $X'=L(X)$ shows that it must equal the solution $X_C$ from step [](#xc-is-solution){.pf-ref}.
Substituting $L^k(C)=A^kCB^k$ from step [](#l-power-formula){.pf-ref} gives the boxed formula.
:::

:::

::: {.pf-step #entrywise-formula}
If $C=(c_{ij})$, then the solution in step [](#general-solution-boxed){.pf-ref} has entries
$$
x_{ij}(t)
=\sum_{k=0}^{\min(i,j)-1}\frac{t^k}{k!}c_{i-k,j-k}
\qquad(1\leq i,j\leq4).
$$

::: pf-proof
Left multiplication by $A^k$ shifts the rows of a matrix downward by $k$
places, inserting zero rows at the top, while right multiplication by $B^k$
shifts its columns to the right by $k$ places, inserting zero columns at the
left. Therefore
$$
(A^kCB^k)_{ij}
=\begin{cases}
c_{i-k,j-k},&i>k\text{ and }j>k,\\
0,&\text{otherwise}.
\end{cases}
$$
Substituting this into step [](#general-solution-boxed){.pf-ref} gives the stated entry formula.
:::

:::

::: pf-qed
Step [](#general-solution-boxed){.pf-ref} gives all solutions, and step [](#entrywise-formula){.pf-ref} records their entries explicitly.
:::

:::
:::
