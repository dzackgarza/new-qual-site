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
$$
F_{2n+1}F_{2n-1}-F_{2n}^2=1
$$
for all $n\ge1$.
:::

::: {.solution}

Let
$$
\phi=\frac{1+\sqrt5}{2},
\qquad
\psi=\frac{1-\sqrt5}{2}.
$$
Then
$$
\phi^2=\phi+1,
\qquad
\psi^2=\psi+1,
\qquad
\phi-\psi=\sqrt5.
$$

::: pf

::: pf-step

The sequence
$$
G_n=\frac{\phi^n-\psi^n}{\sqrt5}
$$
satisfies
$$
G_0=0,
\qquad
G_1=1,
\qquad
G_n=G_{n-1}+G_{n-2}
$$
for $n\ge2$.


::: pf-proof

The initial values are
$$
G_0=\frac{1-1}{\sqrt5}=0
$$
and
$$
G_1=\frac{\phi-\psi}{\sqrt5}=1.
$$

Since
$$
\phi^2=\phi+1,
$$
one has
$$
\phi^n=\phi^{n-1}+\phi^{n-2}
$$
for $n\ge2$.
The same identity holds for $\psi$.
Subtracting and dividing by $\sqrt5$ gives
$$
G_n=G_{n-1}+G_{n-2}.
$$

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\boxed{
F_n
=
\frac{\phi^n-\psi^n}{\sqrt5}
}
$$
for every $n\ge0$.


::: pf-proof

The Fibonacci sequence and $(G_n)$ satisfy the same second-order recurrence with the same initial values.
The recurrence uniquely determines every subsequent term.
Thus
$$
F_n=G_n
$$
for all $n$.

:::

:::

::: {.pf-step #s1-3}

For $n\ge2$,
$$
\frac{F_n}{F_{n-1}}
=
\phi
\frac{
1-(\psi/\phi)^n
}{
1-(\psi/\phi)^{n-1}
}.
$$


::: pf-proof

Using step [](#s1-2){.pf-ref},
$$
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
$$
The denominator is nonzero because
$$
F_{n-1}>0
$$
for $n\ge2$.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\left|\frac{\psi}{\phi}\right|<1.
$$


::: pf-proof

The numbers satisfy
$$
\phi>1
$$
and
$$
|\psi|
=
\frac{\sqrt5-1}{2}
<
1.
$$
Therefore
$$
\left|\frac{\psi}{\phi}\right|
<
1.
$$

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
\lim_{n\to\infty}
\frac{F_n}{F_{n-1}}
=
\phi
=
\frac{1+\sqrt5}{2}.
}
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
\left(\frac{\psi}{\phi}\right)^n
\to0.
$$
Taking the limit in step [](#s1-3){.pf-ref} gives
$$
\lim_{n\to\infty}
\frac{F_n}{F_{n-1}}
=
\phi
\frac{1-0}{1-0}
=
\phi.
$$
This proves part (a).

:::

:::

::: {.pf-step #s1-6}

Define
$$
D_m
=
F_{m+1}F_{m-1}-F_m^2
$$
for $m\ge1$.
Then
$$
\boxed{D_{m+1}=-D_m}.
$$


::: pf-proof

Using
$$
F_{m+2}=F_{m+1}+F_m,
$$
one has
$$
\begin{aligned}
D_{m+1}
&=
F_{m+2}F_m-F_{m+1}^2\\
&=
(F_{m+1}+F_m)F_m-F_{m+1}^2\\
&=
F_mF_{m+1}+F_m^2-F_{m+1}^2.
\end{aligned}
$$

Also,
$$
F_{m-1}=F_{m+1}-F_m,
$$
so
$$
\begin{aligned}
D_m
&=
F_{m+1}(F_{m+1}-F_m)-F_m^2\\
&=
F_{m+1}^2-F_mF_{m+1}-F_m^2.
\end{aligned}
$$
Comparing the two formulas gives
$$
D_{m+1}=-D_m.
$$

:::

:::

::: {.pf-step #s1-7}

One has
$$
D_1=-1.
$$


::: pf-proof

Since
$$
F_0=0,
\qquad
F_1=1,
\qquad
F_2=1,
$$
one obtains
$$
D_1
=
F_2F_0-F_1^2
=
1\cdot0-1
=
-1.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
F_{m+1}F_{m-1}-F_m^2
=
(-1)^m
}
$$
for every $m\ge1$.


::: pf-proof

By step [](#s1-6){.pf-ref}, the numbers $D_m$ alternate sign:
$$
D_m=(-1)^{m-1}D_1.
$$
Using step [](#s1-7){.pf-ref},
$$
D_m
=
(-1)^{m-1}(-1)
=
(-1)^m.
$$
This is Cassini's identity.

:::

:::

::: {.pf-step #s1-9}

Setting
$$
m=2n
$$
in step [](#s1-8){.pf-ref} gives
$$
\boxed{
F_{2n+1}F_{2n-1}-F_{2n}^2
=
1.
}
$$


::: pf-proof

Since
$$
(-1)^{2n}=1,
$$
step [](#s1-8){.pf-ref} becomes exactly the identity required in part (b).

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves part (a), and step [](#s1-9){.pf-ref} proves part (b).

:::

:::

:::
