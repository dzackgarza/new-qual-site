---
schema: qual/card@1
id: E-AMD-5QO44RPA
kind: problem
title: No simple group of order $p^2 q^2$ for primes $p<q$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that no group of order $p^2 q^2$ is simple for $p<q$ primes.
:::

::: {.solution}
Let \(|G|=p^2q^2\) with primes \(p<q\), and write \(n_q\) for the number of Sylow \(q\)-subgroups. Sylow gives
\[
n_q\mid p^2,
\qquad
n_q\equiv1\pmod q,
\]
so \(n_q\in\{1,p,p^2\}\). The value \(p\) is impossible because \(p<q\).

If \(n_q=1\), the Sylow \(q\)-subgroup is a proper nontrivial normal subgroup, so \(G\) is not simple.

It remains to consider \(n_q=p^2\). Then
\[
p^2\equiv1\pmod q,
\]
so \(q\mid(p-1)(p+1)\). Since \(q>p\), we have \(q\nmid p-1\), hence \(q\mid p+1\). Thus \(q=p+1\), forcing \((p,q)=(2,3)\). Hence \(|G|=36\) and \(n_3=4\).

Let \(G\) act by conjugation on its four Sylow \(3\)-subgroups. This gives a homomorphism
\[
\varphi:G\to S_4.
\]
The action is nontrivial because it is transitive on a set of size \(4\), so \(\ker\varphi\ne G\). It is also not faithful, because \(|G|=36>|S_4|=24\), so \(\ker\varphi\ne1\). Therefore \(\ker\varphi\) is a proper nontrivial normal subgroup of \(G\).

Thus no group of order \(p^2q^2\) with \(p<q\) is simple.
:::
