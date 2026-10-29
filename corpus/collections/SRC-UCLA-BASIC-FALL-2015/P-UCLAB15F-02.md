---
schema: qual/card@1
id: P-UCLAB15F-02
kind: problem
title: Weighted mean value theorem for integrals
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Basic Examination, Fall 2015, `assets/attachments/basic-15F.pdf`; the PDF is image-only and the preserved extraction supplies the statement text.
---

::: {.problem}
Let $a,b\in\RR$ with $a<b$.
Show that if $g,h:[a,b]\to\RR$ are continuous and $h\ge0$, then there is $c\in[a,b]$ such that
$$
\int_a^b g(x)h(x)\,dx=g(c)\int_a^b h(x)\,dx.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let
$$
m=\min_{x\in[a,b]}g(x),
\qquad
M=\max_{x\in[a,b]}g(x).
$$
These numbers exist.


::: pf-proof

The interval $[a,b]$ is compact and $g$ is continuous.
Hence the extreme value theorem gives a minimum and a maximum.

:::

:::

::: {.pf-step #s1-2}

Since $h\ge0$,
$$
m\int_a^b h(x)\,dx
\le
\int_a^b g(x)h(x)\,dx
\le
M\int_a^b h(x)\,dx.
$$


::: pf-proof

For every $x$,
$$
m\le g(x)\le M.
$$
Multiplying by the nonnegative number $h(x)$ gives
$$
mh(x)\le g(x)h(x)\le Mh(x).
$$
Integrate over $[a,b]$.

:::

:::

::: {.pf-step #s1-3}

If
$$
\int_a^b h(x)\,dx=0,
$$
then the desired identity holds for every $c\in[a,b]$.


::: pf-proof

Since $h$ is continuous and nonnegative, the equality
$$
\int_a^b h(x)\,dx=0
$$
forces
$$
h\equiv0.
$$
Hence
$$
\int_a^b g(x)h(x)\,dx=0.
$$
The right-hand side is also
$$
g(c)\cdot0=0.
$$

:::

:::

::: {.pf-step #s1-4}

Suppose
$$
\int_a^b h(x)\,dx>0.
$$
Then
$$
m
\le
\frac{\int_a^b g(x)h(x)\,dx}
{\int_a^b h(x)\,dx}
\le
M.
$$


::: pf-proof

Divide the inequalities from step [](#s1-2){.pf-ref} by the positive number
$$
\int_a^b h(x)\,dx.
$$

:::

:::

::: {.pf-step #s1-5}

There exists $c\in[a,b]$ such that
$$
g(c)
=
\frac{\int_a^b g(x)h(x)\,dx}
{\int_a^b h(x)\,dx}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the continuous function $g$ attains the values $m$ and $M$.
By step [](#s1-4){.pf-ref}, the displayed quotient lies between them.
The intermediate value theorem therefore gives a point $c$ at which $g$ equals this quotient.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\int_a^b g(x)h(x)\,dx
=
g(c)\int_a^b h(x)\,dx
}
$$
for some $c\in[a,b]$.


::: pf-proof

Step [](#s1-3){.pf-ref} handles the case in which the integral of $h$ is zero.
Otherwise multiply the identity in step [](#s1-5){.pf-ref} by
$$
\int_a^b h(x)\,dx.
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required weighted mean value theorem.

:::

:::

:::
