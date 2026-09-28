---
schema: qual/card@1
id: P-ALGREV1-02
kind: problem
title: Inner automorphisms form a normal subgroup
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Review1.md, open-ended question 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Conjugated an arbitrary inner automorphism by an arbitrary automorphism and obtained c_{phi(g)}."
---

::: {.problem}
Prove or disprove that $\operatorname{Inn}(G)\trianglelefteq\operatorname{Aut}(G)$.
:::

::: {.solution}
The assertion is true.

<1>1. Conjugating an inner automorphism by any automorphism gives another inner automorphism.
::: {.proof}
For $g\in G$, let
$$
c_g(x)=gxg^{-1}
$$
be the corresponding inner automorphism. Let
$\varphi\in\operatorname{Aut}(G)$. For every $x\in G$,
$$
\begin{aligned}
(\varphi c_g\varphi^{-1})(x)
&=\varphi\bigl(g\varphi^{-1}(x)g^{-1}\bigr)\\
&=\varphi(g)x\varphi(g)^{-1}\\
&=c_{\varphi(g)}(x).
\end{aligned}
$$
Hence
$$
\varphi c_g\varphi^{-1}=c_{\varphi(g)}\in\operatorname{Inn}(G).
$$
:::

<1>2. Therefore $\operatorname{Inn}(G)$ is normal in $\operatorname{Aut}(G)$.
::: {.proof}
Step <1>1 shows that
$$
\varphi\operatorname{Inn}(G)\varphi^{-1}
\subseteq\operatorname{Inn}(G)
$$
for every $\varphi\in\operatorname{Aut}(G)$. Applying the same argument to
$\varphi^{-1}$ gives the reverse inclusion. Thus
$$
\boxed{\operatorname{Inn}(G)\trianglelefteq\operatorname{Aut}(G).}
$$
:::
:::
