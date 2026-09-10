---
schema: qual/card@1
id: E-AMD-3LUW3P7R
kind: problem
title: $\Inn(G)$ is normal in $\Aut(G)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Normal Subgroups
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
Show that $\Inn(G) \normal \Aut(G)$.
:::

::: {.solution}
For \(g\in G\), write \(c_g(x)=gxg^{-1}\). Then \(\Inn(G)=\{c_g:g\in G\}\).

Let \(\phi\in\Aut(G)\). For every \(g,x\in G\),
\[
(\phi c_g\phi^{-1})(x)
=\phi\bigl(g\phi^{-1}(x)g^{-1}\bigr)
=\phi(g)x\phi(g)^{-1}
=c_{\phi(g)}(x).
\]
Hence
\[
\phi c_g\phi^{-1}=c_{\phi(g)}\in\Inn(G).
\]
Therefore \(\Inn(G)\trianglelefteq\Aut(G)\).
:::
