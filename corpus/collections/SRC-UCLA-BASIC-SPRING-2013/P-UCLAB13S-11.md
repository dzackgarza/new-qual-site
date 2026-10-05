---
schema: qual/card@1
id: P-UCLAB13S-11
kind: problem
title: Two identities for Fibonacci numbers
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Spring 2013.
---

::: {.problem}
Define the Fibonacci sequence by $F_0=0$, $F_1=1$, and $F_n=F_{n-1}+F_{n-2}$ for $n\ge2$.

(a) Show that the limit of $F_n/F_{n-1}$ as $n\to\infty$ exists and find its value.

(b) Prove that
\[
F_{2n+1}F_{2n-1}-F_{2n}^2=1
\]
for all $n\ge1$.
:::

::: {.solution}
Let
\[
\phi=\frac{1+\sqrt5}{2},
\qquad
\psi=\frac{1-\sqrt5}{2}.
\]
Then
\[
\phi^2=\phi+1,
\qquad
\psi^2=\psi+1,
\qquad
\phi-\psi=\sqrt5.
\]

<1>1. The sequence
\[
G_n=\frac{\phi^n-\psi^n}{\sqrt5}
\]
satisfies
\[
G_0=0,
\qquad
G_1=1,
\qquad
G_n=G_{n-1}+G_{n-2}
\]
for $n\ge2$.

::: {.proof}
The initial values are
\[
G_0=\frac{1-1}{\sqrt5}=0
\]
and
\[
G_1=\frac{\phi-\psi}{\sqrt5}=1.
\]

Since
\[
\phi^2=\phi+1,
\]
one has
\[
\phi^n=\phi^{n-1}+\phi^{n-2}
\]
for $n\ge2$.
The same identity holds for $\psi$.
Subtracting and dividing by $\sqrt5$ gives
\[
G_n=G_{n-1}+G_{n-2}.
\]
:::

<1>2. Therefore
\[
\boxed{
F_n
=
\frac{\phi^n-\psi^n}{\sqrt5}
}
\]
for every $n\ge0$.

::: {.proof}
The Fibonacci sequence and $(G_n)$ satisfy the same second-order recurrence with the same initial values.
The recurrence uniquely determines every subsequent term.
Thus
\[
F_n=G_n
\]
for all $n$.
:::

<1>3. For $n\ge2$,
\[
\frac{F_n}{F_{n-1}}
=
\phi
\frac{
1-(\psi/\phi)^n
}{
1-(\psi/\phi)^{n-1}
}.
\]

::: {.proof}
Using step <1>2,
\[
\begin{aligned}
\frac{F_n}{F_{n-1}}
&=
\frac{\phi^n-\psi^n}
{\phi^{n-1}-\psi^{n-1}}\\
&=
\phi
\frac{
1-(\psi/\phi)^n
}{
1-(\psi/\phi)^{n-1}
}.
\end{aligned}
\]
The denominator is nonzero because
\[
F_{n-1}>0
\]
for $n\ge2$.
:::

<1>4. One has
\[
\left|\frac{\psi}{\phi}\right|<1.
\]

::: {.proof}
The numbers satisfy
\[
\phi>1
\]
and
\[
|\psi|
=
\frac{\sqrt5-1}{2}
<
1.
\]
Therefore
\[
\left|\frac{\psi}{\phi}\right|
<
1.
\]
:::

<1>5. Hence
\[
\boxed{
\lim_{n\to\infty}
\frac{F_n}{F_{n-1}}
=
\phi
=
\frac{1+\sqrt5}{2}.
}
\]

::: {.proof}
By step <1>4,
\[
\left(\frac{\psi}{\phi}\right)^n
\to0.
\]
Taking the limit in step <1>3 gives
\[
\lim_{n\to\infty}
\frac{F_n}{F_{n-1}}
=
\phi
\frac{1-0}{1-0}
=
\phi.
\]
This proves part (a).
:::

<1>6. Define
\[
D_m
=
F_{m+1}F_{m-1}-F_m^2
\]
for $m\ge1$.
Then
\[
\boxed{D_{m+1}=-D_m}.
\]

::: {.proof}
Using
\[
F_{m+2}=F_{m+1}+F_m,
\]
one has
\[
\begin{aligned}
D_{m+1}
&=
F_{m+2}F_m-F_{m+1}^2\\
&=
(F_{m+1}+F_m)F_m-F_{m+1}^2\\
&=
F_mF_{m+1}+F_m^2-F_{m+1}^2.
\end{aligned}
\]

Also,
\[
F_{m-1}=F_{m+1}-F_m,
\]
so
\[
\begin{aligned}
D_m
&=
F_{m+1}(F_{m+1}-F_m)-F_m^2\\
&=
F_{m+1}^2-F_mF_{m+1}-F_m^2.
\end{aligned}
\]
Comparing the two formulas gives
\[
D_{m+1}=-D_m.
\]
:::

<1>7. One has
\[
D_1=-1.
\]

::: {.proof}
Since
\[
F_0=0,
\qquad
F_1=1,
\qquad
F_2=1,
\]
one obtains
\[
D_1
=
F_2F_0-F_1^2
=
1\cdot0-1
=
-1.
\]
:::

<1>8. Therefore
\[
\boxed{
F_{m+1}F_{m-1}-F_m^2
=
(-1)^m
}
\]
for every $m\ge1$.

::: {.proof}
By step <1>6, the numbers $D_m$ alternate sign:
\[
D_m=(-1)^{m-1}D_1.
\]
Using step <1>7,
\[
D_m
=
(-1)^{m-1}(-1)
=
(-1)^m.
\]
This is Cassini's identity.
:::

<1>9. Setting
\[
m=2n
\]
in step <1>8 gives
\[
\boxed{
F_{2n+1}F_{2n-1}-F_{2n}^2
=
1.
}
\]

::: {.proof}
Since
\[
(-1)^{2n}=1,
\]
step <1>8 becomes exactly the identity required in part (b).
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>5 proves part (a), and step <1>9 proves part (b).
:::
:::
