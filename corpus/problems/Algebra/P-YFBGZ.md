---
schema: qual/card@1
id: P-YFBGZ
kind: problem
title: Radical ideals in $\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Nilpotence
  - Prime Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Classify all **radical ideals** in the ring of integers $\mathbb{Z}$.
:::

::: solution
Every ideal of $\mathbb Z$ is $(n)$ for a unique $n\ge0$.

The zero ideal is radical because $\mathbb Z$ is reduced. Now let
\[
n=p_1^{a_1}\cdots p_r^{a_r}
\]
with distinct primes $p_i$. Put
\[
\operatorname{rad}(n)=p_1\cdots p_r.
\]
Then
\[
\sqrt{(n)}=(\operatorname{rad}(n)).
\]
Indeed, if $x^m\in(n)$, then every $p_i$ divides $x$, so $\operatorname{rad}(n)\mid x$. Conversely, if $\operatorname{rad}(n)\mid x$, then for
\[
N\ge\max_i a_i
\]
we have $n\mid x^N$.

Thus $(n)$ is radical exactly when
\[
n=\operatorname{rad}(n),
\]
i.e. when $n$ is squarefree. Including $n=1$ and $n=0$, the radical ideals are precisely
\[
\boxed{(0)\text{ and }(p_1\cdots p_r)\text{ with the }p_i\text{ distinct}}.
\]
:::
