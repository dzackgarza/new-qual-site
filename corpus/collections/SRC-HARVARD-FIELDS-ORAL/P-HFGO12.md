---
schema: qual/card@1
id: P-HFGO12
kind: problem
title: An inseparable field extension
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Give an example of an inseparable field extension.
:::

::: solution
Let $p$ be prime, let
\[
F=\mathbb F_p(t),
\]
and let $u$ satisfy
\[
u^p=t.
\]
Then
\[
E=F(u)/F
\]
is an inseparable extension of degree $p$.

<1>1. The polynomial
\[
f(x)=x^p-t\in F[x]
\]
is irreducible.
::: proof
Regard $f$ first as a polynomial in $\mathbb F_p[t][x]$. It is Eisenstein at
the prime element $t$: every nonleading coefficient is divisible by $t$, the
constant term $-t$ is not divisible by $t^2$, and the leading coefficient is
$1$. Thus $f$ is irreducible over $\mathbb F_p(t)$ by Eisenstein's criterion
and Gauss's lemma.
:::

<1>2. The polynomial $f$ is inseparable.
::: proof
In characteristic $p$,
\[
f'(x)=p x^{p-1}=0.
\]
In an algebraic closure, if $u^p=t$, then
\[
x^p-t=x^p-u^p=(x-u)^p,
\]
so the unique root $u$ has multiplicity $p$.
:::

<1>3. Hence $E/F$ is inseparable.
::: proof
The minimal polynomial of $u$ over $F$ is the irreducible polynomial $f$ from
<1>1, and <1>2 shows that it has a repeated root. Therefore $u$ is inseparable
over $F$, so $E/F$ is an inseparable extension.
:::
:::
