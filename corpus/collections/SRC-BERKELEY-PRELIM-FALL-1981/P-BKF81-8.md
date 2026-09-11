---
schema: qual/card@1
id: P-BKF81-8
kind: problem
title: Zeros of $3z^{100}-e^z$ in the unit disk
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
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
  note: "Applied Rouché on the unit circle and then used the simultaneous equations f(z)=f'(z)=0 to rule out multiple zeros."
---

::: problem
Let $f(z)=3z^{100}-e^z$.

(a) How many zeros does $f$ have in the unit disk, counting multiplicities?

(b) Are the zeros distinct?
:::

::: solution
<1>1. Count the zeros in the unit disk.
::: proof
On $|z|=1$,
$$
|3z^{100}|=3,
$$
while
$$
|e^z|=e^{\operatorname{Re}z}\le e<3.
$$
Thus
$$
|-e^z|<|3z^{100}|
$$
on the unit circle. By Rouché's theorem,
$$
f(z)=3z^{100}-e^z
$$
and $3z^{100}$ have the same number of zeros in $|z|<1$, counted with
multiplicity. The latter has a zero of multiplicity $100$ at $0$. Hence
$$
\boxed{f\text{ has }100\text{ zeros in the unit disk, counted with multiplicity}.}
$$
:::

<1>2. Every zero of $f$ in the unit disk is simple.
::: proof
Suppose $z$ were a multiple zero. Then
$$
f(z)=0
$$
and
$$
f'(z)=0.
$$
The first equation gives
$$
e^z=3z^{100}.
$$
In particular $z\ne0$. Since
$$
f'(z)=300z^{99}-e^z,
$$
substituting the root equation yields
$$
f'(z)
=300z^{99}-3z^{100}
=3z^{99}(100-z).
$$
Thus a multiple zero would have to satisfy $z=100$, because $z\ne0$. But
$100$ is not in the unit disk. Therefore every zero in $|z|<1$ is simple.

Consequently the $100$ zeros counted in step <1>1 are
$$
\boxed{100\text{ distinct zeros}.}
$$
:::
:::
