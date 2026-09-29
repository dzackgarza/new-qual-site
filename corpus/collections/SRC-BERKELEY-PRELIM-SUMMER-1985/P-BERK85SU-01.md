---
schema: qual/card@1
id: P-BERK85SU-01
kind: problem
title: Real $2\times2$ square roots of $-I$ and of $\operatorname{diag}(-1,-1-\varepsilon)$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Writing A=[[a,b],[c,d]], the equations from A^2=-I force a+d=0
    and bc=-1-a^2. Setting b=-p and c=q gives a^2=pq-1 and hence the
    stated parameterization. For the second part, A commutes with A^2;
    the target diagonal matrix has distinct diagonal entries, so A must
    be diagonal, which cannot square to a matrix with negative diagonal.
---

::: {.problem}
1. Show that a real $2\times2$ matrix $A$ satisfies $A^2=-I$ if and only if
\[
A=\begin{pmatrix}
\pm\sqrt{pq-1}&-p\\
q&\mp\sqrt{pq-1}
\end{pmatrix},
\]
where $p,q\in\mathbb R$, $pq\ge1$, and the two signs are chosen consistently.

2. Show that for every $\varepsilon>0$ there is no real $2\times2$ matrix $A$ such that
\[
A^2=\begin{pmatrix}-1&0\\0&-1-\varepsilon\end{pmatrix}.
\]
:::

::: {.solution}
Write
$$
A=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1}

If $A^2=-I$, then
$$
a+d=0.
$$

::: pf-proof

Expanding the square gives
$$
A^2=
\begin{pmatrix}
a^2+bc&b(a+d)\\
c(a+d)&d^2+bc
\end{pmatrix}.
$$
Thus $A^2=-I$ implies
$$
a^2+bc=-1,
\qquad
d^2+bc=-1,
$$
and hence
$$
a^2=d^2.
$$
If $a+d\neq0$, the off-diagonal equations
$$
b(a+d)=0,
\qquad
c(a+d)=0
$$
would force $b=c=0$. The first diagonal equation would then give
$a^2=-1$, impossible over $\RR$. Therefore $a+d=0$.

:::

:::

::: {.pf-step #s2}

If $A^2=-I$, then there are $p,q\in\RR$ with $pq\ge1$ such
that
$$
A=
\begin{pmatrix}
\pm\sqrt{pq-1}&-p\\
q&\mp\sqrt{pq-1}
\end{pmatrix}.
$$

::: pf-proof

By step [](#s1){.pf-ref}, $d=-a$. The diagonal equation becomes
$$
a^2+bc=-1.
$$
Set
$$
p=-b,
\qquad
q=c.
$$
Then
$$
a^2-pq=-1,
$$
so
$$
pq=a^2+1\ge1
$$
and
$$
a=\pm\sqrt{pq-1}.
$$
Since $d=-a$, the two diagonal signs are opposite, exactly as in the
stated form.

:::

:::

::: {.pf-step #s3}

Every matrix of the displayed form in part 1 satisfies
$$
A^2=-I.
$$

::: pf-proof

Let
$$
s=\pm\sqrt{pq-1},
\qquad
A=
\begin{pmatrix}
s&-p\\
q&-s
\end{pmatrix}.
$$
Then
$$
A^2=
\begin{pmatrix}
s^2-pq&0\\
0&s^2-pq
\end{pmatrix}.
$$
Since $s^2=pq-1$, this is $-I$.

:::

:::

::: {.pf-step #s4}

Part 1 is therefore proved.

::: pf-proof

Step [](#s2){.pf-ref} proves necessity, and step [](#s3){.pf-ref} proves sufficiency.

:::

:::

::: {.pf-step #s5}

For part 2, suppose for contradiction that a real matrix $A$
satisfies
$$
A^2=
D
\coloneqq
\begin{pmatrix}
-1&0\\
0&-1-\varepsilon
\end{pmatrix},
\qquad
\varepsilon>0.
$$
Then $A$ commutes with $D$.

::: pf-proof

Since $D=A^2$,
$$
AD
=
AA^2
=
A^3
=
A^2A
=
DA.
$$

:::

:::

::: {.pf-step #s6}

Any real $2\times2$ matrix commuting with $D$ is diagonal.

::: pf-proof

Write
$$
A=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}.
$$
The equation $AD=DA$ gives
$$
-b(1+\varepsilon)=-b,
\qquad
-c=-c(1+\varepsilon).
$$
Since $\varepsilon>0$, these equations force
$$
b=c=0.
$$
Thus $A$ is diagonal.

:::

:::

::: {.pf-step #s7}

No real diagonal matrix can square to $D$.

::: pf-proof

If
$$
A=
\begin{pmatrix}
a&0\\
0&d
\end{pmatrix},
$$
then
$$
A^2=
\begin{pmatrix}
a^2&0\\
0&d^2
\end{pmatrix}.
$$
Equality with $D$ would require $a^2=-1$, impossible for
$a\in\RR$.

:::

:::

::: {.pf-step #s8}

Therefore, for every $\varepsilon>0$, there is no real
$2\times2$ matrix whose square is
$$
\begin{pmatrix}
-1&0\\
0&-1-\varepsilon
\end{pmatrix}.
$$

::: pf-proof

Steps [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} show that assuming such a matrix exists leads to a
contradiction.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves part 1, and step [](#s8){.pf-ref} proves part 2.

:::

:::

:::
