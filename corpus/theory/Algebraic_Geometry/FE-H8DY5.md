---
schema: qual/card@1
id: FE-H8DY5
kind: example
title: The line with doubled origin, and dropping each hypothesis
classification:
  areas:
  - algebraic-geometry
  topics:
  - Separated Morphisms
  - Reduced Schemes
  - Counterexamples
relations:
- kind: uses
  target: PR-QX0VL
review: draft
prompts:
- Give an example of a non-separated morphism.
- Give two morphisms agreeing on a dense open that are not equal.
---

::: {.example title="Not separated"}
Glue two copies of $\AA^1_k$ along $\AA^1 \sm \ts{0}$ by the identity.
The result $X$ has two origins, and $X \to \Spec k$ is not separated: the two inclusions $\AA^1 \to X$ agree on the dense open $\AA^1 \sm \ts{0}$ and differ at $0$, so the agreement locus is not closed.

By the proposition this *is* the failure of separatedness, not merely an illustration of it.
:::

::: {.example title="Separated but not reduced"}
Take $Z = \Spec k[\varepsilon]/(\varepsilon^2)$ and $X = \AA^1 = \Spec k[x]$, with $g$ and $h$ given by $x \mapsto 0$ and $x \mapsto \varepsilon$.
Both are morphisms to a separated $X$, and they agree on the unique point of $Z$ — indeed on every reduced subscheme of $Z$ — but $g \neq h$.
The dense open here is not proper, and it need not be: the point is that on a nonreduced base, agreeing topologically is not agreeing.
:::

::: {.remark}
The two examples separate the two hypotheses, which is what the follow-up asks for.
The doubled line is also the standard example of a scheme that is not a variety in the classical sense while being perfectly good as a scheme, and it is where "why is separatedness in the definition of a variety" gets its answer.
:::
