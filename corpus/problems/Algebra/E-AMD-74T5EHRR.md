---
schema: qual/card@1
id: E-AMD-74T5EHRR
kind: problem
title: The center of $S_n$ is trivial for $n\geq 3$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Permutations
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
Show that $Z(S_n) = 1$ for $n\geq 3$
:::

::: {.solution}
Let \(\sigma\in S_n\) be nonidentity. Choose \(i\) with \(\sigma(i)=j\ne i\). Since \(n\ge3\), choose \(k\notin\{i,j\}\), and let \(\tau=(j\ k)\).

Then \(\tau(i)=i\), so
\[
(\sigma\tau)(i)=\sigma(i)=j,
\]
while
\[
(\tau\sigma)(i)=\tau(j)=k.
\]
Thus \(\sigma\tau\ne\tau\sigma\), so \(\sigma\notin Z(S_n)\). Therefore the identity is the only central element:
\[
\boxed{Z(S_n)=1\qquad(n\ge3).}
\]
:::
