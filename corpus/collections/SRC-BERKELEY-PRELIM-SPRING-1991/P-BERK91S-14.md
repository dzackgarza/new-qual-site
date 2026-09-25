---
schema: qual/card@1
id: P-BERK91S-14
kind: problem
title: Norm growth for a linear system in $\RR^3$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-23
  note: Compared all nine matrix entries, the nontrivial-solution hypothesis, and Euclidean norm growth with Problem 14 in the retained MinerU Flash extraction of Spring91.pdf.
---

::: {.problem}
Let $x(t)$ be a nontrivial solution of
$$
\frac{dx}{dt}=Ax,
\qquad
A=\begin{pmatrix}
1&6&1\\
-4&4&11\\
-3&-9&8
\end{pmatrix}.
$$
Prove that the Euclidean norm $\norm{x(t)}$ is an increasing function of $t$.
:::

::: {.hint}
Let $S\coloneqq(A+A^{\mathsf T})/2$. Differentiating the squared
Euclidean norm gives
$$
\frac{d}{dt}\norm{x(t)}^2=2x(t)^{\mathsf T}Sx(t).
$$
For a real column vector $v=(v_1,v_2,v_3)^{\mathsf T}$,
$$
v^{\mathsf T}Sv
=(v_1+v_2-v_3)^2+(v_2+2v_3)^2+2v_2^2+3v_3^2.
$$
Uniqueness for the linear differential equation excludes a
zero value of a nontrivial solution.
:::

::: {.solution}
Set
$$
S\coloneqq\frac{A+A^{\mathsf T}}2
=\begin{pmatrix}
1&1&-1\\
1&4&1\\
-1&1&8
\end{pmatrix}.
$$

<1>1. The quadratic form defined by $S$ is positive definite.

::: {.proof}
For $v=(v_1,v_2,v_3)^{\mathsf T}\in\RR^3$,
$$
\begin{aligned}
v^{\mathsf T}Sv
&=v_1^2+2v_1v_2-2v_1v_3+4v_2^2+2v_2v_3+8v_3^2\\
&=(v_1+v_2-v_3)^2+(v_2+2v_3)^2+2v_2^2+3v_3^2.
\end{aligned}
$$
This is nonnegative. If it is zero, then the last two terms give $v_2=v_3=0$, and the first square then gives $v_1=0$. Hence $v^{\mathsf T}Sv>0$ for every nonzero $v$.
:::

<1>2. $x(t)\neq0$ for every $t$ in the interval of definition of the solution.

::: {.proof}
If $x(t_0)=0$ for some $t_0$, then the zero solution and the given solution have the same initial value at $t_0$. Uniqueness for the linear system $x'=Ax$ therefore forces $x(t)\equiv0$, contrary to the hypothesis that the solution is nontrivial.
:::

<1>3. $\dfrac{d}{dt}\norm{x(t)}^2>0$ for every $t$.

::: {.proof}
Since $x'=Ax$,
$$
\begin{aligned}
\frac{d}{dt}\norm{x(t)}^2
&=x'(t)^{\mathsf T}x(t)+x(t)^{\mathsf T}x'(t)\\
&=x(t)^{\mathsf T}(A^{\mathsf T}+A)x(t)\\
&=2x(t)^{\mathsf T}Sx(t).
\end{aligned}
$$
By step <1>2, $x(t)$ is nonzero, so step <1>1 makes the final expression strictly positive.
:::

<1>4. $\norm{x(t)}$ is strictly increasing in $t$.

::: {.proof}
Step <1>3 shows that $t\mapsto\norm{x(t)}^2$ is strictly increasing. The square-root function is strictly increasing on $[0,\infty)$, so $t\mapsto\norm{x(t)}$ is strictly increasing as well.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves the required monotonicity.
:::
:::
