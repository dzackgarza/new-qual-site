---
title: Littlewood's three principles
order: 20
problems:
  topics:
  - Measure Theory
  - Convergence of Functions
---

# Littlewood's three principles

Three approximation patterns and their governing theorems:

| Principle | Theorem |
| --- | --- |
| Every measurable set is nearly a finite union of intervals | regularity of Lebesgue measure |
| Every measurable function is nearly continuous | Lusin |
| Every a.e. convergent sequence is nearly uniformly convergent | Egorov |

"Nearly" means outside a set of measure less than $\eps$, and in each case the exceptional set can be taken to be open or closed as convenient.

::: {.remark title="Transfer pattern"}
Each converts a measure-theoretic hypothesis into a hypothesis from undergraduate analysis, where the tools are stronger.
That is the standard use: to prove something about a measurable function, prove it for continuous functions and transfer with Lusin; to prove something about an a.e. convergent sequence, prove it for uniform convergence and transfer with Egorov.

Egorov needs finite measure, and $f_n = \chi_{[n,n+1]}$ on $\RR$ shows why.
Lusin needs the function finite a.e., which is the same hypothesis in disguise.
:::

The statements and proofs are on [[real-analysis/integration/the-convergence-theorems|The convergence theorems]].
