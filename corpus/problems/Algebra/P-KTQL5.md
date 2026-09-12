---
schema: qual/card@1
id: P-KTQL5
kind: problem
title: Centre of $S_n$
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
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
What is the center $Z(S_n)$ of the symmetric group $S_n$? Prove it.
:::

::: solution
For $n=1$, $S_1$ is trivial, so $Z(S_1)=S_1$. For $n=2$, $S_2$ is abelian, so $Z(S_2)=S_2$.

Now let $n\ge3$ and suppose $\sigma\in Z(S_n)$ is nontrivial. Choose $a$ with $\sigma(a)=b\ne a$, and choose $c$ distinct from $a,b$. Let $\tau=(bc)$. Then $\tau(a)=a$, so
\[
(\sigma\tau)(a)=\sigma(a)=b,
\]
whereas
\[
(\tau\sigma)(a)=\tau(b)=c.
\]
Thus $\sigma\tau\ne\tau\sigma$, contradicting $\sigma\in Z(S_n)$.

Therefore
\[
Z(S_n)=
\begin{cases}
S_n,&n=1,2,\\
\{1\},&n\ge3.
\end{cases}
\]
:::
