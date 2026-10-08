---
schema: qual/card@1
id: P-C2FE5
kind: problem
title: Short five lemma
classification:
  areas:
  - algebra
  topics:
  - Exact Sequences
  - Homological Algebra
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
Let $R$ be a ring with the following commutative diagram of $R$-modules, where each row represents a short exact sequence of $R$-modules:

\begin{tikzcd}
0 \ar[r] & A \ar[d, "\alpha"] \ar[r, "f"] & B \ar[d, "\beta"] \ar[r, "g"] & C \ar[r] \ar[d, "\gamma"] & 0 \\
0 \ar[r] & A' \ar[r, "f'"] & B'\ar[r, "g'"] & C' \ar[r] & 0 
\end{tikzcd}

Prove that if $\alpha$ and $\gamma$ are **isomorphisms**, then $\beta$ is an **isomorphism** (The Short Five Lemma).
:::

::: {.solution}
<1>1. The map $\beta:B\to B'$ is injective.

::: {.proof}
Let $b\in B$ satisfy $\beta(b)=0$. Commutativity gives $\gamma(g(b))=g'(\beta(b))=0$. Since $\gamma$ is injective, $g(b)=0$, hence exactness yields $b=f(a)$ for some $a\in A$. Then $f'(\alpha(a))=\beta(f(a))=0$. Injectivity of $f'$ and $\alpha$ implies $a=0$, so $b=0$.
:::

<1>2. The map $\beta$ is surjective.

::: {.proof}
Let $b'\in B'$. Since $\gamma$ is surjective, choose $c\in C$ with $\gamma(c)=g'(b')$. Since $g$ is surjective, choose $b\in B$ with $g(b)=c$. Then $g'(b'-\beta(b))=g'(b')-\gamma(g(b))=0$. Exactness gives an $a'\in A'$ with $f'(a')=b'-\beta(b)$. Because $\alpha$ is surjective, choose $a\in A$ with $\alpha(a)=a'$. Commutativity then yields $b'-\beta(b)=f'(\alpha(a))=\beta(f(a))$, hence $b'=\beta(b+f(a))$.
:::

<1>3. The map $\beta$ is an isomorphism.

::: {.proof}
Steps <1>1 and <1>2 show that $\beta$ is bijective. Its inverse is $R$-linear because $\beta$ is linear, so it is an isomorphism of modules.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the short five lemma.
:::
:::
