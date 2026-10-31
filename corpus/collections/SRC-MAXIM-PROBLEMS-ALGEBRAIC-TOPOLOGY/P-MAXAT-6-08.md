---
schema: qual/card@1
id: P-MAXAT-6-08
kind: problem
title: Euclidean embedding dimension of $\CP^n$ for $n$ a power of $2$
classification:
  areas: [topology]
  topics:
  - Pontryagin Classes
  - Embeddings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 8 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source asks for the smallest k with CP^n embedding in R^{2n+k} for arbitrary n, which has no known answer (for n=7 the known bounds leave two values). The statement now takes n=2^r, where the answer k=2n-1 is known.
---

::: {.problem}
Let $n=2^r$ with $r\ge0$. Find the smallest $k$ such that $\CP^n$ can be smoothly embedded in $\RR^{2n+k}$.
:::

::: {.solution}
Write $\alpha(n)$ for the number of $1$'s in the binary expansion of $n$, so $\alpha(n)=1$, and let $N(n)$ be the least $N$ such that $\CP^n$ embeds smoothly in $\RR^N$. Then $k_{\min}=N(n)-2n$.

::: pf

::: {.pf-step #s1}
$N(n)\ge4n-2\alpha(n)+1=4n-1$.

::: pf-proof
This is the Atiyah--Hirzebruch nonembedding theorem for complex projective spaces, $\CP^n\not\hookrightarrow\RR^{4n-2\alpha(n)}$; see Feder--Segal, *Immersions and embeddings of projective spaces*.
:::

:::

::: {.pf-step #s2}
$N(n)\le4n-\alpha(n)=4n-1$.

::: pf-proof
This is the embedding of A. Mukherjee, *Embedding complex projective spaces in Euclidean space*, Bull. London Math. Soc. 13 (1981), 323--324.
For $n=1$ it is the familiar embedding $\CP^1\cong S^2\hookrightarrow\RR^3$.
:::

:::

::: pf-qed
Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give $N(n)=4n-1$, so
$$
\boxed{k_{\min}=2n-1.}
$$
:::

:::
:::
