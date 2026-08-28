---
schema: qual/card@1
id: FE-2UZDB
kind: example
title: Example of a sequence of differentiable functions $f_n \to f$ uniformly with $f_n' \to g$ pointwise for some $g$, but $g' \neq \lim f_n'$.
prompts:
- Give a sequence $f_n \to f$ uniformly with $f_n' \to g$ pointwise but $g' \neq \lim f_n'$.
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Differentiation
  - Counterexamples
relations: []
review: draft
---

::: {.example}
- $f_n(x)= {x \over 1 + nx^2} \to 0$ uniformly

  - Since $\norm{f_n}_\infty = 1/2\sqrt{n} \to 0.$

- $$f_n'(x) = {1-nx^2 \over (1+nx^2)^2} \to \chi_{\theset{0}} \not\equiv 0.$$
:::
