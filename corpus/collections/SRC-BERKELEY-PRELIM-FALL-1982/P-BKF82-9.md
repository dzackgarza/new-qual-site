---
schema: qual/card@1
id: P-BKF82-9
kind: problem
title: An integral inequality for a nonnegative function
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Introduced F(t)=1+2∫_0^t f, differentiated sqrt(F), and used f²≤F to obtain (sqrt F)'≤1."
---

::: problem
Let $f\ge0$ be continuous on $[0,1]$ and suppose
\[
f(t)^2\le1+2\int_0^t f(s)\,ds.
\]
Show that $f(t)\le1+t$ for $t\in[0,1]$.
:::

::: solution
Define
$$
F(t)=1+2\int_0^t f(s)\,ds.
$$
Because $f\ge0$, we have $F(t)\ge1$.

<1>1. Bound the derivative of $\sqrt{F}$.
::: proof
By the fundamental theorem of calculus,
$$
F'(t)=2f(t).
$$
The hypothesis says
$$
f(t)^2\le F(t).
$$
Since both sides are nonnegative,
$$
f(t)\le\sqrt{F(t)}.
$$
Therefore
$$
\frac{d}{dt}\sqrt{F(t)}
=\frac{F'(t)}{2\sqrt{F(t)}}
=\frac{f(t)}{\sqrt{F(t)}}
\le1.
$$
:::

<1>2. Integrate the differential inequality.
::: proof
Since $F(0)=1$, step <1>1 gives
$$
\sqrt{F(t)}-1
\le t
$$
for $0\le t\le1$. Thus
$$
\sqrt{F(t)}\le1+t.
$$
Using again $f(t)\le\sqrt{F(t)}$,
$$
\boxed{f(t)\le1+t}
$$
for every $t\in[0,1]$.
:::
:::
